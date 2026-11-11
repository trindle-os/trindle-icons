# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 25: eiskaltdcpp to etl.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_LIGHT, BLUE_SOFT, BROWN, BROWN_DEEP, BROWN_SOFT, circle, CX, CY, CYAN_DARK,
    CYAN_DEEP, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_SOFT, g, GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DEEP,
    INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line,
    ORANGE, ORANGE_DARK, ORANGE_DEEP, path, PINK, poly, PURPLE, PURPLE_SOFT, RED, RED_DARK,
    RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke, TEAL, TEAL_DEEP, TEAL_LIGHT,
)
from glyphs.kit import ellipse_b, gear_g, registry, ring_b

ICONS, SMALL, reg, small = registry()


@reg("eiskaltdcpp", PINK)
def eiskaltdcpp():
    lines = line(22, 30, 41, 19.5, INK, 3.4) + line(22, 30, 41, 40.5, INK, 3.4)
    return lines + circle(21.5, 30, 6, INK) + circle(41.5, 19, 6, INK) + circle(41.5, 41, 6, INK)


@reg("ekiga", ORANGE_DEEP)
def ekiga():
    hand = stroke("M27 14C21 17 18.5 23.5 18.5 30C18.5 36.5 21 43 27 46", INK, 6)
    caps = rrect(23.5, 11.5, 8, 6.5, 3, INK) + rrect(23.5, 42, 8, 6.5, 3, INK)
    wave = stroke("M25 30H28L30.5 23L33.5 37L36.5 25L39 33L41 30H43", INK, 2.6)
    return hand + caps + wave + circle(46, 30, 2.8, INK)


@reg("electorrent", BLUE_GREY_LIGHT)
def electorrent():
    mag = g(stroke("M22 16V29A10 10 0 0 0 42 29V16", INK, 7.5)
            + line(18, 20.5, 26, 20.5, HOLE, 2.4, "butt") + line(38, 20.5, 46, 20.5, HOLE, 2.4, "butt"),
            "rotate(45 32 30) translate(0 3)")
    waves = stroke("M38 16A9 9 0 0 1 46 24", INK, 2.6) + stroke("M39 10.5A14.5 14.5 0 0 1 51.5 23", INK, 2.6)
    return g(mag + waves, "translate(-2 1)")


ELECTRIP_PAD = path('M22 16H42C47.5 16 50.5 20 50.5 25L51.5 40C52 44 48 46 45.5 43L39.5 36H24.5L18.5 43C16 46 12 44 12.5 40L13.5 25C13.5 20 16.5 16 22 16Z', INK)


@reg("electrip", INDIGO_LIGHT)
def electrip():
    pad = ELECTRIP_PAD
    cross = line(21.5, 22, 21.5, 30, HOLE, 3) + line(17.5, 26, 25.5, 26, HOLE, 3)
    dots = "".join(circle(x, y, 1.9, HOLE) for x, y in [(42, 22.5), (42, 29.5), (38.5, 26), (45.5, 26)])
    return pad + cross + dots


@reg("electron", BLUE_GREY_DARK)
def electron():
    orbits = "".join(ellipse_b(CX, CY, 16.5, 6.5, INK, 2.4, a) for a in (30, 90, 150))
    return orbits + circle(CX, CY, 3.2, INK)


def _btc(colour, w=3.6):
    b = stroke("M27.5 22.5H34C36.5 22.5 38 23.8 38 26C38 28.1 36.5 29.5 34 29.5H27.5"
               "M27.5 29.5H35C37.6 29.5 39.3 31 39.3 33.3C39.3 35.5 37.6 37 35 37H27.5M27.5 20V39.5", colour, w)
    ticks = (line(30.5, 17, 30.5, 20.5, colour, 2.4) + line(34.5, 17, 34.5, 20.5, colour, 2.4) +
             line(30.5, 38.5, 30.5, 42, colour, 2.4) + line(34.5, 38.5, 34.5, 42, colour, 2.4))
    return g(b + ticks, "rotate(14 32 30) translate(-1.5 0)")


