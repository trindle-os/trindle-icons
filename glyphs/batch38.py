# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 38: kali-jad to kexi.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
import math
from lm import *
from glyphs.kit import _gear, registry, _ring
from glyphs.kit import shared_kde_s

ICONS, SMALL, reg, small = registry()

def _ellipse(cx, cy, rx, ry, fill):
    return path(f"M{f(cx - rx)} {f(cy)}a{f(rx)} {f(ry)} 0 1 0 {f(2 * rx)} 0"
                f"a{f(rx)} {f(ry)} 0 1 0 {f(-2 * rx)} 0Z", fill)

def _sector(cx, cy, r, a0, a1, fill):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return path(f"M{f(cx)} {f(cy)}L{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {big} 1 {f(x1)} {f(y1)}Z", fill)

def _kde(k_w=3.4, teeth=9):
    gear = _gear(CX, CY, 17, 13.5, teeth, INK, .45) + circle(CX, CY, 10, HOLE)
    k = (line(28, 23, 28, 37.5, INK, k_w) + line(29, 30.5, 37, 22.5, INK, k_w) +
         line(31.5, 29, 37.5, 37.5, INK, k_w))
    return gear + k

@reg("kali-jad", RED_DEEP)
def kali_jad():
    return rrect(16, 13, 32, 34, 4, INK) + stroke(
        "M37 18.5V32.5C37 38.5 33.5 41.5 28.5 41.5C25.5 41.5 23.5 40.5 22 38.5", HOLE, 5)

def _kali_dragon(w=2.2):
    body = stroke("M41 21.5C33.5 20 27.5 24.5 27.5 30.5C27.5 36.5 33 39 39.5 39.5"
                  "C44.5 40 47.5 43 48.5 48", INK, 3)
    head = poly([(37.5, 19.5), (43.5, 20.5), (49.5, 25), (44, 25.8), (40, 24.5)], INK, 1.5)
    whiskers = (stroke("M38.5 19.5C31 14 22 11.5 13 11.5", INK, w)
                + stroke("M37 21C30.5 18 23 17.5 14.5 18.5", INK, w)
                + stroke("M34 22.5C29 22 23 23 18 25.5", INK, w))
    return body + head + whiskers

@reg("kali-menu", BLUE_GREY)
def kali_menu():
    plate = poly([(24, 15), (49, 15), (41, 46), (15, 46)], BLUE_GREY_DARK, 3)
    return plate + _kali_dragon()

@reg("kali-set", GREY)
def kali_set():
    head = path("M40 48V40.5C45 37.5 47.5 31.5 46.5 25C45.5 17 38.5 12 30.5 12"
                "C22.5 12 17 18 17 25.5L14 32.5H17.5V37C17.5 39 19 40.5 21 40.5H25.5V48Z", INK)
    wrench = (circle(34, 21, 5.8, HOLE) + rrect(32, 12, 4, 9, 1, INK)
              + line(34, 25, 34, 48, HOLE, 3.6, "butt"))
    return head + wrench

@reg("kali-undercover", GREY_DARK)
def kali_undercover():
    crown = path("M22.5 25L25.5 16C26.3 14 28 13.7 30 14.8C31.4 15.6 32.6 15.6 34 14.8"
                 "C36 13.7 37.7 14 38.5 16L41.5 25Z", INK)
    brim = line(14.5, 26, 49.5, 26, INK, 3.4)
    specs = (rrect(16.5, 31, 13.5, 10, 4, INK) + rrect(34, 31, 13.5, 10, 4, INK)
             + line(29, 34, 35, 34, INK, 2.4))
    return crown + brim + specs

@reg("kali-unix-privesc-check", BROWN)
def kali_monkey():
    fur = BROWN_SOFT
    head = circle(17, 27, 5.5, fur) + circle(47, 27, 5.5, fur) + circle(32, 30, 15.5, fur)
    mask = (circle(26.5, 25, 6, INK) + circle(37.5, 25, 6, INK) + _ellipse(32, 36.5, 12.5, 8, INK))
    face = (circle(26.5, 24.5, 2.6, BROWN_DARK) + circle(37.5, 24.5, 2.6, BROWN_DARK)
            + stroke("M25.5 37Q32 42 38.5 37", BROWN_DARK, 2.6))
    return head + mask + face

@reg("kalzium", RED_LIGHT)
def kalzium():
    out = ""
    for x, y in [(19, 18), (45, 18), (19, 42), (45, 42)]:
        out += line(32, 30, x, y, INK, 2.8) + circle(x, y, 4.6, INK)
    return out + circle(32, 30, 7.5, INK)

@reg("kame-editor", ORANGE_DARK)
def kame_editor():
    rot = 30
    shell = g(_ellipse(32, 30, 14.5, 18, INK), f"rotate({rot} 32 30)")
    rim = g(f'<path d="M20.5 30a11.5 14.5 0 1 0 23 0a11.5 14.5 0 1 0 -23 0Z" fill="none" '
            f'stroke="{HOLE}" stroke-width="2.4"/>', f"rotate({rot} 32 30)")
    hexp = [pt(32, 30, 6.5, 30 * 1 + 60 * k) for k in range(6)]
    hexa = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexp) + "Z", HOLE, 2.4)
    spokes = ""
    for k in range(6):
        a = 30 + 60 * k
        th = math.radians(a - rot)
        r = 1 / math.sqrt((math.cos(th) / 11.5) ** 2 + (math.sin(th) / 14.5) ** 2)
        spokes += line(*pt(32, 30, 6.5, a), *pt(32, 30, r, a), HOLE, 2.4)
    return shell + rim + hexa + spokes

