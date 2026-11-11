# SPDX-License-Identifier: GPL-3.0-or-later
"""Render a batch for checking: each Papirus reference beside the new icon.

    venv/bin/python tools/preview.py batch07          -> previews/work/batch07.png
    venv/bin/python tools/preview.py batch07 small    -> 16/24px versions, enlarged

Left of each pair is Papirus (reference only), right is ours.
"""
import importlib, io, os, sys
import cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from lm import icon, small_icon  # noqa: E402
from build import SRC  # noqa: E402


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    batch = sys.argv[1]
    small = len(sys.argv) > 2 and sys.argv[2] == "small"
    mod = importlib.import_module(f"glyphs.{batch}")
    names = sorted(mod.ICONS)
    sz, cols, pad = 96, 8, 8
    cellw = sz * 2 + pad * 3
    rows = (len(names) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cellw, rows * (sz + pad * 2)), (27, 29, 41))
    for i, n in enumerate(names):
        fn, tile = mod.ICONS[n]
        x, y = (i % cols) * cellw + pad, (i // cols) * (sz + pad * 2) + pad
        src = os.path.join(SRC, n + ".svg")
        if os.path.exists(src):
            ref = cairosvg.svg2png(url=src, output_width=sz, output_height=sz)
        elif os.path.exists(os.path.join(ROOT, "refs", n + ".png")):
            buf = io.BytesIO()
            Image.open(os.path.join(ROOT, "refs", n + ".png")).convert("RGBA").resize((sz, sz)).save(buf, "PNG")
            ref = buf.getvalue()
        else:
            buf = io.BytesIO()
            Image.new("RGBA", (sz, sz)).save(buf, "PNG")
            ref = buf.getvalue()
        if small:
            sfn = getattr(mod, "SMALL", {}).get(n, fn)
            png = cairosvg.svg2png(bytestring=small_icon(sfn(), tile, 16).encode(), output_width=16, output_height=16)
            ours = Image.open(io.BytesIO(png)).convert("RGBA").resize((sz, sz), Image.NEAREST)
        else:
            png = cairosvg.svg2png(bytestring=icon(fn(), tile).encode(), output_width=sz, output_height=sz)
            ours = Image.open(io.BytesIO(png)).convert("RGBA")
        r = Image.open(io.BytesIO(ref)).convert("RGBA")
        sheet.paste(r, (x, y), r)
        sheet.paste(ours, (x + sz + pad, y), ours)
    os.makedirs(os.path.join(ROOT, "previews", "work"), exist_ok=True)
    out = os.path.join(ROOT, "previews", "work", f"{batch}{'-small' if small else ''}.png")
    sheet.save(out)
    print(out, len(names), "icons, in name order:", " ".join(names))


if __name__ == "__main__":
    main()
