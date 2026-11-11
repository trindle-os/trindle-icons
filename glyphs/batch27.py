# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 27: ffmulticonverter to forager.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_SOFT, BLUE_SOFT, BROWN_DARK, BROWN_DEEP, circle, CX, CY, DEEP_ORANGE,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DARK, f, g,
    GREY, GREY_DARK, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_SOFT, INK,
    LIGHT_BLUE_LIGHT, line, ORANGE_DARK, ORANGE_DEEP, ORANGE_LIGHT, ORANGE_SOFT, path, PINK,
    PINK_DARK, PINK_LIGHT, poly, pt, PURPLE_DARK, PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED,
    RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke, YELLOW_DARK, YELLOW_LIGHT,
)
from glyphs.kit import (
    _ring, FIREFOX_BODY, registry,
)

ICONS, SMALL, reg, small = registry()


@reg("ffmulticonverter", BLUE_GREY_DEEP)
def ffmulticonverter():
    top = path("M46 17C40 12.5 27 12 20.5 17.5C15.5 22 18 28.5 25 30L34 31.5"
               "C29 28.5 23.5 27 24 23.5C24.8 19 36 17 46 17Z", INK)
    bot = path("M18 43C24 47.5 37 48 43.5 42.5C48.5 38 46 31.5 39 30L30 28.5"
               "C35 31.5 40.5 33 40 36.5C39.2 41 28 43 18 43Z", BLUE_GREY_SOFT)
    return top + bot


@reg("filmulator-gui", DEEP_ORANGE_DEEP)
def filmulator():
    strip = rrect(13, 17, 38, 26, 3, INK)
    holes = "".join(rrect(x, y, 3, 2.4, 0.8, HOLE) for x in (16, 22, 28, 34, 40, 45.5)
                    for y in (18.6, 39))
    word = (stroke("M18.5 36V24H24.5M18.5 29.5H23.5", HOLE, 2.6) +
            line(28, 29, 28, 36, HOLE, 2.6) + circle(28, 24.5, 1.5, HOLE) +
            line(32.5, 23.5, 32.5, 36, HOLE, 2.6) +
            stroke("M37 36V29M37 31C37 28 42 28 42 31V36M42 31C42 28 47 28 47 31V36", HOLE, 2.6))
    return strip + holes + word


@reg("flacon", DEEP_ORANGE_DEEP)
def flacon():
    box = rrect(15, 13, 34, 34, 6, INK)
    disc_ = circle(30, 32, 10.5, HOLE) + circle(30, 32, 3.2, INK)
    arm = stroke("M43 18V29L37 35", HOLE, 2.6) + circle(43, 18, 2.4, HOLE)
    return box + disc_ + arm


@reg("flowblade", BLUE_GREY_DARK)
def flowblade():
    strip = rrect(15, 12, 34, 36, 4, INK)
    holes = "".join(rrect(x, y, 3.4, 3.4, 0.8, HOLE) for x in (17.5, 43.1)
                    for y in (15, 22, 29, 36, 42.5))
    blade = path("M34 15H40.5C36.5 20 41 25 37.5 30C34 35 39 40 35.5 45H23.5Z", HOLE)
    return strip + holes + blade


@reg("flash", RED_DEEP)
def flash():
    return (stroke("M45 16C37 14.5 33.5 19 31.5 28C29.5 37.5 26.5 43.5 19 43.5", INK, 5.5) +
            line(25, 29, 40, 29, INK, 5))


@reg("foobnix", BLUE_DARK)
def foobnix():
    return rrect(15, 13, 34, 34, 3, INK) + poly([(27, 21), (41, 30), (27, 39)], HOLE, 2.5)


@reg("fmit", YELLOW_DARK)
def fmit():
    screen = rrect(14, 14, 36, 22, 3, INK)
    fm = (stroke("M19 31V19H26M19 24.5H25", RED, 3) +
          stroke("M30 31V24M30 26C30 22.5 35.5 22.5 35.5 26V31M35.5 26C35.5 22.5 41 22.5 41 26V31",
                 RED, 3))
    grille = rrect(14, 39, 22, 3, 1.5, INK) + rrect(14, 44, 22, 3, 1.5, INK) + circle(45, 43, 3, INK)
    return screen + fm + grille


