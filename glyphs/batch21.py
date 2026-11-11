# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 21: desktop-environment-lxqt to distributor-logo-archlabs."""
from lm import (
    AMBER, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_LIGHT,
    BLUE_GREY_SOFT, BLUE_LIGHT, BROWN, BROWN_DEEP, BROWN_LIGHT, BROWN_SOFT, circle, cpath, cut,
    DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE_LIGHT, f, g, GREY_DARK,
    GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INK, LIGHT_BLUE_DEEP, line,
    ORANGE_DARK, ORANGE_DEEP, ORANGE_SOFT, path, poly, pt, PURPLE, PURPLE_DEEP, RED, RED_DARK,
    RED_DEEP, rrect, stroke, TEAL_DARK, TEAL_DEEP, TEAL_LIGHT,
)
from glyphs.kit import badge_d, ellipse_d, gear_c, registry, _ring, star_d
from glyphs.kit import shared_discord

ICONS, SMALL, reg, small = registry()


def nix(cx, cy, s, colour, w):
    """Nix snowflake: six bars round a hexagon, each running past a corner."""
    out = ""
    for k in range(6):
        n = 60 * k + 30
        m = pt(cx, cy, 6.5 * s, n)
        a = pt(m[0], m[1], 3.75 * s, n - 90)
        b = pt(m[0], m[1], 10 * s, n + 90)
        c = pt(m[0], m[1], 6 * s, n + 90)
        d = pt(c[0], c[1], 4 * s, n + 30)
        out += line(a[0], a[1], b[0], b[1], colour, w) + line(c[0], c[1], d[0], d[1], colour, w)
    return out


@reg("desktop-environment-lxqt", LIGHT_BLUE_DEEP)
def lxqt():
    head = circle(38, 17, 3.8, INK) + poly([(40.5, 15), (47.5, 16.5), (40.5, 19)], INK, 1.5)
    body = path("M35 19.5C30.5 23 30.5 29 35 32.5C40 36.5 39 44 31.5 46.5"
                "C36 42.5 35.5 38.5 31.5 35.5C26.5 31.5 27 24 33 18.5Z", INK)
    wings = (stroke("M15 24C19 30.5 24 33 29.5 32.5", INK, 3.4) +
             stroke("M17.5 33.5C21.5 38.5 26 40 31 39", INK, 3.4))
    return head + body + wings


@reg("desktop-environment-tde", INDIGO)
def tde():
    return (gear_c(32, 31, 13.5, INK, HOLE, 8, 8.2) +
            stroke("M26 26H38M32 26V38", INK, 4))


@reg("desktop-environment-unity", PURPLE_DEEP)
def unity():
    return stroke("M24 16V32A8 8 0 0 0 40 32V16", INK, 7)


@reg("desktop-environment-xfce", BLUE_DARK)
def xfce():
    body = path("M17 38C16 31 22 26.5 30 25.5C35 25 38 22.5 40.5 19.5"
                "C42.5 17.5 45.5 17.5 47 19.5L49.5 23.5C48 25 46.5 26 45.5 28"
                "C45.5 34 40.5 39 33 40C27 41 20 41 17 38Z", INK)
    ear = circle(40.5, 17.5, 3.8, INK)
    eye = circle(44.5, 22, 1.3, HOLE)
    tail = stroke("M18 37C13.5 38.5 12.5 43 16 45.5", INK, 2.4)
    feet = line(26, 40, 24.5, 44, INK, 2.4) + line(38, 38.5, 39.5, 43, INK, 2.4)
    return body + ear + eye + tail + feet


@reg("desktop-profiler", DEEP_PURPLE_LIGHT)
def desktop_profiler():
    win = rrect(14, 12, 36, 36, 6, INK) + rrect(17.5, 20, 29, 24.5, 3, HOLE)
    return win + gear_c(32, 32.2, 7.5, INK, HOLE, 8)


