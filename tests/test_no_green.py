# SPDX-License-Identifier: GPL-3.0-or-later
"""Fails if any built icon uses a green fill or stroke (hue 75 to 165 degrees)."""
import colorsys
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from svgs import own_svgs  # noqa: E402
HUE_MIN, HUE_MAX = 75, 165
MIN_SATURATION = 0.12


def is_green(hex6):
    r, g, b = (int(hex6[i:i + 2], 16) / 255 for i in (0, 2, 4))
    h, _, s = colorsys.rgb_to_hls(r, g, b)
    return HUE_MIN <= h * 360 <= HUE_MAX and s > MIN_SATURATION


def main():
    seen, bad, files = {}, [], 0
    for path in own_svgs("Trindle-Circle"):
        files += 1
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for colour in set(re.findall(r'(?:fill|stroke)="#([0-9A-Fa-f]{6})"', text)):
            if colour not in seen:
                seen[colour] = is_green(colour)
            if seen[colour]:
                bad.append((os.path.relpath(path, ROOT), "#" + colour))
    assert files, "no built SVGs found: run build.py first"
    assert not bad, f"{len(bad)} green colours, first: {bad[:5]}"
    print(f"ok: {files} SVGs, {len(seen)} colours, none green (hue {HUE_MIN}-{HUE_MAX}, saturation > {MIN_SATURATION})")


if __name__ == "__main__":
    main()