@reg("kamoso", GREY_DARK)
def kamoso():
    cam = circle(32, 27, 14.5, INK) + circle(32, 27, 8.5, HOLE) + circle(32, 27, 5.5, CYAN)
    stand = line(32, 40, 32, 45, INK, 3.4) + rrect(23, 44, 18, 4.4, 2.2, INK)
    return cam + stand

@reg("kanagram", YELLOW_DARK)
def kanagram():
    k = (line(16, 17.5, 16, 42.5, INK, 4.6) + line(17.5, 31, 27, 17.5, INK, 4.6)
         + line(20.5, 28, 28, 42.5, INK, 4.6))
    gg = stroke("M47 21C45.5 18.8 43.2 17.5 40.3 17.5C35.3 17.5 32 22 32 30C32 38 35.3 42.5 40.3 42.5"
                "C44.3 42.5 47.3 40 47.3 35.3V31.5H41.5", INK, 4.6)
    return k + gg

@reg("kanatest", ORANGE_DEEP)
def kanatest():
    return (stroke("M18.5 20.5C25 21.5 33 20.5 41 18", INK, 3.8)
            + stroke("M28 13C27 24 28 36 32.5 46", INK, 3.8)
            + stroke("M38.5 25.5C31 31.5 22.5 37.5 22.5 42.5C22.5 46.5 28 46 32 41.5"
                     "C36 37 39.5 31 41.5 27.5C47.5 27.5 50 33 48 38.5C46.5 42.5 42 45 37 46", INK, 3.8))

