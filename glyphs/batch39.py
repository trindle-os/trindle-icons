# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 39: keybase to kmplot, mostly KDE apps and games.

Same kit and rules as batch01: palette tile, mark in INK, HOLE for
cut-outs, mostly one colour.
"""
from lm import *
from glyphs.kit import registry, _ring, _star_b

ICONS, SMALL, reg, small = registry()

def _photo(frame_y=14):
    """Kipi photo card: frame, sun, hills."""
    card = rrect(13, frame_y, 32, 26, 4, INK)
    sun = circle(36, frame_y + 8, 3.6, HOLE)
    hills = path(f"M16 {frame_y + 22}L24 {frame_y + 13}L30 {frame_y + 19}L34 {frame_y + 15}"
                 f"L42 {frame_y + 22}Z", HOLE, ' stroke="HOLE" stroke-width="1.5" stroke-linejoin="round"')
    return card + sun + hills

@reg("keybase", BLUE)
def keybase():
    head = circle(32, 32, 14, INK)
    hair = path("M18 31C18 22 24 17 32 17C40 17 46 22 46 31C42 27 38 25 32 24.5"
                "C28 27 23 29 18 31Z", DEEP_ORANGE_LIGHT)
    bun = circle(34, 15, 4.5, DEEP_ORANGE_LIGHT)
    eyes = circle(26.5, 35, 1.9, INDIGO_DARK) + circle(37.5, 35, 1.9, INDIGO_DARK)
    return head + hair + bun + eyes

@reg("keymon", BLUE_GREY_DEEP)
def keymon():
    board = rrect(13, 15, 34, 22, 4, INK)
    keys = "".join(circle(18.5 + 6 * c, 21 + 6 * r, 1.8, HOLE)
                   for r in range(2) for c in range(5))
    bar = rrect(17, 31.5, 14, 2.6, 1.3, HOLE)
    badge = circle(42, 39, 10, HOLE) + circle(42, 39, 8.2, DEEP_ORANGE)
    eye = path("M35.5 39Q42 32.5 48.5 39Q42 45.5 35.5 39Z", INK) + circle(42, 39, 2.4, DEEP_ORANGE)
    return board + keys + bar + badge + eye

@reg("keysmith", TEAL)
def keysmith():
    shackle = stroke("M24 25V19.5A8 8 0 0 1 40 19.5V25", INK, 4)
    body = circle(32, 34, 13.5, INK)
    dial = _ring(32, 34, 8.2, HOLE, 2.4) + circle(32, 34, 3.8, HOLE)
    notch = line(32, 23.5, 32, 25.5, HOLE, 2)
    return shackle + body + dial + notch

@reg("kfloppy", BLUE_GREY_DEEP)
def kfloppy():
    disk = path("M17 13H42L47 18V44A3 3 0 0 1 44 47H20A3 3 0 0 1 17 44Z", INK,
                ' stroke="INK" stroke-width="2" stroke-linejoin="round"')
    shutter = rrect(23, 13, 16, 10, 2, HOLE) + rrect(33, 15, 4, 6, 1, INK)
    label = rrect(21, 30, 22, 14, 2.5, HOLE)
    stripe = rrect(23, 39.5, 18, 2.5, 1.2, ORANGE)
    return disk + shutter + label + stripe

@reg("kfoldersync", BLUE_DEEP)
def kfoldersync():
    folder = path("M14 18A3 3 0 0 1 17 15H26L29.5 18.5H47A3 3 0 0 1 50 21.5V42A3 3 0 0 1 47 45"
                  "H17A3 3 0 0 1 14 42Z", INK)
    arrows = (stroke("M24.5 31A7.5 7.5 0 0 1 37.5 26", HOLE, 3) +
              poly([(35, 22.5), (40.5, 24.5), (36.5, 28.5)], HOLE, 1) +
              stroke("M39.5 33A7.5 7.5 0 0 1 26.5 38", HOLE, 3) +
              poly([(29, 41.5), (23.5, 39.5), (27.5, 35.5)], HOLE, 1))
    return folder + arrows

@reg("kfouleggs", BLUE_DARK)
def kfouleggs():
    a, b = INK, BLUE_SOFT
    blue = (line(24, 16, 40, 16, a, 5) + line(40, 16, 40, 30, a, 5) +
            circle(24, 16, 5.5, a) + circle(40, 16, 5.5, a) + circle(40, 30, 5.5, a))
    green = (line(24, 30, 24, 44, b, 5) + line(24, 44, 40, 44, b, 5) +
             circle(24, 30, 5.5, b) + circle(24, 44, 5.5, b) + circle(40, 44, 5.5, b))
    return blue + green

@reg("kfourinline", BLUE_DEEP)
def kfourinline():
    return (circle(24, 22, 7, INK) + circle(40, 22, 7, RED_LIGHT) +
            circle(24, 38, 7, INDIGO_DARK) + circle(40, 38, 7, RED_LIGHT))

@reg("kgeography", BLUE)
def kgeography():
    globe = circle(32, 30, 16, INK)
    land = (path("M20 19C23 16 28 15 30 17C31 20 27 21 27 24C27 27 30 28 29 32"
                 "C28 36 25 38 24 42C21 39 18 34 18 29C18 25 18.5 21.5 20 19Z", HOLE) +
            path("M36 16C40 17 44 20 46 24C45 27 42 26 40 28C41 32 44 34 42 38"
                 "C40 41 37 42 36 39C36 35 33 33 34 29C35 26 33 23 34 20Z", HOLE))
    return globe + land

@reg("kget", BLUE)
def kget():
    return (stroke("M32 13V36M23 27.5L32 36.5L41 27.5", INK, 5) +
            line(20, 45, 44, 45, INK, 4.5))

@reg("kghostview", BLUE_DEEP)
def kghostview():
    sheet = path("M20 11H37L46 20V46A3 3 0 0 1 43 49H20A3 3 0 0 1 17 46V14A3 3 0 0 1 20 11Z", INK)
    fold = path("M37 11V17A3 3 0 0 0 40 20H46Z", BLUE_SOFT)
    lens = _ring(30, 30, 6.5, HOLE, 3.4) + line(35, 35, 40, 40.5, HOLE, 4)
    return sheet + fold + lens

@reg("kgoldrunner", BLUE_DEEP)
def kgoldrunner():
    rails = line(19, 17, 19, 41, INK, 3) + line(28, 17, 28, 41, INK, 3)
    rungs = "".join(line(19, y, 28, y, INK, 2.6) for y in (22, 29, 36))
    bricks = "".join(rrect(13 + 9.75 * k, 42, 8.75, 6, 1.5, INK) for k in range(4))
    gold = _star_b(41, 23, 7, AMBER)
    return rails + rungs + bricks + gold

@reg("kgraphviewer", BLUE_GREY)
def kgraphviewer():
    top = rrect(24, 13, 16, 9, 2.5, INK)
    left = rrect(13, 38, 16, 9, 2.5, INK)
    right = rrect(35, 38, 16, 9, 2.5, INK)
    edges = (stroke("M29 22L22.5 33", INK, 3) + poly([(19.5, 32), (25.5, 33.5), (21, 37.5)], INK, 1.5) +
             stroke("M35 22L41.5 33", INK, 3) + poly([(44.5, 32), (38.5, 33.5), (43, 37.5)], INK, 1.5))
    return top + edges + left + right

@reg("khangman", DEEP_PURPLE)
def khangman():
    coils = "".join(rrect(26.5, 12 + 5 * k, 11, 4, 2, INK) for k in range(3))
    rope = line(32, 26, 32, 29, INK, 3)
    loop = stroke("M32 28C24 35 24 45 32 45C40 45 40 35 32 28Z", INK, 3.4)
    return coils + rope + loop

@reg("khotkeys", RED_DEEP)
def khotkeys():
    key = rrect(14, 12, 36, 36, 8, INK)
    h = stroke("M25 20V40M39 20V40M25 30H39", HOLE, 5)
    return key + h

@reg("kicad", INDIGO)
def kicad():
    k = stroke("M19 15V45M35 15L21.5 30L35.5 45", INK, 5.8)
    i = line(43.5, 28, 43.5, 45, INK, 5.8) + circle(43.5, 18.5, 3.4, INK)
    return k + i

@reg("kid3", PURPLE_DEEP)
def kid3():
    note = (stroke("M26 38V17L44 13V34", INK, 3.8) +
            f'<ellipse cx="21.5" cy="38.5" rx="5.5" ry="4.5" fill="{INK}"/>' +
            f'<ellipse cx="39.5" cy="34.5" rx="5.5" ry="4.5" fill="{INK}"/>')
    tag = g(path("M26 37H45L50 42L45 47H26Z", AMBER_SOFT,
                 ' stroke="#FFD65D" stroke-width="2" stroke-linejoin="round"') +
            circle(45.3, 42, 1.6, PURPLE_DEEP), "rotate(-14 38 42)")
    return note + tag

@reg("kig", ORANGE_DEEP)
def kig():
    return (_ring(26, 24, 10.5, INK, 3.4) +
            rrect(27.5, 25.5, 20, 20, 1.5, "none", f' stroke="{INK}" stroke-width="3.4"'))

@reg("kigo", ORANGE_DEEP)
def kigo():
    return (circle(32, 19, 6.5, BLUE_GREY_DARK) + circle(18.5, 38, 6.5, INK) +
            circle(32, 38, 6.5, INK) + circle(45.5, 38, 6.5, INK))

@reg("kiki-the-nano-bot", INDIGO_DARK)
def kiki():
    left = f'<ellipse cx="25" cy="30" rx="9.5" ry="16" fill="none" stroke="{INK}" stroke-width="4"/>'
    right = f'<ellipse cx="39" cy="30" rx="9.5" ry="16" fill="none" stroke="{INK}" stroke-width="4"/>'
    eye = path("M27 18C31 22 32 26 32 30C32 34 31 38 27 42C23 38 22 34 22 30C22 26 23 22 27 18Z", DEEP_ORANGE)
    point = poly([(34, 21), (47, 30), (34, 39)], DEEP_ORANGE, 2)
    return right + point + left + eye

@reg("kile", LIGHT_BLUE_DEEP)
def kile():
    k = stroke("M16 16V44M29 16L18 30L29.5 44", INK, 5.5)
    bars = "".join(rrect(33, y, 16, 4.6, 1.5, INK) for y in (17, 25, 33, 40.4))
    cuts = line(41, 16, 41, 45, HOLE, 2)
    return k + bars + cuts

@reg("killbots", BROWN)
def killbots():
    panels = (rrect(13, 11, 22, 22, 3, BROWN_SOFT) + rrect(38, 11, 13, 22, 3, BROWN_SOFT) +
              rrect(13, 36, 22, 13, 3, BROWN_SOFT) + rrect(38, 36, 13, 13, 3, BROWN_SOFT))
    return panels + circle(44.5, 42.5, 4.2, INK)

@reg("killing-floor", DEEP_ORANGE_DEEP)
def killing_floor():
    out = ""
    for k in range(3):
        a = -90 + 120 * k
        c1 = pt(32, 31, 7, a)
        c2 = pt(32, 31, 10.5, a)
        out += cut(cpath(c1[0], c1[1], 9) + cpath(c2[0], c2[1], 6.3), INK)
    ring = _ring(32, 31, 9.5, INK, 2.4)
    gaps = "".join(line(*pt(32, 31, 3, 30 + 120 * k), *pt(32, 31, 12.5, 30 + 120 * k), HOLE, 1.8)
                   for k in range(3))
    return out + ring + gaps + circle(32, 31, 3.2, HOLE)

@reg("kimagemapeditor", BLUE_DARK)
def kimagemapeditor():
    globe = circle(32, 30, 16, INK)
    tags = stroke("M24 23L17.5 30L24 37M40 23L46.5 30L40 37", HOLE, 3.6)
    pin = path("M32 20.5A5.5 5.5 0 0 1 37.5 26C37.5 30 32 36 32 36C32 36 26.5 30 26.5 26"
               "A5.5 5.5 0 0 1 32 20.5Z", HOLE) + circle(32, 26, 2, INK)
    return globe + tags + pin

@reg("kindd", LIGHT_BLUE)
def kindd():
    bird = path("M13 27C18 25 22 27 25 31C25 24 22 18 17 14C26 15 33 21 35 29"
                "C37 26 40 23 44 23C47 23 49 24.5 50 26.5L46 27.5C45.5 33 42 38 36 41"
                "C31 43.5 25 43 21 40L15 42.5L18 37C15.5 34 14 31 13 27Z", INK)
    return bird + circle(44.5, 26.5, 1.3, HOLE)

@reg("king-phisher-icon", BLUE_GREY_DARK)
def king_phisher():
    blade = path("M13 19C24 12 38 14 50 36C41 25 30 20.5 21 22C18 21 15 20 13 19Z", INK)
    eye = circle(28, 33, 10, INK) + circle(28, 33, 6.5, ORANGE) + circle(28, 33, 3.4, BLUE_GREY_DARK)
    glint = circle(25.5, 30.5, 1.6, INK)
    return blade + eye + glint

@reg("kipi-dngconverter", RED_LIGHT)
def kipi_dng():
    badge = circle(42, 40, 10, HOLE) + circle(42, 40, 8.3, ORANGE_DARK)
    arrow = (stroke("M46.3 38.5A4.6 4.6 0 1 0 45 43.5", INK, 2.6) +
             poly([(44.2, 34.3), (48.6, 35.8), (46.8, 40)], INK, 1))
    return _photo() + badge + arrow

@reg("kipi-expoblending", RED_LIGHT)
def kipi_expo():
    badge = circle(42, 40, 10, HOLE) + circle(42, 40, 8.3, DEEP_PURPLE)
    arrow = line(42, 35, 42, 42, INK, 2.8) + poly([(37.5, 40.5), (46.5, 40.5), (42, 45.5)], INK, 1.2)
    return _photo() + badge + arrow

@reg("kipi-logo", ORANGE_DEEP)
def kipi_logo():
    pal = path("M31 13C42 13 50 20 50 29C50 35 45 37 41 36C38 35.5 36 37 37 40"
               "C38 44 35 47 31 47C21 47 14 40 14 30C14 20 21 13 31 13Z", INK)
    thumb = circle(30, 40, 3.2, HOLE)
    dots = (circle(24, 22, 3.3, BLUE_DEEP) + circle(33, 19.5, 3.3, ORANGE_DARK) +
            circle(41.5, 24, 3.3, RED_DEEP) + circle(21, 31.5, 3.3, ORANGE))
    return pal + thumb + dots

@reg("kipi-panorama", INDIGO_LIGHT)
def kipi_panorama():
    frame = rrect(12, 18, 40, 24, 3.5, INK)
    sun = circle(41, 26, 4, HOLE)
    hills = path("M15 36L22 31L27 33.5L33 30L40 33L49 32V36Z", HOLE)
    water = rrect(15, 37.5, 34, 2.4, 1.2, HOLE)
    return frame + sun + hills + water

@reg("kiriki", RED_DEEP)
def kiriki():
    return circle(21, 19, 5.6, INK) + circle(32, 30, 5.6, RED_SOFT) + circle(43, 41, 5.6, INK)

@reg("kitematic", LIGHT_BLUE_LIGHT)
def kitematic():
    block = rrect(14, 16, 36, 28, 7, INK)
    k = (line(25, 16, 25, 44, HOLE, 3) +
         poly([(28, 30), (37, 20), (37, 40)], HOLE, 2) +
         line(40.5, 16, 40.5, 44, HOLE, 3))
    return block + k

@reg("kiten", GREY_SOFT)
def kiten():
    return circle(32, 30, 14, RED)

@reg("kitty", DEEP_ORANGE_DEEP)
def kitty():
    ears = (poly([(15, 22), (17, 11), (26, 17)], INK, 3) +
            poly([(49, 22), (47, 11), (38, 17)], INK, 3))
    screen = rrect(13, 17, 38, 30, 6, INK)
    prompt = stroke("M21 26L27.5 31L21 36", HOLE, 3.6) + line(31, 38, 41, 38, HOLE, 3.6)
    return ears + screen + prompt

@reg("kiwix-desktop", GREY_DARK)
def kiwix():
    body = f'<ellipse cx="30" cy="31" rx="13" ry="10.5" fill="{INK}"/>'
    head = circle(40.5, 22.5, 5.5, INK)
    beak = stroke("M44.5 25L50 36", INK, 2.4)
    legs = stroke("M26 40V47M24 47H28.5M33 40.5V47M31 47H35.5", INK, 2.4)
    eye = circle(41.5, 21.5, 1.3, HOLE)
    return body + head + beak + legs + eye

@reg("kjots", AMBER_DEEP)
def kjots():
    book = rrect(16, 12, 30, 37, 4, INK)
    spine = line(22, 12, 22, 49, HOLE, 2.4)
    pencil = (line(29, 39, 43, 21, HOLE, 5) + poly([(26.5, 42.5), (28, 36.5), (31.5, 39.5)], HOLE, 1))
    return book + spine + pencil

@reg("kjumpingcube", GREY_DEEP)
def kjumpingcube():
    return "".join(circle(x, y, 4.6, INK) for x, y in
                   [(20, 18), (44, 18), (32, 30), (20, 42), (44, 42)])

@reg("klatexformula", GREY_DARK)
def klatexformula():
    ff = stroke("M42 16C40 12.5 36 12.5 34.5 15.5C33 18.5 32 28 30.5 37C29.5 43 27.5 47.5 22 46", INK, 3.6)
    bar = line(25, 25.5, 40, 25.5, INK, 3.2)
    return ff + bar

@reg("klavaro", BLUE_GREY_DEEP)
def klavaro():
    board = rrect(13, 29, 38, 19, 3.5, INK)
    keys = "".join(circle(18.5 + 5.4 * c, 34.5, 1.7, HOLE) for c in range(6))
    space = rrect(21, 40, 22, 3, 1.5, HOLE)
    cap = path("M23 11H41A3 3 0 0 1 44 14V27L32 33L20 27V14A3 3 0 0 1 23 11Z", GREY_DEEP)
    k = stroke("M28 16V27M36 16L29.5 21.5L36.5 27", INK, 3)
    return board + keys + space + cap + k

@reg("klayout", ORANGE_DEEP)
def klayout():
    k = stroke("M19 14V46M34 14L21 30L35 46", INK, 6)
    l = stroke("M41 30L38.5 45H47", INK, 3.4)
    return k + l

@reg("kleopatra", AMBER_DARK)
def kleopatra():
    brow = stroke("M16 20C24 16 38 16 49 20", INK, 3.2)
    eye = stroke("M15 29C22 23 34 22.5 45 29H49C38 36 26 37 15 29", INK, 3.2)
    pupil = circle(31, 29, 5, INK)
    tear = stroke("M29 35V45M36 35C39 40 41 44 45.5 44C48 44 49 41.5 47 40.5", INK, 3)
    return brow + eye + pupil + tear

@reg("klickety", BLUE_GREY_DARK)
def klickety():
    return (rrect(14, 12, 17, 17, 3, RED) + rrect(33, 12, 17, 17, 3, BLUE_DEEP) +
            rrect(14, 31, 17, 17, 3, ORANGE) + rrect(33, 31, 17, 17, 3, ORANGE_DEEP))

@reg("klines", BLUE_DEEP)
def klines():
    cols = ["INK", "INK", AMBER_SOFT, AMBER_SOFT, "INK", "INK", "INK", AMBER_SOFT, "INK",
            AMBER_SOFT, "INK", "INK"]
    return "".join(circle(21 + 11 * (k % 3), 14.5 + 10.5 * (k // 3), 4.3, cols[k])
                   for k in range(12))

@reg("klystrack", GREY_DARK)
def klystrack():
    gauge = path("M17 29A15 15 0 0 1 47 29Z", AMBER)
    needle = line(32, 29, 40, 18.5, RED, 2.6)
    keys = rrect(14, 32, 36, 16, 3, INK)
    blacks = "".join(rrect(18 + 6 * k, 32, 3, 9, 1, HOLE) for k in range(5))
    return gauge + needle + keys + blacks

@reg("kmahjongg", RED_DEEP)
def kmahjongg():
    box = rrect(19, 19, 26, 14, 3, "none", f' stroke="{INK}" stroke-width="3.6"')
    stem = stroke("M32 11V48", INK, 3.8)
    return box + stem + line(28, 12.5, 36, 14, INK, 3)

@reg("kmenuedit", BLUE_GREY)
def kmenuedit():
    panel = path("M17 12H47A3 3 0 0 1 50 15V41A3 3 0 0 1 47 44H36L32 49L28 44H17"
                 "A3 3 0 0 1 14 41V15A3 3 0 0 1 17 12Z", INK)
    hi = rrect(14, 23.5, 36, 9, 0, CYAN)
    rows = "".join(rrect(19, y - 1.8, 4, 3.6, 1.2, c) + rrect(26, y - 1.8, 19, 3.6, 1.8, c)
                   for y, c in [(18, HOLE), (28, INK), (38, HOLE)])
    return panel + hi + rows

@reg("kmines", BLUE_GREY_DEEP)
def kmines():
    spikes = "".join(g(rrect(28.5, 11, 7, 10, 3, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    return spikes + circle(32, 30, 12.5, INK) + circle(27.5, 25.5, 2.6, HOLE)

@reg("kmix", GREY_DARK)
def kmix():
    return (circle(32, 30, 17, INK) + circle(32, 30, 12, HOLE) +
            circle(32, 30, 9.5, AMBER) + circle(32, 30, 4.5, HOLE))

@reg("kmouth", RED)
def kmouth():
    eyes = (f'<ellipse cx="24.5" cy="21" rx="3.3" ry="4.3" fill="{INK}"/>'
            f'<ellipse cx="39.5" cy="21" rx="3.3" ry="4.3" fill="{INK}"/>')
    mouth = path("M16 30H48C48 40 41 47 32 47C23 47 16 40 16 30Z", INK)
    tongue = path("M24 42.5C26 38.5 38 38.5 40 42.5C37.5 44.5 35 45.5 32 45.5C29 45.5 26.5 44.5 24 42.5Z",
                  RED_SOFT)
    return eyes + mouth + tongue

@reg("kmplayer", INDIGO_DARK)
def kmplayer():
    strip = rrect(19, 11, 26, 38, 3, INK)
    holes = "".join(rrect(x, 14.5 + 6.5 * k, 3, 3.5, .8, HOLE) for k in range(5) for x in (21.5, 39.5))
    frame = rrect(27, 14, 10, 32, 1.5, HOLE)
    return strip + holes + frame + _star_b(32, 30.5, 7.2, PINK_LIGHT, 1.4)

@reg("kmplot", BLUE_GREY)
def kmplot():
    axes = stroke("M16 13V47M14 30H50", INK, 2.6)
    curve = stroke("M17 44C24 44 26 16 32 16C38 16 40 44 47 44", INK, 3.8)
    dash = stroke("M18 22H46", RED_SOFT, 2.4, ' stroke-dasharray="4 3"')
    return axes + dash + curve

@small("keymon")
def keymon_s():
    board = rrect(13, 15, 34, 22, 4, INK)
    keys = "".join(circle(20 + 9 * c, 22, 2.6, HOLE) for c in range(3))
    badge = circle(42, 39, 11, HOLE) + circle(42, 39, 9.2, DEEP_ORANGE)
    return board + keys + badge + circle(42, 39, 4, INK)

@small("kgoldrunner")
def kgoldrunner_s():
    ladder = stroke("M19 15V41M29 15V41M19 24H29M19 33H29", INK, 3.6)
    floor = rrect(13, 42, 38, 6.5, 2, INK)
    return ladder + floor + _star_b(41, 23, 8, AMBER)

@small("kid3")
def kid3_s():
    note = (stroke("M26 36V17L44 13V32", INK, 4.4) +
            circle(21.5, 36.5, 5.5, INK) + circle(39.5, 32.5, 5.5, INK))
    return note

@small("killing-floor")
def killing_floor_s():
    out = ""
    for k in range(3):
        a = -90 + 120 * k
        c1 = pt(32, 31, 7.5, a)
        c2 = pt(32, 31, 11.5, a)
        out += cut(cpath(c1[0], c1[1], 9.5) + cpath(c2[0], c2[1], 6), INK)
    return out + circle(32, 31, 3.5, HOLE)

@small("kipi-dngconverter")
def kipi_dng_s():
    return (rrect(13, 14, 30, 26, 4, INK) + circle(34, 22, 4, HOLE) +
            circle(42, 40, 11, HOLE) + circle(42, 40, 9.3, DEEP_PURPLE_LIGHT))

@small("kipi-expoblending")
def kipi_expo_s():
    return (rrect(13, 14, 30, 26, 4, INK) + circle(34, 22, 4, HOLE) +
            circle(42, 40, 11, HOLE) + circle(42, 40, 9.3, DEEP_PURPLE))

@small("klines")
def klines_s():
    cols = ["INK", AMBER_SOFT, AMBER_SOFT, "INK"]
    return "".join(circle(24 + 16 * (k % 2), 22 + 16 * (k // 2), 7, cols[k]) for k in range(4))

@small("kmplayer")
def kmplayer_s():
    strip = rrect(18, 11, 28, 38, 3, INK)
    frame = rrect(24, 15, 16, 30, 2, HOLE)
    return strip + frame + _star_b(32, 30, 8, PINK_LIGHT, 1.6)

@small("klavaro")
def klavaro_s():
    board = rrect(13, 30, 38, 18, 3.5, INK)
    cap = path("M22 10H42A3 3 0 0 1 45 13V27L32 34L19 27V13A3 3 0 0 1 22 10Z", DEEP_PURPLE_LIGHT)
    k = stroke("M28 15V28M37 15L29.5 21.5L37.5 28", INK, 3.6)
    return board + cap + k

@small("kmenuedit")
def kmenuedit_s():
    panel = path("M17 12H47A3 3 0 0 1 50 15V41A3 3 0 0 1 47 44H36L32 49L28 44H17"
                 "A3 3 0 0 1 14 41V15A3 3 0 0 1 17 12Z", INK)
    hi = rrect(14, 22, 36, 12, 0, CYAN)
    rows = rrect(19, 16, 26, 3.6, 1.8, HOLE) + rrect(19, 26.2, 26, 3.6, 1.8, INK) + rrect(19, 37, 26, 3.6, 1.8, HOLE)
    return panel + hi + rows

@small("keysmith")
def keysmith_s():
    shackle = stroke("M24 25V19.5A8 8 0 0 1 40 19.5V25", INK, 4.4)
    return shackle + circle(32, 34, 14, INK) + circle(32, 34, 5.5, HOLE)

@small("kfoldersync")
def kfoldersync_s():
    folder = path("M14 18A3 3 0 0 1 17 15H26L29.5 18.5H47A3 3 0 0 1 50 21.5V42A3 3 0 0 1 47 45"
                  "H17A3 3 0 0 1 14 42Z", INK)
    arc = stroke("M25 35A7.5 7.5 0 1 1 32 39.5", HOLE, 3.4)
    return folder + arc + poly([(21.5, 31.5), (29, 33), (24.5, 39)], HOLE, 1)

@small("kgeography")
def kgeography_s():
    land = path("M22 18C27 15 31 17 30 22C29 26 25 27 27 32C29 37 26 41 23 42"
                "C19 38 17 33 17 29C17 24 19 20 22 18Z", HOLE)
    return circle(32, 30, 16, INK) + land + circle(40, 28, 4.5, HOLE)

@small("kile")
def kile_s():
    k = stroke("M17 16V44M30 16L19 30L30.5 44", INK, 6)
    return k + "".join(rrect(34, y, 14, 6, 2, INK) for y in (16, 27, 38))

@small("kimagemapeditor")
def kimagemapeditor_s():
    return circle(32, 30, 16, INK) + stroke("M26 21L18.5 30L26 39M38 21L45.5 30L38 39", HOLE, 4.4)

@small("kleopatra")
def kleopatra_s():
    eye = stroke("M14 29C22 22 36 22 48 29C36 36 22 36 14 29Z", INK, 3.6)
    return eye + circle(31, 29, 5, INK) + stroke("M29 35V45", INK, 3.6)

@small("kmplot")
def kmplot_s():
    axes = stroke("M16 13V47M14 30H50", INK, 3)
    return axes + stroke("M17 44C24 44 26 16 32 16C38 16 40 44 47 44", INK, 4.4)
