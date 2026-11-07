# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 43: lskat .. mate-panel-drawer."""
import math
from lm import *
from glyphs.kit import arc, ell_e, registry, _ring, _star

ICONS, SMALL, reg, small = registry()

def diamond(cx, cy, r, fill, rounding=0):
    return poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill, rounding)

def sparkle(cx, cy, r, fill):
    return poly(_star(cx, cy, r, r * .32, 4), fill, 1)

@reg("lskat", RED_DEEP)
def lskat():
    card = g(rrect(19, 12, 26, 36, 4, INK), "rotate(-6 32 30)")
    return (card + diamond(32, 30, 7.5, HOLE, 1.5)
            + g(diamond(24.5, 18.5, 2.6, HOLE) + diamond(39.5, 41.5, 2.6, HOLE), "rotate(-6 32 30)"))

@reg("ltris", BLUE_DEEP)
def ltris():
    out = ""
    for c in range(4):
        out += rrect(16 + c * 8, 39, 7, 7, 1.5, INK)
    for c in range(3):
        out += rrect(16 + c * 8, 31, 7, 7, 1.5, INK)
    for x, y in [(40, 31), (40, 23), (40, 15), (32, 15)]:
        out += rrect(x, y, 7, 7, 1.5, RED_SOFT)
    return out

@reg("lugaru", BROWN_LIGHT)
def lugaru():
    ears = (g(ell_e(25, 20, 4.2, 10.5, INK), "rotate(-14 25 20)") +
            g(ell_e(39, 20, 4.2, 10.5, INK), "rotate(14 39 20)"))
    inner = (g(ell_e(25, 19.5, 1.6, 7, HOLE), "rotate(-14 25 20)") +
             g(ell_e(39, 19.5, 1.6, 7, HOLE), "rotate(14 39 20)"))
    head = ell_e(32, 36, 12, 10.5, INK)
    face = (circle(27, 34.5, 2, HOLE) + circle(37, 34.5, 2, HOLE) +
            poly([(29.8, 39), (34.2, 39), (32, 41.5)], PINK_SOFT, 1.2))
    return ears + inner + head + face

@reg("lzdoom", DEEP_PURPLE)
def lzdoom():
    return stroke("M19.5 20V39.5H27", GREY_SOFT, 5) + stroke("M31 20.5H45L31 39.5H45", INK, 5)

@reg("machinarium", YELLOW_DARK)
def machinarium():
    top = rrect(29.5, 12, 5, 7, 1.2, INK)
    dome = path("M18 46V31C18 23 24 18.5 32 18.5C40 18.5 46 23 46 31V46Z", INK)
    seam = line(32, 22, 32, 30, HOLE, 2.2)
    eyes = (circle(25.5, 35, 4.3, HOLE) + circle(38.5, 35, 4.3, HOLE) +
            circle(25.5, 35, 1.9, INK) + circle(38.5, 35, 1.9, INK))
    band = line(18, 42, 46, 42, HOLE, 2.4, "butt")
    return top + dome + seam + eyes + band

@reg("magicka-2", RED_DEEP)
def magicka():
    staff = line(19.5, 24, 21, 47, INK, 3)
    orb = circle(19, 20, 4, LIGHT_BLUE_SOFT)
    hood = path("M24 47L27.5 30C25.5 21 29.5 14 35.5 14C42 14 46 20.5 44.5 28.5L49 47Z", INK)
    face = circle(36, 25.5, 5.8, HOLE)
    arm = stroke("M26 36L21 34", INK, 3.4)
    return staff + orb + hood + face + arm

@reg("makehuman", ORANGE_DEEP)
def makehuman():
    body = poly([(14, 18.5), (32, 29), (50, 18.5), (47.5, 25), (35, 32.5), (32, 47),
                 (29, 32.5), (16.5, 25)], INK, 2)
    return body + circle(32, 20.5, 4, INK)

@reg("mame", BLUE_DEEP)
def mame():
    return stroke("M15 41L27.5 19.5V36L41 19.5V41L49 32", INK, 5.5)

