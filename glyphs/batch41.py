# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 41: ksudoku to lftp.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import _arc, _gear_d, registry, _ring

ICONS, SMALL, reg, small = registry()

def _jack():
    """Quarter-inch jack plug, drawn pointing right then turned up-right."""
    j = (rrect(13, 26.5, 16, 7, 2.5, INK) + rrect(30.5, 25, 3.5, 10, 1.2, INK) +
         rrect(34, 28, 10, 4, 1, INK) + rrect(45.3, 28.2, 4.7, 3.6, 1.8, INK))
    return g(j, "rotate(-45 32 30)")

@reg("ksudoku", BLUE_DEEP)
def ksudoku():
    out = ""
    for r in range(3):
        for c in range(3):
            col = INK if (r + c) % 2 == 0 else BLUE_LIGHT
            out += rrect(13.25 + c * 13, 11.25 + r * 13, 11.5, 11.5, 2, col)
    two = stroke("M42.4 15.4A2.6 2.4 0 1 1 46.4 17.8L42.2 21.4H47", HOLE, 2.2)
    three = stroke("M29.6 26.4H34.2L31.4 29.4A2.3 2.2 0 1 1 29.4 33", HOLE, 2.2)
    nine = (_ring(18.9, 40.8, 2.2, HOLE, 2.2) + stroke("M21.1 40.8V42.8Q21.1 46 17.6 46.2", HOLE, 2.2))
    return out + two + three + nine

@reg("kteatime", ORANGE_DARK)
def kteatime():
    handle = _ring(44.5, 32, 5, INK, 3.4)
    cup = circle(30.5, 30, 15, INK)
    tea = circle(30.5, 30, 10.5, ORANGE_LIGHT)
    return handle + cup + tea

@reg("ktechlab", BLUE_GREY_DEEP)
def ktechlab():
    pins = "".join(rrect(x, y, 8, 4, 2, INK) for x in (13.5, 42.5) for y in (17, 28, 39))
    chip = rrect(19, 11.5, 26, 37, 4, INK)
    cells = "".join(rrect(23 + c * 9.5, 16 + r * 9.5, 8, 8, 1.8, HOLE)
                    for r in range(3) for c in range(2))
    return pins + chip + cells

@reg("kthememgr", AMBER_DEEP)
def kthememgr():
    top = poly([(32, 12.5), (47, 20.5), (32, 28.5), (17, 20.5)], INK, 2.5)
    left = poly([(17, 20.5), (32, 28.5), (32, 47), (17, 39)], AMBER_SOFT, 2.5)
    right = poly([(47, 20.5), (32, 28.5), (32, 47), (47, 39)], AMBER_DARK, 2.5)
    return top + left + right

@reg("ktikz", INDIGO)
def ktikz():
    sheet = rrect(15, 11, 25, 33, 4, INK)
    badge = circle(40, 38, 11.5, HOLE) + circle(40, 38, 10, INDIGO_DARK)
    pencil = (line(35.5, 42.5, 43, 35, INK, 3.4) +
              poly([(33.3, 44.7), (34, 40.8), (37.2, 44)], INK, 1))
    return sheet + badge + pencil

@reg("ktimer", LIGHT_BLUE_DEEP)
def ktimer():
    button = g(rrect(14, 13, 9, 5, 2, INK), "rotate(-40 18.5 15.5)")
    face = circle(32, 31, 15.5, INK)
    dots = "".join(circle(*pt(32, 31, 10.5, a), 1.8, HOLE) for a in (-90, 0, 90, 180))
    hand = line(32, 31, 37, 23, ORANGE, 3)
    return button + face + dots + hand + circle(32, 31, 2.8, HOLE)

@reg("ktimetracker", BLUE_GREY)
def ktimetracker():
    button = rrect(27, 11, 10, 4, 1.5, INK)
    face = circle(32, 31, 15.5, INK)
    pie = path("M32 31V18.5A12.5 12.5 0 0 1 44.5 31Z", BLUE_LIGHT)
    hand = line(32, 31, 44.5, 31, HOLE, 2.4) + circle(32, 31, 2.4, HOLE)
    return button + face + pie + hand