@reg("kapman", AMBER_LIGHT)
def kapman():
    return (path("M44.3 21.4A15 15 0 1 0 44.3 38.6L33 30Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
            + circle(31, 21, 2.6, HOLE))

@reg("kapow", AMBER_DEEP)
def kapow():
    hands = AMBER_DARK
    face = circle(32, 30, 16.5, INK) + _sector(32, 30, 12.5, -90, -30, HOLE)
    ticks = "".join(circle(*pt(32, 30, 12.5, a), 1.6, hands) for a in (0, 90, 180))
    return (face + ticks + line(32, 30, 21.5, 35, hands, 2.8) + line(32, 30, 41, 24.5, hands, 2.8)
            + circle(32, 30, 2.6, hands))

@reg("kapptemplate", ORANGE)
def kapptemplate():
    check = "".join(rrect(14 + 9 * c, 12 + 9 * r, 9, 9, 1.5, ORANGE_SOFT)
                    for r in range(4) for c in range(4) if (r + c) % 2 == 0)
    return check + _gear(32, 30, 14, 10.5, 8, INK, .5) + circle(32, 30, 4.8, HOLE)

@reg("karbon", TEAL)
def karbon():
    a, b = pt(32, 30, 16.5, 205), pt(32, 30, 16.5, 25)
    disc_ = circle(32, 30, 16.5, INK)
    region = path(f"M{f(a[0])} {f(a[1])}C24 27 28 38 {f(b[0])} {f(b[1])}"
                  f"A16.5 16.5 0 0 1 {f(a[0])} {f(a[1])}Z", TEAL_DARK)
    nodes = "".join(circle(x, y, 3.6, TEAL_DARK) + circle(x, y, 2, INK)
                    for x, y in [(21, 22.5), (32, 35.5), (43.5, 38)])
    return disc_ + region + nodes

@reg("kasteroids", GREY_DEEP)
def kasteroids():
    rock = path("M17.5 27C17.5 18.5 24.5 14 32 14C40 14 47 18.5 47 27C48 32.5 46 38.5 42 42"
                "C37 46.5 27 46.5 22 42C18 38.5 17 32.5 17.5 27Z", INK)
    lava = path("M17.6 31C22 33 25 30 29 32C33 34 37 31 41 32.5C44 33.5 46 32 47.4 30.5"
                "C47.2 35.5 45.2 39.5 42 42C37 46.5 27 46.5 22 42C19 39.5 17.5 35.5 17.6 31Z", DEEP_ORANGE_LIGHT)
    craters = circle(25.5, 22, 3.8, HOLE) + circle(37.5, 19.5, 2.6, HOLE) + circle(41, 26.5, 2.4, HOLE)
    spots = circle(27, 38.5, 3.4, DEEP_ORANGE_DEEP) + circle(37.5, 38.5, 3.4, DEEP_ORANGE_DEEP)
    return rock + lava + craters + spots

@reg("kate", BLUE_DEEP)
def kate():
    crest = path("M14 19C18 17 22 13 28 12C32 11.5 35.5 12.5 37.5 13.5C31.5 14 29.5 17.5 31 21.5"
                 "L26 23C24 19.5 18.5 18.5 14 19Z", INK)
    wing = path("M21 36.5C16 30.5 19 25.5 27 23C35 20.5 42 18.5 49 16.5C40 20.5 30.5 23.5 25.5 27"
                "C22 29.5 20 32.5 21 36.5Z", INK)
    loop = stroke("M48.5 17C42.5 23 37 26.5 30.5 27.5C24.5 28.5 20 30 20 34.5C20 38.5 24.5 40.5 28.5 39.5"
                  "C32.5 38.5 32.5 33.5 30 30", INK, 3.4)
    tail = poly([(30.5, 28.5), (35, 28.3), (50, 40), (39.5, 37.5)], INK, 1.5)
    leg = poly([(32.5, 34), (35.5, 36), (41, 51), (36.5, 44)], INK, 1.5)
    return g(crest + wing + loop + tail + leg, "translate(32 31) scale(.88) translate(-32 -31)")

@reg("katomic", GREY_DARK)
def katomic():
    dark = _ring(23.5, 22, 7.8, INK, 3) + _ring(40.5, 38, 7.8, INK, 3)
    light = (circle(40, 21, 9.5, HOLE) + circle(40, 21, 8, INK)
             + circle(24, 38.5, 9.5, HOLE) + circle(24, 38.5, 8, INK))
    return dark + light

@reg("kawaii-player", BROWN_SOFT)
def kawaii_player():
    tails = (stroke("M21 16C15.5 20 15 29 19.5 35", BROWN_DEEP, 4.4)
             + stroke("M43 16C48.5 20 49 29 44.5 35", BROWN_DEEP, 4.4))
    return tails + circle(32, 24, 11, INK) + line(32, 35, 32, 47, BROWN_DEEP, 3)

@reg("kawanime", LIGHT_BLUE_DEEP)
def kawanime():
    hair = path("M32 12C21 12 15 20 15 30V47H22.5V37C25 40.5 28.5 42.5 32 42.5C35.5 42.5 39 40.5 41.5 37"
                "V47H49V30C49 20 43 12 32 12Z", INK)
    face = path("M22 27C25.5 25.5 29 22.5 31 19C33.5 23 37.5 25.5 42 26.5V33C42 38.5 37.5 42.5 32 42.5"
                "C26.5 42.5 22 38.5 22 33Z", DEEP_ORANGE_SOFT)
    eyes = circle(27, 32, 2.4, LIGHT_BLUE_DARK) + circle(37, 32, 2.4, LIGHT_BLUE_DARK)
    bows = "".join(poly([(x - 5, 16), (x, 19.5), (x - 5, 23)], PINK_SOFT, 1.5)
                   + poly([(x + 5, 16), (x, 19.5), (x + 5, 23)], PINK_SOFT, 1.5) for x in (18, 46))
    return hair + face + eyes + bows

@reg("kbackup", BLUE_GREY)
def kbackup():
    sheet = path("M17 11H31L37 17V38A2.5 2.5 0 0 1 34.5 40.5H17A2.5 2.5 0 0 1 14.5 38V13.5A2.5 2.5 0 0 1 17 11Z", INK)
    lines = "".join(rrect(18.5, y, 12, 2.4, 1.2, HOLE) for y in (21, 26))
    gap = rrect(25.5, 23.5, 26, 27, 4.5, HOLE)
    disk = rrect(27, 25, 23, 24, 3.5, BLUE_GREY_DARK)
    shutter = rrect(31.5, 25, 14, 7.5, 1, BLUE_GREY_SOFT)
    label = rrect(30.5, 36, 16, 10, 1.5, INK)
    return sheet + lines + gap + disk + shutter + label

@reg("kbibtex", TEAL)
def kbibtex():
    book = rrect(17, 12, 30, 36, 4, INK) + line(23, 12, 23, 48, HOLE, 2.2, "butt")
    k = (line(29.5, 21, 29.5, 39, HOLE, 4.2) + line(30.5, 31, 40, 21, HOLE, 4.2)
         + line(33, 28.5, 40, 39, HOLE, 4.2))
    return book + k

@reg("kblackbox", GREY_DARK)
def kblackbox():
    return (stroke("M23.5 21C23.5 15.5 27.5 12.5 32 12.5C36.8 12.5 40.5 15.8 40.5 20.5"
                   "C40.5 25 36.5 26.5 34 28.5C32.5 29.7 32 31 32 34.5", INK, 5.5)
            + circle(32, 43.5, 3.6, INK))

@reg("kblocks", RED_LIGHT)
def kblocks():
    sq = "".join(rrect(x, y, 15, 15, 3, INK) for x, y in [(15.5, 13), (33.5, 13), (15.5, 31), (33.5, 31)])
    return sq + circle(41, 20.5, 3.8, HOLE) + circle(23, 38.5, 3.8, HOLE)

@reg("kbounce", BLUE)
def kbounce():
    return circle(32, 30, 15.5, INK)

@reg("kbreakout", BROWN_LIGHT)
def kbreakout():
    bricks = "".join(rrect(x, y, 6.5, 5, 1, INK) for x, y in
                     [(28, 13), (35.5, 13), (43, 13), (35.5, 20), (43, 20), (15, 21)])
    return bricks + circle(33, 35, 3.2, INK) + rrect(22, 43, 20, 4.4, 2.2, INK)

@reg("kbruch", BROWN_SOFT)
def kbruch():
    one = stroke("M28.5 16.5L32.5 13.5V26.5", INK, 3.6)
    bar = line(19.5, 30.5, 44.5, 30.5, INK, 3.6)
    four = stroke("M35 47V34.5L25 43.5H39.5", INK, 3.6)
    return one + bar + four

@reg("kcachegrind", BLUE_DEEP)
def kcachegrind():
    gear = _gear(32, 30, 17, 13.5, 10, INK, .45) + circle(32, 30, 11, HOLE)
    pie = _sector(32, 30, 8.5, -90, 50, BLUE_SOFT)
    return gear + pie + line(32, 30, 32, 21.5, INK, 2.4) + circle(32, 30, 2.2, INK)

@reg("kcmdevices", GREY_DEEP)
def kcmdevices():
    return circle(32, 30, 16, INK) + circle(32, 30, 6.5, HOLE)

@reg("kcmdf", BLUE_GREY)
def kcmdf():
    return (rrect(24.5, 13, 15, 15, 3, INK) + rrect(15.5, 31, 15, 15, 3, INK)
            + rrect(33.5, 31, 15, 15, 3, INK))

@reg("kcmmemory", GREY_DARK)
def kcmmemory():
    chip = rrect(18, 13, 28, 34, 3, INK)
    lanes = "".join(line(x, y0, x, y1, HOLE, 2.4) for x, y0, y1 in
                    [(25.5, 18.5, 22), (25.5, 26.5, 36), (32, 18.5, 41.5), (38.5, 18.5, 26), (38.5, 30.5, 41.5)])
    pins = "".join(rrect(x, y, 3, 2.4, .8, INK) for y in (16, 21.5, 27, 32.5, 38, 43.5) for x in (14, 47))
    return chip + lanes + pins

@reg("kdbg", BROWN_SOFT)
def kdbg():
    return "".join(rrect(x, y, 13.5, 13.5, 2.5, c) for (x, y), c in
                   [((17, 15), INK), ((33.5, 15), RED_DEEP), ((17, 31.5), INK), ((33.5, 31.5), INK)])

@reg("kde-frameworks", CYAN_DEEP)
def kde_frameworks():
    return _kde()

@reg("kdeconnect", BLUE_GREY_DEEP)
def kdeconnect():
    phone = rrect(20, 11, 24, 38, 4, INK) + rrect(22.5, 16, 19, 25.5, 1.5, HOLE)
    extras = line(29.5, 13.5, 34.5, 13.5, HOLE, 1.6) + rrect(29, 43.5, 6, 2.6, 1.3, HOLE)
    k = (line(28, 23, 28, 35, INK, 3) + line(29, 29.5, 36, 22.5, INK, 3) + line(31.3, 28, 36.3, 35, INK, 3))
    return phone + extras + k

@reg("kdenlive", BLUE_GREY_DARK)
def kdenlive():
    dashes = "".join(rrect(26 - w, y, w, 2.8, 1.4, INK) for y, w in
                     [(16, 5), (21, 9), (26, 12), (31, 12), (36, 9), (41, 6)])
    head = line(29, 17, 29, 47, RED, 3) + poly([(25, 12.5), (33, 12.5), (29, 17.5)], RED, 1.5)
    play = poly([(34, 20.5), (48.5, 30), (34, 39.5)], INK, 2.5)
    return dashes + head + play

@reg("kdesvn", BLUE_LIGHT)
def kdesvn():
    links = stroke("M17 30H33V17.5M33 30L37.5 42H46", INK, 2.8)
    nodes = "".join(circle(x, y, 3.6, INK) for x, y in
                    [(17, 30), (25, 30), (33, 30), (33, 17.5), (37.5, 42), (46, 42)])
    return links + nodes

@reg("kdevelop", LIGHT_BLUE_DEEP)
def kdevelop():
    gear = _gear(32, 30, 17.5, 13.5, 8, INK, .5)
    k = (line(27, 21.5, 27, 38.5, HOLE, 4.2) + line(28, 31, 37.5, 21.5, HOLE, 4.2)
         + line(30.5, 29, 37.5, 38.5, HOLE, 4.2))
    return gear + k

@reg("kdiamond", BLUE_GREY_DARK)
def kdiamond():
    d = 9
    out = ""
    for (cx, cy), c in [((22.5, 20.5), BLUE_LIGHT), ((41.5, 20.5), AMBER),
                        ((22.5, 39.5), RED_LIGHT), ((41.5, 39.5), GREY)]:
        out += poly([(cx, cy - d), (cx + d, cy), (cx, cy + d), (cx - d, cy)], c, 2.5)
    return out

@reg("kdiff3", GREY_DARK)
def kdiff3():
    top = path("M21 12H43A4 4 0 0 1 47 16V30H17V16A4 4 0 0 1 21 12Z", INK)
    bottom = path("M17 30H47V44A4 4 0 0 1 43 48H21A4 4 0 0 1 17 44Z", GREY_LIGHT)
    lines = "".join(rrect(22, y, 20, 2.6, 1.3, HOLE) for y in (17, 22.5, 34.5, 40))
    return top + bottom + lines

@reg("kdiskmark", CYAN_DEEP)
def kdiskmark():
    dome = path("M14 40A18 18 0 0 1 50 40Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    arc = stroke("M19.5 38.5A12.5 12.5 0 0 1 44.5 38.5", HOLE, 2.4)
    needle = line(32, 39, 38, 28.5, HOLE, 3.2) + circle(32, 39, 3, HOLE)
    return dome + arc + needle

@reg("kdocker", INDIGO)
def kdocker():
    win = rrect(14.5, 13, 20, 14, 3, INK)
    arrow = stroke("M36.5 19C42 19 44 22.5 44 29", INK, 3.6) + poly([(38.5, 29.5), (49.5, 29.5), (44, 36)], INK, 2)
    dock = rrect(13, 39, 38, 9, 3, INK) + "".join(circle(x, 43.5, 1.8, HOLE) for x in (36, 41, 46))
    return win + arrow + dock

@reg("kdots", INDIGO_DEEP)
def kdots():
    grid = ("".join(line(x, 13, x, 47, INDIGO_LIGHT, 2.2) for x in (19, 32, 45))
            + "".join(line(15, y, 49, y, INDIGO_LIGHT, 2.2) for y in (17, 30, 43)))
    link = stroke("M32 17L45 30L32 43L19 30Z", INK, 2.6)
    dots = "".join(circle(x, y, 3.6, INK) for x, y in [(32, 17), (45, 30), (32, 43), (19, 30)])
    red = circle(32, 30, 3.6, RED_LIGHT) + circle(19, 43, 3.6, RED_LIGHT)
    return grid + link + dots + red

@reg("keduca", BLUE_GREY)
def keduca():
    ball = circle(32, 30, 16.5, INK) + path("M32 13.5A16.5 16.5 0 0 1 32 46.5Z", RED_LIGHT)
    q = (stroke("M26 24C26 19.5 28.8 17 32.3 17C36 17 38.5 19.5 38.5 23C38.5 26.5 35.5 27.5 33.8 29"
                "C32.8 29.8 32.3 31 32.3 33.5", HOLE, 4.4) + circle(32.3, 40, 2.8, HOLE))
    return ball + q

@reg("keep", AMBER_DEEP)
def keep():
    bulb = circle(32, 24, 11.5, INK) + circle(32, 24, 6.5, HOLE)
    base = rrect(25.5, 33, 13, 13, 2.5, INK) + line(28.5, 38, 35.5, 38, HOLE, 2.2) + line(28.5, 42, 35.5, 42, HOLE, 2.2)
    return bulb + base

@reg("keepass", INDIGO_LIGHT)
def keepass():
    shackle = stroke("M24.5 29V22.5A7.5 7.5 0 0 1 39.5 22.5V29", INK, 4.4)
    body = rrect(18.5, 27, 27, 20.5, 4, INK)
    hole = circle(32, 35, 3, HOLE) + rrect(30.8, 35, 2.4, 6.5, 1.2, HOLE)
    return shackle + body + hole

@reg("keepassx", ORANGE_DARK)
def keepassx():
    key = (line(40, 22, 18, 44, HOLE, 8) + line(40, 22, 18, 44, INK, 4.4)
           + circle(42, 19.5, 7, HOLE) + circle(42, 19.5, 5.8, INK) + circle(43, 18.5, 2.2, HOLE)
           + line(22, 40, 26, 44, INK, 3.6))
    jaw = g(rrect(12.5, 16.5, 7.5, 4, 1, HOLE), "rotate(45 19.5 18.5)")
    wrench = line(21, 20, 46, 45, INK, 4.6) + circle(19.5, 18.5, 5.8, INK) + jaw
    return wrench + key

@reg("keeweb", INDIGO)
def keeweb():
    ring = _ring(23, 21, 6.8, INK, 4.4)
    shaft = line(28, 26, 45, 43, INK, 4.4)
    teeth = line(38.5, 36.5, 34.5, 40.5, INK, 3.8) + line(43, 41, 39.5, 44.5, INK, 3.8)
    return ring + shaft + teeth

@reg("kega-fusion", INDIGO)
def kega_fusion():
    orange = DEEP_ORANGE_LIGHT
    bar = rrect(16, 13, 8.5, 34, 1.5, INK)
    arm = poly([(24.5, 27), (37, 13), (47, 13), (31, 31.5)], INK, 1.5)
    leg = poly([(28, 33.5), (33.5, 26.5), (48, 47), (38, 47)], INK, 1.5)

    t = (38 - 26.5) / (47 - 26.5)
    xr = 33.5 + t * (48 - 33.5)
    tl = (38 - 33.5) / (47 - 33.5)
    xl = 28 + tl * (38 - 28)
    band = (rrect(16, 38, 8.5, 9, 1.5, orange) + rrect(16, 38, 8.5, 4, 0, orange)
            + poly([(xl, 38), (xr, 38), (48, 47), (38, 47)], orange, 1.5))
    return bar + arm + leg + band

@reg("kerbal-space-program", BLUE_GREY_DARK)
def kerbal():
    helmet = circle(16.5, 28, 3.6, INK) + circle(47.5, 28, 3.6, INK) + circle(32, 28, 16, INK)
    visor = circle(32, 28, 12, HOLE)
    head = path("M23.5 40V25C23.5 19.5 26.5 16.5 29 16.5C30.5 16.5 31 18 32 18C33 18 34 16.5 36 16.5"
                "C39 16.5 40.5 20 40.5 25V40C36 41.8 28 41.8 23.5 40Z", LIGHT_BLUE_SOFT)
    eyes = circle(28, 27, 3, INK) + circle(36.5, 27, 3, INK) + circle(28.6, 27.4, 1.3, HOLE) + circle(37.1, 27.4, 1.3, HOLE)
    mouth = stroke("M27 34.5Q32 37 37 34.5", LIGHT_BLUE_DARK, 2.4)
    neck = rrect(23, 45, 18, 3.6, 1.8, INK)
    return helmet + visor + head + eyes + mouth + neck

@reg("keurocalc", BLUE)
def keurocalc():
    e = stroke("M44.5 17.5C42.3 15.3 39.3 14 35.8 14C27.3 14 22 21 22 30C22 39 27.3 46 35.8 46"
               "C39.3 46 42.3 44.7 44.5 42.5", INK, 4.4)
    return e + line(16, 26, 34, 26, INK, 3.6) + line(16, 34, 32, 34, INK, 3.6)

@reg("kexi", LIGHT_BLUE)
def kexi():
    return "".join(rrect(19, y, 26, 8.5, 4.25, INK) for y in (15, 25.5, 36))

@small("kali-menu")
def kali_menu_s():
    plate = poly([(24, 15), (49, 15), (41, 46), (15, 46)], BLUE_GREY_DARK, 3)
    body = stroke("M41 21.5C33.5 20 27.5 24.5 27.5 30.5C27.5 36.5 33 39 39.5 39.5"
                  "C44.5 40 47.5 43 48.5 48", INK, 3.4)
    head = poly([(37, 19), (43.5, 20), (50, 25), (44, 26.5), (39.5, 25)], INK, 2)
    return (plate + body + head + stroke("M38.5 19.5C31 14 22 12 14 12.5", INK, 2.6)
            + stroke("M36 22C30 20 23 20.5 16 23", INK, 2.6))

@small("kali-undercover")
def kali_undercover_s():
    crown = path("M22 24L25.5 14.5C26.3 12.5 28 12.5 32 14C36 12.5 37.7 12.5 38.5 14.5L42 24Z", INK)
    return (crown + line(14, 25.5, 50, 25.5, INK, 3.6) + rrect(15, 31, 15, 12, 4.5, INK)
            + rrect(34, 31, 15, 12, 4.5, INK) + line(29, 35, 35, 35, INK, 3))

@small("kali-unix-privesc-check")
def kali_monkey_s():
    fur = BROWN_SOFT
    head = circle(16, 27, 6, fur) + circle(48, 27, 6, fur) + circle(32, 30, 16, fur)
    mask = circle(26, 25, 7, INK) + circle(38, 25, 7, INK) + _ellipse(32, 37, 13, 8.5, INK)
    return head + mask + circle(26, 25, 3.2, BROWN_DARK) + circle(38, 25, 3.2, BROWN_DARK)

@small("kame-editor")
def kame_editor_s():
    shell = g(_ellipse(32, 30, 15, 18.5, INK), "rotate(30 32 30)")
    hexa = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in
                                 [pt(32, 30, 7, 30 + 60 * k) for k in range(6)]) + "Z", HOLE, 3)
    return shell + hexa

