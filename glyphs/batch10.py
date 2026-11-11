# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 10: betaflight-configurator to boostnote."""
import math
from lm import (
    AMBER, AMBER_DEEP, AMBER_SOFT, BLACK, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_LIGHT, BLUE_SOFT, BROWN_DEEP, circle, CX, CY, CYAN_DEEP, CYAN_LIGHT, CYAN_SOFT,
    DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, f, g, GREY_DARK, GREY_LIGHT, HOLE, INDIGO,
    INDIGO_DARK, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP, line, ORANGE,
    ORANGE_DARK, ORANGE_DEEP, ORANGE_LIGHT, path, PINK, poly, pt, PURPLE, PURPLE_LIGHT,
    PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_SOFT, rrect, stroke, TEAL_DEEP, TEAL_LIGHT, WHITE,
)
from glyphs.kit import registry, ring_b

ICONS, SMALL, reg, small = registry()


@reg("betaflight-configurator", AMBER_DEEP)
def betaflight():
    wings = (path("M31 27C25 22 18 17 13.5 14.5C16 19.5 21.5 25.5 28.5 29.5Z", INK) +
             path("M29 31C23.5 29.5 18 29 14 30C18.5 33 24 34.5 29.5 34Z", INK))
    thorax = circle(34, 30, 5, INK)
    head = path("M37.5 24.5C39 19.5 43.5 16.5 48.5 17C47.5 21.5 44.5 25.5 39.5 27.5Z", INK)
    body = g(rrect(26, 34, 21, 12, 6, INK), "rotate(20 36.5 40)")
    stripes = (line(33, 34.5, 29.5, 43, HOLE, 2.4) + line(38.5, 36.5, 35.5, 45, HOLE, 2.4))
    return wings + thorax + head + body + g(stripes, "")


@reg("betterbird", DEEP_ORANGE)
def betterbird():
    disc = circle(CX, 31, 16, INK)
    crest = (path("M16.5 29C14 22 14.5 15.5 18 11C18.5 16 21 19.5 25 20.5L22 24Z", INK) +
             path("M23 19.5C23.5 14.5 27 11 32 10C30.5 12.5 30.5 14 31.5 15.5Z", INK))
    swirl = stroke("M37 36.5C33 39.5 26.5 37.5 26 32C25.5 27 30 23.5 34.5 25"
                   "C38 26.5 38.5 31 35.5 32.5", HOLE, 3.6)
    return disc + crest + swirl


