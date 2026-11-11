# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 37: jamovi .. kali-forensics-trans."""
from lm import (
    AMBER, AMBER_DEEP, AMBER_LIGHT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP, BROWN_LIGHT, circle, cpath,
    cut, CX, CY, CYAN, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_LIGHT, g,
    GREY_DARK, GREY_DEEP, HOLE, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE_DEEP, line,
    ORANGE_DEEP, path, PINK_DARK, PINK_DEEP, PINK_SOFT, poly, pt, PURPLE_DARK, PURPLE_SOFT, RED,
    RED_DEEP, RED_LIGHT, rrect, stroke, YELLOW_DARK, YELLOW_DEEP, YELLOW_LIGHT,
)
from glyphs.kit import ell_c, registry, _ring

ICONS, SMALL, reg, small = registry()


@reg("jamovi", BLUE_DEEP)
def jamovi():
    return path("M16.5 14H26.5V32C26.5 36 28 38.5 30.5 38.5C32 38.5 33 37.5 34 35L42.5 14H48.5L39 39"
                "C37 44 34 46.5 29.5 46.5C21.5 46.5 16.5 41.5 16.5 34Z", INK)


def _j():
    return (stroke("M25 15.5H43", INK, 5) +
            stroke("M37 15.5V34C37 41 33 45 27.5 45C23 45 20 42.5 20 39", INK, 6) +
            circle(20.5, 38, 4.2, INK))


@reg("jgray", GREY_DEEP)
@reg("jgreen", BLUE_DEEP)
@reg("jred", RED_DEEP)
@reg("jyellow", AMBER_DEEP)
@reg("jblue", BLUE)
def jblue():
    return _j()


@reg("jango", BLUE_DARK)
def jango():
    return circle(35, 16, 3.6, INK) + stroke("M35 24V38C35 43.5 31.5 46 26.5 45", INK, 6)


@reg("jpexs-decompiler", LIGHT_BLUE_DEEP)
def jpexs():
    return (stroke("M17.5 44V16H29M17.5 29.5H27", INK, 5) +
            stroke("M35 44V16H46.5M35 29.5H44.5", INK, 5))


@reg("junior_install_icon", RED_DEEP)
def junior():
    return stroke("M44 18C40 30 36 40 29 41C23 42 18.5 37.5 18.5 31C18.5 24 24 19.5 29.5 20.5"
                  "C35 21.5 38 33 44.5 42", INK, 4.6)


@reg("kalgebra", YELLOW_DARK)
def kalgebra():
    return stroke("M43 17V15H20L33 30L20 45H43V43", INK, 4.6)


@reg("kakoune", DEEP_ORANGE_DEEP)
def kakoune():
    d = g(rrect(17, 15, 30, 30, 6, INK), "rotate(45 32 30)")
    return d + stroke("M27 20V40M38 20L28 30.5L38 40", HOLE, 4.8)


@reg("juci", INDIGO_LIGHT)
def juci():
    c = stroke("M26.5 20H17.5V40H26.5", INK, 5)
    plus = "".join(line(x - 4.5, 30, x + 4.5, 30, INK, 3.8) + line(x, 25.5, x, 34.5, INK, 3.8)
                   for x in (34, 45))
    return c + plus


@reg("kajongg", ORANGE_DEEP)
def kajongg():
    return (rrect(15, 12, 34, 36, 5, INK) + stroke("M22 23H42V34H22Z", HOLE, 3.6)
            + line(32, 17, 32, 43, HOLE, 4))


@reg("jazzradio", ORANGE_DEEP)
def jazzradio():
    heads = circle(22, 41, 5.5, INK) + circle(41, 37, 5.5, INK)
    stems = line(26, 41, 26, 18, INK, 3.6) + line(45, 37, 45, 14, INK, 3.6)
    beam = poly([(26, 16), (45, 12), (45, 19), (26, 23)], INK, 3)
    return heads + stems + beam


@reg("juk", BLUE_GREY_DEEP)
def juk():
    return (g(ell_c(27, 40, 6.5, 5, AMBER), "rotate(-20 27 40)") +
            line(32.5, 39, 32.5, 15, AMBER, 3.6) +
            stroke("M32.5 15.5C34 21.5 43 22 40 33", AMBER, 3.6))