@small("kamoso")
def kamoso_s():
    return (circle(32, 27, 15.5, INK) + circle(32, 27, 8, CYAN)
            + line(32, 40, 32, 45, INK, 4) + rrect(22, 44, 20, 5, 2.5, INK))

@small("kanagram")
def kanagram_s():
    k = (line(17, 17, 17, 43, INK, 5.2) + line(19, 31, 28, 17, INK, 5.2) + line(22, 28.5, 29, 43, INK, 5.2))
    gg = stroke("M47.5 21C46 18.5 43.5 17 40.5 17C36 17 33.5 22 33.5 30C33.5 38 36 43 40.5 43"
                "C45 43 47.5 40 47.5 35V32H42", INK, 5.2)
    return k + gg

@small("kanatest")
def kanatest_s():
    return (stroke("M18 21C25 22 33 21 41 18.5", INK, 4)
            + stroke("M28 13C27 24 28 36 32.5 46.5", INK, 4)
            + stroke("M39 26C31 32 22 38 22 43C22 47 28 46 32 41.5C36 37 39.5 31 42 28"
                     "C48.5 28 50.5 34 48 39.5C46.5 43 42.5 45.5 37.5 46.5", INK, 4))

@small("kapow")
def kapow_s():
    hands = LIGHT_BLUE_DARK
    return (circle(32, 30, 17, INK) + _sector(32, 30, 13, -90, -30, HOLE)
            + line(32, 30, 22, 35, hands, 3.4) + line(32, 30, 41, 24.5, hands, 3.4))

