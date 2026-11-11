# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 9: avidemux to bespoke_icon."""
import math
from lm import (
    AMBER, AMBER_LIGHT, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, BLUE_LIGHT, BLUE_SOFT, BROWN, BROWN_DEEP, BROWN_SOFT, circle, cut, CYAN,
    CYAN_DARK, CYAN_DEEP, CYAN_LIGHT, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DEEP, DEEP_PURPLE_SOFT, f, g, GREY_DARK,
    GREY_DEEP, GREY_LIGHT, HOLE, INDIGO, INDIGO_LIGHT, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_SOFT, line, ORANGE, ORANGE_DARK, ORANGE_DEEP, path, PINK_DEEP, PINK_LIGHT,
    PINK_SOFT, poly, pt, PURPLE_LIGHT, RED, RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, rrect,
    stroke, TEAL, TEAL_DARK,
)
from glyphs.kit import ellipse_f, gear_e, registry, _ring

ICONS, SMALL, reg, small = registry()


@reg("avidemux", GREY_DARK)
def avidemux():
    body = rrect(15, 22, 34, 24, 4, INK)
    bar = rrect(15, 13, 34, 6.5, 2.5, INK)
    bar += "".join(line(x, 14.3, x - 3.5, 18.2, HOLE, 2.2, "butt") for x in (24, 32, 40))
    cam = rrect(21, 28, 14, 12, 2.5, HOLE) + poly([(35, 34), (42.5, 29.5), (42.5, 38.5)], HOLE, 1.5)
    return body + g(bar, "rotate(-8 15 19.5)") + cam


@reg("avimetaedit", INDIGO_LIGHT)
def avimetaedit():
    return (stroke("M14.5 40L21 20L27.5 40", INK, 4.4) +
            stroke("M30.5 20L37 40L43.5 20", INK, 4.4) + line(49, 20, 49, 40, INK, 4.4))


_PEAR = ("M32 12C27 12 25.5 17 24.5 21C20 25 18 30 18 35C18 43 24 48 32 48"
         "C40 48 46 43 46 35C46 30 44 25 39.5 21C38.5 17 37 12 32 12Z")


@reg("avocado", BLUE)
def avocado():
    fruit = (path(_PEAR, INK) + g(path(_PEAR, BLUE_SOFT), "translate(32 34) scale(.74) translate(-32 -34)")
             + circle(32, 36, 6.2, BROWN_DEEP))
    return g(fruit, "translate(32 30) scale(.95) rotate(28) translate(-32 -30)")


_EGG = "M32 12C25 12 17 26 17 35C17 43 24 48 32 48C40 48 47 43 47 35C47 26 39 12 32 12Z"


@reg("avocode", TEAL)
def avocode():
    return path(_EGG, INK) + g(path(_EGG, HOLE), "translate(32 36) scale(.5) translate(-32 -32)")


def _avogadro(orbit, balls):
    a = stroke("M19 45L32 14L45 45", INK, 5.5)
    rot = -24
    orb = g(ellipse_f(32, 30, 18, 6.5, "none", f' stroke="{orbit}" stroke-width="2.6"'),
            f"rotate({rot} 32 30)")
    out = a + orb
    for t, r in [(205, 4.2), (-15, 3.3)]:
        x, y = 18 * math.cos(math.radians(t)), 6.5 * math.sin(math.radians(t))
        c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        out += circle(32 + x * c - y * s, 30 + x * s + y * c, r, balls)
    return out


@reg("avogadro-icon", DEEP_ORANGE_DEEP)
def avogadro():
    return _avogadro(DEEP_ORANGE_SOFT, AMBER_SOFT)


@reg("avogadro2", BLUE_DEEP)
def avogadro2():
    return _avogadro(BLUE_SOFT, LIGHT_BLUE_SOFT)


@reg("awesomebump", BLUE_DEEP)
def awesomebump():
    a = stroke("M15 44L23.5 18.5L32 44", INK, 5.2)
    b = path("M33 16H40.5A6 6 0 0 1 41.2 28.8V29.2A7.4 7.4 0 0 1 41 44H33Z", INK)
    return g(a + b, "translate(1.5 0)")


