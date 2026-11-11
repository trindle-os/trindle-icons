# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 33: gummi to hoppscotch.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER_DARK, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, BROWN, BROWN_DARK, circle, CX, CY, CYAN, CYAN_DARK, CYAN_DEEP,
    DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP,
    INDIGO_SOFT, INK, LIGHT_BLUE_DEEP, line, ORANGE, ORANGE_DEEP, ORANGE_SOFT, path, PINK_LIGHT,
    poly, pt, PURPLE, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_SOFT, rrect, stroke, TEAL,
    TEAL_DEEP, TEAL_SOFT, YELLOW,
)
from glyphs.kit import arc_c, registry, _ring

ICONS, SMALL, reg, small = registry()


def _lambda():
    lam = stroke("M24.5 19H28.5L39 41", INK, 4.6) + stroke("M31.8 27.5L25.5 41", INK, 4.6)
    return _ring(CX, CY, 16, INK, 3.4) + g(lam, "translate(32 30.5) scale(.78) translate(-31.8 -30)")


def _two(body):
    badge = (circle(42.5, 40.5, 10, HOLE) + circle(42.5, 40.5, 8.3, INK) +
             stroke("M39.4 37.6C39.4 35.9 40.8 34.8 42.5 34.8C44.3 34.8 45.5 35.9 45.5 37.4"
                    "C45.5 40 40 42.3 39.3 46.2H45.8", HOLE, 2.4))
    return g(body, "translate(29 27) scale(.86) translate(-32 -30)") + badge


@reg("half-life-blue-shift", BLUE)
@reg("half-life-deathmatch", BROWN)
@reg("half-life-opposing-force", PURPLE_SOFT)
@reg("half-life", ORANGE_DEEP)
def half_life():
    return _lambda()


@reg("half-life2-deathmatch", BROWN)
@reg("half-life2-lost-coast", BLUE_DARK)
@reg("half-life2", ORANGE_DEEP)
def half_life2():
    return _two(_lambda())


@reg("half-life-alyx", DEEP_ORANGE_DARK)
def half_life_alyx():
    return stroke("M20 17H25.5L32.5 31", INK, 4.6) + stroke("M44 16L30.5 44H25", INK, 4.6)


@reg("gummi", CYAN_DEEP)
def gummi():
    return stroke("M42.5 20.5A13.5 13.5 0 1 0 45.5 30.5H34", INK, 6)


@reg("guvcview", GREY_DARK)
def guvcview():
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 10.5, HOLE) +
            circle(CX, CY, 6.5, GREY_SOFT) + circle(29.5, 27.5, 2, INK))


@reg("gweled", LIGHT_BLUE_DEEP)
def gweled():
    gem = poly([(22, 14), (42, 14), (49, 22), (32, 46.5), (15, 22)], INK, 2.5)
    cuts = (stroke("M16 22H48", HOLE, 1.8) + stroke("M26.5 22L32 44L37.5 22", HOLE, 1.8) +
            stroke("M22.5 15L26.5 22L32 15L37.5 22L41.5 15", HOLE, 1.8))
    return gem + cuts


@reg("gwenview", PINK_LIGHT)
def gwenview():
    eye = path("M12.5 30C17.5 20.5 24.5 15.5 32 15.5C39.5 15.5 46.5 20.5 51.5 30"
               "C46.5 39.5 39.5 44.5 32 44.5C24.5 44.5 17.5 39.5 12.5 30Z", INK)
    pic = circle(CX, CY, 10.5, HOLE)
    hills = poly([(23.5, 36), (29, 28.5), (32.5, 32), (35.5, 28), (40.5, 36)], INK, 2)
    return eye + pic + hills + circle(35.5, 24.5, 2, INK)


@reg("gzdoom", INDIGO)
def gzdoom():
    gg = stroke("M27.5 24.3A7.8 7.8 0 1 0 29.8 30.5H23.5", INDIGO_SOFT, 4.6)
    z = stroke("M35 22H46L35 38.5H46", INK, 4.6)
    return gg + z


