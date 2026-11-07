# SPDX-License-Identifier: GPL-3.0-or-later
"""Contact sheet of named SVG icons from one folder.

    venv/bin/python tools/sheet.py <svg folder> <out.png> <size> <name> [<name> ...]

Names are file names without .svg. Set BG="r,g,b" to change the background.
"""
import cairosvg, sys, io, os
from PIL import Image

if len(sys.argv) < 5:
    sys.exit(__doc__)
d, out = sys.argv[1], sys.argv[2]
try:
    sz = int(sys.argv[3])
except ValueError:
    sys.exit(__doc__)
names = sys.argv[4:]
if any(os.sep in n or n.startswith(".") for n in names):
    sys.exit("names must be plain file names without folders")
try:
    bg = tuple(int(x) for x in os.environ.get("BG", "42,44,47").split(","))
    assert len(bg) == 3
except (ValueError, AssertionError):
    sys.exit('BG must look like "42,44,47"')
cols = 10
pad = 10
cell = sz + pad
sheet = Image.new("RGB", (cols * cell + pad, ((len(names) + cols - 1) // cols) * cell + pad), bg)
for i, n in enumerate(names):
    png = cairosvg.svg2png(url=os.path.join(d, n + ".svg"), output_width=sz, output_height=sz)
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    sheet.paste(im, (pad + (i % cols) * cell, pad + (i // cols) * cell), im)
sheet.save(out)