@reg("awgg", BLUE_DARK)
def awgg():
    globe = circle(32, 28, 15, INK)
    lines = (ellipse_f(32, 28, 6.5, 15, "none", f' stroke="{HOLE}" stroke-width="2"') +
             line(17.5, 28, 46.5, 28, HOLE, 2, "butt"))
    arrow = path("M28.5 21H35.5V33H41L32 45L23 33H28.5Z", PINK_LIGHT,
                 f' stroke="{HOLE}" stroke-width="2.2" stroke-linejoin="round"')
    return globe + lines + arrow


@reg("ayatana-settings", GREY_DEEP)
def ayatana_settings():
    return (gear_e(32, 30, 13, 8, 7, 4, INK) + circle(32, 30, 8.5, HOLE) +
            _ring(31, 30, 3.6, CYAN_LIGHT, 2.6) + line(34.6, 26.4, 34.6, 34, CYAN_LIGHT, 2.6))


@reg("azardi", RED)
def azardi():
    a = stroke("M13.5 44L21.5 17L29.5 44", INK, 5) + line(17.3, 36, 25.7, 36, INK, 4)
    z = stroke("M33.5 17.5H48L33.5 42.5H48.5", INK, 5)
    return a + z


@reg("azote", LIGHT_BLUE)
def azote():
    a = cut("M28.5 13H35.5L49 46.5H38.5L32 32L25.5 46.5H15Z"
            "M32 19.5L35 27.5H29Z", INK)
    return a + circle(45, 15.5, 3.6, AMBER_SOFT)


@reg("azpainter", ORANGE_DEEP)
def azpainter():
    swoosh = (stroke("M16.5 45C19 33 26 22 40 16", INK, 3.4) +
              stroke("M19.5 45.5C23 36 29.5 29 42 24.5", INK, 3.4) +
              stroke("M23 46C27 40 32.5 35.5 42 32.5", INK, 3.4))
    pencil = line(47.5, 12.5, 38.5, 25, AMBER_SOFT, 5, "butt") + poly(
        [(36.5, 23.5), (40.5, 26.5), (35.5, 29.5)], BROWN_DEEP, 1.5)
    return swoosh + pencil


@reg("azuredatastudio", LIGHT_BLUE_DEEP)
def azuredatastudio():
    can = path("M16 18V40A11 4.5 0 0 0 38 40V18Z", INK) + ellipse_f(27, 18, 11, 4.5, INK)
    rim = ellipse_f(27, 18, 7.5, 2.2, LIGHT_BLUE_SOFT)
    pulse = stroke("M16 31H20.5L23.5 26L27 35L30 29.5H34", HOLE, 2.2)
    cog = circle(41, 39, 10, HOLE) + gear_e(41, 39, 6, 8, 3.6, 2.4, INK) + circle(41, 39, 2.4, HOLE)
    return can + rim + pulse + cog


@reg("baba-is-you", BLUE_GREY_DARK)
def baba():
    body = rrect(15, 19, 32, 18, 9, INK) + circle(40.5, 19, 3.4, INK) + circle(46, 20.5, 3, INK)
    legs = "".join(line(x, 34, x + dx, 42.5, INK, 3.2) for x, dx in
                   [(19.5, -.5), (25, .5), (36, 0), (42, .8)])
    tail = line(16, 24, 13.5, 21, INK, 2.6)
    return body + legs + tail + circle(40, 26, 1.8, HOLE) + circle(45.5, 26.5, 1.3, HOLE)


_HEART = [".XX.XX.", "XXXXXXX", "XXXXXXX", ".XXXXX.", "..XXX..", "...X..."]
_HEART_S = [".X.X.", "XXXXX", "XXXXX", ".XXX.", "..X.."]


def _pixheart(rows, pitch, cell):
    w, h = len(rows[0]) * pitch, len(rows) * pitch
    x0, y0 = 32 - w / 2 + (pitch - cell) / 2, 30 - h / 2 + (pitch - cell) / 2
    return "".join(rrect(x0 + c * pitch, y0 + r * pitch, cell, cell, 1.1, INK)
                   for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == "X")