@reg("desmume", INDIGO_LIGHT)
def desmume():
    body = rrect(17, 11, 30, 38, 5, INK)
    screens = rrect(21, 14.5, 22, 13, 2, HOLE) + rrect(25, 33, 14, 12, 2, HOLE)
    hinge = line(17.5, 30, 46.5, 30, HOLE, 1.6)
    dpad = line(19.5, 39, 23, 39, HOLE, 1.8, "butt") + line(21.25, 37.25, 21.25, 40.75, HOLE, 1.8, "butt")
    btns = circle(42.8, 37.5, 1.2, HOLE) + circle(42.8, 41, 1.2, HOLE)
    return body + screens + hinge + dpad + btns


@reg("desura", RED)
def desura():
    horns = (poly([(20, 22), (17, 11), (26, 17)], INK, 2.5) +
             poly([(44, 22), (47, 11), (38, 17)], INK, 2.5))
    body = circle(32, 31, 15, INK)
    eye = circle(32, 28, 7, HOLE) + circle(33.2, 27, 3.2, INK)
    mouth = stroke("M27 39.5C30 41.5 34 41.5 37 39.5", HOLE, 2.2)
    return horns + body + eye + mouth


@reg("dev.Cogitri.Health", RED_DEEP)
def health():
    heart = path("M32 46C24 40 15 34 15 24.5C15 19 19 15 24 15C27.5 15 30.5 17 32 20"
                 "C33.5 17 36.5 15 40 15C45 15 49 19 49 24.5C49 34 40 40 32 46Z", INK)
    pulse = stroke("M18 29.5H25L28 24.5L32 35.5L35.5 27.5L37.5 30.5H46", HOLE, 2.6)
    return heart + pulse


@reg("dev.alextren.Spot", BLUE_GREY_DARK)
def spot():
    band = stroke("M19.5 32V25A12.5 12.5 0 0 1 44.5 25V32", INK, 3.2)
    return band + circle(32, 33, 12, INK) + circle(32, 33, 7, AMBER)


@reg("dev.atoft.Reactions", AMBER_DEEP)
def reactions():
    sheet = rrect(30, 12, 18, 36, 4, INK)
    cells = "".join(rrect(33.5, 15.5 + 7.5 * k, 11, 5, 1.5, HOLE) for k in range(4))
    face = circle(24, 31, 11.5, HOLE) + circle(24, 31, 9.5, INK)
    eyes = (stroke("M18.5 26.5L21.5 28.5L18.5 30.5", HOLE, 2.2) +
            stroke("M29.5 26.5L26.5 28.5L29.5 30.5", HOLE, 2.2))
    mouth = path("M19 33H29A5 5 0 0 1 19 33Z", HOLE)
    return sheet + cells + face + eyes + mouth


@reg("dev.boxi.Boxi", BLUE_GREY)
def boxi():
    out = rrect(13, 16, 38, 28, 5, INK) + line(32, 16.5, 32, 43.5, HOLE, 2.2)
    for x in (17, 36):
        out += stroke(f"M{x} 24L{x + 4} 27.5L{x} 31", HOLE, 2.4) + line(x + 5.5, 32, x + 10, 32, HOLE, 2.4)
    return out


@reg("dev.edfloreshz.Done", BROWN_LIGHT)
def done():
    return rrect(15, 13, 34, 34, 8, INK) + stroke("M23 26H41M23 34H41M23 42H33", HOLE, 4)


@reg("dev.geopjr.Collision", AMBER_DEEP)
def collision():
    bars = "".join(rrect(15 + 9 * k, 16, 6.5, 4, 2, INK) + rrect(15 + 9 * k, 40, 6.5, 4, 2, INK)
                   for k in range(4))
    tick = circle(32, 30, 10.5, HOLE) + circle(32, 30, 8.5, INDIGO_LIGHT) + \
        circle(32, 30, 3.2, INK)
    return bars + tick


@reg("dev.mufeed.Wordbook", BLUE_DEEP)
def wordbook():
    book = rrect(17, 12, 30, 35, 4, INK) + line(22.5, 12.5, 22.5, 46.5, HOLE, 2.2)
    w = stroke("M27 21L30.3 32L34 24.5L37.7 32L41 21", HOLE, 2.8)
    mark = poly([(36, 42), (41, 42), (41, 50), (38.5, 47.5), (36, 50)], RED, 1)
    return book + w + mark


