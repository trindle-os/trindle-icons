# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 29: gahshomar to gisto.

Same hand as batch01: chunky rounded marks in INK, HOLE for cut-outs,
any second shade a palette step.
"""
from lm import (
    AMBER, AMBER_DEEP, AMBER_LIGHT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_LIGHT, BROWN, BROWN_LIGHT, BROWN_SOFT, circle, cpath, cut, CYAN_DEEP,
    DEEP_ORANGE, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_SOFT, f, g,
    GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE,
    LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, line, ORANGE, ORANGE_DEEP, path, PINK, PINK_DEEP,
    PINK_LIGHT, poly, pt, PURPLE, PURPLE_LIGHT, RED, RED_DEEP, rrect, stroke, YELLOW_DARK,
)
from glyphs.kit import arc, _gear_c, registry, _ring

ICONS, SMALL, reg, small = registry()


def _g_path():
    x0, y0 = pt(32, 30, 12.5, -45)
    x1, y1 = pt(32, 30, 12.5, 0)
    return (f"M{f(x0)} {f(y0)}A12.5 12.5 0 1 0 {f(x1)} {f(y1)}"
            f"L44.5 30H33.5")


@reg("gahshomar", DEEP_ORANGE)
def gahshomar():
    page = rrect(15, 15, 34, 32, 6, INK)
    band = rrect(15, 15, 34, 8, 4, INK) + rect_line()
    rings = rrect(22, 11, 4, 8, 2, INK) + rrect(38, 11, 4, 8, 2, INK)
    script = (stroke("M42 29C42 33 40 35 37 35H23", HOLE, 2.6)
              + stroke("M31 30.5V35M26 29.5l1 1.5", HOLE, 2.6)
              + stroke("M40 41H24C22 41 21 39.5 21.5 38", HOLE, 2.6)
              + circle(34.5, 28, 1.5, HOLE))
    return page + band + rings + script


def rect_line():
    return line(15.5, 23, 48.5, 23, HOLE, 2)


@reg("gajim", BROWN_SOFT)
def gajim():
    head = circle(32, 20, 7.5, INK)
    body = path("M17 46C17 36 23 30.5 32 30.5C41 30.5 47 36 47 46Z", INK)
    collar = poly([(28, 30.5), (36, 30.5), (32, 35)], HOLE, 1.5)
    return head + body + collar


@reg("galculator", BLUE_DEEP)
def galculator():
    disp = rrect(17, 12, 30, 8, 2.5, INK)
    keys = ""
    for r in range(3):
        for c in range(3):
            keys += rrect(17 + c * 8, 24 + r * 8, 6, 6, 1.8, INK)
    keys += rrect(41, 24, 6, 22, 1.8, INK)
    return disp + keys


@reg("galternatives", ORANGE_DEEP)
def galternatives():
    x0, y0 = pt(32, 30, 14, -20)
    gring = stroke(f"M{f(x0)} {f(y0)}A14 14 0 1 0 46 30", INK, 4.5)
    bar = line(46, 30, 40, 30, INK, 4.5)
    a = circle(32, 30, 8, INK) + circle(31, 30, 3.2, HOLE) + rrect(34.3, 25.5, 2.4, 9, 1.2, HOLE)
    return gring + bar + a


@reg("gambas3", LIGHT_BLUE_DEEP)
def gambas3():
    body = stroke("M38 17C27 15 18 21 18 30C18 38 24 43 31 43", INK, 8)
    bands = (line(23, 22, 26.5, 25, HOLE, 1.6) + line(20, 29.5, 24.5, 30, HOLE, 1.6)
             + line(21.5, 37, 25.5, 35, HOLE, 1.6))
    tail = poly([(30, 43), (38, 37.5), (39.5, 47)], INK, 2.5)
    head = circle(40, 18, 5.5, INK) + circle(41.5, 16.5, 1.4, HOLE)
    whisk = stroke("M44 15C47 12 49 12 50 13M45 19C48 19 50 21 50 23", INK, 2.2)
    claws = stroke("M35 22.5L40 27M33 25L36 30.5", INK, 2.4)
    return body + bands + tail + head + whisk + claws


@reg("gamejolt", INDIGO_LIGHT)
def gamejolt():
    bolt = poly([(37, 12), (21, 32), (30, 32), (26, 48), (44, 26), (34, 26), (40, 12)], INK, 2.5)
    return bolt


@reg("gammastep", RED)
def gammastep():
    bulb = path("M32 12C24.5 12 19 17.5 19 24.5C19 29 21.5 32 24 34.5C25.5 36 26 37.5 26 39H38"
                "C38 37.5 38.5 36 40 34.5C42.5 32 45 29 45 24.5C45 17.5 39.5 12 32 12Z", INK)
    fil = stroke("M28 36V29L30 31.5L32 29L34 31.5L36 29V36", HOLE, 1.8)
    base = rrect(26, 40.5, 12, 3, 1.5, INK) + rrect(27, 44.5, 10, 3, 1.5, INK)
    return bulb + fil + base


@reg("gaphor", INDIGO_LIGHT)
def gaphor():
    left = rrect(14, 24, 11, 13, 2.5, INK) + line(16.5, 28, 22.5, 28, HOLE, 1.6)
    top = rrect(32, 12, 18, 12, 2.5, INK) + line(35, 16.5, 47, 16.5, HOLE, 1.6)
    bot = rrect(32, 36, 18, 12, 2.5, INK) + line(35, 40.5, 47, 40.5, HOLE, 1.6)
    conn = stroke("M19.5 24V18H30M19.5 37V42H30", INK, 2.4)
    return left + top + bot + conn


@reg("gargoyle-house", BROWN_LIGHT)
def gargoyle_house():
    roof = poly([(13, 29), (32, 13), (51, 29)], INK, 3)
    chim = rrect(18.5, 13, 5, 10, 1.5, INK)
    wall = rrect(17, 27, 30, 20, 2.5, INK)
    door = rrect(21.5, 32, 8, 15, 1.5, HOLE)
    win = rrect(34, 32, 9, 8, 1.5, HOLE)
    return chim + roof + wall + door + win


@reg("garrysmod", BLUE)
def garrysmod():
    bowl = _ring(31, 25, 7.5, INK, 5.5)
    stem = stroke("M38.5 17V36C38.5 42.5 34.5 45.5 29.5 45.5C26.5 45.5 24 44.5 22.5 42.5", INK, 5.5)
    return bowl + stem


@reg("gaupol", GREY_DARK)
def gaupol():
    bubble = path("M20 14H44C47.3 14 50 16.7 50 20V36C50 39.3 47.3 42 44 42H26L16 48L18 41.7"
                  "C15.6 40.9 14 38.6 14 36V20C14 16.7 16.7 14 20 14Z", INK)
    dots = circle(24, 28, 2.8, HOLE) + circle(32, 28, 2.8, HOLE) + circle(40, 28, 2.8, HOLE)
    return bubble + dots


@reg("gb-studio", YELLOW_DARK)
def gb_studio():
    body = path("M19 12H45C47.2 12 49 13.8 49 16V37C49 43 45 48 38 48H19"
                "C16.8 48 15 46.2 15 44V16C15 13.8 16.8 12 19 12Z", INK)
    screen = rrect(20, 17, 24, 20, 3, HOLE)
    square = rrect(27, 21, 13, 12, 2, INK)
    led = circle(23.5, 27, 1.6, INK)
    return body + screen + square + led


GBRAINY_HEAD = path('M34 12C24 12 17.5 18.5 17.5 27C17.5 29.5 16.5 31 15 33.5C14.2 35 15 36 16.5 36H18.5V40C18.5 42 20 43.5 22 43.5H25.5V48H44V38.5C47.5 35.5 49.5 31 49.5 26.5C49.5 18 43 12 34 12Z', INK)


@reg("gbrainy", CYAN_DEEP)
def gbrainy():
    head = GBRAINY_HEAD
    brain = path("M26 21.5C26 18.5 29 16.5 32 17.3C33.5 15.5 37 15.5 38.5 17.5C41.5 17 44.5 19.5 44 22.5"
                 "C46 24 46 27.5 44 29C44.5 31.5 42 33.5 39.5 33C38 35 34.5 35 33 33.3"
                 "C30.5 34.5 27.5 33 27.5 30.5C25 29.5 24.5 26 26.5 24.5C25.8 23.5 25.7 22.5 26 21.5Z", HOLE)
    fold = stroke("M31 22C33 23 33 26 31 27.5M37.5 21.5C36 24 38 26.5 40.5 26.5M34.5 29V33", INK, 1.8)
    return head + brain + fold


@reg("gcolor3", BLUE_GREY_DARK)
def gcolor3():
    cols = [AMBER, INDIGO_SOFT, BLUE, PURPLE, RED, ORANGE]
    out = ""
    for k, c in enumerate(cols):
        a0, a1 = -90 + 60 * k, -30 + 60 * k
        x0, y0 = pt(32, 31, 16, a0)
        x1, y1 = pt(32, 31, 16, a1)
        out += path(f"M32 31L{f(x0)} {f(y0)}A16 16 0 0 1 {f(x1)} {f(y1)}Z", c)
    pen = (stroke("M24 39L40.5 22.5", HOLE, 7.5) + stroke("M24 39L40.5 22.5", INK, 3.5)
           + stroke("M40.5 22.5L45 18", HOLE, 9.5) + stroke("M40.5 22.5L45 18", INK, 5.5)
           + stroke("M22 41L24 39", INK, 2.2))
    return out + pen


@reg("gcompris", ORANGE_DEEP)
def gcompris():
    wings = poly([(14, 28), (32, 24), (50, 28), (50, 33), (32, 32), (14, 33)], INK, 3)
    tail = poly([(24, 44), (32, 41), (40, 44), (40, 47), (24, 47)], INK, 2.5)
    body = path("M32 15C35.5 15 37 18 37 22V38C37 42 34.5 46 32 46C29.5 46 27 42 27 38V22"
                "C27 18 28.5 15 32 15Z", INK)
    prop = line(24, 13, 40, 13, INK, 2.6) + circle(32, 14.5, 2.2, INK)
    cockpit = path("M32 21a3 4 0 1 0 0.01 0Z", HOLE)
    return wings + tail + body + prop + cockpit


@reg("gcompris-edit", BLUE_GREY)
def gcompris_edit():
    head = cut(cpath(32, 22, 10.5) + "M28.5 10H35.5V21.5A3.5 3.5 0 0 1 28.5 21.5Z", INK)
    handle = rrect(28, 28, 8, 20, 4, INK)
    return head + handle


@reg("gconf-editor", DEEP_PURPLE_SOFT)
def gconf_editor():
    lens = _ring(28.5, 26.5, 10, INK, 5)
    handle = line(36, 34, 46, 44, INK, 6.5)
    return lens + handle


@reg("gcstar", BLUE)
def gcstar():
    face = circle(32, 30, 16.5, INK)
    eyes = path("M25 24.5a3.5 5.5 0 1 0 0.01 0Z", HOLE) + path("M39 24.5a3.5 5.5 0 1 0 0.01 0Z", HOLE)
    return face + eyes


def _db(cx, cy, s=1):
    out = ""
    for k in range(3):
        y = cy - 8 * s + k * 7 * s
        out += (path(f"M{f(cx - 10 * s)} {f(y)}V{f(y + 4.5 * s)}"
                     f"A{f(10 * s)} {f(3.5 * s)} 0 0 0 {f(cx + 10 * s)} {f(y + 4.5 * s)}"
                     f"V{f(y)}Z", INK)
                + f'<ellipse cx="{f(cx)}" cy="{f(y)}" rx="{f(10 * s)}" ry="{f(3.5 * s)}" fill="{INK}" '
                  f'stroke="{HOLE}" stroke-width="1.6"/>')
    top = f'<ellipse cx="{f(cx)}" cy="{f(cy - 8 * s)}" rx="{f(10 * s)}" ry="{f(3.5 * s)}" fill="{INK}"/>'
    return out + top


@reg("gda-browser-5.0", GREY_DARK)
def gda_browser():
    return _db(32, 26, 1.35)


@reg("gda-control-center", GREY_DARK)
def gda_control():
    badge = circle(41, 39, 10.5, HOLE) + circle(41, 39, 9, RED)
    return _db(28, 24, 1.15) + badge + _gear_c(41, 39, 4.5, INK, RED)


@reg("gddccontrol", BLUE_DEEP)
def gddccontrol():
    mon = rrect(13, 13, 34, 25, 3.5, INK)
    screen = path("M17 17H43L17 34Z", HOLE)
    stand = rrect(25, 38, 10, 5, 1, INK) + rrect(20, 42.5, 20, 3.5, 1.75, INK)
    badge = rrect(33, 30, 18, 18, 5, HOLE) + rrect(35, 32, 14, 14, 3.5, INK)
    tools = line(38, 35, 46, 43, HOLE, 2.4) + line(46, 35, 38, 43, HOLE, 2.4)
    return mon + screen + stand + badge + tools


@reg("gdevilspie", DEEP_ORANGE)
def gdevilspie():
    horns = (path("M20 20C17 17 16.5 13 18 10C19.5 13 22.5 15 25 16Z", INK)
             + path("M44 20C47 17 47.5 13 46 10C44.5 13 41.5 15 39 16Z", INK))
    crust = circle(32, 31, 14, INK) + "".join(
        circle(*pt(32, 31, 14, 15 * k), 2.6, INK) for k in range(24))
    gap = circle(32, 31, 10.5, HOLE) + circle(32, 31, 9, INK)
    slits = "".join(g(path("M32 24.5C33.5 26.5 33.5 28 32 29.5C30.5 28 30.5 26.5 32 24.5Z", HOLE),
                      f"rotate({60 * k} 32 31)") for k in range(6))
    return horns + crust + gap + slits


@reg("gdlauncher", LIGHT_BLUE_DARK)
def gdlauncher():
    hexa = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in
                                 [pt(32, 30, 17.5, -90 + 60 * k) for k in range(6)]) + "Z", INK, 2.6)
    horns = circle(22, 25, 5, INK) + circle(42, 25, 5, INK)
    curls = _ring(22, 25, 2, HOLE, 1.6) + _ring(42, 25, 2, HOLE, 1.6)
    head = path("M26 20H38C40.5 20 42 22 42 24.5V32C42 37.5 38 41 32 41C26 41 22 37.5 22 32V24.5"
                "C22 22 23.5 20 26 20Z", INK)
    eyes = circle(27.5, 28, 2.2, HOLE) + circle(36.5, 28, 2.2, HOLE)
    nose = circle(29.5, 35.5, 1.4, HOLE) + circle(34.5, 35.5, 1.4, HOLE)
    face = g(horns + head + curls + eyes + nose, "translate(32 30.5) scale(.78) translate(-32 -30.5)")
    return hexa + face


@reg("gdm-xnest", GREY_DARK)
def gdm_xnest():
    return cut("M18 15H46A5 5 0 0 1 51 20V40A5 5 0 0 1 46 45H18A5 5 0 0 1 13 40V20A5 5 0 0 1 18 15Z"
               "M21 21H43V39H21Z", INK) + rrect(25, 25, 14, 10, 1.5, INK)


@reg("geany", AMBER_DEEP)
def geany():
    body = path("M20 26H42V38C42 43 38.5 46 34 46H28C23.5 46 20 43 20 38Z", INK)
    lid = path("M21 25C21 20.5 25.5 18 31 18C36.5 18 41 20.5 41 25Z", INK) + circle(31, 16, 2.5, INK)
    spout = poly([(21, 32), (14, 24), (16.5, 23), (21, 28)], INK, 2)
    handle = stroke("M42 29H47V39H42", INK, 3)
    dia = "".join(poly([(x, 32.5), (x + 2.5, 35.5), (x, 38.5), (x - 2.5, 35.5)], HOLE, 0.8)
                  for x in (25, 31, 37))
    return body + lid + spout + handle + dia


@reg("gear-up", BROWN)
def gear_up():
    return stroke(_g_path(), AMBER_LIGHT, 6)


@reg("gedit", BLUE_GREY_DEEP)
def gedit():
    page = path("M18 12H38L46 20V45C46 46.7 44.7 48 43 48H18C16.3 48 15 46.7 15 45V15"
                "C15 13.3 16.3 12 18 12Z", INK)
    fold = path("M38 12V18C38 19.1 38.9 20 40 20H46Z", HOLE)
    lines = line(20, 26, 30, 26, HOLE, 2.2) + line(20, 32, 27, 32, HOLE, 2.2) + line(20, 38, 24, 38, HOLE, 2.2)
    pen = (stroke("M27 41L45 23", HOLE, 9) + stroke("M28.5 39.5L45 23", AMBER, 5.5)
           + poly([(25, 43.5), (26.5, 37.5), (31, 42)], AMBER, 1))
    return page + fold + lines + pen


@reg("geforcenow", ORANGE_DEEP)
def geforcenow():
    outer = arc(32, 39.2, 20.2, -152.9, -27.1) + arc(32, 20.8, 20.2, 27.1, 152.9)
    inner = arc(32, 37.83, 14.33, -146.9, -33.1) + arc(32, 22.17, 14.33, 33.1, 146.9)
    r_outer = arc(32, 39.2, 20.2, -90, -27.1) + arc(32, 20.8, 20.2, 27.1, 90)
    r_inner = arc(32, 37.83, 14.33, -90, -33.1) + arc(32, 22.17, 14.33, 33.1, 90)
    return (stroke(outer + inner, INK, 3) + circle(27, 30, 3.8, INK)
            + rrect(32, 13, 18, 34, 3, INK) + stroke(r_outer + r_inner, HOLE, 3))


@reg("gelemental", PURPLE_LIGHT)
def gelemental():
    flask = stroke("M28 13H36M29 13.5V25L18.5 42C17.2 44.5 18.5 46.5 21.5 46.5H42.5"
                   "C45.5 46.5 46.8 44.5 45.5 42L35 25V13.5", INK, 3)
    liquid = path("M22.5 37H41.5L44 41.5C45 43.3 44.2 44.5 42.3 44.5H21.7C19.8 44.5 19 43.3 20 41.5Z", INK)
    bubbles = circle(33, 21, 2, INK) + circle(29.5, 28, 1.7, INK) + circle(34, 32, 2.2, INK)
    return flask + liquid + bubbles


@reg("gemini", BLUE_GREY_DARK)
def gemini():
    return circle(32, 21, 8.8, LIGHT_BLUE) + circle(32, 39, 8.8, AMBER)


@reg("gens", INDIGO_SOFT)
def gens():
    return stroke(_g_path(), INK, 6)


@reg("gens-gs", INDIGO)
def gens_gs():
    quills = (poly([(30, 19), (11, 16), (27, 28)], INK, 3)
              + poly([(27, 25), (10, 31), (27, 35)], INK, 3)
              + poly([(28, 32), (14, 45), (33, 39)], INK, 3)
              + poly([(31, 21), (27, 11), (39, 18)], INK, 3))
    head = circle(35, 29, 11.5, INK)
    eye = path("M34 19.5C38.5 18.5 44 21 44 26C44 29 41.5 30 38.5 29.5C35.5 29 34 26.5 33.5 23.5Z", HOLE)
    pupil = circle(40, 25, 1.8, INK)
    muzzle = path("M31 34C35 38.5 44 39 48.5 33C47 30.5 44 30 41.5 31C38 32 34 32.5 31 34Z", DEEP_ORANGE_SOFT)
    nose = circle(47.5, 31, 2.6, INK)
    return quills + head + eye + pupil + muzzle + nose


def _geny(colour):
    return _ring(23.5, 30, 5, colour, 3.4) + _ring(39, 30, 8, colour, 3.6)


@reg("genymotion", PINK_LIGHT)
def genymotion():
    return _geny(INK)


@reg("genymotion-player", GREY_SOFT)
def genymotion_player():
    return _geny(PINK)


@reg("geogebra", INDIGO_LIGHT)
def geogebra():
    ell = f'<ellipse cx="32" cy="30.5" rx="15" ry="12" transform="rotate(-18 32 30.5)" fill="none" stroke="{INK}" stroke-width="2.4"/>'
    dots = ""
    for a in (-120, -40, 30, 110, 190):
        x, y = pt(32, 30.5, 13.5, a)
        dots += circle(x, y, 4.3, HOLE) + circle(x, y, 3.3, INK)
    return ell + dots


@reg("geonkick", GREY_DARK)
def geonkick():
    disc_ = circle(32, 30, 16.5, INK)
    wave = stroke("M17 31H21.5C23 31 23.5 20 26 20C28.5 20 28 40 31 40C33.5 40 33.5 25 36 25"
                  "C38 25 38 34 40 34C41.5 34 41.5 29 43 29H47", HOLE, 2.6)
    return disc_ + wave


@reg("geotranz", RED_DEEP)
def geotranz():
    towers = ""
    for x in (14, 41):
        towers += poly([(x, 20), (x, 15), (x + 2.5, 15), (x + 2.5, 18), (x + 3.75, 18), (x + 3.75, 15),
                        (x + 6.25, 15), (x + 6.25, 18), (x + 7.5, 18), (x + 7.5, 15), (x + 9, 15),
                        (x + 9, 46), (x, 46)], INK, 1.2)
    wall = poly([(23, 28), (23, 25), (26, 25), (26, 27.5), (30, 27.5), (30, 25), (34, 25), (34, 27.5),
                 (38, 27.5), (38, 25), (41, 25), (41, 46), (23, 46)], INK, 1.2)
    door = path("M28.5 46V38.5C28.5 36.5 30 35 32 35C34 35 35.5 36.5 35.5 38.5V46Z", HOLE)
    wins = rrect(17, 24, 3, 6, 1.5, HOLE) + rrect(44, 24, 3, 6, 1.5, HOLE)
    return towers + wall + door + wins


@reg("gerbera", ORANGE_DEEP)
def gerbera():
    petals = "".join(g(f'<ellipse cx="32" cy="18" rx="3.2" ry="7.5" fill="{INK}"/>', f"rotate({30 * k} 32 30)")
                     for k in range(12))
    return petals + circle(32, 30, 7.5, HOLE) + circle(32, 30, 5, INK) + circle(32, 30, 2.2, HOLE)


@reg("gerbview", GREY_DEEP)
def gerbview():
    chip = rrect(19, 14, 16, 28, 3, INK)
    pins = "".join(line(35, y, 41, y, INK, 2.2) + line(13, y, 19, y, INK, 2.2) for y in (19, 25, 31, 37))
    badge = circle(40, 38, 10.5, HOLE) + circle(40, 38, 9, RED_DEEP)
    eye = path("M32.5 38C35 34 45 34 47.5 38C45 42 35 42 32.5 38Z", INK) + circle(40, 38, 2.4, RED_DEEP)
    return chip + pins + badge + eye


@reg("gespeaker", BLUE_GREY_DARK)
def gespeaker():
    head = path("M16 20C16 15 20 13 26 13C33 13 38 15.5 38 21V33C38 37 36 40 32 41V47H22V42"
                "C18 40 16 37 16 33Z", INK)
    eyes = path("M20 23H26L25 27.5H21Z", HOLE) + path("M29 23H35L34 27.5H30Z", HOLE)
    mouth = stroke("M20.5 34.5H34", HOLE, 2.4)
    waves = stroke(arc(38, 29, 6, -45, 45), INK, 2.6) + stroke(arc(38, 29, 11, -45, 45), INK, 2.6)
    return head + eyes + mouth + waves


@reg("gfie_icon", BLUE_LIGHT)
def gfie():
    fish = f'<ellipse cx="27" cy="27" rx="13" ry="9.5" fill="{INK}"/>'
    tail = poly([(37, 27), (48, 18.5), (47, 35.5)], INK, 3)
    eye = circle(20.5, 24.5, 1.9, HOLE)
    badge = circle(40, 39, 10.5, HOLE) + circle(40, 39, 9, BLUE_DARK)
    pen = stroke("M36 43L44 35", INK, 3.4) + poly([(34.5, 44.5), (35.2, 41.3), (37.7, 43.8)], INK, 0.8)
    return fish + tail + eye + badge + pen


@reg("gftp", CYAN_DEEP)
def gftp():
    box = cut("M24 12H40A3 3 0 0 1 43 15V29A3 3 0 0 1 40 32H24A3 3 0 0 1 21 29V15A3 3 0 0 1 24 12Z"
              "M26 17H38V27H26Z", INK)
    wire = stroke("M32 32V38M19 44H45", INK, 2.6) + line(32, 38, 32, 44, INK, 2.6)
    nodes = circle(19, 44, 4, INK) + circle(32, 44, 4, INK) + circle(45, 44, 4, INK)
    return box + wire + nodes


@reg("ghex", BROWN_LIGHT)
def ghex():
    out = ""
    for cx, cy in ((25, 21), (40, 30), (25, 39)):
        out += poly([pt(cx, cy, 8.8, 60 * k) for k in range(6)], INK, 2)
    seps = stroke("M33.5 21.5L29.5 30.5L33.5 38.5M17 30H29.5", HOLE, 1.8)
    return out + seps


@reg("ghidra", RED_DEEP)
def ghidra():
    body = stroke(arc(32, 30, 15.5, 20, 285), INK, 4)
    head = path("M17 28C19 21 25 17.5 32 18L42 20.5L37.5 24L47 25.5L39 29.5C38 33.5 34 36 29 35.5"
                "C23 35 18.5 32.5 17 28Z", INK)
    horn = poly([(21, 22), (15, 13), (27, 18.5)], INK, 2)
    eye = poly([(27, 23.5), (33, 23), (29.5, 26.5)], HOLE, 1)
    return body + horn + head + eye


@reg("ghostwriter", BLUE_GREY_DEEP)
def ghostwriter():
    ghost = path("M32 12C23.5 12 18 18.5 18 27V47C20.5 45 22.5 45 25 47C27.5 45 29.5 45 32 47"
                 "C34.5 45 36.5 45 39 47C41.5 45 43.5 45 46 47V27C46 18.5 40.5 12 32 12Z", INK)
    arms = circle(17.5, 31, 3.5, INK) + circle(46.5, 31, 3.5, INK)
    eyes = path("M26.5 22a2.8 4 0 1 0 0.01 0Z", HOLE) + path("M37.5 22a2.8 4 0 1 0 0.01 0Z", HOLE)
    return ghost + arms + eyes


@reg("gifcurry", DEEP_PURPLE)
def gifcurry():
    return _ring(32, 30, 15.5, INK, 3) + stroke("M21 37L27 21L32 38L37 22L43 38", INK, 4)


@reg("gifup", DEEP_ORANGE_LIGHT)
def gifup():
    bars = rrect(13, 15, 5, 30, 2.5, INK) + rrect(20.5, 15, 5, 30, 2.5, INK)
    play = poly([(29, 15), (50, 30), (29, 45)], INK, 3.5)
    return bars + play


@reg("giggle", RED_DEEP)
def giggle():
    stems = stroke("M22 36C24 29 29 21 33 16M42 38C41 30 38 22 33 16", INK, 2.4)
    leaf = path("M33 16C27 12 20 13 17 18C23 21 29 20 33 16Z", INK)
    cherries = (circle(21, 38, 8, INK) + circle(42, 39, 8.5, HOLE) + circle(42, 39, 7.5, INK)
                + circle(18.5, 35.5, 1.8, HOLE) + circle(39.5, 36.5, 1.8, HOLE))
    return stems + leaf + cherries


@reg("gish", AMBER)
def gish():
    blob = path("M14 38C14 26 21.5 18 32 18C42.5 18 50 26 50 38C50 42.5 47 44 43 44H21C17 44 14 42.5 14 38Z", INK)
    eyes = (path("M18.5 30C22 27.5 27.5 28.5 29.5 31.5C27 34.5 20 34.5 18.5 30Z", HOLE)
            + path("M45.5 30C42 27.5 36.5 28.5 34.5 31.5C37 34.5 44 34.5 45.5 30Z", HOLE))
    return blob + eyes


@reg("gisto", BLUE_DEEP)
def gisto():
    lb = stroke("M20 17C17 17 16.5 18.5 16.5 21V26.5C16.5 28.5 15.5 30 13.5 30C15.5 30 16.5 31.5 16.5 33.5"
                "V39C16.5 41.5 17 43 20 43", INK, 2.6)
    rb = stroke("M44 17C47 17 47.5 18.5 47.5 21V26.5C47.5 28.5 48.5 30 50.5 30C48.5 30 47.5 31.5 47.5 33.5"
                "V39C47.5 41.5 47 43 44 43", INK, 2.6)
    x0, y0 = pt(32, 30, 8.5, -45)
    x1, y1 = pt(32, 30, 8.5, 0)
    gl = stroke(f"M{f(x0)} {f(y0)}A8.5 8.5 0 1 0 {f(x1)} {f(y1)}L40.5 30H33.5", INK, 3.6)
    return lb + rb + gl


@small("gahshomar")
def gahshomar_s():
    return (rrect(14, 13, 36, 35, 7, INK) + line(14.5, 23, 49.5, 23, HOLE, 3.5)
            + stroke("M42 29C42 34 40 36 37 36H22", HOLE, 3.6))


@small("galculator")
def galculator_s():
    keys = "".join(rrect(15 + c * 12, 26 + r * 11, 9, 8, 2, INK) for r in range(2) for c in range(2))
    return rrect(15, 11, 34, 10, 3, INK) + keys + rrect(39, 26, 10, 19, 2, INK)


@small("galternatives")
def galternatives_s():
    x0, y0 = pt(32, 30, 14.5, -20)
    return (stroke(f"M{f(x0)} {f(y0)}A14.5 14.5 0 1 0 46.5 30", INK, 5) + line(46.5, 30, 41, 30, INK, 5)
            + circle(32, 30, 7.5, INK) + circle(31, 30, 3.2, HOLE))


@small("gambas3")
def gambas3_s():
    body = stroke("M38 17C27 15 18 21 18 30C18 38 24 43 31 43", INK, 9)
    tail = poly([(30, 43), (39, 37), (40, 48)], INK, 3)
    head = circle(40, 18, 6, INK) + circle(41.5, 16.5, 1.8, HOLE)
    whisk = stroke("M45 14C47.5 12 49 12 50 13", INK, 2.4)
    return body + tail + head + whisk


@small("gaphor")
def gaphor_s():
    return (rrect(13, 23, 12, 14, 3, INK) + rrect(32, 11, 19, 14, 3, INK) + rrect(32, 35, 19, 14, 3, INK)
            + stroke("M19 23V18H30M19 37V42H30", INK, 2.6))


@small("gbrainy")
def gbrainy_s():
    head = GBRAINY_HEAD
    brain = f'<ellipse cx="35" cy="25" rx="9.5" ry="8" fill="{HOLE}"/>'
    return head + brain


@small("gcolor3")
def gcolor3_s():
    cols = [AMBER, BLUE_LIGHT, BLUE, PURPLE, RED, ORANGE]
    out = ""
    for k, c in enumerate(cols):
        x0, y0 = pt(32, 30, 17, -90 + 60 * k)
        x1, y1 = pt(32, 30, 17, -30 + 60 * k)
        out += path(f"M32 30L{f(x0)} {f(y0)}A17 17 0 0 1 {f(x1)} {f(y1)}Z", c)
    return out + stroke("M24 38L42 20", HOLE, 7) + stroke("M24 38L42 20", INK, 3.4)


def _db_s(cx, cy, s):
    out = ""
    for k in range(2):
        y = cy - 5 * s + k * 9 * s
        out += (path(f"M{f(cx - 10 * s)} {f(y)}V{f(y + 6 * s)}"
                     f"A{f(10 * s)} {f(3.5 * s)} 0 0 0 {f(cx + 10 * s)} {f(y + 6 * s)}V{f(y)}Z", INK)
                + f'<ellipse cx="{f(cx)}" cy="{f(y)}" rx="{f(10 * s)}" ry="{f(3.5 * s)}" fill="{INK}" '
                  f'stroke="{HOLE}" stroke-width="2.4"/>')
    return out + f'<ellipse cx="{f(cx)}" cy="{f(cy - 5 * s)}" rx="{f(10 * s)}" ry="{f(3.5 * s)}" fill="{INK}"/>'


@small("gda-browser-5.0")
def gda_browser_s():
    return _db_s(32, 25, 1.45)


@small("gda-control-center")
def gda_control_s():
    badge = circle(42, 40, 11, HOLE) + circle(42, 40, 9.5, RED)
    return _db_s(27, 23, 1.2) + badge + circle(42, 40, 4.8, INK) + circle(42, 40, 2, RED)


@small("gddccontrol")
def gddccontrol_s():
    mon = rrect(12, 12, 36, 26, 4, INK) + path("M16.5 16.5H43.5L16.5 33.5Z", HOLE)
    stand = rrect(20, 41, 18, 4, 2, INK)
    badge = rrect(32, 29, 20, 20, 6, HOLE) + rrect(34.5, 31.5, 15, 15, 4, INK)
    return mon + stand + badge + line(38, 35, 46, 43, HOLE, 3) + line(46, 35, 38, 43, HOLE, 3)


@small("gdevilspie")
def gdevilspie_s():
    horns = (path("M20 20C17 17 16.5 13 18 10C19.5 13 22.5 15 25 16Z", INK)
             + path("M44 20C47 17 47.5 13 46 10C44.5 13 41.5 15 39 16Z", INK))
    return horns + circle(32, 31, 16, INK) + circle(32, 31, 9.5, HOLE) + circle(32, 31, 6, INK)


@small("gdlauncher")
def gdlauncher_s():
    horns = circle(20.5, 24, 6, INK) + circle(43.5, 24, 6, INK)
    head = path("M25 17H39C42 17 44 19.5 44 22.5V32C44 39 39 44 32 44C25 44 20 39 20 32V22.5"
                "C20 19.5 22 17 25 17Z", INK)
    eyes = circle(26.5, 28, 2.8, HOLE) + circle(37.5, 28, 2.8, HOLE)
    return horns + head + eyes + rrect(28, 35, 8, 3.5, 1.75, HOLE)


@small("gedit")
def gedit_s():
    page = rrect(14, 11, 30, 38, 5, INK)
    lines = line(20, 22, 32, 22, HOLE, 3) + line(20, 30, 28, 30, HOLE, 3)
    pen = stroke("M27 43L47 23", HOLE, 11) + stroke("M28.5 41.5L47 23", AMBER, 7)
    return page + lines + pen


@small("geogebra")
def geogebra_s():
    ell = f'<ellipse cx="32" cy="30.5" rx="15" ry="12" transform="rotate(-18 32 30.5)" fill="none" stroke="{INK}" stroke-width="3"/>'
    dots = "".join(circle(*pt(32, 30.5, 13.5, a), 4.8, INK) for a in (-110, 10, 130))
    return ell + dots


@small("geonkick")
def geonkick_s():
    return circle(32, 30, 17, INK) + stroke("M16 31H21C23 31 23.5 19 26.5 19C29.5 19 29 41 32.5 41"
                                           "C35.5 41 35.5 28 38.5 28C40.5 28 41 31 43 31H48", HOLE, 3.4)


@small("geotranz")
def geotranz_s():
    t = ""
    for x in (13, 40):
        t += poly([(x, 46), (x, 14), (x + 4, 14), (x + 4, 18), (x + 7, 18), (x + 7, 14), (x + 11, 14), (x + 11, 46)], INK, 1)
    wall = rrect(22, 26, 20, 20, 1, INK)
    door = path("M28 46V39C28 36.8 29.8 35 32 35C34.2 35 36 36.8 36 39V46Z", HOLE)
    return t + wall + door


@small("gerbera")
def gerbera_s():
    petals = "".join(g(f'<ellipse cx="32" cy="17" rx="4.2" ry="8" fill="{INK}"/>', f"rotate({45 * k} 32 30)")
                     for k in range(8))
    return petals + circle(32, 30, 8, HOLE) + circle(32, 30, 5, INK)


@small("gerbview")
def gerbview_s():
    chip = rrect(17, 12, 20, 30, 4, INK)
    pins = "".join(line(12, y, 17, y, INK, 3) for y in (19, 28, 37))
    badge = circle(41, 39, 11.5, HOLE) + circle(41, 39, 10, RED_DEEP)
    eye = path("M33 39C35.5 34.5 46.5 34.5 49 39C46.5 43.5 35.5 43.5 33 39Z", INK) + circle(41, 39, 2.6, RED_DEEP)
    return chip + pins + badge + eye


@small("gespeaker")
def gespeaker_s():
    head = path("M15 20C15 15 19 12 26 12C33 12 38 15 38 21V33C38 37 36 40 32 41V48H21V42"
                "C17 40 15 37 15 33Z", INK)
    eyes = rrect(19, 22, 7, 6, 2, HOLE) + rrect(28, 22, 7, 6, 2, HOLE)
    waves = stroke(arc(38, 29, 8, -45, 45), INK, 3.2)
    return head + eyes + waves


@small("gfie_icon")
def gfie_s():
    fish = f'<ellipse cx="27" cy="27" rx="14" ry="10.5" fill="{INK}"/>'
    tail = poly([(37, 27), (49, 17), (48, 36)], INK, 3)
    badge = circle(41, 40, 11, HOLE) + circle(41, 40, 9.5, BLUE_DARK)
    return fish + tail + circle(20.5, 24.5, 2.4, HOLE) + badge + stroke("M36.5 44.5L45 36", INK, 4)


@small("ghidra")
def ghidra_s():
    body = stroke(arc(32, 30, 15.5, 20, 285), INK, 5)
    head = path("M16 28C18 21 25 17 32 17.5L44 21L47 26L39 30C38 34 34 37 29 36.5"
                "C23 36 17.5 33 16 28Z", INK)
    return body + head + circle(29, 24.5, 2.2, HOLE)


@small("gifcurry")
def gifcurry_s():
    return _ring(32, 30, 16, INK, 3.4) + stroke("M22 37L27.5 22L32 36L36.5 22L42 37", INK, 4.4)


@small("giggle")
def giggle_s():
    stems = stroke("M22 34C24 28 29 21 33 15M42 36C41 29 38 21 33 15", INK, 3)
    leaf = path("M33 15C27 11 20 12 17 17C23 20 29 19 33 15Z", INK)
    return stems + leaf + circle(21, 38, 9, INK) + circle(42, 39, 10, HOLE) + circle(42, 39, 8.5, INK)


@small("gisto")
def gisto_s():
    lb = stroke("M21 15C17 15 16.5 17 16.5 20V26C16.5 28.5 15 30 13 30C15 30 16.5 31.5 16.5 34"
                "V40C16.5 43 17 45 21 45", INK, 3.4)
    rb = stroke("M43 15C47 15 47.5 17 47.5 20V26C47.5 28.5 49 30 51 30C49 30 47.5 31.5 47.5 34"
                "V40C47.5 43 47 45 43 45", INK, 3.4)
    x0, y0 = pt(32, 30, 8, -45)
    gl = stroke(f"M{f(x0)} {f(y0)}A8 8 0 1 0 40 30H33", INK, 4.4)
    return lb + rb + gl


@small("genymotion-player")
def genymotion_player_s():
    return _ring(22.5, 30, 5.5, PINK_DEEP, 4.2) + _ring(40, 30, 8.5, PINK_DEEP, 4.4)


@small("genymotion")
def genymotion_s():
    return _ring(22.5, 30, 5.5, INK, 4.2) + _ring(40, 30, 8.5, INK, 4.4)
