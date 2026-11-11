# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 84: twenty plain marks for apps that ship no icon of their own.
Each is a shape that means nothing in particular, on its own colour, so a
desktop can hand a different one to each unknown app (trindle-generic-01..20)."""
from lm import (
    AMBER_DEEP, BLUE, BLUE_GREY, BLUE_LIGHT, BROWN, circle, CYAN, DEEP_ORANGE, DEEP_PURPLE, g,
    GREY_DEEP, HOLE, INDIGO, INK, LIGHT_BLUE, line, ORANGE_DEEP, path, PINK, PINK_DEEP, poly,
    pt, PURPLE, PURPLE_LIGHT, RED, RED_DEEP, rrect, stroke, TEAL, TEAL_DEEP,
)
from glyphs.kit import registry

ICONS, SMALL, reg, _ = registry()


def generic(n, tile):
    return reg(f"trindle-generic-{n:02d}", tile)


@generic(1, BLUE)
def cube():
    top = poly([(32, 11), (49, 20), (32, 29), (15, 20)], INK, 2)
    left = poly([(15, 23.5), (30.5, 32), (30.5, 50), (15, 41.5)], INK, 2)
    right = poly([(33.5, 32), (49, 23.5), (49, 41.5), (33.5, 50)], INK, 2)
    return top + f'<g opacity=".75">{left}</g>' + f'<g opacity=".55">{right}</g>'


@generic(2, PURPLE)
def spark():
    return path("M32 10C33.6 24 36 26.4 50 28C36 29.6 33.6 32 32 46C30.4 32 28 29.6 14 28C28 26.4 30.4 24 32 10Z", INK)


@generic(3, TEAL)
def hexagon():
    outer = poly([pt(32, 30, 19, 60 * k - 90) for k in range(6)], INK, 3)
    inner = poly([pt(32, 30, 8, 60 * k - 90) for k in range(6)], HOLE, 1.5)
    return outer + inner


@generic(4, INDIGO)
def layers():
    sheet = lambda y, o: f'<g opacity="{o}">' + poly([(32, y - 8), (50, y), (32, y + 8), (14, y)], INK, 2) + "</g>"
    return sheet(40, .55) + sheet(31, .75) + sheet(22, 1)


@generic(5, RED)
def rings():
    return (circle(25, 30, 11, "none", ' stroke="INK" stroke-width="4"')
            + circle(39, 30, 11, "none", ' stroke="INK" stroke-width="4"'))


@generic(6, DEEP_ORANGE)
def triangle():
    return poly([(32, 12), (51, 46), (13, 46)], INK, 4) + poly([(32, 28), (40, 41), (24, 41)], HOLE, 1.5)


@generic(7, AMBER_DEEP)
def _star():
    return poly([pt(32, 31, 19 if k % 2 == 0 else 8.5, 36 * k - 90) for k in range(10)], INK, 1.5)


@generic(8, DEEP_PURPLE)
def crescent():
    return path("M38 12A18 18 0 1 0 50 40A15 15 0 1 1 38 12Z", INK) + circle(44, 20, 2.5, INK)


@generic(9, BLUE_LIGHT)
def leaf():
    blade = path("M15 47C15 25 27 13 49 13C49 35 37 47 15 47Z", INK)
    vein = stroke("M20 42Q32 30 42 20", HOLE, 2.6)
    return blade + vein


@generic(10, PINK)
def dots():
    return circle(32, 18, 7, INK) + circle(21, 38, 7, INK) + circle(43, 38, 7, INK)


@generic(11, CYAN)
def waves():
    w = lambda y: stroke(f"M13 {y}Q18.5 {y - 6} 22.5 {y}T32 {y}T41.5 {y}T51 {y}", INK, 5)
    return w(23) + w(37)


@generic(12, BROWN)
def puzzle():
    return path("M15 21H25A5.5 5.5 0 1 1 36 21H46V31A5.5 5.5 0 1 1 46 42V48H15V38A5.5 5.5 0 1 0 15 27Z", INK)


@generic(13, BLUE_GREY)
def window():
    frame = rrect(12, 14, 40, 32, 5, INK)
    pane = rrect(15.5, 23, 33, 19.5, 2.5, HOLE)
    lights = "".join(circle(18.5 + 5 * k, 18.5, 1.7, HOLE) for k in range(3))
    return frame + pane + lights


@generic(14, ORANGE_DEEP)
def grid():
    d = lambda cx, cy: poly([(cx, cy - 8), (cx + 8, cy), (cx, cy + 8), (cx - 8, cy)], INK, 1.5)
    return d(32, 19) + d(21, 30) + d(43, 30) + d(32, 41)


@generic(15, RED_DEEP)
def flower():
    petals = "".join(circle(*pt(32, 30, 10, 72 * k - 90), 7.5, INK) for k in range(5))
    return petals + circle(32, 30, 5, HOLE) + circle(32, 30, 2.5, INK)


@generic(16, TEAL_DEEP)
def loop():
    return stroke("M32 30C27 22 15 21 15 30C15 39 27 38 32 30C37 22 49 21 49 30C49 39 37 38 32 30Z", INK, 4.4)


@generic(17, LIGHT_BLUE)
def orbit():
    ring = '<ellipse cx="32" cy="30" rx="20" ry="6.5" fill="none" stroke="INK" stroke-width="3"/>'
    front = (stroke("M12 30A20 6.5 0 0 0 52 30", HOLE, 6.5) + stroke("M12 30A20 6.5 0 0 0 52 30", INK, 3))
    return g(ring + circle(32, 30, 11, INK) + front, "rotate(-20 32 30)")


@generic(18, PINK_DEEP)
def drop():
    return path("M32 11C38 21 46 28 46 36A14 14 0 0 1 18 36C18 28 26 21 32 11Z", INK) + \
        stroke("M25 37A7 7 0 0 0 30 43", HOLE, 2.6)


@generic(19, PURPLE_LIGHT)
def clover():
    lobes = "".join(circle(*pt(32, 30, 8.5, 90 * k + 45), 9, INK) for k in range(4))
    return lobes + circle(32, 30, 3, HOLE)


@generic(20, GREY_DEEP)
def gem():
    outline = poly([(20, 14), (44, 14), (52, 24), (32, 47), (12, 24)], INK, 2)
    facets = (line(12.5, 24, 51.5, 24, HOLE, 2.2) + stroke("M24.5 14.5L27 24L32 46", HOLE, 2.2)
              + stroke("M39.5 14.5L37 24L32 46", HOLE, 2.2))
    return outline + facets