@reg("kaffeine", BROWN_DEEP)
def kaffeine():
    body = rrect(16, 25, 32, 21, 3.5, INK)
    top = rrect(16, 14.5, 32, 7.5, 2.5, INK)
    stripes = "".join(line(x, 15.5, x - 3, 21, HOLE, 2.4) for x in (26, 34, 42))
    play = poly([(28, 30), (28, 41), (37.5, 35.5)], HOLE, 2)
    return top + stripes + body + play


@reg("k9-copy", GREY_DARK)
def k9copy():
    disc = cut(cpath(29, 28, 15) + cpath(29, 28, 4), INK)
    badge = (circle(41.5, 40, 9.5, HOLE) + circle(41.5, 40, 8, RED) +
             circle(41.5, 40, 4.6, INK) + circle(41.5, 40, 2.1, RED))
    return disc + badge


@reg("java", RED)
def java():
    cup = path("M19 31H40V36C40 41 36 44 31 44H28C23 44 19 41 19 36Z", INK)
    handle = stroke("M40 33.5C45 33 45.5 40 39.5 40", INK, 2.6)
    saucer = line(16, 48, 43, 48, INK, 2.8)
    steam = (stroke("M30 27C26 23.5 34 21 30 16.5C28.5 14.5 29.5 12.5 31.5 11.5", INK, 2.8) +
             stroke("M35.5 26.5C33.5 24 37.5 22.5 35.5 19.5", INK, 2.4))
    return g(cup + handle + saucer + steam, "translate(1.5 -1)")


@reg("jd-gui", BROWN_LIGHT)
def jdgui():
    cup = path("M15 26H41V36C41 41.5 37 45.5 31.5 45.5H24.5C19 45.5 15 41.5 15 36Z", INK)
    coffee = ell_c(28, 26, 13, 3.8, INK) + ell_c(28, 26, 10, 2.4, BROWN_DEEP)
    handle = stroke("M41 29.5H43C46 29.5 47.5 31.5 47.5 33.5C47.5 36.5 45 38.5 41 38.5", INK, 3)
    steam = stroke("M29 19C26 16.5 32 14.5 29 11", INK, 2.8)
    return cup + coffee + handle + steam


@reg("javasnoop", DEEP_ORANGE_DEEP)
def javasnoop():
    horns = (poly([(18, 27), (15, 12), (27, 21)], INK, 2.5) +
             poly([(46, 27), (49, 12), (37, 21)], INK, 2.5))
    head = circle(32, 32, 14, INK)
    eyes = stroke("M23 29.5L29 33L23.5 36", HOLE, 3) + stroke("M41 29.5L35 33L40.5 36", HOLE, 3)
    return horns + head + eyes


@reg("jdeveloper", RED_DEEP)
def jdeveloper():
    return (circle(CX, CY, 16.5, INK) + circle(35.5, 30, 12, HOLE) +
            circle(37.5, 30, 8.5, INK) + circle(40, 30, 5, HOLE))


@reg("jprofiler", BLUE_DEEP)
def jprofiler():
    face = circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.5, HOLE)
    needle = poly([(29.5, 33), (34.5, 35), (40.5, 18)], INK, 1.6)
    dot = circle(32, 34, 4.8, INK) + circle(32, 34, 3, RED)
    return face + needle + dot


@reg("jamulus", LIGHT_BLUE_DEEP)
def jamulus():
    cloud = (circle(24, 33, 8.5, INK) + circle(34, 25.5, 11, INK) + circle(42.5, 34, 7, INK)
             + rrect(16, 33, 33, 9, 4.5, INK))
    bolt = poly([(36, 17), (27, 31), (33, 31), (29.5, 43), (40, 27), (34, 27), (38, 17)], HOLE, 1.2)
    return cloud + bolt


@reg("jasp", BLUE_GREY_LIGHT)
def jasp():
    pts = [(36, 14), (45, 16.5), (35, 42), (25, 44.5), (19, 37.5), (25.5, 31.5)]
    d = "M" + "L".join(f"{x} {y}" for x, y in pts)
    lines = stroke(d, INK, 2.6) + line(36, 14, 35, 42, INK, 2.6)
    return lines + "".join(circle(x, y, 3.2, INK) for x, y in pts)


@reg("jclic", ORANGE_DEEP)
def jclic():
    j = path("M30 21H41V33C41 41.5 35.5 46.5 28 46.5C21.5 46.5 17.5 42.5 16.5 37L25 35.5"
             "C25.5 37.5 26.5 38.5 28 38.5C29.5 38.5 30 37.5 30 35Z", INK)
    sq = g(rrect(17.5, 12.5, 13, 13, 2, YELLOW_LIGHT), "rotate(-14 24 19)")
    return j + sq