@reg("hacknet", ORANGE_DEEP)
def hacknet():
    out = arc_c(CX, CY, 15.5, -70, 110, INK, 3.4) + arc_c(CX, CY, 15.5, 140, 250, INK, 3.4)
    out += arc_c(CX, CY, 10, 160, 380, INK, 3) + arc_c(CX, CY, 10, 60, 120, INK, 3)
    return out + _ring(CX, CY, 4.8, INK, 2.8) + circle(CX, CY, 1.6, INK)


@reg("haguichi", RED)
def haguichi():
    return line(25, 30, 40.5, 45, RED_SOFT, 7.5) + line(40.5, 15, 25, 30, INK, 7.5)


@reg("hakuneko-desktop", DEEP_ORANGE_SOFT)
def hakuneko():
    iris = circle(33, 32, 9.5, DEEP_PURPLE) + circle(33, 32, 4, INK)
    lash = stroke("M13.5 28C19 19.5 28 16 38 18.5C43 19.8 47 22.8 50 27", INK, 4.6)
    lid = stroke("M22 41C27.5 44 37.5 44.5 44 40", INK, 2.4)
    return iris + lash + lid


@reg("hamster", BLUE_DARK)
def hamster():
    teeth = "".join(g(rrect(29.5, 11.5, 5, 5, 1.5, INK), f"rotate({45 * k} 32 30)")
                    for k in range(8))
    return (teeth + circle(CX, CY, 13.5, INK) + circle(CX, CY, 9.5, HOLE) +
            line(24.5, 36, 39.5, 24, INK, 3.4))


@reg("harbour-pure-maps", BLUE_DEEP)
def pure_maps():
    drop = circle(30.5, 31.5, 15, INK) + rrect(30.5, 14.5, 17, 17, 3.5, INK)
    return drop + circle(30.5, 31.5, 8.5, HOLE) + circle(30.5, 31.5, 4.5, INK)


@reg("hardinfo2", BLUE_GREY_DEEP)
def hardinfo2():
    segs = "".join(arc_c(32, 36, 17, 190 + 28 * k, 190 + 28 * k + 21, INK, 5.5) for k in range(6))
    return segs + line(32, 36, 42.5, 22.5, INK, 3.6) + circle(32, 36, 4.5, INK)


@reg("harmonoid", DEEP_PURPLE)
def harmonoid():
    frame = (f'<rect x="19.5" y="13" width="25" height="34" rx="4.5" fill="none" '
             f'stroke="{INK}" stroke-width="3.6"/>')
    return frame + circle(32, 21.5, 3.8, INK) + _ring(32, 36, 5.8, INK, 3.4)


@reg("harmony", PINK_LIGHT)
def harmony():
    return (stroke("M27 16L23.5 44", INK, 5.4) + stroke("M41 16L37.5 44", INK, 5.4) +
            stroke("M25.5 30.5H39", INK, 5))


@reg("haroopad", BLUE_DEEP)
def haroopad():
    crest = poly([(22, 17), (25, 10), (28.5, 16), (32, 10), (35, 17)], INK, 2)
    head = path("M28.5 15C37 15 41 21.5 41 29C41 38 36 45.5 28.5 45.5C21 45.5 16 38 16 29"
                "C16 21.5 20 15 28.5 15Z", INK)
    eyes = (circle(23.3, 27, 4.6, HOLE) + circle(33.7, 27, 4.6, HOLE) +
            circle(23.8, 27.5, 2.2, INK) + circle(33.2, 27.5, 2.2, INK))
    beak = poly([(25, 33), (32, 33), (28.5, 38.5)], HOLE, 2)
    hash_ = (line(44.5, 30, 43, 43, INK, 2.4) + line(49.5, 30, 48, 43, INK, 2.4) +
             line(41.5, 34, 51, 34, INK, 2.4) + line(41, 39.5, 50.5, 39.5, INK, 2.4))
    return crest + head + eyes + beak + hash_