@small("kapptemplate")
def kapptemplate_s():
    check = rrect(13, 11, 19, 19, 2, ORANGE_SOFT) + rrect(32, 30, 19, 19, 2, ORANGE_SOFT)
    return check + _gear(32, 30, 15, 11, 6, INK, .5) + circle(32, 30, 4.5, HOLE)

@small("karbon")
def karbon_s():
    a, b = pt(32, 30, 17, 205), pt(32, 30, 17, 25)
    region = path(f"M{f(a[0])} {f(a[1])}C24 27 28 38 {f(b[0])} {f(b[1])}"
                  f"A17 17 0 0 1 {f(a[0])} {f(a[1])}Z", TEAL_DARK)
    nodes = "".join(circle(x, y, 4.2, TEAL_DARK) + circle(x, y, 2.4, INK) for x, y in [(21, 22.5), (32, 35.5)])
    return circle(32, 30, 17, INK) + region + nodes

@small("kasteroids")
def kasteroids_s():
    rock = path("M16.5 27C16.5 18 24 13 32 13C40.5 13 48 18 48 27C49 33 47 39 43 42.5"
                "C37.5 47.5 26.5 47.5 21 42.5C17 39 16 33 16.5 27Z", INK)
    lava = path("M16.6 31.5C22 34 26 30.5 32 32.5C38 34.5 43 31 48.4 31"
                "C48 36 46 40 43 42.5C37.5 47.5 26.5 47.5 21 42.5C18 40 16.5 36 16.6 31.5Z", DEEP_ORANGE_LIGHT)
    return rock + lava + circle(26, 22, 4.2, HOLE) + circle(39, 22, 3, HOLE)