@reg("fluajho", BLUE_GREY_DARK)
def fluajho():
    drop = path("M32 11C38 19.5 46.5 26 46.5 35A14.5 14.5 0 0 1 17.5 35C17.5 26 26 19.5 32 11Z", INK)
    swirl = stroke("M35 20.5C28.5 25 25 30 25 35.5A7 7 0 1 0 32 28.5C29.5 28.5 27.5 29.5 26 31", HOLE, 3.6)
    return drop + swirl


@reg("flycast", PURPLE_DEEP)
def flycast():
    d = ("M32 30a3 3 0 0 1 6 0a6 6 0 0 1 -12 0a9 9 0 0 1 18 0"
         "a12 12 0 0 1 -24 0a15 15 0 0 1 22.5 -13")
    return g(stroke(d, INK, 3.4), "translate(0 1.5)")


@reg("fluxgui", BLUE_DEEP)
def fluxgui():
    top = path("M15.5 30A16.5 16.5 0 0 1 48.5 30Z", AMBER_SOFT)
    sun = circle(38.5, 23.5, 4.2, DEEP_ORANGE_LIGHT)
    bot = path("M15.5 31.5H48.5A16.5 16.5 0 0 1 15.5 31.5Z", INK)
    return top + sun + bot


@reg("fofix", ORANGE_DEEP)
def fofix():
    x = line(20, 16, 44, 45, INK, 7) + line(44, 16, 20, 45, INK, 7)
    flames = (path("M20 16C17 12.5 18 9.5 20.5 8C20 10.5 22 12 23.5 14Z", INK) +
              path("M44 16C47 12.5 46 9.5 43.5 8C44 10.5 42 12 40.5 14Z", INK))
    return x + flames


@reg("foobillardplus", DEEP_ORANGE_DEEP)
def foobillardplus():
    flame = path("M22 30C18 22 22 15 28 12C27 17 30 19 33 19C34 15 37 13 41 12"
                 "C39.5 16 42 19 45 21C47 24 47 28 46 30Z", DEEP_ORANGE_SOFT)
    white = circle(25, 35, 10.5, INK)
    black = circle(40, 37, 9.5, BROWN_DARK, f' stroke="{HOLE}" stroke-width="1.8"') + circle(41.5, 39, 3.2, INK)
    return flame + white + black


def _fox(globe_colour):
    globe = circle(32.8, 26.8, 11.2, globe_colour)
    body = FIREFOX_BODY
    ear = poly([(18.5, 17.5), (19.5, 9.5), (25.5, 14.5)], INK, 2.5)
    tail = path("M37 13.5C42 13.8 46 17 47 21.5C44 18.5 40.5 17.5 36.5 18.5"
                "C35 16.5 35.5 14.5 37 13.5Z", INK)
    return globe + body + ear + tail


@reg("firefox-nightly", DEEP_PURPLE)
@reg("firefox-developer-edition", BLUE_DEEP)
def firefox_dev():
    return _fox(INDIGO_DARK)


@reg("fi.skyjake.Lagrange", BLUE)
def lagrange():
    planet = circle(29, 33, 11, INK)
    orbit = g(f'<ellipse cx="0" cy="0" rx="8" ry="19" fill="none" stroke="{HOLE}" stroke-width="5.4"/>'
              f'<ellipse cx="0" cy="0" rx="8" ry="19" fill="none" stroke="{INK}" stroke-width="2.6"/>',
              "translate(30 31) rotate(-35)")
    sun = circle(43, 18, 5, AMBER_SOFT)
    return planet + orbit + sun


@reg("figma", BLUE_GREY_DARK)
def figma():
    sep = f' stroke="{HOLE}" stroke-width="1.4"'
    tl = path("M27 15H32V25H27A5 5 0 0 1 27 15Z", RED_LIGHT, sep)
    tr = path("M32 15H37A5 5 0 0 1 37 25H32Z", RED_SOFT, sep)
    ml = path("M27 25H32V35H27A5 5 0 0 1 27 25Z", PURPLE_LIGHT, sep)
    mr = circle(37, 30, 5, LIGHT_BLUE_LIGHT, sep)
    bl = path("M27 35H32V40A5 5 0 1 1 27 35Z", ORANGE_DEEP, sep)
    return g(tl + tr + ml + mr + bl, "translate(32 30) scale(1.3) translate(-32 -30)")