@reg("dev.tchx84.Portfolio", BROWN)
def portfolio():
    handle = stroke("M26 19.5V16.5A2.5 2.5 0 0 1 28.5 14H35.5A2.5 2.5 0 0 1 38 16.5V19.5", INK, 3)
    body = rrect(14, 19, 36, 28, 5, INK)
    lock = circle(32, 30.5, 2.8, HOLE) + poly([(30.6, 31), (33.4, 31), (34.2, 37), (29.8, 37)], HOLE, 1)
    return handle + body + lock


@reg("dev.vlinkz.NixSoftwareCenter", INDIGO)
def nix_software():
    handle = stroke("M25 22V19A7 7 0 0 1 39 19V22", INK, 3)
    bag = poly([(14, 21), (50, 21), (48, 48), (16, 48)], INK, 3)
    return handle + bag + nix(32, 34.5, .82, HOLE, 2.4)


@reg("dev.vlinkz.NixosConfEditor", TEAL_DARK)
def nixos_conf():
    braces = (stroke("M17.5 14C13.5 14 14 18 14 22C14 26 13.5 29 11.5 30"
                     "C13.5 31 14 34 14 38C14 42 13.5 46 17.5 46", INK, 3) +
              stroke("M46.5 14C50.5 14 50 18 50 22C50 26 50.5 29 52.5 30"
                     "C50.5 31 50 34 50 38C50 42 50.5 46 46.5 46", INK, 3))
    return braces + nix(32, 30, 1, INK, 2.6)


@reg("devassistant", BLUE_DEEP)
def devassistant():
    back = poly([(19, 13), (48, 13), (48, 42)], INDIGO_DEEP, 3)
    square = poly([(16, 14), (16, 47), (49, 47)], INK, 3)
    hole = poly([(21.5, 29), (21.5, 41.5), (34, 41.5)], HOLE, 1.5)
    return back + square + hole


@reg("devdocs", ORANGE_DEEP)
def devdocs():
    note = path("M19 13H45A3 3 0 0 1 48 16V36L37 47H19A3 3 0 0 1 16 44V16A3 3 0 0 1 19 13Z", INK)
    fold = path("M48 36H40A3 3 0 0 0 37 39V47Z", ORANGE_SOFT)
    key = _ring(24.5, 27, 4.2, HOLE, 3) + line(28.7, 27, 41, 27, HOLE, 3.2)
    return note + fold + key


@reg("devhelp", RED_DEEP)
def devhelp():
    book = rrect(16, 12, 27, 36, 4, INK) + line(21.5, 12.5, 21.5, 47.5, HOLE, 2.2)
    d = stroke("M27 21.5V38.5H30A8.5 8.5 0 0 0 30 21.5Z", HOLE, 3.4)
    tabs = "".join(rrect(44.5, 15 + 9.5 * k, 4.5, 7, 1.8, INK) for k in range(3))
    return book + d + tabs


@reg("devhub", TEAL_LIGHT)
def devhub():
    return (rrect(13, 21, 38, 18, 9, INK) +
            ellipse_d(24.5, 30, 2.8, 4, HOLE) + ellipse_d(39.5, 30, 2.8, 4, HOLE))


def _da():
    pts = [(100, 0), (71.4, 0), (68.6, 2.9), (55.1, 28.6), (50.9, 31.4), (0, 31.4),
           (0, 71), (26.4, 71), (28.8, 73.8), (0, 130.5), (0, 167), (28.6, 167),
           (31.4, 164.1), (44.8, 138.4), (47.7, 135.5), (100, 135.5), (100, 96),
           (73.6, 96), (71.2, 93.1), (100, 36.5)]
    k = .228
    return [(32 - 50 * k + x * k, 11 + y * k) for x, y in pts]


@reg("deviantart", ORANGE_DARK)
def deviantart():
    return poly(_da(), INK, 1.5)


DEVILUTIONX_HORNS = path('M22.5 20C17 18.5 14 14 15 9C17 13 20.5 14.5 25.5 15.5Z', INK) + path('M41.5 20C47 18.5 50 14 49 9C47 13 43.5 14.5 38.5 15.5Z', INK)


