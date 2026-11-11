# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 63: servo to sm.puri.Chatty.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
palette step.
"""
import math
from lm import (
    AMBER, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_LIGHT, BLUE_SOFT, BROWN_DEEP, BROWN_LIGHT, BROWN_SOFT, circle, cpath, cut, CX, CY,
    CYAN_DEEP, CYAN_LIGHT, DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_LIGHT, g, GREY, GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INK, INK_SLATE,
    LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE, ORANGE_DARK, ORANGE_LIGHT,
    path, PINK_LIGHT, poly, pt, PURPLE_LIGHT, RED, RED_DARK, RED_DEEP, RED_LIGHT, rrect, stroke,
    TEAL, TEAL_DEEP, TEAL_SOFT, YELLOW, YELLOW_DARK, YELLOW_SOFT,
)
from glyphs.kit import _gear_k, registry, _ring

ICONS, SMALL, reg, small = registry()


def _aperture(n, r=16, core=6, w=2, rot=-90):
    """Camera iris: n blades, each edge of the centre polygon run out to the rim."""
    out = circle(CX, CY, r, INK)
    vs = [pt(CX, CY, core, rot + 360 / n * k) for k in range(n)]
    out += poly(vs, HOLE, 1)
    for k in range(n):
        (x0, y0), (x1, y1) = vs[k], vs[(k + 1) % n]
        dx, dy = x1 - x0, y1 - y0
        ln = math.hypot(dx, dy)
        dx, dy = dx / ln, dy / ln
        fx, fy = x1 - CX, y1 - CY
        b = fx * dx + fy * dy
        c = fx * fx + fy * fy - r * r
        t = -b + math.sqrt(b * b - c)
        out += line(x0, y0, x1 + dx * t, y1 + dy * t, HOLE, w)
    return out


@reg("servo", TEAL)
def servo():
    out = circle(CX, CY, 16, INK)
    core = [pt(CX, 29, 7.5, 90 + 72 * k) for k in range(5)]
    out += poly(core, HOLE, 2)
    for (x, y), a in ((core[0], 90), (core[2], 234), (core[3], 306)):
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        fx, fy = x - CX, y - CY
        b = fx * dx + fy * dy
        t = -b + math.sqrt(b * b - (fx * fx + fy * fy - 16 ** 2))
        out += line(x, y, x + dx * t, y + dy * t, HOLE, 2.4, "butt")
    return out


@reg("session-desktop", GREY_DEEP)
def session():
    top = stroke("M41 22.5V19.5A5 5 0 0 0 36 14.5H26A5 5 0 0 0 21 19.5V21.5"
                 "A5 5 0 0 0 26 26.5H34", INK, 4)
    bot = stroke("M30 33.5H38A5 5 0 0 1 43 38.5V40.5A5 5 0 0 1 38 45.5H28"
                 "A5 5 0 0 1 23 40.5V37.5", INK, 4)
    return g(top + bot, "translate(32 30) scale(.95) translate(-32 -30)")


@reg("sftpclient", LIGHT_BLUE_DEEP)
def sftpclient():
    cloud = path("M20 40A7 7 0 0 1 19 26A9.5 9.5 0 0 1 37 21.5A8 8 0 0 1 47 29"
                 "A5.5 5.5 0 0 1 45.5 40Z", INK)
    rack = "".join(rrect(30, y, 19, 4, 2, LIGHT_BLUE_SOFT) + circle(45.5, y + 2, 1, LIGHT_BLUE_DARK)
                   for y in (34, 39.5, 45))
    return g(cloud, "translate(-3 -4)") + rack


@reg("sfxr-qt", BLUE_GREY)
def sfxr():
    out = ""
    for y, x in ((19, 24), (30, 36), (41, 28)):
        out += rrect(15, y - 2, 34, 4, 2, BLUE_GREY_DARK)
        out += circle(x, y, 5.2, INK)
    return out


@reg("sgt-launcher", GREY_DARK)
def sgt():
    tl = circle(23, 21, 6.5, INK)
    tr = rrect(39.5, 13.5, 4.5, 15, 1.5, INK) + rrect(34.5, 18.5, 15, 4.5, 1.5, INK)
    bl = poly([(23, 32.5), (30, 45), (16, 45)], INK, 2.5)
    br = rrect(42.5, 32, 3.2, 15, 1.4, INK) + poly([(43, 33), (43, 40.5), (34.5, 36.75)], INK, 2)
    return tl + tr + bl + br


def _shadow():
    big = cut(cpath(CX, CY, 16.5) + cpath(34, 28, 12.5), INK)
    small = circle(22.5, 39.5, 7.5, HOLE) + _ring(22.5, 39.5, 5.2, INK, 3.6)
    return big + small


@reg("shadow", BLUE_GREY_DARK)
def shadow():
    return _shadow()


@reg("shadow-beta", BLUE_GREY_DARK)
def shadow_beta():
    badge = circle(45, 17, 8.5, HOLE) + circle(45, 17, 7, DEEP_ORANGE)
    beta = stroke("M43 23.5V14A2.8 2.8 0 0 1 48.6 14A2.5 2.5 0 0 1 45.2 16.6"
                  "A2.7 2.7 0 1 1 43 20.8", INK, 2.2)
    return g(_shadow(), "translate(-2 2) translate(32 30) scale(.92) translate(-32 -30)") + badge + beta


@reg("shadow-dev", BLUE_GREY_DARK)
def shadow_dev():
    badge = circle(45, 17, 8.5, HOLE) + circle(45, 17, 7, RED)
    alpha = stroke("M49 13.5C48 18.5 46.5 20.5 43.8 20.5A2.8 3.3 0 1 1 43.8 13.9"
                   "C46 13.9 47.3 17.5 49 20.5", INK, 2.2)
    return g(_shadow(), "translate(-2 2) translate(32 30) scale(.92) translate(-32 -30)") + badge + alpha


@reg("shadow-tactics", RED_DARK)
def shadow_tactics():
    disc_ = circle(CX, CY, 16.5, INK)
    hat = poly([(24, 20.5), (33, 15.5), (40, 20.5)], HOLE, 1.5)
    head = circle(32.5, 22.5, 2.6, HOLE)
    body = poly([(29, 25), (36, 25), (38, 36), (35.5, 36), (35, 46), (32.5, 46),
                 (32, 38), (30.5, 46), (28, 46), (28.5, 36), (27, 36)], HOLE, 1.5)
    sword = line(21, 43, 44, 30, HOLE, 2.2)
    return disc_ + hat + head + body + sword


@reg("shadowsocks-qt5", GREY)
def shadowsocks():
    plane = poly([(14.5, 30), (48, 14), (38.5, 46), (30.5, 36.5)], INK, 2.5)
    fold = poly([(30.5, 36.5), (48, 14), (29.5, 43.5)], GREY_SOFT, 1.5)
    return plane + fold


@reg("shadps4", INDIGO)
def shadps4():
    four = stroke("M35 45V17L18 37H43", INK, 4.6)
    ring = _ring(20, 18, 4, INK, 2.4)
    x = stroke("M42 36.5L48 42.5M48 36.5L42 42.5", INK, 2.4)
    return g(four, "translate(-1.5 -1)") + ring + x


@reg("shadwen", DEEP_PURPLE_DEEP)
def shadwen():
    sigma = path("M18 13H45V20H41.5L40 17H26.5L35.5 30L26.5 43H40L41.5 40H45V47H18"
                 "L29.5 30Z", INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return sigma


@reg("sharik", DEEP_PURPLE_LIGHT)
def sharik():
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 13, HOLE) +
            stroke("M22.5 40.5C25 31 34 22.5 43.5 19.5", INK, 4.2))


@reg("sheepy-a-short-adventure", BLUE_GREY_DEEP)
def sheepy():
    ears = rrect(12.5, 22, 7, 11, 3.5, INK) + rrect(44.5, 22, 7, 11, 3.5, INK)
    head = rrect(16.5, 13, 31, 29, 13, INK)
    visor = rrect(21, 20, 22, 14, 7, HOLE)
    eyes = circle(27, 26.5, 2.3, INK) + circle(37, 26.5, 2.3, INK)
    body = path("M22 41H42L43 48H21Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return body + ears + head + visor + eyes + rrect(30, 29.5, 4, 2.2, 1.1, INK)


@reg("sheets", BLUE_GREY)
def sheets():
    bars = "".join(rrect(x, 30 - h, 5, h, 1.5, INK) for x, h in
                   ((16, 7), (23.5, 12), (31, 9), (38.5, 16)))
    base = rrect(14, 33, 36, 15, 3, INK)
    cells = "".join(rrect(17 + c * 11, 36 + r * 5.5, 8, 3, 1.2, HOLE)
                    for r in range(2) for c in range(3))
    return g(bars, "translate(2 0)") + base + cells


@reg("shellnoob", DEEP_ORANGE_DARK)
def shellnoob():
    return (stroke("M17 20L27 29L17 38", INK, 4.6) +
            line(31.5, 40, 46, 40, INK, 4.6))


@reg("shotcut", CYAN_DEEP)
def shotcut():
    sq = rrect(16, 16, 32, 28, 3.5, INK)
    gap = rrect(29.2, 14, 7.6, 32, 0, HOLE)
    bar = rrect(30.5, 11, 5, 38, 2.5, INK)
    return sq + gap + bar


@reg("showtime", INDIGO)
def showtime():
    tri = poly([(17, 13.5), (48, 30), (17, 46.5)], INK, 5)
    inner = poly([(22, 30), (32, 23.5), (32, 36.5)], HOLE, 3)
    return g(tri, "translate(1 0)") + g(inner, "translate(1 0)")


@reg("shutter", BLUE_DEEP)
def shutter():
    return _aperture(6, core=5.5, w=2.2, rot=-60)


@reg("shutter-encoder", DEEP_ORANGE_DEEP)
def shutter_encoder():
    return _aperture(5, core=6.5, w=2.4, rot=-90)


@reg("sideka", BLUE)
def sideka():
    body = path("M26 17C30 13.5 42 13.5 46 17C47.5 22 47.5 30 44 37C40.5 43.5 34 47 27 47"
                "C29.5 43 30 38 27.5 33C24 26.5 24 21 26 17Z", INK)
    eyes = circle(32.5, 23.5, 3.6, HOLE) + circle(41, 23.5, 3.6, HOLE)
    pupils = circle(32.5, 23.5, 1.4, INK) + circle(41, 23.5, 1.4, INK)
    beak = poly([(35.3, 27), (38.2, 27), (36.75, 30)], HOLE, 1)
    waves = (stroke("M22 22A10 10 0 0 0 22 36", INK, 2.4) +
             stroke("M17 18A16 16 0 0 0 17 40", INK, 2.4))
    return body + eyes + pupils + beak + waves


@reg("sidekick-browser", RED)
def sidekick():
    s = poly([(20, 13), (44, 13), (44, 19), (27, 21.5), (44, 30), (44, 47),
              (20, 47), (20, 41), (37, 38.5), (20, 30)], INK, 2)
    return s


@reg("sigil", RED_DARK)
def sigil():
    s = stroke("M40.5 18C38 14.5 35 13.5 31.5 13.5C26 13.5 22.5 17 22.5 21.5"
               "C22.5 30 41.5 29 41.5 38C41.5 43 37 46.5 31.5 46.5C27 46.5 24 44.5 22 41", INK, 4.2)
    return s + circle(41.5, 19.5, 3, INK) + circle(22, 40, 3, INK)


@reg("silksong", RED_DARK)
def silksong():
    mask = path("M32 13C42 13 47.5 21 47.5 30C47.5 40 41 47 32 47C23 47 16.5 40 16.5 30"
                "C16.5 21 22 13 32 13Z", INK)
    horn = path("M32 16C34.5 21 34.5 27 32 33C29.5 27 29.5 21 32 16Z", HOLE)
    eyes = path("M25.5 34a2.7 4.2 0 1 0 0.01 0Z", HOLE) + path("M38.5 34a2.7 4.2 0 1 0 0.01 0Z", HOLE)
    return mask + horn + eyes


@reg("simon", GREY_DARK)
def simon():
    out = ""
    for (dx, dy), c in (((-8, -8), RED_LIGHT), ((8, -8), LIGHT_BLUE_SOFT),
                        ((-8, 8), BLUE_LIGHT), ((8, 8), AMBER_SOFT)):
        out += circle(CX + dx, CY + dy, 8.8, c)
    return out + circle(CX, CY, 7, HOLE) + circle(CX, CY, 5.5, INK)


@reg("simple-image-reducer", ORANGE_DARK)
def simple_image_reducer():
    club = (circle(32, 25.5, 4.6, INK) + circle(27.2, 32, 4.6, INK) + circle(36.8, 32, 4.6, INK) +
            poly([(32, 30), (34.5, 40), (29.5, 40)], INK, 1.5))
    arcs = (stroke("M19 26A14 14 0 0 1 42 18", INK, 3) +
            poly([(44.5, 14), (45.5, 22.5), (37.5, 20)], INK, 1.5) +
            stroke("M45 34A14 14 0 0 1 22 42", INK, 3) +
            poly([(19.5, 46), (18.5, 37.5), (26.5, 40)], INK, 1.5))
    return club + arcs


@reg("simplenote", BLUE_DEEP)
def simplenote():
    base = circle(CX, CY, 16.5, INK)
    s = path("M36.5 16.5C30 14 22.5 17 22.5 23.5C22.5 29.5 28.5 30.5 33 31.5"
             "C36.5 32.3 37.5 34 37.5 36C37.5 40 33 43.5 27.5 43.5C33 46 43 44 43.5 36"
             "C44 29.5 37.5 28 33.5 27C30 26.2 28.5 25 28.5 23C28.5 19.5 32 16.5 36.5 16.5Z", HOLE)
    return base + s


@reg("simplescreenrecorder", RED_DEEP)
def ssr():
    screen = rrect(13.5, 15, 37, 26, 3.5, INK)
    cam = rrect(21.5, 22, 13, 12, 2.5, HOLE) + poly([(35, 28), (42.5, 23), (42.5, 33)], HOLE, 2)
    stand = rrect(18, 43.5, 28, 3.5, 1.75, INK)
    return screen + cam + stand


@reg("simsu", GREY_DEEP)
def simsu():
    out = ""
    grey = {(1, 0), (0, 2), (2, 1)}
    for r in range(3):
        for c in range(3):
            out += rrect(14.5 + c * 12, 12.5 + r * 12, 11, 11, 2, GREY_SOFT if (c, r) in grey else INK)
    d = INK_SLATE
    six = stroke("M22 14.8C19.5 15.3 17.5 17.3 17.5 19.8A2.5 2.5 0 1 0 22.5 19.8A2.5 2.5 0 0 0 17.5 19.8", d, 2.4)
    seven = stroke("M29.3 26.8H34.8L31.3 33.5", d, 2.4)
    two = stroke("M41.4 40A2.6 2.6 0 1 1 46.2 41.6L41.4 45.4H46.8", d, 2.4)
    return out + six + seven + two


@reg("simutrans", BLUE)
def simutrans():
    gear = _gear_k(CX, CY, 13.5, 10, INK, 5, 6)
    body = rrect(22.5, 20, 19, 20, 5, HOLE)
    window = rrect(25, 23, 14, 7, 2, INK)
    lights = circle(27, 35, 1.8, INK) + circle(37, 35, 1.8, INK)
    return gear + body + window + lights


@reg("singular", LIGHT_BLUE_DARK)
def singular():
    loop = stroke("M30 30C26 24 22.5 22 19.5 22C16.5 22 14.5 25.5 14.5 30C14.5 34.5 16.5 38 19.5 38"
                  "C22.5 38 26 36 30 30L42 15", INK, 3)
    lo = stroke("M30 30L42 45", INK, 3)
    fan = (stroke("M36 30L46 20.5", INK, 2.6) + stroke("M36 30L46 39.5", INK, 2.6) +
           stroke("M41 30L49 25", INK, 2.4) + stroke("M41 30L49 35", INK, 2.4))
    return loop + lo + fan


@reg("sioyek", BLUE_DEEP)
def sioyek():
    left = rrect(14.5, 15, 17, 32, 3, ORANGE_LIGHT)
    right = rrect(32.5, 15, 17, 32, 3, INK)
    mark = poly([(26, 11), (32, 11), (32, 29), (29, 25.5), (26, 29)], BLUE_GREY_DARK, 1.5)
    return left + right + mark


@reg("sirikali", LIGHT_BLUE_DEEP)
def sirikali():
    shackle = stroke("M24.5 27V21.5A7.5 7.5 0 0 1 39.5 21.5V27", INK, 4)
    body = rrect(18.5, 26, 27, 21, 4, INK)
    hole = circle(32, 34, 3.2, HOLE) + rrect(30.6, 34, 2.8, 7.5, 1.4, HOLE)
    return shackle + body + hole


@reg("sk1", BLUE_GREY_DARK)
def sk1():
    top = rrect(15, 13, 26, 7, 1.5, BLUE_LIGHT)
    right = rrect(42, 13, 7, 26, 1.5, PINK_LIGHT)
    bot = rrect(23, 40, 26, 7, 1.5, AMBER)
    left = rrect(15, 21, 7, 26, 1.5, INK)
    return top + right + bot + left


@reg("sk1-color-picker", GREY_DARK)
def sk1_picker():
    cols = [PURPLE_LIGHT, RED, ORANGE, YELLOW, CYAN_LIGHT, BLUE]
    out = poly([pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)], INK, 3)
    for k, c in enumerate(cols):
        a = pt(CX, CY, 14.5, -90 + 60 * k)
        b = pt(CX, CY, 14.5, -30 + 60 * k)
        out += poly([(CX, CY), a, b], c, 0.8)
    return out


@reg("skanlite", BLUE_GREY_DEEP)
def skanlite():
    page = rrect(19.5, 13, 25, 34, 2.5, INK)
    scan = rrect(13.5, 25, 37, 5, 2.5, RED_LIGHT)
    return page + rrect(13.5, 23.8, 37, 7.4, 3.7, HOLE) + scan


@reg("skanpage", BLUE_DEEP)
def skanpage():
    doc = rrect(19.5, 15.5, 23, 31, 3, INK)
    lines = "".join(rrect(23, y, w, 2.6, 1.3, HOLE) for y, w in
                    ((27, 16), (32, 16), (37, 10)))
    back = rrect(24, 13, 23, 29, 3, BLUE_SOFT)
    bar = rrect(13.5, 19.5, 37, 4.6, 2.3, INK)
    gap = rrect(13.5, 18.2, 37, 7.2, 3.6, HOLE)
    return back + doc + lines + gap + bar


@reg("skrooge", AMBER_DEEP)
def skrooge():
    coin = circle(CX, CY, 16.5, INK) + _ring(CX, CY, 13.2, HOLE, 1.8)
    euro = (stroke("M38.5 22.5A7.5 8 0 1 0 38.5 37.5", HOLE, 3.2) +
            line(22.5, 28, 33, 28, HOLE, 2.4) + line(22.5, 32.5, 33, 32.5, HOLE, 2.4))
    return coin + g(euro, "translate(1.5 0)")


SKULLGIRLS_HEART = path('M32 46.5C24 40 14 33 14 23.5C14 17.5 18.5 13.5 23.5 13.5C27.5 13.5 30.5 16 32 19C33.5 16 36.5 13.5 40.5 13.5C45.5 13.5 50 17.5 50 23.5C50 33 40 40 32 46.5Z', INK)


@reg("skullgirls", RED_DEEP)
def skullgirls():
    heart = SKULLGIRLS_HEART
    skull = circle(32, 26.5, 8.5, HOLE) + rrect(27, 30, 10, 9, 2.5, HOLE)
    eyes = (poly([(26.5, 23.5), (31, 26), (27, 28.5)], INK, 1.2) +
            poly([(37.5, 23.5), (33, 26), (37, 28.5)], INK, 1.2))
    teeth = line(30.5, 35, 30.5, 38.5, INK, 1.4) + line(33.5, 35, 33.5, 38.5, INK, 1.4)
    return heart + skull + eyes + teeth


@reg("skydrive", BLUE_DEEP)
def skydrive():
    back = path("M17 34A6 6 0 0 1 16.5 22A8.5 8.5 0 0 1 32 18.5A7 7 0 0 1 41 24Z", BLUE_SOFT)
    front = path("M23.5 44A6.5 6.5 0 0 1 23.5 31A9.5 9.5 0 0 1 41 27A7.5 7.5 0 0 1 48.5 36"
                 "A5 5 0 0 1 46 44Z", INK)
    return back + front


@reg("skyrim-script-extender", GREY_DARK)
def skse():
    gear = _gear_k(CX, CY, 13.5, 8, INK, 6.5, 6)
    inner = circle(CX, CY, 10, HOLE)
    dragon = path("M32 20.5L33.8 23.5L39.5 20.5L37.5 26.5L35 28.5L37.5 33.5L33.5 31.5L32 40"
                  "L30.5 31.5L26.5 33.5L29 28.5L26.5 26.5L24.5 20.5L30.2 23.5Z", INK,
                  f' stroke="{INK}" stroke-width="1" stroke-linejoin="round"')
    return gear + inner + dragon


@reg("slade", BROWN_DEEP)
def slade():
    gear = _gear_k(CX, CY, 13.5, 10, INK, 5, 6)
    s = stroke("M38 21.5C36.5 20.5 34.5 20 32.5 20C28.5 20 26 22 26 25C26 30.5 38.5 29 38.5 35"
               "C38.5 38 35.5 40 31.5 40C29 40 27 39.5 25.5 38.5", BLUE_DEEP, 4.2)
    return gear + s


@reg("slay-the-spire", AMBER_DEEP)
def slay_the_spire():
    flame = path("M32 12C33 18 38 20 40.5 26C44 34 40 44 32 46.5C24 44 20 34 23.5 26"
                 "C25 22.5 28 21 28 16C30.5 18 31.5 15 32 12Z", INK)
    gem = poly([(32, 27), (36.5, 34), (32, 42), (27.5, 34)], HOLE, 1.5)
    return flame + gem


@reg("slic3r", YELLOW_DARK)
def slic3r():
    a = path("M17.5 36.5A15 15 0 0 1 43.5 17.5Z", INK)
    b = path("M20.5 42.5L46.5 23.5A15 15 0 0 1 20.5 42.5Z", YELLOW_SOFT)
    return g(a, "translate(-2.2 -1.6)") + g(b, "translate(2.2 1.6)")


@reg("slimbookbattery", BROWN_LIGHT)
def slimbook():
    ring = _ring(CX, CY, 15, INK, 3.6)
    bolt = poly([(35, 17.5), (24.5, 32), (31, 32), (29, 42.5), (39.5, 28), (33, 28)], INK, 1.5)
    return ring + bolt


@reg("slime-rancher", PINK_LIGHT)
def slime_rancher():
    blob = path("M32 14C44 14 49 22 49 32C49 42 42 46.5 32 46.5C22 46.5 15 42 15 32C15 22 20 14 32 14Z", INK)
    eyes = path("M25 24.5a2.6 3.8 0 1 0 0.01 0Z", HOLE) + path("M39 24.5a2.6 3.8 0 1 0 0.01 0Z", HOLE)
    mouth = path("M25 33H39C39 38 36 41 32 41C28 41 25 38 25 33Z", HOLE)
    return blob + eyes + mouth


@reg("slimjet", BLUE)
def slimjet():
    plane = path("M14.5 33L22 30.5L28.5 30.5L22.5 19H27L37.5 29.5H45C48.5 29.5 50 30.5 50 31.5"
                 "C50 32.5 48.5 33.5 45 33.5H37.5L27 44H22.5L28.5 32.5H22Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return g(plane, "translate(0 -1.5)")


@reg("slingscold", GREY_DEEP)
def slingscold():
    body = path("M46 16C40 15.5 33.5 18 29 23L25 27.5L36.5 39L41 35C46 30.5 48.5 24 48 18Z", INK)
    fins = (poly([(27, 25.5), (19.5, 25), (15.5, 30), (23, 31)], INK, 1.5) +
            poly([(38.5, 37), (39, 44.5), (34, 48.5), (33, 41)], INK, 1.5))
    window = circle(39.5, 24.5, 3, HOLE)
    flame = poly([(24.5, 35), (29, 39.5), (18, 46)], INK, 2)
    return body + fins + window + flame


@reg("slingshot", TEAL_DEEP)
def slingshot():
    planet = circle(29, 33, 14, INK)
    land = (path("M18 29C21 25.5 26 26 26.5 29.5C27 33 23 35 19.5 34C17 33 16.5 31 18 29Z", TEAL_SOFT) +
            path("M26 42C28 39 32 39.5 32.5 42.5C32.8 44.5 30 46 27.5 45.5C25.5 45 25 43.5 26 42Z", TEAL_SOFT))
    band = stroke("M37.5 36C44 30 49 21 47 15.5C45.5 11.5 40 14 35 20", RED_LIGHT, 3)
    target = circle(37, 36.5, 6.2, RED_LIGHT) + circle(37, 36.5, 3.4, INK) + circle(37, 36.5, 1.4, RED_LIGHT)
    return planet + land + band + target


CHATTY_BUBBLE = path('M18 14H46A3.5 3.5 0 0 1 49.5 17.5V38.5A3.5 3.5 0 0 1 46 42H37L32 47.5L27 42H18A3.5 3.5 0 0 1 14.5 38.5V17.5A3.5 3.5 0 0 1 18 14Z', INK)


@reg("sm.puri.Chatty", BROWN_SOFT)
def chatty():
    bubble = CHATTY_BUBBLE
    face = (circle(25.5, 24, 2.5, HOLE) + circle(38.5, 24, 2.5, HOLE) +
            stroke("M24 31.5C28 36 36 36 40 31.5", HOLE, 3))
    return bubble + face


def _badge_s(fill, letter):
    return (g(_shadow(), "translate(-3 3) translate(32 30) scale(.85) translate(-32 -30)") +
            circle(44, 18, 10, HOLE) + circle(44, 18, 8.5, fill) + letter)


@small("shadow-beta")
def shadow_beta_s():
    return _badge_s(DEEP_ORANGE, stroke("M41.5 25V15.5A3 3 0 0 1 47.5 15.5A2.6 2.6 0 0 1 44 18"
                                      "A3 3 0 1 1 41.5 22.5", INK, 2.6))


@small("shadow-dev")
def shadow_dev_s():
    return _badge_s(RED, stroke("M48.5 14C47.5 19.5 46 21.5 43 21.5A3 3.6 0 1 1 43 14.3"
                                      "C45.5 14.3 47 18 48.5 21.5", INK, 2.6))


@small("shadow-tactics")
def shadow_tactics_s():
    return (circle(CX, CY, 16.5, INK) + poly([(22, 22), (32, 15), (42, 22)], HOLE, 2) +
            poly([(27.5, 24), (36.5, 24), (38, 46), (26, 46)], HOLE, 2))


@small("shadps4")
def shadps4_s():
    return stroke("M36 46V15L17 38H45", INK, 6)


@small("sheets")
def sheets_s():
    bars = "".join(rrect(x, 29 - h, 7, h, 2, INK) for x, h in ((16, 8), (25, 14), (34, 18)))
    return bars + rrect(14, 32, 36, 16, 3.5, INK) + rrect(18, 37, 28, 3.5, 1.75, HOLE)


@small("shutter")
def shutter_s():
    return _aperture(5, core=6.5, w=3, rot=-90)


@small("shutter-encoder")
def shutter_encoder_s():
    return _aperture(5, core=7, w=3, rot=-90)


@small("sideka")
def sideka_s():
    body = path("M22 17C27 13 42 13 47 17C48.5 23 48 31 44 38C40 44.5 33 47.5 24 47.5"
                "C27 43 27.5 38 25 33C21 26 20.5 21 22 17Z", INK)
    return body + circle(30.5, 24, 4.5, HOLE) + circle(40.5, 24, 4.5, HOLE)


@small("simple-image-reducer")
def sir_s():
    club = (circle(32, 22.5, 6.5, INK) + circle(25, 31.5, 6.5, INK) + circle(39, 31.5, 6.5, INK) +
            poly([(32, 29), (36, 44), (28, 44)], INK, 2))
    return club


@small("simsu")
def simsu_s():
    out = ""
    for r in range(2):
        for c in range(2):
            out += rrect(14 + c * 18.5, 12 + r * 18.5, 17, 17, 3, GREY_SOFT if (c + r) % 2 else INK)
    return out + stroke("M18.5 17H26.5L21 26", INK_SLATE, 3.2) + stroke("M37.5 36A3.8 3.8 0 1 1 44.5 38.5L37.5 44.5H45.5", INK_SLATE, 3.2)


@small("simutrans")
def simutrans_s():
    return (_gear_k(CX, CY, 14, 8, INK, 6.5, 6) + rrect(22.5, 20, 19, 20, 5, HOLE) +
            rrect(25.5, 23.5, 13, 7, 2.5, INK))


@small("singular")
def singular_s():
    loop = stroke("M31 30C27 24 23 22 20 22C16.5 22 14.5 25.5 14.5 30C14.5 34.5 16.5 38 20 38"
                  "C23 38 27 36 31 30L43 15M31 30L43 45", INK, 4)
    return loop + stroke("M38 30L48 22M38 30L48 38", INK, 3.5)


@small("skanpage")
def skanpage_s():
    return (rrect(19, 13, 26, 34, 3.5, INK) + rrect(13, 22.5, 38, 8, 4, HOLE) +
            rrect(13, 24, 38, 5, 2.5, INK) + rrect(23, 35, 18, 3.5, 1.75, HOLE))


@small("skrooge")
def skrooge_s():
    euro = (stroke("M39.5 21.5A8.5 9 0 1 0 39.5 38.5", HOLE, 4) +
            line(22, 27.5, 33, 27.5, HOLE, 3.2) + line(22, 33, 33, 33, HOLE, 3.2))
    return circle(CX, CY, 16.5, INK) + g(euro, "translate(1.5 0)")


@small("skullgirls")
def skullgirls_s():
    heart = SKULLGIRLS_HEART
    skull = circle(32, 27, 9.5, HOLE) + rrect(26.5, 30, 11, 9.5, 3, HOLE)
    return heart + skull + circle(28, 27, 2.6, INK) + circle(36, 27, 2.6, INK)


@small("skyrim-script-extender")
def skse_s():
    return (_gear_k(CX, CY, 14, 8, INK, 7, 6) + circle(CX, CY, 9.5, HOLE) +
            poly([(32, 22), (38, 26), (34.5, 29), (32, 39), (29.5, 29), (26, 26)], INK, 2))


@small("slade")
def slade_s():
    s = stroke("M38.5 21.5C37 20.3 35 19.5 32.5 19.5C28 19.5 25.5 22 25.5 25C25.5 31 39 29 39 35"
               "C39 38.5 35.5 40.5 31.5 40.5C28.5 40.5 26.5 39.8 25 38.5", BLUE_DEEP, 5.2)
    return _gear_k(CX, CY, 14, 8, INK, 6.5, 6) + s


@small("slingshot")
def slingshot_s():
    return (circle(29, 33, 14, INK) + stroke("M37.5 36C44 30 49 21 47 15.5C45.5 11.5 40 14 35 20", RED_LIGHT, 3.5) +
            circle(37, 36.5, 6.5, RED_LIGHT) + circle(37, 36.5, 3, INK))


@small("sm.puri.Chatty")
def chatty_s():
    bubble = CHATTY_BUBBLE
    return bubble + circle(25, 24, 3.2, HOLE) + circle(39, 24, 3.2, HOLE) + stroke("M23.5 31C28 36.5 36 36.5 40.5 31", HOLE, 3.5)
