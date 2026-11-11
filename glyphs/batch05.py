# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 5: abbaye to albion-online."""
from lm import (
    AMBER_SOFT, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT,
    BROWN, BROWN_DARK, circle, cut, CX, CY, CYAN, CYAN_DARK, CYAN_DEEP, CYAN_LIGHT,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DEEP,
    INDIGO_SOFT, INK, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, LIGHT_BLUE_SOFT, line, ORANGE_DEEP,
    ORANGE_SOFT, path, PINK_LIGHT, poly, pt, PURPLE_DEEP, PURPLE_SOFT, RED, RED_DARK, RED_DEEP,
    RED_LIGHT, RED_SOFT, rrect, stroke, TEAL_DEEP, YELLOW,
)
from glyphs.kit import registry, ring_b

ICONS, SMALL, reg, small = registry()


@reg("abbaye", GREY_DARK)
def abbaye():
    arm = poly([(29, 30), (24.5, 13), (39.5, 13), (35, 30)], YELLOW, 2.5)
    return "".join(g(arm, f"rotate({90 * k} 32 30)") for k in range(4))


@reg("abe", ORANGE_DEEP)
def abe():
    face = path("M20 30H40L41 34L46.5 38.5L41 40V46H26C22 46 20 43 20 40Z", DEEP_ORANGE_SOFT)
    ear = path("M27 34.5C24 33.5 22 36 23.5 38.5C25 40.5 27.5 40 28.5 38.5Z", DEEP_ORANGE_DEEP)
    eye = circle(36, 34.5, 2.2, BROWN_DARK)
    helmet = path("M18 27C18 18 24 13 32 13C40 13 46 18 46 27Z", INK)
    brim = rrect(14.5, 25.5, 35, 5, 2.5, INK)
    return face + ear + eye + helmet + brim


@reg("acreloaded", RED_DEEP)
def acreloaded():
    top = poly([(29, 13), (43, 19), (29, 25.5), (15, 19)], INK, 2.5)
    left = poly([(15, 19), (29, 25.5), (29, 44), (15, 37.5)], RED_SOFT, 2.5)
    right = poly([(43, 19), (29, 25.5), (29, 44), (43, 37.5)], RED_LIGHT, 2.5)
    badge = rrect(33.5, 31.5, 16, 16, 4, INK, f' stroke="{HOLE}" stroke-width="2"')
    plus = line(41.5, 35, 41.5, 44, HOLE, 3.2) + line(37, 39.5, 46, 39.5, HOLE, 3.2)
    return top + left + right + badge + plus


@reg("adventure-capitalist", ORANGE_DEEP)
def adventure_capitalist():
    s = stroke("M43 19.5C41 16.5 37 15 32 15C25.5 15 21.5 18 21.5 22.5"
               "C21.5 31 42.5 28 42.5 37.5C42.5 42 38 45 31.5 45C26 45 22.5 43 20.5 40", INK, 5.5)
    bar = line(32, 11, 32, 49, AMBER_SOFT, 3, "round", f' stroke-linejoin="round"')
    return s + line(32, 11, 32, 49, HOLE, 6) + bar


@reg("adventures-of-shuggy", DEEP_PURPLE_LIGHT)
def shuggy():
    head = path("M18 12L25.5 20H38.5L46 12L47 30C47 38 41 44 32 45C23 44 17 38 17 30Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    wings = (poly([(17, 24), (12, 26), (13, 34), (17, 33)], DEEP_PURPLE_DEEP, 1.5) +
             poly([(47, 24), (52, 26), (51, 34), (47, 33)], DEEP_PURPLE_DEEP, 1.5))
    eyes = circle(26.5, 31, 5, LIGHT_BLUE_LIGHT) + circle(37.5, 31, 5, LIGHT_BLUE_LIGHT)
    fangs = (poly([(26.5, 40), (29.5, 40), (28, 44)], HOLE, 1) +
             poly([(34.5, 40), (37.5, 40), (36, 44)], HOLE, 1))
    return wings + head + eyes + fangs


