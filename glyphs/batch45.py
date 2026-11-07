# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 45: mikutter to motrix.

Same rules as batch01: tile is the palette step nearest the brand colour,
the mark is INK, HOLE is the tile showing through, extra shades come
from the palette.
"""
from lm import *
from glyphs.kit import arc, badge, ell_f, gear_h, registry, _ring, shrink

ICONS, SMALL, reg, small = registry()

def globe(cx, cy, r, fill, line_col, w=2.2):
    return (circle(cx, cy, r, fill) +
            f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(r * .42)}" ry="{f(r)}" fill="none" '
            f'stroke="{line_col}" stroke-width="{f(w)}"/>' +
            line(cx - r, cy, cx + r, cy, line_col, w, "butt"))

@reg("mikutter", PINK_LIGHT)
def mikutter():
    return stroke("M19 42V28A6.5 6.5 0 0 1 32 28V42M32 28A6.5 6.5 0 0 1 45 28V42", INK, 7)

@reg("milkytracker", BLUE_DEEP)
def milkytracker():
    carton = path("M18 21L22 13H42L46 21V46A2.5 2.5 0 0 1 43.5 48.5H20.5A2.5 2.5 0 0 1 18 46Z", INK)
    ridge = line(18.5, 21, 45.5, 21, HOLE, 2.2, "butt")
    m = stroke("M21.5 42V28.5L25.5 35L29.5 28.5V42", HOLE, 2.6)
    t = stroke("M34 28.5H42.5M38.25 28.5V42", HOLE, 2.6)
    return carton + ridge + m + t

@reg("min", ORANGE_DEEP)
def min_():
    disc = circle(CX, CY, 11.5, BLUE_DEEP)
    half = path(arc(CX, CY, 11.5, -60, 120) + "Z", INDIGO_DEEP)
    return _ring(CX, CY, 14.5, INK, 4) + disc + half

@reg("mindustry", GREY_DARK)
def mindustry():
    m = path("M24 16H29.5L32 21L34.5 16H40V44H35V27L32 33L29 27V44H24Z", INK)
    chev = (stroke("M20 22L14.5 30L20 38", ORANGE_LIGHT, 3.4) +
            stroke("M44 22L49.5 30L44 38", ORANGE_LIGHT, 3.4))
    return m + chev

@reg("minetest", LIGHT_BLUE_DARK)
def minetest():
    ground = poly([(32, 33), (48, 40.5), (32, 48), (16, 40.5)], LIGHT_BLUE_SOFT, 2)
    trunk = rrect(29.5, 27, 5, 13, 1, BROWN_SOFT)
    top = poly([pt(32, 20.5, 9.5, -90 + 60 * k) for k in range(6)], INK, 2)
    shade = poly([(32, 20.5), pt(32, 20.5, 9.5, 30), pt(32, 20.5, 9.5, 90)], LIGHT_BLUE_SOFT, 2)
    return ground + trunk + top + shade

@reg("minetime", GREY_DEEP)
def minetime():
    left = poly([(18, 20), (25, 16), (25, 44), (18, 44)], GREY_SOFT, 1.5)
    rest = poly([(25, 16), (32, 25), (39, 16), (46, 20), (46, 44), (39, 44), (39, 29), (32, 37), (25, 29)], INK, 1.5)
    return left + rest

@reg("minicraft+", TEAL_DARK)
def minicraft():
    m = stroke("M17 44L24.5 20L31 38L38.5 20L43 44", INK, 6)
    plus = stroke("M44 11V21M39 16H49", AMBER_LIGHT, 3.6)
    return m + plus

@reg("minigalaxy", YELLOW_DARK)
def minigalaxy():
    body = path("M18 49V43A7 7 0 0 1 25 36H39A7 7 0 0 1 46 43V49Z", INK)
    helmet = circle(32, 27, 16, INK) + circle(32, 27, 13, HOLE)
    head = path("M22 38V26A10 10 0 0 1 42 26V38Z", YELLOW_SOFT)
    eye = circle(32, 25.5, 5.5, INK) + circle(33, 26, 2.6, BROWN_DARK)
    smile = stroke("M27.5 33.5Q32 36 36.5 33.5", YELLOW_DARK, 2.2)
    return body + helmet + head + eye + smile

@reg("minitube", BROWN)
def minitube():
    tv = rrect(14, 15, 36, 29, 5, INK)
    screen = rrect(17.5, 18.5, 22, 22, 5, BLUE_LIGHT)
    knobs = circle(45, 22.5, 2.3, HOLE) + circle(45, 29.5, 2.3, HOLE)
    grille = rrect(42.5, 35, 5, 2.2, 1, HOLE) + rrect(42.5, 38.5, 5, 2.2, 1, HOLE)
    return tv + screen + knobs + grille

def _mint(w=3.4):
    return (stroke("M16 15V35A6 6 0 0 0 22 41H42A6 6 0 0 0 48 35V26A5 5 0 0 0 38 26", INK, w) +
            stroke("M23 15V34", INK, w) + stroke("M28.5 34V26A4.75 4.75 0 0 1 38 26V34", INK, w))

@reg("mint-dev-settings", INDIGO_SOFT)
def mint_dev_settings():
    return (shrink(_mint(), .82, 28.5, 26) + badge(42.5, 40.5, BLUE_DEEP) +
            gear_h(42.5, 40.5, 4.8, INK, BLUE_DEEP))

@reg("mintnanny", LIGHT_BLUE_DEEP)
def mintnanny():
    world = globe(29, 27, 14.5, INK, HOLE, 2.4)
    alert = rrect(41.25, 34, 2.5, 7, 1.25, INK) + circle(42.5, 44.5, 1.5, INK)
    return world + badge(42.5, 40.5, RED_DEEP, 9.5) + alert

@reg("mintsources-additional", GREY_DEEP)
def mintsources_additional():
    return rrect(27, 13, 10, 16, 2, INK) + poly([(17, 28), (47, 28), (32, 46)], INK, 3)

@reg("mintsources-foreign", PINK_LIGHT)
def mintsources_foreign():
    q = stroke("M24 21.5A8 8 0 1 1 35.5 28.5C33 30 32 31.5 32 35", INK, 5.5)
    return q + circle(32, 43.5, 3.3, INK)

@reg("mintsources-maintenance", BLUE_GREY)
def mintsources_maintenance():
    return gear_h(CX, CY, 12.5, INK, HOLE, 8, 6.5)

@reg("mintsources-ppa", BLUE_GREY_DEEP)
def mintsources_ppa():
    out = ""
    for k in range(6):
        a0, a1 = -90 + 60 * k, -30 + 60 * k
        out += poly([pt(CX, CY, 16, a0), pt(CX, CY, 16, a1), pt(CX, CY, 8, a1), pt(CX, CY, 8, a0)],
                    INK, 0)
        out += line(*pt(CX, CY, 7.5, a0), *pt(CX, CY, 16.5, a0), HOLE, 2, "butt")
    inner = poly([pt(CX, CY, 6.5, -90 + 60 * k) for k in range(6)], AMBER_LIGHT, 1.5)
    return out + inner

@reg("mintupload", INDIGO_LIGHT)
def mintupload():
    return rrect(28.5, 26, 7, 21, 1.5, INK) + poly([(19, 28), (45, 28), (32, 13)], INK, 3)

@reg("minuet", DEEP_PURPLE_DEEP)
def minuet():
    cols = [RED_LIGHT, ORANGE_LIGHT, YELLOW_LIGHT, PURPLE_SOFT, BLUE_LIGHT, PURPLE_SOFT]
    keys = "".join(rrect(15 + 5.8 * k, 14, 4.8, 32, 1.8, c) for k, c in enumerate(cols))
    blacks = "".join(rrect(18.2 + 5.8 * k, 12.5, 4, 17, 1.5, HOLE) for k in (0, 1, 3, 4))
    return keys + blacks

@reg("miro", RED_DEEP)
def miro():
    return stroke("M18.5 43V22H40.5A5 5 0 0 1 45.5 27V43M29.5 22V43", INK, 6.5).replace(
        'stroke-linecap="round" stroke-linejoin="round"', 'stroke-linecap="butt" stroke-linejoin="miter"')

@reg("mist", INDIGO_DEEP)
def mist():
    top = poly([(32, 11), (44, 31), (32, 37.5), (20, 31)], INK, 1.5)
    shade = poly([(32, 11), (44, 31), (32, 37.5)], DEEP_PURPLE_SOFT, 1.5)
    low = poly([(20, 34.5), (32, 41), (44, 34.5), (32, 49)], INK, 1.5)
    return top + shade + low

@reg("mixcloud", DEEP_PURPLE_DEEP)
def mixcloud():
    cloud = path("M20 43A9 9 0 0 1 19 25A11 11 0 0 1 40 20.5A9.5 9.5 0 0 1 45 43Z", INK)
    marks = (stroke(arc(28, 33, 5, -60, 60), HOLE, 3) + stroke(arc(28, 33, 10, -55, 55), HOLE, 3))
    return g(cloud + marks, "translate(0 -2)")

@reg("mixxx", DEEP_ORANGE_DEEP)
def mixxx():
    disc = circle(CX, CY, 16.5, INK)
    groove = _ring(CX, CY, 12, HOLE, 2)
    centre = circle(CX, CY, 7, HOLE) + circle(CX, CY, 4.2, INK) + circle(CX, CY, 1.8, HOLE)
    return disc + groove + centre

@reg("mkusb", INDIGO_SOFT)
def mkusb():
    body = (line(19, 43, 43, 19, INK, 3.4) + poly([(45.5, 16.5), (37, 18.5), (43.5, 25)], INK, 2))
    br1 = stroke("M27 35L25 29L28.5 25.5", INK, 3) + circle(28.5, 25.5, 3.2, INK)
    br2 = stroke("M33 29L39 31L42 34", INK, 3) + g(rrect(39.5, 31.5, 6, 6, 1, INK), "rotate(45 42.5 34.5)")
    return body + br1 + br2 + circle(19, 43, 4.5, INK)

def _mkv():
    orbit = ell_f(32, 30, 18, 8, "none", -25, f' stroke="{INK}" stroke-width="3"')
    core = circle(32, 30, 11, INK)
    swirl = stroke("M26 32.5A6 6 0 0 1 38 29", HOLE, 2.6)
    ball = circle(38.5, 20, 5.8, HOLE) + circle(38.5, 20, 4.4, RED)
    return orbit + core + swirl + ball + circle(18.5, 39, 3, INK)

@reg("mkvinfo", BLUE_GREY_DEEP)
def mkvinfo():
    info = circle(43, 36, 1.5, INK) + rrect(41.75, 39, 2.5, 7, 1.25, INK)
    return shrink(_mkv(), .85, 28, 27) + badge(43, 40.5, BROWN_LIGHT, 9.5) + info

@reg("mkvmergeGUI", BLUE_GREY_DEEP)
def mkvmerge():
    return _mkv()

@reg("ml.prevete.Daty", BLUE_GREY_DARK)
def daty():
    bars = [(15, 3, RED_LIGHT), (19.5, 3, RED_LIGHT), (24, 1.5, RED_LIGHT),
            (27, 3, AMBER_DEEP), (31.5, 1.5, AMBER_DEEP), (34.5, 3, AMBER_DEEP),
            (39, 3, BLUE_LIGHT), (43.5, 1.5, BLUE_LIGHT), (46.5, 2.5, BLUE_LIGHT)]
    return rrect(13, 15, 38, 30, 3, INK) + "".join(rrect(x + .5, 18, w + .3, 24, .4, c) for x, w, c in bars)

@reg("mlgui", GREY_DARK)
def mlgui():
    wheel = _ring(CX, CY, 14, INK, 4.2)
    holes = "".join(circle(*pt(CX, CY, 14, -90 + 72 * k), 1.8, HOLE) for k in range(5))
    v = stroke("M15 14H20L32 44L44 14H49M24 23H40", AMBER_DEEP, 4.4)
    return wheel + holes + v

@reg("mlterm", BLUE_GREY_DARK)
def mlterm():
    t = stroke("M16 18L24 25L16 32", INK, 4.4) + rrect(27, 30, 12, 4.4, 2.2, INK)
    return t + badge(42.5, 40.5, BLUE_DEEP, 9) + globe(42.5, 40.5, 6.5, INK, BLUE_DEEP, 1.8)

@reg("mnemosyne", BLUE_GREY_DEEP)
def mnemosyne():
    return g(_mnem(), "translate(32 30) scale(1.12) translate(-34 -30)")

def _mnem():
    fore = path("M31 27C33 18 38 12 41 11C44 16 46 21 43 27C47 28 50 33 49 39"
                "C47 45 40 48 35 44C33 42 31 37 31 27Z", INK)
    veins = stroke("M35.5 21L39.5 18.5M34.5 25.5L39 24", HOLE, 2.2)
    body = line(29, 29, 40, 47, BLUE_GREY_DARK, 2.6) + circle(29, 29, 3, BLUE_GREY_DARK)
    ant = stroke("M27.5 27.5C24 22 20 21.5 17 22.5", BLUE_GREY_DARK, 2.2) + circle(17, 22.5, 2.3, BLUE_GREY_DARK)
    return fore + veins + body + ant

@reg("mntray", TEAL)
def mntray():
    box = rrect(20, 22, 29, 20, 3, TEAL_DARK) + poly([(38, 41), (44, 41), (41, 46)], TEAL_DARK, 2)
    bars = rrect(15, 12, 7.5, 28, 1.2, INK) + rrect(25, 12, 7.5, 21, 1.2, INK)
    return box + bars

@reg("modelio", RED_DEEP)
def modelio():
    out = _ring(CX, CY, 15.5, INK, 2.4)
    out += stroke(arc(CX, CY, 11.5, -55, 55), INK, 4.5)
    out += "".join(rrect(x, 30 - h / 2, 3.6, h, 1.8, INK) for x, h in [(20.5, 9), (26, 14), (31.5, 10)])
    return out

@reg("modelsim", INDIGO_DEEP)
def modelsim():
    bar = rrect(15, 13, 34, 5, 2.5, INDIGO_SOFT)
    m = path("M15 47V26A4 4 0 0 1 22.5 24L32 37L41.5 24A4 4 0 0 1 49 26V47H42V36L34.5 46H29.5L22 36V47Z", INK)
    return bar + m

@reg("modem-manager-gui", DEEP_ORANGE_DEEP)
def modem_manager():
    out = ""
    for a, c in [(-150, ORANGE_SOFT), (-122, INK), (-95, ORANGE_SOFT), (-68, INK), (-40, ORANGE_SOFT)]:
        out += g(path("M32 45C28 38 28 25 32 13C36 25 36 38 32 45Z", c,
                      f' stroke="{HOLE}" stroke-width="1.4"'), f"rotate({a + 90} 32 45)")
    return g(out, "translate(0 1)")

@reg("moderndeck", LIGHT_BLUE_DEEP)
def moderndeck():
    bubble = path("M18 14H46A3 3 0 0 1 49 17V39A3 3 0 0 1 46 42H36L32 47L28 42H18A3 3 0 0 1 15 39V17A3 3 0 0 1 18 14Z", INK)
    code = (stroke("M27 21.5L21.5 28L27 34.5", HOLE, 3.6) + stroke("M37 21.5L42.5 28L37 34.5", HOLE, 3.6) +
            stroke("M35 20.5L29 35.5", HOLE, 3.6))
    return bubble + code

@reg("moe-era", PINK_SOFT)
def moe_era():
    m = stroke("M14.5 38V24L19 31L23.5 24V38", INK, 3.4)
    o = _ring(32, 31, 5.3, GREY_DEEP, 3.6)
    e = stroke("M48 24H41.5V38H48M41.5 31H46.5", BLUE_DARK, 3.4)
    return m + o + e

@reg("mog", BLUE_GREY_DARK)
def mog():
    return _ring(CX, CY, 11.5, INK, 7.5)

@reg("molotov", AMBER)
def molotov():
    mm = stroke("M21.5 24.5C23.5 21.5 25 22.5 24.5 26.5L22 39"
                "M24.5 30C26.5 24 30 21.5 30.5 25L28.5 38"
                "M30.5 29C32.5 23.5 36 21.5 36.5 25L35 35.5C34.8 37.5 36.5 38 38.5 36.5", INK, 3.2)
    under = stroke("M20 44C27 42.5 33 42.5 38 43.5", INK, 2.6) + rrect(40.5, 41, 4, 3.8, 1.2, INK)
    return mm + under

@reg("monero", DEEP_ORANGE)
def monero():
    disc = circle(CX, CY, 16.5, DEEP_ORANGE_DARK)
    top = path("M15.9 35.5A16.5 16.5 0 1 1 48.1 35.5Z", HOLE)
    m = poly([(15.9, 35.5), (20.5, 35.5), (20.5, 20), (32, 31.5), (43.5, 20), (43.5, 35.5), (48.1, 35.5),
              (47.3, 39.5), (39, 39.5), (39, 30.5), (32, 37.5), (25, 30.5), (25, 39.5), (16.7, 39.5)], INK)
    return disc + top + m

@reg("money-manager-ex", ORANGE_DEEP)
def money_manager_ex():
    s = stroke("M42 21.5C40 18.5 36.5 17 32 17C26 17 21.5 19.5 21.5 24C21.5 33 42.5 27 42.5 36"
               "C42.5 40.5 38 43 32 43C27 43 23.5 41.5 21.5 38.5", INK, 5.5)
    return line(32, 11.5, 32, 48.5, ORANGE_SOFT, 2.6) + s

@reg("moneydance", DEEP_ORANGE_LIGHT)
def moneydance():
    out = ""
    for k in range(5):
        y = 42 - 5 * k
        out += ell_f(30, y, 12, 4.3, INK, 0, f' stroke="{HOLE}" stroke-width="1.6"')
    out = "".join(ell_f(38, 33 - 5 * k, 9, 3.4, ORANGE_SOFT, 0, f' stroke="{HOLE}" stroke-width="1.4"')
                  for k in range(3)) + out
    return g(out, "translate(1 0)")

@reg("mongodb-compass", GREY_DEEP)
def mongodb():
    leaf = path("M32 11C38.5 18 42 25 41.5 31.5C41 38.5 36 42.5 33.3 44.5L32.8 49H31.2L30.7 44.5"
                "C28 42.5 23 38.5 22.5 31.5C22 25 25.5 18 32 11Z", INK)
    rib = line(32, 19, 32, 44, HOLE, 2.2)
    return leaf + rib

@reg("mono", BLUE_GREY_DEEP)
def mono():
    box = rrect(15, 14, 34, 32, 4, INK)
    head = path("M18.5 22C24 19.5 31 19 38 20.5C41 21.2 43 22.5 43.5 24.5C40 23.8 36.5 24 34 25.3"
                "C37 27.5 39 31 38 35.5L34.5 33.5C33.5 36.5 31 39 28 40L37 41V43H20.5L27.5 34"
                "C23 31.5 20 27.5 18.5 22Z", HOLE)
    return box + head

@reg("monochroma", GREY_DARK)
def monochroma():
    c = stroke(arc(CX, CY, 13.5, 40, 320), INK, 6)
    return c + circle(CX, CY, 7.5, INK) + circle(CX, CY, 3.3, RED)

@reg("monodevelop", BLUE_GREY_DARK)
def monodevelop():
    white = stroke("M18 45V27A9.5 9.5 0 0 1 37 27C37 31.5 34 34 30.5 34C27.5 34 25.5 32 25.5 29"
                   "C25.5 27 27 25.5 29 25.5", INK, 3.8)
    blue = stroke("M44 15V33A9.5 9.5 0 0 1 25 33C25 28.5 28 26 31.5 26" "C34.5 26 36.5 28 36.5 31"
                  "C36.5 33 35 34.5 33 34.5", BLUE_LIGHT, 3.8)
    return g(white + blue, "translate(0 0)")

@reg("moonlight", BLUE_GREY_DEEP)
def moonlight():
    spokes = "".join(line(*pt(CX, CY, 14, a), *pt(CX, CY, 14, a + 180), INK, 2.8, "butt")
                     for a in (0, 45, 90, 135))
    return _ring(CX, CY, 14.5, INK, 4) + spokes + circle(CX, CY, 3, INK)

@reg("moonlighter", TEAL)
def moonlighter():
    cells = [
        (26, 12, 4, 4), (34, 12, 4, 4), (27, 15, 10, 3),
        (30, 18, 4, 7),
        (16, 21, 4, 12), (44, 21, 4, 12), (19, 29, 6, 4), (39, 29, 6, 4), (13, 25, 4, 4), (47, 25, 4, 4),
        (23, 25, 4, 4), (37, 25, 4, 4),
        (24, 32, 16, 4), (21, 35, 22, 3), (20, 38, 6, 6), (38, 38, 6, 6), (22, 44, 20, 4),
        (29, 25, 6, 7),
    ]
    return "".join(rrect(x, y, w, h, .6, INK) for x, y, w, h in cells)

@reg("morgen", PINK_DARK)
def morgen():
    return (circle(CX, CY, 16.5, PINK_SOFT) +
            path("M15.6 31.5H48.4A16.5 16.5 0 0 1 15.6 31.5Z", DEEP_ORANGE_SOFT) +
            path("M18.5 39.5H45.5A16.5 16.5 0 0 1 18.5 39.5Z", AMBER_SOFT))

@reg("morpheus", BLUE_GREY_DARK)
def morpheus():
    gap = f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"'
    base = rrect(15, 13, 34, 34, 5, INK)
    red = path("M15 18A5 5 0 0 1 20 13H22L27 23L24.5 33L15 35Z", RED, gap)
    blue = path("M28 36L44 31L49 34V42A5 5 0 0 1 44 47H27Z", BLUE_DEEP, gap)
    return base + red + blue + path("M27 23H39L44 31L28 36L24.5 33Z", AMBER, gap)

@reg("mosaic", INDIGO)
def mosaic():
    s = stroke("M42 15H23A7 7 0 0 0 23 29H41A7 7 0 0 1 41 43H22", INK, 4)
    ends = circle(43, 15, 3.6, INK) + circle(21, 43, 3.6, INK)
    world = circle(32, 29, 9.5, HOLE) + globe(32, 29, 7.5, INK, HOLE, 2)
    return s + ends + world

@reg("moserial", GREY_DARK)
def moserial():
    dish = g(path("M13 29A15 15 0 0 0 43 29Z", INK), "rotate(-40 28 29)")
    feed = line(28, 29, 42, 16, INK, 2.6) + circle(42.5, 15.5, 3.2, AMBER_LIGHT)
    stand = poly([(26, 34), (32, 34), (36, 45), (22, 45)], INK, 2) + rrect(16, 44.5, 28, 4.5, 1.5, INK)
    return dish + feed + stand

@reg("motrix", PURPLE_LIGHT)
def motrix():
    box = rrect(16, 15, 32, 31, 6, INK)
    slot = rrect(20, 18.5, 24, 6, 2, PURPLE_DARK)
    dashes = rrect(26, 20.7, 4, 1.6, .8, AMBER_LIGHT) + rrect(34, 20.7, 4, 1.6, .8, AMBER_LIGHT)
    return box + slot + dashes

@small("milkytracker")
def milkytracker_s():
    carton = path("M17 21L21 12H43L47 21V46A3 3 0 0 1 44 49H20A3 3 0 0 1 17 46Z", INK)
    return carton + stroke("M23 42V28L32 37L41 28V42", HOLE, 4.2)

@small("min")
def min_s():
    return _ring(CX, CY, 14, INK, 5) + circle(CX, CY, 10, BLUE_DEEP) + path(arc(CX, CY, 10, -60, 120) + "Z", INDIGO_DEEP)

@small("mindustry")
def mindustry_s():
    return (path("M22 15H29L32 21L35 15H42V45H36V29L32 35L28 29V45H22Z", INK) +
            stroke("M17 24L13 30L17 36M47 24L51 30L47 36", ORANGE_LIGHT, 3))

@small("minetest")
def minetest_s():
    ground = poly([(32, 32), (49, 40), (32, 48), (15, 40)], BLUE_SOFT, 2)
    return ground + rrect(29, 26, 6, 14, 1, BROWN_SOFT) + poly([pt(32, 20, 11, -90 + 60 * k) for k in range(6)], INK, 2)

@small("minigalaxy")
def minigalaxy_s():
    helmet = circle(32, 29, 17, INK) + circle(32, 29, 13.5, HOLE)
    head = path("M21 43V27A11 11 0 0 1 43 27V43Z", YELLOW_SOFT)
    return helmet + head + circle(32, 27, 6.5, INK) + circle(33, 27.5, 3, BROWN_DARK)

@small("mint-dev-settings")
def mint_dev_settings_s():
    return (shrink(_mint(4.2), .78, 27, 25) + badge(43, 41, BLUE_DEEP, 10) +
            gear_h(43, 41, 5.5, INK, BLUE_DEEP))

@small("mintnanny")
def mintnanny_s():
    world = globe(28.5, 26.5, 14, INK, HOLE, 3)
    alert = rrect(41.25, 33.5, 3.5, 8, 1.75, INK) + circle(43, 45.5, 2, INK)
    return world + badge(43, 40.5, RED_DEEP, 10) + alert

@small("mintsources-ppa")
def mintsources_ppa_s():
    out = poly([pt(CX, CY, 17, -90 + 60 * k) for k in range(6)], INK, 2)
    return out + poly([pt(CX, CY, 8, -90 + 60 * k) for k in range(6)], AMBER_LIGHT, 2)

@small("minuet")
def minuet_s():
    cols = [RED_LIGHT, YELLOW_LIGHT, BLUE_LIGHT, BLUE_LIGHT]
    keys = "".join(rrect(14 + 9.2 * k, 14, 8, 32, 2, c) for k, c in enumerate(cols))
    return keys + "".join(rrect(19.6 + 9.2 * k, 12, 5, 17, 1.5, HOLE) for k in (0, 2))

@small("mixcloud")
def mixcloud_s():
    cloud = path("M19 44A10 10 0 0 1 18 24A12 12 0 0 1 41 19A10.5 10.5 0 0 1 46 44Z", INK)
    return g(cloud + stroke(arc(27, 33, 7, -60, 60), HOLE, 4.2), "translate(0 -2)")

@small("mixxx")
def mixxx_s():
    return circle(CX, CY, 17, INK) + circle(CX, CY, 8, HOLE) + circle(CX, CY, 4, INK)

@small("mkusb")
def mkusb_s():
    return (line(18, 44, 42, 20, INK, 4.5) + poly([(47, 15), (36, 17), (45, 26)], INK, 2) +
            circle(18, 44, 5.5, INK) + stroke("M28 34L24 26", INK, 4) + circle(24, 25, 4, INK))

def _mkv_s():
    orbit = ell_f(32, 30, 18, 8, "none", -25, f' stroke="{INK}" stroke-width="3.4"')
    return (orbit + circle(32, 30, 11.5, INK) + circle(39, 19.5, 7, HOLE) + circle(39, 19.5, 5.5, RED))

@small("mkvinfo")
def mkvinfo_s():
    info = circle(43.5, 35, 2, INK) + rrect(41.75, 38.5, 3.5, 8, 1.75, INK)
    return shrink(_mkv_s(), .8, 27.5, 26) + badge(43.5, 40.5, BLUE_DEEP, 10) + info

@small("mkvmergeGUI")
def mkvmerge_s():
    return _mkv_s()

@small("ml.prevete.Daty")
def daty_s():
    bars = [(16, 5, RED_LIGHT), (23.5, 3, RED_LIGHT), (29, 5, BLUE_LIGHT), (36.5, 3, BLUE_LIGHT),
            (42, 5, BLUE_LIGHT)]
    return rrect(13, 15, 38, 30, 3, INK) + "".join(rrect(x, 18.5, w, 23, .5, c) for x, w, c in bars)

@small("mlgui")
def mlgui_s():
    return _ring(CX, CY, 14, INK, 5) + stroke("M14 14H20L32 45L44 14H50", BLUE_LIGHT, 5.5)

@small("mlterm")
def mlterm_s():
    t = stroke("M15 18L24 25.5L15 33", INK, 5) + rrect(26, 29.5, 10, 5, 2.5, INK)
    return t + badge(43, 41, BLUE_DEEP, 10) + globe(43, 41, 7, INK, BLUE_DEEP, 2.4)

@small("mnemosyne")
def mnemosyne_s():
    wing = path("M29 29C31 18 37 11 41 10C45 16 47 21 44 27C48 28 51 33 50 39"
                "C48 46 40 49 35 45C32 42 29 37 29 29Z", INK)
    return wing + line(27, 29, 40, 48, BLUE_GREY_DARK, 3.4) + circle(27, 29, 4, BLUE_GREY_DARK)

@small("modelio")
def modelio_s():
    return (_ring(CX, CY, 15.5, INK, 3) + stroke(arc(CX, CY, 10.5, -55, 55), INK, 5) +
            rrect(19.5, 24, 5, 12, 2.5, INK) + rrect(27, 21, 5, 18, 2.5, INK))

@small("modem-manager-gui")
def modem_manager_s():
    out = ""
    for a, c in [(-140, ORANGE_SOFT), (-90, INK), (-40, ORANGE_SOFT)]:
        out += g(path("M32 46C27 38 27 24 32 11C37 24 37 38 32 46Z", c,
                      f' stroke="{HOLE}" stroke-width="2"'), f"rotate({a + 90} 32 46)")
    return out

@small("moderndeck")
def moderndeck_s():
    bubble = path("M18 13H46A3 3 0 0 1 49 16V40A3 3 0 0 1 46 43H37L32 49L27 43H18A3 3 0 0 1 15 40V16A3 3 0 0 1 18 13Z", INK)
    return bubble + stroke("M26 21L20 28L26 35M38 21L44 28L38 35", HOLE, 4.2)

@small("moe-era")
def moe_era_s():
    return stroke("M18 42V19L32 33L46 19V42", INK, 6)

@small("molotov")
def molotov_s():
    mm = stroke("M21 41L24 24M24 31C26 23 32 21 31 28L29 41M31 31C33 23 39 21 38 28L36.5 41", INK, 5)
    return mm + rrect(40, 40, 5, 5, 1.5, INK)

@small("moneydance")
def moneydance_s():
    return "".join(ell_f(32, 42 - 7 * k, 14, 5, INK, 0, f' stroke="{HOLE}" stroke-width="2.4"') for k in range(4))

@small("mongodb-compass")
def mongodb_s():
    return path("M32 10C39 18 43 25 42.5 32C42 39 36.5 43 34 45L33 50H31L30 45"
                "C27.5 43 22 39 21.5 32C21 25 25 18 32 10Z", INK)

@small("mono")
def mono_s():
    box = rrect(14, 13, 36, 34, 5, INK)
    head = path("M18 21C26 18 35 18 44 22L36 26C39 29 40 33 38 38L28 37L36 44H19L27 34C22 31 19 27 18 21Z", HOLE)
    return box + head

@small("monochroma")
def monochroma_s():
    return stroke(arc(CX, CY, 14, 40, 320), INK, 6) + circle(CX, CY, 7, INK) + circle(CX, CY, 3.5, RED)

@small("monodevelop")
def monodevelop_s():
    white = stroke("M17 46V27A10 10 0 0 1 37 27C37 32 33 34 29.5 34", INK, 4.6)
    blue = stroke("M47 14V33A10 10 0 0 1 27 33C27 28 31 26 34.5 26", BLUE_LIGHT, 4.6)
    return white + blue

@small("moonlight")
def moonlight_s():
    spokes = "".join(line(*pt(CX, CY, 14, a), *pt(CX, CY, 14, a + 180), INK, 3.4, "butt") for a in (0, 60, 120))
    return _ring(CX, CY, 14.5, INK, 5) + spokes

@small("moonlighter")
def moonlighter_s():
    cells = [(26, 11, 12, 6), (29, 17, 6, 9), (14, 21, 6, 13), (44, 21, 6, 13), (18, 29, 28, 6),
             (21, 35, 22, 13)]
    return "".join(rrect(x, y, w, h, 1, INK) for x, y, w, h in cells) + rrect(28, 38, 8, 6, 1, HOLE)

@small("morpheus")
def morpheus_s():
    gap = f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"'
    return (rrect(14, 12, 36, 36, 5, INK) +
            path("M14 17A5 5 0 0 1 19 12H22L27 24L24 36L14 38Z", RED, gap) +
            path("M28 38L45 32L50 35V43A5 5 0 0 1 45 48H27Z", BLUE_DEEP, gap) +
            path("M27 24H40L45 32L28 38L24 36Z", AMBER, gap))

@small("mosaic")
def mosaic_s():
    s = stroke("M44 14H23A7.5 7.5 0 0 0 23 29H41A7.5 7.5 0 0 1 41 44H20", INK, 5)
    return s + circle(32, 29, 10, HOLE) + circle(32, 29, 8, INK)

@small("moserial")
def moserial_s():
    dish = g(path("M12 29A16 16 0 0 0 44 29Z", INK), "rotate(-40 28 29)")
    return dish + rrect(25, 33, 8, 12, 1.5, INK) + rrect(16, 44, 28, 5, 2, INK) + circle(42, 16, 4, AMBER_LIGHT)

@small("motrix")
def motrix_s():
    return rrect(15, 14, 34, 33, 6, INK) + rrect(19, 18, 26, 8, 2.5, PURPLE_DARK)