@reg("manaplus", DEEP_ORANGE_DEEP)
def manaplus():
    m = stroke("M16.5 44V33C16.5 29 19 27 22.5 27C26 27 28.5 29 28.5 33V44"
               "M28.5 33C28.5 29 31 27 34.5 27C38 27 40.5 29 40.5 33V44", INK, 5)
    plus = line(44, 14, 44, 25, INK, 3.8) + line(38.5, 19.5, 49.5, 19.5, INK, 3.8)
    return m + plus

@reg("marsshooter", DEEP_ORANGE_DARK)
def marsshooter():
    spots = "".join(circle(x, y, r, DEEP_ORANGE_DEEP) for x, y, r in
                    [(25.5, 23, 4.5), (38, 34.5, 5.5), (39.5, 21, 2.6), (24, 38, 3), (31, 30, 2)])
    return circle(CX, CY, 16.5, DEEP_ORANGE_LIGHT) + spots

@reg("luakit", BLUE_DARK)
def luakit():
    globe = circle(CX, CY, 16.5, BLUE_DEEP)
    moon = circle(29.5, 31.5, 12, INK) + circle(35, 26.5, 10, BLUE_DEEP)
    return globe + moon

@reg("lvim", DEEP_PURPLE_DARK)
def lvim():
    orbit = g(ell_e(32, 30, 19, 6, "none", ' stroke="#9C7EC8" stroke-width="2.6"'), "rotate(-20 32 30)")
    return (_ring(CX, CY, 13, INK, 3.4) + stroke("M24 23V37H29", INK, 3.2)
            + stroke("M31.5 23L35.5 37L39.5 23", INK, 3.2) + orbit)

@reg("lynx", BLUE_GREY_DEEP)
def lynx():
    red = poly([(43, 19), (34.5, 32.5), (29.5, 27.5)], RED_LIGHT, 1.5)
    white = poly([(21, 41), (34.5, 32.5), (29.5, 27.5)], INK, 1.5)
    return _ring(CX, CY, 16, INK, 2.6) + red + white

@reg("lyricfier", PURPLE)
def lyricfier():
    return "".join(rrect(x - 2.4, 30 - h, 4.8, 2 * h, 2.4, INK)
                   for x, h in [(17.5, 8), (24.75, 13), (32, 16), (39.25, 11), (46.5, 7)])

@reg("magnatune", BLUE_DARK)
def magnatune():
    bars = (rrect(21, 25.5, 5.5, 9, 2.75, HOLE) + rrect(29.25, 21, 5.5, 18, 2.75, HOLE) +
            rrect(37.5, 24, 5.5, 12, 2.75, HOLE))
    return circle(CX, CY, 16.5, INK) + bars

@reg("mail.ru-cloud", LIGHT_BLUE_DEEP)
def mailru_cloud():
    cloud = (circle(23, 32, 7.5, INK) + circle(33.5, 25, 10, INK) + circle(42.5, 32.5, 6.5, INK) +
             rrect(15.5, 31, 33.5, 12, 6, INK))
    dots = circle(28.5, 34, 5.5, ORANGE) + circle(37, 33, 4.5, AMBER)
    return cloud + dots

@reg("mailspring", TEAL)
def mailspring():
    env = rrect(15, 19, 34, 23, 4, INK)
    lines = (stroke("M18 22.5L32 33L46 22.5", HOLE, 2.8) +
             stroke("M18.5 38.5L26.5 31.5", HOLE, 2.4) + stroke("M45.5 38.5L37.5 31.5", HOLE, 2.4))
    return env + lines

@reg("makemkv", GREY_DARK)
def makemkv():
    disc = circle(32, 25.5, 14, INK) + circle(32, 25.5, 5, HOLE) + circle(32, 25.5, 2, INK)
    band = rrect(15, 35, 34, 13, 3.5, GREY)
    mkv = (stroke("M19 45V38.5L22.5 42L26 38.5V45", INK, 2.3) +
           stroke("M29.5 38.5V45M34.5 38.5L30 41.8L34.5 45", INK, 2.3) +
           stroke("M37.5 38.5L41 45L44.5 38.5", INK, 2.3))
    return disc + band + mkv