@reg("fiji", BLUE_DEEP)
def fiji():
    frame = stroke("M20 46H15.5V13.5H48.5V46H44", INK, 3.6)
    letters = (stroke("M21.5 42V20H28.5M21.5 29H27.5", INK, 3.6) +
               line(32.5, 25, 32.5, 42, INK, 3.6) + circle(32.5, 20, 2, INK) +
               stroke("M37.5 25V38.5C37.5 41 36 42.5 34 42.5", INK, 3.6) + circle(37.5, 20, 2, INK) +
               line(42.5, 25, 42.5, 42, INK, 3.6) + circle(42.5, 20, 2, INK))
    return frame + letters


@reg("fontbase", INDIGO)
def fontbase():
    return stroke("M17 38L27 26Q32 20 37 26L47 38", INK, 9) + circle(32, 40, 3.5, INK)


@reg("fontforge", BLUE_GREY_DARK)
def fontforge():
    def ff(dx):
        return (stroke(f"M{f(dx + 31)} 15C{f(dx + 26)} 13.5 {f(dx + 24)} 16 {f(dx + 23)} 21"
                       f"L{f(dx + 19.5)} 40C{f(dx + 18.5)} 45 {f(dx + 16)} 46 {f(dx + 13)} 45", INK, 3.4))
    return ff(0) + ff(10) + line(18, 25.5, 42, 25.5, INK, 3.2)


@reg("fontmatrix", RED_DARK)
def fontmatrix():
    shade = path("M20 46V20Q20 17 23 17H42Q49 17 49 24V46H42V26Q42 24 40 24H38V46H31V24H27V46Z", DEEP_ORANGE_SOFT)
    m = path("M16 44V18Q16 15 19 15H38Q45 15 45 22V44H38V24Q38 22 36 22H34V44H27V22H23V44Z", INK)
    return shade + m


@reg("fontypython", BLUE_GREY)
def fontypython():
    return (line(26, 20, 26, 46, INDIGO_DARK, 6) +
            stroke("M26 17H33A8.5 8.5 0 0 1 33 34H29", INK, 6))


@reg("focuswriter", BLUE_GREY_DARK)
def focuswriter():
    return (_ring(CX, CY, 15.5, INK, 3.2) + circle(CX, CY, 11, INK) +
            stroke("M37 23H28.5V38M28.5 30.5H35", HOLE, 4))


@reg("filebot", BLUE_DEEP)
def filebot():
    fch = (stroke("M30 15C26 13.5 23.5 15.5 22.8 19.5L19.5 42C19 45 17 46.5 14.5 46", INK, 3.6) +
           line(17.5, 25.5, 28, 25.5, INK, 3.4))
    b = stroke("M37.5 13.5L33.5 41", INK, 3.6) + _ring(40.5, 34.5, 6.5, INK, 3.6)
    return fch + b


@reg("filelight", INDIGO)
def filelight():
    outer = stroke("M32 14A16 16 0 1 1 16.2 32.5", INDIGO_SOFT, 4.4)
    mid = _ring(CX, CY, 10.5, INK, 4.4)
    return outer + mid + circle(CX, CY, 5, INK)


@reg("filen", BLUE_GREY_DARK)
def filen():
    circuit = (stroke("M24.5 40V25.5Q24.5 21.5 28.5 21.5H41", INK, 3) +
               stroke("M24.5 30H31", INK, 3) + stroke("M35 25.5V35", INK, 3))
    dots = circle(31.5, 30, 2.8, INK) + circle(35, 36, 2.8, INK) + circle(41, 21.5, 2.8, INK)
    return _ring(CX, CY, 15.5, INK, 3.2) + circuit + dots


@reg("filter", RED_DEEP)
def filter_():
    return poly([(15, 15), (49, 15), (36, 30), (36, 45), (28, 40), (28, 30)], INK, 3)


@reg("flareget", RED_DEEP)
def flareget():
    return rrect(24, 11, 16, 20, 2, INK) + poly([(14, 29), (50, 29), (32, 48)], INK, 3)


@reg("fman", BLUE_GREY_DARK)
def fman():
    dots = circle(20, 15, 2.6, INK) + circle(27, 15, 2.6, INK) + circle(34, 15, 2.6, INK)
    left = rrect(15, 21, 16, 26, 3, INK)
    rows = "".join(rrect(18.5, y, 9, 2.6, 1.3, HOLE) for y in (25.5, 30.5, 35.5, 40.5))
    right = rrect(34, 21, 15, 26, 3, BLUE_GREY_SOFT)
    return dots + left + rows + right


