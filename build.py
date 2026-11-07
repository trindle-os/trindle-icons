# SPDX-License-Identifier: GPL-3.0-or-later
"""Build the Trindle icon theme from the glyph batches.

Writes <size>/apps/<name>.svg for every drawn icon: the full icon (with
its lifted logo) at 32, 48, 64 and 128, and the simplified, effect-free
redraw at 16, 22 and 24. Every Papirus symlink whose target resolves to
a drawn icon is recreated, so alias names match the originals exactly.
"""
import argparse, importlib, json, os, pkgutil, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from lm import icon, small_icon

PAPIRUS = os.environ.get("PAPIRUS_DIR") or os.path.join(ROOT, "Papirus")
SRC = os.path.join(PAPIRUS, "64x64", "apps")
EXTRA = os.path.join(ROOT, "extra_aliases.txt")
FIT_FILE = os.path.join(ROOT, "circle_fit.json")
FULL = [32, 48, 64, 128]
SMALL = [16, 22, 24]
THEME = os.path.join(ROOT, "Trindle-Circle")
NAME = "Trindle Circle"

FIT = {}
if os.path.exists(FIT_FILE):
    with open(FIT_FILE, encoding="utf-8") as fh:
        FIT = json.load(fh)

def load():
    icons, small = {}, {}
    for m in sorted(pkgutil.iter_modules([os.path.join(ROOT, "glyphs")]), key=lambda m: m.name):
        mod = importlib.import_module(f"glyphs.{m.name}")
        for name in mod.ICONS:
            if name in icons:
                raise ValueError(f"icon name {name!r} is defined in more than one batch (again in {m.name})")
        icons.update(mod.ICONS)
        small.update(getattr(mod, "SMALL", {}))
    return icons, small

def check_papirus():
    """A plain message if Papirus is missing, else None."""
    if not os.path.isdir(SRC):
        return f"Papirus apps folder not found at {SRC}. See the README for how to fetch it, or set PAPIRUS_DIR to the Papirus theme root (the folder with index.theme and 64x64/apps)."
    if not os.path.isfile(os.path.join(PAPIRUS, "index.theme")):
        return f"Installed Papirus theme not found at {PAPIRUS}. See the README, or set PAPIRUS_DIR to the Papirus theme root (the folder with index.theme and 64x64/apps)."
    return None

def link_aliases(out, icons):
    links = 0
    for entry in os.scandir(SRC):
        if not entry.is_symlink() or os.path.splitext(entry.name)[0] in icons:
            continue
        target = os.readlink(entry.path)
        final = os.path.splitext(os.path.basename(os.path.realpath(entry.path)))[0]
        if "/" in target or final not in icons:
            continue
        dst = os.path.join(out, entry.name)
        if os.path.islink(dst):
            os.remove(dst)
        os.symlink(target, dst)
        links += 1
    with open(EXTRA, encoding="utf-8") as fh:
        for no, line in enumerate(fh, 1):
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"extra_aliases.txt line {no}: expected 'new old', got {line.strip()!r}")
            new, old = parts
            dst = os.path.join(out, new + ".svg")
            if os.path.exists(os.path.join(out, old + ".svg")) and not os.path.lexists(dst):
                os.symlink(old + ".svg", dst)
                links += 1
    return links

CONTEXT_NAMES = {"apps": "Applications", "mimetypes": "MimeTypes"}

def sym_contexts():
    from symbolic.set1 import SYM
    return {c: CONTEXT_NAMES.get(c, c.capitalize()) for c in sorted({c for c, _ in SYM.values()})}

def write_symbolic():
    """The small one-colour icons (symbolic/<context>/<name>-symbolic.svg),
    the same as every other icon: GTK repaints them in the text colour."""
    from symbolic import kit
    from symbolic.set1 import SYM
    for name, (context, fn) in SYM.items():
        out = os.path.join(THEME, "symbolic", context)
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, name + "-symbolic.svg"), "w", encoding="utf-8") as fh:
            fh.write(kit.outlined(kit.svg(fn()), name))
    return len(SYM)

