# SPDX-License-Identifier: GPL-3.0-or-later
"""Build the Trindle icon theme from the glyph batches.

Writes <size>/apps/<name>.svg for every drawn icon: the full icon (with
its lifted logo) at 32, 48, 64 and 128, and the simplified, effect-free
redraw at 16, 22 and 24. Every Papirus symlink whose target resolves to
a drawn icon is recreated, so alias names match the originals exactly.
"""
import importlib, json, os, pkgutil, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
from lm import icon, small_icon  # noqa: E402

PAPIRUS = os.environ.get("PAPIRUS_DIR") or os.path.join(ROOT, "Papirus")
SRC = os.path.join(PAPIRUS, "64x64", "apps")
EXTRA = os.path.join(ROOT, "extra_aliases.txt")
FIT_FILE = os.path.join(ROOT, "circle_fit.json")
FULL = [32, 48, 64, 128]
SMALL = [16, 22, 24]
THEME = os.path.join(ROOT, "Trindle-Circle")
NAME = "Trindle Circle"


def load_fit():
    """Extra shrink for the few marks too wide for a round tile (tools/circle_fit.py)."""
    if not os.path.exists(FIT_FILE):
        return {}
    with open(FIT_FILE, encoding="utf-8") as fh:
        return json.load(fh)


def load():
    icons, small = {}, {}
    batches = sorted((m for m in pkgutil.iter_modules([os.path.join(ROOT, "glyphs")]) if m.name.startswith("batch")),
                     key=lambda m: m.name)
    for m in batches:
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


def alias_links(icons):
    """The alias links to write in every size folder, as (name, target):
    Papirus's own links to icons we drew, then extra_aliases.txt."""
    links = []
    names = set(icons)
    for entry in os.scandir(SRC):
        if not entry.is_symlink() or os.path.splitext(entry.name)[0] in icons:
            continue
        target = os.readlink(entry.path)
        final = os.path.splitext(os.path.basename(os.path.realpath(entry.path)))[0]
        if "/" in target or final not in icons:
            continue
        links.append((entry.name, target))
        names.add(os.path.splitext(entry.name)[0])
    with open(EXTRA, encoding="utf-8") as fh:
        for no, line in enumerate(fh, 1):
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"extra_aliases.txt line {no}: expected 'new old', got {line.strip()!r}")
            new, old = parts
            if old in names and new not in names:
                links.append((new + ".svg", old + ".svg"))
                names.add(new)
    return links


CONTEXT_NAMES = {"apps": "Applications", "mimetypes": "MimeTypes"}


def sym_contexts():
    from symbolic.set1 import SYM
    return {c: CONTEXT_NAMES.get(c, c.capitalize()) for c in sorted({c for c, _ in SYM.values()})}


def write_symbolic(theme):
    """The small one-colour icons (symbolic/<context>/<name>-symbolic.svg),
    the same as every other icon: GTK repaints them in the text colour."""
    from symbolic import kit
    from symbolic.set1 import SYM
    for name, (context, fn) in SYM.items():
        out = os.path.join(theme, "symbolic", context)
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, name + "-symbolic.svg"), "w", encoding="utf-8") as fh:
            fh.write(kit.outlined(kit.svg(fn()), name))
    return len(SYM)


def papirus_sections(theme):
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
        link = os.path.join(theme, "papirus", d)
        os.makedirs(os.path.dirname(link), exist_ok=True)
        os.symlink(os.path.join(*[".."] * (d.count("/") + 2), "Papirus", d), link)
        out.append(("papirus/" + d, dict(cp[d])))
    return out


def write_hidpi_and_index(theme):
    """<size>@2x folders are links to <size> (identical contents, as Papirus
    does), and index.theme lists every folder so the theme is selectable."""
    sections = []
    for size in sorted(FULL + SMALL):
        base = f"{size}x{size}"
        os.symlink(base, os.path.join(theme, base + "@2x"))
        sections.append((f"{base}/apps", size, 1))
        sections.append((f"{base}@2x/apps", size, 2))
    contexts = sym_contexts()
    symbolic = [f"symbolic/{c}" for c in contexts]
    borrowed = papirus_sections(theme)
    with open(os.path.join(theme, "index.theme"), "w", encoding="utf-8") as fh:
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


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv:
        print("usage: python build.py", file=sys.stderr)
        raise SystemExit(2)
    problem = check_papirus()
    if problem:
        print(problem, file=sys.stderr)
        return 1
    icons, small = load()
    fits = load_fit()
    stage = THEME + ".new"
    shutil.rmtree(stage, ignore_errors=True)
    sizes = FULL + SMALL
    outs = {size: os.path.join(stage, f"{size}x{size}", "apps") for size in sizes}
    for out in outs.values():
        os.makedirs(out)
    for name, (fn, tile) in icons.items():
        fit = fits.get(name, 1)
        full = icon(fn(), tile, fit)
        tiny = small_icon(small.get(name, fn)(), tile, 24, fit)
        for size in sizes:
            svg = full if size in FULL else tiny.replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)
            with open(os.path.join(outs[size], name + ".svg"), "w", encoding="utf-8") as fh:
                fh.write(svg)
    links = alias_links(icons)
    for out in outs.values():
        for name, target in links:
            os.symlink(target, os.path.join(out, name))
    dangling = [e.path for out in outs.values() for e in os.scandir(out)
                if e.is_symlink() and not os.path.exists(e.path)]
    write_hidpi_and_index(stage)
    nsym = write_symbolic(stage)
    print(f"{len(icons)} icons x {len(sizes)} sizes, {len(links)} alias links each, "
          f"{len(small)} small redraws, {nsym} symbolic, {len(dangling)} dangling")
    if dangling:
        return 1
    shutil.rmtree(THEME, ignore_errors=True)
    os.replace(stage, THEME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