@reg("electron-cash", BLUE)
def electron_cash():
    return circle(CX, CY, 17, INK) + _btc(HOLE, 4)


@reg("electron-mail", TEAL_DEEP)
def electron_mail():
    shackle = stroke("M24.5 26V21A7.5 7.5 0 0 1 39.5 21V26", INK, 4)
    env = rrect(15, 25, 34, 22, 3.5, INK)
    flap = stroke("M17.5 27.5L32 38.5L46.5 27.5", HOLE, 2.6)
    return shackle + env + flap


def _orbits(w=2.2):
    return "".join(ellipse_b(CX, CY, 17, 7, INK, w, a) for a in (0, 60, 120))


@reg("electrum", BLUE_DEEP)
def electrum():
    return _orbits() + circle(CX, CY, 9.5, HOLE) + g(_btc(INK, 3), "translate(32 30) scale(.62) translate(-32 -30)")


@reg("electrum-axe", GREY_DEEP)
def electrum_axe():
    a = line(19, 17, 45, 43, INK, 8)
    b = line(45, 17, 19, 43, GREY_SOFT, 8)
    return b + line(28, 26, 36, 34, HOLE, 11, "butt") + a


def _ltc(colour, w):
    return (stroke("M31 18L27 36.5H40", colour, w) + line(24.5, 30, 36, 25.5, colour, w * .8))


@reg("electrum-ltc", LIGHT_BLUE_DEEP)
def electrum_ltc():
    return _orbits() + circle(CX, CY, 9.5, HOLE) + g(_ltc(INK, 4), "translate(32 30) scale(.6) translate(-32 -28)")


@reg("element-desktop-nightly", DEEP_PURPLE)
def element_nightly():
    return "".join(g(stroke("M22.5 25A10.5 10.5 0 0 1 38 17.5", INK, 4.4),
                     f"rotate({90 * k} 32 30)") for k in range(4))


@reg("element4l", LIGHT_BLUE_SOFT)
def element4l():
    eyes = circle(20.5, 27, 4, INK) + circle(43.5, 27, 4, INK)
    return eyes + stroke("M25.5 36C29.5 38.5 34.5 38.5 38.5 36", INK, 3.4)


@reg("elisa", CYAN_DEEP)
def elisa():
    body = rrect(13.5, 16, 37, 27, 4, INK)
    win = rrect(18.5, 21, 27, 10, 5, HOLE)
    reels = circle(24, 26, 3.4, INK) + circle(40, 26, 3.4, INK) + rrect(29.5, 23.5, 5, 5, 1, INK)
    base = path("M22 43L24.5 37.5H39.5L42 43Z", HOLE)
    return body + win + reels + base


@reg("elixir", DEEP_PURPLE_DEEP)
def elixir():
    drop = path("M33 11.5C28 18.5 19.5 27 19.5 36C19.5 43 25 48 32 48C39 48 44.5 43 44.5 36"
                "C44.5 26.5 36.5 21 33 11.5Z", INK)
    swirl = stroke("M31 22C26.5 28 24.5 33 25.5 38C26.2 41.5 29 43.5 32 43.5", DEEP_PURPLE_SOFT, 3)
    return drop + swirl


@reg("emby-server", BROWN_SOFT)
def emby_server():
    d = g(rrect(17.5, 15.5, 29, 29, 5, INK), "rotate(45 32 30)")
    play = poly([(28, 22.5), (39, 30), (28, 37.5)], HOLE, 2.5)
    return d + play


@reg("emerald-theme-manager-icon", ORANGE_DEEP)
def emerald():
    gem = poly([(22, 15), (42, 15), (49.5, 24), (32, 46), (14.5, 24)], INK, 2.5)
    facets = (stroke("M15.5 24H48.5", HOLE, 2.2) + stroke("M26 15.5L23.5 24L32 44.5L40.5 24L38 15.5", HOLE, 2.2)
              + stroke("M23.5 24L32 16L40.5 24", HOLE, 2.2))
    return gem + facets