@reg("jclicauthor", ORANGE_DEEP)
def jclicauthor():
    tri = cut("M15 46L47 46L47 15Z" + "M30 41.5L42.5 41.5L42.5 28.5Z", INK)
    tri = path("M15 46L47 46L47 15Z", "none",
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"') + tri
    sq = g(rrect(16, 13, 13, 13, 2, YELLOW_LIGHT), "rotate(-14 22.5 19.5)")
    return tri + sq


@reg("jclicreports", ORANGE_DEEP)
def jclicreports():
    bars = rrect(15, 33, 9, 14, 2, INK) + rrect(27.5, 27, 9, 20, 2, INK) + rrect(40, 20, 9, 27, 2, INK)
    sq = g(rrect(17, 13, 12, 12, 2, YELLOW_LIGHT), "rotate(-14 23 19)")
    return bars + sq


@reg("jdownloader", BLUE_GREY_DARK)
def jdownloader():
    globe = circle(31, 30, 15, INDIGO_LIGHT) + _ring(31, 30, 15, INK, 2.4)
    arrow = stroke("M19 16C29 18 36 24 39 35", AMBER_LIGHT, 5.5)
    head = poly([(32.5, 34), (46, 32), (41, 44.5)], AMBER_LIGHT, 2.5)
    return globe + arrow + head


@reg("jellyfin", DEEP_PURPLE)
def jellyfin():
    outer = ("M32 12.5C29 12.5 13.5 40.5 15.5 44C17.5 47.5 46.5 47.5 48.5 44"
             "C50.5 40.5 35 12.5 32 12.5Z")
    inner = "M32 22C30.3 22 22.5 37 23.8 39C25 41 39 41 40.2 39C41.5 37 33.7 22 32 22Z"
    core = path("M32 28.5C31 28.5 27.5 35 28.2 35.8C29 36.8 35 36.8 35.8 35.8"
                "C36.5 35 33 28.5 32 28.5Z", INK)
    return cut(outer + inner, INK) + core


@reg("jetbrains-toolbox", PINK_DEEP)
def jetbrains_toolbox():
    top = poly([(32, 13), (48, 21), (32, 29), (16, 21)], INK, 2)
    left = poly([(16, 21), (32, 29), (32, 47), (16, 39)], PINK_SOFT, 2)
    right = poly([(48, 21), (32, 29), (32, 47), (48, 39)], PURPLE_DARK, 2)
    return top + left + right + line(36, 39.5, 42.5, 36.3, INK, 2.8)


@reg("jmonkeyengine", BROWN)
def jmonkey():
    ears = circle(16.5, 31, 5.5, INK) + circle(47.5, 31, 5.5, INK)
    tuft = poly([(24, 18), (27, 11), (31, 16), (35, 10.5), (38, 16.5), (42, 13), (41, 21)], INK, 2)
    head = circle(32, 30, 14.5, INK)
    face = (circle(27, 28.5, 6, HOLE) + circle(37, 28.5, 6, HOLE) + ell_c(32, 37, 10, 6.5, HOLE))
    eyes = circle(27.5, 29, 2.2, INK) + circle(36.5, 29, 2.2, INK)
    mouth = stroke("M26 38C30 41 34 41 38 38", INK, 2.4)
    return ears + tuft + head + face + eyes + mouth


@reg("jockey", BLUE_GREY)
def jockey():
    bracket = stroke("M15 14H17V46", INK, 2.6)
    card = rrect(19, 17, 30, 21, 3, INK)
    chip = rrect(29, 22, 10, 10, 1.5, HOLE)
    pins = "".join(rrect(x, 38, 3.4, 6, 1, INK) for x in (27, 32.5, 38, 43.5))
    return bracket + card + chip + pins


def _john(band):
    hat = rrect(24.5, 10.5, 12, 11, 1.5, INK) + rrect(19.5, 20, 22, 3.6, 1.8, INK)
    b = rrect(24.5, 17.5, 12, 2.6, 0, band) if band else ""
    head = path("M24.5 23H37V29C37 33 34.5 36 31 36C27.5 36 24.5 33 24.5 29Z", INK)
    coat = path("M16 48C16 40 21 35.5 26 34.5L31 38L36 34.5C41 35.5 46 40 46 48Z", INK)
    collar = poly([(37.5, 27), (41, 33.5), (35.5, 36)], INK, 1.5)
    return hat + b + head + collar + coat


@reg("john", RED_DEEP)
def john():
    return _john(None)


@reg("johnny", BLUE_GREY_DARK)
def johnny():
    return _john(RED_LIGHT)


@reg("josm", LIGHT_BLUE_DEEP)
def josm():
    m = poly([(15, 17), (25, 13), (38, 17), (48, 13), (48, 42), (38, 46), (25, 42), (15, 46)], INK, 2)
    folds = line(25, 14, 25, 41, HOLE, 1.8) + line(38, 18, 38, 45, HOLE, 1.8)
    pencil = (line(46, 15, 34, 33, AMBER_DEEP, 5.5, "butt") +
              poly([(31.7, 31.5), (36.3, 34.5), (31.5, 38.5)], BROWN_DARK, 1.5))
    return m + folds + pencil


@reg("journey-of-a-roach", BROWN)
def roach():
    head = rrect(15, 14, 34, 32, 12, INK)
    eyes = (circle(24.5, 32, 6.5, INDIGO_SOFT) + circle(39.5, 32, 6.5, INDIGO_SOFT) +
            circle(25.5, 32.5, 2.3, BLUE_GREY_DARK) + circle(38.5, 32.5, 2.3, BLUE_GREY_DARK))
    crack = stroke("M33 18L37 22.5L41.5 20.5M37 22.5L37.5 25.5", HOLE, 2.2)
    return head + eyes + crack


@reg("jubler", BLUE_DEEP)
def jubler():
    tl = path("M15.5 29.5A14 14 0 0 1 29.5 15.5V29.5Z", AMBER_LIGHT)
    tr = path("M33 15.5A15 15 0 0 1 48 30.5V45.5H33Z", INK)
    bl = path("M15.5 33H29.5V47A14 14 0 0 1 15.5 33Z", PINK_SOFT)
    return tl + tr + bl + circle(41, 24, 2.3, HOLE)


@reg("julia", BLUE_GREY_DARK)
def julia():
    return (circle(32, 19, 7.5, CYAN) + circle(21.5, 37.5, 7.5, RED_LIGHT) +
            circle(42.5, 37.5, 7.5, PURPLE_SOFT))


@reg("jupyter", DEEP_ORANGE_LIGHT)
def jupyter():
    top = path("M16 24C20 14.5 44 14.5 48 24C41 19.5 23 19.5 16 24Z", INK)
    bot = path("M16 36C20 45.5 44 45.5 48 36C41 40.5 23 40.5 16 36Z", INK)
    dots = circle(45, 13.5, 2.8, INK) + circle(18, 44.5, 3.2, INK) + circle(19, 15, 2, INK)
    return top + bot + dots


@reg("k4dirstat", BROWN_LIGHT)
def k4dirstat():
    outer = stroke("M20 20.5A15 15 0 1 1 18 38", INK, 4.4)
    inner = _ring(32, 30, 7.5, INK, 2.6) + path("M24.5 30A7.5 7.5 0 0 1 39.5 30Z", INK)
    return outer + inner


@reg("kaddressbook", BROWN)
def kaddressbook():
    back = (circle(40, 24.5, 5.5, HOLE) + circle(40, 24.5, 4.2, INK) +
            path("M32.5 42C32.5 36 35.5 32.5 40 32.5C44.5 32.5 48 36 48 42Z", INK))
    front = (circle(25, 22.5, 7.5, HOLE) + circle(25, 22.5, 6, INK) +
             path("M13 44C13 36 18 31.5 25 31.5C32 31.5 37 36 37 44Z", INK,
                  f' stroke="{HOLE}" stroke-width="2"'))
    return back + front


@reg("kadu", ORANGE_DEEP)
def kadu():
    pts = [pt(CX, CY, 17.5 if k % 2 == 0 else 13.5, -90 + 15 * k) for k in range(24)]
    sun = poly(pts, INK, 2) + circle(CX, CY, 12, HOLE) + circle(CX, CY, 10.3, INK)
    face = (circle(28, 27.5, 1.8, HOLE) + circle(36, 27.5, 1.8, HOLE) +
            stroke("M26.5 32.5C29.5 36.5 34.5 36.5 37.5 32.5", HOLE, 2.4))
    return sun + face


@reg("kahla", BLUE_DEEP)
def kahla():
    return path("M34 11C35.5 17 30.5 19.5 33 24.5C35 28.5 40.5 27 40.5 21C45.5 26.5 45.5 35 40.5 40.5"
                "C36.5 45 30 47.5 25 45.5C30 43.5 31.5 39.5 29 36.5C26.5 33.5 22.5 35.5 21 38.5"
                "C19 32 23 26 27.5 23C31 20.5 32.5 16.5 34 11Z", INK)


@reg("kaidan", DEEP_PURPLE_LIGHT)
def kaidan():
    bubble = rrect(14.5, 13, 35, 29, 14.5, INK) + poly([(19, 35), (16, 47), (29, 40)], INK, 2)
    lines = (rrect(22, 20, 20, 3.8, 1.9, HOLE) + rrect(20, 26, 24, 3.8, 1.9, HOLE) +
             circle(23, 34, 2, HOLE) + rrect(27, 32.1, 13, 3.8, 1.9, HOLE))
    return bubble + lines


@reg("kairo", YELLOW_DARK)
def kairo():
    front = poly([(19, 17), (33, 13), (33, 47), (19, 47)], INK, 2)
    side = poly([(33, 13), (45, 17), (45, 47), (33, 47)], YELLOW_DEEP, 2)
    return front + side


@reg("kaku", PINK_DARK)
def kaku():
    body = path("M14 32C18 23 28 20 36 25L44 17C47 23 47 37 44 43L36 35C28 40 18 39 14 32Z", INK)
    stripe = stroke("M27 23.5C25 28 25 33 27 37.5", HOLE, 2.6)
    eye = circle(21, 29.5, 2.2, HOLE)
    return body + stripe + eye


@reg("kalarm", RED)
def kalarm():
    bells = circle(19, 17, 6.5, INK) + circle(45, 17, 6.5, INK)
    legs = line(23, 43, 19.5, 47.5, INK, 3.2) + line(41, 43, 44.5, 47.5, INK, 3.2)
    body = circle(32, 31.5, 17, HOLE) + circle(32, 31.5, 15, INK)
    hands = stroke("M32 23V31.5L38 35.5", HOLE, 3.2)
    return bells + legs + body + hands


@reg("kali-dbpwaudit", BLUE_GREY)
def kali_dbpwaudit():
    dome = path("M19 31V26A13 13 0 0 1 45 26V31Z", INK)
    eye = circle(32, 24, 5.3, HOLE) + circle(32, 24, 2.7, BLUE)
    body = rrect(16, 32.5, 32, 16, 4, INK)
    dots = "".join(circle(x, 37, 1.7, HOLE) for x in (23, 29, 35, 41))
    key = circle(32, 42.5, 2, HOLE) + rrect(31, 42.5, 2, 3.5, .8, HOLE)
    return dome + eye + body + dots + key


@reg("kali-forensics-trans", AMBER_DEEP)
def kali_forensics():
    fingers = (line(23.5, 32, 17.5, 21, INK, 6) + line(28, 27, 24.5, 14, INK, 6) +
               line(34, 26.5, 34, 12.5, INK, 6) + line(39.5, 29, 42.5, 17, INK, 6) +
               line(40, 38, 47.5, 31, INK, 6))
    palm = path("M21 33C21 28 25 26 32 26C39 26 42 29 42 35C42 42 37 47.5 30.5 47.5"
                "C25 47.5 21 42 21 35Z", INK)
    return fingers + palm


@small("jpexs-decompiler")
def jpexs_s():
    return (stroke("M17 45V15H29M17 30H27", INK, 6) +
            stroke("M35 45V15H47M35 30H45", INK, 6))


@small("kaffeine")
def kaffeine_s():
    return (rrect(15, 14, 34, 7, 2.5, INK) + rrect(15, 24, 34, 23, 3.5, INK) +
            poly([(27, 29), (27, 42), (38.5, 35.5)], HOLE, 2))


@small("kali-dbpwaudit")
def kali_dbpwaudit_s():
    dome = path("M18 32V26A14 14 0 0 1 46 26V32Z", INK)
    eye = circle(32, 24, 6, HOLE) + circle(32, 24, 3.2, BLUE)
    return dome + eye + rrect(15, 33.5, 34, 15, 4, INK) + circle(32, 41, 3, HOLE)


@small("jmonkeyengine")
def jmonkey_s():
    ears = circle(16, 31, 6, INK) + circle(48, 31, 6, INK)
    head = circle(32, 30, 15.5, INK)
    face = circle(27, 28.5, 6.5, HOLE) + circle(37, 28.5, 6.5, HOLE) + ell_c(32, 37.5, 10.5, 6.5, HOLE)
    return ears + head + face + circle(27.5, 29, 2.6, INK) + circle(36.5, 29, 2.6, INK)


@small("jockey")
def jockey_s():
    return (rrect(15, 16, 34, 23, 3, INK) + rrect(28, 21.5, 11, 11, 1.5, HOLE) +
            "".join(rrect(x, 39, 5, 7, 1, INK) for x in (22, 30, 38)))


@small("kaidan")
def kaidan_s():
    bubble = rrect(14, 13, 36, 30, 15, INK) + poly([(19, 35), (16, 48), (30, 41)], INK, 2)
    return bubble + rrect(21, 22, 22, 5, 2.5, HOLE) + rrect(21, 30, 16, 5, 2.5, HOLE)


@small("josm")
def josm_s():
    m = poly([(15, 17), (25, 13), (38, 17), (48, 13), (48, 42), (38, 46), (25, 42), (15, 46)], INK, 2)
    return m + line(46, 14, 32, 35, AMBER_DEEP, 7, "butt")


@small("jamulus")
def jamulus_s():
    cloud = (circle(23, 33, 9, INK) + circle(34, 25, 11.5, INK) + circle(43, 34, 7.5, INK)
             + rrect(14, 33, 36, 10, 5, INK))
    return cloud + poly([(37, 15), (26, 32), (33, 32), (28.5, 45), (41, 27), (34, 27), (39, 15)], HOLE, 1.5)


@small("jasp")
def jasp_s():
    pts = [(36, 14), (45, 17), (34, 43), (21, 39)]
    d = "M" + "L".join(f"{x} {y}" for x, y in pts)
    return stroke(d, INK, 3.4) + "".join(circle(x, y, 4, INK) for x, y in pts)


@small("java")
def java_s():
    cup = path("M17 29H42V35C42 41 37.5 45 32 45H27C21.5 45 17 41 17 35Z", INK)
    return (cup + stroke("M42 32C48 32 48 41 41 41", INK, 3) +
            stroke("M30 25C26 21 34 19 30 13", INK, 3.4))


@small("jdeveloper")
def jdeveloper_s():
    return circle(CX, CY, 17, INK) + circle(37, 30, 11, HOLE) + circle(40.5, 30, 6, INK)


@small("jprofiler")
def jprofiler_s():
    return (circle(CX, CY, 17, INK) + circle(CX, CY, 12, HOLE) +
            poly([(28.5, 33), (35, 36), (41, 17)], INK, 2) + circle(32, 34, 4.5, RED))


@small("juci")
def juci_s():
    return (stroke("M27 18H17V42H27", INK, 6) + line(31, 30, 47, 30, INK, 5) +
            line(39, 22, 39, 38, INK, 5))


@small("k4dirstat")
def k4dirstat_s():
    return stroke("M20 20A15 15 0 1 1 18 38.5", INK, 5.5) + circle(32, 30, 8, INK)


@small("kadu")
def kadu_s():
    pts = [pt(CX, CY, 18 if k % 2 == 0 else 13, -90 + 22.5 * k) for k in range(16)]
    return poly(pts, INK, 2) + circle(CX, CY, 11.5, HOLE) + circle(CX, CY, 9.5, INK)


@small("kakoune")
def kakoune_s():
    d = g(rrect(16, 14, 32, 32, 6, INK), "rotate(45 32 30)")
    return d + stroke("M27 19V41M38.5 19L28 30.5L38.5 41", HOLE, 6)


@small("kalarm")
def kalarm_s():
    bells = circle(18, 16, 7, INK) + circle(46, 16, 7, INK)
    body = circle(32, 31.5, 18, HOLE) + circle(32, 31.5, 16, INK)
    return bells + body + stroke("M32 22V32L39 36", HOLE, 4)


@small("kaku")
def kaku_s():
    body = path("M13 32C17 22 28 19 36 24.5L46 15C49 23 49 38 46 45L36 35.5C28 41 17 40 13 32Z", INK)
    return body + circle(21, 29.5, 3, HOLE)


@small("jupyter")
def jupyter_s():
    top = path("M15 25C19 13 45 13 49 25C41 19.5 23 19.5 15 25Z", INK)
    bot = path("M15 35C19 47 45 47 49 35C41 40.5 23 40.5 15 35Z", INK)
    return top + bot + circle(47, 13, 3.5, INK)