@small("kate")
def kate_s():
    crest = path("M13 19C18 16.5 22 12.5 28 11.5C32 11 35.5 12 38 13.5C31.5 14 29.5 17.5 31 22"
                 "L25.5 23.5C23.5 19.5 18.5 18.5 13 19Z", INK)
    wing = path("M21 37C15.5 30.5 19 25 27 22.5C35 20 42 18 50 15.5C41 20.5 31 24 26 27.5"
                "C22.5 30 20 33 21 37Z", INK)
    tail = poly([(29, 28), (35, 27.5), (50, 40), (39, 38)], INK, 2)
    leg = poly([(31.5, 33.5), (36, 35.5), (41, 49), (35, 43)], INK, 2)
    return g(crest + wing + tail + leg, "translate(32 31) scale(.9) translate(-32 -31)")

@small("katomic")
def katomic_s():
    return (_ring(23, 21.5, 7.5, INK, 3.4) + _ring(41, 38.5, 7.5, INK, 3.4)
            + circle(41, 21, 10, HOLE) + circle(41, 21, 8, INK)
            + circle(23, 39, 10, HOLE) + circle(23, 39, 8, INK))

@small("kawanime")
def kawanime_s():
    hair = path("M32 11C20.5 11 14.5 19.5 14.5 30V48H23V38C25.5 41.5 28.5 43 32 43C35.5 43 38.5 41.5 41 38"
                "V48H49.5V30C49.5 19.5 43.5 11 32 11Z", INK)
    face = path("M22.5 26.5C26 25 29 22 31 18.5C33.5 22.5 37.5 25 41.5 26V33C41.5 38.5 37.5 43 32 43"
                "C26.5 43 22.5 38.5 22.5 33Z", DEEP_ORANGE_SOFT)
    bows = circle(15.5, 17.5, 4, PINK_SOFT) + circle(48.5, 17.5, 4, PINK_SOFT)
    return hair + face + bows

