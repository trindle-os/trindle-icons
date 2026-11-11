# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 107: Trindle Scan, the scanner app."""
from lm import DEEP_PURPLE, HOLE, INK, rrect, stroke
from glyphs.kit import fit, registry

ICONS, SMALL, reg, _ = registry()


@reg("org.trindle.Scan", DEEP_PURPLE)
def scan():
    out = stroke("M19 32V12H45V32", INK, 4.4)
    out += rrect(8, 32, 48, 22, 6, INK) + stroke("M17 43H47", HOLE, 4)
    return fit(out, 0.7, 32.0, 32.0)
