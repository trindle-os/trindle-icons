# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 107: Trindle Scan, the scanner app. This batch holds 1 icon. It is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import fit, H, I, registry

ICONS, SMALL, reg, _ = registry()

@reg("org.trindle.Scan", DEEP_PURPLE)
def i2101():
    out = stroke("M19 32V12H45V32", I, 4.4)
    out += rrect(8, 32, 48, 22, 6, I) + stroke("M17 43H47", H, 4)
    return fit(out, 0.7, 32.0, 32.0)