def _jail():
    bars = "".join(line(x, 14, x, 46, RED_SOFT, 3.4) for x in (21, 32, 43))
    bars += "".join(line(15, y, 49, y, RED_SOFT, 3.4) for y in (20, 30, 40))
    return bars


@reg("firejail-ui", RED_DEEP)
def firejail_ui():
    wand = line(23, 21, 43, 41, HOLE, 7.5) + line(23, 21, 43, 41, INK, 4)
    spark = poly([(37, 13), (38.6, 17.4), (43, 19), (38.6, 20.6), (37, 25), (35.4, 20.6),
                  (31, 19), (35.4, 17.4)], INK, 1)
    return _jail() + wand + spark


@reg("firetools", RED_DEEP)
def firetools():
    lock = (stroke("M36 34V30A6 6 0 0 1 48 30V34", HOLE, 7) +
            stroke("M36 34V30A6 6 0 0 1 48 30V34", INK, 3.2) +
            rrect(31.5, 33, 21, 15, 3.5, INK, f' stroke="{HOLE}" stroke-width="2"') +
            circle(42, 40, 2.4, HOLE))
    return g(_jail() + lock, "translate(-2 -1)")


@reg("firewall-config", RED_DEEP)
def firewall_config():
    rows = [[(14, 17), (32, 18)], [(14, 7), (22, 20), (43, 7)], [(14, 17), (32, 18)]]
    out = ""
    for r, bricks in enumerate(rows):
        for x, w in bricks:
            out += rrect(x + 0.9, 14 + r * 11 + 0.9, w - 1.8, 9.2, 2, INK)
    return g(out, "translate(0.6 -1.5)")


@reg("firewatch", DEEP_ORANGE)
def firewatch():
    shield = path("M32 12C37 14.5 42 16 47 16.5V28C47 37.5 41 44 32 48C23 44 17 37.5 17 28V16.5"
                  "C22 16 27 14.5 32 12Z", INK)
    tree = (poly([(32, 19), (39, 29), (25, 29)], HOLE, 2) +
            poly([(32, 24), (41, 36), (23, 36)], HOLE, 2) + rrect(30, 35, 4, 6, 0.8, HOLE))
    return shield + tree


@reg("fish", BLUE_GREY_DEEP)
def fish():
    return (stroke("M22 21L14 30L22 39", RED_SOFT, 4.4) +
            stroke("M28 21L36 30L28 39", ORANGE_SOFT, 4.4) +
            stroke("M50 21L42 30L50 39", YELLOW_LIGHT, 4.4))


@reg("flamerobin", RED_DEEP)
def flamerobin():
    body = path("M34 12C40 12 44 16 44 21L49 23L44.5 25.5C46.5 29 47 32 47 35"
                "C47 43 40.5 48 32 48C23.5 48 17 42 17 34C17 26 23 21 25 14"
                "C27 18 28 21 30 23C29 18 30.5 13.5 34 12Z", INK)
    eye = circle(38.5, 18.5, 1.9, HOLE)
    inner = path("M31 30C33.5 34 37 36 37 40A5 5 0 0 1 27 40C27 36 29.5 34 31 30Z", HOLE)
    return body + eye + inner


@reg("flameshot", PURPLE_DEEP)
def flameshot():
    back = path("M20 46C14 38 16 26 24 15C23.5 23 25.5 28 29 32C30 24 34 19 41 15"
                "C38.5 23 39.5 29 42 33C44 29 46.5 26.5 50 25C47 33 47 42 40 46Z", INK)
    inner = path("M24 46C21 40 22.5 33 27 28C27.5 34 30 38 33 41C34.5 36 37 33.5 41 32"
                 "C40 38 40 43 37 46Z", PURPLE_SOFT)
    return back + inner


@reg("flare", ORANGE_DEEP)
def flare():
    flame = path("M32 11C31 17 36 20 39 17C44 23 47 30 46 37L32 47L18 37C16 29 20 23 25 20"
                 "C24.5 24 26 26 28 27C27 21 28 15 32 11Z", INK)
    cross = stroke("M21 34L32 41L43 34M21 41L32 34L43 41", HOLE, 2.6)
    return flame + cross


@reg("flashforge", BLUE_DEEP)
def flashforge():
    diamond = g(rrect(17, 15, 30, 30, 8, INK), "rotate(45 32 30)")
    bolt = stroke("M35.5 15.5L28 29.5H36L28.5 44.5", HOLE, 3.8)
    return diamond + bolt


