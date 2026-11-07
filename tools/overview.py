# SPDX-License-Identifier: GPL-3.0-or-later
"""Contact sheets of a whole theme, split into pages: previews/[circle-]all-NN.png

    venv/bin/python tools/overview.py [Trindle-Circle]
"""
import io, os, sys
import cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1].startswith("-")):
    sys.exit(__doc__)
THEME = sys.argv[1] if len(sys.argv) > 1 else "Trindle-Circle"
d = os.path.join(ROOT, THEME, "64x64", "apps")
TAG = "circle-"
names = sorted(e.name for e in os.scandir(d) if e.is_file(follow_symlinks=False))
os.makedirs(os.path.join(ROOT, "previews"), exist_ok=True)
sz, gap, cols, per = 48, 8, 40, 1000
for p in range(0, len(names), per):
    chunk = names[p:p + per]
    rows = (len(chunk) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (sz + gap) + gap, rows * (sz + gap) + gap), (27, 29, 41))
    for i, n in enumerate(chunk):
        png = cairosvg.svg2png(url=os.path.join(d, n), output_width=sz, output_height=sz)
        im = Image.open(io.BytesIO(png)).convert("RGBA")
        sheet.paste(im, (gap + (i % cols) * (sz + gap), gap + (i // cols) * (sz + gap)), im)
    out = os.path.join(ROOT, "previews", f"{TAG}all-{p // per + 1:02d}.png")
    sheet.save(out)
    print(out, chunk[0], "to", chunk[-1])