@reg("maltego", BLUE_GREY_DEEP)
def maltego():
    return (circle(CX, CY, 16.5, INK) + circle(26.5, 23.5, 5, BLUE) +
            circle(38.5, 30.5, 5, BLUE_LIGHT) + circle(26.5, 37.5, 5, RED))

@reg("masterpassword-gui", BLUE_GREY_DARK)
def masterpassword():
    dots = circle(20.5, 30, 3.3, INK) + circle(29, 30, 3.3, INK) + circle(37.5, 30, 3.3, INK)
    return dots + rrect(42.5, 20.5, 4, 19, 2, BLUE_LIGHT)

@reg("lsp-plugins", CYAN_DEEP)
def lsp():
    return (stroke("M14.5 21V39H22", INK, 4) +
            stroke("M35 23.8C34 22 32.3 21 30.2 21C27.3 21 25.5 22.7 25.5 25"
                   "C25.5 30.5 35.5 28 35.5 34.2C35.5 37.2 33 39 30 39"
                   "C27.8 39 26 38 25 36.2", INK, 4)
            + stroke("M40 39V21H44.3A5 5 0 0 1 44.3 31H40", INK, 4))

@reg("lucidchart", ORANGE_DEEP)
def lucidchart():
    links = line(19, 30, 33.5, 20.5, INK, 3) + line(19, 30, 33.5, 39.5, INK, 3)
    dots = "".join(circle(x, y, r, INK) for x, y, r in
                   [(19, 30, 5.8), (33.5, 20.5, 5), (45, 20.5, 5), (33.5, 39.5, 5), (45, 39.5, 5)])
    return links + dots

@reg("luckyBackup", BLUE)
def luckybackup():
    out = ""
    for a0, a1 in [(185, 305), (5, 125)]:
        out += stroke(arc(CX, CY, 12.5, a0, a1), INK, 5)
        tip = pt(CX, CY, 12.5, a1 + 30)
        out += poly([pt(CX, CY, 6.5, a1), pt(CX, CY, 18.5, a1), tip], INK, 2)
    return out

@reg("luminance-hdr", RED_DEEP)
def luminance():
    back = rrect(14, 13, 24, 22, 3.5, AMBER_LIGHT)
    mid = rrect(19, 18, 25, 23, 3.5, ORANGE)
    front = rrect(24, 24, 26, 23, 3.5, INK)
    hill = path("M26.5 44.5C31 44.5 32.5 31 37.5 31C42.5 31 44 44.5 47.5 44.5Z", HOLE)
    return back + mid + front + hill

@reg("lunacy", LIGHT_BLUE_DEEP)
def lunacy():
    bar = rrect(17, 14, 10.5, 32, 2, INK)
    tri = poly([(30.5, 46), (46.5, 46), (46.5, 27)], INK, 2.4)
    return bar + tri + sparkle(40.5, 18.5, 6.5, INK)

@reg("lunarclient", BLUE_GREY_DARK)
def lunarclient():
    house = stroke("M19.5 28L32 16.5L44.5 28V43.5H19.5Z", INK, 3.4)
    moon = circle(30.5, 33, 6.5, INK) + circle(33.8, 30.8, 5.5, HOLE)
    stars = circle(38.5, 27, 1.4, INK) + circle(36.5, 37.5, 1.2, INK)
    return house + moon + stars

@reg("lyne", PINK)
def lyne():
    xs = [18.5, 27.5, 36.5, 45.5]
    word = (stroke("M16 13V19H21", INK, 2.2) + stroke("M25 13L27.5 16L30 13M27.5 16V19", INK, 2.2)
            + stroke("M34 19V13L39 19V13", INK, 2.2) + stroke("M48 13H43V19H48M43 16H47", INK, 2.2))
    grid = "".join(diamond(x, y, 3.8, INK, 1) for x in xs for y in [27, 35.5, 44])
    return word + grid