def papirus_sections():
    """Papirus's full-colour folders other than apps (places, mimetypes,
    devices, actions, status...), linked into this theme as papirus/<dir>.

    A file or folder asks for a list of names such as ['inode-directory',
    'folder', 'inode-directory-symbolic', 'folder-symbolic'], and GTK tries
    every name in this theme before it looks in Papirus. Without these links
    our one-colour folder-symbolic would win over Papirus's coloured folder."""
    import configparser
    cp = configparser.ConfigParser(strict=False, interpolation=None)
    cp.optionxform = str
    cp.read(os.path.join(PAPIRUS, "index.theme"), encoding="utf-8")
    out = []
    for d in cp["Icon Theme"]["Directories"].split(","):
        d = d.strip()
        if not d or "symbolic" in d or d.split("/")[-1] in ("apps", "categories"):
            continue
        if not os.path.isdir(os.path.join(PAPIRUS, d)):
            continue
        link = os.path.join(THEME, "papirus", d)
        os.makedirs(os.path.dirname(link), exist_ok=True)
        if os.path.lexists(link):
            os.remove(link)

        os.symlink(os.path.join(*[".."] * (d.count("/") + 2), "Papirus", d), link)
        out.append(("papirus/" + d, dict(cp[d])))
    return out

def write_hidpi_and_index():
    """<size>@2x folders are links to <size> (identical contents, as Papirus
    does), and index.theme lists every folder so the theme is selectable."""
    sections = []
    for size in sorted(FULL + SMALL):
        base = f"{size}x{size}"
        dbl = os.path.join(THEME, base + "@2x")
        if not os.path.lexists(dbl):
            os.symlink(base, dbl)
        sections.append((f"{base}/apps", size, 1))
        sections.append((f"{base}@2x/apps", size, 2))
    contexts = sym_contexts()
    symbolic = [f"symbolic/{c}" for c in contexts]
    borrowed = papirus_sections()
    with open(os.path.join(THEME, "index.theme"), "w", encoding="utf-8") as fh:
        fh.write(f"[Icon Theme]\nName={NAME}\n"
                 "Comment=Warm flat app icons on coloured circles\n"
                 "Inherits=Papirus,hicolor\n"
                 "Example=firefox\n"
                 "DisplayDepth=32\n"
                 f"Directories={','.join([d for d, _, _ in sections] + symbolic + [d for d, _ in borrowed])}\n")
        for d, size, scale in sections:
            fh.write(f"\n[{d}]\nContext=Applications\nSize={size}\n"
                     + (f"Scale={scale}\n" if scale > 1 else "") + "Type=Fixed\n")
        for d in symbolic:
            fh.write(f"\n[{d}]\nContext={contexts[d.split('/')[1]]}\nSize=16\n"
                     "MinSize=8\nMaxSize=512\nType=Scalable\n")
        for d, keys in borrowed:
            fh.write(f"\n[{d}]\n" + "".join(f"{k}={v}\n" for k, v in keys.items()))

def clean():
    """Drop what an earlier build left, so removed icons do not stay on disk."""
    for size in FULL + SMALL:
        base = os.path.join(THEME, f"{size}x{size}")
        shutil.rmtree(base, ignore_errors=True)
        if os.path.islink(base + "@2x"):
            os.remove(base + "@2x")
    for sub in ("symbolic", "papirus"):
        shutil.rmtree(os.path.join(THEME, sub), ignore_errors=True)

def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the Trindle Circle icon theme.")
    ap.parse_args(argv)
    problem = check_papirus()
    if problem:
        print(problem, file=sys.stderr)
        return 1
    icons, small = load()
    clean()
    links = 0
    for size in FULL + SMALL:
        out = os.path.join(THEME, f"{size}x{size}", "apps")
        os.makedirs(out, exist_ok=True)

    for name, (fn, tile) in icons.items():
        fit = FIT.get(name, 1)
        full = icon(fn(), tile, fit)
        tiny = small_icon(small.get(name, fn)(), tile, 24, fit)
        for size in FULL + SMALL:
            svg = full if size in FULL else tiny.replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)
            with open(os.path.join(THEME, f"{size}x{size}", "apps", name + ".svg"), "w", encoding="utf-8") as fh:
                fh.write(svg)
    for size in FULL + SMALL:
        links = link_aliases(os.path.join(THEME, f"{size}x{size}", "apps"), icons)
    dangling = [e.path for s in FULL + SMALL
                for e in os.scandir(os.path.join(THEME, f"{s}x{s}", "apps"))
                if e.is_symlink() and not os.path.exists(e.path)]
    write_hidpi_and_index()
    nsym = write_symbolic()
    print(f"{len(icons)} icons x {len(FULL + SMALL)} sizes, {links} alias links each, "
          f"{len(small)} small redraws, {nsym} symbolic, {len(dangling)} dangling")
    return 1 if dangling else 0

if __name__ == "__main__":
    sys.exit(main())
