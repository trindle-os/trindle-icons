# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 19: crayon-physics-deluxe to dangerous-golf.

Same kit and rules as batch01: palette tile nearest the brand colour,
mark in INK, HOLE for cut-throughs, a second shade only where the logo
really needs one.
"""
import math
from lm import *
from glyphs.kit import arc, ellipse_c, gear_f, registry, _ring, _star

ICONS, SMALL, reg, small = registry()

def frame(x, y, w, h, r, colour, sw):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(r)}" '
            f'fill="none" stroke="{colour}" stroke-width="{f(sw)}"/>')

@reg("crayon-physics-deluxe", AMBER)
def crayon_physics():
    return (poly(_star(32, 31, 17.5, 8), INK, 5) +
            poly(_star(32, 31.3, 11, 5), HOLE, 3))

@reg("crusader-kings-2", RED_DEEP)
def crusader_kings():
    shield = path("M17 14H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    cross = rrect(29.3, 17, 5.4, 27, 1, HOLE) + rrect(20.5, 24, 23, 5.4, 1, HOLE)
    return shield + cross

def _heart(cx, cy, s, rot, colour, extra=""):
    d = "M0 7C-9 1 -11 -5 -6 -8C-3 -9.6 -0.5 -8 0 -5.5C0.5 -8 3 -9.6 6 -8C11 -5 9 1 0 7Z"
    return g(path(d, colour, extra), f"translate({cx} {cy}) rotate({rot}) scale({s})")

@reg("crush-crush", PINK_LIGHT)
def crush_crush():
    back = _heart(25.5, 24, 1.3, -14, INK)
    front = _heart(38.5, 35.5, 1.3, 12, PINK_SOFT,
                   f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    return back + front

NECRO = ["..XXXXXXX..",
         ".XXXXXXXXX.",
         "XXXXXXXXXXX",
         "XXXXXXXXXXX",
         "XXeeXXXeeXX",
         "XXeeXXXeeXX",
         "XXXXX.XXXXX",
         ".XXXXXXXXX.",
         "..XXXXXXX..",
         "..X.X.X.X..",
         "..XXXXXXX.."]

def _necro(rows, u, x0, y0):
    out = ""
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            ch = row[c]
            if ch == ".":
                c += 1
                continue
            e = c
            while e < len(row) and row[e] == ch:
                e += 1
            col = INK if ch == "X" else PINK_SOFT
            out += f'<rect x="{f(x0 + c * u)}" y="{f(y0 + r * u)}" width="{f((e - c) * u + .05)}" height="{f(u + .05)}" fill="{col}"/>'
            c = e
    return out

@reg("crypt-of-the-necrodancer", PINK_DARK)
def necrodancer():
    return _necro(NECRO, 3, 15.5, 13.5)

def _cs_soldier():
    s = HOLE
    return (circle(29.6, 18.6, 2.9, s) +
            poly([(26.5, 22.3), (32, 22.3), (33, 32), (27, 32.5)], s, 2) +
            line(31, 23.6, 43.5, 23.6, s, 2.4) + line(28.5, 25, 35, 25.5, s, 2.8) +
            stroke("M28.3 31.5L25.6 37.5L24.2 44", s, 3.2) +
            stroke("M31.6 31.5L35 37.5L35.8 44", s, 3.2))

def _cs():
    return circle(CX, CY, 16.5, INK) + _cs_soldier()

@reg("cs", AMBER_DEEP)
def cs():
    return _cs()

@reg("cscz", YELLOW_DARK)
def cscz():
    return _cs()

@reg("csgo", GREY_DARK)
def csgo():
    return _cs()

@reg("css", BLUE_DEEP)
def css():
    return _cs()

@reg("cuphead", RED_DEEP)
def cuphead():
    head = circle(31, 33, 13.5, INK)
    top = ellipse_c(31, 22.5, 9.5, 3.4, RED_DARK, ) + ellipse_c(31, 22.5, 9.5, 3.4, INK, 2.2)
    straw = stroke("M33.5 22L38 12.5L45.5 14.5", INK, 3.4)
    eyes = ellipse_c(26.5, 32, 2.6, 4.3, HOLE) + ellipse_c(35.5, 32, 2.6, 4.3, HOLE)
    nose = circle(31, 38.5, 2.6, RED_LIGHT)
    return head + top + straw + eyes + nose

@reg("cuttlefish", AMBER_DEEP)
def cuttlefish():
    dome = path("M18 33C18 22 24 15 32 15C40 15 46 22 46 33Z", INK)
    arms = "".join(stroke(d, INK, 4.4) for d in [
        "M20 31C19.5 37 17 40 15.5 43", "M27 32C27 38 25.5 42 24 45.5",
        "M37 32C37 38 38.5 42 40 45.5", "M44 31C44.5 37 47 40 48.5 43"])
    eyes = (circle(27, 26, 3.6, HOLE) + circle(37, 26, 3.6, HOLE) +
            circle(27.8, 26.6, 1.7, INK) + circle(37.8, 26.6, 1.7, INK))
    return dome + arms + eyes

@reg("cuyo", BLUE_GREY_LIGHT)
def cuyo():
    head = path("M21.5 32V23A10.5 8.5 0 0 1 42.5 23V32Z", INK)
    body = rrect(14, 30, 36, 15, 7.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    eyes = (ellipse_c(27.5, 29.5, 3.2, 4.2, HOLE) + ellipse_c(36.5, 29.5, 3.2, 4.2, HOLE) +
            circle(27.5, 30.5, 1.8, INK) + circle(36.5, 30.5, 1.8, INK))
    return head + body + eyes

@reg("cyberpunk-2077", YELLOW)
def cyberpunk():
    x, y, w, h, gap = 15.4, 20.5, 6, 17, 3.4
    xs = [x + k * (w + gap) for k in range(4)]
    two = f"M{xs[0]} {y}H{xs[0] + w}V{y + h / 2}H{xs[0]}V{y + h}H{xs[0] + w}"
    zero = f"M{xs[1]} {y}H{xs[1] + w}V{y + h}H{xs[1]}Z"
    sev = lambda a: f"M{a} {y}H{a + w}L{a + 2} {y + h}"
    digits = "".join(stroke(d, INK, 3) for d in [two, zero, sev(xs[2]), sev(xs[3])])
    return digits + line(15.4, 44, 38, 44, CYAN, 2.6)

@reg("danganronpa", GREY)
def danganronpa():
    dark = BLUE_GREY_DARK
    left = circle(20.5, 18, 5.5, INK) + circle(32, 31, 15, INK)
    right = circle(43.5, 18, 5.5, dark) + path("M32 16A15 15 0 0 1 32 46Z", dark)
    muzzle = ellipse_c(32, 38, 7, 5, INK)
    nose = ellipse_c(32, 35, 2.4, 1.7, dark)
    eye_l = circle(25, 28, 2, dark)
    eye_r = poly([(35.5, 26.5), (43.5, 23), (40.5, 27.5), (44.5, 29.5), (36, 30)], RED, 1)
    return left + right + muzzle + nose + eye_l + eye_r

@reg("dangerous-golf", AMBER_DEEP)
def dangerous_golf():
    hole = ellipse_c(33, 41, 11, 4.6, INK) + ellipse_c(33, 41, 7, 2.4, HOLE)
    pin = line(34, 40, 34, 14, INK, 2.6) + poly([(34, 13.5), (45, 17.5), (34, 22)], INK, 1.5)
    burst = stroke("M16 35L20 27L24 33.5L28 27", INK, 3)
    return hole + pin + burst

@reg("cromite", TEAL_LIGHT)
def cromite():
    return (_ring(CX, CY, 13, INK, 5) + circle(CX, CY, 7, TEAL_DARK) +
            line(37, 25, 48, 14, HOLE, 4.2))

def _history(cx=32, cy=30, s=1.0):
    r = 11 * s
    th = math.radians(-150)
    px, py = cx + r * math.cos(th), cy + r * math.sin(th)
    d = (math.sin(th), -math.cos(th))
    rad = (math.cos(th), math.sin(th))
    tip = (px + 5.5 * s * d[0], py + 5.5 * s * d[1])
    bc = (px - 1.2 * s * d[0], py - 1.2 * s * d[1])
    c1 = (bc[0] + 4.8 * s * rad[0], bc[1] + 4.8 * s * rad[1])
    c2 = (bc[0] - 4.8 * s * rad[0], bc[1] - 4.8 * s * rad[1])
    return (stroke(arc(cx, cy, r, -150, 150), INK, 4 * s) + poly([tip, c1, c2], INK, 1.5) +
            stroke(f"M{f(cx)} {f(cy - 6 * s)}V{f(cy)}L{f(cx + 4.5 * s)} {f(cy + 3.5 * s)}", INK, 3 * s))

@reg("cronopete_preferences", GREY_DEEP)
def cronopete_prefs():
    return _history(33, 30, 1.35)

@reg("cronopete_restore", GREY_DEEP)
def cronopete_restore():
    badge = (circle(41, 40, 10, HOLE) + circle(41, 40, 8.3, BLUE) +
             stroke("M36.5 41.5C37 38.5 39 37 42.5 37", INK, 2.6) +
             poly([(42, 33.5), (46.5, 37), (42, 40.5)], INK, 1))
    return _history(29, 26.5, 1.2) + badge

@reg("crossover", DEEP_ORANGE_DEEP)
def crossover():
    a = path("M21 44C12.5 34 18 16 37.5 13.5C27.5 19 22.5 30 27 42Z", INK)
    return a + g(path("M21 44C12.5 34 18 16 37.5 13.5C27.5 19 22.5 30 27 42Z", BLUE_SOFT),
                 "rotate(180 32 29)")

@reg("crossstudio", BLUE_GREY_DEEP)
def crossstudio():
    back = stroke("M46.5 14.5C38 22 26 38 17.5 45.5", BLUE_GREY_SOFT, 6)
    up = stroke("M17.5 14.5C22 18.5 27 24 32 30", INK, 6)
    low = stroke("M32 30C37 36 42 41.5 46.5 45.5", ORANGE_LIGHT, 6)
    return back + up + low

@reg("crow-translate", LIGHT_BLUE_DARK)
def crow_translate():
    vane = path("M19 44C19.5 33 27 20 45.5 13C43 27 35 39 21.5 45.5Z", INK)
    notches = (poly([(30, 21), (27, 22.5), (31.5, 25)], HOLE) +
               poly([(40.5, 33), (43.5, 32), (38.5, 29.5)], HOLE))
    quill = stroke("M16 47.5L40.5 19", HOLE, 2.2) + line(16, 47.5, 20, 43, INK, 2.6)
    return vane + notches + quill

@reg("crunchyroll", DEEP_ORANGE_LIGHT)
def crunchyroll():
    return (circle(CX, CY, 16.5, INK) + circle(34.5, 28.5, 10.5, HOLE) +
            circle(38, 25, 4.8, INK))

@reg("cryptomator", INDIGO_SOFT)
def cryptomator():
    head = path("M21 27V22A11 10 0 0 1 43 22V27Z", INK)
    eyes = circle(27.5, 21, 2.1, HOLE) + circle(36.5, 21, 2.1, HOLE)
    shield = path("M19.5 26.5H44.5V35C44.5 41 38.5 45 32 47.5C25.5 45 19.5 41 19.5 35Z", INK,
                  f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    key = circle(32, 33.5, 2.9, HOLE) + poly([(30.4, 35), (33.6, 35), (34.5, 41.5), (29.5, 41.5)], HOLE, 1)
    return head + eyes + shield + key

@reg("cryptr", BLUE_GREY_DEEP)
def cryptr():
    body = rrect(15, 13, 34, 34, 6, INK)
    rivets = "".join(circle(x, y, 1.6, HOLE) for x in (19.3, 44.7) for y in (17.3, 42.7))
    door = rrect(21.5, 19.5, 21, 21, 3, HOLE)
    key = circle(32, 27, 3.6, INK) + poly([(30, 28.5), (34, 28.5), (35.3, 36.5), (28.7, 36.5)], INK, 1)
    return body + rivets + door + key

@reg("credentials-preferences", BLUE_GREY)
def credentials():
    cloud = (circle(24, 31, 8, INK) + circle(34.5, 26.5, 10.5, INK) + circle(43, 33, 6.5, INK) +
             rrect(16, 31, 33.5, 10.5, 5.25, INK))
    back = circle(37.5, 28.5, 2.6, HOLE) + path("M32.8 38.5A4.7 4.7 0 0 1 42.2 38.5Z", HOLE)
    front = (circle(29.5, 27.5, 3.3, INK) + circle(29.5, 27.5, 3.1, HOLE) +
             path("M23.5 39A6 6 0 0 1 35.5 39Z", HOLE))
    return cloud + back + front

@reg("cs-actions", BROWN_LIGHT)
def cs_actions():
    rows = "".join(rrect(15.5, y - 3, 6, 6, 1.5, INK) + rrect(25, y - 1.6, w, 3.2, 1.6, INK)
                   for y, w in [(17, 23), (27.5, 23), (38, 9)])
    pencil = (line(47, 31, 40.5, 37.5, INK, 5.2, "butt") +
              poly([(37.2, 44.8), (38.4, 38.2), (43.8, 43.6)], INK, 1.2))
    return rows + pencil

@reg("cs-applets", BLUE_DEEP)
def cs_applets():
    screen = frame(15.5, 15, 33, 30, 4, INK, 3)
    bar = path("M15.5 36H48.5V41A4 4 0 0 1 44.5 45H19.5A4 4 0 0 1 15.5 41Z", INK)
    keys = "".join(rrect(19.8 + k * 6.6, 38.3, 4.4, 4.4, 1, HOLE) for k in range(4))
    return screen + bar + keys

@reg("cs-desktop", BLUE_DEEP)
def cs_desktop():
    screen = frame(15.5, 14, 33, 29, 4, INK, 3)
    top = path("M15.5 18A4 4 0 0 1 19.5 14H44.5A4 4 0 0 1 48.5 18V21.5H15.5Z", INK)
    tab = rrect(25, 40, 14, 7, 2.5, INK)
    return screen + top + tab

@reg("cs-login", GREY_DARK)
def cs_login():
    out = ""
    for y in (17, 32):
        out += rrect(15, y, 34, 11, 3.5, INK)
        out += "".join(circle(22 + 7 * k, y + 5.5, 2.3, HOLE) for k in range(3))
    return out

def _sparkle(x, y, s):
    return poly([(x, y - s), (x + s * .28, y - s * .28), (x + s, y), (x + s * .28, y + s * .28),
                 (x, y + s), (x - s * .28, y + s * .28), (x - s, y), (x - s * .28, y - s * .28)], INK, .8)

@reg("cs-nightlight", INDIGO_DARK)
def cs_nightlight():
    moon = circle(33.5, 31.5, 11.5, INK)
    craters = (circle(29.5, 27.5, 2.7, INDIGO_SOFT) + circle(38, 34.5, 3, INDIGO_SOFT) +
               circle(30.5, 37, 1.8, INDIGO_SOFT))
    stars = _sparkle(18.5, 17.5, 4.2) + _sparkle(45.5, 15.5, 3) + _sparkle(18, 40, 2.8)
    return moon + craters + stars

@reg("cs-overview", BLUE)
def cs_overview():
    screen = frame(15.5, 15, 33, 30, 4, INK, 3)
    tl = path("M15.5 19A4 4 0 0 1 19.5 15H25.5A10 10 0 0 1 15.5 25Z", INK)
    br = path("M48.5 41A4 4 0 0 1 44.5 45H38.5A10 10 0 0 1 48.5 35Z", INK)
    return screen + tl + br

@reg("cs-panel", BLUE_DARK)
def cs_panel():
    screen = frame(15.5, 15, 33, 30, 4, INK, 3)
    bar = path("M15.5 37H48.5V41A4 4 0 0 1 44.5 45H19.5A4 4 0 0 1 15.5 41Z", INK)
    return screen + bar

@reg("cudatext-512", ORANGE_DEEP)
def cudatext():
    bracket = stroke("M41 15H24.5A5 5 0 0 0 19.5 20V40A5 5 0 0 0 24.5 45H41", INK, 4.6)
    u = stroke("M28.5 22.5V31.5A4.75 4.75 0 0 0 38 31.5", INK, 4) + line(38, 22.5, 38, 38, INK, 4)
    return bracket + u

@reg("cumulonimbus", YELLOW_LIGHT)
def cumulonimbus():
    return (stroke(arc(31, 30, 15, 40, 320), INK, 3.8) +
            stroke(arc(31, 30, 9.4, 40, 320), INK, 3.8) + circle(31, 30, 4, INK))

@reg("cups", GREY_DEEP)
def cups():
    paper_in = rrect(22, 13, 20, 12, 2, INK)
    body = rrect(15, 21, 34, 17, 4, INK, f' stroke="{HOLE}" stroke-width="2"')
    led = circle(20, 26, 1.9, HOLE)
    paper_out = rrect(21, 32, 22, 15, 2, INK, f' stroke="{HOLE}" stroke-width="2"')
    lines = rrect(25, 36.5, 14, 2.6, 1.3, HOLE) + rrect(25, 41, 9, 2.6, 1.3, HOLE)
    return paper_in + body + led + paper_out + lines

@reg("cura-icon", LIGHT_BLUE_DEEP)
def cura():
    body = poly([(22, 13.5), (48.5, 13.5), (48.5, 39), (42, 46.5), (15.5, 46.5), (15.5, 21)], INK, 3)
    c = stroke("M40.5 22.5H28.5A4 4 0 0 0 24.5 26.5V33.5A4 4 0 0 0 28.5 37.5H40.5", HOLE, 6)
    return body + c

@reg("curlew", LIGHT_BLUE)
def curlew():
    head = circle(29.5, 19, 3.4, INK)
    beak = stroke("M26.8 20C22.5 21.5 19 25.5 16.5 31", INK, 2.3)
    body = path("M26.5 20.5C25.5 25 25 28.5 26 32.5C27.5 37.5 32.5 40.5 38 39.5"
                "C42 38.8 45.5 36.8 49 35.5C45.5 32 41 28 35.5 27.3C32.5 27 31 25 32.5 20.5Z", INK)
    legs = line(32.5, 39, 31.5, 47, INK, 2.3) + line(36.5, 39, 38, 47, INK, 2.3)
    return head + beak + body + legs

@reg("cursor", BLUE_GREY_DARK)
def cursor():
    v = [pt(CX, CY, 17, -90 + 60 * k) for k in range(6)]
    hexa = poly(v, BLUE_GREY_LIGHT, 2.5)
    arrow = poly([v[5], v[1], v[3]], INK, 2)
    return hexa + arrow

@reg("custom-toolbox", GREY_DARK)
def custom_toolbox():
    tools = line(18, 15, 38, 35, INK, 4.4) + line(40, 15, 17, 38, INK, 4.4)
    blade = poly([(38, 12.5), (44, 15), (40, 19)], INK, 2)
    cog = (circle(41, 40, 10, HOLE) + gear_f(41, 40, 8.6, 6.4, 8, INK) + circle(41, 40, 2.6, HOLE))
    return tools + blade + cog

@reg("cutecom", BLUE_GREY_DEEP)
def cutecom():
    top = rrect(21, 13, 22, 11, 1.5, BLUE_GREY_SOFT)
    body = rrect(15, 20, 34, 25, 4, INK)
    lines = "".join(rrect(32 - w / 2, y, w, 3, 1.5, HOLE) for y, w in [(26, 22), (32, 16), (38, 10)])
    return top + body + lines

@reg("cutegram", RED_DEEP)
def cutegram():
    return poly([(46.5, 13.5), (17, 27.5), (30.5, 31), (34.5, 45)], INK, 3.5)

@reg("cutemarked", DEEP_ORANGE_LIGHT)
def cutemarked():
    box = rrect(13.5, 19, 37, 22, 4, INK)
    m = stroke("M19.5 35V25L24.5 30.5L29.5 25V35", HOLE, 3)
    arrow = line(40, 24.5, 40, 31, HOLE, 3) + poly([(35.5, 31), (44.5, 31), (40, 36)], HOLE, 1)
    return box + m + arrow

@reg("cutemaze", BROWN_LIGHT)
def cutemaze():
    walls = ["M35 15H16V45H48V15H42", "M23 21V39", "M23 21H36", "M42 21V39H29",
             "M29 27V39", "M36 27V33"]
    return "".join(stroke(d, INK, 3.4) for d in walls)

@reg("cutentr", GREY_DARK)
def cutentr():
    body = rrect(15, 13, 34, 34, 5, INK)
    screen = rrect(20, 17, 24, 13, 2, HOLE)
    pad = line(20.5, 38.5, 28.5, 38.5, HOLE, 2.8) + line(24.5, 34.5, 24.5, 42.5, HOLE, 2.8)
    btns = circle(37, 38.5, 2.2, HOLE) + circle(43, 38.5, 2.2, HOLE)
    return body + screen + pad + btns

@reg("cutepeaks", TEAL_DEEP)
def cutepeaks():
    up = poly([(15, 28.5), (23.5, 17), (32, 28.5)], INK, 2)
    down = poly([(15, 31.5), (32, 31.5), (23.5, 43)], CYAN_SOFT, 2)
    peak = poly([(32.5, 43), (41, 14), (49, 43)], INK, 2)
    return up + down + peak

@reg("cutter", GREY_DARK)
def cutter():
    rim = _ring(CX, CY, 15.5, INK, 3)
    slab = poly([(20, 39.5), (28.5, 20.5), (33, 20.5), (26.5, 39.5)], INK, 1.5)
    tri = (poly([(31, 30), (37, 25.3), (37, 34.7)], INK, 1.5) +
           poly([(37.5, 30), (43.5, 25.3), (43.5, 34.7)], INK, 1.5))
    return rim + slab + tri

@reg("cvpcb", GREY_DEEP)
def cvpcb():
    leads = (line(14.5, 23, 24, 23, INK, 3) + line(14.5, 37, 24, 37, INK, 3) +
             line(42, 30, 49.5, 30, INK, 3))
    amp = poly([(23, 15), (23, 45), (44, 30)], INK, 3)
    signs = (line(26.5, 23, 31.5, 23, HOLE, 2.4) + line(26.5, 37, 31.5, 37, HOLE, 2.4) +
             line(29, 34.5, 29, 39.5, HOLE, 2.4))
    return leads + amp + signs

@reg("cyan", BLUE_DARK)
def cyan():
    pick = path("M32 47.5C24 40.5 16 30.5 16 21.5C16 15.5 23 12.5 32 12.5C41 12.5 48 15.5 48 21.5"
                "C48 30.5 40 40.5 32 47.5Z", INK)
    c = stroke("M38.5 21C35 17.5 28.5 18.5 26.5 24.5C24.5 30.5 26.5 36.5 31.5 36.5"
               "C34.5 36.5 36.5 35 38 33", HOLE, 3.2)
    flourish = stroke("M38.5 21C40.5 18.5 38 16.5 35.5 18.5", HOLE, 2.4)
    return pick + c + flourish

@reg("cz.pervoj.valdo-gtk", ORANGE_DEEP)
def valdo():
    return (gear_f(CX, CY, 17, 13.5, 10, INK, 2) + circle(CX, CY, 10, HOLE) +
            stroke("M26.5 23.5L32 37L37.5 23.5", INK, 4))

@reg("d-feet", BLUE_GREY_DARK)
def d_feet():
    return _ring(35.5, 25.5, 8.5, INK, 4.6) + line(28.8, 32.2, 19, 42, INK, 6)

@reg("d-tracker", BROWN)
def d_tracker():
    caps = rrect(18.5, 12, 27, 4.6, 2.3, INK) + rrect(18.5, 43.4, 27, 4.6, 2.3, INK)
    glass = stroke("M22.5 17C22.5 24 29 26.5 29.5 30C29 33.5 22.5 36 22.5 43"
                   "M41.5 17C41.5 24 35 26.5 34.5 30C35 33.5 41.5 36 41.5 43", INK, 2.6)
    sand = poly([(26.5, 21.5), (37.5, 21.5), (32, 27.5)], INK, 1.5) + \
        path("M25.5 41.5C26 37.5 29.5 35 32 34C34.5 35 38 37.5 38.5 41.5Z", INK)
    return caps + glass + sand

@small("crypt-of-the-necrodancer")
def necrodancer_s():
    rows = [".XXXXX.",
            "XXXXXXX",
            "XeeXeeX",
            "XeeXeeX",
            "XXX.XXX",
            ".XXXXX.",
            ".X.X.X."]
    return _necro(rows, 4.8, 15.2, 13.2)

@small("cs")
def cs_s():
    return _cs_small()

def _cs_small():
    s = HOLE
    return (circle(CX, CY, 17, INK) + circle(28.5, 18, 3.8, s) +
            poly([(25, 22.5), (32, 22.5), (32.5, 32.5), (25.5, 33)], s, 2.4) +
            line(29, 24.5, 45, 24.5, s, 3.6) +
            stroke("M27 32L22.5 44", s, 4.4) + stroke("M31 32L36.5 44", s, 4.4))

for _n in ("cscz", "csgo", "css"):
    SMALL[_n] = _cs_small

@small("cumulonimbus")
def cumulonimbus_s():
    return stroke(arc(31, 30, 14, 40, 320), INK, 4.2) + circle(31, 30, 5.5, INK)

@small("cutemaze")
def cutemaze_s():
    walls = ["M34 15H16V45H48V15H42", "M25 23V37", "M25 23H39V37"]
    return "".join(stroke(d, INK, 3.6) for d in walls)

@small("cutemarked")
def cutemarked_s():
    box = rrect(13, 18, 38, 24, 4.5, INK)
    m = stroke("M19 36V24.5L24.5 31L30 24.5V36", HOLE, 3.4)
    arrow = poly([(35, 29), (45, 29), (40, 36.5)], HOLE, 1) + line(40, 23.5, 40, 30, HOLE, 3.4)
    return box + m + arrow

@small("cyberpunk-2077")
def cyberpunk_s():
    x, y, w, h, gap = 17, 20, 12, 20, 6
    sev = lambda a: f"M{a} {y}H{a + w}L{a + 3} {y + h}"
    return stroke(sev(x), INK, 4.4) + stroke(sev(x + w + gap), INK, 4.4)

@small("cs-login")
def cs_login_s():
    out = ""
    for y in (16, 32):
        out += rrect(14, y, 36, 12, 4, INK)
        out += "".join(circle(22 + 10 * k, y + 6, 2.8, HOLE) for k in range(3))
    return out

@small("cuttlefish")
def cuttlefish_s():
    dome = path("M17 34C17 22 23.5 14 32 14C40.5 14 47 22 47 34Z", INK)
    arms = "".join(stroke(d, INK, 4.6) for d in [
        "M21 32C20 38 17.5 41 16 44", "M32 33V46", "M43 32C44 38 46.5 41 48 44"])
    return dome + arms + circle(26.5, 26, 4, HOLE) + circle(37.5, 26, 4, HOLE)

@small("credentials-preferences")
def credentials_s():
    cloud = (circle(24, 31, 8, INK) + circle(34.5, 26.5, 10.5, INK) + circle(43, 33, 6.5, INK) +
             rrect(16, 31, 33.5, 10.5, 5.25, INK))
    return cloud + circle(32, 27.5, 3.8, HOLE) + path("M25 40A7 7 0 0 1 39 40Z", HOLE)

@small("cutter")
def cutter_s():
    slab = poly([(16, 43), (26.5, 17), (33, 17), (23, 43)], INK, 2)
    tri = (poly([(30.5, 30), (39.5, 22.5), (39.5, 37.5)], INK, 2) +
           poly([(39.5, 30), (48.5, 22.5), (48.5, 37.5)], INK, 2))
    return slab + tri

@small("cz.pervoj.valdo-gtk")
def valdo_s():
    return (gear_f(CX, CY, 17.5, 13, 8, INK, 2) + circle(CX, CY, 10, HOLE) +
            stroke("M26.5 23.5L32 37.5L37.5 23.5", INK, 4.2))
