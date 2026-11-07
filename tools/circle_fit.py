# SPDX-License-Identifier: GPL-3.0-or-later
"""Find round-tile icons whose logo spills past the circle and record how
much to shrink each one, in circle_fit.json. Run after adding glyphs:

    venv/bin/python tools/circle_fit.py && venv/bin/python build.py
"""
import io, json, os, sys
import cairosvg
from PIL import Image, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import build
import lm

OUTSIDE = Image.new("L", (128, 128))
OUTSIDE.putdata([255 if ((x + .5 - 64) ** 2 + (y + .5 - 64) ** 2) ** .5 > 52.5 else 0
                 for y in range(128) for x in range(128)])

def spill(svg):
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=128, output_height=128)
    alpha = Image.open(io.BytesIO(png)).convert("RGBA").getchannel("A")
    solid = alpha.point(lambda a: 255 if a > 60 else 0)
    return ImageChops.darker(solid, OUTSIDE).histogram()[255]

def main():
    fit = {}
    for name, (fn, tile) in build.load()[0].items():
        k = 1.0
        while spill(lm.icon(fn(), tile, k)) > 6 and k > .7:
            k = round(k - .04, 2)
        if k < 1:
            fit[name] = k
    with open(build.FIT_FILE, "w", encoding="utf-8") as fh:
        json.dump(fit, fh, indent=1, sort_keys=True)
    print(len(fit), "icons shrunk to fit the circle")

if __name__ == "__main__":
    main()