@reg("flickr", BLUE_GREY_DARK)
def flickr():
    return circle(23, 30, 8.5, BLUE) + circle(41, 30, 8.5, PINK)


@reg("flightgear", BLUE_DEEP)
def flightgear():
    plane = (rrect(29.2, 11, 5.6, 38, 2.8, INK) +
             poly([(32, 23), (49, 33), (49, 37), (32, 32), (15, 37), (15, 33)], INK, 2) +
             poly([(32, 41), (39, 45), (39, 47.5), (32, 46), (25, 47.5), (25, 45)], INK, 1.5))
    return g(plane, "rotate(45 32 30)")


@reg("floating-point", BLUE_GREY_DEEP)
def floating_point():
    return circle(CX, CY, 15, RED_LIGHT)


@reg("florence", GREY_DARK)
def florence():
    kb = rrect(13, 18, 38, 24, 4, INK)
    keys = "".join(rrect(17 + c * 8, 21.5 + r * 6, 5.5, 3.8, 1, HOLE) for r in range(2) for c in range(4))
    return kb + keys + rrect(19, 34.5, 26, 3.8, 1, HOLE)


@reg("flow", BLUE_GREY_DARK)
def flow():
    links = stroke("M21 21H41V40M21 21V39", INK, 3)
    boxes = (rrect(14, 14, 14, 13, 2.5, INK, f' stroke="{HOLE}" stroke-width="1.6"') +
             circle(41, 21, 6, RED_LIGHT) +
             rrect(14, 32, 16, 14, 2.5, INK) + rrect(35, 35, 13, 11, 2.5, ORANGE_LIGHT))
    return links + boxes


@reg("fluent-reader", BLUE_DEEP)
def fluent_reader():
    back = rrect(24, 12, 25, 29, 4, BLUE_SOFT)
    front = rrect(15, 22, 24, 26, 4, INK, f' stroke="{HOLE}" stroke-width="2"')
    fch = stroke("M33 28H23V42M23 35H31", HOLE, 3.6)
    return back + front + fch