@reg("devilutionx", RED_DARK)
def devilutionx():
    horns = (DEVILUTIONX_HORNS)
    skull = path("M20 29C19 20 24.5 14 32 14C39.5 14 45 20 44 29C43.7 32 42.5 34.5 41 36"
                 "V41H23V36C21.5 34.5 20.3 32 20 29Z", INK)
    eyes = (poly([(23.5, 25), (30, 27.5), (28.5, 32), (24.5, 31)], HOLE, 1.5) +
            poly([(40.5, 25), (34, 27.5), (35.5, 32), (39.5, 31)], HOLE, 1.5))
    nose = poly([(32, 32.5), (34, 36.5), (30, 36.5)], HOLE, 1)
    jaw = rrect(24, 40, 16, 8, 2.5, INK)
    teeth = "".join(line(x, 38.5, x, 45.5, HOLE, 1.6) for x in (28, 32, 36))
    return horns + skull + eyes + nose + jaw + teeth


@reg("devpod", DEEP_PURPLE_LIGHT)
def devpod():
    d = path("M20 13H31C41 13 48 20.5 48 30C48 39.5 41 47 31 47H28.5V38H31"
             "C35.5 38 39 34.5 39 30C39 25.5 35.5 22 31 22H29V33H20Z", INK)
    pod = path("M16 47C16 42 19.5 37.5 24.5 37.5C25 37.5 25.8 37.6 26 37.7V47Z", INK)
    return d + pod


@reg("dia", GREY_DARK)
def dia():
    d = stroke("M24 14V44M24 14H28A14 15 0 0 1 28 44H24", INK, 3.6)
    return d + stroke("M19.5 43.5L24 48L28.5 43.5", INK, 3.2)


@reg("diablo-2", ORANGE_DEEP)
def diablo2():
    d = cut("M15 12H31C41.5 12 48.5 19.5 48.5 29C48.5 38.5 41.5 46 31 46H15L18.5 41.5V16.5Z"
            "M26 19H30C35 19 38.5 23 38.5 29C38.5 35 35 39 30 39H26Z", INK)
    ii = (rrect(22, 27, 20, 4, 1.5, RED_DARK) + rrect(25, 27, 4.5, 21, 1.5, RED_DARK) +
          rrect(34.5, 27, 4.5, 21, 1.5, RED_DARK))
    return d + ii


@reg("digikam", BLUE_GREY_DARK)
def digikam():
    return (circle(32, 30, 16.5, INK) + circle(32, 30, 12, HOLE) +
            circle(32, 30, 8.5, BLUE_LIGHT) + circle(29.3, 27.3, 2.8, INK))


@reg("digitallyimported", BLUE_DEEP)
def digitallyimported():
    d = stroke("M17 20.5H27A7 7 0 0 1 34 27.5V32.5A7 7 0 0 1 27 39.5H17V27", INK, 4.2)
    i = circle(42.5, 21, 2.8, INK) + line(42.5, 27, 42.5, 39.5, INK, 4.8)
    return d + i


@reg("dillo", BLUE_DARK)
def dillo():
    globe = circle(29.5, 31, 15, INK)
    d = (_ring(34.5, 36, 5.8, RED, 4) + line(40.3, 14.5, 40.3, 42, RED, 4))
    return globe + d


@reg("ding", ORANGE_DEEP)
def ding():
    pages = rrect(14, 15, 17, 30, 3, INK) + rrect(33, 15, 17, 30, 3, INK)
    q = stroke("M19 24.5A3.8 3.8 0 1 1 24.5 28C23 29 22.5 30 22.5 32", HOLE, 2.6) + circle(22.5, 37.5, 1.7, HOLE)
    lines = "".join(rrect(36.5, y, w, 2.6, 1.3, HOLE) for y, w in [(21, 10), (27, 10), (33, 7), (39, 10)])
    return pages + q + lines


@reg("dino", TEAL_DEEP)
def dino():
    spikes = "".join(poly([pt(31, 30, 13, a - 12), pt(31, 30, 20, a), pt(31, 30, 13, a + 12)], INK, 2)
                     for a in (-70, -35, 0, 35))
    head = path("M16 38C14.5 25 21 15.5 31 15.5C40 15.5 45.5 22 45.5 30C45.5 38.5 40 45 32 46"
                "C27 46.5 20 45 16 38Z", INK)
    eye = circle(23.5, 27, 2.4, HOLE)
    mouth = stroke("M16.5 38C21 40 26 40.5 31 39.5", HOLE, 2.2)
    return spikes + head + eye + mouth