@reg("babe", PINK_LIGHT)
def babe():
    return _pixheart(_HEART, 5.2, 4.3)


@reg("backdoor-factory", BLUE_DEEP)
def backdoor():
    frame = rrect(31, 12, 15, 36, 2, BLUE_DARK) + stroke("M33 12.5H45.5V47.5H33", INK, 3)
    door = poly([(18, 16), (34, 12), (34, 48), (18, 44)], INK, 2.5)
    return frame + door + circle(29.5, 31, 2, HOLE)


@reg("badland", BLUE_GREY_DEEP)
def badland():
    n = 30
    pts = [pt(32, 33, 14.5 if k % 2 == 0 else 12.3, 360 / n * k) for k in range(n)]
    fur = poly(pts, INK, 1)
    tufts = (poly([(24, 22), (22.5, 11), (26, 15), (27.5, 11.5), (30, 20)], INK, 1.2) +
             poly([(34, 20), (36, 12), (38, 15.5), (41.5, 11), (40.5, 22)], INK, 1.2))
    eyes = (circle(33, 38, 3.8, HOLE) + circle(34, 38, 1.7, INK) +
            circle(41.5, 37.5, 2.8, HOLE) + circle(42, 37.5, 1.2, INK))
    return fur + tufts + eyes


@reg("baidunetdisk", BLUE)
def baidunetdisk():
    return (_ring(22, 34, 6.5, INK, 4) + _ring(42, 34, 6.5, INK, 4) +
            line(22, 40.5, 42, 40.5, INK, 4) + _ring(32, 23.5, 7, RED_SOFT, 4))


@reg("baiji-manga-viewer", CYAN_DEEP)
def baiji():
    body = stroke("M22 25.5C31 20 44.5 22 44.5 32C44.5 40 36 44 30 39.5", INK, 8.5)
    snout = poly([(24, 21), (14, 26.5), (24, 30)], INK, 2.5)
    fin = poly([(31.5, 22), (35, 13.5), (39, 22.5)], INK, 1.5)
    tail = poly([(31, 36.5), (23, 34.5), (25.5, 43.5)], INK, 2)
    return body + snout + fin + tail + circle(23, 24.5, 1.5, HOLE)


BAKA_HEAD = path('M16 22L17 12L25.5 17.2C29.5 15.8 34.5 15.8 38.5 17.2L47 12L48 22C49.5 25 50 28 50 31C50 41 42 47 32 47C22 47 14 41 14 31C14 28 14.5 25 16 22Z', INK)


@reg("baka-mplayer", GREY_DARK)
def baka():
    head = BAKA_HEAD
    eyes = "".join(circle(x, 31, 6.6, HOLE) + circle(x, 31, 3.8, INK) for x in (24.5, 39.5))
    return g(head + eyes, "translate(32 30) scale(.95) translate(-32 -30)")


@reg("baldis-basics", BLUE_GREY_LIGHT)
def baldi():
    head = ellipse_f(32, 24, 9.5, 11.5, INK) + circle(22.5, 25, 2.4, INK) + circle(41.5, 25, 2.4, INK)
    face = (circle(28.3, 22, 2, HOLE) + circle(35.7, 22, 2, HOLE) +
            stroke("M27.5 30Q32 33.5 36.5 30", HOLE, 2))
    curl = stroke("M31.5 12.8C31 10 33 9 35.5 10.5", INK, 2.2)
    shirt = path("M15 49V43C15 40 18 38 22 37.5C25 39.5 28.5 40.5 32 40.5"
                 "C35.5 40.5 39 39.5 42 37.5C46 38 49 40 49 43V49Z", INK)
    return head + face + curl + shirt


@reg("bambustudio", ORANGE_DARK)
def bambustudio():
    return (rrect(16, 13, 32, 34, 4, INK) + line(32, 13, 32, 47, HOLE, 2.8, "butt") +
            line(16, 36.5, 32, 31.5, HOLE, 2.8, "butt") + line(32, 26, 48, 21, HOLE, 2.8, "butt"))


@reg("bandcamp", CYAN_DEEP)
def bandcamp():
    b = line(18, 15, 18, 42, INK, 4.6) + _ring(24.5, 35.5, 6.5, INK, 4.6)
    c = stroke("M46.5 30A7.8 7.8 0 1 0 46.5 41", INK, 4.6)
    return g(b + c, "translate(0 -2)")