@reg("ktorrent", BLUE)
def ktorrent():
    column = rrect(27, 11, 10, 25, 5, INK)
    splash = path("M13.5 30C20 31.5 25 34 27 31H37C39 34 44 31.5 50.5 30"
                  "C46 37 40.5 46 32 48C23.5 46 18 37 13.5 30Z", INK)
    drops = "".join(circle(x, y, r, INK) for x, y, r in
                    [(15.5, 24.5, 2), (20.5, 21, 1.6), (48.5, 24.5, 2), (43.5, 21, 1.6)])
    return column + splash + drops

@reg("ktuberling", RED_SOFT)
def ktuberling():
    head = circle(32, 30, 17, INK)
    eyes = circle(24.5, 23.5, 2.4, HOLE) + circle(39.5, 23.5, 2.4, HOLE)
    snout = rrect(25, 26, 14, 9, 4.5, HOLE) + circle(29, 30.5, 1.8, INK) + circle(35, 30.5, 1.8, INK)
    smile = stroke("M24.5 38.5Q32 44.5 39.5 38.5", HOLE, 2.6)
    return head + eyes + snout + smile

@reg("kturtle", BLUE_GREY)
def kturtle():
    limbs = (circle(32, 13.5, 4.5, INK) + stroke("M32 44V48", INK, 3) +
             "".join(g(rrect(-3.5, -5, 7, 10, 3.5, INK), f"translate({x} {y}) rotate({a})")
                     for x, y, a in [(20, 20.5, -45), (44, 20.5, 45), (20, 40, 45), (44, 40, -45)]))
    shell = path("M32 16.5C40.5 16.5 45 22.5 45 30.5C45 38.5 40.5 45 32 45"
                 "C23.5 45 19 38.5 19 30.5C19 22.5 23.5 16.5 32 16.5Z", INK,
                 f' stroke="{HOLE}" stroke-width="2.4"')
    return limbs + shell

@reg("kube", DEEP_ORANGE_DEEP)
def kube():
    bar = rrect(17, 12, 6.5, 36, 2.5, INK)
    chev = stroke("M36.5 20L27.5 31L36.5 42", INK, 5.5) + stroke("M46.5 20L37.5 31L46.5 42", INK, 5.5)
    return bar + chev

@reg("kubeplayer", RED_DEEP)
def kubeplayer():
    screen = rrect(13, 13, 38, 34, 6, INK)
    play = poly([(28, 18.5), (39, 25), (28, 31.5)], HOLE, 2)
    slider = line(19, 40, 45, 40, HOLE, 3) + circle(37, 40, 3.6, HOLE)
    return screen + play + slider

