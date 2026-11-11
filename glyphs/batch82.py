# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 82: the publisher's own apps. Flow keeps its yellow tile and navy mark."""
from lm import (
    AMBER_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_LIGHT, BRAND_YELLOW, circle,
    CYAN, DEEP_ORANGE, GREY, HOLE, INDIGO, INK, line, NAVY, ORANGE, poly, pt, RED, rrect,
    stroke, TEAL,
)
from glyphs.kit import registry

ICONS, SMALL, reg, _ = registry()


@reg("uk.lightmorph.Flow", BRAND_YELLOW)
def flow():
    mouse = rrect(25.5, 17.5, 13, 23, 6.5, "none", f' stroke="{NAVY}" stroke-width="4.4"')
    wheel = line(32, 23.5, 32, 28, NAVY, 4.4)
    left = stroke("M21 29H12M16 25L12 29L16 33", NAVY, 4.4)
    right = stroke("M43 29H52M48 25L52 29L48 33", NAVY, 4.4)
    return mouse + wheel + left + right


@reg("trindle", BRAND_YELLOW)
def trindle():
    ring = f'<circle cx="32" cy="30" r="16" fill="none" stroke="{NAVY}" stroke-width="3.6"/>'
    dots = "".join(circle(*pt(32, 30, 10, 45 * k - 90), 2, NAVY) for k in range(8))
    return ring + dots


@reg("talk", NAVY)
def talk():
    return "".join(line(x, 30 - h, x, 30 + h, BRAND_YELLOW, 4.4)
                   for x, h in [(18, 5.5), (25, 10), (32, 14), (39, 10), (46, 5.5)])


@reg("trindle-deb", BLUE_GREY)
def trindle_deb():
    box = poly([(17, 22), (32, 16), (47, 22), (47, 40), (32, 46), (17, 40)], INK, 2.5)
    seam = stroke("M17 22L32 28L47 22M32 28V46", HOLE, 2.4)
    arrow = line(32, 8.5, 32, 20, CYAN, 4) + stroke("M27 15.5L32 20.5L37 15.5", CYAN, 4)
    return box + seam + arrow


@reg("trindle-store", BLUE_GREY_DEEP)
def trindle_store():
    tiles = (rrect(15, 13, 15, 15, 4, BLUE_LIGHT) + rrect(34, 13, 15, 15, 4, ORANGE) +
             rrect(15, 32, 15, 15, 4, RED))
    arrow = line(41.5, 32, 41.5, 45, GREY, 4.4) + stroke("M36 40L41.5 45.5L47 40", GREY, 4.4)
    return tiles + arrow


@reg("trindle-activity", BLUE_GREY_DARK)
def trindle_activity():
    return stroke("M13 30H20L24 20L30 41L35 17L40 36L43 30H51", AMBER_DEEP, 4.4)


@reg("trindle-app-library", INDIGO)
def app_library():
    return "".join(rrect(16 + 11.5 * i, 14 + 11.5 * j, 9, 9, 2.5, INK) for i in range(3) for j in range(3))


@reg("trindle-launcher", TEAL)
def launcher():
    bar = rrect(10, 21, 44, 18, 9, "none", ' stroke="INK" stroke-width="3.6"')
    lens = circle(22, 29, 4.5, "none", ' stroke="INK" stroke-width="3"') + line(25.5, 32.5, 28.5, 35.5, INK, 3)
    text = line(34, 30, 46, 30, INK, 3)
    return bar + lens + text


@reg("trindle-first-setup", DEEP_ORANGE)
def first_setup():
    board = rrect(17, 13, 30, 36, 5, INK)
    clip = rrect(25, 9.5, 14, 7, 3, INK) + rrect(28, 11.5, 8, 3, 1.5, HOLE)
    ticks = "".join(circle(25.5, y + .5, 2, HOLE) + line(34, y + 0.5, 42, y + 0.5, HOLE, 2.6)
                    for y in (24, 35))
    return board + clip + ticks