@reg("bareftp", BLUE_GREY_DEEP)
def bareftp():
    up = line(25, 44, 25, 23, INK, 5) + poly([(16.5, 25), (25, 13.5), (33.5, 25)], INK, 2.5)
    down = line(39, 16, 39, 37, AMBER, 5) + poly([(30.5, 35), (39, 46.5), (47.5, 35)], AMBER, 2.5)
    return up + down


@reg("barony", DEEP_ORANGE)
def barony():
    shield = path("M17 14H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    b = stroke("M22.5 23C23.5 20.5 25.5 19.5 28 19.5H34A5 5 0 0 1 34 29.5H28.5"
               "M34 29.5A5.8 5.8 0 0 1 34 41H28.5V19.5", HOLE, 3.8)
    return shield + b


@reg("barotrauma", TEAL_DARK)
def barotrauma():
    helm = rrect(20, 12, 24, 7.5, 3, INK) + rrect(26.5, 10.5, 11, 4, 2, INK)
    shaft = rrect(28.5, 17, 7, 25, 3.5, INK) + poly([(28.5, 38), (35.5, 38), (34, 47.5), (29.5, 44)], INK, 2)
    tent = stroke("M28 44C23.5 42 22.5 37.5 25.5 35C28 33 27.5 29.5 25 28.5", RED_LIGHT, 2.6)
    return helm + shaft + tent


@reg("barrier", CYAN_DARK)
def barrier():
    a = stroke("M18.5 20C17 30 21 39 31 42", INK, 5.5)
    b = stroke("M26 41C28 30 35.5 23.5 46.5 23", CYAN_SOFT, 5.5)
    spirals = (_ring(19.5, 15.5, 4.2, INK, 2.6) + circle(19.5, 15.5, 1.5, INK) +
               _ring(35, 42.5, 4.2, INK, 2.6) + circle(35, 42.5, 1.5, INK))
    return a + b + spirals


@reg("bashtop", RED_DARK)
def bashtop():
    out = ""
    for x, y, w in [(22, 13, 17), (22, 19.3, 7), (35, 19.3, 7), (22, 25.6, 17),
                    (22, 31.9, 7), (35, 31.9, 7), (22, 38.2, 17)]:
        out += rrect(x, y, w, 5.2, 1.2, INK)
    return out


_APPLE = ("M32 21C29 19 23 18.5 19.5 22.5C15.5 27 16.5 35 20.5 41C23 44.8 25.5 47 28 46.5"
          "C29.5 46.2 30.5 45.5 32 45.5C33.5 45.5 34.5 46.2 36 46.5C38.5 47 41 44.8 43 42"
          "C44.5 40 45.5 38 46 36.5C42.5 35 40.5 32 40.5 28.5C40.5 25.5 42 23.2 44.2 22"
          "C42 19.5 39 18.5 36.5 19C34.5 19.3 33.5 20.3 32 21Z")


@reg("basilisk2", BLUE_GREY_DARK)
def basilisk2():
    cols = [BROWN_SOFT, AMBER_LIGHT, ORANGE, RED, PURPLE_LIGHT, BLUE]
    bands = "".join(rrect(10, 18.5 + 4.8 * k, 44, 5.2 if k < 5 else 10, 0, c) for k, c in enumerate(cols))
    leaf = path("M32 18.5C32 14 35 11 39.5 11C39.5 15.5 36.5 18.5 32 18.5Z", BROWN_SOFT)
    return (f'<clipPath id="lm-apple"><path d="{_APPLE}"/></clipPath>'
            f'<g clip-path="url(#lm-apple)">{bands}</g>' + leaf)