@reg("haruna", GREY_DARK)
def haruna():
    strip = rrect(16, 13, 32, 34, 3.5, INK)
    holes = "".join(rrect(x, y, 3.2, 3.6, 1, HOLE) for x in (18.5, 42.3)
                    for y in (16, 22.5, 29, 35.5, 42))
    h = (rrect(24.5, 16, 5, 28, 1.5, HOLE) + rrect(34.5, 16, 5, 28, 1.5, HOLE) +
         rrect(24.5, 27.3, 15, 5.4, 1, HOLE))
    return strip + holes + h


@reg("hashit", LIGHT_BLUE_DEEP)
def hashit():
    return (line(28, 15, 25, 45, INK, 5) + line(40, 15, 37, 45, INK, 5) +
            line(17.5, 24, 46.5, 24, INK, 5) + line(17.5, 36, 46.5, 36, INK, 5))


@reg("hatari", CYAN_DARK)
def hatari():
    return (rrect(16, 13, 9.5, 34, 2, INK) + rrect(38.5, 13, 9.5, 34, 2, INK) +
            rrect(16, 26, 32, 8, 1.5, INK))


@reg("hb-icon", AMBER_DARK)
def hb_icon():
    glass = (poly([(13.5, 18), (31, 18), (22.2, 29)], INK, 2.2) +
             line(22.2, 28, 22.2, 43, INK, 2.6) + line(17, 44.5, 27.5, 44.5, INK, 3))
    fruit = f'<ellipse cx="39" cy="37" rx="8.5" ry="10.5" fill="{INK}"/>'
    hatch = (line(33, 32, 43, 44, HOLE, 1.6) + line(34, 28, 46.5, 42.5, HOLE, 1.6) +
             line(45, 32, 35, 44, HOLE, 1.6) + line(44, 28, 31.5, 42.5, HOLE, 1.6))
    leaves = poly([(39, 27), (33.5, 17), (37.5, 21), (39, 12), (40.5, 21), (45, 16), (42, 27)], INK, 1.6)
    return glass + leaves + fruit + hatch


@reg("hdajackretask", BLUE_GREY)
def hdajackretask():
    dots = "".join(circle(x, y, 3.8, INK) for x in (19.5, 44.5) for y in (18, 30, 42))
    wires = line(19.5, 18, 44.5, 30, INK, 2.6) + line(19.5, 42, 44.5, 18, INK, 2.6)
    return wires + dots


@reg("hdspconf", RED_DEEP)
def hdspconf():
    handle = line(31, 29, 46, 45, INK, 4.6)
    head = g(rrect(15, 20, 23, 10, 3, INK), "rotate(-45 26.5 25)")
    led = line(21.5, 29, 30.5, 20, HOLE, 2, "butt", ' stroke-dasharray="2 1.6"')
    return handle + head + led


@reg("hdspmixer", TEAL_DEEP)
def hdspmixer():
    out = ""
    for x, y in [(21.5, 22), (32, 35), (42.5, 26)]:
        out += line(x, 14, x, 46, INK, 2.6) + rrect(x - 5, y - 3, 10, 6, 2, INK)
    return out


@reg("headset", CYAN_DEEP)
def headset():
    return stroke("M13 30H18L20 26L22 34L24.5 22L27 38L29.5 16L32 44L34.5 18L37 40L39.5 24"
                  "L42 35L44 27L46 30H51", INK, 2.6)


@reg("heaptrack", DEEP_ORANGE_DEEP)
def heaptrack():
    flame = path("M28 47C20.5 45.5 17 39.5 18.5 32.5C19.5 28 23 26 23.5 20C27.5 23 28 27.5 27 31"
                 "C30 28.5 31 24 30 16.5C36 21 38 29 36 36C37 34.5 38 33 38 31C39.5 38.5 36 46.5 28 47Z", INK)
    return flame + rrect(40.5, 12, 4.5, 36, 2.25, INK)


