# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 65: spideroak to subsurface-icon."""
import math
from lm import *
from glyphs.kit import _gear, registry, _star_d

ICONS, SMALL, reg, small = registry()

def _cloud(fill):
    return (circle(25, 31, 7, fill) + circle(34, 26, 9.5, fill) + circle(42, 32, 6, fill)
            + rrect(15, 30, 34, 13, 6.5, fill))

def _db(cx, top, bot, rx, ry, seps):
    body = path(f"M{f(cx - rx)} {f(top)}A{f(rx)} {f(ry)} 0 0 1 {f(cx + rx)} {f(top)}"
                f"V{f(bot)}A{f(rx)} {f(ry)} 0 0 1 {f(cx - rx)} {f(bot)}Z", INK)
    lines = "".join(stroke(f"M{f(cx - rx)} {f(y)}A{f(rx)} {f(ry)} 0 0 0 {f(cx + rx)} {f(y)}", HOLE, 2.2)
                    for y in [top] + seps)
    return body + lines

def _sr(w=4.2):
    s = stroke("M28.5 18.5C26.5 16.5 24.5 16 22.5 16C19.5 16 17.5 18 17.5 21"
               "C17.5 27 28.5 26 28.5 34C28.5 38 26 40.5 22.5 40.5C20 40.5 18 39.5 16.5 37.5", INK, w)
    r = stroke("M35 42V16H40.5C44.5 16 46.5 18.5 46.5 22.5C46.5 26.5 44 29 40.5 29H35"
               "M40.5 29L47 42", INK, w)
    return s + r

def _crescent(ox, oy, r1, ix, iy, r2, fill):
    d = math.hypot(ix - ox, iy - oy)
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(r1 * r1 - a * a)
    ux, uy = (ix - ox) / d, (iy - oy) / d
    mx, my = ox + a * ux, oy + a * uy
    p1 = (mx - h * uy, my + h * ux)
    p2 = (mx + h * uy, my - h * ux)
    dd = (f"M{f(p1[0])} {f(p1[1])}A{f(r1)} {f(r1)} 0 1 0 {f(p2[0])} {f(p2[1])}"
          f"A{f(r2)} {f(r2)} 0 1 1 {f(p1[0])} {f(p1[1])}Z")
    return path(dd, fill)

@reg("spideroak", DEEP_ORANGE_LIGHT)
def spideroak():
    arrow = line(32, 40, 32, 28.5, HOLE, 3.4) + stroke("M27 32.5L32 27.5L37 32.5", HOLE, 3.4)
    return g(_cloud(INK) + arrow, "translate(0 -2)")

@reg("sportstracker", BLUE_DARK)
def sportstracker():
    head = circle(38.5, 15, 3.8, INK)
    body = stroke("M36 22L30.5 32", INK, 4.6)
    arms = stroke("M24 25L29 21.5H36L40 27.5L45 25", INK, 3.6)
    legs = (stroke("M30.5 32L37.5 36L36.5 44", INK, 3.8) +
            stroke("M30.5 32L26.5 39.5H18.5", INK, 3.8))
    return head + body + arms + legs

@reg("spotify-qt", CYAN_DEEP)
def spotify_qt():
    qt = poly([(22, 14), (48, 14), (48, 38), (42, 46), (16, 46), (16, 22)], INK, 3)
    bars = (stroke("M21 25C28 22.5 36 23 43 26.5", HOLE, 3.4) +
            stroke("M22.5 31C28.5 29.3 34.5 29.7 40.5 32.8", HOLE, 3) +
            stroke("M24 36.5C29 35.3 33.5 35.7 38 38", HOLE, 2.6))
    return qt + bars

@reg("spring-tool-suite", DEEP_PURPLE_SOFT)
def spring_tool_suite():
    gear = _gear(32, 30, 17, 13.5, 12, INK)
    leaf = path("M24.5 38C23.5 29 29 21.5 41 20.5C41.5 32 34.5 38.5 24.5 38Z", HOLE)
    vein = stroke("M25.5 37C29 32 33 28.5 37 25.5", INK, 2.2)
    return gear + circle(32, 30, 14, INK) + leaf + vein

@reg("spyder", RED_DEEP)
def spyder():
    web = (stroke("M16 13V36M16 13H40M16 13L30 27", INK, 2.4) +
           stroke("M16 24.5C20 24 23 22.5 23 19.5C24.5 17.5 26 15.5 27.5 13", INK, 2.4) +
           stroke("M16 34C22.5 33.5 27 31 29 26C33 24 35.5 18.5 37 13", INK, 2.4))
    s = stroke("M46 28.5C44.8 27 43 26.3 40.8 26.3C37.8 26.3 35.8 28 35.8 30.5"
               "C35.8 35.5 46.5 34 46.5 40C46.5 43 44 45 40.5 45C38 45 36 44 34.8 42.3", INK, 4.4)
    return web + s