@reg("age-of-empires-2", INDIGO_DEEP)
def aoe2():
    plume = path("M34 17C30 11 22 10 17.5 14C14 17.5 14 24 16 30C17 25 20 21.5 25 20.5"
                 "C27.5 20 30 20.5 32 22Z", INDIGO_SOFT)
    helmet = path("M24 38C24 26 28 17 34 16C41 17 45 26 46 38C43 40 39 41 35 40.5"
                  "C31 40 27 39.5 24 38Z", INK)
    slot = path("M37.5 23C40.5 24 42 28 41.5 32C39.5 31 38 28 37.5 23Z", HOLE)
    brim = stroke("M16 40C24 42 34 44 49 40", INK, 3.6)
    return plume + helmet + slot + brim


@reg("albion-online", DEEP_ORANGE_DEEP)
def albion():
    pommel = rrect(25, 11, 14, 5, 2.5, INK)
    grip = rrect(28.5, 15, 7, 8, 0, DEEP_ORANGE_SOFT)
    guard = rrect(15, 22, 34, 6.5, 3.25, INK)
    blade = path("M26.5 29H37.5V41L32 48L26.5 41Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return pommel + grip + guard + blade


@reg("alan-wake", BLUE_GREY_DARK)
def alan_wake():
    beam = path("M24 12H40L47 45C47.3 46.6 46.3 48 44.7 48H19.3C17.7 48 16.7 46.6 17 45Z", INK)
    man = (circle(31.5, 21, 3, HOLE) +
           path("M27.5 25.5H35.5L36.5 36H34.5L35 46H32.3L31.5 38L30.7 46H28L28.5 36H26.5Z", HOLE,
                f' stroke="{HOLE}" stroke-width="1" stroke-linejoin="round"'))
    return beam + man


@reg("airstrike", RED_DEEP)
def airstrike():
    balloon = path("M32 11C41.5 11 47 17.5 47 25C47 31 42 35 38.5 38H25.5C22 35 17 31 17 25"
                   "C17 17.5 22.5 11 32 11Z", INK)
    stripes = (path("M32 11C27 11 25 18 25 25C25 31 27 35 28.5 38H35.5C37 35 39 31 39 25"
                    "C39 18 37 11 32 11Z", HOLE))
    mid = path("M32 11C30 12 29.5 18 29.5 25C29.5 31 30.5 35 31 38H33C33.5 35 34.5 31 34.5 25"
               "C34.5 18 34 12 32 11Z", INK)
    ropes = line(26.5, 38, 28, 42, INK, 1.8) + line(37.5, 38, 36, 42, INK, 1.8)
    basket = path("M25.5 41.5H38.5L37 48H27Z", INK,
                  f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return balloon + stripes + mid + ropes + basket


@reg("abdownloadmanager", DEEP_PURPLE_DEEP)
def abdownloadmanager():
    bowl = path("M15 30A17 17 0 0 0 49 30H43.5A11.5 11.5 0 0 1 20.5 30Z", INK)
    fill = path("M22 34C26 32 30 36 34 34C37 32.5 40 33 42 34.5A10.5 10.5 0 0 1 22 34Z", DEEP_PURPLE_SOFT)
    arrow = line(32, 13, 32, 29, INK, 3.6) + stroke("M26 23.5L32 29.5L38 23.5", INK, 3.6)
    return _dash_top() + bowl + fill + arrow


def _dash_top():
    out = ""
    for k in range(5):
        a = 200 + 35 * k
        x0, y0 = pt(CX, CY, 15.5, a - 7)
        x1, y1 = pt(CX, CY, 15.5, a + 7)
        out += stroke(f"M{f(x0)} {f(y0)}A15.5 15.5 0 0 1 {f(x1)} {f(y1)}", INK, 3)
    return out


@reg("abiword", BLUE_DEEP)
def abiword():
    return path("M14.5 46C20 32 30 18 42 12.5C44 11.8 45.5 12.5 45.8 14.5L49.5 46H42.5"
                "L39.3 22C31 27.5 25.5 36 22 46Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')


@reg("abricotine", DEEP_ORANGE_LIGHT)
def abricotine():
    return (line(35, 12, 31, 48, INK, 4.2, "butt") +
            line(46, 19, 17, 41, INK, 4.2, "butt") +
            line(16, 25, 46, 39, INK, 4.2, "butt"))


@reg("abrowser", BLUE_DEEP)
def abrowser():
    globe = circle(33.5, 28, 15, INK)
    grid = (f'<ellipse cx="33.5" cy="28" rx="6.5" ry="15" fill="none" stroke="{HOLE}" stroke-width="2"/>'
            + line(18.5, 28, 48.5, 28, HOLE, 2, "butt")
            + stroke("M21 20H46M21 36H46", HOLE, 2))
    cursor = poly([(15, 30), (30, 38.5), (24, 40.5), (21.5, 47)], INK, 2)
    cursor_edge = poly([(15, 30), (30, 38.5), (24, 40.5), (21.5, 47)], HOLE, 6.5)
    return globe + grid + cursor_edge + cursor


@reg("acestream", LIGHT_BLUE_DEEP)
def acestream():
    return (circle(CX, CY, 16.5, INK) + ring_b(CX, CY, 13.2, HOLE, 2) +
            poly([(28, 22.5), (39.5, 30), (28, 37.5)], HOLE, 2.5))


@reg("acetoneiso", PURPLE_DEEP)
def acetoneiso():
    cd = circle(29, 28, 15.5, INK) + circle(29, 28, 5.5, HOLE) + circle(29, 28, 2.4, INK)
    badge = circle(41.5, 40, 9.5, HOLE)
    arrow = (stroke("M45.5 40A4.2 4.2 0 1 1 42.5 36", INK, 2.6) +
             poly([(41.2, 33), (45.5, 36), (41.2, 39)], INK, 1.2))
    return cd + badge + circle(41.5, 40, 7.5, PURPLE_SOFT) + arrow


@reg("acroread", RED_DEEP)
def acroread():
    return stroke("M16.5 43.5C22 39 27 31.5 30 24C32 18.5 31.5 14 29.5 14C27.5 14 27 18 28.5 22.5"
                  "C31 30 37.5 37.5 44 40C47.5 41.3 48.5 39.5 46.5 38C43 35.5 34 35 26.5 38"
                  "C21 40 17 42.5 16.5 43.5Z", INK, 3.4)


@reg("actionaz", CYAN_DEEP)
def actionaz():
    frame = stroke("M26 40H21A6 6 0 0 1 15 34V19A6 6 0 0 1 21 13H43A6 6 0 0 1 49 19V34"
                   "A6 6 0 0 1 43 40H38", INK, 5.5)
    a = path("M29.5 22H34.5L44.5 48H39.5L32 28.5L24.5 48H19.5Z", INK,
             f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    edge = path("M29.5 22H34.5L44.5 48H39.5L32 28.5L24.5 48H19.5Z", HOLE,
                f' stroke="{HOLE}" stroke-width="5.5" stroke-linejoin="round"')
    return frame + edge + a


@reg("activitywatch", GREY_DARK)
def activitywatch():
    a = stroke("M17 30L23 14L29 30M19.5 24H26.5", INK, 3)
    w = stroke("M33 32L36.5 46L40.5 37L44.5 46L48 32", INK, 3)
    hand = line(17, 45, 46, 15, INK, 2.4)
    return a + w + hand + circle(CX, CY, 3.6, INK)


@reg("advanced-rest-client", LIGHT_BLUE_DEEP)
def arc():
    up = poly([(25, 11.5), (36, 24), (30, 24), (30, 47), (20, 47), (20, 24), (14, 24)], INK, 2)
    down = poly([(40.5, 47.5), (50, 36.5), (44.5, 36.5), (44.5, 24), (36.5, 24), (36.5, 36.5), (31, 36.5)],
                LIGHT_BLUE_SOFT, 2)
    return up + down


@reg("advert-block", RED)
def advert_block():
    return circle(CX, CY, 16.5, INK) + rrect(20, 26.5, 24, 7, 1.5, HOLE)


@reg("aegisub", RED_DEEP)
def aegisub():
    hexa = poly([pt(CX, CY, 17, -90 + 60 * k) for k in range(6)], RED_DARK, 3)
    eye = path("M14 30C19 22 25 19 32 19C39 19 45 22 50 30C45 38 39 41 32 41C25 41 19 38 14 30Z", INK)
    return hexa + eye + circle(CX, CY, 7.5, HOLE) + circle(CX, CY, 3.6, INK)


@reg("aeskulap", INDIGO)
def aeskulap():
    rod = line(32, 16, 32, 48, INK, 3)
    knob = circle(32, 14, 3, INK)
    wings = (path("M30 19C26 14 20 14 15 16C19 17 21 19 22 21C24 22 27 22 30 21.5Z", INK) +
             path("M34 19C38 14 44 14 49 16C45 17 43 19 42 21C40 22 37 22 34 21.5Z", INK))
    snake = stroke("M27 25C33 22.5 39.5 25 37.5 28.5C35.5 31.5 27 31 26 35C25 39 38 38 38 42"
                   "C38 44.5 34.5 45.5 32 45", INK, 2.6)
    return wings + knob + rod + snake


@reg("afl", CYAN_DEEP)
def afl():
    ears = (path("M22 31C17 24 14 15 15.5 11C19 11 25 18 28.5 27Z", INK) +
            path("M42 31C47 24 50 15 48.5 11C45 11 39 18 35.5 27Z", INK))
    inner = (path("M22 26C19.5 21 18 16.5 18.5 14.5C20.5 15.5 23.5 19.5 25.5 24Z", HOLE) +
             path("M42 26C44.5 21 46 16.5 45.5 14.5C43.5 15.5 40.5 19.5 38.5 24Z", HOLE))
    head = path("M32 25C41 25 46 30 46 37C46 44 40 48 32 48C24 48 18 44 18 37C18 30 23 25 32 25Z", INK)
    face = (circle(26.5, 34.5, 2.2, HOLE) + circle(37.5, 34.5, 2.2, HOLE) +
            path("M29 39.5H35L32 42.5Z", PINK_LIGHT, f' stroke="{PINK_LIGHT}" stroke-width="1.5" stroke-linejoin="round"'))
    return ears + inner + head + face


@reg("agave", GREY_DEEP)
def agave():
    def leaf(deg, length, colour):
        d = (f"M32 45C27 {45 - length * .5} 28.5 {45 - length * .8} 32 {45 - length}"
             f"C35.5 {45 - length * .8} 37 {45 - length * .5} 32 45Z")
        return g(path(d, colour, f' stroke="{HOLE}" stroke-width="1.4"'), f"rotate({deg} 32 45)")
    return (leaf(-66, 25, GREY_SOFT) + leaf(66, 25, GREY_SOFT) +
            leaf(-33, 30, INK) + leaf(33, 30, INK) + leaf(0, 33, INK))


@reg("agent", BLUE_DEEP)
def agent():
    return (circle(CX, CY, 16.5, INK) + circle(32, 20.5, 2.8, HOLE) +
            rrect(29.3, 25.5, 5.4, 16, 2.7, HOLE))


@reg("agentdesktop", PURPLE_SOFT)
def agentdesktop():
    bubble = path("M32 13A16.5 16.5 0 1 1 22.5 43.5L15 46.5L17.5 38.5A16.5 16.5 0 0 1 32 13Z", INK)
    at = (ring_b(32, 29.5, 5, HOLE, 3) +
          stroke("M37 25V32.5C37 35 38.5 36 40 36C42 36 43.5 34 43.5 29.5"
                 "A11.5 11.5 0 1 0 38 39.3", HOLE, 3))
    return bubble + at


@reg("agordejo", GREY_DARK)
def agordejo():
    flag = path("M24 11H40L46 48L32 40L18 48Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return flag + poly([(32, 19), (36, 26.5), (32, 34), (28, 26.5)], HOLE, 1.5)


def _aimp(inner):
    return circle(CX, CY, 16.5, INK) + inner


@reg("aimp", ORANGE_DEEP)
def aimp():
    tri = cut("M32 18L44 40H20Z" + "M32 26.5L37.3 36H26.7Z", HOLE)
    gap = rrect(33, 36, 4.5, 5, 0, INK)
    return _aimp(g(tri + gap, "translate(0 -1)"))


@reg("aimp-ac", ORANGE_DEEP)
def aimp_ac():
    arrow = (poly([(21.5, 20.5), (34, 20.5), (21.5, 33)], HOLE, 2.5) +
             line(26, 25, 41, 40, HOLE, 5))
    return _aimp(arrow)


@reg("aimp-ate", ORANGE_DEEP)
def aimp_ate():
    pencil = g(rrect(28.5, 17, 7, 20, 1.5, HOLE) +
               poly([(28.5, 38.5), (35.5, 38.5), (32, 44)], HOLE, 1.5),
               "rotate(45 32 30)")
    return _aimp(pencil)


@reg("air", RED_DEEP)
def air():
    blob = path("M30 13C35 11 38 14 38 18C38 22 43 26 46.5 32C49 37 47 43 42 42C37 41 33 37 27 39"
                "C21 41 16 40 16 36C16 32 22 29 24 24C26 19 26 15 30 13Z", INK)
    return blob + circle(33, 30, 5.2, HOLE)


@reg("aircrack-ng", LIGHT_BLUE_DEEP)
def aircrack():
    bolt = poly([(49.5, 13), (24.5, 29.5), (33, 31.5), (14.5, 47.5), (40.5, 30), (32, 28.5)], INK, 3)
    wifi = (stroke("M17 22A13 13 0 0 1 33 18", INK, 3) +
            stroke("M20.5 27A8 8 0 0 1 30 24.5", INK, 3) +
            circle(25.5, 31, 2.2, INK))
    return g(bolt, "translate(0 0)") + wifi


@reg("airtame-application", BLUE_DEEP)
def airtame():
    return (stroke("M18 24.5C22 20.5 26 20.5 32 24C38 27.5 42 27.5 46 23.5", INK, 4.4) +
            stroke("M18 36.5C22 32.5 26 32.5 32 36C38 39.5 42 39.5 46 35.5", INK, 4.4))


@reg("airvpn", CYAN_DARK)
def airvpn():
    outer = path("M20 44A8.5 8.5 0 0 1 18.5 27.2A11 11 0 0 1 39 21.5A9.5 9.5 0 0 1 45 44Z", INK)
    inner = path("M23.5 38.5A4.5 4.5 0 0 1 23 29.6A7 7 0 0 1 36 27A5.8 5.8 0 0 1 40.5 38.5Z", CYAN_LIGHT)
    return outer + inner


@reg("airwave-manager", RED_DEEP)
def airwave():
    prongs = rrect(22.5, 12, 5, 16, 2, INK) + rrect(36.5, 12, 5, 16, 2, INK)
    body = rrect(17, 25, 30, 22, 4, INK)
    return prongs + body + rrect(26, 34, 12, 3.4, 1.7, HOLE)


@reg("akira", DEEP_ORANGE_DEEP)
def akira():
    top = poly([(32, 12), (45, 45), (34, 36.5)], INK, 2.5)
    left = poly([(32, 12), (34, 36.5), (19, 45)], DEEP_ORANGE_SOFT, 2.5)
    wedge = poly([(22, 34), (43, 30), (19, 45)], AMBER_SOFT, 2.5)
    return top + left + wedge


@reg("akonaditray", BLUE_DEEP)
def akonaditray():
    disc = circle(31, 30, 16, INK)
    wave = path("M13 30C20 26 34 26 50 32C49 41 41 47 31 47C21 47 14 40 13 30Z", BLUE_SOFT)
    crest = path("M31 14C24 17 22 24 22.5 27.5C25 27 27.5 26.8 30 26.8C29 22 29 17 31 14Z", BLUE_SOFT)
    return disc + wave


def _rss(arc_colour):
    return (circle(21, 40, 4, INK) +
            stroke("M18.5 28.5A13 13 0 0 1 32.5 42.5", arc_colour, 4.6) +
            stroke("M18.5 18A23.5 23.5 0 0 1 43 42.5", arc_colour, 4.6))


@reg("akregator", ORANGE_DEEP)
def akregator():
    return _rss(INK)


@reg("akregator_empty", ORANGE_DEEP)
def akregator_empty():
    return _rss(ORANGE_SOFT)


@reg("albert", CYAN_DARK)
def albert():
    return stroke("M47 20C41 22 38 32 33 36.5C29.5 40 24 41 20.5 38.5C17 36 17.5 30 21 26"
                  "C25 22 30 23.5 33 28C36 32.5 39 39 47 40", INK, 4)


@reg("accerciser", RED_DEEP)
def accerciser():
    bar = rrect(13, 27.5, 38, 5, 2.5, BLUE_LIGHT)
    plates = (rrect(19.5, 12, 8, 36, 4, INK) + rrect(36.5, 12, 8, 36, 4, INK) +
              rrect(14.5, 19, 4, 22, 2, INK) + rrect(45.5, 19, 4, 22, 2, INK))
    return bar + plates


@reg("accessories-calculator", BLUE_GREY)
def calculator():
    plus = line(22, 15.5, 22, 26.5, INK, 3.4) + line(16.5, 21, 27.5, 21, INK, 3.4)
    minus = line(36.5, 21, 47.5, 21, INK, 3.4)
    times = line(18, 35, 26, 43, INK, 3.4) + line(26, 35, 18, 43, INK, 3.4)
    eq = circle(42, 39, 8.5, INK) + rrect(37.5, 35.2, 9, 2.6, 1.3, HOLE) + rrect(37.5, 40.2, 9, 2.6, 1.3, HOLE)
    return plus + minus + times + eq


@reg("accessories-camera", BLUE_GREY_DARK)
def camera():
    head = circle(32, 27, 15, INK) + circle(32, 27, 9.5, HOLE) + circle(32, 27, 6, CYAN)
    stand = path("M26 41H38L41 47H23Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return stand + head + circle(29.5, 24.5, 1.8, INK)


@reg("accessories-character-map", BLUE_GREY)
def charmap():
    back = rrect(30, 12, 19, 22, 3.5, BLUE_GREY_SOFT) + circle(36, 18, 1.8, HOLE) + circle(43, 18, 1.8, HOLE)
    front = rrect(15, 22, 23, 26, 4, INK, f' stroke="{HOLE}" stroke-width="2"')
    a = (ring_b(25.5, 38.5, 4.2, HOLE, 2.8) + line(29.7, 34, 29.7, 43, HOLE, 2.8) +
         line(22.5, 27, 26, 30, HOLE, 2.6))
    return back + front + a


def _book(ribbon_x):
    book = rrect(17, 12, 30, 36, 4, INK)
    spine = rrect(21, 12, 2.4, 36, 0, HOLE)
    ribbon = path(f"M{ribbon_x} 12H{ribbon_x + 6}V27L{ribbon_x + 3} 24L{ribbon_x} 27Z", HOLE)
    return book + spine + ribbon


@reg("accessories-dictionary", RED_DEEP)
def dictionary():
    return _book(27)


@reg("accessories-ebook-reader", TEAL_DEEP)
def ebook():
    return _book(36)


@reg("accessories-notes", BROWN)
def notes():
    paper = rrect(18, 14, 28, 34, 3.5, INK)
    clip = rrect(24.5, 11, 15, 7, 3, BROWN_DARK) + circle(32, 13.5, 1.5, INK)
    lines = "".join(rrect(23, y, w, 2.6, 1.3, HOLE) for y, w in
                    [(24, 18), (29.5, 18), (35, 18), (40.5, 11)])
    return paper + clip + lines


@reg("accessories-safe", GREY_DARK)
def safe():
    body = rrect(15, 13, 34, 34, 5, INK)
    door = rrect(21, 17.5, 24, 25, 3, HOLE)
    dial = circle(33, 30, 7.5, INK) + circle(33, 30, 3, HOLE)
    hinges = rrect(17, 20, 2.4, 5, 1.2, HOLE) + rrect(17, 35, 2.4, 5, 1.2, HOLE)
    return body + door + dial + hinges


@reg("accessories-text-editor", BLUE_GREY)
def text_editor():
    sheet = rrect(16, 12, 26, 34, 3.5, INK)
    lines = "".join(rrect(20.5, y, w, 2.6, 1.3, HOLE) for y, w in
                    [(18, 17), (23.5, 17), (29, 17), (34.5, 10)])
    pencil = g(rrect(40, 20, 7, 21, 1.5, RED) +
               poly([(40, 42.5), (47, 42.5), (43.5, 48)], INK, 1.5) +
               rrect(40, 20, 7, 3.5, 1.5, INK),
               "rotate(40 43.5 34)")
    edge = g(rrect(40, 20, 7, 28, 2, HOLE, f' stroke="{HOLE}" stroke-width="4" stroke-linejoin="round"'),
             "rotate(40 43.5 34)")
    return sheet + lines + edge + pencil


@reg("administration", BLUE_GREY_DARK)
def administration():
    wrench = (line(26, 26, 43, 43, BLUE_GREY_SOFT, 4.4) + circle(22.5, 22.5, 7, BLUE_GREY_SOFT) +
              poly([(22.5, 22.5), (13.5, 20), (20, 13.5)], HOLE, 0))
    hammer = (line(21, 43, 38.5, 25.5, INK, 4) +
              g(rrect(33, 14, 18, 7.5, 2, INK), "rotate(45 42 17.75)"))
    return wrench + hammer


@small("abdownloadmanager")
def abdownloadmanager_s():
    bowl = path("M14 29A18 18 0 0 0 50 29H43A11 11 0 0 1 21 29Z", INK)
    arrow = line(32, 12, 32, 29, INK, 5) + stroke("M24.5 22L32 29.5L39.5 22", INK, 5)
    return bowl + arrow


@small("abrowser")
def abrowser_s():
    globe = circle(33.5, 28, 15, INK)
    grid = f'<ellipse cx="33.5" cy="28" rx="6.5" ry="15" fill="none" stroke="{HOLE}" stroke-width="3.2"/>'
    cur = [(14, 29), (31, 38.5), (24, 41), (21.5, 48)]
    return globe + grid + poly(cur, HOLE, 7) + poly(cur, INK, 2)


@small("accessories-character-map")
def charmap_s():
    back = rrect(29, 11, 21, 22, 4, BLUE_GREY_SOFT)
    front = rrect(14, 21, 26, 28, 4.5, INK, f' stroke="{HOLE}" stroke-width="2.5"')
    a = ring_b(25, 38, 5, HOLE, 3.6) + line(30, 32.5, 30, 43.5, HOLE, 3.6)
    return back + front + a


@small("acestream")
def acestream_s():
    return circle(CX, CY, 17, INK) + poly([(27, 21), (41, 30), (27, 39)], HOLE, 3)


@small("acetoneiso")
def acetoneiso_s():
    cd = circle(29, 28, 16, INK) + circle(29, 28, 5.5, HOLE)
    badge = circle(42, 40, 10, HOLE) + circle(42, 40, 8, PURPLE_SOFT)
    return cd + badge + stroke("M46 40A4.5 4.5 0 1 1 42 35.5", INK, 3.4)


@small("activitywatch")
def activitywatch_s():
    a = stroke("M16 30L22.5 13L29 30", INK, 4)
    w = stroke("M33 32L37 47L41 38L45 47L49 32", INK, 4)
    return a + w + line(17, 45, 46, 15, INK, 3)


@small("agentdesktop")
def agentdesktop_s():
    bubble = path("M32 12A17 17 0 1 1 22.5 44L14.5 47L17 38.5A17 17 0 0 1 32 12Z", INK)
    return bubble + ring_b(32, 29.5, 6.5, HOLE, 4.2)


@small("aeskulap")
def aeskulap_s():
    wings = (path("M30 20C26 13 19 13 13.5 15.5C18 17 20 20 21 23H30Z", INK) +
             path("M34 20C38 13 45 13 50.5 15.5C46 17 44 20 43 23H34Z", INK))
    snake = stroke("M25 26.5C35 24 42 28 37 32C33 35 25 34 25 39C25 43 34 42 37 45", INK, 3.6)
    return wings + line(32, 12, 32, 48, INK, 4) + snake


@small("agave")
def agave_s():
    def leaf(deg, length):
        d = (f"M32 46C25 {46 - length * .5} 27.5 {46 - length * .8} 32 {46 - length}"
             f"C36.5 {46 - length * .8} 39 {46 - length * .5} 32 46Z")
        return g(path(d, INK), f"rotate({deg} 32 46)")
    return leaf(-55, 26) + leaf(55, 26) + leaf(0, 34)


@small("alan-wake")
def alan_wake_s():
    beam = path("M23 11H41L48 45C48.3 46.6 47.3 48 45.7 48H18.3C16.7 48 15.7 46.6 16 45Z", INK)
    man = circle(32, 20.5, 4, HOLE) + rrect(27, 26, 10, 22, 2.5, HOLE)
    return beam + man


@small("accessories-text-editor")
def text_editor_s():
    sheet = rrect(15, 11, 28, 36, 4, INK)
    lines = "".join(rrect(20, y, w, 4, 2, HOLE) for y, w in [(18, 18), (26, 18), (34, 11)])
    pencil = g(rrect(39.5, 20, 9, 22, 2, RED) +
               poly([(39.5, 43), (48.5, 43), (44, 49)], INK, 1.5), "rotate(40 44 34)")
    edge = g(rrect(39.5, 20, 9, 29, 2, HOLE, f' stroke="{HOLE}" stroke-width="4.5" stroke-linejoin="round"'),
             "rotate(40 44 34)")
    return sheet + lines + edge + pencil


@small("accessories-notes")
def notes_s():
    paper = rrect(17, 13, 30, 36, 4, INK)
    clip = rrect(24, 10, 16, 7.5, 3, BROWN_DARK)
    lines = "".join(rrect(22, y, w, 4, 2, HOLE) for y, w in [(23, 20), (31, 20), (39, 13)])
    return paper + clip + lines


@small("administration")
def administration_s():
    wrench = (line(26, 26, 44, 44, BLUE_GREY_SOFT, 5.5) + circle(22, 22, 8, BLUE_GREY_SOFT) +
              poly([(22, 22), (12, 19), (19, 12)], HOLE, 0))
    hammer = (line(20, 44, 38.5, 25.5, INK, 5.5) +
              g(rrect(32, 13, 20, 9, 2.5, INK), "rotate(45 42 17.5)"))
    return wrench + hammer
