# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 53: org.kde.neochat to paperwork.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import arc, ell_g, _gear_i, registry, _ring, rot_b, _slabs
from glyphs.kit import shared_opensuse

ICONS, SMALL, reg, small = registry()

def _chip(x, y, s, pin_w, pin_len, n=3):
    """Square chip with n pins on each side."""
    out = rrect(x, y, s, s, 3.5, INK)
    step = s / (n + 1)
    for i in range(1, n + 1):
        c = x + step * i
        out += rrect(c - pin_w / 2, y - pin_len - 1, pin_w, pin_len + 2, pin_w / 2, INK)
        out += rrect(c - pin_w / 2, y + s - 1, pin_w, pin_len + 2, pin_w / 2, INK)
        c = y + step * i
        out += rrect(x - pin_len - 1, c - pin_w / 2, pin_len + 2, pin_w, pin_w / 2, INK)
        out += rrect(x + s - 1, c - pin_w / 2, pin_len + 2, pin_w, pin_w / 2, INK)
    return out

@reg("org.kde.neochat", CYAN)
def neochat():
    back = (rrect(22, 19, 28, 21, 6, CYAN_DARK) +
            poly([(40, 38), (47, 46.5), (46, 38)], CYAN_DARK, 2))
    front = (rrect(14, 13, 30, 22, 6, INK) +
             poly([(18.5, 33), (18.5, 42.5), (27, 33)], INK, 2.5))
    lines = "".join(rrect(19.5, y, w, 3, 1.5, HOLE) for y, w in [(18, 19), (23.5, 19), (29, 12)])
    return back + front + lines

@reg("org.tabos.twofun", RED_DEEP)
def twofun():
    return _ring(CX, CY, 16, INK, 2.4) + circle(CX, CY, 12, INK)

@reg("org.ubuntubudgie.quickchar", INDIGO_LIGHT)
def quickchar():
    page = rrect(22, 14, 26, 33, 4, INK)
    lines = "".join(rrect(28, y, 14, 3, 1.5, HOLE) for y in (27, 33, 39))
    badge = circle(21, 20, 10, HOLE) + circle(21, 20, 8, INDIGO_DARK)
    arrow = (stroke("M15.5 21.5C17 17 22.5 15.5 26 19", INK, 2.4) +
             poly([(27.8, 16.2), (27.5, 22), (22.5, 20.5)], INK, 1))
    return page + lines + badge + arrow

@reg("org.librepcb.LibrePCB", PURPLE_SOFT)
def librepcb():
    return _chip(20, 18, 24, 3.4, 5) + circle(25.5, 23.5, 2, HOLE)

@reg("org.rnd2.cpupower_gui", LIGHT_BLUE_DEEP)
def cpupower():
    bolt = poly([(34.5, 20.5), (25.5, 32), (31.5, 32), (29.5, 40), (38.5, 28), (32.5, 28)], HOLE, 1.2)
    return _chip(19, 17, 26, 3.4, 4.5) + bolt

@reg("org.processing.processingide", BLUE_GREY_DEEP)
def processing():
    return _ring(CX, CY, 15, INK, 4.4) + poly([(28, 22.5), (39.5, 30), (28, 37.5)], INK, 3)

@reg("org.wezfurlong.wezterm", DEEP_PURPLE_DEEP)
def wezterm():
    dollar = (stroke("M27 22.5C25.5 20.5 23.8 19.5 21.5 19.5C18.5 19.5 16.5 21.3 16.5 23.7"
                     "C16.5 29.5 27.5 27.5 27.5 34.2C27.5 37.2 25 39.5 21.5 39.5"
                     "C19 39.5 17 38.5 15.5 36.5", INK, 3.4) +
              line(21.8, 15.5, 21.8, 43.5, INK, 3))
    w = stroke("M31.5 19.5L35.5 40L40.3 26L45 40L49 19.5", INK, 3.6)
    return dollar + w

@reg("org.xfce.terminal-settings", BLUE_GREY_DARK)
def xfce_terminal_settings():
    prompt = stroke("M15.5 15.5L24 22.5L15.5 29.5", INK, 4.5) + rrect(26.5, 27, 12, 4.6, 2.3, INK)
    gear = circle(40, 38, 12, HOLE) + _gear_i(40, 38, 7, DEEP_ORANGE, HOLE)
    return g(prompt + gear, "translate(0 -1)")