@small("kbackup")
def kbackup_s():
    sheet = path("M16 10H31L37.5 16.5V38A2.5 2.5 0 0 1 35 40.5H16A2.5 2.5 0 0 1 13.5 38V12.5A2.5 2.5 0 0 1 16 10Z", INK)
    return (sheet + rrect(24, 22, 28, 28.5, 5, HOLE) + rrect(26, 24, 24, 25, 3.5, BLUE_GREY_DARK)
            + rrect(30, 35, 16, 11, 2, INK))

@small("kbreakout")
def kbreakout_s():
    bricks = "".join(rrect(x, y, 9, 6.5, 1.2, INK) for x, y in [(27, 12), (38, 12), (38, 21), (14, 21)])
    return bricks + circle(32, 35, 4, INK) + rrect(20, 43, 24, 5, 2.5, INK)

@small("kbruch")
def kbruch_s():
    return (stroke("M28 16.5L33 13V26", INK, 4) + line(18.5, 30.5, 45.5, 30.5, INK, 4)
            + stroke("M35.5 47.5V35L25 44H40", INK, 4))

@small("kcachegrind")
def kcachegrind_s():
    return (_gear(32, 30, 17.5, 13.5, 8, INK, .5) + circle(32, 30, 10.5, HOLE)
            + _sector(32, 30, 8.5, -90, 60, BLUE_SOFT))

@small("kcmmemory")
def kcmmemory_s():
    chip = rrect(17, 12, 30, 36, 3.5, INK)
    lanes = line(26, 18, 26, 42, HOLE, 3) + line(38, 18, 38, 42, HOLE, 3)
    pins = "".join(rrect(x, y, 4, 3.5, 1, INK) for y in (16, 28, 40) for x in (12, 48))
    return chip + lanes + pins