def _emily():
    win = rrect(13, 13, 38, 32, 4, INK) + rrect(13, 13, 38, 6.5, 0, INK)
    bar = line(15.5, 20, 48.5, 20, HOLE, 2.2)
    note = path("M20 24H38V35C38 38 40 40 42 40H24C21.8 40 20 38.2 20 36Z", AMBER)
    curl = path("M38 35C38 38 40 40 42 40C44 40 45 38.5 45 36.5V33H40C38.9 33 38 33.9 38 35Z", AMBER_DEEP)
    return win + bar + note + curl


@reg("emily-is-away", BLUE_GREY)
def emily_is_away():
    return _emily()


@reg("emily-is-away-too", BLUE_GREY)
def emily_is_away_too():
    badge = circle(44, 42, 8, BLUE_GREY_DARK)
    two = stroke("M40.5 39.5C40.8 37.8 42.2 37 44 37C46 37 47.3 38.3 47.3 40C47.3 42.5 42.5 44 40.5 46.5H47.5", INK, 2.3)
    return g(_emily(), "translate(-2 -1)") + badge + two


@reg("empathy", BLUE)
def empathy():
    bubble = path("M18 13H46A4 4 0 0 1 50 17V39A4 4 0 0 1 46 43H42.5V49.5L36 43H18A4 4 0 0 1 14 39V17A4 4 0 0 1 18 13Z", INK)
    face = circle(CX, 28, 10, HOLE)
    eyes = circle(28.3, 25.5, 1.8, INK) + circle(35.7, 25.5, 1.8, INK)
    smile = stroke("M26.5 30.5C29.5 34 34.5 34 37.5 30.5", INK, 2.3)
    return bubble + face + eyes + smile


@reg("emulationstation", LIGHT_BLUE_DARK)
def emulationstation():
    e = stroke("M28.5 20H17.5V40H28.5M17.5 30H26.5", INK, 5)
    s = stroke("M46 20.5H38.5C35.5 20.5 34 22.5 34 25C34 27.5 35.5 29.5 38.5 29.8H41.5"
               "C44.5 30 46 32.3 46 35C46 37.7 44.5 39.5 41.5 39.5H34", INK, 5)
    return e + s


@reg("emule", BROWN)
def emule():
    ears = (poly([(24, 27), (17, 11), (29, 24)], INK, 3.5) + poly([(40, 27), (47, 11), (35, 24)], INK, 3.5))
    inner = (poly([(24.5, 23.5), (20.5, 15.5), (26.5, 22)], BROWN_SOFT, 1.5) +
             poly([(39.5, 23.5), (43.5, 15.5), (37.5, 22)], BROWN_SOFT, 1.5))
    head = path("M32 22C38.5 22 42 26.5 42 32C42 34.5 41 36 40.5 38C43 39.5 43.5 42 43 44"
                "C42 47.5 38 49 32 49C26 49 22 47.5 21 44C20.5 42 21 39.5 23.5 38"
                "C23 36 22 34.5 22 32C22 26.5 25.5 22 32 22Z", INK)
    eyes = circle(27.5, 31, 2.2, HOLE) + circle(36.5, 31, 2.2, HOLE)
    nose = circle(28, 43.5, 1.6, HOLE) + circle(36, 43.5, 1.6, HOLE)
    return g(ears + inner + head + eyes + nose, "translate(0 -3)")


@reg("encryptpad", INDIGO_LIGHT)
def encryptpad():
    shackle = stroke("M23 27V21.5A9 9 0 0 1 41 21.5V27", INK, 4.5)
    body = rrect(16, 26, 32, 22, 4, INK)
    return shackle + body + line(21, 34, 43, 34, HOLE, 2.4) + line(21, 40, 43, 40, HOLE, 2.4)