@reg("org.xfce.volman", GREY_DARK)
def volman():
    plug = rrect(22, 12, 20, 11, 2, INK) + rrect(26, 15.5, 4, 3.6, 0.8, HOLE) + rrect(34, 15.5, 4, 3.6, 0.8, HOLE)
    body = rrect(16, 24, 32, 24, 4, INK)
    lines = "".join(rrect(x, y, w, 2.8, 1.4, HOLE) for x, y, w in
                    [(23, 29.5, 18), (21, 34.6, 22), (23, 39.7, 18)])
    return plug + body + lines

@reg("org.xfce.Gigolo", LIGHT_BLUE_DEEP)
def gigolo():
    screen = rrect(15, 12, 34, 23, 4, INK)
    cloud = (circle(27, 25.5, 4.5, HOLE) + circle(33.5, 22, 5.8, HOLE) + circle(39.5, 26, 4, HOLE) +
             rrect(23, 25.5, 20, 4.5, 2.25, HOLE))
    dots = "".join(circle(x, 39.5, 2.2, INK) for x in (25.5, 32, 38.5))
    base = line(15, 46.5, 49, 46.5, INK, 2.6) + rrect(27, 43.5, 10, 6, 2, INK)
    return screen + cloud + dots + base

@reg("org.pipewire.Helvum", BLUE_GREY_DEEP)
def helvum():
    box = rrect(14, 22, 36, 24, 5, INK)
    jacks = "".join(circle(x, y, 3.4, HOLE) + circle(x, y, 1.4, INK)
                    for x in (22, 32, 42) for y in (29, 38.5))
    cable = stroke("M22 18C22 14.5 20 12.5 17 11.5", INK, 2.6) + rrect(19.5, 15.5, 5, 9, 1.5, INK)
    return box + jacks + cable

