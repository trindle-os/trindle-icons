# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 83: apps on Trindle's desktop that still had no icon."""
from lm import (
    AMBER_LIGHT, BLACK, BLUE_GREY_SOFT, BLUE_LIGHT, circle, CYAN_DEEP, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE_LIGHT, g, HOLE, INDIGO_DARK, INDIGO_SOFT, INK, line,
    ORANGE_LIGHT, path, poly, RED, rrect, stroke, TEAL_DARK, TEAL_LIGHT,
)
from glyphs.kit import registry

ICONS, SMALL, reg, small = registry()


@reg("eu.usdx.UltraStarDeluxe", DEEP_ORANGE_DEEP)
def ultrastar():
    wings = ""
    for side in (-1, 1):
        for ang, ln_ in [(62, 15), (90, 17), (118, 14)]:
            wings += g(rrect(32 - 2.8, 24 - ln_ - 5, 5.6, ln_ - 3, 2.8, INK),
                       f"rotate({side * ang} 32 24)")
    head = circle(32, 20, 7.5, INK) + "".join(circle(32 + x, 20 + y, 1.1, HOLE)
                                              for x in (-3, 0, 3) for y in (-3, 0, 3))
    handle = path("M28 28H36L34.5 46A2.5 2.5 0 0 1 29.5 46Z", INK, f' stroke="{HOLE}" stroke-width="2"')
    band = rrect(27.5, 29, 9, 4, 1.5, ORANGE_LIGHT)
    return wings + handle + band + circle(32, 20, 8.8, HOLE) + head


@reg("io.github.najepaliya.kleaner", RED)
def kleaner():
    seven = stroke("M16 20H31L20 42", INK, 5)
    tri = poly([(38, 22), (49, 42), (27, 42)], INK, 2) + poly([(38, 30), (43.5, 38.5), (32.5, 38.5)], HOLE, 1)
    return seven + tri


@reg("io.github.shonebinu.Defuse", BLUE_LIGHT)
def defuse():
    frame = rrect(15, 13, 34, 34, 5, INK)
    checks = "".join(rrect(32 + c * 4, 16 + r * 4, 4, 4, 0, BLUE_GREY_SOFT)
                     for r in range(7) for c in range(4) if (r + c) % 2 == 0)
    blob = path("M22 44C21 36 22 27 29 26C34 25 38 28 38.5 34C39 39 38.5 42 38 44Z", DEEP_ORANGE_LIGHT)
    eyes = circle(27.5, 32, 2.2, INK) + circle(33.5, 32, 2.2, INK) + circle(27.8, 32.3, 1, BLACK) + circle(33.8, 32.3, 1, BLACK)
    return frame + checks + blob + eyes


@reg("moe.liam.audimorf", INDIGO_DARK)
def audimorf():
    record = (f'<circle cx="32" cy="30" r="17" fill="none" stroke="{INK}" stroke-width="2.6"/>'
              f'<circle cx="32" cy="30" r="12.5" fill="none" stroke="{INDIGO_SOFT}" stroke-width="1.6"/>')
    wings = (path("M31.5 22C27 14 16 14 16.5 21C17 27 24 30 31.5 29Z", INK) +
             path("M32.5 22C37 14 48 14 47.5 21C47 27 40 30 32.5 29Z", INK) +
             path("M31.5 29C25 30.5 21.5 36 24.5 40C27 42.5 30.5 38 31.5 33Z", INK) +
             path("M32.5 29C39 30.5 42.5 36 39.5 40C37 42.5 33.5 38 32.5 33Z", INK))
    body = rrect(30.3, 19, 3.4, 22, 1.7, INDIGO_SOFT)
    feelers = stroke("M31 19.5L27.5 14.5M33 19.5L36.5 14.5", INK, 1.8)
    return record + wings + body + feelers


@reg("net.fhannenheim.musicfetch", DEEP_PURPLE_LIGHT)
def musicfetch():
    disk = path("M18 13H41L47 19V45A2 2 0 0 1 45 47H19A2 2 0 0 1 17 45V15A2 2 0 0 1 18 13Z", INK)
    shutter = rrect(24, 13, 15, 10, 1.5, HOLE) + rrect(33, 15, 4, 6, 1, INK)
    label = rrect(21, 29, 22, 15, 3, HOLE)
    note = circle(29.5, 40, 2.8, INK) + line(31.8, 40, 31.8, 32, INK, 2.4) + line(31.8, 32.5, 36, 33.5, INK, 2.4)
    return disk + shutter + label + note


@reg("re.sonny.Eloquent", TEAL_LIGHT)
def eloquent():
    paper = rrect(20, 11, 20, 14, 2, INK) + line(23.5, 16, 33, 16, HOLE, 2) + line(23.5, 20.5, 30, 20.5, HOLE, 2)
    body = rrect(14, 25, 36, 20, 5, INK)
    keys = "".join(circle(20 + 6 * k, 32, 1.8, HOLE) for k in range(5)) + rrect(23, 38, 18, 3, 1.5, HOLE)
    tick = circle(44, 16, 6.5, TEAL_DARK) + circle(44, 16, 2.6, INK)
    return paper + body + keys + tick


@reg("xyz.safeworlds.hiit", CYAN_DEEP)
def hiit():
    ring = f'<circle cx="32" cy="30" r="16" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    done = stroke("M32 18A12 12 0 0 1 43.4 26.3", AMBER_LIGHT, 5)
    rest = stroke("M43.4 26.3A12 12 0 1 1 32 18", INK, 5)
    knob = circle(32, 30, 4, INK)
    return ring + rest + done + knob


@small("eu.usdx.UltraStarDeluxe")
def ultrastar_s():
    wings = "".join(line(32 + s * 6, 25 + dy, 32 + s * 15, 21 + dy, INK, 4)
                    for s in (-1, 1) for dy in (-2, 4))
    return wings + circle(32, 20, 7.5, INK) + path("M28 28H36L34.5 46A2.5 2.5 0 0 1 29.5 46Z", INK)