@reg("sqldeveloper", BLUE_GREY)
def sqldeveloper():
    db = _db(28, 18, 41, 13, 4.5, [26.5, 34])
    badge = (f'<circle cx="41.5" cy="39.5" r="9" fill="#7D94A0" stroke="{HOLE}" stroke-width="2.4"/>'
             + poly([(39, 35), (46, 39.5), (39, 44)], INK, 1.5))
    return db + badge

@reg("sqlitebrowser", GREY_DARK)
def sqlitebrowser():
    return _db(32, 18, 42, 15, 5, [26.5, 34.5])

@reg("squeak", GREY_DEEP)
def squeak():
    ears = (poly([(19, 27), (19, 11.5), (29, 20)], INK, 3) +
            poly([(45, 27), (45, 11.5), (35, 20)], INK, 3))
    inner = (poly([(21.5, 22), (21.5, 16.5), (25, 19.5)], HOLE, 1.5) +
             poly([(42.5, 22), (42.5, 16.5), (39, 19.5)], HOLE, 1.5))
    head = path("M32 19C40 19 45.5 25 45.5 31.5C45.5 38.5 39.5 44 32 44C24.5 44 18.5 38.5 18.5 31.5"
                "C18.5 25 24 19 32 19Z", INK)
    face = circle(26.5, 30.5, 2.4, HOLE) + circle(37.5, 30.5, 2.4, HOLE) + circle(32, 36, 2, HOLE)
    whisk = (stroke("M13 32.5L18.8 34M13.5 39L19.5 37", INK, 2.2) +
             stroke("M51 32.5L45.2 34M50.5 39L44.5 37", INK, 2.2))
    return ears + inner + head + face + whisk

@reg("sr-editor", GREY_DARK)
def sr_editor():
    badge = (f'<circle cx="43" cy="40" r="8.5" fill="#7D94A0" stroke="{HOLE}" stroke-width="2.4"/>'
             + _gear(43, 40, 5.4, 4, 8, INK) + circle(43, 40, 1.8, BLUE_GREY_LIGHT))
    return g(_sr(4.2), "translate(32 29) scale(.92) translate(-32 -29)") + badge

@reg("ssdeep", TEAL_DEEP)
def ssdeep():
    ring = f'<circle cx="28" cy="26" r="9.5" fill="none" stroke="{INK}" stroke-width="5"/>'
    return ring + line(35.5, 33.5, 45.5, 43.5, INK, 6.5)

@reg("st", GREY_DARK)
def st():
    return stroke("M16 38H22.5V22H47.5V38M35 22V38", INK, 5.2)

@reg("stacer", BLUE_GREY_DARK)
def stacer():
    dots = "".join(circle(*pt(32, 30, 15, a), 2.1, INK) for a in range(120, 421, 30) if a != 390)
    hub = circle(32, 30, 4.2, INK)
    needle = poly([(32, 27.2), (45, 32.5), (32, 32.8)], INK, 1.5)
    return dots + hub + needle

@reg("stack", INDIGO_LIGHT)
def stack():
    top = poly([(32, 13.5), (47, 21), (32, 28.5), (17, 21)], INK, 2.5)
    return (top + stroke("M17 28.5L32 36L47 28.5", INK, 4.2) +
            stroke("M17 36.5L32 44L47 36.5", INK, 4.2))

@reg("stage", BLUE)
def stage():
    tabs = rrect(22, 13, 20, 4.5, 2.2, INK) + rrect(18.5, 18.5, 27, 4.5, 2.2, INK)
    card = rrect(15, 24, 34, 23, 4, INK)
    play = poly([(29, 29.5), (38, 35.5), (29, 41.5)], HOLE, 2)
    return g(tabs + card + play, "translate(0 -1)")

@reg("standard-notes", BLUE_DEEP)
def standard_notes():
    page = rrect(16, 12, 32, 36, 4.5, INK)
    head = line(16, 20.5, 48, 20.5, HOLE, 2.4, "butt")
    lines = "".join(rrect(21, y, w, 2.8, 1.4, HOLE) for y, w in [(25.5, 22), (31, 18), (36.5, 22), (42, 13)])
    return page + head + lines