@small("kde-frameworks")
def kde_frameworks_s():
    return shared_kde_s()

@small("kdeconnect")
def kdeconnect_s():
    phone = rrect(18.5, 10, 27, 40, 4.5, INK) + rrect(22, 15, 20, 28, 1.5, HOLE)
    k = (line(27.5, 21.5, 27.5, 36.5, INK, 3.4) + line(28.5, 29.5, 36.5, 21.5, INK, 3.4)
         + line(31, 27.5, 37, 36.5, INK, 3.4))
    return phone + k

@small("kdenlive")
def kdenlive_s():
    dashes = "".join(rrect(26 - w, y, w, 4, 2, INK) for y, w in [(18, 7), (26, 12), (34, 9)])
    head = line(29, 17, 29, 47, RED, 3.4) + poly([(24.5, 12), (33.5, 12), (29, 18)], RED, 1.5)
    return dashes + head + poly([(34, 19.5), (49.5, 30), (34, 40.5)], INK, 2.5)

@small("kdesvn")
def kdesvn_s():
    return (stroke("M16 30H32V16M32 30L37 43H47", INK, 3.2)
            + "".join(circle(x, y, 4.4, INK) for x, y in [(16, 30), (32, 30), (32, 16), (37, 43), (47, 43)]))

@small("kdevelop")
def kdevelop_s():
    return (_gear(32, 30, 18, 14, 7, INK, .5) + line(26.5, 21, 26.5, 39, HOLE, 4.6)
            + line(27.5, 31, 38, 21, HOLE, 4.6) + line(30.5, 29, 38, 39, HOLE, 4.6))

@small("kdiff3")
def kdiff3_s():
    top = path("M21 11H43A4 4 0 0 1 47 15V30H17V15A4 4 0 0 1 21 11Z", INK)
    bottom = path("M17 30H47V45A4 4 0 0 1 43 49H21A4 4 0 0 1 17 45Z", GREY_LIGHT)
    return top + bottom + "".join(rrect(21.5, y, 21, 4, 2, HOLE) for y in (18.5, 36.5))

@small("kdiskmark")
def kdiskmark_s():
    dome = path("M13 41A19 19 0 0 1 51 41Z", INK, f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return dome + line(32, 40, 39, 27.5, HOLE, 4) + circle(32, 40, 3.8, HOLE)

@small("kdocker")
def kdocker_s():
    return (rrect(13.5, 12, 21, 15, 3, INK) + stroke("M36.5 19C43 19 44.5 22.5 44.5 28", INK, 4)
            + poly([(38.5, 28.5), (50.5, 28.5), (44.5, 35.5)], INK, 2) + rrect(12.5, 39, 39, 10, 3.5, INK))

@small("kdots")
def kdots_s():
    link = stroke("M32 15L47 30L32 45L17 30Z", INK, 3)
    dots = "".join(circle(x, y, 4.4, INK) for x, y in [(32, 15), (47, 30), (32, 45), (17, 30)])
    return link + dots + circle(32, 30, 4.4, RED_LIGHT)

@small("keduca")
def keduca_s():
    ball = circle(32, 30, 17, INK) + path("M32 13A17 17 0 0 1 32 47Z", RED_LIGHT)
    return (ball + stroke("M25.5 23.5C25.5 18.5 28.5 16 32.3 16C36.5 16 39 18.8 39 22.5"
                          "C39 26.5 35.5 27.5 33.8 29.3C32.8 30.3 32.3 31.5 32.3 33.5", HOLE, 4.6)
            + circle(32.3, 41, 3.3, HOLE))

@small("keep")
def keep_s():
    return (circle(32, 23.5, 12.5, INK) + circle(32, 23.5, 6.5, HOLE)
            + rrect(25, 33, 14, 14, 3, INK) + line(28.5, 40, 35.5, 40, HOLE, 3))

@small("keepassx")
def keepassx_s():
    wrench = line(20, 19, 46, 45, INK, 5)
    key = (line(40, 22, 18, 44, HOLE, 9) + line(40, 22, 18, 44, INK, 5)
           + circle(42, 19.5, 8.5, HOLE) + circle(42, 19.5, 7, INK) + circle(43, 18.5, 2.6, HOLE))
    return wrench + circle(18, 17, 5, INK) + key

@small("kerbal-space-program")
def kerbal_s():
    helmet = circle(32, 29, 17.5, INK) + circle(32, 29, 13, HOLE)
    head = path("M22.5 42V25C22.5 19 26 16 29 16C30.5 16 31 17.5 32 17.5C33 17.5 34 16 36 16"
                "C39.5 16 41.5 19.5 41.5 25V42C36 44 28 44 22.5 42Z", LIGHT_BLUE_SOFT)
    eyes = circle(27.5, 28, 3.8, INK) + circle(37, 28, 3.8, INK)
    return helmet + head + eyes

@small("kexi")
def kexi_s():
    return "".join(rrect(18, y, 28, 9, 4.5, INK) for y in (13, 25.5, 38))