@reg("hedgewars", PURPLE)
def hedgewars():
    spikes = (poly([(24, 17), (14, 18), (21, 24)], INK, 2) + poly([(22, 24), (12.5, 28), (21, 31)], INK, 2) +
              poly([(22, 31), (14, 37), (23, 36.5)], INK, 2))
    body = circle(33.5, 28, 12.5, INK)
    feet = (circle(28, 42, 5, HOLE) + circle(28, 42, 3.8, INK) +
            circle(39.5, 42.5, 5, HOLE) + circle(39.5, 42.5, 3.8, INK))
    eyes = (circle(35, 23.5, 3.4, HOLE) + circle(41.5, 23.5, 3.4, HOLE) +
            circle(35.8, 24, 1.5, INK) + circle(42.2, 24, 1.5, INK))
    mouth = stroke("M33 32.5C36 31 39 31.5 41 30.5", HOLE, 2.2)
    return spikes + body + feet + eyes + mouth


@reg("helix", DEEP_PURPLE_DEEP)
def helix():
    b = stroke("M43 14L21 25L43 36L21 46", DEEP_PURPLE_SOFT, 4.6)
    a = stroke("M21 14L43 25L21 36L43 46", INK, 4.6)
    return b + a


@reg("helltaker", RED_DEEP)
def helltaker():
    crown = poly([(22, 19), (23, 11), (26, 16), (29, 9.5), (32, 15), (35, 9.5), (38, 16),
                  (41, 11), (42, 19)], BROWN_DARK, 1.6)
    hair = path("M32 15.5C42 15.5 48 22 47 31L50 36L45 36C44 41 39 45 32 45C25 45 20 41 19 36"
                "L14 36L17 31C16 22 22 15.5 32 15.5Z", INK)
    face = path("M23 29L27 25L31 28.5L35 25L41 29.5V35C41 40 37 43 32 43C27 43 23 40 23 35Z", RED_SOFT)
    eyes = stroke("M25.5 33.5C26.5 35 28.5 35 29.5 33.5", RED_DARK, 1.8) + \
        stroke("M34.5 33.5C35.5 35 37.5 35 38.5 33.5", RED_DARK, 1.8)
    return hair + crown + face + eyes


@reg("helm", BLUE_DEEP)
def helm():
    shell = path("M16 30A16 16 0 0 1 48 30V42.5A2.5 2.5 0 0 1 45.5 45H41.5A2.5 2.5 0 0 1 39 42.5"
                 "V37A7 7 0 0 0 25 37V42.5A2.5 2.5 0 0 1 22.5 45H18.5A2.5 2.5 0 0 1 16 42.5Z", INK)
    return shell + rrect(29, 27, 6, 14.5, 3, INK) + line(19, 30, 26, 30, HOLE, 2) + line(38, 30, 45, 30, HOLE, 2)


@reg("help-browser", INDIGO)
def help_browser():
    return (stroke("M24.5 21.5C24.5 16.5 28 13.5 32.5 13.5C37 13.5 40.5 16.5 40.5 20.8"
                   "C40.5 25.5 36.5 27 34 29.5C33 30.5 32.5 32 32.5 35", INK, 5.6) +
            circle(32.5, 43.5, 3.4, INK))


@reg("heroesofnewerth", BLUE_GREY)
def hon():
    h = stroke("M14.5 22V36M22.5 22V36M14.5 29H22.5", INK, 3.6)
    o = _ring(32, 29, 5.2, INK, 3.6)
    n = stroke("M41.5 36V22L49.5 36V22", INK, 3.6)
    return h + o + n + rrect(25.5, 39.5, 13, 3.6, 1.8, INK)


@reg("heroic", LIGHT_BLUE_DEEP)
def heroic():
    shield = path("M17 14H47L45 33C44 40.5 38.5 45 32 48C25.5 45 20 40.5 19 33Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    blade = poly([(32, 17), (34.8, 21.5), (34.3, 32), (29.7, 32), (29.2, 21.5)], HOLE, 1.5)
    hilt = rrect(26.5, 32.5, 11, 3, 1.5, HOLE) + line(32, 35, 32, 38.5, HOLE, 2.8) + circle(32, 41, 2.4, HOLE)
    return shield + blade + hilt


@reg("hexalate", BLUE_GREY_DARK)
def hexalate():
    cols = [RED, YELLOW, BLUE_GREY_LIGHT, CYAN, BLUE, PURPLE]
    out = circle(CX, CY, 16.5, INDIGO_DARK)
    for k, c in enumerate(cols):
        a0 = -105 + 60 * k
        x0, y0 = pt(CX, CY, 16.5, a0)
        x1, y1 = pt(CX, CY, 16.5, a0 + 30)
        out += path(f"M32 30L{f(x0)} {f(y0)}A16.5 16.5 0 0 1 {f(x1)} {f(y1)}Z", c)
    return out


@reg("hexchat", DEEP_ORANGE_DEEP)
def hexchat():
    hexa = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in (pt(CX, CY, 17, 60 * k) for k in range(6))) + "Z"
    return (stroke(hexa, INK, 4.4) + line(25.5, 22, 38.5, 38, INK, 5) + line(38.5, 22, 25.5, 38, INK, 5))


