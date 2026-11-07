# SPDX-License-Identifier: GPL-3.0-or-later
"""Preview the symbolic icons: each at 16px (enlarged to show pixels) and at
48px, light on dark and dark on light.  venv/bin/python tools/symsheet.py out.png"""
import io, os, sys
import cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from symbolic.kit import C, svg as wrap
from symbolic.set1 import SYM

names = sorted(SYM)
cols, cw, ch = 12, 150, 64
sheet = Image.new("RGB", (cols * cw, ((len(names) + cols - 1) // cols) * ch), (27, 29, 41))
for i, name in enumerate(names):
    svg = SYM[name][1]()
    x, y = (i % cols) * cw, (i // cols) * ch
    for k, (fg, bg) in enumerate([("#EDEDF0", (27, 29, 41)), ("#1B1D29", (236, 236, 240))]):
        doc = wrap(svg).replace(C, fg)
        tile = Image.new("RGB", (72, 60), bg)
        big = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=doc.encode(), output_width=48, output_height=48))).convert("RGBA")
        tiny = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=doc.encode(), output_width=16, output_height=16))).convert("RGBA")
        tile.paste(big, (2, 6), big)
        tile.paste(tiny, (54, 22), tiny)
        sheet.paste(tile, (x + k * 74, y + 2))
sheet.save(sys.argv[1])