@reg("lyrebird", BROWN)
def lyrebird():
    tail = (stroke("M33 37C39 33 45 27 45 19C45 15.5 42.5 14 40 15.5", INK, 3.4) +
            stroke("M31 36C28 30 25.5 24.5 27.5 18.5C28.5 15.5 31.5 15.5 32 18", INK, 3.4) +
            stroke("M32.5 36C35 30 37 24 36 16", INK, 2.6))
    body = ell_e(26, 39, 8.5, 5.5, INK) + circle(18.5, 35, 3.8, INK)
    beak = poly([(15.5, 34), (12.5, 36), (15.5, 36.5)], INK, 1)
    legs = line(25, 44, 24, 48, INK, 2.2) + line(29, 44, 30, 48, INK, 2.2)
    return tail + body + beak + legs + circle(18, 34.3, 1.1, HOLE)

@reg("lyx", INDIGO_DEEP)
def lyx():
    return (stroke("M16 18V38H24", INK, 4.2) +
            stroke("M26.5 24L31 33M36 24L29.5 44", AMBER_LIGHT, 4.2) +
            stroke("M38.5 19L48 38M48 19L38.5 38", RED_SOFT, 4.2))

@reg("magictree", BLUE_DEEP)
def magictree():
    tiers = (poly([(32, 18), (39.5, 28.5), (24.5, 28.5)], INK, 3) +
             poly([(32, 24.5), (43.5, 37.5), (20.5, 37.5)], INK, 3) +
             poly([(32, 31), (47.5, 47), (16.5, 47)], INK, 3))
    balls = "".join(circle(x, y, 1.8, HOLE) for x, y in
                    [(29, 26), (35, 33), (27.5, 34.5), (24, 44), (32, 42), (40, 44)])
    return tiers + balls + poly(_star(32, 15.5, 5.5, 2.4), AMBER_SOFT, 1)

@reg("makagiga", CYAN_DEEP)
def makagiga():
    stripes = "".join(line(x, 47, x + 5, 41.5, CYAN_SOFT, 2.6) for x in (19, 27, 35, 43))
    cloud = (circle(24, 29, 7, INK) + circle(34.5, 24.5, 9, INK) + circle(43, 30, 6, INK) +
             rrect(15, 28, 34.5, 10, 5, INK))
    plus = "".join(line(x, 28.5, x, 34, HOLE, 2.4) + line(x - 2.75, 31.25, x + 2.75, 31.25, HOLE, 2.4)
                   for x in (27, 38))
    return stripes + cloud + plus

@reg("mandelbulber2", YELLOW_DARK)
def mandelbulber():
    pts = []
    turns = 2.8
    for i in range(0, 200):
        t = i / 199 * turns * 2 * math.pi
        r = 1.2 + 14.8 * t / (turns * 2 * math.pi)
        pts.append((CX + r * math.cos(t), CY + r * math.sin(t)))
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts)
    return stroke(d, INK, 3)

@reg("mangareader", BLUE_GREY_DEEP)
def mangareader():
    arches = stroke("M17 38V24.5C17 20.5 19.5 18.5 23 18.5C26.5 18.5 29 20.5 29 24.5"
                    "M29 24.5C29 20.5 31.5 18.5 35 18.5C38.5 18.5 41 20.5 41 24.5V38", INK, 4)
    eyes = _ring(23, 30, 3, INK, 2.6) + _ring(35, 30, 3, INK, 2.6)
    foot = stroke("M26 42.5H41C44 42.5 46 44 46 46.5", INK, 3.6)
    return arches + eyes + foot

@reg("manjaro-architect", BLUE_GREY_DEEP)
def manjaro_architect():
    hash_ = (line(19, 15, 18, 27, INK, 2.4) + line(24.5, 15, 23.5, 27, INK, 2.4) +
             line(15.5, 19, 27, 19, INK, 2.4) + line(15, 23.5, 26.5, 23.5, INK, 2.4))
    under = line(30, 27, 38, 27, INK, 3)
    badge = circle(39, 37, 10.5, TEAL_LIGHT)
    arrow = line(39, 31, 39, 42.5, INK, 3) + stroke("M34.5 38.5L39 43L43.5 38.5", INK, 3)
    return hash_ + under + badge + arrow

