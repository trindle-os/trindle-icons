# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 108: ten icons Papirus draws with green or a tick, redrawn in
Trindle's own style so no green and no tick reaches the desktop."""
from lm import (
    BLUE, BLUE_DEEP, BLUE_GREY, circle, DEEP_PURPLE, HOLE, INDIGO, INK, line, ORANGE, path,
    PURPLE, rrect, stroke,
)
from glyphs.kit import registry, arc

ICONS, SMALL, reg, _ = registry()


def power(cx, cy, r):
    return stroke(arc(cx, cy, r, -60, 240), HOLE, 2.4) + line(cx, cy - r - 1, cx, cy - 1, HOLE, 2.4)


@reg("x-office-spreadsheet", BLUE_DEEP)
def spreadsheet():
    cells = "".join(line(14, y, 50, y, HOLE, 2) for y in (26, 38)) + line(30, 14, 30, 50, HOLE, 2)
    return rrect(14, 14, 36, 36, 4, INK) + cells


@reg("application-x-codeblocks-workspace", DEEP_PURPLE)
def codeblocks():
    left = stroke("M26 20L14 32L26 44", INK, 4)
    right = stroke("M38 20L50 32L38 44", INK, 4)
    return left + right + line(34, 17, 30, 47, INK, 3)


@reg("text-vnd.trolltech.linguist", INDIGO)
def linguist():
    bubble = path("M14 16H50V40H34L24 50V40H14Z", INK)
    return bubble + line(20, 24, 44, 24, HOLE, 2.4) + line(20, 31, 36, 31, HOLE, 2.4)


@reg("audio-card", ORANGE)
def audio_card():
    card = rrect(12, 18, 40, 28, 4, INK)
    return card + circle(26, 32, 7, HOLE) + circle(26, 32, 2.4, INK) + line(38, 26, 46, 26, HOLE, 2.4) + line(38, 32, 46, 32, HOLE, 2.4)


@reg("financial-categories", PURPLE)
def categories():
    pie = circle(30, 33, 17, INK)
    cut_ = path("M30 33L30 16A17 17 0 0 1 47 33Z", HOLE)
    return pie + cut_ + path("M33 12A17 17 0 0 1 50 29L33 29Z", INK)


@reg("smartphoneconnected", BLUE_DEEP)
def phone_connected():
    phone = rrect(18, 12, 20, 38, 4, INK) + rrect(21, 17, 14, 24, 1.5, HOLE)
    waves = stroke("M43 24A8 8 0 0 1 43 38", INK, 2.4) + stroke("M47 20A13 13 0 0 1 47 42", INK, 2.4)
    return phone + waves


@reg("blueman-trusted-emblem", BLUE)
def trusted():
    shield = path("M32 12L48 18V32C48 41 41 47 32 51C23 47 16 41 16 32V18Z", INK)
    return shield + circle(32, 29, 5, HOLE) + path("M26 40C27 35 37 35 38 40Z", HOLE)


@reg("osd-duplicate", BLUE_GREY)
def duplicate():
    back = rrect(12, 14, 28, 22, 3, INK, ' opacity=".6"')
    front = rrect(24, 28, 28, 22, 3, INK)
    return back + front + rrect(28, 32, 20, 14, 1.5, HOLE)


@reg("osd-shutd-laptop", BLUE_GREY)
def shutdown_laptop():
    screen = rrect(16, 14, 32, 22, 3, INK)
    base = rrect(10, 39, 44, 6, 3, INK)
    return screen + base + power(32, 25, 6)


@reg("osd-shutd-screen", BLUE_GREY)
def shutdown_screen():
    screen = rrect(12, 14, 40, 28, 3, INK)
    stand = rrect(28, 42, 8, 6, 1, INK) + rrect(22, 47, 20, 3, 1.5, INK)
    return screen + stand + power(32, 28, 7)