@reg("starbound", DEEP_PURPLE_LIGHT)
def starbound():
    rays = "".join(line(*pt(35, 26, 9, a), *pt(35, 26, 12.5, a), INK, 2.4) for a in range(150, 391, 40))
    sun = circle(35, 26, 6, INK)
    planet = path("M14 26C31 26 44 34.5 49.5 47.5H14Z", INK,
                  f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"')
    return rays + sun + planet

@reg("stardew-valley", BLUE_GREY)
def stardew_valley():
    comb = circle(21, 13.8, 2.4, RED) + circle(25, 14.5, 2.2, RED)
    beak = poly([(16.5, 19), (13, 21.5), (17, 23)], AMBER, 1.2)
    legs = stroke("M30 41L29 47M37 41L38 47", AMBER, 2.4)
    body = path("M18.5 18.5C18.5 15.5 20.5 14.5 22.5 14.5C26 14.5 27 17.5 27 21"
                "C27 25 29 27.5 33 27.5C37 27.5 40 25 42 22L46 19.5L48.5 20.5"
                "C49 25 48 30 46 33C43 38.5 38.5 42 32 42C24 42 18.5 36.5 18.5 29Z", INK)
    wing = stroke("M29 32.5C32 35.5 37 35.5 40.5 32", HOLE, 2.2)
    return legs + comb + beak + body + wing + circle(21.5, 19.5, 1.4, HOLE) + \
        circle(18.8, 25.5, 1.8, RED)

@reg("stardict", BROWN_LIGHT)
def stardict():
    back = rrect(28.5, 12.5, 18, 34, 3.5, INK)
    front = rrect(17, 18, 16, 28.5, 3.5, INK,
                  f' stroke="{HOLE}" stroke-width="2.4"')
    spines = line(22, 19.5, 22, 45, HOLE, 2.2, "butt") + line(37.5, 12.5, 37.5, 16.5, HOLE, 2.2, "butt")
    pages = line(35, 41.5, 44, 41.5, HOLE, 2.2)
    return back + pages + line(33.5, 12.5, 33.5, 16.2, HOLE, 2.2, "butt") + front + \
        line(21.5, 19.3, 21.5, 45.3, HOLE, 2.2, "butt") + line(24, 40.5, 30, 40.5, HOLE, 2.2)

@reg("stargus", GREY_DARK)
def stargus():
    left = path("M30 40C22.5 37 17 29 16.5 17C20.5 25 25.5 28.5 31 29.5Z", INK)
    right = path("M34 40C41.5 37 47 29 47.5 17C43.5 25 38.5 28.5 33 29.5Z", INK)
    body = path("M32 22C36 25 37.5 31 36 36L32 45L28 36C26.5 31 28 25 32 22Z", INK)
    eye = circle(32, 31.5, 2.6, CYAN_SOFT)
    return left + right + body + eye

@reg("staruml", RED)
def staruml():
    star = _star_d(32, 31, 18, 8, INK, -90, 3)
    cuts = "".join(line(32, 31, *pt(32, 31, 9, -90 + 36 * (2 * k + 1)), HOLE, 2.2) for k in range(5))
    return star + cuts

@reg("stata", BLUE_GREY)
def stata():
    s, gap = 8.5, 2.6
    x0, y0 = 32 - (3 * s + 2 * gap) / 2, 30 - (3 * s + 2 * gap) / 2
    cells = [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
    return "".join(rrect(x0 + c * (s + gap), y0 + r * (s + gap), s, s, 1.6, INK) for r, c in cells)

@reg("steadyflow", LIGHT_BLUE)
def steadyflow():
    arrow = line(32, 27, 32, 38.5, HOLE, 3.4) + stroke("M27 34L32 39L37 34", HOLE, 3.4)
    return g(_cloud(INK) + arrow, "translate(0 -2)")

@reg("stealth-bastard-deluxe", BROWN_LIGHT)
def stealth_bastard():
    head = circle(32, 30, 16, INK)
    strap = line(16.5, 26, 47.5, 26, BROWN_DARK, 4, "butt")
    goggles = (circle(25.5, 26, 6, BROWN_DARK) + circle(25.5, 26, 4, AMBER) +
               circle(38.5, 26, 6, BROWN_DARK) + circle(38.5, 26, 4, AMBER))
    mouth = rrect(29, 38, 6, 2.6, 1.3, BROWN_SOFT)
    return head + strap + goggles + mouth

@reg("steam-rom-manager", BLUE_GREY_DARK)
def steam_rom_manager():
    cards = ""
    for r in range(3):
        for c in range(2):
            x, y = 15 + c * 17, 13 + r * 12
            cards += rrect(x, y, 15, 10, 2.5, INK) + rrect(x + 3, y + 3.9, 9, 2.2, 1.1, HOLE)
    pen = (line(47, 20, 31, 41, HOLE, 9) + line(47, 20, 33, 38.5, INK, 5) +
           poly([(29.5, 43.5), (30.5, 37.5), (35, 41)], INK, 1.2))
    return cards + pen

@reg("steam_icon_341800", RED_DEEP)
def keep_talking():
    bomb = circle(29, 33, 14, INK)
    cap = g(rrect(34.5, 16.5, 8, 6.5, 1.8, INK), "rotate(45 38.5 19.75)")
    fuse = stroke("M40.5 17.5C42 14.5 44 13.5 46 14.5", INK, 2.4)
    spark = _star_d(47.5, 13.5, 4.5, 1.8, INK, -90, 0.8)
    ring = f'<circle cx="29" cy="33" r="8.5" fill="none" stroke="{HOLE}" stroke-width="2.4"/>'
    return bomb + cap + fuse + spark + ring

@reg("steam_icon_553850", AMBER_DEEP)
def helldivers():
    skull = poly([(17, 13), (47, 13), (49, 24), (45, 34), (41, 35), (41, 45), (23, 45), (23, 35),
                  (19, 34), (15, 24)], INK, 3)
    eyes = circle(25.5, 26, 4.8, HOLE) + circle(38.5, 26, 4.8, HOLE)
    nose = poly([(32, 30.5), (34, 34), (30, 34)], HOLE, 1)
    teeth = stroke("M29 39V45M35 39V45", HOLE, 2.2)
    return skull + eyes + nose + teeth

@reg("steamdeck-gaming-return", BLUE_GREY_DARK)
def steamdeck_return():
    arc = stroke("M27.5 14A16 16 0 0 1 27.5 46", INK, 5)
    dot = circle(27.5, 30, 8.8, INK)
    arrow = stroke("M31.5 30H23.5M27 26.5L23.5 30L27 33.5", HOLE, 2.4)
    return g(arc + dot + arrow, "translate(1.5 0)")

@reg("steamlink", BLUE_DEEP)
def steamlink():
    base = circle(32, 30, 16.5, INK)
    pad = path("M24 23.5H40C43 23.5 44.5 25.5 45 28.5L45.5 34.5C46 37.5 43 39 41 37L37.5 33.5"
               "H26.5L23 37C21 39 18 37.5 18.5 34.5L19 28.5C19.5 25.5 21 23.5 24 23.5Z", HOLE)
    return base + pad + circle(25.5, 29, 2.3, INK) + circle(38.5, 29, 2.3, INK)

@reg("steamvr", LIGHT_BLUE_DEEP)
def steamvr():
    knobs = rrect(12.5, 25, 5, 10, 2, INK) + rrect(46.5, 25, 5, 10, 2, INK)
    body = rrect(15.5, 18.5, 33, 23, 7, INK)
    visor = path("M23 22.5H41C43.5 22.5 44.5 24 44.5 26.5V32C44.5 34.5 43.5 36 41 36H36L34 33H30L28 36"
                 "H23C20.5 36 19.5 34.5 19.5 32V26.5C19.5 24 20.5 22.5 23 22.5Z", HOLE)
    return knobs + body + visor

@reg("stella", ORANGE_DEEP)
def stella():
    mid = rrect(29.8, 13, 4.4, 34, 1.2, INK)
    left = path("M23 13H28V27C28 37 24.5 44.5 16 47.5L14 43C20.5 40 23 34 23 27Z", INK)
    right = path("M41 13H36V27C36 37 39.5 44.5 48 47.5L50 43C43.5 40 41 34 41 27Z", INK)
    return mid + left + right

@reg("stellaris", TEAL_DARK)
def stellaris():
    planet = circle(29, 34, 13.5, INK)
    land = (path("M20 29C23 27 26 28.5 25 31.5C24 34 21 33.5 19.5 36C18 33 18 31 20 29Z", HOLE) +
            path("M31 38C34 36 38 37 38.5 40C36 43 32 44 29.5 43C29 41 29.5 39 31 38Z", HOLE))
    ship = path("M48.5 12.5L41 30L37 26.5L24 43L33 23.5L37 26Z", INK,
                f' stroke="{HOLE}" stroke-width="2.2" stroke-linejoin="round"')
    return planet + land + ship

@reg("stellarium", INDIGO_DEEP)
def stellarium():
    moon = _crescent(35.5, 30, 15, 27, 25, 12.5, INK)
    stars = (_star_d(20.5, 37, 5.8, 2.6, INK, -90, 1.2) + _star_d(24, 22, 4.2, 1.9, INK, -90, 1) +
             _star_d(18, 14.5, 3, 1.4, INK, -90, 0.8))
    return moon + stars

@reg("step", TEAL)
def step():
    bar = rrect(15, 13, 34, 4.5, 2.2, INK)
    strings = "".join(line(x, 16, x, 33, INK, 2.2) for x in (22.5, 32, 41.5))
    balls = "".join(circle(x, 37.5, 4.6, INK) for x in (22.5, 32, 41.5))
    return bar + strings + balls

@reg("stepmania-ssc", AMBER_DEEP)
def stepmania():
    return line(20, 42, 41.5, 20.5, INK, 8.5) + stroke("M25 18.5H44V37.5", INK, 8.5)

@reg("sticky", PURPLE_LIGHT)
def sticky():
    note = path("M19 14H45A4 4 0 0 1 49 18V36L39 46H19A4 4 0 0 1 15 42V18A4 4 0 0 1 19 14Z", INK)
    band = line(15, 21, 49, 21, HOLE, 2.2, "butt")
    fold = path("M39 46V39.5A1.5 1.5 0 0 1 40.5 38H49Z", HOLE)
    curl = path("M40.5 44.5V40.5H44.5Z", INK)
    return note + band + fold + curl

@reg("stock_xfburn-burn-cd", BLUE_GREY)
def xfburn():
    disc_ = cut(cpath(29, 28.5, 15.5) + cpath(29, 28.5, 4), INK)
    ring = f'<circle cx="29" cy="28.5" r="7.5" fill="none" stroke="{HOLE}" stroke-width="2.2"/>'
    badge = (f'<circle cx="42" cy="40" r="8.5" fill="#CB7900" stroke="{HOLE}" stroke-width="2.4"/>'
             + line(39, 43, 45, 37, INK, 3.2) + poly([(37, 45), (37.7, 42), (40, 44.3)], INK, 0.8))
    return disc_ + ring + badge

@reg("stoken-gui", RED)
def stoken():
    ring = f'<circle cx="17.5" cy="14.5" r="3.2" fill="none" stroke="{INK}" stroke-width="2.4"/>'
    link = line(19.8, 16.8, 22.5, 19.5, INK, 2.4)
    ball = circle(29, 26, 11, INK)
    handle = line(35.5, 32.5, 45, 42, INK, 9.5) + line(38.5, 35.5, 43, 40, HOLE, 3)
    return ring + link + ball + handle

@reg("strawberry", RED_DEEP)
def strawberry():
    berry = path("M32 47C22 45 16 36.5 16.5 28.5C17 22.5 22.5 20.5 32 22.5"
                 "C41.5 20.5 47 22.5 47.5 28.5C48 36.5 42 45 32 47Z", INK)
    seeds = "".join(circle(x, y, 1.4, HOLE) for x, y in
                    [(24, 29), (32, 28.5), (40, 29), (27.5, 35), (36.5, 35), (32, 41), (21, 34), (43, 34)])
    leaves = poly([(20, 21), (27, 19), (32, 12.5), (37, 19), (44, 21), (36.5, 24.5), (32, 27),
                   (27.5, 24.5)], LIGHT_BLUE_SOFT, 2)
    return berry + seeds + leaves

@reg("streamtuner", BLUE)
def streamtuner():
    note = stroke("M25.5 40V18L43.5 13.5V31", INK, 4) + circle(20.5, 40, 5.5, INK)
    badge = f'<circle cx="41" cy="39" r="9" fill="{INK}" stroke="{HOLE}" stroke-width="2.4"/>'
    hash_ = stroke("M38.5 34.5V43.5M43.5 34.5V43.5M36.5 37H45.5M36.5 41H45.5", HOLE, 2)
    return note + badge + hash_

@reg("stremio", DEEP_PURPLE)
def stremio():
    top = poly([(15, 30), (32, 13), (49, 30)], INK, 3.5)
    bot = poly([(15, 30), (49, 30), (32, 47)], DEEP_PURPLE_SOFT, 3.5)
    play = poly([(28.5, 23), (39, 30), (28.5, 37)], HOLE, 2)
    return top + bot + play

@reg("stretchly", TEAL_DARK)
def stretchly():
    base = circle(32, 30, 16.5, INK)
    s = stroke("M38.5 22C36.5 20 34 19.5 31.5 19.5C28 19.5 25.5 21.5 26 24.5"
               "C26.8 29 38 28.5 38 34.5C38 38 35 40.5 31 40.5C28.5 40.5 26 39.5 24.5 37.5", HOLE, 4.2)
    return base + s

@reg("stride", BLUE_DEEP)
def stride():
    leg = poly([(29, 13), (36.5, 13), (49.5, 46), (41.5, 46)], INK, 2.5)
    ramp = path("M14.5 46.5C21 43.5 25 37 27.5 29.5L33 43.5L31.5 46.5Z", INK,
                f' stroke="{HOLE}" stroke-width="2.2" stroke-linejoin="round"')
    return leg + ramp

@reg("studio-3t", PURPLE_SOFT)
def studio_3t():
    shell = path("M22 34.5C22 25 28.5 18.5 36.5 18.5C44.5 18.5 49 25 49 32.5C49 34.5 48 36 46 36"
                 "H23.5C22.5 36 22 35.5 22 34.5Z", INK)
    head = path("M14 34C14 30 17 28 20 28C23 28 25 30.5 25 33V36H16C14.8 36 14 35.2 14 34Z", INK)
    legs = rrect(25.5, 34, 6, 9, 3, INK) + rrect(39.5, 34, 6, 9, 3, INK)
    return shell + head + legs + circle(18.5, 31.5, 1.4, HOLE) + stroke("M26 36H46", HOLE, 1.8)

@reg("stuntrally", YELLOW_DARK)
def stuntrally():
    return _sr(4.6)

@reg("subdownloader", ORANGE_DEEP)
def subdownloader():
    bubble = rrect(14, 14, 36, 25, 5, INK) + poly([(28, 38), (36, 38), (32, 44.5)], INK, 2)
    lines = "".join(line(21, y, 43, y, HOLE, 2.6) for y in (20.5, 26.5, 32.5))
    return bubble + lines

@reg("sublime-merge", TEAL_DEEP)
def sublime_merge():
    upper = poly([(17, 18.5), (22.5, 13.5), (39, 27), (33, 32)], TEAL_SOFT, 2.5)
    lower = poly([(16, 41.5), (32.5, 27.5), (48, 27.5), (48, 34), (35, 34), (21.5, 46)], INK, 2.5)
    return upper + lower

@reg("subsonic", AMBER_DEEP)
def subsonic():
    scope = stroke("M34 21V14H38", INK, 2.6)
    tower = rrect(27, 18.5, 12, 9, 3, INK)
    hull = rrect(18, 24, 32, 18, 9, INK)
    tail = poly([(12.5, 27), (19, 31), (19, 35), (12.5, 39)], INK, 2)
    ports = "".join(circle(x, 33, 2.8, HOLE) for x in (27, 34, 41))
    return scope + tower + tail + hull + ports

@reg("substance", RED_DEEP)
def substance():
    return stroke("M45 18.5L39.5 13.5H24.5L18.5 21L45 36.5L39.5 46.5H24.5L19 41.5", INK, 5.8)

@reg("subsurface-icon", BLUE_DARK)
def subsurface():
    wave = stroke("M14 13.5C17 11.5 20 11.5 23 13.5C26 15.5 29 15.5 32 13.5C35 11.5 38 11.5 41 13.5"
                  "C44 15.5 47 15.5 50 13.5", INK, 2.6)
    head = circle(31, 22, 3.6, INK)
    tank = g(rrect(33.5, 25, 5, 12, 2.5, INK), "rotate(12 36 31)")
    torso = line(30.5, 27.5, 29, 36, INK, 5.5)
    arms = stroke("M30 29L24 33.5L21.5 30.5", INK, 2.8)
    legs = stroke("M29 36L25.5 44M29.5 36L34 43.5", INK, 3.2)
    fins = (poly([(23, 43), (27.5, 45), (22, 48.5)], INK, 1.5) +
            poly([(32, 44.5), (36.5, 42.5), (38, 48)], INK, 1.5))
    return wave + tank + head + torso + arms + legs + fins

@small("spotify-qt")
def spotify_qt_s():
    qt = poly([(22, 13), (49, 13), (49, 39), (42, 47), (15, 47), (15, 21)], INK, 3)
    return qt + stroke("M21 25.5C28 22.5 36 23 43 27", HOLE, 4.5) + stroke("M23.5 34C29 32.5 34.5 33 40 36", HOLE, 4)

@small("spring-tool-suite")
def spring_tool_suite_s():
    gear = _gear(32, 30, 17.5, 13.5, 8, INK, 0.55)
    leaf = path("M23.5 39C22.5 29 29 21 42 20C42.5 32.5 34.5 40 23.5 39Z", HOLE)
    return gear + circle(32, 30, 14, INK) + leaf

@small("spyder")
def spyder_s():
    web = stroke("M15 12V33M15 12H37M15 12L28 25", INK, 3) + stroke("M15 24C21 23 24 19 26 12", INK, 3)
    s = stroke("M47 28C45.5 26.3 43.5 25.5 41 25.5C37.5 25.5 35 27.5 35 30.5"
               "C35 36 47.5 34.5 47.5 41C47.5 44.5 44.5 46.5 40.5 46.5C37.5 46.5 35.5 45.5 34 43.5", INK, 5)
    return web + s

@small("sqldeveloper")
def sqldeveloper_s():
    db = _db(27, 18, 41, 13, 4.5, [29.5])
    badge = (f'<circle cx="41" cy="39" r="10" fill="#9E9D9E" stroke="{HOLE}" stroke-width="2.6"/>'
             + poly([(38, 34), (46, 39), (38, 44)], INK, 1.5))
    return db + badge

@small("sqlitebrowser")
def sqlitebrowser_s():
    return _db(32, 18, 42, 15, 5, [30])

@small("squeak")
def squeak_s():
    ears = (poly([(18, 28), (18, 11), (29, 20)], INK, 3) + poly([(46, 28), (46, 11), (35, 20)], INK, 3))
    head = circle(32, 32, 13.5, INK)
    return ears + head + circle(26.5, 30.5, 3, HOLE) + circle(37.5, 30.5, 3, HOLE)

@small("sr-editor")
def sr_editor_s():
    return _sr(5.2)

@small("stuntrally")
def stuntrally_s():
    return _sr(5.2)

@small("stacer")
def stacer_s():
    dots = "".join(circle(*pt(32, 30, 15, a), 2.8, INK) for a in range(135, 406, 45) if a != 360)
    return dots + circle(32, 30, 5, INK) + poly([(32, 26.5), (46, 32.5), (32, 33.5)], INK, 1.5)

@small("stack")
def stack_s():
    top = poly([(32, 12), (48, 20.5), (32, 29), (16, 20.5)], INK, 2.5)
    return top + stroke("M16 32L32 40.5L48 32", INK, 5.5)

@small("stage")
def stage_s():
    return (rrect(19, 13, 26, 5.5, 2.5, INK) + rrect(14, 21, 36, 26, 4.5, INK) +
            poly([(28, 27), (39, 34), (28, 41)], HOLE, 2))

@small("standard-notes")
def standard_notes_s():
    page = rrect(15, 12, 34, 36, 5, INK) + line(15, 21, 49, 21, HOLE, 3, "butt")
    return page + "".join(rrect(21, y, w, 4, 2, HOLE) for y, w in [(27, 22), (35, 15)])

@small("starbound")
def starbound_s():
    rays = "".join(line(*pt(35, 26, 10, a), *pt(35, 26, 14, a), INK, 3) for a in (180, 225, 270, 315, 360))
    planet = path("M13 27C31 27 44 35 50 48H13Z", INK,
                  f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')
    return rays + circle(35, 26, 7, INK) + planet

@small("stardew-valley")
def stardew_valley_s():
    comb = circle(22, 13.5, 3, RED)
    beak = poly([(16, 18.5), (12, 21.5), (16.5, 23.5)], AMBER, 1.2)
    body = path("M17.5 19C17.5 15.5 20 14 22.5 14C26 14 27.5 17 27.5 21"
                "C27.5 25 29.5 27.5 33 27.5C37 27.5 40 25 42 22L46 19L49 20.5"
                "C49.5 25 48.5 30 46.5 33.5C43.5 39 38.5 43 32 43C23.5 43 17.5 37 17.5 29Z", INK)
    return comb + beak + body + stroke("M32 43V47", AMBER, 3)

@small("stardict")
def stardict_s():
    back = rrect(29, 12, 18, 35, 3.5, INK)
    front = rrect(16, 18, 17, 29, 3.5, INK, f' stroke="{HOLE}" stroke-width="3"')
    return back + front + line(22, 19.5, 22, 45.5, HOLE, 3, "butt")

@small("staruml")
def staruml_s():
    return _star_d(32, 31, 18.5, 8.5, INK, -90, 3)

@small("steam-rom-manager")
def steam_rom_manager_s():
    cards = "".join(rrect(15 + c * 18, 13 + r * 18, 15, 15, 3, INK) for r in range(2) for c in range(2))
    pen = line(48, 19, 30, 42, HOLE, 11) + line(48, 19, 31, 40.5, INK, 6)
    return cards + pen

@small("steam_icon_341800")
def keep_talking_s():
    bomb = circle(29, 33, 14.5, INK)
    cap = g(rrect(34, 16, 9, 7.5, 2, INK), "rotate(45 38.5 19.75)")
    return bomb + cap + _star_d(47, 13.5, 5, 2.2, INK, -90, 0.8)

@small("steam_icon_553850")
def helldivers_s():
    skull = poly([(17, 13), (47, 13), (49, 24), (45, 34), (41, 35), (41, 45), (23, 45), (23, 35),
                  (19, 34), (15, 24)], INK, 3)
    return skull + circle(25, 26, 5.5, HOLE) + circle(39, 26, 5.5, HOLE)

@small("steamdeck-gaming-return")
def steamdeck_return_s():
    return g(stroke("M27.5 13A17 17 0 0 1 27.5 47", INK, 6) + circle(27.5, 30, 9.5, INK),
             "translate(1.5 0)")

@small("steamlink")
def steamlink_s():
    base = circle(32, 30, 17, INK)
    pad = path("M23.5 22.5H40.5C43.5 22.5 45 25 45.5 28L46 35C46.5 38 43 39.5 41 37.5L37.5 34"
               "H26.5L23 37.5C21 39.5 17.5 38 18 35L18.5 28C19 25 20.5 22.5 23.5 22.5Z", HOLE)
    return base + pad

@small("steamvr")
def steamvr_s():
    return (rrect(11.5, 24, 6, 12, 2, INK) + rrect(46.5, 24, 6, 12, 2, INK) +
            rrect(14.5, 17.5, 35, 25, 7.5, INK) + rrect(20, 23, 24, 14, 4, HOLE))

@small("stella")
def stella_s():
    mid = rrect(29.3, 12, 5.4, 36, 1.5, INK)
    left = path("M21.5 12H27.5V27C27.5 37 24 45 15.5 48.5L13 43C19.5 40 21.5 34 21.5 27Z", INK)
    right = path("M42.5 12H36.5V27C36.5 37 40 45 48.5 48.5L51 43C44.5 40 42.5 34 42.5 27Z", INK)
    return mid + left + right

@small("stellaris")
def stellaris_s():
    ship = path("M49 11.5L41 31L37 27L23 44.5L33 23L37.5 26.5Z", INK,
                f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')
    return circle(29, 34, 14, INK) + ship

@small("stellarium")
def stellarium_s():
    return _crescent(36, 30, 15.5, 27, 25, 12.5, INK) + _star_d(20, 36, 7.5, 3.4, INK, -90, 1.2)

@small("step")
def step_s():
    bar = rrect(14, 12, 36, 5.5, 2.5, INK)
    strings = "".join(line(x, 16, x, 32, INK, 2.8) for x in (21.5, 32, 42.5))
    return bar + strings + "".join(circle(x, 37, 5.2, INK) for x in (21.5, 32, 42.5))

@small("sticky")
def sticky_s():
    note = path("M19 13H45A4 4 0 0 1 49 17V35L38 46H19A4 4 0 0 1 15 42V17A4 4 0 0 1 19 13Z", INK)
    return note + path("M38 46V38H49Z", HOLE)

@small("stock_xfburn-burn-cd")
def xfburn_s():
    disc_ = cut(cpath(29, 28.5, 16) + cpath(29, 28.5, 4.5), INK)
    badge = f'<circle cx="42" cy="40" r="9" fill="#CB7900" stroke="{HOLE}" stroke-width="2.8"/>'
    return disc_ + badge + line(38.5, 43.5, 45.5, 36.5, INK, 3.4)

@small("stoken-gui")
def stoken_s():
    return circle(28, 25, 12.5, INK) + line(35, 32, 45, 42, INK, 11)

@small("strawberry")
def strawberry_s():
    berry = path("M32 48C21.5 46 15.5 37 16 28.5C16.5 22.5 22.5 20.5 32 22.5"
                 "C41.5 20.5 47.5 22.5 48 28.5C48.5 37 42.5 46 32 48Z", INK)
    leaves = poly([(19.5, 21), (27, 18.5), (32, 12), (37, 18.5), (44.5, 21), (32, 27)], GREY_SOFT, 2)
    return berry + leaves + circle(26, 32, 1.9, HOLE) + circle(38, 32, 1.9, HOLE) + circle(32, 39, 1.9, HOLE)

@small("streamtuner")
def streamtuner_s():
    note = stroke("M25.5 40V18L43.5 13.5V30", INK, 5) + circle(20.5, 40, 6.2, INK)
    return note + f'<circle cx="41" cy="39" r="9.5" fill="{INK}" stroke="{HOLE}" stroke-width="2.8"/>' + \
        stroke("M38 34.5V43.5M44 34.5V43.5", HOLE, 2.6)

@small("stremio")
def stremio_s():
    return (poly([(14, 30), (32, 12), (50, 30)], INK, 3.5) + poly([(14, 30), (50, 30), (32, 48)], DEEP_PURPLE_SOFT, 3.5)
            + poly([(28, 22), (40, 30), (28, 38)], HOLE, 2))

@small("stretchly")
def stretchly_s():
    s = stroke("M39 22C37 20 34 19 31.5 19C27.5 19 25 21.5 25.5 24.5"
               "C26.5 29.5 38.5 28.5 38.5 35C38.5 38.5 35 41 31 41C28 41 25.5 40 24 38", HOLE, 5)
    return circle(32, 30, 17, INK) + s

@small("studio-3t")
def studio_3t_s():
    shell = path("M21 36C21 25 28 18 36.5 18C45 18 49.5 25 49.5 33C49.5 35.5 48.5 37 46.5 37H22C21.5 37 21 36.5 21 36Z", INK)
    head = path("M13 35C13 30.5 16 28 19.5 28C23 28 25 30.5 25 33.5V37H15C13.8 37 13 36.2 13 35Z", INK)
    return shell + head + rrect(25, 35, 7, 9, 3, INK) + rrect(39.5, 35, 7, 9, 3, INK)

@small("subdownloader")
def subdownloader_s():
    bubble = rrect(13, 13, 38, 27, 5, INK) + poly([(27, 39), (37, 39), (32, 46)], INK, 2)
    return bubble + line(20.5, 21.5, 43.5, 21.5, HOLE, 3.6) + line(20.5, 30.5, 43.5, 30.5, HOLE, 3.6)

@small("subsonic")
def subsonic_s():
    tower = rrect(26, 16, 14, 10, 3, INK)
    hull = rrect(17, 23, 34, 20, 10, INK)
    tail = poly([(11.5, 26.5), (19, 31), (19, 35), (11.5, 39.5)], INK, 2)
    return tower + tail + hull + circle(28, 33, 3.2, HOLE) + circle(38, 33, 3.2, HOLE)

@small("subsurface-icon")
def subsurface_s():
    wave = stroke("M13 13.5C17 10.5 21 10.5 25 13.5C29 16.5 33 16.5 37 13.5C41 10.5 45 10.5 49 13.5", INK, 3.2)
    body = circle(31, 22.5, 4.3, INK) + line(30.5, 28, 29, 36, INK, 7) + \
        g(rrect(34, 25, 6, 12, 3, INK), "rotate(12 37 31)")
    legs = stroke("M29 36L25 45M29.5 36L35 44.5", INK, 4)
    return wave + body + legs