@reg("diodon", BLUE_GREY)
def diodon():
    back = rrect(27, 12, 21, 26, 3, INK) + "".join(
        rrect(31, y, 13, 2.4, 1.2, HOLE) for y in (16, 21))
    front = rrect(16, 21, 22, 27, 3, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    lines = "".join(rrect(20, y, w, 2.6, 1.3, HOLE) for y, w in [(27, 14), (32.5, 14), (38, 14), (43, 9)])
    return back + front + lines


def _dirt_d(x, y, s, colour):
    return g(cut("M0 0H11C18 0 22 5 22 12C22 19 18 24 11 24H0Z"
                 "M7 6.5V17.5H10.5C13.5 17.5 15 15.5 15 12C15 8.5 13.5 6.5 10.5 6.5Z", colour),
             f"translate({f(x)} {f(y)}) scale({f(s)})")


@reg("dirt-rally", GREY_DARK)
def dirt_rally():
    d = _dirt_d(21, 11, 1, INK)
    o = DEEP_ORANGE_LIGHT
    x0, y0, h = 15.5, 39, 8
    letters = [
        "M0 8V0H3A2 2 0 0 1 3 4H0M2.5 4L5 8",
        "M0 8L2.5 0L5 8M1 5.3H4",
        "M0 0V8H4.5",
        "M0 0V8H4.5",
        "M0 0L2.5 4L5 0M2.5 4V8",
    ]
    out = ""
    for k, d_ in enumerate(letters):
        out += g(stroke(d_, o, 2.2), f"translate({f(x0 + 7 * k)} {y0})")
    return d + out


@reg("dirt4", GREY_DARK)
def dirt4():
    d = _dirt_d(14, 12, 1.1, INK)
    four = stroke("M45 47V26L34 40H49", DEEP_ORANGE, 4.5)
    return d + four


def _discord():
    return shared_discord()


@reg("discord-development", GREY_DARK)
@reg("discord-canary", ORANGE_DEEP)
def discord_canary():
    return _discord()


@reg("disk-burner", GREY_DEEP)
def disk_burner():
    disc = cut(cpath(29.5, 28.5, 15.5) + cpath(29.5, 28.5, 4.5), INK)
    hub = _ring(29.5, 28.5, 7, HOLE, 1.6)
    flame = path("M42 34.5C44.8 37 45.8 38.8 45.8 41A3.8 3.8 0 0 1 38.2 41"
                 "C38.2 39.2 39.5 38 40.2 36.5C41.2 37.5 41.6 38.2 41.8 39.2"
                 "C42.4 37.6 42.5 36 42 34.5Z", INK)
    return disc + hub + badge_d(42, 40, DEEP_ORANGE_DEEP) + flame


def _drive():
    body = rrect(15, 12, 30, 34, 5, INK)
    platter = path("M21.5 19H30A8.5 8.5 0 1 1 21.5 27.5Z", HOLE) + circle(30, 27.5, 3.5, INK)
    return body + platter


@reg("disk-usage-analyzer", BLUE_GREY)
def disk_usage():
    info = circle(42, 36.3, 1.5, INK) + line(42, 39.5, 42, 44.3, INK, 2.8)
    return _drive() + badge_d(42, 40, BLUE) + info


@reg("disk-utility", GREY_DARK)
def disk_utility():
    return _drive() + badge_d(42, 40, PURPLE) + gear_c(42, 40, 3.8, INK, PURPLE, 8, 1.6)


@reg("display.im6", INDIGO)
def imagemagick():
    hat = path("M14 44C18 40 20.5 32 23 24C25.5 16.5 31 12 37.5 12C42.5 12 46.5 15 49 19.5"
               "C46 17.5 43 17.5 41 19.5C40.5 27 43 35 47.5 41C46 45 38.5 47 30.5 47"
               "C22.5 47 16.5 46 14 44Z", INK)
    stars = star_d(25.5, 36, 5.2, AMBER) + star_d(34, 26, 4.6, AMBER) + star_d(37.5, 39, 4.2, AMBER)
    return hat + stars


@reg("dissenter-browser", LIGHT_BLUE_DEEP)
def dissenter():
    bubble = path("M19 15H33A15 15 0 0 1 33 45H19A4 4 0 0 1 15 41V19A4 4 0 0 1 19 15Z", INK)
    lines = "".join(rrect(21, y, w, 3.4, 1.7, HOLE) for y, w in [(21.5, 19), (28.3, 19), (35.1, 13)])
    return bubble + lines


@reg("distributor-logo-absolute", BROWN_DEEP)
def absolute():
    block = rrect(14, 12, 23, 23, 3, INK)
    a = stroke("M20 18.5H27.5A2.5 2.5 0 0 1 30 21V29M30 23.5H22.5A2.5 2.5 0 0 0 20 26V26.5"
               "A2.5 2.5 0 0 0 22.5 29H30", HOLE, 2.6)
    tall = rrect(40, 12, 10, 23, 2.5, BROWN_SOFT)
    wide = rrect(14, 38, 23, 10, 2.5, BROWN_SOFT)
    dot = rrect(40, 38, 10, 10, 2.5, INK)
    return block + a + tall + wide + dot


@reg("distributor-logo-academix", BLUE_DEEP)
def academix():
    left = path("M32 13.5A16.5 16.5 0 0 0 32 46.5Z", INDIGO_DARK)
    right = path("M32 13.5A16.5 16.5 0 0 1 32 46.5Z", RED_DEEP)
    a = stroke("M21.5 44L32 16L42.5 44M26.5 34.5H37.5", INK, 4.4)
    return left + right + a


@reg("distributor-logo-aix", BLUE_GREY_LIGHT)
def aix():
    rim = _ring(32, 30, 16, INK, 3)
    a = stroke("M20.5 36L24 24L27.5 36M21.8 32H26.2", INK, 2.8)
    i = line(32, 24, 32, 36, INK, 2.8)
    x = stroke("M36 24L43.5 36M43.5 24L36 36", INK, 2.8)
    return rim + a + i + x


@reg("distributor-logo-alpine", BLUE_DARK)
def alpine():
    hexa = poly([pt(32, 30, 17.5, 60 * k) for k in range(6)], INK, 3)
    mts = (stroke("M17.5 37L27 27.5L32.5 33", HOLE, 4) +
           stroke("M29 37L37 29L46 37", HOLE, 4))
    return hexa + mts


def _penguin(colour, hole):
    body = path("M21 47C18.5 38 19.5 28 24 21C26 16.5 28.5 12.5 32.5 12C35.5 11.7 37.5 13.5 38.2 16"
                "L44.5 18.5L38.5 19.5C38 23.5 38.8 27.5 40.5 32.5C42.3 38 42.3 43 40.5 47Z", colour)
    belly = path("M36.5 21.5C36 26.5 36.5 31.5 38 36.5C39 40 39 44 38 47H33"
                 "C34.5 40 33.8 30 36.5 21.5Z", hole)
    return body + belly + circle(33.5, 15.8, 1.2, hole)


@reg("distributor-logo-alt-linux", AMBER)
def alt_linux():
    big = g(_penguin(INK, HOLE), "translate(4 0)")
    little = g(_penguin(INK, HOLE).replace('fill="INK"', f'fill="INK" stroke="{HOLE}" stroke-width="3" paint-order="stroke"', 1),
               "translate(41 17.5) scale(-.62 .62)")
    return big + little


@reg("distributor-logo-android", BLUE_GREY_LIGHT)
def android():
    dome = path("M16.5 42A15.5 15.5 0 0 1 47.5 42Z", INK)
    ant = line(22.5, 29, 18.5, 22, INK, 2.8) + line(41.5, 29, 45.5, 22, INK, 2.8)
    eyes = circle(25, 36, 2.2, HOLE) + circle(39, 36, 2.2, HOLE)
    return dome + ant + eyes


@reg("distributor-logo-antix", BLUE_GREY_DARK)
def antix():
    sphere = circle(33, 31, 14, BLUE_GREY_SOFT)
    a = stroke("M16 12C25 21 36 35 46 48", HOLE, 8) + stroke("M16 12C25 21 36 35 46 48", INK, 4.5)
    b = stroke("M49 12C39 22 27 36 18 47", HOLE, 8) + stroke("M49 12C39 22 27 36 18 47", INK, 4.5)
    return sphere + a + b


ARCHBANG_ARCH = path('M32 11C37 22 43 34 50 47C44 43.5 38 41.5 32 41.5C26 41.5 20 43.5 14 47C21 34 27 22 32 11Z', INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')


@reg("distributor-logo-archbang", BLUE_DEEP)
def archbang():
    arch = ARCHBANG_ARCH
    bang = poly([(30.2, 22), (33.8, 22), (33, 33), (31, 33)], HOLE, 1.5) + circle(32, 37.3, 2, HOLE)
    return arch + bang


@reg("distributor-logo-archlabs", BLUE_GREY_DARK)
def archlabs():
    arch = ARCHBANG_ARCH
    flame = path("M33 22C38 27 39.5 31 38.5 35C37.5 38.5 35 40 32 40C28.5 40 26 37.5 26 34"
                 "C26 30.5 28.5 29 29.5 26.5C30.5 28 31 29.5 31 31C32.5 29 33.5 26 33 22Z", HOLE)
    return arch + flame


@small("desmume")
def desmume_s():
    return (rrect(17, 11, 30, 38, 5, INK) + rrect(20.5, 14, 23, 14, 2, HOLE) +
            rrect(20.5, 32, 23, 14, 2, HOLE))


@small("dirt-rally")
def dirt_rally_s():
    return _dirt_d(17, 11, 1.2, INK) + rrect(15, 42, 34, 5, 2.5, DEEP_ORANGE_LIGHT)


@small("dev.geopjr.Collision")
def collision_s():
    bars = "".join(rrect(14 + 19.5 * k, 16, 16.5, 5, 2.5, INK) + rrect(14 + 19.5 * k, 39, 16.5, 5, 2.5, INK)
                   for k in range(2))
    return bars + circle(32, 30, 10, GREY_DEEP) + circle(32, 30, 3.4, INK)


@small("dev.atoft.Reactions")
def reactions_s():
    sheet = rrect(30, 12, 18, 36, 4, INK)
    face = circle(24, 31, 12, HOLE) + circle(24, 31, 10, INK)
    return sheet + face + circle(20.5, 28.5, 1.8, HOLE) + circle(27.5, 28.5, 1.8, HOLE) + \
        path("M18.5 33H29.5A5.5 5.5 0 0 1 18.5 33Z", HOLE)


@small("devilutionx")
def devilutionx_s():
    horns = (DEVILUTIONX_HORNS)
    skull = path("M20 29C19 20 24.5 14 32 14C39.5 14 45 20 44 29C43.7 32 42.5 34.5 41 36"
                 "V47H23V36C21.5 34.5 20.3 32 20 29Z", INK)
    return horns + skull + circle(26.5, 28, 3.5, HOLE) + circle(37.5, 28, 3.5, HOLE)


@small("distributor-logo-aix")
def aix_s():
    rim = _ring(32, 30, 17, INK, 2.6)
    return rim + stroke("M18.5 38L23 22L27.5 38", INK, 3.4) + line(32.5, 22, 32.5, 38, INK, 3.4) + \
        stroke("M37 22L45.5 38M45.5 22L37 38", INK, 3.4)


@small("disk-utility")
def disk_utility_s():
    body = rrect(14, 11, 30, 34, 5, INK) + circle(28.5, 26, 7, HOLE)
    return body + circle(42, 40, 10.5, HOLE) + circle(42, 40, 9, PURPLE) + \
        gear_c(42, 40, 4.5, INK, PURPLE, 6, 1.8)


@small("desktop-environment-lxqt")
def lxqt_s():
    head = circle(38, 16.5, 4.5, INK) + poly([(41, 14.5), (48.5, 16.5), (41, 19)], INK, 1.5)
    body = path("M35 19.5C30 23 30 29.5 35 33C40 37 39 44.5 31 47"
                "C35.5 42.5 35 39 30.5 36C25.5 32 26 24 33 18.5Z", INK)
    return head + body + stroke("M15 26C19 33 24 35.5 29 35", INK, 4)


@small("desktop-environment-tde")
def tde_s():
    return gear_c(32, 30, 14.5, INK, HOLE, 6, 9) + stroke("M26 25H38M32 25V38", INK, 4.2)


@small("dev.Cogitri.Health")
def health_s():
    heart = path("M32 47C24 41 14 34.5 14 24.5C14 18.5 18.5 14 24 14C27.5 14 30.5 16 32 19"
                 "C33.5 16 36.5 14 40 14C45.5 14 50 18.5 50 24.5C50 34.5 40 41 32 47Z", INK)
    return heart + stroke("M18 29H25L29 22L33 36L36.5 29H46", HOLE, 3.2)


@small("dev.boxi.Boxi")
def boxi_s():
    out = rrect(12, 15, 40, 30, 5, INK) + line(32, 15.5, 32, 44.5, HOLE, 2.4)
    for x in (17, 37):
        out += stroke(f"M{x} 24L{x + 6} 30L{x} 36", HOLE, 3.2)
    return out


@small("dev.vlinkz.NixSoftwareCenter")
def nix_software_s():
    handle = stroke("M25 21V18A7 7 0 0 1 39 18V21", INK, 3)
    bag = poly([(13, 21), (51, 21), (49, 49), (15, 49)], INK, 3)
    return handle + bag + circle(32, 35, 8.5, HOLE) + circle(32, 35, 4, INK)


@small("dev.vlinkz.NixosConfEditor")
def nixos_conf_s():
    braces = (stroke("M19 13C14.5 13 15 18 15 22C15 26 14.5 29 12 30"
                     "C14.5 31 15 34 15 38C15 42 14.5 47 19 47", INK, 3.4) +
              stroke("M45 13C49.5 13 49 18 49 22C49 26 49.5 29 52 30"
                     "C49.5 31 49 34 49 38C49 42 49.5 47 45 47", INK, 3.4))
    hexa = poly([pt(32, 30, 9.5, 60 * k) for k in range(6)], INK, 2)
    return braces + hexa + circle(32, 30, 4.2, HOLE)


@small("devhelp")
def devhelp_s():
    book = rrect(15, 12, 29, 36, 4, INK)
    d = stroke("M24 20.5V39.5H28A9.5 9.5 0 0 0 28 20.5Z", HOLE, 4)
    tabs = rrect(45.5, 16, 5, 10, 2, INK) + rrect(45.5, 30, 5, 10, 2, INK)
    return book + d + tabs


@small("diodon")
def diodon_s():
    back = rrect(27, 11, 22, 27, 3, INK)
    front = rrect(15, 21, 24, 28, 3, INK, f' stroke="{HOLE}" stroke-width="2.6"')
    lines = "".join(rrect(19.5, y, 15, 3.4, 1.7, HOLE) for y in (28, 35.5))
    return back + front + lines


@small("disk-usage-analyzer")
def disk_usage_s():
    body = rrect(14, 11, 30, 34, 5, INK) + circle(28.5, 26, 7, HOLE)
    return body + circle(42, 40, 10.5, HOLE) + circle(42, 40, 9, BLUE) + \
        line(42, 38, 42, 45, INK, 3) + circle(42, 34, 1.8, INK)


@small("disk-burner")
def disk_burner_s():
    disc = cut(cpath(29.5, 28.5, 16) + cpath(29.5, 28.5, 5), INK)
    return disc + circle(42, 40, 10.5, HOLE) + circle(42, 40, 9, DEEP_ORANGE_DEEP) + \
        path("M42 33.5C45.5 37 46.5 39 46.5 41.5A4.5 4.5 0 0 1 37.5 41.5C37.5 38.5 40 37 42 33.5Z", INK)


@small("distributor-logo-alt-linux")
def alt_linux_s():
    return g(_penguin(INK, HOLE), "translate(32 30) scale(1.1) translate(-30.5 -29.5)")


@small("distributor-logo-absolute")
def absolute_s():
    return (rrect(13, 11, 24, 24, 3, INK) + rrect(40, 11, 11, 24, 3, BROWN_SOFT) +
            rrect(13, 38, 24, 11, 3, BROWN_SOFT) + rrect(40, 38, 11, 11, 3, INK) +
            circle(25, 23, 5, HOLE))