@reg("beyond-a-steel-sky", BLUE_DARK)
def steel_sky():
    man = (circle(26, 16, 3.6, INK) +
           path("M21 22.5C21 21 22.5 20 24 20H28C29.5 20 31 21 31 22.5V35H29.5V48H22.5V35H21Z",
                INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"'))
    bot = (circle(40, 31, 3.6, INK) + line(40, 27.5, 41.5, 24, INK, 2.2) +
           rrect(35, 35, 10, 8, 2.5, INK) + rrect(36, 43, 3, 5, 1.2, INK) + rrect(41, 43, 3, 5, 1.2, INK))
    arm = line(31, 27, 36.5, 33, INK, 2.8)
    return g(man + arm + bot, "translate(0 -1)")


@reg("beyondallreason", GREY_DARK)
def bar():
    w = 3.4
    b = stroke("M14.5 22V38H19.5C22 38 23.5 36.5 23.5 34C23.5 31.5 22 30 19.5 30H14.5"
               "M14.5 22H19C21.3 22 22.5 23.3 22.5 26C22.5 28.5 21.3 30 19 30", INK, w)
    a = stroke("M26 38L31 22H33L38 38M27.8 33H36.2", INK, w)
    r = stroke("M41 38V22H45.5C48 22 49.5 23.8 49.5 26.2C49.5 28.6 48 30.3 45.5 30.3H41"
               "M45 30.3L49.5 38", INK, w)
    return b + a + r


@reg("bforartists", BLUE)
def bforartists():
    lobe = stroke(f"M{f(pt(32, 30, 11.5, 150)[0])} {f(pt(32, 30, 11.5, 150)[1])}"
                  f"A11.5 11.5 0 0 1 {f(pt(32, 30, 11.5, 212)[0])} {f(pt(32, 30, 11.5, 212)[1])}", INK, 10.5)
    return "".join(g(lobe, f"rotate({120 * k + 20} 32 30)") for k in range(3)) 


@reg("bibletime", INDIGO)
def bibletime():
    book = rrect(17, 12, 24, 34, 3.5, INK) + rrect(17, 12, 4, 34, 2, INDIGO_DARK)
    cross = line(30.5, 17, 30.5, 35, HOLE, 4.2) + line(24.5, 23, 36.5, 23, HOLE, 4.2)
    clock = (circle(41.5, 40, 9, DEEP_ORANGE_LIGHT) + circle(41.5, 40, 6.2, INK) +
             stroke("M41.5 36.5V40.5H45", DEEP_ORANGE_LIGHT, 2.2))
    return book + cross + clock


@reg("big-finish-downloader", INDIGO_DARK)
def tardis():
    lamp = rrect(30, 10.5, 4, 4, 1.2, INK)
    roof = rrect(21, 14, 22, 5, 2, INK)
    box = rrect(20, 18, 24, 31, 2, INK)
    sign = rrect(22.5, 20.5, 19, 3, 1, HOLE)
    panes = "".join(rrect(x, y, 7.5, 5.5, 1, HOLE) for x in (23, 33.5) for y in (26, 34, 42)
                    if y < 42) + rrect(23, 42, 7.5, 4.5, 1, HOLE) + rrect(33.5, 42, 7.5, 4.5, 1, HOLE)
    return g(lamp + roof + box + sign + panes, "translate(0 -.5)")


@reg("biglybt", BLUE_DEEP)
def biglybt():
    arrow = poly([(22, 13), (42, 13), (42, 28), (49, 28), (32, 47), (15, 28), (22, 28)], INK, 3)
    slot = rrect(20.5, 18, 23, 7, 3.5, HOLE)
    return arrow + slot + rrect(29, 20, 7, 3, 1.5, INK) + circle(39, 21.5, 1.5, INK)


@reg("billard-gl", ORANGE_DEEP)
def billard():
    ball = circle(CX, CY, 16.5, INK)
    r, o = 16.5, 8.5
    h = math.sqrt(r * r - o * o)
    d, n = (math.sqrt(.5), math.sqrt(.5)), (-math.sqrt(.5), math.sqrt(.5))
    P = lambda so, sh: (CX + so * o * n[0] + sh * h * d[0], CY + so * o * n[1] + sh * h * d[1])
    a1, b1, b2, a2 = P(1, -1), P(1, 1), P(-1, 1), P(-1, -1)
    band = path(f"M{f(a1[0])} {f(a1[1])}L{f(b1[0])} {f(b1[1])}A{r} {r} 0 0 0 {f(b2[0])} {f(b2[1])}"
                f"L{f(a2[0])} {f(a2[1])}A{r} {r} 0 0 0 {f(a1[0])} {f(a1[1])}Z", ORANGE)
    spot = circle(CX, CY, 7, INK)
    num = line(28.8, 27.2, 28.8, 33.3, BLACK, 2.2) + stroke(
        "M32.3 27.3H36L33.8 29.6C35.8 29.6 36.8 30.5 36.8 31.6C36.8 33 35.3 33.6 34 33.6"
        "C33.2 33.6 32.4 33.3 32 32.8", BLACK, 1.9)
    return ball + band + spot + num


@reg("binance", AMBER_DEEP)
def binance():
    def dia(cx, cy, s):
        return g(rrect(cx - s / 2, cy - s / 2, s, s, 1.2, INK), f"rotate(45 {cx} {cy})")
    chev = (stroke("M22.5 23.5L32 14L41.5 23.5", INK, 4.6) +
            stroke("M22.5 36.5L32 46L41.5 36.5", INK, 4.6))
    return dia(CX, CY, 7) + dia(18.5, CY, 5.8) + dia(45.5, CY, 5.8) + chev


@reg("binaryninja", RED)
def binaryninja():
    head = circle(CX, CY, 16, INK)
    band = rrect(14, 23, 36, 12, 5, HOLE)
    eyes = (poly([(19.5, 26), (29.5, 27), (28, 31.5), (21, 31)], INK, 1.8) +
            poly([(44.5, 26), (34.5, 27), (36, 31.5), (43, 31)], INK, 1.8))
    return head + band + eyes


@reg("bingwall", LIGHT_BLUE_DEEP)
def bingwall():
    peaks = stroke("M15 43L24.5 25L32 38.5L39.5 23L49 43Z", INK, 4)
    return peaks + circle(21, 16.5, 3.4, INK)


@reg("bioshock-infinite", RED_DARK)
def bioshock():
    badge = path("M16 18C21 18 25.5 16 32 12.5C38.5 16 43 18 48 18C48.5 29 43 41 32 47.5"
                 "C21 41 15.5 29 16 18Z", INK)
    pts = [pt(32, 30.5, 8.5 if k % 2 == 0 else 3.8, -90 + 36 * k) for k in range(10)]
    return badge + poly(pts, HOLE, 2)


@reg("birdfont", BLUE)
def birdfont():
    b = path("M18 14H33C39.5 14 43 17.5 43 22.5C43 25.5 41.5 27.5 39.5 28.5C43.5 29.5 46 32.5 46 37"
             "C46 43 41.5 46 35 46H18Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    fl = stroke("M25.5 40V20.5H34.5M25.5 29.5H32.5", HOLE, 4.2)
    return b + fl


@reg("birdie", BLUE_DEEP)
def birdie():
    body = path("M17 32C17 20 23.5 12.5 32 12.5C40.5 12.5 47 20 47 32C47 41 41 46.5 32 46.5"
                "C23 46.5 17 41 17 32Z", INK)
    tuft = path("M29 13.5C29.5 10.5 31 9.5 33 10C32 11 31.8 12 32 13.2Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    eyes = circle(25, 29, 3, HOLE) + circle(39, 29, 3, HOLE)
    beak = poly([(27.5, 34.5), (36.5, 34.5), (32, 39)], ORANGE_LIGHT, 2)
    return body + tuft + eyes + beak


@reg("bisq", PURPLE_LIGHT)
def bisq():
    tail = stroke("M20 38C14 36 12.5 27 16 21.5C18.5 17.5 23 17 25 19", INK, 3.6)
    head = path("M23 26L22 13.5L30 19.5H36L44 13.5L43 26C45 29 45.5 32 45 35"
                "C44 42.5 38.5 47 33 47C27.5 47 22 42.5 21 35C20.5 32 21 29 23 26Z", INK)
    eyes = (poly([(26, 31), (31, 32.5), (27.5, 35)], HOLE, 1.5) +
            poly([(40, 31), (35, 32.5), (38.5, 35)], HOLE, 1.5))
    nose = poly([(31, 38.5), (35, 38.5), (33, 40.5)], HOLE, 1.2)
    return g(tail + head + eyes + nose, "translate(-1 -1)")


@reg("bitcoin", ORANGE_DEEP)
def bitcoin():
    b = stroke("M26 21H34.5C37.5 21 39.5 22.8 39.5 25.5C39.5 28.2 37.5 30 34.5 30H26"
               "M26 30H35.5C38.8 30 41 31.9 41 34.8C41 37.6 38.8 39.5 35.5 39.5H26M26 18V42", INK, 4)
    ticks = (line(30, 15, 30, 19, INK, 3) + line(35, 15, 35, 19, INK, 3) +
             line(30, 41.5, 30, 45.5, INK, 3) + line(35, 41.5, 35, 45.5, INK, 3))
    return g(b + ticks, "rotate(14 32 30) translate(-1 0)")


@reg("bitmap2component", ORANGE_DARK)
def bitmap2component():
    bowl = ring_b(31, 36, 6.5, INK, 4.4)
    a = stroke("M23.5 21.5C25.5 19.5 28 18.5 31 18.5C35.5 18.5 37.5 21 37.5 26V43", INK, 4.4)
    return rrect(15, 11, 34, 4, 2, ORANGE_LIGHT) + bowl + a


@reg("bitshares2-light", LIGHT_BLUE)
def bitshares():
    stem = path("M20 13L30 23V47H20Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    wheel = circle(35, 36, 11.5, INK) + circle(35, 36, 4.2, HOLE)
    spokes = "".join(line(*pt(35, 36, 6, a), *pt(35, 36, 11.8, a), HOLE, 1.6)
                     for a in range(-60, 181, 60))
    return g(stem + wheel + spokes, "translate(-.5 -2)")


@reg("bitwig-studio", DEEP_ORANGE)
def bitwig():
    s, r = 5.6, 2.35
    rows = [(20.5, [2, 3, 4, 5]), (27.5, [1, 2, 3, 4, 5, 6]), (34.5, [1, 2, 5, 6])]
    return "".join(circle(32 + (c - 3.5) * s, y + 3, r, INK) for y, cs in rows for c in cs)


@reg("bizhawk", BLUE_LIGHT)
def bizhawk():
    suit = path("M13 27L32 32L51 27L45 36L37 48H27L19 36Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    lapels = poly([(27, 32), (32, 32.5), (37, 32), (32, 47)], BLUE_DEEP, 1.5)
    tie = poly([(30.8, 33.5), (33.2, 33.5), (34, 42), (32, 44.5), (30, 42)], BLACK, 1)
    head = path("M26 31C25 24 27 15.5 34 15C39 14.7 41 19 40.5 24C40 28 38.5 30.5 38 32Z", INK)
    beak = poly([(27, 19.5), (21, 22.5), (27.5, 24.5)], AMBER, 2)
    eye = circle(34.5, 20, 1.6, BLACK)
    return suit + lapels + tie + head + beak + eye


@reg("black-desert", BLUE_GREY_DARK)
def black_desert():
    outer = stroke("M32 14L44.5 26.5L32 39L19.5 26.5L27 19L36.5 28.5L32 33", INK, 3.8)
    dots = circle(20.5, 40, 3.2, RED) + circle(43.5, 40, 3.2, RED)
    return outer + dots


@reg("black-mesa", DEEP_ORANGE_DEEP)
def black_mesa():
    ring_ = ring_b(CX, CY, 15.5, INK, 3.4)
    r = 13.2
    dx = math.sqrt(r * r - 25)
    fill = path(f"M{f(32 - r)} 30H33.5V35H{f(32 + dx)}A{r} {r} 0 0 1 {f(32 - r)} 30Z", INK)
    return ring_ + fill


def _fusion(colour):
    blob = (line(24, 23.5, 39.5, 17.5, colour, 8.5) + line(26, 24, 31.5, 32, colour, 5) +
            line(29.5, 33.5, 40.5, 29.5, colour, 7.5) + circle(32.5, 43.5, 3.4, colour))
    return blob


@reg("blackmagic-Fusion8", INDIGO)
def fusion8():
    return _fusion(INK)


@reg("blackmagic-Fusion9", AMBER)
def fusion9():
    return ring_b(CX, CY, 16, INK, 3.2) + g(_fusion(INK), "translate(32 30) scale(.78) translate(-32 -30)")


@reg("blackmagicraw-player", ORANGE_DEEP)
def braw_player():
    strip = rrect(15, 12, 9, 36, 2, INK) + "".join(rrect(17.5, y, 4, 3.4, 1, HOLE)
                                                     for y in (15.5, 22, 28.5, 35, 41.5))
    play = poly([(29, 17), (49, 30), (29, 43)], INK, 4)
    return strip + play


@reg("blackmagicraw-speedtest", BLUE_GREY_DARK)
def braw_speed():
    dial = stroke("M20.5 42A16 16 0 1 1 43.5 42", INK, 4)
    red = stroke("M47.5 32A16 16 0 0 1 43.5 42", RED, 4)
    needle = line(32, 30, 41.5, 38, INK, 3.6) + circle(CX, CY, 3.6, INK)
    tick = line(32, 17.5, 32, 21, INK, 2.6)
    return dial + red + needle + tick


@reg("blastem", RED_DARK)
def blastem():
    def px(cells, colour):
        return "".join(f'<rect x="{x}" y="{y}" width="4.2" height="4.2" fill="{colour}"/>'
                       for x, y in cells)
    u = 4
    outer = [(x, y) for y in range(-3, 4) for x in range(-3, 4) if abs(x) + abs(y) <= 4]
    inner = [(0, y) for y in range(-2, 3)] + [(x, 0) for x in (-2, -1, 1, 2)]
    tail = [(-4, 0), (-5, 0), (-6, 0), (-4, -1), (-4, 1), (-5, -1), (-5, 1)]
    cx, cy = 35.8, 28
    cell = lambda c: [(f(cx + x * u), f(cy + y * u)) for x, y in c]
    return px(cell(tail), DEEP_ORANGE_LIGHT) + px(cell(outer), ORANGE_LIGHT) + px(cell(inner), INK)


@reg("bless", BROWN_DEEP)
def bless():
    out = ""
    for r, row in enumerate(["0101", "1010", "0110"]):
        for c, ch in enumerate(row):
            x, y = 16.5 + c * 7.5, 14 + r * 9
            if ch == "1":
                out += rrect(x + 1.6, y, 2.6, 7, 1.3, INK)
            else:
                out += rrect(x, y, 5.8, 7, 1.6, "none", f' stroke="{INK}" stroke-width="2.3"')
    pencil = g(rrect(34, 32, 17, 6, 1.5, AMBER) + rrect(48, 32, 4, 6, 1.5, RED_SOFT) +
               poly([(34, 32), (34, 38), (29, 35)], AMBER_SOFT, 1), "rotate(-40 40 35)")
    return out + g(pencil, "translate(-4 6)")


@reg("blinken", BLUE_GREY_DARK)
def blinken():
    cols = [RED, INDIGO_SOFT, BLUE, AMBER]
    out = ""
    for k, c in enumerate(cols):
        a0, a1 = -90 + 90 * k + 5, -90 + 90 * (k + 1) - 5
        p0, p1 = pt(CX, CY, 12.5, a0), pt(CX, CY, 12.5, a1)
        out += stroke(f"M{f(p0[0])} {f(p0[1])}A12.5 12.5 0 0 1 {f(p1[0])} {f(p1[1])}", c, 7.5)
    return out + circle(CX, CY, 5, INK)


def _blob(badge):
    band = rrect(12.5, 13, 39, 9.5, 3, RED) + path("M14 18L10 30L16 26L17 21Z", RED)
    brows = (poly([(19.5, 26.5), (28.5, 29.5), (28.5, 31)], INK, 2) +
             poly([(44.5, 26.5), (35.5, 29.5), (35.5, 31)], INK, 2))
    eyes = circle(24.5, 33, 3.4, INK) + circle(39.5, 33, 3.4, INK)
    out = band + brows + eyes + rrect(27, 41, 10, 2.6, 1.3, INK)
    if badge:
        out += circle(43, 41.5, 8, RED_DEEP) + stroke("M40.2 38.8C40.7 37.3 41.8 36.6 43 36.6"
                                                         "C44.6 36.6 45.6 37.6 45.6 39C45.6 40.8 43.5 42.5 40.2 46H46",
                                                         WHITE, 2.4)
    return out


@reg("blobAndConquer", AMBER)
def blob_conquer():
    return _blob(True)


@reg("blobwars", AMBER)
def blobwars():
    return _blob(False)


@reg("blobby", BLUE_GREY)
def blobby():
    ball = circle(CX, CY, 16.5, INK)
    seams = (stroke("M22 16.5C27.5 22 29.5 30 27.5 45.5", HOLE, 2.6) +
             stroke("M15.5 29C24 27 34 29 43 36.5", HOLE, 2.6) +
             stroke("M31 13.5C39 17 44.5 24.5 47.5 32.5", HOLE, 2.6))
    return ball + seams


@reg("bloboats", INDIGO_LIGHT)
def bloboats():
    hull = path("M13 34H51L45.5 44.5C45 45.5 44 46 43 46H20C19 46 18 45.5 17.5 44.5Z", INK)
    cabin = path("M18 20C22 19 34 16.5 40 16L41 32H19Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    m = stroke("M24 28.5L26.5 21.5L30 26L33.5 20.5L35.5 28", HOLE, 2.6)
    return hull + cabin + m


@reg("blockbench", BLUE_DEEP)
def blockbench():
    back = poly([(20, 16), (48, 20), (44, 30), (16, 26)], INK, 2.5)
    seat = poly([(15, 31.5), (43, 35), (40.5, 40), (13, 36.5)], INK, 2.5)
    legs = line(19, 38, 19.5, 46, INK, 3.2) + line(37.5, 41, 37, 47.5, INK, 3.2)
    return back + seat + legs


@reg("blockout", CYAN_DEEP)
def blockout():
    out = ""
    for r in range(3):
        for c in range(3):
            colour = CYAN_LIGHT if r == 0 else INK
            if c == 1:
                colour = BLUE_SOFT if r == 0 else CYAN_SOFT
            out += rrect(15 + c * 11.7, 13 + r * 11.7, 10.2, 10.2, 2.2, colour)
    return out


@reg("blogilo", LIGHT_BLUE)
def blogilo():
    base = rrect(15, 13, 34, 34, 8, INK)
    b = path("M22 25A6 6 0 0 1 28 19H33A6 6 0 0 1 39 25V26.5A2.5 2.5 0 0 0 41.5 29"
             "A2 2 0 0 1 42 31V35A6 6 0 0 1 36 41H28A6 6 0 0 1 22 35Z", HOLE)
    bars = rrect(27, 23.5, 7.5, 3.4, 1.7, INK) + rrect(27, 32, 10.5, 3.4, 1.7, INK)
    return base + b + bars


@reg("bloomrpc", CYAN_DEEP)
def bloomrpc():
    left = path("M32 47C22 46 15.5 38 16 22C22 25 29 31 32 40Z", CYAN_SOFT)
    right = path("M32 47C42 46 48.5 38 48 22C42 25 35 31 32 40Z", CYAN_SOFT)
    mid = path("M32 12C38.5 18 41 27 39.5 36C38.5 42 35.5 45.5 32 47C28.5 45.5 25.5 42 24.5 36"
               "C23 27 25.5 18 32 12Z", INK)
    return left + right + mid


@reg("bluefish", BLUE_DEEP)
def bluefish():
    body = path("M13 31C15.5 23 24 18.5 31.5 18.5C39 18.5 43 24 44.5 29"
                "C43 35 39 40 31.5 40C24 40 15.5 37 13 31Z", INK)
    tail = poly([(42, 29.5), (51, 21), (49, 29.5), (51, 38)], INK, 2.5)
    fin = poly([(26, 20), (30, 14), (35, 19)], INK, 2)
    return body + tail + fin + circle(21.5, 28, 2.2, HOLE)


@reg("bluej", BLUE_DEEP)
def bluej():
    body = path("M21 22C21 16 26 12.5 32 12.5C38 12.5 41 15.5 43 19L47 42C47.5 45 46 47 43 47"
                "H25C22.5 47 21 45 21 42Z", INK)
    crest = path("M30 13C35 12 41 13 45 17.5L41 18.5C39.5 26 36.5 32 32 36"
                 "C34 30 35 24 34.5 19.5C33.5 16.5 31.5 14.5 30 13Z", BLUE_DARK)
    beak = poly([(22, 22), (13, 26.5), (22.5, 28)], INK, 2)
    return body + crest + beak + circle(27.5, 22, 2.2, BLACK)


@reg("bluejeans", BLUE_DEEP)
def bluejeans():
    box = rrect(14, 15, 28, 30, 6, INK)
    cam = poly([(42, 30), (50, 23), (50, 37)], INK, 2.5)
    b = stroke("M22 21.5V38.5H29.5C32.5 38.5 34.5 36.8 34.5 34.2C34.5 31.7 32.5 30 29.5 30H22"
               "M22 21.5H28.8C31.5 21.5 33 23 33 25.7C33 28.3 31.5 30 28.8 30", HOLE, 4)
    return box + cam + b


@reg("bluemail", INDIGO)
def bluemail():
    env = rrect(13, 20, 38, 26, 4, INK)
    flap = stroke("M15.5 22.5L32 36L48.5 22.5", HOLE, 2.6)
    badge = rrect(25, 12, 14, 14, 4, INK) + rrect(25, 12, 14, 14, 4, "none",
                                                   f' stroke="{HOLE}" stroke-width="2"')
    b = stroke("M29.5 14.5V22.5M29.5 20A2.8 2.8 0 1 0 35.1 20A2.8 2.8 0 1 0 29.5 20", HOLE, 2.3)
    return env + flap + badge + b


@reg("blush-blush", PURPLE_LIGHT)
def blush():
    pad = path("M32 29C37.5 29 43.5 35 43.5 40C43.5 44.5 39.5 46 36.5 45"
               "C34.5 44.5 33.5 44 32 44C30.5 44 29.5 44.5 27.5 45C24.5 46 20.5 44.5 20.5 40"
               "C20.5 35 26.5 29 32 29Z", INK)
    toes = "".join(g(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="5.2" fill="{INK}"/>', f"rotate({a} {x} {y})")
                   for x, y, a in [(18, 26.5, -25), (26.5, 18.5, -8), (37.5, 18.5, 8), (46, 26.5, 25)])
    return pad + toes


@reg("boinc", INDIGO_DARK)
def boinc():
    arcs = ""
    for k in range(4):
        a0, a1 = 45 + 90 * k + 14, 45 + 90 * (k + 1) - 14
        p0, p1 = pt(CX, CY, 14, a0), pt(CX, CY, 14, a1)
        arcs += stroke(f"M{f(p0[0])} {f(p0[1])}A14 14 0 0 1 {f(p1[0])} {f(p1[1])}", INK, 4.4)
    cross = "".join(line(*pt(CX, CY, 8.5, a), *pt(CX, CY, 15, a), INK, 3.2) for a in (45, 135, 225, 315))
    return arcs + cross + circle(CX, CY, 5.5, AMBER)


@reg("bomber", CYAN_DEEP)
def bomber():
    ship = path("M17 26C24 22 36 21.5 43 22.5C47 23 50 25.5 50 28.5C50 32 45 36.5 36 39.5"
                "L17 46L27 36L17 33Z", INK)
    fin = poly([(22, 25), (20.5, 15.5), (29, 22.5)], INK, 2)
    nozzle = rrect(12, 25.5, 6, 8, 1.5, BLUE_GREY_DARK)
    canopy = path("M41 23C45.5 23 49.5 25 50 28.5C47 28.5 43 26.5 41 23Z", BLUE_GREY_DARK)
    return fin + ship + nozzle + canopy


@reg("bomi", PINK)
def bomi():
    return (ring_b(CX, CY, 15.5, INK, 3.6) + rrect(24, 21, 4, 18, 2, INK) +
            poly([(31.5, 21), (41.5, 30), (31.5, 39)], INK, 2.8))


@reg("bookworm", PURPLE)
def bookworm():
    book = rrect(17, 12, 30, 36, 3.5, INK) + rrect(17, 12, 5.5, 36, 2.5, PURPLE_SOFT)
    ribbon = path("M36 10.5H42V29L39 26L36 29Z", AMBER,
                  f' stroke="{AMBER}" stroke-width="1.2" stroke-linejoin="round"')
    return book + ribbon


@reg("boomaga", BLUE_GREY)
def boomaga():
    paper = rrect(21, 12, 20, 10, 2, INK)
    body = rrect(14, 20, 34, 18, 4, INK)
    tray = rrect(21, 32, 20, 13, 2, INK) + rrect(19, 31, 24, 2.4, 1.2, HOLE)
    lines_ = rrect(24, 36, 11, 2.4, 1.2, HOLE) + rrect(24, 40, 8, 2.4, 1.2, HOLE)
    led = circle(19, 25, 1.8, GREY_LIGHT)
    badge = circle(44.5, 41, 8.5, RED) + stroke("M40.5 41H48.5M40.5 41L43 38.5M40.5 41L43 43.5"
                                                        "M48.5 41L46 38.5M48.5 41L46 43.5", WHITE, 2.3)
    return paper + body + tray + lines_ + led + badge


@reg("boostnote", TEAL_LIGHT)
def boostnote():
    plane = poly([(15, 30), (48, 14), (38, 45), (31, 36)], INK, 2.5)
    fold = poly([(31, 36), (48, 14), (29, 43)], TEAL_DEEP, 1.5)
    return plane + fold


@small("bless")
def bless_s():
    out = ""
    for r, row in enumerate(["010", "101"]):
        for c, ch in enumerate(row):
            x, y = 15.5 + c * 11, 13 + r * 13
            if ch == "1":
                out += rrect(x + 2.5, y, 4, 10, 2, INK)
            else:
                out += rrect(x, y, 8.5, 10, 2.5, "none", f' stroke="{INK}" stroke-width="3"')
    pencil = g(rrect(32, 31, 19, 8, 2, AMBER) + poly([(32, 31), (32, 39), (26, 35)], AMBER_SOFT, 1.5),
               "rotate(-40 40 35)")
    return out + g(pencil, "translate(-3 7)")


@small("big-finish-downloader")
def tardis_s():
    box = rrect(30, 10, 4, 4, 1.2, INK) + rrect(20, 14, 24, 35, 2.5, INK)
    panes = "".join(rrect(x, y, 7.5, 8, 1.2, HOLE) for x in (23, 33.5) for y in (20, 31))
    return g(box + panes, "translate(0 -.5)")


@small("beyondallreason")
def bar_s():
    w = 2.8
    b = stroke("M14.5 22V38H19.5C22 38 23.5 36.5 23.5 34C23.5 31.5 22 30 19.5 30H14.5"
               "M14.5 22H19C21.3 22 22.5 23.3 22.5 26C22.5 28.5 21.3 30 19 30", INK, w)
    a = stroke("M26 38L31 22H33L38 38M27.8 33H36.2", INK, w)
    r = stroke("M41 38V22H45.5C48 22 49.5 23.8 49.5 26.2C49.5 28.6 48 30.3 45.5 30.3H41"
               "M45 30.3L49.5 38", INK, w)
    return b + a + r


@small("bitshares2-light")
def bitshares_s():
    stem = path("M20 13L30 23V47H20Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return g(stem + circle(35, 36, 11.5, INK) + circle(35, 36, 5, HOLE), "translate(-.5 -2)")


@small("blastem")
def blastem_s():
    u = 6
    outer = [(x, y) for y in range(-2, 3) for x in range(-2, 3) if abs(x) + abs(y) <= 2]
    inner = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    cx, cy = 35, 27
    rect = lambda cs, c: "".join(f'<rect x="{f(cx + x * u)}" y="{f(cy + y * u)}" width="6.2" height="6.2" fill="{c}"/>'
                                 for x, y in cs)
    return rect([(-3, 0), (-4, 0)], DEEP_ORANGE_LIGHT) + rect(outer, ORANGE_LIGHT) + rect(inner, INK)


@small("bitwig-studio")
def bitwig_s():
    s, r = 8, 3.3
    rows = [(19, [1, 2, 3]), (29, [0, 1, 2, 3, 4]), (39, [0, 1, 3, 4])]
    return "".join(circle(32 + (c - 2) * s, y + 1, r, INK) for y, cs in rows for c in cs)


@small("billard-gl")
def billard_s():
    full = billard()
    return full[:full.index('<path d="M28.8')] + circle(CX, CY, 3, BLACK)


def _blob_s(badge):
    band = rrect(12.5, 12, 39, 10, 3, RED)
    eyes = circle(24, 32, 4.6, INK) + circle(40, 32, 4.6, INK)
    brows = line(18.5, 25.5, 28, 28, INK, 3.4) + line(45.5, 25.5, 36, 28, INK, 3.4)
    out = band + eyes + brows
    if badge:
        out += circle(44, 42, 8, RED_DEEP)
    return out


@small("blobAndConquer")
def blob_conquer_s():
    return _blob_s(True)


@small("blobwars")
def blobwars_s():
    return _blob_s(False)


@small("bitcoin")
def bitcoin_s():
    b = stroke("M26 21H34C37 21 39 22.8 39 25.5C39 28.2 37 30 34 30H26"
               "M26 30H35C38.5 30 40.5 31.9 40.5 34.8C40.5 37.6 38.5 39.5 35 39.5H26M26 16V44", INK, 4.2)
    return g(b + line(33, 16, 33, 20, INK, 3.4) + line(33, 40, 33, 44, INK, 3.4), "rotate(14 32 30) translate(-1 0)")


@small("bibletime")
def bibletime_s():
    book = rrect(16, 12, 26, 35, 3.5, INK)
    cross = line(29, 17, 29, 35, HOLE, 5) + line(22, 23.5, 36, 23.5, HOLE, 5)
    return book + cross + circle(42.5, 40, 9, DEEP_ORANGE_LIGHT)


@small("boomaga")
def boomaga_s():
    body = rrect(21, 11, 22, 10, 2, INK) + rrect(13, 19, 38, 20, 4, INK) + rrect(20, 32, 24, 14, 2, INK)
    return body + rrect(18, 31, 28, 3, 1.5, HOLE) + circle(45, 42, 8, RED)


@small("bluemail")
def bluemail_s():
    env = rrect(12, 17, 40, 29, 4.5, INK)
    return env + stroke("M15 20.5L32 35L49 20.5", HOLE, 3.4)