@reg("basingstoke", DEEP_PURPLE_DEEP)
def basingstoke():
    skull = path("M16 26C16 17 23 13 32 13C41 13 48 17 48 26V36H43V45H21V36H16Z", INK,
                 f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return skull + circle(25, 27, 4.8, HOLE) + circle(39, 27, 4.8, HOLE)


@reg("bastion", BLUE_DEEP)
def bastion():
    cog = gear_e(35, 33, 13.5, 9, 5, 3.5, BLUE_SOFT, 10)
    skull = path("M17 27C17 19 23 14 31.5 14C40 14 46 19 46 27C46 31 44.5 34 42 36V41"
                 "H38V38H35V41H31V38H28V41H24V36C19.5 34 17 31 17 27Z", INK)
    eyes = (poly([(22, 26.5), (28.5, 28.5), (25.5, 31)], HOLE, 1.5) +
            poly([(41, 26.5), (34.5, 28.5), (37.5, 31)], HOLE, 1.5))
    spots = circle(32, 17.8, 1.8, RED_LIGHT) + ellipse_f(33, 21.5, 3, 1.8, RED_LIGHT)
    return cog + skull + eyes + spots


@reg("battleblock-theater", GREY_DEEP)
def battleblock():
    posts = "".join(rrect(x - 2.8, 24, 5.6, 22, 1.5, BLUE_SOFT) + circle(x, 24, 4.2, INK)
                    for x in (20, 44))
    return posts + line(14.5, 37, 49.5, 37, INK, 3.2)


@reg("bauh", BROWN)
def bauh():
    top = poly([(32, 23), (47, 29.5), (32, 36), (17, 29.5)], INK, 2.5)
    left = poly([(17, 29.5), (32, 36), (32, 48), (17, 41.5)], BROWN_SOFT, 2.5)
    right = poly([(47, 29.5), (32, 36), (32, 48), (47, 41.5)], BROWN_DEEP, 2.5)
    globe = (circle(32, 20.5, 8.8, INK) + circle(32, 20.5, 6.5, BLUE) +
             path("M28 17C30 16 32 17.5 31 19.5C30 21 32 22.5 34 21.5L35.5 24"
                  "C33 25.5 29 25 27.5 22.5C26.5 20.5 26.8 18 28 17Z", CYAN))
    return top + left + right + globe


@reg("bazecor", PINK_DEEP)
def bazecor():
    outer = cut("M15 18.5L37.5 13L49 18L33 47.5L15 25Z"
                "M22 23.5L39 19.5L32.5 36.5Z", INK)
    fold = poly([(39, 19.5), (49, 18), (33, 47.5), (32.5, 36.5)], PINK_SOFT, 1)
    return outer + fold


@reg("bbc", RED_DEEP)
def bbc():
    out = ""
    b = "M-2.4 -3.2H.8A1.6 1.6 0 0 1 .8 0H-2.4M.8 0A1.6 1.6 0 0 1 .8 3.2H-2.4V-3.2"
    c = "M2.6 -2.2A3.2 3.2 0 1 0 2.6 2.2"
    for k, d in enumerate([b, b, c]):
        cx = 18.5 + 13.5 * k
        out += rrect(cx - 5.8, 24.2, 11.6, 11.6, 1.5, INK)
        out += g(stroke(d, HOLE, 1.9), f"translate({f(cx)} 30)")
    return out


@reg("bcompare", BLUE_GREY_DEEP)
def bcompare():
    disc_ = circle(32, 30, 11, INK) + circle(32, 30, 3.2, HOLE)
    red = (stroke("M20 22A15 15 0 0 1 32 15", RED_LIGHT, 4) +
           poly([(15, 18.5), (23.5, 17.5), (21.5, 26)], RED_LIGHT, 1.5))
    blue = (stroke("M44 38A15 15 0 0 1 32 45", BLUE_SOFT, 4) +
            poly([(49, 41.5), (40.5, 42.5), (42.5, 34)], BLUE_SOFT, 1.5))
    return disc_ + red + blue


@reg("beamng-drive", DEEP_ORANGE_DEEP)
def beamng():
    return (line(21, 33, 41.5, 19, INK, 3) + line(41.5, 19, 43, 40.5, INK, 3) +
            circle(21, 33, 7.5, INK) + circle(41.5, 19, 4.6, INK) + circle(43, 40.5, 6.2, INK))


@reg("beast", BLUE_GREY_LIGHT)
def beast():
    out = ""
    daggers = [((28.5, 14), (30.5, 34)), ((42, 19), (33, 34.5)),
               ((16.5, 30.5), (32, 37)), ((46, 31.5), (35, 38))]
    for (hx, hy), (tx, ty) in daggers:
        a = math.degrees(math.atan2(ty - hy, tx - hx))
        L = math.hypot(tx - hx, ty - hy)
        dag = (rrect(-4, -3.2, 10, 6.4, 1.8, INK) +
               poly([(6, -1.8), (L, 0), (6, 1.8)], INK, 1))
        out += g(dag, f"translate({f(hx)} {f(hy)}) rotate({f(a)})")
    return out


def _beat_face():
    face = _ring(32, 30, 15, INK, 3.2)
    shades = path("M19.5 24H44.5L43.5 27C43 30 41 31.5 38.5 31.5C36 31.5 34 30 33.5 27.5H30.5"
                  "C30 30 28 31.5 25.5 31.5C23 31.5 21 30 20.5 27Z", INK)
    smile = stroke("M25.5 36.5Q32 41 38.5 36.5", INK, 2.6)
    return face + shades + smile


@reg("beat-hazard", AMBER)
def beat_hazard():
    return _beat_face()


@reg("beat-hazard-2", AMBER)
def beat_hazard2():
    badge = circle(42.5, 40.5, 8.5, RED_DEEP)
    two = stroke("M39.5 38.2C39.5 36.3 41 35.3 42.6 35.3C44.3 35.3 45.6 36.4 45.6 38"
                 "C45.6 40.3 41.6 42.2 39.5 45.3H45.8", HOLE, 2.2)
    return g(_beat_face(), "translate(-3 -2) scale(1)") + badge + two


@reg("beat-saber", BLUE_GREY_DARK)
def beat_saber():
    block = rrect(21, 19, 22, 22, 4, INK) + stroke("M26 26L32 32L38 26", HOLE, 3)
    red = line(15, 14, 45, 44, RED_LIGHT, 3) + line(45, 44, 49, 48, INK, 4)
    blue = line(49, 14, 19, 44, BLUE_LIGHT, 3) + line(19, 44, 15, 48, INK, 4)
    return block + red + blue


@reg("becalm", DEEP_PURPLE)
def becalm():
    moon = circle(22, 20, 5, INK)
    sail = poly([(38, 13.5), (38, 35), (28, 35)], INK, 2)
    hull = path("M24 37H48L45 42H27Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    waves = (stroke("M15 41C19 38.5 22 38.5 25 41", DEEP_PURPLE_SOFT, 2.6) +
             stroke("M15 46.5C19.5 44 24 44 28 46.5C32 49 36.5 49 40.5 46.5C43.5 44.5 46.5 44.5 49 46", DEEP_PURPLE_SOFT, 2.6))
    return moon + sail + line(38, 13.5, 38, 37, INK, 1.8) + hull + waves


@reg("beekeeper-studio", AMBER)
def beekeeper():
    b = stroke("M24 13V34A8.5 8.5 0 1 0 32.5 25.5H30", INK, 5)
    ticks = line(35, 29, 35, 33, INK, 2.2) + line(38.5, 29, 38.5, 33, INK, 2.2)
    return g(b, "translate(0 2)") + ticks


@reg("beeper", INDIGO)
def beeper():
    top = stroke("M22 30V22A8 8 0 0 1 30 14H35A8 8 0 0 1 35 30H29", INK, 4)
    bot = path("M22 32H36A7.5 7.5 0 0 1 36 47H22Z", INK)
    tail = poly([(22, 36), (29, 36), (22, 42)], HOLE, 1.5)
    return top + bot + tail


BEHOLDER_HEAD = path('M17 30C17 20 23.5 13.5 32 13.5C36 13.5 39 14.5 41.5 16.5L45 13L44 18L48.5 16.5L46.5 21C47.5 24 48 27 48 30C48 40 41 46.5 32 46.5C23 46.5 17 40 17 30Z', INK)


def _beholder():
    head = BEHOLDER_HEAD
    eyes = (path("M24 32C25 28.5 29 27.5 32 29.5C30 31 27 32 24 32Z", HOLE) +
            path("M37 32C38 30 40.5 29 43 30.5C42 31.5 39.5 32.2 37 32Z", HOLE))
    return head + eyes


@reg("beholder", GREY_DARK)
def beholder():
    return _beholder()


@reg("beholder-2", GREY_DARK)
def beholder2():
    two = stroke("M39.5 38.2C39.5 36.3 41 35.3 42.6 35.3C44.3 35.3 45.6 36.4 45.6 38"
                 "C45.6 40.3 41.6 42.2 39.5 45.3H45.8", INK, 2.2)
    return (g(_beholder(), "translate(-3 -2)") + circle(42.5, 40.5, 9.5, HOLE) +
            circle(42.5, 40.5, 8.5, DEEP_ORANGE_DEEP) + two)


@reg("bendy-and-the-ink-machine", AMBER)
def bendy():
    head = _ring(32, 31, 14.5, INK, 3)
    cap = path("M17.5 31C17.5 22 24 16.5 32 16.5C40 16.5 46.5 22 46.5 31"
               "C44 27 40 25 36.5 25C34.5 25 33 26 32 28C31 26 29.5 25 27.5 25"
               "C24 25 20 27 17.5 31Z", INK)
    horns = (path("M20 21C17 18 16 14.5 17 11.5C19.5 14 22.5 15.5 25.5 16.5Z", INK) +
             path("M44 21C47 18 48 14.5 47 11.5C44.5 14 41.5 15.5 38.5 16.5Z", INK))
    eyes = "".join(path(f"M{x - 3.2} 30A3.3 3.3 0 1 0 {x + 3.2} 30L{x} 31.5Z", INK) for x in (26, 38))
    grin = path("M22.5 35.5Q32 44 41.5 35.5Q32 39.5 22.5 35.5Z", INK,
                f' stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"')
    return head + cap + horns + eyes + grin


@reg("beneath-a-steel-sky", GREY_LIGHT)
def steel_sky():
    towers = [(15, 30, 6), (21, 20, 5), (26, 34, 5), (31, 14, 6), (37, 26, 5), (42, 18, 5), (47, 32, 3)]
    out = ""
    for x, top, w in towers:
        out += rrect(x, top, w, 47 - top, 1, INK)
    out += line(33.5, 14, 33.5, 10.5, INK, 1.6) + line(44.5, 18, 44.5, 14, INK, 1.6)
    out += "".join(rrect(x + 1.5, y, 2, 2.4, .5, HOLE) for x, y in [(31, 20), (31, 27), (21, 26), (42, 24), (42, 31)])
    return out


@reg("besiege", RED_DEEP)
def besiege():
    rod = line(14.5, 13.5, 49.5, 13.5, INK, 2.4) + poly([(13, 13.5), (17, 11), (17, 16)], INK, 1) + \
        poly([(51, 13.5), (47, 11), (47, 16)], INK, 1)
    banner = path("M19 15.5H45V40L32 48L19 40Z", INK)
    tower = path("M25.5 21H28.5V23.5H30.5V21H33.5V23.5H35.5V21H38.5V27H36V40.5H28V27H25.5Z", HOLE)
    door = path("M30.5 40.5V35A1.5 1.5 0 0 1 33.5 35V40.5Z", INK)
    return rod + banner + tower + door


@reg("bespoke_icon", CYAN_DARK)
def bespoke():
    b = line(23, 14, 23, 41, INK, 4.8) + _ring(30.5, 33.5, 7.5, INK, 4.8)
    top = circle(17, 13.5, 2.2, CYAN_SOFT) + poly([(44, 12), (49, 12), (46.5, 15.5)], CYAN_SOFT, 1)
    return g(b, "translate(0 -1)") + top + circle(32, 46, 2.8, CYAN_SOFT)


@small("babe")
def babe_s():
    return _pixheart(_HEART_S, 7.4, 6.4)


@small("bbc")
def bbc_s():
    return "".join(rrect(18.5 + 13.5 * k - 6, 24, 12, 12, 1.5, INK) for k in range(3))


@small("avimetaedit")
def avimetaedit_s():
    return (stroke("M14.5 41L20.5 19L26.5 41", INK, 3.2) +
            stroke("M30.5 19L36.5 41L42.5 19", INK, 3.2) + line(48.5, 19, 48.5, 41, INK, 3.2))


@small("avidemux")
def avidemux_s():
    return (rrect(14, 21, 36, 26, 4, INK) + g(rrect(14, 12, 36, 6.5, 2.5, INK), "rotate(-8 14 18.5)") +
            rrect(20, 27, 15, 14, 2.5, HOLE) + poly([(35, 34), (44, 28.5), (44, 39.5)], HOLE, 1.5))


@small("awgg")
def awgg_s():
    return circle(32, 29, 16, INK) + path("M28 18H36V31H42.5L32 44L21.5 31H28Z", PINK_LIGHT,
                                          f' stroke="{HOLE}" stroke-width="1.6" stroke-linejoin="round"')


@small("azpainter")
def azpainter_s():
    return (stroke("M16 45C19 32 27 22 40 17", INK, 3.4) + stroke("M22 46C26 37 33 31 44 28", INK, 3.4) +
            line(48, 12, 40, 23, AMBER_SOFT, 4.5, "butt"))


@small("azuredatastudio")
def azuredatastudio_s():
    can = path("M15 17V40A11 4.5 0 0 0 37 40V17Z", INK) + ellipse_f(26, 17, 11, 4.5, INK)
    cog = circle(41, 39, 11, HOLE) + gear_e(41, 39, 7, 6, 4.5, 2.6, INK) + circle(41, 39, 2.8, HOLE)
    return can + cog


@small("baka-mplayer")
def baka_s():
    head = BAKA_HEAD
    return head + "".join(circle(x, 31, 7, HOLE) + circle(x, 31, 3.2, INK) for x in (24, 40))


@small("beast")
def beast_s():
    out = ""
    for (hx, hy), (tx, ty) in [((28, 13), (31, 35)), ((46, 22), (34, 36)), ((16, 31), (31, 38))]:
        a = math.degrees(math.atan2(ty - hy, tx - hx))
        L = math.hypot(tx - hx, ty - hy)
        dag = rrect(-4, -3.8, 11, 7.6, 2, INK) + poly([(7, -2.4), (L, 0), (7, 2.4)], INK, 1)
        out += g(dag, f"translate({f(hx)} {f(hy)}) rotate({f(a)})")
    return out


def _beat_face_s():
    face = _ring(32, 30, 15.5, INK, 2.2)
    shades = path("M18.5 23H45.5L44.5 27C44 30.5 41.5 32.5 38.5 32.5C35.5 32.5 33.5 30.5 33 28H31"
                  "C30.5 30.5 28.5 32.5 25.5 32.5C22.5 32.5 20 30.5 19.5 27Z", INK)
    return face + shades + stroke("M25 37Q32 42 39 37", INK, 2.2)


@small("beat-hazard")
def beat_hazard_s():
    return _beat_face_s()


@small("beat-hazard-2")
def beat_hazard2_s():
    return (g(_beat_face_s(), "translate(-3 -2)") + circle(43, 41, 9, RED_DEEP) +
            stroke("M40 38.5C40 36.5 41.3 35.5 43 35.5C44.8 35.5 46 36.7 46 38.2"
                   "C46 40.5 42 42.5 40 45.8H46.3", HOLE, 1.8))


def _beholder_s():
    head = BEHOLDER_HEAD
    eyes = (path("M21.5 33C23 27.5 29 26 33 29.5C30 32 26 33 21.5 33Z", HOLE) +
            path("M36 33C37.5 29.5 41.5 28 45 30.5C43.5 32.3 40 33.2 36 33Z", HOLE))
    return head + eyes


@small("beholder")
def beholder_s():
    return _beholder_s()


@small("beholder-2")
def beholder2_s():
    two = stroke("M40 38.5C40 36.5 41.3 35.5 43 35.5C44.8 35.5 46 36.7 46 38.2"
                 "C46 40.5 42 42.5 40 45.8H46.3", INK, 1.8)
    return (g(_beholder_s(), "translate(-3 -2)") + circle(43, 41, 10, HOLE) +
            circle(43, 41, 9, DEEP_ORANGE_DEEP) + two)