@reg("hidemy.name", BLUE_DARK)
def hidemy():
    shield = path("M17.5 11.5L24 17.5H40L46.5 11.5V30C46.5 39 40 44.5 32 48C24 44.5 17.5 39 17.5 30Z", INK,
                  f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    t = stroke("M25.5 22.5H38.5M32 22.5V42", HOLE, 3)
    return shield + t


@reg("higan", RED)
def higan():
    return (stroke("M20 22L23 30", INK, 4) + stroke("M44.5 21L40.5 29", INK, 4) +
            stroke("M32 13V26C32 35 27 42 18 46", INK, 4.4) +
            stroke("M32.5 29C35 37 40 43 47 46", INK, 4.4))


@reg("hipchat", BLUE_DARK)
def hipchat():
    bubble = stroke("M32 15.5C22.5 15.5 16 21.5 16 29.5C16 37.5 22.5 43.5 32 43.5"
                    "C34 43.5 36 43.2 37.5 42.7L45 46.5L43.5 40C46.5 37.3 48 33.5 48 29.5"
                    "C48 21.5 41.5 15.5 32 15.5Z", INK, 4)
    return bubble + stroke("M25.5 31.5C29.5 34.5 34.5 34.5 38.5 31.5", INK, 3.2)


@reg("hiri", ORANGE_DEEP)
def hiri():
    wing = path("M13 13H30.5L33 18.5C27 18 21.5 19 17 21.5C18 19 17.5 16 13 13Z", ORANGE_SOFT)
    h = (stroke("M31 15.5L23 46", INK, 5.2) +
         stroke("M25.5 34C29 28.5 33 26 37 26C40.5 26 41.5 28.5 40.5 32L38.5 39.5C37.8 43 39.5 45 44 44", INK, 5.2))
    return wing + h


@reg("hitori", GREY_DARK)
def hitori():
    out = ""
    for r in range(4):
        for c in range(4):
            fill = HOLE if (r, c) in [(0, 0), (2, 1)] else (GREY_SOFT if (r, c) in [(0, 2), (1, 2), (2, 3)] else INK)
            out += rrect(15 + c * 9, 13 + r * 9, 7, 7, 1.5, fill)
    return out


@reg("hivelytracker", BLUE_GREY_DEEP)
def hivelytracker():
    h = rrect(14, 15, 7, 30, 2, INK) + rrect(26, 15, 7, 30, 2, INK) + rrect(14, 26.5, 19, 7, 1.5, INK)
    t = stroke("M41.5 17.5V38C41.5 41 43 42 46.5 42", INK, 6) + rrect(36, 24, 14, 6, 2, INK)
    return h + t


@reg("hollow-knight", INDIGO_DEEP)
def hollow_knight():
    horns = (path("M24.5 22C18 19.5 16.5 14.5 18.5 10.5C19.2 14.5 22 17 27.5 18.5Z", INK) +
             path("M39.5 22C46 19.5 47.5 14.5 45.5 10.5C44.8 14.5 42 17 36.5 18.5Z", INK))
    head = path("M20 31C20 23 25.5 18.5 32 18.5C38.5 18.5 44 23 44 31C44 39.5 39.5 46.5 32 46.5"
                "C24.5 46.5 20 39.5 20 31Z", INK)
    eyes = (f'<ellipse cx="26.5" cy="34" rx="3.4" ry="4.8" fill="{HOLE}"/>'
            f'<ellipse cx="37.5" cy="34" rx="3.4" ry="4.8" fill="{HOLE}"/>')
    return horns + head + eyes


@reg("homebank", ORANGE)
def homebank():
    house = poly([(32, 19.5), (42, 28), (42, 39.5), (22, 39.5), (22, 28)], INK, 2)
    return _ring(CX, CY, 15.5, INK, 4) + house + rrect(37, 20.5, 3.6, 7, 0.8, INK)


@reg("hook", GREY_DARK)
def hook():
    h = stroke("M13.5 24.5V35.5M19 24.5V35.5M13.5 30H19", INK, 2.8)
    oo = _ring(26.5, 30, 4.4, INK, 2.8) + _ring(38, 30, 4.4, INK, 2.8)
    k = stroke("M45 24.5V35.5M50.5 24.5L45.5 30L50.5 35.5", INK, 2.8)
    return h + oo + k


@reg("hoppscotch", TEAL)
def hoppscotch():
    beam = poly([(27, 26), (37, 26), (45, 47), (19, 47)], TEAL_SOFT, 2)
    dome = path("M25.5 21A6.5 6 0 0 1 38.5 21Z", INK)
    saucer = f'<ellipse cx="32" cy="22.5" rx="15.5" ry="4.8" fill="{INK}"/>'
    dots = circle(25.5, 23, 1.3, HOLE) + circle(32, 23.8, 1.3, HOLE) + circle(38.5, 23, 1.3, HOLE)
    return beam + dome + saucer + dots


def _lambda_s():
    return stroke("M22.5 16H27.5L41 44", INK, 5.5) + stroke("M32 27L23 44", INK, 5.5)


def _two_s(body):
    return (g(body, "translate(28 27) scale(.85) translate(-32 -30)") +
            circle(42, 41, 10, HOLE) + circle(42, 41, 8, INK))


for _n in ["half-life", "half-life-blue-shift", "half-life-deathmatch", "half-life-opposing-force"]:
    SMALL[_n] = _lambda_s
for _n in ["half-life2", "half-life2-deathmatch", "half-life2-lost-coast"]:
    SMALL[_n] = lambda: _two_s(_lambda_s())


@small("gweled")
def gweled_s():
    return poly([(21, 14), (43, 14), (50, 22), (32, 47), (14, 22)], INK, 2.5) + stroke("M15 22.5H49", HOLE, 2.4)


@small("gwenview")
def gwenview_s():
    eye = path("M12 30C17.5 20 24.5 15 32 15C39.5 15 46.5 20 52 30C46.5 40 39.5 45 32 45C24.5 45 17.5 40 12 30Z", INK)
    return eye + circle(CX, CY, 10, HOLE) + circle(CX, CY, 5, INK)


@small("gzdoom")
def gzdoom_s():
    return stroke("M26.5 24A8 8 0 1 0 29 31H23.5", INDIGO_SOFT, 5.2) + stroke("M35 21H46L35 39H46", INK, 5.2)


@small("hacknet")
def hacknet_s():
    return (arc_c(CX, CY, 14, -60, 150, INK, 4) + arc_c(CX, CY, 14, 180, 260, INK, 4) +
            circle(CX, CY, 6, INK))


@small("hamster")
def hamster_s():
    teeth = "".join(g(rrect(29, 11, 6, 6, 1.5, INK), f"rotate({90 * k} 32 30)") for k in range(4))
    return teeth + circle(CX, CY, 14, INK) + line(24, 37, 40, 23, HOLE, 3.6)


@small("harmonoid")
def harmonoid_s():
    return rrect(18, 12, 28, 36, 5, INK) + circle(32, 21, 4, HOLE) + circle(32, 36.5, 6.5, HOLE)


@small("haroopad")
def haroopad_s():
    head = circle(32, 31, 15, INK) + poly([(26, 18), (32, 11), (38, 18)], INK, 2)
    return head + circle(26, 29, 5, HOLE) + circle(38, 29, 5, HOLE) + poly([(28, 36), (36, 36), (32, 42)], HOLE, 2)


@small("haruna")
def haruna_s():
    return rrect(14, 13, 36, 34, 4, INK) + stroke("M25 19V41M39 19V41M25 30H39", HOLE, 5)


@small("hashit")
def hashit_s():
    return (line(27, 15, 25, 45, INK, 5) + line(39.5, 15, 37.5, 45, INK, 5) +
            line(17.5, 23.5, 46.5, 23.5, INK, 5) + line(17.5, 36.5, 46.5, 36.5, INK, 5))


@small("hb-icon")
def hb_icon_s():
    glass = poly([(12.5, 17), (32, 17), (22, 29)], INK, 2.5) + line(22, 28, 22, 45, INK, 3.5)
    fruit = f'<ellipse cx="40" cy="36" rx="9" ry="11" fill="{INK}"/>'
    leaves = poly([(35, 26), (36, 13), (40, 20), (44, 13), (45, 26)], INK, 2)
    return glass + leaves + fruit


@small("hdajackretask")
def hdajackretask_s():
    dots = "".join(circle(x, y, 5, INK) for x in (18, 46) for y in (17, 43))
    return line(18, 17, 46, 43, INK, 3.5) + line(18, 43, 46, 17, INK, 3.5) + dots


@small("hdspmixer")
def hdspmixer_s():
    out = ""
    for x, y in [(20, 22), (32, 36), (44, 26)]:
        out += line(x, 14, x, 46, INK, 2.8) + rrect(x - 5.5, y - 4, 11, 8, 2.5, INK)
    return out


@small("headset")
def headset_s():
    return stroke("M13 30H18L22.5 21L27.5 39L32 15L36.5 45L41.5 21L46 30H51", INK, 3.4)


@small("hedgewars")
def hedgewars_s():
    spikes = poly([(24, 16), (12, 24), (22, 30), (13, 37), (25, 37)], INK, 2)
    return (spikes + circle(34, 28, 13.5, INK) + circle(29, 43, 4.5, INK) + circle(40, 43, 4.5, INK) +
            circle(36, 24, 3.8, HOLE) + circle(43, 24, 3.2, HOLE))


@small("helix")
def helix_s():
    return stroke("M43 14L21 30L43 46", DEEP_PURPLE_SOFT, 6) + stroke("M21 14L43 30L21 46", INK, 6)


@small("helltaker")
def helltaker_s():
    crown = poly([(21, 20), (23, 10), (28, 16), (32, 9), (36, 16), (41, 10), (43, 20)], BROWN_DARK, 2)
    hair = circle(32, 31, 16, INK)
    face = path("M22 30L27 25L32 29L37 25L42 30V35C42 41 37.5 44 32 44C26.5 44 22 41 22 35Z", RED_SOFT)
    return hair + crown + face


@small("heroesofnewerth")
def hon_s():
    return _ring(32, 28, 9, INK, 5) + rrect(21, 41, 22, 5, 2.5, INK)


@small("hexchat")
def hexchat_s():
    hexa = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in (pt(CX, CY, 17, 60 * k) for k in range(6))) + "Z"
    return path(hexa, INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"') + \
        line(26, 23, 38, 37, HOLE, 4.5) + line(38, 23, 26, 37, HOLE, 4.5)


@small("hitori")
def hitori_s():
    out = ""
    for r in range(3):
        for c in range(3):
            fill = HOLE if (r, c) in [(0, 0), (1, 2), (2, 1)] else INK
            out += rrect(14 + c * 12.5, 12 + r * 12.5, 10.5, 10.5, 2, fill)
    return out


@small("hivelytracker")
def hivelytracker_s():
    h = rrect(13, 14, 8, 32, 2, INK) + rrect(26, 14, 8, 32, 2, INK) + rrect(13, 26, 21, 8, 1.5, INK)
    return h + rrect(38.5, 16, 8, 30, 2, INK) + rrect(36, 23, 15, 7, 2, INK)


@small("homebank")
def homebank_s():
    return poly([(32, 14), (48, 28), (48, 45), (16, 45), (16, 28)], INK, 3)


@small("hook")
def hook_s():
    return _ring(23, 30, 8.5, INK, 5) + _ring(41, 30, 8.5, INK, 5)