@reg("manjaro-settings-manager", TEAL)
def manjaro_settings():
    logo = (rrect(15, 13, 9, 34, 1.5, INK) + rrect(15, 13, 22, 9, 1.5, INK) +
            rrect(28, 26, 9, 21, 1.5, INK) + rrect(41, 13, 9, 34, 1.5, INK))
    badge = circle(42.5, 40.5, 10.5, HOLE) + circle(42.5, 40.5, 8.8, DEEP_PURPLE_LIGHT)
    teeth = "".join(g(rrect(41.1, 33.5, 2.8, 3.5, .6, INK), f"rotate({45 * k} 42.5 40.5)") for k in range(8))
    gear = teeth + circle(42.5, 40.5, 4.6, INK) + circle(42.5, 40.5, 1.9, DEEP_PURPLE_LIGHT)
    return logo + badge + gear

@reg("manuskript", GREY_DEEP)
def manuskript():
    vane = path("M19 43C18.5 29 30 16 47 13.5C45.5 30 34 42 19 43Z", INK)
    spine = stroke("M20 42L38 23.5", HOLE, 2.2)
    notch = stroke("M33.5 36L29.5 33", HOLE, 2.2)
    quill = line(20, 42, 15, 47, INK, 2.8)
    return vane + spine + notch + quill

@reg("manyverse", INDIGO)
def manyverse():
    m = stroke("M19.5 37.5V20L32 34L44.5 20V37.5", INK, 4.4)
    ends = _ring(19.5, 41.5, 3.3, INK, 2.6) + _ring(44.5, 41.5, 3.3, INK, 2.6)
    return m + ends

@reg("maple", BLUE_DARK)
def maple():
    right = [(32, 11.5), (35.5, 18.5), (39.5, 16.5), (38, 26), (44, 20), (45.5, 24),
             (50.5, 23), (47.5, 30), (50, 32.5), (41, 38.5), (42, 42), (33.2, 40.5), (33.2, 48)]
    left = [(64 - x, y) for x, y in reversed(right)]
    return poly(right + left, INK, 1.4)

@reg("maps", BLUE)
def maps():
    base = ell_e(32, 44, 11, 3.6, "none", f' stroke="{INK}" stroke-width="2.4"')
    pin = path("M32 12C25.5 12 20.5 17 20.5 23.5C20.5 31.5 32 44 32 44C32 44 43.5 31.5 43.5 23.5"
               "C43.5 17 38.5 12 32 12Z", INK)
    return base + pin + circle(32, 23.5, 4.6, HOLE)

@reg("maps-alt", BROWN_LIGHT)
def maps_alt():
    curve = stroke("M14 35C20 33 23 41 30 41C36 41 39 45.5 49 45.5", AMBER_SOFT, 3)
    road = stroke("M47 13L27 33V48", INK, 5)
    pin = (path("M41 30C37.7 30 35.5 32.4 35.5 35.3C35.5 39 41 44.5 41 44.5C41 44.5 46.5 39 46.5 35.3"
                "C46.5 32.4 44.3 30 41 30Z", RED_LIGHT) + circle(41, 35.3, 2, INK))
    return curve + road + pin

@reg("marble", BLUE_DARK)
def marble():
    globe = circle(CX, CY, 16.5, BLUE_LIGHT)
    land = (path("M21 22C24 18.5 28 19 29 22C30 25.5 26 26 26.5 30C27 34 23 35 21 32"
                 "C19 29 18.5 25 21 22Z", LIGHT_BLUE_LIGHT) +
            path("M36 37C38.5 35 42 36 42.5 38.5C43 41 40 43.5 37.5 42.5C35.5 41.5 34.5 38.5 36 37Z", LIGHT_BLUE_LIGHT))
    red = poly([(44, 18), (34.3, 32.3), (29.7, 27.7)], RED_LIGHT, 1.5)
    white = poly([(20, 42), (34.3, 32.3), (29.7, 27.7)], INK, 1.5)
    return globe + land + red + white