@reg("endless-sky", INDIGO_DEEP)
def endless_sky():
    ship = (rrect(28.5, 12, 7, 36, 3.5, INK) + poly([(20, 44), (32, 34), (44, 44), (44, 47), (20, 47)], INK, 2.5)
            + rrect(21, 18, 5, 14, 2.5, INK) + rrect(38, 18, 5, 14, 2.5, INK))
    flames = (poly([(21.5, 18), (23.5, 11), (25.5, 18)], DEEP_ORANGE_LIGHT, 1.5) +
              poly([(38.5, 18), (40.5, 11), (42.5, 18)], DEEP_ORANGE_LIGHT, 1.5))
    return g(ship + flames, "rotate(45 32 30)")


@reg("endless-zone", CYAN_DARK)
def endless_zone():
    body = rrect(13, 27, 36, 6, 3, INK) + path("M47 27C50 27 52 28.5 52 30C52 31.5 50 33 47 33Z", INK)
    wings = (poly([(33, 28), (26, 13), (30.5, 13), (41, 28)], INK, 2) +
             poly([(33, 32), (26, 47), (30.5, 47), (41, 32)], INK, 2))
    tail = poly([(14, 28), (12, 21), (15.5, 21), (19.5, 28)], INK, 1.5)
    return g(body + wings + tail, "rotate(-12 32 30)")


@reg("engauge-digitizer", GREY_DEEP)
def engauge():
    axes = stroke("M17 15V44H47", INK, 3)
    curve = stroke("M21 37L28 33L34.5 30L42 22", INK, 2.6)
    pts = "".join(circle(x, y, 3.2, INK) for x, y in [(28, 33), (34.5, 30), (42, 22)])
    ends = circle(17, 15, 3.6, RED_SOFT) + circle(17, 44, 3.6, RED_SOFT) + circle(47, 44, 3.6, RED_SOFT)
    return axes + curve + pts + ends


@reg("enhanced_browsing", DEEP_PURPLE)
def enhanced_browsing():
    colon = circle(22.5, 23, 3.3, INK) + circle(22.5, 37, 3.3, INK)
    return colon + line(31, 44, 42, 16, BLUE_SOFT, 4.6)


@reg("enjoy-music-player", TEAL_LIGHT)
def enjoy():
    return poly([(25, 15.5), (46, 30), (25, 44.5)], INK, 5)


@reg("enpass", BLUE_DARK)
def enpass():
    shape = path("M20 14H27.5V17.5A4.5 4.5 0 0 0 36.5 17.5V14H44A4 4 0 0 1 48 18V32"
                 "C48 41 41 47 32 47C23 47 16 41 16 32V18A4 4 0 0 1 20 14Z", INK)
    hole = circle(CX, 29, 4.2, HOLE) + rrect(30.2, 29, 3.6, 10, 1.8, HOLE)
    return shape + hole


@reg("ensembles", DEEP_ORANGE_DEEP)
def ensembles():
    spk = (circle(22, 21, 7.5, INK) + circle(22, 21, 3.8, HOLE) + circle(22, 21, 1.8, INK) +
           circle(42, 21, 7.5, INK) + circle(42, 21, 3.8, HOLE) + circle(42, 21, 1.8, INK))
    keys = rrect(14, 32, 36, 15, 3, INK)
    blacks = "".join(rrect(x, 32, 3.5, 8.5, 1, HOLE) for x in (19.5, 26, 36, 42.5))
    gaps = "".join(line(x, 41, x, 47, HOLE, 1.6, "butt") for x in (21.2, 27.8, 32, 37.8, 44.3))
    return spk + keys + blacks + gaps


@reg("entangle", LIGHT_BLUE_DEEP)
def entangle():
    a = circle(26, 24, 11, INK) + circle(26, 24, 6, HOLE)
    b = circle(39, 37, 11.5, HOLE) + circle(39, 37, 10, INK) + circle(39, 37, 5, HOLE)
    tangle = stroke("M22 21C28 23 34 30 36 39", RED_LIGHT, 2.6) + stroke("M30 22C27 29 30 36 42 40", RED_LIGHT, 2.6)
    return a + b + tangle


