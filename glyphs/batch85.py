# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 85: Trindle Folders' own actions, drawn from the matching small
one-colour icons so the two sizes always agree."""
from lm import BLUE_DEEP, BLUE_GREY, DEEP_PURPLE, g, INDIGO_LIGHT, TEAL
from symbolic.set1 import SYM
from glyphs.kit import registry

ICONS, SMALL, _, _ = registry()


TILES = {"install-font": DEEP_PURPLE, "checksum": INDIGO_LIGHT, "rotate-left": BLUE_DEEP,
         "rotate-right": BLUE_DEEP, "rotate-half": BLUE_DEEP, "resize": TEAL,
         "type-location": BLUE_GREY, "forget": BLUE_GREY}


def _from_symbolic(name):
    def glyph():
        body = SYM[name][1]().replace('"#bebebe"', '"INK"')
        return g('<g fill="none" stroke="INK" stroke-width="1.8" stroke-linecap="round" '
                 f'stroke-linejoin="round">{body}</g>', "translate(11 9) scale(2.625)")
    return glyph


for _k, _tile in TILES.items():
    ICONS[f"trindle-folders-{_k}"] = (_from_symbolic(f"trindle-folders-{_k}"), _tile)