@reg("marknoto", AMBER_DEEP)
def marknoto():
    note = path("M20 14H44A3 3 0 0 1 47 17V35L35 47H20A3 3 0 0 1 17 44V17A3 3 0 0 1 20 14Z", INK)
    curl = path("M47 35H38A3 3 0 0 0 35 38V47Z", AMBER_LIGHT)
    code = (stroke("M26.5 24.5L22 29.5L26.5 34.5", HOLE, 3) + stroke("M37.5 24.5L42 29.5L37.5 34.5", HOLE, 3)
            + stroke("M34 22.5L30 36.5", HOLE, 3))
    return note + curl + code

@reg("markpado", BROWN)
def markpado():
    return (stroke("M24 21L15 30L24 39", INK, 4.6) + stroke("M40 21L49 30L40 39", INK, 4.6)
            + stroke("M35.5 17L28.5 43", INK, 4.6))

@reg("marktext", BLUE_DARK)
def marktext():
    m = stroke("M17 41V19L32 31L47 19V41", INK, 5)
    chev = stroke("M24.5 38.5L32 44L39.5 38.5", LIGHT_BLUE_SOFT, 4)
    return m + chev

@reg("massif-visualizer", PURPLE_LIGHT)
def massif():
    page = rrect(19, 12.5, 29, 35, 3.5, INK)
    chart = path("M23 44L28.5 31L33 37L39.5 23L45 44Z", HOLE, f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"')
    rings = "".join(rrect(14.5, y, 9, 3.8, 1.9, INK, f' stroke="{HOLE}" stroke-width="1.6"')
                    for y in (16.5, 24.5, 32.5, 40.5))
    return page + chart + rings

@reg("masterpdfeditor", RED)
def masterpdf():
    return stroke("M16 42L24.5 20.5L33 36.5L40 24.5L48 42", INK, 6)

@reg("mat", RED_DEEP)
def mat():
    board = rrect(14, 13.5, 36, 17, 4.5, INK)
    post = rrect(29, 29, 6, 18, 2, INK)
    letters = (stroke("M18.5 26V18L21.5 22L24.5 18V26", HOLE, 2.4) +
               stroke("M28.5 26L32 18L35.5 26M29.6 23.4H34.4", HOLE, 2.4) +
               stroke("M38.5 18H45.5M42 18V26", HOLE, 2.4))
    return board + post + letters

@reg("mate", BROWN_SOFT)
def mate():
    arcs = stroke(arc(35, 30, 13.5, -135, 135), INK, 4.2) + stroke(arc(35, 30, 7, -120, 120), INK, 3.6)
    tri_pts = [(17, 19), (34, 30), (17, 41)]
    return arcs + poly(tri_pts, HOLE, 7) + poly(tri_pts, INK, 2.5)

@reg("mate-inhibit-applet", ORANGE_DARK)
def mate_inhibit():
    pole = stroke("M14.5 16V45", INK, 3.4) + line(14.5, 16, 18, 16, INK, 3.4)
    board = rrect(19.5, 17, 31, 26, 4, INK)
    zz = stroke("M25 25H35L25 37H35", HOLE, 3.8) + stroke("M38.5 21H44L38.5 27.5H44", HOLE, 2.4)
    return pole + board + zz

@reg("mate-panel-drawer", AMBER_DEEP)
def mate_drawer():
    body = rrect(14, 15, 36, 30, 5, INK)
    face = rrect(18, 19, 28, 22, 3, AMBER_SOFT)
    handle = rrect(25.5, 28, 13, 4.5, 2.25, BROWN_DARK)
    return body + face + handle

@small("lsp-plugins")
def lsp_s():
    return (stroke("M17 19V41H27", INK, 5.5) +
            stroke("M45 22.5C43.8 20.3 41.7 19 39 19C35.5 19 33 21 33 24"
                   "C33 31 46 28 46 35.5C46 39 43 41 39 41C36.3 41 34 39.8 32.8 37.5", INK, 5.5))

@small("lyne")
def lyne_s():
    return "".join(diamond(x, y, 5, INK, 1) for x in (21, 32, 43) for y in (19, 30, 41))

@small("lvim")
def lvim_s():
    return (_ring(CX, CY, 15, INK, 3.6) + stroke("M23 22V38H29", INK, 4)
            + stroke("M32 22L36.5 38L41 22", INK, 4))

@small("makemkv")
def makemkv_s():
    disc = circle(32, 25, 14, INK) + circle(32, 25, 5, HOLE)
    return disc + rrect(15, 36, 34, 12, 3.5, INDIGO_SOFT)

@small("mat")
def mat_s():
    board = rrect(13, 12, 38, 21, 5, INK)
    post = rrect(28.5, 31, 7, 16, 2.5, INK)
    return board + post + stroke("M24 28V17.5L32 24L40 17.5V28", HOLE, 3.6)

@small("massif-visualizer")
def massif_s():
    page = rrect(18, 12, 31, 36, 4, INK)
    chart = poly([(22, 44), (29, 29), (34, 35), (40, 22), (45, 44)], HOLE, 2)
    return page + chart

@small("manjaro-architect")
def manjaro_architect_s():
    hash_ = (line(19.5, 14, 18.5, 28, INK, 3.4) + line(26, 14, 25, 28, INK, 3.4) +
             line(15, 19, 29.5, 19, INK, 3.4) + line(14.5, 24, 29, 24, INK, 3.4))
    badge = circle(39, 37, 11, TEAL_LIGHT)
    arrow = line(39, 30.5, 39, 43, INK, 3.8) + stroke("M34 38.5L39 43.5L44 38.5", INK, 3.8)
    return hash_ + badge + arrow

@small("manjaro-settings-manager")
def manjaro_settings_s():
    logo = (rrect(15, 13, 9, 34, 1.5, INK) + rrect(15, 13, 22, 9, 1.5, INK) +
            rrect(28, 26, 9, 21, 1.5, INK) + rrect(41, 13, 9, 34, 1.5, INK))
    return logo + circle(42.5, 40.5, 11, HOLE) + circle(42.5, 40.5, 9.5, DEEP_PURPLE_LIGHT) + circle(42.5, 40.5, 4, INK)

@small("lyrebird")
def lyrebird_s():
    tail = (stroke("M33 37C39 33 45 27 45 19C45 15.5 42.5 14 40 15.5", INK, 3.6) +
            stroke("M31 36C28 30 25.5 24.5 27.5 18.5C28.5 15.5 31.5 15.5 32 18", INK, 3.6))
    return tail + ell_e(26, 39, 9, 6, INK) + circle(18.5, 35, 4.2, INK)

@small("mate-panel-drawer")
def mate_drawer_s():
    return rrect(13, 15, 38, 30, 5, INK) + rrect(24, 27, 16, 6, 3, HOLE)

@small("lyx")
def lyx_s():
    return (stroke("M16 16V40H26", INK, 5.5) +
            stroke("M31.5 17L47 40M47 17L31.5 40", RED_SOFT, 5.5))

@small("mandelbulber2")
def mandelbulber_s():
    pts = []
    turns = 1.8
    for i in range(120):
        t = i / 119 * turns * 2 * math.pi
        r = 2 + 14 * t / (turns * 2 * math.pi)
        pts.append((CX + r * math.cos(t), CY + r * math.sin(t)))
    return stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts), INK, 4)

@small("marknoto")
def marknoto_s():
    note = path("M19 13H45A3 3 0 0 1 48 16V35L35 48H19A3 3 0 0 1 16 45V16A3 3 0 0 1 19 13Z", INK)
    code = stroke("M27 23L20.5 30L27 37", HOLE, 4) + stroke("M37 23L43.5 30L37 37", HOLE, 4)
    return note + code

@small("mate-inhibit-applet")
def mate_inhibit_s():
    return rrect(15, 15, 34, 30, 5, INK) + stroke("M23.5 22.5H40.5L23.5 38H40.5", HOLE, 5)

@small("mangareader")
def mangareader_s():
    arches = stroke("M17 40V24C17 20 19.5 17.5 23 17.5C26.5 17.5 29 20 29 24"
                    "M29 24C29 20 31.5 17.5 35 17.5C38.5 17.5 41 20 41 24V40", INK, 5)
    return arches + stroke("M29 44H45", INK, 4.4)