@reg("ente", GREY_DARK)
def ente():
    return stroke("M22 30.5H41.5C41.5 24 37.5 19.5 31.8 19.5C25.8 19.5 21.5 24.3 21.5 30.5"
                  "C21.5 36.7 25.8 41.5 32 41.5C35.5 41.5 38.3 40 40.3 37.5", INK, 5.5)


@reg("enteauth", PURPLE)
def enteauth():
    shield = path("M32 11.5L47 17.5V29C47 38 40.5 44.5 32 48.5C23.5 44.5 17 38 17 29V17.5Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    lock = stroke("M28 30V27A4 4 0 0 1 36 27V30", HOLE, 2.6) + rrect(25.5, 29.5, 13, 10, 2.5, HOLE)
    return shield + lock


@reg("enter-the-gungeon", ORANGE_DEEP)
def gungeon():
    eyes = circle(20, 31, 6.8, INK) + circle(44, 31, 6.8, INK)
    return eyes + rrect(27.5, 30, 9, 4, 2, INK)


@reg("enve", TEAL)
def enve():
    e = stroke("M46 40C41 45.5 34.5 47 28 45.5C20.5 43.5 16.5 37 17 30C17.5 21 24.5 14.5 33 14.5", INK, 6.5)
    return e + circle(35, 26.5, 8.5, INK)


@reg("envy24control", RED_DEEP)
def envy24control():
    v = stroke("M16 20L22 40L31 20", INK, 4.5)
    i = line(37.5, 20, 34, 40, INK, 4.5)
    a = stroke("M40 40L46.5 20L49 40M42.5 33H48", INK, 4)
    return g(v + i + a, "translate(-1.5 0)")


@reg("eog", INDIGO)
def eog():
    photo = rrect(20, 13, 30, 26, 3.5, INK)
    split = path("M50 16.5V35.5A3.5 3.5 0 0 1 46.5 39H26Z", INDIGO_SOFT)
    lens = circle(23, 38, 10.5, HOLE) + circle(23, 38, 8.5, INK) + circle(23, 38, 5.2, PURPLE_SOFT)
    return photo + split + lens


@reg("epic-games", BLUE_GREY_DARK)
def epic_games():
    shield = path("M19 12H45A3 3 0 0 1 48 15V40L32 48L16 40V15A3 3 0 0 1 19 12Z", INK)
    e = stroke("M36.5 19.5H27.5V34.5H36.5M27.5 27H34.5", HOLE, 4)
    chev = stroke("M23 40.5L32 44.5L41 40.5", HOLE, 2.2)
    return shield + e + chev


@reg("epiphany-game", PURPLE_SOFT)
def epiphany_game():
    hat = poly([(15, 13), (49, 13), (43, 22), (21, 22)], AMBER_SOFT, 2.5)
    head = path("M14.5 24C14.5 18.5 22 16 32 16C42 16 49.5 18.5 49.5 24C49.5 29.5 42 33 32 33C22 33 14.5 29.5 14.5 24Z", INK)
    face = rrect(23, 22, 4, 4, .8, HOLE) + rrect(37, 22, 4, 4, .8, HOLE) + rrect(24, 27.5, 16, 2.6, 1.3, HOLE)
    body = rrect(25, 34.5, 14, 13, 2, INK) + line(32, 36.5, 32, 45.5, HOLE, 2.2)
    return hat + head + face + body


@reg("epsonscan2", INDIGO)
def epsonscan2():
    lid = poly([(20, 14), (46, 14), (41, 27), (15, 27)], INK, 2.5)
    glass = poly([(23, 17.5), (42, 17.5), (39, 24), (20, 24)], HOLE, 1)
    base = path("M14 31H50L47 45H17Z", INK, f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    beam = line(21, 21, 36, 21, LIGHT_BLUE_SOFT, 2.4)
    slot = rrect(20, 35, 24, 3, 1.5, HOLE)
    return lid + glass + beam + base + slot


@reg("epsxe", GREY_DEEP)
def epsxe():
    body = rrect(12, 16, 40, 28, 7, INK)
    lid = circle(CX, 30, 10.5, HOLE) + circle(CX, 30, 8.5, INK)
    p = stroke("M30 36V23H33.5C35.7 23 37 24.4 37 26.3C37 28.2 35.7 29.5 33.5 29.5H30", RED_LIGHT, 2.4)
    btns = circle(17.5, 37.5, 2.2, HOLE) + circle(46.5, 37.5, 2.2, HOLE)
    return body + lid + p + btns


@reg("eqonomize", ORANGE_DARK)
def eqonomize():
    bars = rrect(15, 31, 12, 16, 2, RED_SOFT) + rrect(33, 20, 14, 27, 2, INK)
    euro = stroke("M44 29.5C43 28.5 42 28 40.5 28C38 28 36.5 30.5 36.5 33.5C36.5 36.5 38 39 40.5 39"
                  "C42 39 43 38.5 44 37.5M34.5 32H40.5M34.5 35H40.5", HOLE, 1.8)
    arrow = stroke("M21 27C21 20 24 16 29.5 16", INK, 3) + poly([(28.5, 12), (34, 16), (28.5, 20)], INK, 1.5)
    return bars + euro + arrow


def _snake(colour):
    return path("M27 11.5H35A4 4 0 0 1 39 15.5V25A4 4 0 0 1 35 29H26A4 4 0 0 0 22 33V36H18.5"
                "A4 4 0 0 1 14.5 32V24.5A4 4 0 0 1 18.5 20.5H31V19H23V15.5A4 4 0 0 1 27 11.5Z", colour)


@reg("eric", BLUE_DEEP)
def eric():
    py = (_snake(INK) + circle(27, 15.3, 1.6, HOLE) +
          g(_snake(AMBER_SOFT) + circle(27, 15.3, 1.6, HOLE), "rotate(180 26.75 28)"))
    badge = circle(41, 40, 10, HOLE) + gear_g(41, 40, 6.2, RED_LIGHT, HOLE)
    return g(py, "translate(-1 -1)") + badge


@reg("ericWeb", BLUE_DEEP)
def ericweb():
    globe = circle(CX, CY, 17, INK)
    land = (path("M21 20C24 17 28 16.5 30 18.5C31.5 20.5 29 22 29.5 24.5C30 27 33 27 33 30"
                 "C33 33 29.5 35 27.5 38C26 40.5 24 40 23 37C22 34 19.5 32.5 18.5 29.5C18 26 18.5 22.5 21 20Z", ORANGE) +
            path("M37 16.5C41.5 18 45 21.5 46 25.5C44 26.5 41.5 25.5 39.5 26.5C37.5 27.5 38.5 31 36.5 31.5"
                 "C35 32 34.5 29.5 35.5 27C36 25 34 23.5 35 21C35.5 19.5 37 18.5 37 16.5Z", ORANGE) +
            path("M40 35C42 34 44.5 34.5 45 36C43.5 40 40.5 43 37 44.5C36.5 42 38 39 40 35Z", ORANGE))
    return globe + land


@reg("estmob-sendanywhere", RED)
def sendanywhere():
    top = stroke("M16.5 32V21A6 6 0 0 1 22.5 15H42", INK, 4)
    bot = stroke("M47.5 28V39A6 6 0 0 1 41.5 45H22", INK, 4)
    heads = poly([(40, 10.5), (46.5, 15), (40, 19.5)], INK, 2) + poly([(24, 40.5), (17.5, 45), (24, 49.5)], INK, 2)
    eyes = rrect(24, 25.5, 5, 8, 2.5, INK) + rrect(35, 25.5, 5, 8, 2.5, INK)
    return top + bot + heads + eyes


@reg("etcher", BLUE_DEEP)
def etcher():
    top = poly([(32, 12.5), (47, 20.5), (32, 28.5), (17, 20.5)], INK, 2.5)
    left = poly([(17, 20.5), (32, 28.5), (32, 47), (17, 39)], BLUE_SOFT, 2.5)
    right = poly([(47, 20.5), (32, 28.5), (32, 47), (47, 39)], BLUE_SOFT, 2.5)
    return top + left + right


@reg("eternallands", BROWN_DEEP)
def eternallands():
    e = stroke("M31 15C27 14 21 14.5 18 16M21.5 15.5C20.5 22 20.5 30 21 36C23.5 37.5 27 37.5 30.5 36"
               "M21 25.5C23.5 25 26 25 28 25.5", INK, 3.6)
    l = stroke("M37 20C36 28 35.5 36 36.5 41C38 45.5 42 46 44.5 43.5C45.5 42 44.5 40 42.5 40.5", INK, 3.6)
    return g(e + l, "translate(0 1)")


@reg("etherape", BLUE_DARK)
def etherape():
    return ring_b(CX, CY, 14, INK, 4) + stroke("M12 30H24L28 21L33 39L37.5 25L40 30H52", LIGHT_BLUE_SOFT, 3.2)


@reg("ethereumwallet", BLUE_GREY)
def ethereumwallet():
    top = poly([(32, 11), (44, 30), (32, 36.5), (20, 30)], INK, 1.5)
    shade = poly([(32, 11), (44, 30), (32, 36.5)], GREY_SOFT, 1.5)
    bot = poly([(20, 33.5), (32, 40), (44, 33.5), (32, 49)], INK, 1.5)
    return top + shade + bot


@reg("etherwall", BLUE_GREY_DARK)
def etherwall():
    v = poly([(14, 14), (50, 14), (36, 47), (28, 47)], AMBER, 3)
    stripes = "".join(line(x, 15, x - 8, 34, HOLE, 2.4, "butt") for x in (38, 43.5))
    return v + stripes


@reg("etl", RED_DARK)
def etl():
    return path("M21 12H44L41 18.5H30L28.5 26H38L35 32.5H27.5L26 40H40L37 46.5H17L22 30.5L19 26H23.5Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')


@small("electron")
def electron_s():
    return "".join(ellipse_b(CX, CY, 16, 6, INK, 2.8, a) for a in (30, 150)) + circle(CX, CY, 3.6, INK)


@small("electron-cash")
def electron_cash_s():
    return circle(CX, CY, 17.5, INK) + g(_btc(HOLE, 3.2), "translate(32 30) scale(1.12) translate(-32 -30)")


@small("electorrent")
def electorrent_s():
    mag = g(stroke("M22 16V29A10 10 0 0 0 42 29V16", INK, 8)
            + line(18, 21, 26, 21, HOLE, 2.6, "butt") + line(38, 21, 46, 21, HOLE, 2.6, "butt"),
            "rotate(45 32 30) translate(0 3)")
    return g(mag + stroke("M39 13A12 12 0 0 1 49.5 23.5", INK, 3), "translate(-2 1)")


@small("ekiga")
def ekiga_s():
    hand = stroke("M27 14C21 17 18.5 23.5 18.5 30C18.5 36.5 21 43 27 46", INK, 6.5)
    caps = rrect(23, 11, 9, 7, 3.5, INK) + rrect(23, 42, 9, 7, 3.5, INK)
    return hand + caps + stroke("M27 30H30L34 22L38 38L41 30H44", INK, 3)


@small("electrip")
def electrip_s():
    pad = ELECTRIP_PAD
    return (pad + line(22, 21.5, 22, 30.5, HOLE, 3.5) + line(17.5, 26, 26.5, 26, HOLE, 3.5)
            + circle(38.5, 28, 2.6, HOLE) + circle(44.5, 23.5, 2.6, HOLE))


@small("emerald-theme-manager-icon")
def emerald_s():
    gem = poly([(22, 14), (42, 14), (50, 24), (32, 47), (14, 24)], INK, 2.5)
    return gem + stroke("M16 24H48", HOLE, 3) + stroke("M26 24L32 42L38 24", HOLE, 3)


@small("emily-is-away-too")
def emily_too_s():
    return (g(_emily(), "translate(-3 -2)") + circle(43.5, 41.5, 10, BLUE_GREY_DARK)
            + stroke("M39.5 38C40 36 41.5 35 43.5 35C45.8 35 47.2 36.5 47.2 38.5C47.2 41.5 42 43.5 39.5 47H47.5", INK, 2.6))


@small("empathy")
def empathy_s():
    bubble = path("M18 13H46A4 4 0 0 1 50 17V39A4 4 0 0 1 46 43H42.5V49.5L36 43H18A4 4 0 0 1 14 39V17A4 4 0 0 1 18 13Z", INK)
    return (bubble + circle(26, 23.5, 2.8, HOLE) + circle(38, 23.5, 2.8, HOLE)
            + stroke("M23 30.5C27.5 36 36.5 36 41 30.5", HOLE, 3))


@small("electrum")


@small("electrum-ltc")
def electrum_ltc_s():
    return ring_b(CX, CY, 16, INK, 2.4) + g(_ltc(INK, 4), "translate(32 30) scale(.95) translate(-32 -28)")


@small("engauge-digitizer")
def engauge_s():
    axes = stroke("M17 15V44H47", INK, 3.2)
    ends = circle(17, 15, 4, RED_SOFT) + circle(47, 44, 4, RED_SOFT)
    return axes + stroke("M23 37L42 22", INK, 3) + circle(30, 31.5, 3.8, INK) + circle(42, 22, 3.8, INK) + ends


@small("ensembles")
def ensembles_s():
    spk = (circle(22, 21, 8, INK) + circle(22, 21, 3.5, HOLE) +
           circle(42, 21, 8, INK) + circle(42, 21, 3.5, HOLE))
    keys = rrect(14, 32, 36, 15, 3, INK)
    return spk + keys + "".join(rrect(x, 32, 4, 9, 1, HOLE) for x in (21, 30, 39))


@small("entangle")
def entangle_s():
    a = circle(26, 24, 11, INK) + circle(26, 24, 5.5, HOLE)
    b = circle(39, 37, 12, HOLE) + circle(39, 37, 10, INK) + circle(39, 37, 4.5, HOLE)
    return a + b


@small("epic-games")
def epic_games_s():
    shield = path("M19 12H45A3 3 0 0 1 48 15V40L32 48L16 40V15A3 3 0 0 1 19 12Z", INK)
    return shield + stroke("M38 19H26.5V37H38M26.5 28H36", HOLE, 4)


@small("eqonomize")
def eqonomize_s():
    bars = rrect(15, 31, 12, 16, 2, RED_SOFT) + rrect(33, 20, 14, 27, 2, INK)
    arrow = stroke("M21 27C21 20 24 16 29.5 16", INK, 3) + poly([(28.5, 12), (34, 16), (28.5, 20)], INK, 1.5)
    return bars + arrow


@small("eric")
def eric_s():
    py = _snake(INK) + g(_snake(AMBER_SOFT), "rotate(180 26.75 28)")
    return g(py, "translate(-1 -1)") + circle(41, 40, 10.5, HOLE) + circle(41, 40, 8, RED_LIGHT) + circle(41, 40, 3, HOLE)


@small("etherape")
def etherape_s():
    return ring_b(CX, CY, 14, INK, 4) + stroke("M12 30H23L28 20L35 40L40 30H52", LIGHT_BLUE_SOFT, 3)


@small("ethereumwallet")
def ethereumwallet_s():
    top = poly([(32, 11), (44, 30), (32, 36.5), (20, 30)], INK, 1.5)
    bot = poly([(20, 34), (32, 40.5), (44, 34), (32, 49)], INK, 1.5)
    return top + bot