@reg("fluid", BLUE)
def fluid():
    flask = path("M27.5 11H36.5V23L47 42C48.5 45 47 47.5 43.5 47.5H20.5C17 47.5 15.5 45 17 42L27.5 23Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    liquid = path("M22.5 38H41.5L43.5 42C44 43 43.5 43.5 42.5 43.5H21.5C20.5 43.5 20 43 20.5 42Z", BLUE_DARK)
    bubbles = circle(32, 17, 2, HOLE) + circle(30.5, 25, 2.2, HOLE) + circle(34, 31.5, 2.4, HOLE)
    return flask + liquid + bubbles


@reg("fheroes2", BROWN_DEEP)
def fheroes2():
    shield = path("M17 14C22 12 27 11 32 11C37 11 42 12 47 14C47.5 26 44 39 32 48"
                  "C20 39 16.5 26 17 14Z", INK)
    bolt = poly([(35, 13.5), (26, 30), (32, 30), (27.5, 45), (39, 26), (33, 26), (38, 13.5)], AMBER, 1.5)
    return shield + bolt


@reg("five-or-more", INDIGO_DEEP)
def five_or_more():
    row = "".join(circle(18 + 7 * k, 16 + 7 * k, 4.4, INK) for k in range(5))
    extra = circle(39, 16, 4.4, INDIGO_SOFT) + circle(46, 23, 4.4, RED_LIGHT) + circle(18, 37, 4.4, ORANGE_DEEP)
    return row + extra


def _ball(patch_r=6, edge_r=4.4):
    dark = BLUE_GREY_DARK
    out = circle(CX, CY, 16.5, INK)
    centre = [pt(CX, CY, patch_r, -90 + 72 * k) for k in range(5)]
    out += "".join(line(x, y, *pt(CX, CY, 13, -90 + 72 * k), dark, 2.2) for k, (x, y) in enumerate(centre))
    out += poly(centre, dark, 1.5)
    for k in range(5):
        cx, cy = pt(CX, CY, 15.5, -90 + 72 * k)
        out += poly([pt(cx, cy, edge_r, -90 + 72 * k + 36 + 72 * j) for j in range(5)], dark, 1.2)
    return out + _ring(CX, CY, 16.5, INK, 1.6)


@reg("football", ORANGE_DARK)
def football():
    return _ball()


@reg("for-the-king", PURPLE_DARK)
def for_the_king():
    hexa = poly([pt(CX, CY, 16, -90 + 60 * k) for k in range(6)], PURPLE_LIGHT, 3)
    inner = poly([pt(CX, CY, 11.5, -90 + 60 * k) for k in range(6)], HOLE, 2)
    blade = poly([(28.5, 22), (35.5, 22), (35.5, 40), (32, 46), (28.5, 40)], INK, 1.5)
    guard = rrect(23, 18.5, 18, 4, 2, INK)
    grip = rrect(30, 12, 4, 7, 1.5, INK) + circle(32, 11.5, 2.6, INK)
    return hexa + inner + blade + guard + grip


@reg("forager", PINK_LIGHT)
def forager():
    base = g(rrect(15, 17, 34, 31, 9, PINK_DARK), "rotate(-6 32 30)")
    body = g(rrect(15, 13, 34, 31, 9, INK), "rotate(-6 32 30)")
    eyes = path("M25 23.5a2.2 3.4 0 1 0 0.01 0Z", DEEP_PURPLE_DARK) + path("M37 22.5a2.2 3.4 0 1 0 0.01 0Z", DEEP_PURPLE_DARK)
    mouth = stroke("M28.5 32.5Q31.7 35.8 35 32", DEEP_PURPLE_DARK, 2.2)
    return base + body + eyes + mouth


@reg("foot", BLUE_GREY_DEEP)
def foot():
    sole = path("M22 21C27 20 29 24 28.5 30C28 36 28.5 40 25.5 44.5C22.5 47 18 45.5 18 40"
                "C18 35 20 32 19.5 28C19 24.5 19 21.5 22 21Z", INK)
    toes = (circle(19.5, 16, 2.8, INK) + circle(24.5, 14.5, 2.2, INK) + circle(28.5, 15.5, 1.9, INK) +
            circle(31.5, 18, 1.7, INK))
    return sole + toes + rrect(34, 39, 14, 4.5, 2.25, INK)


@small("filmulator-gui")
def filmulator_s():
    strip = rrect(13, 15, 38, 30, 3, INK)
    holes = "".join(rrect(x, y, 4.5, 3, 1, HOLE) for x in (16, 25, 34.5, 43.5) for y in (17, 40))
    return strip + holes + stroke("M26 36V25H38M26 30.5H35", HOLE, 3.6)


@small("fiji")
def fiji_s():
    return (stroke("M21 46H15.5V13.5H48.5V46H43", INK, 4.2) +
            stroke("M22.5 42V20H30M22.5 30H29", INK, 4.2) +
            line(35, 22, 35, 42, INK, 4.2) + line(42, 22, 42, 42, INK, 4.2))


@small("filen")
def filen_s():
    return (_ring(CX, CY, 15.5, INK, 3.4) + stroke("M25 40V26Q25 22 29 22H40", INK, 4) +
            circle(40, 22, 3.4, INK) + stroke("M25 31H32", INK, 4) + circle(33, 31, 3.4, INK))


def _jail_s():
    return ("".join(line(x, 14, x, 46, RED_SOFT, 4) for x in (22, 42)) +
            "".join(line(15, y, 49, y, RED_SOFT, 4) for y in (21, 39)))


@small("firejail-ui")
def firejail_ui_s():
    return _jail_s() + line(22, 20, 43, 41, HOLE, 9) + line(22, 20, 43, 41, INK, 5.5)


@small("firetools")
def firetools_s():
    lock = (stroke("M24 32V27A8 8 0 0 1 40 27V32", HOLE, 9) +
            stroke("M24 32V27A8 8 0 0 1 40 27V32", INK, 4.5) +
            rrect(19, 30, 26, 18, 4, INK, f' stroke="{HOLE}" stroke-width="2.4"'))
    return _jail_s() + lock


@small("fish")
def fish_s():
    return (stroke("M22 20L13 30L22 40", RED_SOFT, 5) +
            stroke("M28 20L37 30L28 40", ORANGE_SOFT, 5) +
            stroke("M51 20L42 30L51 40", YELLOW_LIGHT, 5))


@small("five-or-more")
def five_or_more_s():
    return ("".join(circle(18 + 9.3 * k, 16 + 9.3 * k, 5.2, INK) for k in range(4)) +
            circle(44, 17, 5.2, RED_LIGHT) + circle(20, 42, 5.2, GREY))


@small("flycast")
def flycast_s():
    d = "M32 30a4 4 0 0 1 8 0a8 8 0 0 1 -16 0a12 12 0 0 1 24 0"
    return g(stroke(d, INK, 4), "translate(-4 2)")


@small("flow")
def flow_s():
    return (stroke("M21 21H41V40M21 21V39", INK, 4) + rrect(13, 13, 16, 15, 3, INK) +
            circle(42, 20, 7, RED_LIGHT) + rrect(13, 32, 17, 15, 3, INK) +
            rrect(34, 34, 15, 13, 3, GREY_SOFT))


@small("flowblade")
def flowblade_s():
    strip = rrect(14, 12, 36, 36, 4, INK)
    holes = "".join(rrect(x, y, 4.5, 5, 1, HOLE) for x in (16.5, 43) for y in (15, 27.5, 40))
    return strip + holes + path("M34 15H42C37 21 43 25 38.5 30C34 35 40 40 36 45H23Z", HOLE)


@small("florence")
def florence_s():
    kb = rrect(12, 16, 40, 28, 4, INK)
    keys = "".join(rrect(16 + c * 11, 20.5 + r * 7.5, 8, 5, 1.2, HOLE) for r in range(2) for c in range(3))
    return kb + keys + rrect(19, 36, 26, 5, 1.2, HOLE)


@small("fman")
def fman_s():
    left = rrect(14, 14, 18, 34, 3.5, INK)
    rows = "".join(rrect(18, y, 10, 4, 2, HOLE) for y in (19, 27, 35))
    return left + rows + rrect(35, 14, 15, 34, 3.5, BLUE_GREY_SOFT)


@small("fmit")
def fmit_s():
    return (rrect(13, 12, 38, 26, 3.5, INK) +
            stroke("M19 33V18H27M19 25H26", RED, 4) +
            stroke("M32 33V24C32 21 39 21 39 24V33M39 25C39 21 45.5 21 45.5 25V33", RED, 3.6) +
            rrect(13, 42, 24, 5, 2.5, INK) + circle(45, 44.5, 3.8, INK))


@small("focuswriter")
def focuswriter_s():
    return circle(CX, CY, 17, INK) + stroke("M38 21H28V39M28 30.5H36", HOLE, 5)


@small("fontforge")
def fontforge_s():
    def ff(dx):
        return stroke(f"M{f(dx + 30)} 14C{f(dx + 25)} 13 {f(dx + 23)} 16 {f(dx + 22.5)} 21"
                      f"L{f(dx + 20)} 40C{f(dx + 19)} 45 {f(dx + 16)} 46 {f(dx + 13.5)} 45", INK, 4)
    return ff(-1) + ff(11) + line(17, 25.5, 43, 25.5, INK, 3.6)


@small("fi.skyjake.Lagrange")
def lagrange_s():
    orbit = g(f'<ellipse cx="0" cy="0" rx="8.5" ry="19" fill="none" stroke="{HOLE}" stroke-width="6.5"/>'
              f'<ellipse cx="0" cy="0" rx="8.5" ry="19" fill="none" stroke="{INK}" stroke-width="3.4"/>',
              "translate(30 31) rotate(-35)")
    return circle(29, 33, 12, INK) + orbit + circle(44, 17, 5.5, AMBER_SOFT)


@small("foobillardplus")
def foobillardplus_s():
    return (circle(24, 31, 12, INK) +
            circle(41, 36, 10.5, BROWN_DARK, f' stroke="{HOLE}" stroke-width="2.2"') + circle(43, 39, 3.8, INK))


@small("football")
def football_s():
    return _ball(7, 5)


@small("flare")
def flare_s():
    flame = path("M32 10C31 17 36 20 39.5 16.5C45 23 48 30 47 38L32 48L17 38C15 29 20 23 25 20"
                 "C24.5 24 26 26 28 27C27 21 28 14.5 32 10Z", INK)
    return flame + stroke("M22 34L32 41L42 34", HOLE, 3.6)


@small("forager")
def forager_s():
    body = g(rrect(14, 13, 36, 34, 9, INK), "rotate(-6 32 30)")
    eyes = path("M25 22.5a3 4.2 0 1 0 0.01 0Z", DEEP_PURPLE_DARK) + path("M38.5 21.5a3 4.2 0 1 0 0.01 0Z", DEEP_PURPLE_DARK)
    return body + eyes
