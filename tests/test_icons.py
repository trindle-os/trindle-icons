# SPDX-License-Identifier: GPL-3.0-or-later
"""Every drawing makes well-formed SVG, and lm.icon, lift and small_icon give the expected shape.
Run: venv/bin/python tests/test_icons.py"""
import os, sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import build  # noqa: E402
import lm  # noqa: E402

SVG = "{http://www.w3.org/2000/svg}svg"


def check_lm():
    glyph = '<circle cx="32" cy="30" r="10" fill="INK"/>'
    full = ET.fromstring(lm.icon(glyph, lm.RED_DEEP))
    assert full.tag == SVG and full.get("width") == "64" and full.get("viewBox") == "0 0 64 64"
    assert 'fill="INK"' not in lm.icon(glyph, lm.RED_DEEP), "INK was not replaced"
    assert lm.WHITE in lm.icon(glyph, lm.RED_DEEP) and lm.BLACK in lm.icon(glyph, lm.YELLOW_LIGHT)
    small = ET.fromstring(lm.small_icon(glyph, lm.RED_DEEP, 16))
    assert small.get("width") == "16" and small.get("height") == "16" and small.get("viewBox") == "0 0 64 64"
    lifted = lm.lift('<path d="M0 0" fill="#FFFFFF"/>')
    assert lifted.count("<g ") == 3 and lm.BLACK in lifted and "#FFFFFF" not in lifted
    ids = lm.lift('<clipPath id="a"/><path clip-path="url(#a)"/>')
    assert "a-s0" in ids and "a-s2" in ids, "lifted copies must not share ids"


def check_drawings():
    icons, small = build.load()
    assert len(icons) > 5000
    for name, (fn, tile) in icons.items():
        for label, svg in (("full", lm.icon(fn(), tile)), ("small", lm.small_icon(small.get(name, fn)(), tile, 24))):
            try:
                root = ET.fromstring(svg)
            except ET.ParseError as e:
                raise AssertionError(f"{name} ({label}) is not well-formed SVG: {e}")
            assert root.tag == SVG, f"{name} ({label}) is not an svg"
    return len(icons)


if __name__ == "__main__":
    check_lm()
    print("ok lm", check_drawings(), "drawings")