@reg("kubrick", BLUE_GREY_DEEP)
def kubrick():
    cols = [RED, AMBER, AMBER,
            AMBER, BLUE, AMBER,
            BLUE, AMBER, RED]
    return "".join(rrect(13.5 + (k % 3) * 12.8, 11.5 + (k // 3) * 12.8, 11, 11, 2.2, c)
                   for k, c in enumerate(cols))

@reg("kuiviewer", GREY_DEEP)
def kuiviewer():
    big = _gear_d(38.5, 22.5, 8.5, 8, 4.4, 3.8, INK, HOLE, 3.4)
    small = _gear_d(23.5, 38, 7, 8, 3.8, 3.2, INK, HOLE, 2.8)
    return big + small

@reg("kup", GREY_DARK)
def kup():
    x = line(17.5, 15.5, 46.5, 44.5, INK, 4.4) + line(46.5, 15.5, 17.5, 44.5, INK, 4.4)
    return x + _ring(32, 30, 9.5, INK, 4.4)

@reg("kupfer", DEEP_ORANGE_DARK)
def kupfer():
    head = circle(32, 19.5, 8.5, INK) + circle(32, 19.5, 4.5, HOLE)
    cone = path("M24.5 30H39.5L34 47.5H30Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    band = line(24, 34.5, 40, 34.5, HOLE, 2.4, "butt")
    return head + cone + band

@reg("kuro", TEAL_DEEP)
def kuro():
    return line(18, 30.5, 26.5, 39, TEAL_SOFT, 8) + line(26.5, 39, 46, 19.5, INK, 8)

@reg("kvantum", DEEP_PURPLE)
def kvantum():
    k = stroke("M24 16L20 44", INK, 4.4) + stroke("M34 16L21.5 31L28.5 44", INK, 4.4)
    v = stroke("M34 26L37 43L46 26", INK, 4.4)
    return k + v

@reg("kvirc", PURPLE_DEEP)
def kvirc():
    gear = _gear_d(32, 31, 13, 8, 5.5, 4, INK, AMBER, 8)
    v = stroke("M22 15L32 41L42 15", DEEP_ORANGE, 5.2)
    return gear + v

@reg("kwalletmanager", BLUE_DEEP)
def kwalletmanager():
    card = rrect(13, 13, 30, 22, 3, INK)
    photo = rrect(16.5, 16.5, 9.5, 11, 1.5, HOLE)
    person = circle(21.25, 20.5, 2.2, INK) + path("M18 27.5C18 24.5 24.5 24.5 24.5 27.5Z", INK)
    lines = rrect(29, 18, 10, 2.4, 1.2, HOLE) + rrect(29, 23, 7, 2.4, 1.2, HOLE)
    wallet = rrect(26, 29, 25, 19, 3.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    strap = rrect(27, 36, 23, 4, 0, HOLE)
    return card + photo + person + lines + wallet + strap

@reg("kwave", BLUE_DEEP)
def kwave():
    return stroke("M13 30H16.5L18.5 25L20.5 35L22.5 20L24.5 40L26.5 15.5L29 44.5L31 22L33 38"
                  "L35 13.5L37.5 46L39.5 23L41.5 37L43.5 26L45.5 33L47.5 30H51", INK, 2.4)

@reg("kwordquiz", LIGHT_BLUE_DEEP)
def kwordquiz():
    back = rrect(13.5, 18, 20, 30, 3, ORANGE)
    front = rrect(27.5, 11, 23, 32, 3.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    q = stroke("M34.5 21.5A4.8 4.8 0 1 1 41.5 25.5C39.8 26.8 39 27.8 39 30.5", HOLE, 3.6)
    return back + front + q + circle(39, 36.5, 2.3, HOLE)

@reg("kxstitch", GREY_DEEP)
def kxstitch():
    cells = "".join(rrect(x, y, 17, 17, 3, INK) + rrect(x + 5.5, y + 5.5, 6, 6, 1.2, HOLE)
                    for x in (13.5, 33.5) for y in (11.5, 31.5))
    x = line(18, 16, 46, 44, RED_DEEP, 6) + line(46, 16, 18, 44, RED_DEEP, 6)
    return cells + x

@reg("l3afpad", DEEP_PURPLE_SOFT)
def l3afpad():
    leaf = path("M15 47C13 30 23 15 49 11C47 34 37 47 15 47Z", INK)
    lines = (rrect(27, 20, 13, 2.6, 1.3, HOLE) + rrect(23, 26, 16, 2.6, 1.3, HOLE) +
             rrect(21, 32, 11, 2.6, 1.3, HOLE))
    three = stroke("M22.5 37.2H27L24.8 39.6A2 1.9 0 1 1 22.3 42.6", HOLE, 2.2)
    return leaf + lines + three

def _four(colour):
    return stroke("M36.5 44V17L20 36.5H43", colour, 5)

@reg("l4d", INDIGO_LIGHT)
def l4d():
    return circle(32, 30, 16.5, INK) + _four(RED_DEEP) + circle(20, 22, 1.8, RED_DEEP) + circle(45, 40, 1.5, RED_DEEP)

@reg("l4d2", YELLOW_DARK)
def l4d2():
    splat = path("M18 16C24 12 30 17 36 14C43 11 49 16 47 24C45.5 30 50 34 47 41"
                 "C44 47 37 44 31 47C24 50 16 45 17 38C18 32 13 28 14.5 22.5C15 19.5 16 17.5 18 16Z", INK)
    two = stroke("M43 11.5A3 2.8 0 1 1 48 14.5L43.2 18.8H49", INK, 2.6)
    return splat + g(_four(RED_DEEP), "translate(32 31) scale(.85) translate(-31 -30.5)") + two

@reg("laborejo", BLUE_GREY)
def laborejo():
    head = path("M23 13A8 8 0 0 0 26 27V45.5A2.5 2.5 0 0 0 31 45.5V27A8 8 0 0 0 34 13V19.5H23Z", INK)
    arcs = "".join(stroke(f"M35 {y}C43 {y + 3} 43 {y + 8} 35 {y + 11}", INK, 2.8)
                   for y in (13, 22.5, 32))
    return head + arcs

@reg("labplot", BLUE_GREY_DARK)
def labplot():
    axes = line(17, 12, 17, 48, INK, 3) + line(14, 30, 50, 30, INK, 3)
    down = stroke("M17 30C25 30 26 45 32.5 45C39 45 40 30 48 30", BLUE_GREY_SOFT, 3)
    up = stroke("M17 30C25 30 26 15 32.5 15C39 15 40 30 48 30", INK, 3.4)
    ticks = line(32.5, 26.5, 32.5, 33.5, INK, 3) + line(44, 26.5, 44, 33.5, INK, 3)
    return axes + down + up + ticks

@reg("labwc_tweaks", PINK_DEEP)
def labwc_tweaks():
    left = poly([(14, 16), (28, 21), (28, 46), (14, 41)], INK, 2.5)
    right = poly([(50, 16), (36, 21), (36, 46), (50, 41)], INK, 2.5)
    wrench = (path("M26 13A7 7 0 0 0 29.5 25V45A2.5 2.5 0 0 0 34.5 45V25A7 7 0 0 0 38 13V18.5H26Z",
                   AMBER, f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"'))
    return left + right + wrench

@reg("labyrinth", BLUE_GREY_DEEP)
def labyrinth():
    links = (stroke("M19 30C24 30 23 18 29 18", INK, 2.6) + line(19, 30, 29, 30, INK, 2.6) +
             stroke("M19 30C24 30 23 42 29 42", INK, 2.6))
    bars = "".join(rrect(29, y - 3.5, 20, 7, 3.5, INK) for y in (18, 30, 42))
    return links + bars + circle(18.5, 30, 5.5, BLUE_LIGHT)

@reg("ladi-player", INDIGO)
def ladi_player():
    jack = g(_jack(), "translate(29 27) scale(.82) translate(-32 -30)")
    play = poly([(36.5, 34), (49, 41.5), (36.5, 49)], TEAL_LIGHT, 2.5)
    return jack + path("M35 31.5L51.5 41.5L35 51.5Z", HOLE) + play

@reg("ladi-system-log", INDIGO)
def ladi_system_log():
    jack = g(_jack(), "translate(29 27) scale(.82) translate(-32 -30)")
    badge = circle(42, 39, 10.5, HOLE) + circle(42, 39, 9, PINK_LIGHT)
    glass = _ring(41, 38, 3.8, INK, 2.4) + line(43.8, 40.8, 46.5, 43.5, INK, 2.6)
    return jack + badge + glass

@reg("laditools", INDIGO)
def laditools():
    return _jack()

@reg("laigter", DEEP_ORANGE_DEEP)
def laigter():
    flame = path("M31 11C33 18 42 21 45 29C48 38 41 48 32 48C23 48 17 41 18.5 33"
                 "C19.5 28 22.5 25.5 24.5 22.5C25 26 26 28 27.5 29C28 22 29 16 31 11Z", INK)
    core = path("M32.5 30C34.5 34 38.5 36 38.5 40.5C38.5 43.5 36 45.5 32.5 45.5"
                "C29 45.5 26.5 43.5 26.5 40.5C26.5 36 30.5 34 32.5 30Z", AMBER)
    return flame + core

@reg("lampa", BLUE_GREY_DARK)
def lampa():
    outer = cut(cpath(32, 30, 16.5) + cpath(32, 27.8, 12.8), INK)
    mid = cut(cpath(32, 31, 10) + cpath(32, 30, 7), INK)
    return outer + mid + circle(32, 31, 4.2, INK)

@reg("lapce", CYAN_DEEP)
def lapce():
    bar = rrect(16, 12, 6, 36, 2.5, INK)
    tri = stroke("M26.5 14.5V45.5L48.5 30Z", INK, 3.6)
    inner = poly([(30.5, 22.5), (41, 30), (30.5, 37.5)], INK, 1.5)
    return bar + tri + inner

@reg("lara-croft-and-the-temple-of-osiris", AMBER_DARK)
def lara_croft():
    frame = rrect(15, 13, 34, 34, 3, "none", f' stroke="{INK}" stroke-width="3.2"')
    l = stroke("M21.5 20V39.5H30", INK, 3.6)
    c = stroke("M43.5 24A8.5 8.5 0 1 0 43.5 36", INK, 3.6)
    return frame + l + c

@reg("lastfm", RED_DEEP)
def lastfm():
    return stroke("M31 34C28 39.5 16.5 39.5 16.5 30C16.5 20.5 28 20.5 31 26L34 34"
                  "C36 39.5 47 40.5 47.5 34.5C48 29 35 31 35.5 25C36 20.5 44 20 47 24", INK, 4.4)

@reg("latexila", BLUE_DEEP)
def latexila():
    sheet = rrect(15, 11.5, 28, 36, 4, INK)
    sigma = stroke("M27 16.5H20L24 21L20 25.5H27", HOLE, 2.4)
    lines = rrect(20, 31, 12, 2.6, 1.3, HOLE) + rrect(20, 37, 9, 2.6, 1.3, HOLE)
    pencil = (line(47, 16.5, 32.5, 34, BLUE_DARK, 7, "butt") +
              poly([(29.8, 31.8), (35.2, 36.2), (28.5, 38.5)], BLUE_DARK, 1.5))
    return sheet + sigma + lines + g(pencil, "translate(1 0)")

@reg("latte-dock", BROWN_LIGHT)
def latte_dock():
    ell = stroke("M41 16C38 11.5 31 13 31 19.5C31 27 30.5 32 26 35.5C23 37.5 21 35 24 34"
                 "C29 33 35 37 42 34", INK, 3)
    dots = circle(24, 42.5, 2.6, INK) + circle(32, 42.5, 2.6, INK) + circle(40, 42.5, 2.6, INK)
    return ell + dots

@reg("laverna", TEAL)
def laverna():
    note = rrect(14.5, 12.5, 35, 35, 5, INK)
    band = rrect(14.5, 18, 35, 3, 0, HOLE)
    tick = stroke("M23 31H42M23 39H34", HOLE, 4)
    return note + band + tick

@reg("lazarus", INDIGO_LIGHT)
def lazarus():
    pad = path("M32 29C37 29 43 34 43 40C43 44 40 45.5 37 44.5C35 44 33.5 43.5 32 43.5"
               "C30.5 43.5 29 44 27 44.5C24 45.5 21 44 21 40C21 34 27 29 32 29Z", INK)
    toes = "".join(g(path("M0 -5C3 -5 3.5 1 1 5C0 6 -1 6 -1.5 5C-3.5 1 -3 -5 0 -5Z", INK),
                     f"translate({x} {y}) rotate({a})")
                   for x, y, a in [(17, 28, -35), (25, 19, -12), (36, 17, 8), (45, 23, 30)])
    return pad + g(toes, "translate(0 1)")

@reg("lazpaint", BROWN)
def lazpaint():
    palette = cut("M31 13C42 13 50 20 50 28C50 34 45 35 41 34C37 33 35 35 36.5 38.5"
                  "C38 42 35 46 30 46C20 46 14 39 14 29C14 20 21 13 31 13Z" +
                  cpath(26, 38, 3), INK)
    dots = (circle(24, 22.5, 3, BLUE) + circle(34, 20, 3, GREY_DEEP) + circle(43, 26, 3, RED))
    brush = line(46, 30, 27, 44, BROWN_DARK, 3.4) + circle(25.8, 45, 3.2, BROWN_DARK)
    return palette + dots + brush

@reg("lbry", TEAL_DEEP)
def lbry():
    hexa = poly([(13.5, 30), (22.5, 17), (41.5, 17), (50.5, 30), (41.5, 43), (22.5, 43)], INK, 3)
    sheet = stroke("M36 22L21.5 30.5L30 36L43 28", HOLE, 3)
    head = stroke("M38.5 26.5L43 28L41.5 32.5", HOLE, 3)
    return hexa + sheet + head

@reg("ldview", ORANGE_DEEP)
def ldview():
    studs = rrect(17, 14, 12, 8, 2, INK) + rrect(35, 14, 12, 8, 2, INK)
    brick = rrect(13, 20, 38, 27, 3.5, INK, f' stroke="{HOLE}" stroke-width="1.8"')
    return studs + brick

@reg("leocad", RED_DEEP)
def leocad():
    top = poly([(32, 18), (48, 24.5), (32, 31), (16, 24.5)], INK, 2.5)
    left = poly([(16, 24.5), (32, 31), (32, 48), (16, 41.5)], RED_SOFT, 2.5)
    right = poly([(48, 24.5), (32, 31), (32, 48), (48, 41.5)], RED_LIGHT, 2.5)
    stud = (path("M24.5 18.5V24.5A7.5 3.2 0 0 0 39.5 24.5V18.5Z", RED_LIGHT) +
            path("M24.5 18.5a7.5 3.2 0 1 0 15 0a7.5 3.2 0 1 0 -15 0Z", INK,
                 f' stroke="{HOLE}" stroke-width="1.2"'))
    return top + left + right + g(stud, "translate(0 -1)")

@reg("league-of-legends", TEAL_DEEP)
def league_of_legends():
    ring = _ring(34.5, 30.5, 14, INK, 3)
    ell = path("M16 12H27V39H48L44 47H20L22 42V17Z", INK,
               f' stroke="{HOLE}" stroke-width="2.2" stroke-linejoin="round"')
    return ring + ell

@reg("ledger-live-desktop", BLUE_DEEP)
def ledger_live():
    return (_arc(30.5, 31.5, 12.5, 115, 245, INK, 6) + _arc(33.5, 28.5, 12.5, 295, 65, INK, 6))

@reg("leonflix", BLUE_LIGHT)
def leonflix():
    l = stroke("M18.5 16V42H28", INK, 5)
    fl = stroke("M45 18C41 15.5 36 16.5 36 22V43", INK, 5) + line(31, 27.5, 43, 27.5, INK, 4.4)
    return l + fl

@reg("lftp", RED_DEEP)
def lftp():
    top = line(16, 14.5, 45, 14.5, INK, 3) + poly([(44, 10.5), (50, 14.5), (44, 18.5)], INK, 1.5)
    bot = line(48, 45.5, 19, 45.5, INK, 3) + poly([(20, 41.5), (14, 45.5), (20, 49.5)], INK, 1.5)
    word = (stroke("M16.5 38V22H24M16.5 30H22.5", INK, 3.2) +
            stroke("M27.5 22H37.5M32.5 22V38", INK, 3.2) +
            stroke("M41.5 38V22H44.5A4.2 4.2 0 0 1 44.5 30.4H41.5", INK, 3.2))
    return top + bot + word

@small("ksudoku")
def ksudoku_s():
    return "".join(rrect(13.25 + c * 13, 11.25 + r * 13, 11.5, 11.5, 2,
                         INK if (r + c) % 2 == 0 else BLUE_LIGHT)
                   for r in range(3) for c in range(3))

@small("kwave")
def kwave_s():
    return stroke("M13 30H17L20.5 20L25 42L29.5 14L34.5 46L39 20L43 36L46.5 30H51", INK, 3)

@small("lftp")
def lftp_s():
    top = line(15, 20, 43, 20, INK, 5) + poly([(41, 13), (50, 20), (41, 27)], INK, 2)
    bot = line(49, 40, 21, 40, INK, 5) + poly([(23, 33), (14, 40), (23, 47)], INK, 2)
    return top + bot

@small("l3afpad")
def l3afpad_s():
    leaf = path("M15 47C13 30 23 15 49 11C47 34 37 47 15 47Z", INK)
    return leaf + rrect(25, 22, 14, 3.6, 1.8, HOLE) + rrect(21, 30, 14, 3.6, 1.8, HOLE)

@small("ktikz")
def ktikz_s():
    sheet = rrect(14, 11, 26, 34, 4, INK)
    badge = circle(40, 38, 12.5, HOLE) + circle(40, 38, 11, INDIGO_DARK)
    return sheet + badge + line(35, 43, 44, 34, INK, 4.5)

@small("latexila")
def latexila_s():
    sheet = rrect(15, 11.5, 28, 36, 4, INK)
    sigma = stroke("M29 16.5H20L25 22L20 27.5H29", HOLE, 3)
    pencil = line(48, 16.5, 32, 36, PURPLE, 8)
    return sheet + sigma + pencil

@small("kwalletmanager")
def kwalletmanager_s():
    card = rrect(13, 12, 30, 22, 3, INK) + rrect(16.5, 15.5, 10, 12, 1.5, HOLE)
    wallet = rrect(25, 28, 26, 20, 4, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    return card + wallet + rrect(26, 35.5, 24, 5, 0, HOLE)

@small("labyrinth")
def labyrinth_s():
    bars = "".join(rrect(29, y - 4.5, 21, 9, 4.5, INK) for y in (16, 30, 44))
    links = stroke("M19 30L29 16M19 30H29M19 30L29 44", INK, 3.4)
    return links + bars + circle(18.5, 30, 6.5, BLUE_LIGHT)

@small("kvantum")
def kvantum_s():
    return stroke("M26 14L21 46", INK, 5.5) + stroke("M42 14L23.5 31L33 46", INK, 5.5)

@small("lara-croft-and-the-temple-of-osiris")
def lara_croft_s():
    return stroke("M16 16V43H29", INK, 5) + stroke("M48.5 22A11 11 0 1 0 48.5 38", INK, 5)

def _jack_s():
    j = rrect(12, 25.5, 19, 9, 3, INK) + rrect(31, 27.5, 12, 5, 1.5, INK) + circle(47, 30, 3.2, INK)
    return g(j, "rotate(-45 32 30)")

@small("ladi-player")
def ladi_player_s():
    return (g(_jack_s(), "translate(27 26) scale(.85) translate(-32 -30)") +
            path("M33 29L53 41.5L33 54Z", HOLE) + poly([(35, 33), (48, 41.5), (35, 50)], TEAL_LIGHT, 2.5))

@small("ladi-system-log")
def ladi_system_log_s():
    return (g(_jack_s(), "translate(27 26) scale(.85) translate(-32 -30)") +
            circle(42, 39, 12, HOLE) + circle(42, 39, 10.5, PINK_LIGHT))

@small("laditools")
def laditools_s():
    return _jack_s()

@small("ledger-live-desktop")
def ledger_live_s():
    return _arc(30, 32, 13, 125, 235, INK, 7) + _arc(34, 28, 13, 305, 55, INK, 7)
