# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 73: webcord to world-of-goo.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK; HOLE is the tile showing through; any other
shade is another step from the palette.
"""
from lm import *
from glyphs.kit import badge_e, _gear_m, registry, _ring

ICONS, SMALL, reg, small = registry()

def _win_squares(cx, cy, colour):
    out = ""
    for x in (cx - 4.3, cx + .7):
        for y in (cy - 4.3, cy + .7):
            out += rrect(x, y, 3.6, 3.6, .7, colour)
    return out

def _discord_pad(colour, hole):
    pad = path("M19 18.5C22.5 16.5 26 15.5 28.5 15.2L29.5 17.5C31.2 17.2 32.8 17.2 34.5 17.5"
               "L35.5 15.2C38 15.5 41.5 16.5 45 18.5C49 25 50.5 32 49.8 39"
               "C46.5 41.5 43.2 43 40 44L38 40.5C39.3 40 40.5 39.3 41.5 38.6"
               "C35.5 41.5 28.5 41.5 22.5 38.6C23.5 39.3 24.7 40 26 40.5L24 44"
               "C20.8 43 17.5 41.5 14.2 39C13.5 32 15 25 19 18.5Z", colour)
    eyes = (path("M26.3 26.5a3.3 3.7 0 1 0 0.01 0Z", hole) +
            path("M37.7 26.5a3.3 3.7 0 1 0 0.01 0Z", hole))
    return pad + eyes

@reg("webcord", BLUE_LIGHT)
def webcord():
    return _discord_pad(INK, HOLE)

@reg("wechat", LIGHT_BLUE)
def wechat():
    big = path("M27 13C18.7 13 13 18.4 13 25C13 28.6 14.8 31.6 17.6 33.7L16.5 38.5L21.8 35.8"
               "C23.4 36.3 25.2 36.6 27 36.6C35.3 36.6 41 31.4 41 25C41 18.4 35.3 13 27 13Z", INK)
    eyes = circle(22.5, 22.5, 2.2, HOLE) + circle(31.5, 22.5, 2.2, HOLE)
    small = path("M39.5 26.5C45.8 26.5 50.5 30.6 50.5 35.8C50.5 38.6 49.2 41 47 42.7L47.8 46.5"
                 "L43.6 44.4C42.3 44.8 41 45 39.5 45C33.2 45 28.5 40.9 28.5 35.8"
                 "C28.5 30.6 33.2 26.5 39.5 26.5Z", INK, f' stroke="{HOLE}" stroke-width="2.4"')
    eyes2 = circle(35.5, 34, 1.8, HOLE) + circle(43.5, 34, 1.8, HOLE)
    return big + eyes + small + eyes2

def _whatsapp():
    ring_ = (path("M32 14A16 16 0 1 1 23.6 43.6L15.5 46L18 38A16 16 0 0 1 32 14Z", INK) +
             path("M32 17.5A12.5 12.5 0 1 1 25.2 40.5L20.8 41.8L22.1 37.4A12.5 12.5 0 0 1 32 17.5Z", HOLE))
    phone = path("M26 24.5C26.5 23.2 27.5 22.8 28.5 23L30.2 26.8C30.3 27.4 29.7 28.3 29.2 28.8"
                 "C30.3 31.2 32.3 33.2 34.7 34.3C35.2 33.8 36.1 33.2 36.7 33.3L40.5 35"
                 "C40.7 36 40.3 37 39 37.5C34.5 39 24.5 29 26 24.5Z", INK)
    return ring_ + phone

@reg("whatsie", CYAN)
def whatsie():
    return _whatsapp()

@reg("wemeet", BLUE)
def wemeet():
    left = stroke("M16 36.5L24 24L31.5 36.5", BLUE_SOFT, 6.5)
    right = stroke("M24.5 36.5L32 24L40 36.5L48 24", INK, 6.5)
    return left + right

@reg("whalebird", TEAL_LIGHT)
def whalebird():
    body = path("M17 38C16 28 22 17 34 15C41 14 47 18 47 24C47 21 44 20 42 21"
                "C45 27 42 34 36 37C30 40 24 40 21 44C19.5 42 18.5 40.5 17 38Z", INK)
    tail = path("M21 44C18 42 15 42 13.5 44C16 44.5 17.5 46 18 48.5C19 46.5 20 45.5 21 44Z", INK,
                f' stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"')
    fin = path("M28 34C26.5 37.5 23.5 39.5 21 40C24 36 25 33 28 34Z", HOLE)
    eye = circle(38, 21.5, 1.8, HOLE)
    return body + tail + fin + eye

@reg("wire", GREY_SOFT)
def wire():
    u = stroke("M18 17V33.5A7 7 0 0 0 32 33.5A7 7 0 0 0 46 33.5V17", INK, 3.6)
    loop = stroke("M32 33.5V21.5A3.2 3.2 0 0 0 25.6 21.5V33.5", INK, 3.6)
    loop2 = stroke("M32 33.5V21.5A3.2 3.2 0 0 1 38.4 21.5V33.5", INK, 3.6)
    return g(u + loop + loop2, "translate(0 1)")

@reg("webtorrent-desktop", RED_DEEP)
def webtorrent():
    hexa = [pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)]
    hexi = [pt(CX, CY, 12.5, -90 + 60 * k) for k in range(6)]
    d = ("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexa) + "Z" +
         "M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexi) + "Z")
    shell = cut(d, INK) + path(d.split("Z")[0] + "Z", "none",
                               f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    heart = path("M32 39C26 34.5 23.5 31.5 23.5 28C23.5 25.3 25.5 23.3 28 23.3C29.8 23.3 31.2 24.3 32 25.8"
                 "C32.8 24.3 34.2 23.3 36 23.3C38.5 23.3 40.5 25.3 40.5 28C40.5 31.5 38 34.5 32 39Z", INK)
    return shell + heart

@reg("wicd", GREY_DARK)
def wicd():
    fan = path("M14 22A26 26 0 0 1 50 22L32 43Z", INK,
               f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    arcs = (stroke("M19.5 25.5A19 19 0 0 1 44.5 25.5", HOLE, 2.4) +
            stroke("M24.5 30.5A12 12 0 0 1 39.5 30.5", HOLE, 2.4))
    return g(fan + arcs, "translate(0 -1)")

@reg("wihotspot", DEEP_PURPLE_SOFT)
def wihotspot():
    screen = rrect(16, 15, 32, 23, 3, INK)
    base = path("M12.5 40.5H51.5L49.5 45H14.5Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    wifi = (stroke("M24 25.5A11.5 11.5 0 0 1 40 25.5", HOLE, 3) +
            stroke("M27.8 29.3A6 6 0 0 1 36.2 29.3", HOLE, 3) + circle(32, 33, 2, HOLE))
    return screen + base + wifi

@reg("winbox", BLUE)
def winbox():
    disc_ = circle(CX, CY, 17, INK)
    arcs = "".join(stroke(f"M{f(47 - r)} 13A{r} {r} 0 0 0 49 {f(15 + r)}", HOLE, 2.8)
                   for r in (9, 16, 23))
    return disc_ + arcs

@reg("windscribe", BLUE_GREY_DARK)
def windscribe():
    hexo = [pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)]
    hexi = [pt(CX, CY, 13.5, -90 + 60 * k) for k in range(6)]
    d = ("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexo) + "Z" +
         "M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexi) + "Z")
    shell = cut(d, INK)
    w = stroke("M23 23.5L26.5 36.5L32 29.5L37.5 36.5L41 23.5", INK, 3.8)
    return shell + w

@reg("wikipedia", GREY_SOFT)
def wikipedia():
    w = stroke("M16.5 19L24 42L32 23L40 42L47.5 19", INK, 3.2)
    serifs = (line(13, 18, 21, 18, INK, 2.4) + line(28, 18, 36, 18, INK, 2.4) +
              line(43, 18, 51, 18, INK, 2.4))
    return w + serifs

@reg("wordpress", BLUE_DARK)
def wordpress():
    ring_ = _ring(CX, CY, 15.5, INK, 2.6)
    w = stroke("M20.5 23L26 40L32 27L38 40L43.5 23", INK, 3.6)
    return ring_ + w

@reg("wireshark", BLUE_DEEP)
def wireshark():
    return stroke("M14 41H24C28.5 41 29 19 35 19C38.5 19 36.5 31 42.5 41H50", INK, 4)

def _glass(dx=-5, dy=0):
    glass = path("M24 13H40C40.7 21 38.5 28.5 32 30C25.5 28.5 23.3 21 24 13Z", INK)
    wine_ = path("M24.5 18.5H39.5C39.3 23.5 37 28 32 28.8C27 28 24.7 23.5 24.5 18.5Z", RED_SOFT)
    stem = line(32, 30, 32, 43, INK, 3) + line(25.5, 44.5, 38.5, 44.5, INK, 3.4)
    return g(glass + wine_ + stem, f"translate({dx} {dy})")

@reg("wine-help", RED_DARK)
def wine_help():
    q = stroke("M38.5 37A3.5 3.5 0 1 1 42.5 40.2V41.5", INK, 2.6) + circle(42.5, 45.8, 1.5, INK)
    return _glass() + badge_e(42, 40, LIGHT_BLUE_DEEP) + q

@reg("wine-uninstaller", RED_DARK)
def wine_uninstaller():
    x = line(38.5, 36.5, 45.5, 43.5, INK, 2.8) + line(45.5, 36.5, 38.5, 43.5, INK, 2.8)
    return _glass() + badge_e(42, 40, PINK) + x

@reg("winecfg", RED_DARK)
def winecfg():
    gear = _gear_m(42, 40, 6.6, 4.9, 7, INK) + circle(42, 40, 2.1, GREY_DEEP)
    return _glass() + badge_e(42, 40, GREY_DEEP) + gear

@reg("winetricks", RED_DARK)
def winetricks():
    star = poly([pt(42, 40.5, 6 if k % 2 == 0 else 2.6, -90 + 36 * k) for k in range(10)], INK, 1)
    return _glass() + badge_e(42, 40, ORANGE_DEEP) + star

@reg("wine-launcher", BLUE_GREY_DARK)
def wine_launcher():
    pad = path("M22 20H42C47.5 20 50.5 25 50.5 32C50.5 39 48 42.5 45 42.5C42 42.5 40.5 38.5 38 38.5"
               "H26C23.5 38.5 22 42.5 19 42.5C16 42.5 13.5 39 13.5 32C13.5 25 16.5 20 22 20Z", INK)
    dpad = line(21, 29, 28, 29, HOLE, 2.6, "butt") + line(24.5, 25.5, 24.5, 32.5, HOLE, 2.6, "butt")
    btn = (circle(39, 26.5, 1.9, HOLE) + circle(43, 30, 1.9, HOLE) +
           circle(35, 30, 1.9, HOLE) + circle(39, 33.5, 1.9, HOLE))
    return pad + dpad + btn

@reg("winefile", GREY_DEEP)
def winefile():
    tabs = rrect(17, 13, 26, 8, 2, AMBER) + rrect(17, 17, 26, 6, 2, BLUE_SOFT)
    box = rrect(14, 21, 32, 25, 3, INK)
    handle = rrect(22, 29, 12, 3.4, 1.7, HOLE)
    return tabs + box + handle + badge_e(43, 40, BLUE) + _win_squares(43, 40, INK)

@reg("winemine", GREY_DARK)
def winemine():
    gear = cut(("M" + "L".join(f"{f(x)} {f(y)}" for x, y in _gear_pts(29, 28, 16, 12, 8)) + "Z")
               + cpath(29, 28, 5.5), INK)
    return gear + badge_e(43, 40, BLUE) + _win_squares(43, 40, INK)

def _gear_pts(cx, cy, ro, ri, n):
    pts = []
    for k in range(n):
        a = 360 / n * k
        for da, r in [(-.24, ri), (-.13, ro), (.13, ro), (.24, ri)]:
            pts.append(pt(cx, cy, r, a + da * 360 / n))
    return pts

@reg("woeusbgui-icon", GREY_DARK)
def woeusbgui():
    plug = rrect(21, 12, 18, 11, 2, INK) + rrect(24.5, 15, 4, 3.5, .8, HOLE) + rrect(31.5, 15, 4, 3.5, .8, HOLE)
    body = rrect(16, 23, 28, 24, 4, INK)
    slots = rrect(20, 29, 12, 2.8, 1.4, HOLE) + rrect(20, 34.5, 8, 2.8, 1.4, HOLE)
    return plug + body + slots + badge_e(43, 40, BLUE) + _win_squares(43, 40, INK)

@reg("welcome-screen", BLUE_DEEP)
def welcome_screen():
    pole = rrect(29.5, 11, 5, 38, 2.5, INK)
    board = rrect(13, 19, 38, 14, 3, INK)
    txt = rrect(18, 24.5, 28, 3, 1.5, HOLE)
    return pole + board + txt

@reg("windows95", BLUE_GREY_DARK)
def windows95():
    return (rrect(15, 13, 16, 16, 2.5, RED) + rrect(33, 13, 16, 16, 2.5, INDIGO_SOFT) +
            rrect(15, 31, 16, 16, 2.5, BLUE) + rrect(33, 31, 16, 16, 2.5, ORANGE_LIGHT))

@reg("wingpanel", BLUE_DEEP)
def wingpanel():
    frame = rrect(14, 15, 36, 30, 4, "none", f' stroke="{INK}" stroke-width="3"')
    bar = path("M14 19A4 4 0 0 1 18 15H46A4 4 0 0 1 50 19V22H14Z", INK,
               f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return frame + bar

def _switcher(active):
    out = ""
    for i, (x, y) in enumerate([(15, 13), (33, 13), (15, 31), (33, 31)]):
        if i == active:
            out += rrect(x, y, 16, 16, 3, INK)
        else:
            out += rrect(x + 1.3, y + 1.3, 13.4, 13.4, 2.2, "none", f' stroke="{INK}" stroke-width="2.6"')
    return out

@reg("workspace-switcher-top-left", BLUE_DEEP)
def ws_tl():
    return _switcher(0)

@reg("workspace-switcher-right-top", BLUE_DEEP)
def ws_rt():
    return _switcher(1)

@reg("workspace-switcher-left-bottom", BLUE_DEEP)
def ws_lb():
    return _switcher(2)

@reg("workspace-switcher-right-bottom", BLUE_DEEP)
def ws_rb():
    return _switcher(3)

@reg("wordpad", BLUE_GREY)
def wordpad():
    sheet = rrect(17, 11, 30, 38, 3.5, INK)
    lines = "".join(rrect(21.5, y, 21, 2.6, 1.3, HOLE) for y in (17, 22.5, 28, 33.5))
    return sheet + lines + rrect(21.5, 39, 13, 2.6, 1.3, HOLE)

@reg("words", GREY_DEEP)
def words():
    nib = path("M32 12L41 27C41 31 38 34 36 35.5V40H28V35.5C26 34 23 31 23 27Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    slit = line(32, 18, 32, 27, HOLE, 2.2) + circle(32, 29, 2.4, HOLE)
    band = rrect(26, 41, 12, 3.4, 1.7, ORANGE)
    grip = rrect(27, 45.5, 10, 4, 1.5, INK)
    return nib + slit + band + grip

@reg("workflowy", BLUE_DARK)
def workflowy():
    out = ""
    for cx, y in [(20, 19), (25.5, 30), (20, 41)]:
        out += rrect(cx, y - 2.2, 48 - cx - 2, 4.4, 2.2, BLUE_SOFT) + circle(cx, y, 4.6, INK)
    return out

@reg("webplotdigitizer", LIGHT_BLUE_DEEP)
def webplotdigitizer():
    grid = (line(24, 12.5, 24, 47.5, LIGHT_BLUE_SOFT, 2.2) + line(13, 22, 51, 22, LIGHT_BLUE_SOFT, 2.2))
    curve = stroke("M17 42C27 42 26 19 45 17", INK, 3.4)
    knots = circle(17, 42, 3.3, INK) + circle(45, 17, 3.3, INK)
    sigma = stroke("M47 30H38.5L43 36.5L38.5 43H47", INK, 2.8)
    return grid + curve + knots + sigma

@reg("webstorm", LIGHT_BLUE_DEEP)
def webstorm():
    sq = rrect(15, 13, 34, 34, 3, INK)
    w = stroke("M19.5 18.5L21.5 29.5L24.5 22L27.5 29.5L29.5 18.5", HOLE, 2.6)
    s = stroke("M43 19.5C42 18.5 41 18.3 39.5 18.3C37.5 18.3 36 19.3 36 21.2C36 25 43.5 23.5 43.5 27"
               "C43.5 28.8 42 29.8 39.8 29.8C38.2 29.8 36.8 29.3 35.8 28.3", HOLE, 2.6)
    bar = rrect(19, 38.5, 13, 3.2, 1, HOLE)
    return sq + w + s + bar

@reg("weka", INDIGO)
def weka():
    body = path("M14 33C15 25 23 20.5 31 21.5C33 17 36 14 40.5 14.5C44 15 45.5 17.5 45.5 19"
                "L50 21L45 22C44 25 42 28.5 42 32C42 38 36 42.5 29 42C22 41.5 17 38 14 33Z", INK)
    legs = stroke("M28 41.5L25.5 48M33 41.5L34.5 48", INK, 2.6)
    eye = circle(40.8, 18.3, 1.6, HOLE)
    wing = stroke("M20 33C25 35 31 34.5 35 30", HOLE, 2.2)
    return body + legs + eye + wing

@reg("welle.io", BROWN_DEEP)
def welle_io():
    aerial = line(19, 19, 42, 11.5, INK, 2.4)
    box = rrect(13, 18, 38, 28, 4, INK)
    spk = circle(25, 32, 8.5, HOLE) + circle(25, 32, 4, INK)
    knobs = rrect(37, 23, 10, 4, 1.2, DEEP_ORANGE_LIGHT) + circle(39.5, 33, 2.4, HOLE) + circle(44.5, 33, 2.4, HOLE)
    keys = rrect(37, 38.5, 10, 3.5, 1.2, HOLE)
    return aerial + box + spk + knobs + keys

@reg("whatpulse", AMBER_DARK)
def whatpulse():
    pie = path("M15 33H49A17 15 0 0 1 15 33Z", INK)
    cuts = line(32, 33, 32, 48.5, HOLE, 2) + line(32, 33, 20.5, 45, HOLE, 2)
    arrow = stroke("M15 28L24 20L30 25L42 14", INK, 3.6)
    head = poly([(36.5, 13), (45, 11.5), (43.5, 20)], INK, 2)
    return pie + cuts + arrow + head

@reg("widelands", ORANGE_DARK)
def widelands():
    u = stroke("M18 14V38H36V16", INK, 5.5)
    l = stroke("M28 22V44H46", DEEP_ORANGE_LIGHT, 5.5)
    return u + l

@reg("wings3d", RED_DEEP)
def wings3d():
    out = ""
    for cx, cy in [(22, 20), (32, 30), (42, 40)]:
        top = poly([(cx, cy - 7), (cx + 7, cy - 3.5), (cx, cy), (cx - 7, cy - 3.5)], INK, 1.5)
        left = poly([(cx - 7, cy - 3.5), (cx, cy), (cx, cy + 7), (cx - 7, cy + 3.5)], RED_SOFT, 1.5)
        right = poly([(cx + 7, cy - 3.5), (cx, cy), (cx, cy + 7), (cx + 7, cy + 3.5)], RED_DARK, 1.5)
        out += top + left + right
    return out

@reg("wiznote", CYAN_DEEP)
def wiznote():
    return poly([(14, 17), (22, 16), (25, 32), (30, 20), (35.5, 20), (38, 31), (42, 14), (50, 16),
                 (42, 44), (36, 44), (32.5, 32.5), (28, 44), (22, 44)], INK, 2.5)

@reg("wordview", BLUE)
def wordview():
    w = stroke("M15 17L21.5 41L28.5 23L35.5 41L42 17", INK, 5)
    eye = (path("M34.5 40.5C36.5 37 39 35.5 42 35.5C45 35.5 47.5 37 49.5 40.5"
                "C47.5 44 45 45.5 42 45.5C39 45.5 36.5 44 34.5 40.5Z", INK) +
           circle(42, 40.5, 2.4, RED_DEEP))
    return w + badge_e(42, 40.5, RED_DEEP, 9.5) + eye

@reg("wolfenstein", RED_DARK)
def wolfenstein():
    left = poly([(17, 17), (22, 12), (25, 17), (25, 40), (21, 47), (17, 40)], INK, 1.5)
    right = poly([(47, 17), (42, 12), (39, 17), (39, 40), (43, 47), (47, 40)], INK, 1.5)
    mid = poly([(28.5, 18), (32, 12), (35.5, 18), (35.5, 42), (32, 48), (28.5, 42)], INK, 1.5)
    bar = rrect(14, 27.5, 36, 4.5, 1, INK)
    return left + right + mid + bar

@reg("wolfram-language", RED)
def wolfram_language():
    head = poly([(22, 12), (27.5, 21), (33, 21), (37, 12), (39.5, 23), (49, 37.5), (45, 42),
                 (36, 38.5), (33, 47), (24, 42), (17, 34)], INK, 2.5)
    eye = poly([(33.5, 27), (38, 27), (36.5, 29.5)], HOLE, 1)
    return head + eye

@reg("wolfram-player", RED_DEEP)
def wolfram_player():
    star = poly([pt(CX, CY, 17.5 if k % 2 == 0 else 13.5, -90 + 15 * k) for k in range(24)], INK, 1.5)
    spiral = stroke("M32 30.5A2 2 0 0 1 36 30.5A4 4 0 0 1 28 30.5A6.5 6.5 0 0 1 41 30.5"
                    "A9 9 0 0 1 23 31", HOLE, 2.4)
    return star + spiral

@reg("wootility", GREY_DARK)
def wootility():
    frame = rrect(13.5, 14.5, 37, 31, 4, "none", f' stroke="{INK}" stroke-width="3"')
    cap = path("M20 21H24.5L26.5 27.5H29L30.5 21H33.5L35 27.5H37.5L39.5 21H44V38H20Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return frame + cap

@reg("workrave", BROWN)
def workrave():
    wool = "".join(circle(x, y, 7, INK) for x, y in
                   [(24, 17.5), (32, 15), (40, 17.5), (18.5, 25), (45.5, 25),
                    (19, 34), (45, 34), (25, 41), (32, 43), (39, 41)])
    wool += circle(CX, 29, 13, INK)
    face = path("M22 30C22 25 26 23 32 23C38 23 42 25 42 30C42 35 37.5 38 32 38"
                "C26.5 38 22 35 22 30Z", BROWN_SOFT)
    eyes = circle(28, 29, 1.9, BROWN_DARK) + circle(36, 29, 1.9, BROWN_DARK)
    return wool + face + eyes

@reg("world-of-goo", GREY_SOFT)
def world_of_goo():
    ball = circle(32, 32, 15.5, INK)
    eyes = (circle(23.5, 26, 6, HOLE) + circle(40.5, 26, 6, HOLE) +
            circle(25, 27, 2.4, INK) + circle(39, 27, 2.4, INK))
    return ball + eyes

@reg("wesnoth", AMBER_DEEP)
def wesnoth():
    return _wesnoth()

@reg("wesnoth_editor", BLUE_DEEP)
def wesnoth_editor():
    return _wesnoth()

def _wesnoth():
    shield = path("M19 17H45V30C45 38 39.5 43.5 32 47C24.5 43.5 19 38 19 30Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    blades = line(22.5, 20, 41.5, 44, HOLE, 3.2) + line(41.5, 20, 22.5, 44, HOLE, 3.2)
    guards = line(14, 16, 21.5, 11, INK, 3.4) + line(50, 16, 42.5, 11, INK, 3.4)
    hilts = line(16, 12, 20, 16.5, INK, 3.2) + line(48, 12, 44, 16.5, INK, 3.2)
    return shield + blades + guards + hilts

def _sbadge(colour):
    return circle(42.5, 40.5, 10, HOLE) + circle(42.5, 40.5, 8.5, colour)

def _sglass():
    glass = path("M20 12H36C36.7 20 34.5 27.5 28 29C21.5 27.5 19.3 20 20 12Z", INK)
    return glass + line(28, 29, 28, 43, INK, 4) + line(21, 45, 35, 45, INK, 4.4)

@small("webstorm")
def webstorm_s():
    return (rrect(14, 12, 36, 36, 3, INK) + stroke("M19 18L21.5 31L25 23L28.5 31L31 18", HOLE, 3) +
            stroke("M44.5 19.5C43.5 18.5 42.3 18 40.5 18C38.2 18 36.5 19.2 36.5 21.3"
                   "C36.5 25.5 45 24 45 28C45 30 43.2 31.2 40.8 31.2C39 31.2 37.5 30.6 36.3 29.4", HOLE, 3)
            + rrect(19, 38, 14, 4.5, 1.2, HOLE))

@small("webtorrent-desktop")
def webtorrent_s():
    hexa = [pt(CX, CY, 18, -90 + 60 * k) for k in range(6)]
    return poly(hexa, INK, 3) + path(
        "M32 40C25 35 22 31.5 22 27.5C22 24.5 24.2 22.2 27 22.2C29 22.2 31 23.4 32 25.2"
        "C33 23.4 35 22.2 37 22.2C39.8 22.2 42 24.5 42 27.5C42 31.5 39 35 32 40Z", HOLE)

@small("wechat")
def wechat_s():
    big = path("M26 13C18 13 12.5 18.4 12.5 25C12.5 28.6 14.3 31.6 17.1 33.7L16 38.5L21.3 35.8"
               "C22.9 36.3 24.2 36.6 26 36.6C34 36.6 39.5 31.4 39.5 25C39.5 18.4 34 13 26 13Z", INK)
    sm = path("M40 27C46 27 51 31 51 36.2C51 39 49.7 41.4 47.5 43L48.3 47L44 44.8"
              "C42.7 45.2 41.5 45.4 40 45.4C34 45.4 29 41.3 29 36.2C29 31 34 27 40 27Z", INK,
              f' stroke="{HOLE}" stroke-width="3"')
    return big + circle(21, 22.5, 2.8, HOLE) + circle(31, 22.5, 2.8, HOLE) + sm

@small("webplotdigitizer")
def webplotdigitizer_s():
    return (stroke("M16 43C27 43 25 18 47 16", INK, 4) + circle(16, 43, 4.2, INK) + circle(47, 16, 4.2, INK) +
            stroke("M48 30H38.5L43 37L38.5 44H48", INK, 3))

@small("wesnoth")
def wesnoth_s():
    return _wesnoth_s()

@small("wesnoth_editor")
def wesnoth_editor_s():
    return _wesnoth_s()

def _wesnoth_s():
    shield = path("M17 14H47V29C47 38 40.5 44 32 48C23.5 44 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return shield + line(23, 19, 41, 42, HOLE, 3.6) + line(41, 19, 23, 42, HOLE, 3.6)

@small("whatpulse")
def whatpulse_s():
    return (path("M14 33H50A18 15.5 0 0 1 14 33Z", INK) +
            stroke("M14 27L23 19L29.5 24.5L44 13", INK, 4.2) + poly([(37.5, 12), (47, 10.5), (45.5, 20)], INK, 2))

@small("wicd")
def wicd_s():
    return path("M13 21A27 27 0 0 1 51 21L32 44Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"') + \
        stroke("M21 27.5A16 16 0 0 1 43 27.5", HOLE, 3)

@small("wireshark")
def wireshark_s():
    return stroke("M13 42H22C28 42 28 17 35 17C39 17 37 31 44 42H51", INK, 4.4)

@small("wordpress")
def wordpress_s():
    return (circle(CX, CY, 17.5, INK) +
            stroke("M20.5 22L26 41L32 27L38 41L43.5 22", HOLE, 4))

@small("winbox")
def winbox_s():
    return circle(CX, CY, 17.5, INK) + "".join(
        stroke(f"M{f(47 - r)} 13A{r} {r} 0 0 0 49 {f(15 + r)}", HOLE, 3.2) for r in (12, 22))

@small("windscribe")
def windscribe_s():
    hexa = [pt(CX, CY, 18, -90 + 60 * k) for k in range(6)]
    return poly(hexa, INK, 3) + stroke("M21.5 23L25.5 37.5L32 29.5L38.5 37.5L42.5 23", HOLE, 4)

def _wine_s(sym, colour):
    return _sglass() + _sbadge(colour) + sym

@small("wine-help")
def wine_help_s():
    return _wine_s(stroke("M39 37.5A3.6 3.6 0 1 1 42.8 40.6V41.5", INK, 2.8) + circle(42.8, 46, 1.6, INK), LIGHT_BLUE_DEEP)

@small("wine-uninstaller")
def wine_uninstaller_s():
    return _wine_s(line(39, 37, 46, 44, INK, 3) + line(46, 37, 39, 44, INK, 3), PINK)

@small("winecfg")
def winecfg_s():
    return _wine_s(circle(42.5, 40.5, 4.5, INK) + circle(42.5, 40.5, 1.8, AMBER_DARK), AMBER_DARK)

@small("winetricks")
def winetricks_s():
    return _wine_s(poly([pt(42.5, 41, 6 if k % 2 == 0 else 2.8, -90 + 36 * k) for k in range(10)], INK, 1),
                   ORANGE_DEEP)

def _swin():
    return _sbadge(BLUE) + rrect(38, 36, 9, 9, 1.5, INK) + line(42.5, 36, 42.5, 45, BLUE, 1.6, "butt") + \
        line(38, 40.5, 47, 40.5, BLUE, 1.6, "butt")

@small("winefile")
def winefile_s():
    return rrect(13, 14, 30, 30, 3.5, INK) + rrect(19, 24, 14, 4.5, 2.2, HOLE) + _swin()

@small("winemine")
def winemine_s():
    gear = cut(("M" + "L".join(f"{f(x)} {f(y)}" for x, y in _gear_pts(28, 27, 16, 11.5, 7)) + "Z")
               + cpath(28, 27, 5), INK)
    return gear + _swin()

@small("woeusbgui-icon")
def woeusbgui_s():
    return (rrect(20, 11, 18, 10, 2, INK) + rrect(15, 21, 28, 26, 4, INK) +
            rrect(19, 28, 12, 4, 2, HOLE) + _swin())

@small("wine-launcher")
def wine_launcher_s():
    pad = path("M21 18H43C48.5 18 51.5 24 51.5 32C51.5 40 49 44 45.5 44C42 44 40.5 39.5 38 39.5"
               "H26C23.5 39.5 22 44 18.5 44C15 44 12.5 40 12.5 32C12.5 24 15.5 18 21 18Z", INK)
    return pad + line(20, 29, 29, 29, HOLE, 3.4, "butt") + line(24.5, 24.5, 24.5, 33.5, HOLE, 3.4, "butt") + \
        circle(38, 26, 2.6, HOLE) + circle(43, 31.5, 2.6, HOLE)

@small("wolfenstein")
def wolfenstein_s():
    bars = "".join(poly([(x - 4, 17), (x, 11), (x + 4, 17), (x + 4, 41), (x, 47), (x - 4, 41)], INK, 1)
                   for x in (19, 32, 45))
    return bars + rrect(13, 27, 38, 5, 1, INK)

@small("wolfram-language")
def wolfram_language_s():
    return poly([(21, 11), (27.5, 21), (33, 21), (37.5, 11), (40, 23), (50, 37.5), (45.5, 43),
                 (36, 39), (33, 48), (23, 42), (15.5, 33)], INK, 2.5)

@small("wolfram-player")
def wolfram_player_s():
    star = poly([pt(CX, CY, 18 if k % 2 == 0 else 14, -90 + 22.5 * k) for k in range(16)], INK, 1.5)
    return star + stroke("M33 30A3 3 0 0 1 27 30A6.5 6.5 0 0 1 40 30.5", HOLE, 3.2)

@small("workflowy")
def workflowy_s():
    return "".join(rrect(cx, y - 2.5, 49 - cx, 5, 2.5, BLUE_SOFT) + circle(cx, y, 5.5, INK)
                   for cx, y in [(19, 18), (26, 30), (19, 42)])

@small("workrave")
def workrave_s():
    wool = "".join(circle(x, y, 8, INK) for x, y in
                   [(22, 18), (32, 14.5), (42, 18), (18, 29), (46, 29), (22, 40), (32, 43.5), (42, 40)])
    return wool + circle(CX, 29, 14, INK) + path(
        "M21 30C21 24.5 25.5 22.5 32 22.5C38.5 22.5 43 24.5 43 30C43 35.5 38 38.5 32 38.5"
        "C26 38.5 21 35.5 21 30Z", BROWN_SOFT) + circle(27.5, 29, 2.3, BROWN_DARK) + circle(36.5, 29, 2.3, BROWN_DARK)

def _sswitch(active):
    return "".join(rrect(x, y, 16, 16, 3, INK if i == active else BLUE_DARK)
                   for i, (x, y) in enumerate([(14.5, 12.5), (33.5, 12.5), (14.5, 31.5), (33.5, 31.5)]))

@small("workspace-switcher-top-left")
def ws_tl_s():
    return _sswitch(0)

@small("workspace-switcher-right-top")
def ws_rt_s():
    return _sswitch(1)

@small("workspace-switcher-left-bottom")
def ws_lb_s():
    return _sswitch(2)

@small("workspace-switcher-right-bottom")
def ws_rb_s():
    return _sswitch(3)

@small("wordpad")
def wordpad_s():
    return rrect(16, 11, 32, 38, 3.5, INK) + "".join(rrect(21, y, 22, 4, 2, HOLE) for y in (18, 26, 34)) + \
        rrect(21, 41, 13, 4, 2, HOLE)

@small("wordview")
def wordview_s():
    return (stroke("M14 17L21 42L28.5 23L36 42L43 17", INK, 5.5) + _sbadge(RED_DEEP) +
            path("M35 40.5C37 37.5 39.5 36 42.5 36C45.5 36 48 37.5 50 40.5C48 43.5 45.5 45 42.5 45"
                 "C39.5 45 37 43.5 35 40.5Z", INK) + circle(42.5, 40.5, 2.2, RED_DEEP))

@small("wings3d")
def wings3d_s():
    out = ""
    for cx, cy in [(24, 22), (40, 38)]:
        out += poly([(cx, cy - 10), (cx + 10, cy - 5), (cx, cy), (cx - 10, cy - 5)], INK, 1.5)
        out += poly([(cx - 10, cy - 5), (cx, cy), (cx, cy + 10), (cx - 10, cy + 5)], RED_SOFT, 1.5)
        out += poly([(cx + 10, cy - 5), (cx, cy), (cx, cy + 10), (cx + 10, cy + 5)], RED_DARK, 1.5)
    return out

@small("wootility")
def wootility_s():
    return rrect(13, 14, 38, 32, 4, INK) + path(
        "M19.5 20H25L27 27H29.5L31 20H33L34.5 27H37L39 20H44.5V39.5H19.5Z", HOLE)

@small("welle.io")
def welle_io_s():
    return (line(19, 19, 42, 11, INK, 2.8) + rrect(12, 18, 40, 29, 4, INK) +
            circle(24.5, 32.5, 8, HOLE) + rrect(37, 24, 10, 5, 1.5, DEEP_ORANGE_LIGHT) + rrect(37, 34, 10, 5, 1.5, HOLE))

@small("weka")
def weka_s():
    body = path("M13 33C14 25 22 20.5 30.5 21.5C32.5 16.5 36 13 40.5 13.5C44.5 14 46 17 46 19"
                "L51 21L45.5 22.5C44.5 26 42.5 29 42.5 32.5C42.5 38.5 36.5 43 29 42.5C21.5 42 16 38 13 33Z", INK)
    return body + stroke("M27.5 41.5L25 48M33.5 41.5L35 48", INK, 3) + circle(40.8, 18, 2, HOLE)

@small("wire")
def wire_s():
    return stroke("M17 17V33A7.5 7.5 0 0 0 32 33A7.5 7.5 0 0 0 47 33V17M32 33V21", INK, 4.2)

@small("words")
def words_s():
    nib = path("M32 11L42 27C42 31 39 34.5 37 36V41H27V36C25 34.5 22 31 22 27Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return nib + circle(32, 28, 2.8, HOLE) + line(32, 17, 32, 26, HOLE, 2.4) + rrect(26, 43, 12, 5, 2, ORANGE)

@small("world-of-goo")
def world_of_goo_s():
    return circle(32, 31, 17, INK) + circle(23, 26, 7, HOLE) + circle(41, 26, 7, HOLE) + \
        circle(24.5, 27, 3, INK) + circle(39.5, 27, 3, INK)