@reg("pac", BLUE_DEEP)
def pac():
    body = rrect(14, 14, 36, 29, 5, INK)
    jack = path("M19.5 19.5H44.5V35.5H39.5L37 38.5H27L24.5 35.5H19.5Z", HOLE,
                f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"')
    pins = "".join(rrect(22.3 + 4.2 * i, 20.5, 3, 4, 0.6, INK) for i in range(5))
    return g(body + jack + pins, "translate(0 1.5)")

@reg("packet-tracer", AMBER_DEEP)
def packet_tracer():
    lens = _ring(29.5, 27.5, 10, INK, 4)
    grid = "".join(rrect(x, y, 5, 5, 0.8, INK) for x, y in
                   [(24.5, 22.5), (30, 28)]) + "".join(
        f'<rect x="{x}" y="{y}" width="5" height="5" rx=".8" fill="none" stroke="{INK}" stroke-width="1.2"/>'
        for x, y in [(30, 22.5), (24.5, 28)])
    handle = line(37.5, 35.5, 46, 44, INK, 5.5)
    return lens + grid + handle

@reg("org.nickvision.tagger", BLUE_DEEP)
def tagger():
    sheet = rrect(15, 13, 27, 34, 3.5, INK)
    note = stroke("M27.5 37V22.5L33.5 24.5", HOLE, 2.8) + circle(24.8, 37, 3.2, HOLE)
    pen = (line(48, 15.5, 35.5, 38.5, HOLE, 8.5) + line(48, 15.5, 35.5, 38.5, INK, 4.8) +
           poly([(33.3, 37.4), (37.7, 39.8), (33.2, 44)], INK, 1.2))
    return sheet + note + pen

@reg("org.nickvision.tubeconverter", RED)
def tubeconverter():
    arrow = line(32, 13.5, 32, 34, INK, 5) + stroke("M22.5 25.5L32 35L41.5 25.5", INK, 5)
    return arrow + rrect(17.5, 41, 29, 5.5, 2.75, INK)

@reg("org.nongnu.lingot", INDIGO_SOFT)
def lingot():
    fan = path("M14 37A18 18 0 0 1 50 37H41A9 9 0 0 0 23 37Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    needle = circle(32, 40, 5.2, HOLE) + line(32, 40, 38.5, 20, HOLE, 5.5) + line(32, 40, 38.5, 20, INK, 2.8)
    return fan + needle + circle(32, 40, 3.4, INK)

@reg("org.olivevideoeditor.Olive", BLUE_GREY)
def olive():
    twig = stroke("M16 45C23 39 33 29 47 15", INK, 3)
    leaves = ""
    for cx, cy, deg in [(23.5, 33, -85), (31, 22.5, -80), (40, 17, -60),
                        (33.5, 33, 5), (42, 25.5, 0)]:
        leaves += rot_b(path(ell_g(cx, cy, 6.5, 2.8), INK), deg, cx, cy)
    olives = circle(26.5, 40.5, 3.2, INK)
    return leaves + twig + olives

@reg("org.openkj.OpenKJ", BLUE_LIGHT)
def openkj():
    tri = poly([(18.5, 14), (48.5, 30), (18.5, 46)], INK, 6)
    mic = (rrect(24.5, 20.5, 7, 12.5, 3.5, HOLE) +
           stroke("M22 28.5A6 6 0 0 0 34 28.5", HOLE, 2.3) + line(28, 35, 28, 39.5, HOLE, 2.3))
    return tri + mic

@reg("org.tabos.maxcontrol", DEEP_ORANGE)
def maxcontrol():
    top = path("M16 33C23 27 33 26 38 20C40 17 40.5 14 39.5 11.5C46.5 15 49 22.5 45 28"
               "C40 34.5 27 33 16 33Z", INK)
    mid = path("M18 39.5C26 35 37 36.5 44 33.5C47 32 48.5 30 49 28.5"
               "C50.5 33 48 38.5 42 40.5C35 43 25 39.5 18 39.5Z", INK)
    low = path("M22 45.5C29 42.5 36 44 42 43.5C44 43.3 45.5 42.7 46.5 42"
               "C45.5 46 42 48 38 48.3C32 48.8 27 45.5 22 45.5Z", INK)
    return g(top + mid + low, "translate(-1 -1)")

@reg("org.pwsafe.pwsafe", RED_DARK)
def pwsafe():
    big = poly([(15.5, 12), (15.5, 47.5), (51, 47.5)], INK, 3)
    steps = "".join(poly([(x, y), (x, y + 8.6), (x + 8.6, y + 8.6)], HOLE, 1)
                    for x, y in [(19, 17.5), (19, 27.5), (19, 37.5), (29, 37.5)])
    return g(big + steps, "translate(-1.5 0)")

@reg("org.tabos.banking", BLUE)
def banking():
    card = rrect(13, 17, 38, 26, 4.5, INK)
    chip = rrect(18.5, 22, 8, 6.5, 1.5, AMBER)
    num = rrect(18.5, 33.5, 13, 3, 1.5, HOLE)
    mc = circle(38.5, 36, 3.8, RED) + circle(43.5, 36, 3.8, ORANGE)
    return card + chip + num + mc

@reg("org.ubuntubudgie.budgiewpreviews", RED)
def budgiewpreviews():
    loop = stroke(arc(CX, CY, 15, 205, 155 + 360), INK, 4.4)
    tiles = "".join(rrect(x, y, 7.5, 6.5, 1.8, INK) for x in (24, 32.5) for y in (22.5, 31))
    return loop + tiles

@reg("org.ubuntubudgie.shuffler-control", TEAL)
def shuffler():
    return (rrect(15, 13, 10, 10, 2, INK) + rrect(27, 13, 10, 10, 2, INK) +
            rrect(15, 25, 10, 10, 2, INK) + rrect(27, 25, 22, 22, 3, INK))

@reg("org.ubuntubudgie.wallstreet-control", PURPLE)
def wallstreet():
    tiles = "".join(rrect(x, y, 16, 16, 2.5, INK) for x in (15, 33) for y in (13, 31))
    target = _ring(CX, CY, 6, HOLE, 3) + line(21, 30, 43, 30, HOLE, 2.6)
    return rot_b(tiles + target, -15)

@reg("org.vinegarhq.Vinegar.player", BLUE_GREY_LIGHT)
def vinegar_player():
    return rot_b(rrect(16.5, 14.5, 31, 31, 3.5, INK) + rrect(28, 26, 8, 8, 1, HOLE), 15)

@reg("org.vinegarhq.Vinegar.studio", LIGHT_BLUE_DEEP)
def vinegar_studio():
    return _slabs(LIGHT_BLUE_SOFT, INK)

@reg("org.polymc.PolyMC", BLUE)
def polymc():
    top = poly([(32, 12.5), (47.5, 21), (32, 29.5), (16.5, 21)], BLUE_SOFT, 2)
    left = poly([(16.5, 21), (32, 29.5), (32, 47.5), (16.5, 39)], INK, 2)
    right = poly([(47.5, 21), (32, 29.5), (32, 47.5), (47.5, 39)], BROWN, 2)
    grass = (poly([(16.5, 21), (32, 29.5), (32, 34), (27, 31), (22, 30), (16.5, 26)], BLUE_SOFT, 2) +
             poly([(47.5, 21), (32, 29.5), (32, 34), (37, 32), (42, 29.5), (47.5, 27)], BLUE, 2))
    return top + left + right + grass

@reg("org.prismlauncher.PrismLauncher", DEEP_PURPLE_DEEP)
def prism():
    tris = ""
    for k in range(6):
        a0, a1 = -90 + 60 * k, -30 + 60 * k
        p0, p1 = pt(CX, CY, 17, a0), pt(CX, CY, 17, a1)
        tris += poly([(CX, CY), p0, p1], INK if k % 2 == 0 else PURPLE_SOFT, 1.5)
    seams = "".join(line(CX, CY, *pt(CX, CY, 17, -90 + 60 * k), HOLE, 1.6) for k in range(6))
    hexa = poly([pt(CX, CY, 9, -90 + 60 * k) for k in range(6)], HOLE, 1)
    cube = (poly([(CX, CY), pt(CX, CY, 6.5, -150), pt(CX, CY, 6.5, -90), pt(CX, CY, 6.5, -30)], INK, 1) +
            poly([(CX, CY), pt(CX, CY, 6.5, -30), pt(CX, CY, 6.5, 30), pt(CX, CY, 6.5, 90)], DEEP_PURPLE_SOFT, 1) +
            poly([(CX, CY), pt(CX, CY, 6.5, 90), pt(CX, CY, 6.5, 150), pt(CX, CY, 6.5, 210)], PURPLE_SOFT, 1))
    return tris + seams + hexa + cube

@reg("osu", PINK_LIGHT)
def osu():
    o = _ring(18.5, 31, 4, INK, 3.2)
    s = stroke("M31.5 27C30.5 26 29.5 25.8 28.5 25.8C26.8 25.8 25.8 26.8 25.8 28"
               "C25.8 31 31.8 30.2 31.8 33.3C31.8 34.8 30.5 35.9 28.6 35.9C27.2 35.9 26 35.3 25.3 34.4", INK, 3)
    u = stroke("M35.5 26V31.5C35.5 34.3 36.8 35.8 39 35.8C41.2 35.8 42.3 34.3 42.3 31.5V26M42.3 31.5V35.8", INK, 3)
    bang = line(47.5, 21, 47.5, 30.5, INK, 3.6) + circle(47.5, 35.6, 2.1, INK)
    return g(o + s + u + bang, "translate(-1 -1)")

@reg("otter-browser", BLUE)
def otter():
    return path("M32 13.5C38.5 13.5 43.5 21 43.5 30C43.5 40 38.5 46.5 32 46.5"
                "C25.5 46.5 20.5 40 20.5 30C20.5 21 25.5 13.5 32 13.5Z", INK)

@reg("outlast", BLUE_GREY_DEEP)
def outlast():
    return stroke(ell_g(CX, CY, 10.5, 14.5), INK, 6)

@reg("outwiker", GREY_DEEP)
def outwiker():
    o = stroke(ell_g(24, 23.5, 6.5, 9), INK, 4.6)
    wpath = "M28.5 29L32 45L36.5 35L41 45L44.5 29"
    w = stroke(wpath, HOLE, 8.5) + stroke(wpath, ORANGE_LIGHT, 4.6)
    return o + w

def _overcooked(cx, cy, r):
    return circle(cx, cy, r, INK) + stroke(ell_g(cx, cy, r * .33, r * .5), HOLE, r * .29)

@reg("overcooked", RED_DEEP)
def overcooked():
    return _overcooked(CX, CY, 16.5)

@reg("overcooked2", RED_DEEP)
def overcooked2():
    two = "M39.5 38.5C39.5 35.5 41.8 34 44 34C46.3 34 48.3 35.6 48.3 37.8C48.3 40.8 44.5 43.5 40 47.5H48.8"
    return (_overcooked(29.5, 27.5, 15) + stroke(two, HOLE, 8.5) + stroke(two, ORANGE_LIGHT, 4))

@reg("overwatch", ORANGE_DEEP)
def overwatch():
    rim = (stroke(arc(CX, CY, 15.5, -138, -42), INK, 4.8) +
           stroke(arc(CX, CY, 15.5, -22, 202), INK, 4.8))
    left = poly([(28.5, 17.5), (29.8, 33.5), (23.5, 40), (20.5, 37.3), (26.5, 31.3), (26.5, 22)], INK, 1.6)
    right = poly([(35.5, 17.5), (34.2, 33.5), (40.5, 40), (43.5, 37.3), (37.5, 31.3), (37.5, 22)], INK, 1.6)
    return rim + left + right

@reg("owncloud", INDIGO_DARK)
def owncloud():
    out = ""
    for cx, cy, r in [(22.5, 32, 6.5), (41.5, 32, 6.5), (29, 26, 7.5), (37.5, 25, 6.5),
                      (27, 36, 5.5), (37, 36, 5.5), (32, 34.5, 6.5)]:
        out += circle(cx, cy, r, INK, f' stroke="{HOLE}" stroke-width="1.8"')
    return g(out, "translate(0 -.5)")

@reg("package_games_arcade", BLUE_DARK)
def arcade():
    top = rrect(18.5, 12, 27, 7, 2.5, INK)
    body = rrect(20, 17, 24, 31, 3, INK)
    screen = rrect(23.5, 21.5, 17, 12, 2, HOLE)
    stick = line(26.5, 42, 26.5, 38.5, HOLE, 2.2) + circle(26.5, 38, 2.2, HOLE)
    buttons = circle(34.5, 40.5, 1.9, HOLE) + circle(39, 40.5, 1.9, HOLE)
    return top + body + screen + stick + buttons

@reg("pacseek", GREY_DARK)
def pacseek():
    head = circle(31, 30, 16.5, INK)
    mouth = poly([(33, 31), (50, 16), (50, 45)], HOLE)
    teeth = "".join(poly(p, INK, 0.8) for p in [
        [(36, 28.3), (40, 24.8), (39.6, 29.6)], [(40, 24.8), (44.2, 21), (43.8, 26)],
        [(44.2, 21), (48, 17.7), (47.8, 22.5)],
        [(36, 33.5), (40.5, 37), (40, 32.4)], [(40.5, 37), (45, 40.5), (44.5, 35.5)]])
    eye = circle(29, 21.5, 2.8, HOLE)
    return head + mouth + teeth + eye

@reg("page.codeberg.foreverxml.Random", BLUE_GREY_DEEP)
def random_():
    dial = circle(CX, CY, 16, INK)
    dots = "".join(circle(x, y, 2.6, HOLE) for x, y in
                   [(24.5, 22.5), (39.5, 22.5), (24.5, 37.5), (39.5, 37.5)])
    pointer = line(33, 30, 23.5, 28.5, HOLE, 3) + circle(34, 30, 4.4, HOLE)
    return dial + dots + pointer

@reg("page.tesk.Refine", BLUE_DEEP)
def refine():
    panel = rrect(14, 14, 36, 32, 5, INK)
    slider = line(20, 22.5, 44, 22.5, HOLE, 2.6) + circle(33, 22.5, 4, HOLE)
    toggle = rrect(19.5, 31, 14, 8.5, 4.25, HOLE) + circle(29, 35.25, 2.7, INK)
    box = rrect(36, 30.5, 9.5, 9.5, 2, HOLE) + circle(40.75, 35.25, 2.2, INK)
    return panel + slider + toggle + box

@reg("pairs", BLUE_DEEP)
def pairs():
    return stroke("M23 46L30 19C31 15.5 34 14 37.5 14C42.5 14 45.5 17.5 44.5 22"
                  "C43.5 27 37.5 29.5 29 29C24 28.7 20 27 18 24.5", INK, 3.6)

@reg("palapeli", AMBER_DARK)
def palapeli():
    piece = (rrect(16, 20, 27, 27, 3.5, INK) + circle(29.5, 16.5, 5.5, INK) +
             rrect(26.5, 17, 6, 5, 0, INK) + circle(46.5, 33.5, 5.5, INK) + rrect(41, 30.5, 5, 6, 0, INK))
    notch = circle(16, 33.5, 5, HOLE)
    return g(piece + notch, "translate(-.5 -1.5)")

@reg("palemoon", BLUE_DARK)
def palemoon():
    moon = circle(CX, CY, 16.5, INK)
    land = (path("M30 14C33 17 37 16.5 39 19.5C41 22.5 37.5 24.5 39.5 27.5C41.5 30.5 46 29 48 31"
                 "C47.5 36 45 40.5 41 43.5C39.5 40.5 40.5 37 37.5 35C34.5 33 31 35 28.5 32.5"
                 "C26 30 29 26.5 27 24C25 21.5 21 22.5 19.5 21C22.5 17 26 14.8 30 14Z", HOLE) +
            path("M17 33C19.5 32 22.5 33.5 23.5 36C24.5 38.5 23 41 21.5 41.5C19 39 17.5 36.5 17 33Z", HOLE))
    return moon + land

@reg("papagayong", DEEP_PURPLE)
def papagayo():
    head = path("M17 46C14 36 15.5 24 22 17.5C27 12.5 34 11.5 39 14.5"
                "C36 18 35 22.5 35.5 27.5C36 33.5 34 39 29 42.5C25.5 45 21 46 17 46Z", INK)
    crest = poly([(19.5, 20), (13.5, 15.5), (22.5, 16)], INK, 2)
    beak = path("M36.5 15C42.5 13 49.5 17 50 25C50.5 30.5 48.5 34.5 45.5 36.5"
                "C45.5 32 43.5 29.5 40 29C38 28.8 36.5 29.5 35.5 30.5C34.5 24.5 34 18.5 36.5 15Z", AMBER)
    eye = circle(28.5, 22.5, 3, HOLE) + circle(29, 22.5, 1.4, INK)
    return head + crest + beak + eye

@reg("paperwork", BLUE_GREY)
def paperwork():
    upper = poly([(14, 29), (50, 14), (29.5, 34)], INK, 2)
    lower = poly([(29.5, 34), (50, 14), (38, 45)], BLUE_GREY_SOFT, 2)
    fold = poly([(29.5, 34), (31, 43.5), (35, 38.5)], INK, 2)
    return upper + lower + fold

@reg("osmscout-server", BLUE_DEEP)
def osmscout():
    frame = path("M15 13H49V47H29A14 14 0 0 1 15 33Z", INK)
    sea = path("M19 17H45V43H29.5A10.5 10.5 0 0 1 19 32.5Z", HOLE)
    land = path("M33 17H45V43H31C32 39.5 36 38 36 33.5C36 29.5 39.5 27.5 38 24C37 21.5 33.5 20 33 17Z", INK)
    shore = path("M19 31C23 28.5 28 29.5 30 33C31.5 36 29.5 40.5 27.5 42.8A10.5 10.5 0 0 1 19 32.5Z", INK)
    return frame + sea + land + shore

@reg("org.opensuse.opensuse_welcome", BLUE_GREY_LIGHT)
def opensuse_welcome():
    return shared_opensuse()

@small("org.kde.neochat")
def neochat_s():
    front = (rrect(13, 14, 38, 26, 7, INK) + poly([(18.5, 38), (18.5, 47), (28, 38)], INK, 2.5))
    lines = "".join(rrect(20, y, w, 4.5, 2.25, HOLE) for y, w in [(20.5, 24), (29, 15)])
    return front + lines

@small("osu")
def osu_s():
    return _ring(24, 32, 6.5, INK, 5) + line(41, 16, 41, 32, INK, 6) + circle(41, 41, 3.4, INK)

@small("org.librepcb.LibrePCB")
def librepcb_s():
    return _chip(19, 17, 26, 4.4, 4, n=2) + circle(25.5, 23.5, 2.8, HOLE)

@small("org.rnd2.cpupower_gui")
def cpupower_s():
    bolt = poly([(35, 20.5), (25.5, 32), (31.5, 32), (29.5, 40), (39, 28), (33, 28)], HOLE, 2)
    return _chip(19, 17, 26, 5, 4, n=2) + bolt

@small("org.nickvision.tagger")
def tagger_s():
    sheet = rrect(14, 13, 28, 34, 4, INK)
    note = stroke("M27.5 37V22", HOLE, 3.6) + circle(24.5, 37, 4, HOLE)
    pen = line(48, 15, 36, 38, HOLE, 10) + line(48, 15, 36, 38, INK, 6)
    return sheet + note + pen

@small("org.olivevideoeditor.Olive")
def olive_s():
    twig = stroke("M16 45C23 39 33 29 47 15", INK, 3.4)
    leaves = "".join(rot_b(path(ell_g(cx, cy, 7, 3.6), INK), deg, cx, cy)
                     for cx, cy, deg in [(25, 31, -80), (38, 18.5, -65), (36, 32, 0)])
    return twig + leaves

@small("org.xfce.terminal-settings")
def xfce_terminal_settings_s():
    prompt = stroke("M15 15L24.5 22.5L15 30", INK, 5.5)
    gear = circle(39, 37, 13, HOLE) + circle(39, 37, 9.5, DEEP_ORANGE) + circle(39, 37, 3.6, HOLE)
    return prompt + gear

@small("org.xfce.volman")
def volman_s():
    plug = rrect(22, 12, 20, 11, 2, INK) + rrect(26, 15.5, 4.5, 4, 1, HOLE) + rrect(33.5, 15.5, 4.5, 4, 1, HOLE)
    body = rrect(15, 24, 34, 24, 4, INK)
    lines = rrect(22, 30, 20, 4.2, 2.1, HOLE) + rrect(22, 38, 20, 4.2, 2.1, HOLE)
    return plug + body + lines

@small("org.xfce.Gigolo")
def gigolo_s():
    screen = rrect(14, 12, 36, 26, 4.5, INK)
    cloud = (circle(26.5, 27, 5, HOLE) + circle(34, 23, 6.5, HOLE) + circle(40.5, 27.5, 4.5, HOLE) +
             rrect(22, 27, 23, 5, 2.5, HOLE))
    base = line(14, 46, 50, 46, INK, 3.4) + rrect(26, 41.5, 12, 8, 2.5, INK)
    return screen + cloud + base

@small("org.pipewire.Helvum")
def helvum_s():
    box = rrect(13, 21, 38, 26, 5, INK)
    jacks = "".join(circle(x, y, 4.2, HOLE) for x in (23, 41) for y in (28.5, 39.5))
    cable = stroke("M23 18C23 14.5 21 12.5 18 11.5", INK, 3.4) + rrect(20, 15, 6, 9, 1.5, INK)
    return box + jacks + cable

@small("pac")
def pac_s():
    body = rrect(13, 14, 38, 31, 5, INK)
    jack = path("M19 20H45V36H40L37 39.5H27L24 36H19Z", HOLE)
    pins = "".join(rrect(22 + 7 * i, 21, 5, 5, 1, INK) for i in range(3))
    return body + jack + pins

@small("packet-tracer")
def packet_tracer_s():
    return _ring(29, 27, 10.5, INK, 5) + line(37, 35, 46.5, 44.5, INK, 7) + rrect(24, 22, 10, 10, 1.5, INK)

@small("org.nongnu.lingot")
def lingot_s():
    fan = path("M13 38A19 19 0 0 1 51 38H41A9 9 0 0 0 23 38Z", INK)
    needle = circle(32, 40, 6, HOLE) + line(32, 40, 38.5, 19, HOLE, 7) + line(32, 40, 38.5, 19, INK, 3.6)
    return fan + needle + circle(32, 40, 4, INK)

@small("org.tabos.banking")
def banking_s():
    card = rrect(12, 16, 40, 28, 5, INK)
    chip = rrect(17.5, 21, 10, 8, 2, AMBER)
    mc = circle(37.5, 36, 4.8, RED) + circle(44, 36, 4.8, ORANGE)
    return card + chip + mc

@small("org.ubuntubudgie.quickchar")
def quickchar_s():
    page = rrect(21, 13, 28, 35, 4, INK)
    lines = "".join(rrect(29, y, 14, 4, 2, HOLE) for y in (28, 37))
    badge = circle(21, 20, 11, HOLE) + circle(21, 20, 9, INDIGO_DARK)
    return page + lines + badge + stroke("M16 22C17.5 17 23 16 26 19.5", INK, 3)

@small("org.ubuntubudgie.budgiewpreviews")
def budgiewpreviews_s():
    loop = stroke(arc(CX, CY, 15, 210, 150 + 360), INK, 5)
    tiles = "".join(rrect(x, y, 8.5, 7.5, 2, INK) for x in (22.5, 32.5) for y in (21.5, 31))
    return loop + tiles

@small("org.ubuntubudgie.wallstreet-control")
def wallstreet_s():
    tiles = "".join(rrect(x, y, 16, 16, 2.5, INK) for x in (15, 33) for y in (13, 31))
    return rot_b(tiles + _ring(CX, CY, 6.5, HOLE, 4), -15)

@small("org.wezfurlong.wezterm")
def wezterm_s():
    dollar = (stroke("M28 22C26.5 19.5 24.5 18.5 22 18.5C18.8 18.5 16.5 20.5 16.5 23.3"
                     "C16.5 29.5 28 27.3 28 34.5C28 37.8 25.5 40.5 21.8 40.5"
                     "C19.2 40.5 17 39.5 15.5 37.5", INK, 4.4) +
              line(22.2, 14.5, 22.2, 44.5, INK, 3.8))
    return dollar + stroke("M32 19L36 40L40.5 27L45 40L49 19", INK, 4.4)

@small("osmscout-server")
def osmscout_s():
    frame = path("M14 12H50V48H30A16 16 0 0 1 14 32Z", INK)
    sea = path("M19 17H45V43H31A12 12 0 0 1 19 31Z", HOLE)
    land = path("M33 17H45V43H31C32 38 36.5 37 36.5 32C36.5 27 40 25.5 38 22C36.5 19.5 33.5 19 33 17Z", INK)
    return frame + sea + land

@small("page.tesk.Refine")
def refine_s():
    panel = rrect(13, 13, 38, 34, 5, INK)
    slider = line(19, 22, 45, 22, HOLE, 3.4) + circle(33, 22, 4.8, HOLE)
    toggle = rrect(18.5, 31, 16, 10, 5, HOLE) + circle(29.5, 36, 3.2, INK)
    box = rrect(37, 30, 10.5, 11, 2, HOLE)
    return panel + slider + toggle + box

@small("page.codeberg.foreverxml.Random")
def random_s():
    dial = circle(CX, CY, 16.5, INK)
    dots = "".join(circle(x, y, 3.2, HOLE) for x, y in [(24, 22), (40, 22), (24, 38), (40, 38)])
    return dial + dots + circle(33, 30, 5, HOLE)

@small("pacseek")
def pacseek_s():
    head = circle(31, 30, 17, INK)
    mouth = poly([(32, 30.5), (50, 15), (50, 46)], HOLE)
    teeth = poly([(38, 25.3), (44.5, 19.7), (43.5, 27.5)], INK, 1) + poly([(38, 35.8), (44.5, 41.3), (43.5, 33.5)], INK, 1)
    return head + mouth + teeth + circle(28.5, 20.5, 3.4, HOLE)

@small("package_games_arcade")
def arcade_s():
    body = rrect(18, 11, 28, 38, 3.5, INK)
    screen = rrect(22.5, 17, 19, 14, 2, HOLE)
    return body + screen + circle(27, 39.5, 3, HOLE) + circle(37, 39.5, 3, HOLE)

@small("papagayong")
def papagayo_s():
    head = path("M17 46C14 36 15.5 24 22 17.5C27 12.5 34 11.5 39 14.5"
                "C36 18 35 22.5 35.5 27.5C36 33.5 34 39 29 42.5C25.5 45 21 46 17 46Z", INK)
    beak = path("M36.5 15C42.5 13 49.5 17 50 25C50.5 30.5 48.5 34.5 45.5 36.5"
                "C45.5 32 43.5 29.5 40 29C38 28.8 36.5 29.5 35.5 30.5C34.5 24.5 34 18.5 36.5 15Z", AMBER)
    return head + beak + circle(28.5, 22.5, 3.6, HOLE)

@small("palemoon")
def palemoon_s():
    moon = circle(CX, CY, 17, INK)
    land = path("M30 13.5C34 17 38 17 39.5 21C41 24.5 38 27 41 29.5C43 31 46.5 30 49 31.5"
                "C48.5 37 45.5 41.5 41 44.5C39 40 39.5 37 36 35.5C32.5 34 29 35.5 26.5 32"
                "C24.5 29 27.5 26 25 23.5C23 21.5 20.5 22.5 18.5 21.5C21.5 16.5 25.5 14 30 13.5Z", HOLE)
    return moon + land

@small("overwatch")
def overwatch_s():
    rim = (stroke(arc(CX, CY, 16, -135, -45), INK, 5.5) +
           stroke(arc(CX, CY, 16, -20, 200), INK, 5.5))
    left = poly([(28, 17), (29.5, 34), (22.5, 41), (19.5, 38), (25.5, 32), (25.5, 21)], INK, 1.6)
    right = poly([(36, 17), (34.5, 34), (41.5, 41), (44.5, 38), (38.5, 32), (38.5, 21)], INK, 1.6)
    return rim + left + right

@small("owncloud")
def owncloud_s():
    out = ""
    for cx, cy, r in [(21.5, 33, 7), (42.5, 33, 7), (32, 27, 10), (32, 36, 7)]:
        out += circle(cx, cy, r, INK, f' stroke="{HOLE}" stroke-width="2.2"')
    return out

@small("org.pwsafe.pwsafe")
def pwsafe_s():
    big = poly([(14, 11), (14, 48.5), (51.5, 48.5)], INK, 3)
    steps = poly([(18, 22), (18, 34), (30, 34)], HOLE, 1) + poly([(18, 38.5), (18, 44.5), (24, 44.5)], HOLE, 1) + \
        poly([(27, 38.5), (27, 44.5), (33, 44.5)], HOLE, 1)
    return g(big + steps, "translate(-1 0)")

@small("org.prismlauncher.PrismLauncher")
def prism_s():
    hexa = poly([pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)], INK, 2)
    right = poly([(CX, CY)] + [pt(CX, CY, 17.5, a) for a in (-30, 30, 90)], PURPLE_SOFT, 2)
    cube = poly([pt(CX, CY, 8.5, -90 + 60 * k) for k in range(6)], HOLE, 1)
    return hexa + right + cube + stroke("M26 26.5L32 30L38 26.5M32 30V37", INK, 2.4)
