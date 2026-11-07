# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 42: libation .. lplayer."""
import math
from lm import *
from glyphs.kit import _doc, ell_c, registry, _ring
from glyphs.kit import shared_discord

ICONS, SMALL, reg, small = registry()

def _heart(cx, cy, s, fill):
    d = ("M32 44C22 37 16 31 16 24.5C16 19.5 19.8 16 24 16C27.5 16 30.3 18 32 21"
         "C33.7 18 36.5 16 40 16C44.2 16 48 19.5 48 24.5C48 31 42 37 32 44Z")
    return g(path(d, fill), f"translate({f(cx)} {f(cy)}) scale({f(s)}) translate(-32 -30)")

def _band(r, y1, y2, fill, cx=CX, cy=CY):
    """Horizontal slice of a circle between y1 and y2."""
    def xs(y):
        dx = math.sqrt(max(r * r - (y - cy) ** 2, 0))
        return cx - dx, cx + dx
    l1, r1 = xs(y1)
    l2, r2 = xs(y2)
    return path(f"M{f(l1)} {f(y1)}L{f(r1)} {f(y1)}A{f(r)} {f(r)} 0 0 1 {f(r2)} {f(y2)}"
                f"L{f(l2)} {f(y2)}A{f(r)} {f(r)} 0 0 1 {f(l1)} {f(y1)}Z", fill)

@reg("libreoffice-base", PURPLE_DEEP)
def lo_base():
    can = (rrect(21, 23, 10, 17, 4, HOLE) + stroke("M21.5 28.5Q26 30.5 30.5 28.5", INK, 2.2)
           + stroke("M21.5 34Q26 36 30.5 34", INK, 2.2))
    cells = "".join(rrect(33.5 + c * 4.8, 23 + r * 5.8, 3.8, 4.4, 1, HOLE)
                    for r in range(3) for c in range(2))
    return _doc(can + cells, PURPLE_SOFT)

@reg("libreoffice-chart", GREY_DARK)
def lo_chart():
    bars = "".join(rrect(x, 42 - h, 4.4, h, 1.2, HOLE)
                   for x, h in [(21.5, 8), (27, 15), (32.5, 11), (38, 18)])
    return _doc(bars, GREY_SOFT)

@reg("libreoffice-draw", AMBER_DEEP)
def lo_draw():
    shapes = (circle(26, 28, 5, HOLE) + _ring(37.5, 29, 3.8, HOLE, 2.4)
              + poly([(23, 43), (30, 33), (37, 43)], HOLE, 1.5))
    return _doc(shapes, AMBER_SOFT)

@reg("libreoffice-main", BLUE_GREY_DEEP)
def lo_main():
    return _doc("", BLUE_GREY_SOFT)

@reg("libreoffice-math", PINK_DEEP)
def lo_math():
    root = stroke("M20.5 32H23L26 39L29.5 25H33", HOLE, 2.4)
    x = line(34.5, 29, 40.5, 36, HOLE, 2.4) + line(40.5, 29, 34.5, 36, HOLE, 2.4)
    return _doc(root + x + rrect(21, 42, 20, 2.4, 1.2, HOLE), PINK_SOFT)

@reg("librewolf", LIGHT_BLUE_DEEP)
def librewolf():
    wolf = path("M24 45C22.5 38 23 32.5 26 28.5L26.5 20.5L30.5 25.5C32.5 24 35 22.5 37 20.5"
                "L42.5 15L41.5 21.5L38.5 25.5L41 27L36.5 29.5C35.5 33 36.5 38 39.5 43.5"
                "C35 46.5 28.5 46.8 24 45Z", INK)
    return _ring(CX, CY, 15.5, INK, 3.2) + wolf

@reg("liferea", BLUE_DEEP)
def liferea():
    sheet = rrect(19, 13, 29, 30, 3, INK)
    lines = (rrect(23, 17, 13, 4, 1.5, HOLE)
             + "".join(rrect(33.5, y, 10.5, 2.6, 1.3, HOLE) for y in (26, 31, 36)))
    globe = (circle(24, 38, 10, HOLE) + circle(24, 38, 7.8, INK)
             + stroke("M16.5 38H31.5", HOLE, 1.8) + ell_c(24, 38, 3.2, 7.6, HOLE)
             + ell_c(24, 38, 1.4, 7.6, INK))
    return sheet + lines + globe

@reg("linconnect", ORANGE_DEEP)
def linconnect():
    return (f'<rect x="19.5" y="15.5" width="25" height="19" rx="3" fill="none" stroke="{INK}" stroke-width="4.2"/>'
            + rrect(14, 38.5, 36, 5.5, 2.75, INK))

@reg("linphone", DEEP_ORANGE)
def linphone():
    hand = path("M20 16.5C18 16.5 16 18.5 16.5 21.5C18 33.5 26.5 42 38.5 43.5"
                "C41.5 44 43.5 42 43.5 40V36.5L37 33.5L34 36.5C29 34.5 25.5 31 23.5 26L26.5 23L23.5 16.5Z", INK)
    waves = (stroke("M33 14.5A12 12 0 0 1 45 26.5", INK, 3.2)
             + stroke("M32.5 21A5.5 5.5 0 0 1 38 26.5", INK, 3.2))
    return hand + waves

@reg("linuxdcpp", DEEP_ORANGE_DEEP)
def linuxdcpp():
    sep = f' stroke="{HOLE}" stroke-width="1.8"'
    return (circle(25.5, 23.5, 9.5, INK, sep) + circle(28, 37.5, 8, DEEP_ORANGE_SOFT, sep)
            + circle(40, 30, 8.5, BLUE_GREY_DARK, sep))

@reg("lightcord", RED_DEEP)
def lightcord():
    return shared_discord()

@reg("listen.moe-desktop-app", BLUE_GREY_DARK)
def listen_moe():
    return stroke("M20 29V18H31", INK, 5) + stroke("M44 31V42H33", PINK_LIGHT, 5)

@reg("localsend_app", TEAL_DEEP)
def localsend():
    segs = ""
    for k in range(8):
        a0, a1 = -90 + 45 * k + 8, -90 + 45 * k + 37
        x0, y0 = pt(CX, CY, 14, a0)
        x1, y1 = pt(CX, CY, 14, a1)
        segs += stroke(f"M{f(x0)} {f(y0)}A14 14 0 0 1 {f(x1)} {f(y1)}", INK, 5)
    return segs + circle(CX, CY, 7.5, INK)

@reg("loginized", TEAL_LIGHT)
def loginized():
    field = rrect(13, 22.5, 38, 15, 5, INK)
    stars = ""
    for cx in (21.5, 32, 42.5):
        for a in (90, 30, 150):
            x0, y0 = pt(cx, 30, 3.6, a)
            x1, y1 = pt(cx, 30, 3.6, a + 180)
            stars += line(x0, y0, x1, y1, HOLE, 2.3)
    return field + stars

@reg("litecoin-qt", BLUE_DARK)
def litecoin():
    l = path("M29.5 17H35.5L33 27.5L38 25.5L37 29.5L32 31.5L30.5 37.5H42L40.8 42.5H23.5L25.2 35.5"
             "L21 37.2L22 33.2L26.3 31.5Z", HOLE)
    return circle(CX, CY, 16.5, INK) + l

@reg("libation", GREY_DARK)
def libation():
    glass = stroke("M23.5 13H40.5C41 21.5 38 28.5 32 29.5C26 28.5 23 21.5 23.5 13Z", INK, 3)
    wine = path("M24.5 20H39.5C39 25 36.5 27.5 32 28C27.5 27.5 25 25 24.5 20Z", INK)
    return glass + wine + line(32, 30, 32, 43.5, INK, 3.2) + line(25, 45, 39, 45, INK, 3.4)

@reg("libinput-gestures", BLUE_DEEP)
def libinput():
    rip = _ring(30, 18, 6.5, INK, 2.4)
    hand = (rrect(26.5, 16, 7, 24, 3.5, INK) + rrect(26.5, 30, 19, 17, 6, INK)
            + rrect(33, 26.5, 6, 11, 3, INK) + rrect(39.5, 28.5, 6, 11, 3, INK)
            + line(27, 40, 20, 33, INK, 5.5))
    sep = (stroke("M33.2 27V33", HOLE, 1.4) + stroke("M39.5 29V34", HOLE, 1.4))
    return rip + circle(30, 18, 4.3, HOLE) + hand + sep

@reg("librecad", ORANGE_DEEP)
def librecad():
    return (_ring(CX, CY, 13, INK, 5.5) + rrect(13, 26.5, 38, 7, 3.5, INK, f' stroke="{HOLE}" stroke-width="1.6"')
            + rrect(13, 24.5, 8, 11, 3, INK))

@reg("lightsoff", BLUE_GREY_DARK)
def lightsoff():
    lit = rrect(33, 13, 15, 15, 3.5, INK) + rrect(16, 30, 15, 15, 3.5, INK)
    off = rrect(16, 13, 15, 15, 3.5, BLUE_GREY) + rrect(33, 30, 15, 15, 3.5, BLUE_GREY)
    return lit + off

@reg("lite", BLUE_GREY_DARK)
def lite():
    rows = [(14, [(24, 8, INK), (33, 6, PINK_SOFT), (40, 3, INK)]),
            (20.5, [(24, 12, BLUE_GREY_SOFT), (37, 9, BLUE_GREY_SOFT)]),
            (27, [(24, 6, INK), (31, 17, PINK_SOFT)]),
            (33.5, [(28, 10, PINK_SOFT), (39, 7, ORANGE_LIGHT)]),
            (40, [(24, 7, INK), (32, 6, PINK_SOFT), (39, 9, INK)])]
    out = ""
    for y, bars in rows:
        out += rrect(15, y, 6, 3.8, 1.9, BLUE_GREY_LIGHT)
        for x, w, c in bars:
            out += rrect(x, y, w, 3.8, 1.9, c)
    return g(out, "translate(0 1.5)")

@reg("liteide", BLUE_GREY_DEEP)
def liteide():
    swirl = path("M32 13.5A16.5 16.5 0 0 1 32 46.5A8.25 8.25 0 0 1 32 30A8.25 8.25 0 0 0 32 13.5Z", HOLE)
    dots = circle(32, 21.75, 2.6, HOLE) + circle(32, 38.25, 2.6, INK)
    return circle(CX, CY, 16.5, INK) + g(swirl + dots, "rotate(-50 32 30)") + _ring(CX, CY, 16.5, INK, 2.2)

@reg("litesoundsloc", BLUE_DARK)
def litesoundsloc():
    band = stroke("M17.5 34V29A14.5 14.5 0 0 1 46.5 29V34", INK, 4)
    cups = rrect(13.5, 29, 8, 14, 3.5, INK) + rrect(42.5, 29, 8, 14, 3.5, INK)
    zig = stroke("M22 34L27 34L29.5 24L33 44L36.5 30L38.5 34H42", RED_SOFT, 3)
    return band + cups + zig

@reg("litetweaks", RED_DEEP)
def litetweaks():
    handle = rrect(11, 24.5, 20, 11, 4.5, INK)
    grooves = "".join(rrect(15 + 4.5 * k, 27.5, 2.4, 5, 1.2, HOLE) for k in range(3))
    collar = rrect(29.5, 26.5, 5, 7, 1.5, INK)
    shaft = line(34, 30, 49, 30, INK, 3.4) + poly([(48, 28), (53, 30), (48, 32)], INK, 1.5)
    return g(handle + grooves + collar + shaft, "rotate(38 32 30)")

@reg("liteupgrade", TEAL_DEEP)
def liteupgrade():
    arrow = line(32, 13, 32, 31, INK, 5) + stroke("M23.5 23.5L32 32L40.5 23.5", INK, 5)
    return arrow + stroke("M17 32.5V42.5H47V32.5", INK, 5)

@reg("live-usb-kernel-updater", BLUE_GREY_DEEP)
def live_usb():
    plug = (f'<rect x="22.5" y="12" width="17" height="10.5" rx="1.5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
            + rrect(26, 15.5, 3.2, 3, 0.6, INK) + rrect(33, 15.5, 3.2, 3, 0.6, INK))
    body = rrect(17.5, 22, 27, 25, 4, INK)
    badge = circle(43, 40, 9, PURPLE_LIGHT, f' stroke="{HOLE}" stroke-width="2"')
    arrow = (stroke("M46.8 39.5A3.9 3.9 0 1 1 43.2 36", INK, 2.3)
             + poly([(42.5, 33.2), (46.2, 36), (42.5, 38.6)], INK, 1))
    return plug + body + badge + arrow

@reg("livepatch", DEEP_ORANGE_DEEP)
def livepatch():
    r, a0, a1 = 13.5, 205, 155 + 360
    x0, y0 = pt(CX, CY, r, a0)
    x1, y1 = pt(CX, CY, r, a1)
    arc = stroke(f"M{f(x0)} {f(y0)}A{r} {r} 0 1 1 {f(x1)} {f(y1)}", INK, 5)
    tip = pt(x1, y1, 5.5, a1 + 90)
    b1 = pt(x1, y1, 5.5, a1)
    b2 = pt(x1, y1, 5.5, a1 + 180)
    b1 = pt(b1[0], b1[1], 1.5, a1 - 90)
    b2 = pt(b2[0], b2[1], 1.5, a1 - 90)
    return arc + poly([tip, b1, b2], INK, 2)

@reg("lives", BLUE_GREY_DEEP)
def lives():
    film = rrect(14, 13, 30, 29, 3, INK)
    frames = rrect(21.5, 16, 15, 10, 1.5, HOLE) + rrect(21.5, 29, 15, 10, 1.5, HOLE)
    holes = "".join(rrect(x, y, 3, 3, 0.8, HOLE) for x in (16.5, 38.5) for y in (16, 22, 28, 34))
    badge = circle(43, 40, 9, AMBER_DEEP, f' stroke="{HOLE}" stroke-width="2"')
    sc = (line(39.5, 36, 46, 43.5, INK, 2.3) + line(46.5, 36, 40, 43.5, INK, 2.3)
          + circle(39.8, 44, 2, INK) + circle(46.2, 44, 2, INK))
    return film + frames + holes + badge + sc

def _screen(bubbles):
    return (rrect(14, 14, 36, 25, 3.5, INK) + bubbles
            + rrect(27, 38, 10, 5, 0, INK) + rrect(20, 42, 24, 4, 2, INK))

@reg("livewallpaper", LIGHT_BLUE_DEEP)
def livewallpaper():
    return _screen(circle(22, 28, 3.5, HOLE) + circle(27, 20, 2, HOLE) + circle(39, 22, 5, HOLE)
                   + circle(34, 31, 2.8, HOLE) + circle(44.5, 31, 2.2, HOLE))

@reg("livewallpaper-config", BLUE_DEEP)
def livewallpaper_config():
    base = _screen(circle(22, 28, 3.5, HOLE) + circle(27, 20, 2, HOLE) + circle(36, 21, 4.5, HOLE))
    badge = circle(43, 40, 9, PURPLE, f' stroke="{HOLE}" stroke-width="2"')
    teeth = "".join(g(rrect(41.6, 33.8, 2.8, 12.4, 1, INK), f"rotate({a} 43 40)") for a in (0, 60, 120))
    return base + badge + teeth + circle(43, 40, 4.4, INK) + circle(43, 40, 1.8, PURPLE)

@reg("logisim-icon", BLUE_GREY_DEEP)
def logisim():
    wires = (line(13, 24.5, 24, 24.5, TEAL_SOFT, 3.4) + line(13, 35.5, 24, 35.5, TEAL_SOFT, 3.4)
             + line(42, 30, 51, 30, GREY_SOFT, 3.4))
    gate = path("M19.5 17.5C28 17.5 38 20 44.5 30C38 40 28 42.5 19.5 42.5C23 36 23 24 19.5 17.5Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return wires + gate

@reg("lookit", BLUE_GREY)
def lookit():
    cloud = (circle(23.5, 33, 8, INK) + circle(34, 27, 11, INK) + circle(43, 34.5, 6.5, INK)
             + rrect(16, 33, 33.5, 8, 4, INK))
    return cloud + _ring(33.5, 33, 6, HOLE, 2.8) + circle(33.5, 33, 2.4, HOLE)

@reg("losslesscut", CYAN_DEEP)
def losslesscut():
    arm = rrect(15, 18, 33, 6.5, 1.5, INK)
    arm_stripes = "".join(poly([(x, 18.5), (x + 3.5, 18.5), (x + 1.5, 24), (x - 2, 24)], HOLE)
                          for x in (21, 29, 37))
    body = rrect(15, 27, 34, 19, 2.5, INK)
    body_stripes = "".join(poly([(x, 27.5), (x + 3.5, 27.5), (x + 1.5, 32), (x - 2, 32)], HOLE)
                           for x in (20, 28, 36, 44))
    return g(arm + arm_stripes, "rotate(-14 15.5 24.5)") + body + body_stripes

@reg("lplayer", BLUE_GREY_DEEP)
def lplayer():
    disc = circle(CX, CY, 16.5, INK) + _ring(CX, CY, 11.5, HOLE, 1.6)
    centre = (circle(CX, CY, 7.6, HOLE) + path("M32 23.6A6.4 6.4 0 0 0 32 36.4Z", RED)
              + path("M32 23.6A6.4 6.4 0 0 1 32 36.4Z", INK) + circle(CX, CY, 2, HOLE))
    return disc + centre

@reg("life-is-strange", PINK_DARK)
def life_is_strange():
    frame = rrect(16, 12, 32, 37, 3, INK) + rrect(19.5, 15.5, 25, 25, 1.5, HOLE)
    i = line(26, 20.5, 26, 35.5, INK, 3.4)
    s = stroke("M40 21.8C39 20.3 37.6 19.8 36 19.8C33.6 19.8 32 21.3 32 23.5C32 28.5 40.3 26.8 40.3 32"
               "C40.3 34.5 38.4 36.2 36 36.2C34 36.2 32.6 35.4 31.6 34", INK, 3.2)
    return frame + i + s

@reg("lifeograph", ORANGE_DEEP)
def lifeograph():
    book = rrect(17, 13, 30, 34, 3.5, INK) + rrect(37, 13, 2.4, 34, 0, HOLE)
    key = (circle(26.5, 22.5, 5.5, HOLE) + circle(26.5, 22.5, 2.2, INK)
           + rrect(25, 26, 3, 16, 1.5, HOLE) + rrect(27, 34, 4.5, 2.8, 1.4, HOLE)
           + rrect(27, 38.5, 3.5, 2.8, 1.4, HOLE))
    return book + key

@reg("lightworks", RED_DEEP)
def lightworks():
    head = path("M14.5 35C14 24 22 15.5 34 15C42 14.7 47.5 18.5 50 24L37 29L50 34"
                "C47.5 41 41 46 31 46C22 46 15 42 14.5 35Z", INK)
    fin = poly([(19, 21), (17.5, 11.5), (27, 16.5)], INK, 2)
    teeth = "".join(poly([(x, 25.2 + (x - 40) * 0.3), (x + 3, 24.2 + (x - 40) * 0.3), (x + 1.8, 28.2 + (x - 40) * 0.3)], INK)
                    for x in (40, 44.5))
    teeth += "".join(poly([(x, 33.5 + (40 - x) * 0.3), (x + 3, 34.5 + (40 - x) * 0.3), (x + 1.2, 30.5 + (40 - x) * 0.3)], INK)
                     for x in (40, 44.5))
    mouth = poly([(50.5, 24), (36, 29.5), (50.5, 34)], HOLE, 1)
    eye = circle(36, 21.5, 2.2, HOLE)
    gill = stroke("M28 27Q30 31 28 35", HOLE, 1.8)
    return fin + head + mouth + teeth + eye + gill

@reg("lightzone", BLUE_GREY_DARK)
def lightzone():
    egg = path("M32 12C40 12 46.5 24 46.5 33C46.5 42 40.5 48 32 48C23.5 48 17.5 42 17.5 33"
               "C17.5 24 24 12 32 12Z", INK)
    return egg + circle(32, 35, 8.5, AMBER)

@reg("limbo", GREY_LIGHT)
def limbo():
    head = path("M22 30C20.5 22.5 24 16 30.5 14.5L32.5 10.5L35 14L39.5 11.5L39.5 15.5L45 15L42.5 19"
                "C45 21.5 46 25.5 45 29.5C44 34 41 37 37.5 38L38 42C42 43 46 45 47.5 48.5H16.5"
                "C18 45 22 43 26.5 42L27 38C24.5 36.5 22.5 33.5 22 30Z", INK)
    return head + circle(32.5, 28.5, 1.9, HOLE) + circle(39, 28, 1.9, HOLE)

@reg("liquidwar", BLUE_DEEP)
def liquidwar():
    r = 16.5

    def blob(y, colour, wob):
        dx = math.sqrt(r * r - (y - CY) ** 2)
        l, rt = CX - dx, CX + dx
        big = 1 if y < CY else 0
        return path(f"M{f(l)} {f(y)}C{f(l + 9)} {f(y - wob)} {f(rt - 12)} {f(y + wob)} {f(rt)} {f(y)}"
                    f"A{r} {r} 0 {big} 1 {f(l)} {f(y)}Z", colour)
    return (circle(CX, CY, r, INK) + blob(20, RED, 7) + blob(28, AMBER, -7)
            + blob(37, LIGHT_BLUE, 6))

@reg("liri", RED)
def liri():
    bird = poly([(15, 15), (31, 26.5), (41.5, 20), (50, 22), (44.5, 26.5), (43, 36),
                 (33, 43), (15.5, 45), (26, 37.5), (23, 29)], INK, 2.5)
    fold = poly([(31, 26.5), (38, 25), (33, 33)], HOLE, 1)
    return bird + fold

@reg("little-inferno", ORANGE_LIGHT)
def little_inferno():
    cap = rrect(18.5, 12, 27, 7.5, 2, INK)
    shaft = poly([(22, 19), (42, 19), (40, 48), (24, 48)], INK, 1.5)
    bricks = (rrect(26, 24, 8, 2.6, 1, HOLE) + rrect(31, 30.5, 7, 2.6, 1, HOLE)
              + rrect(26.5, 37, 6, 2.6, 1, HOLE))
    return cap + shaft + bricks

@reg("littleweeb", PINK_LIGHT)
def littleweeb():
    hair = path("M32 12C22.5 12 18 19.5 18 27.5C18 35.5 16 41.5 13.5 47.5H24.5L26.5 40.5"
                "C29 41.5 35 41.5 37.5 40.5L39.5 47.5H50.5C48 41.5 46 35.5 46 27.5C46 19.5 41.5 12 32 12Z",
                AMBER_SOFT)
    face = path("M24.5 25C27 23.5 29.5 22 31 19.5C33 22.5 36.5 24 39.5 24.5C39.5 32 36.5 38 32 38"
                "C27.5 38 24.5 32.5 24.5 25Z", INK)
    return hair + face

@reg("lmms", BLUE_GREY)
def lmms():
    return stroke("M24.5 45H17.5V22.5L32 14L46.5 22.5V45H39.5V36.5C39.5 32 36.5 29 32 29"
                  "C27.5 29 24.5 32 24.5 36.5Z", INK, 5)

@reg("logseq", TEAL_DARK)
def logseq():
    return (g(ell_c(23.5, 21, 5.2, 3.8, INK), "rotate(35 23.5 21)")
            + g(ell_c(35, 17, 4, 2.6, INK), "rotate(-15 35 17)")
            + g(ell_c(33, 35.5, 14, 9.5, INK), "rotate(-6 33 35.5)"))

@reg("lollypop", PINK)
def lollypop():
    blades = ""
    for k in range(7):
        a = -90 + k * 360 / 7
        p0 = pt(CX, CY, 7.5, a)
        c0 = pt(CX, CY, 13, a + 30)
        p1 = pt(CX, CY, 16.5, a + 50)
        p2 = pt(CX, CY, 16.5, a + 78)
        c1 = pt(CX, CY, 12, a + 50)
        p3 = pt(CX, CY, 7.5, a + 26)
        blades += path(f"M{f(p0[0])} {f(p0[1])}Q{f(c0[0])} {f(c0[1])} {f(p1[0])} {f(p1[1])}"
                       f"A16.5 16.5 0 0 1 {f(p2[0])} {f(p2[1])}Q{f(c1[0])} {f(c1[1])} {f(p3[0])} {f(p3[1])}Z", HOLE)
    play = poly([(29.5, 25.5), (36.5, 30), (29.5, 34.5)], HOLE, 1.5)
    return circle(CX, CY, 16.5, INK) + blades + play

@reg("love", PINK)
def love():
    x0, y0 = pt(CX, CY, 17, -60)
    x1, y1 = pt(CX, CY, 17, 120)
    blue = path(f"M{f(x0)} {f(y0)}A17 17 0 0 1 {f(x1)} {f(y1)}Z", BLUE)
    return blue + _heart(32, 30.5, 0.72, INK)

def _planet(cx=CX, cy=CY, r=16.5):
    bands = [(-1, 20, GREY_SOFT), (20, 26.5, CYAN_DEEP), (26.5, 33, AMBER_SOFT),
             (33, 39.5, RED_LIGHT), (39.5, 61, CYAN_DEEP)]
    out = ""
    for y1, y2, c in bands:
        y1 = max(cy + (y1 - 30) * r / 16.5, cy - r + 0.01)
        y2 = min(cy + (y2 - 30) * r / 16.5, cy + r - 0.01)
        out += _band(r, y1, y2, c, cx, cy)
    return g(out, f"rotate(-14 {f(cx)} {f(cy)})")

@reg("lovely-planet", BLUE_GREY_DARK)
def lovely_planet():
    return _planet()

@reg("lovely-planet-2", BLUE_GREY_DARK)
def lovely_planet_2():
    badge = circle(43, 40, 9, RED, f' stroke="{HOLE}" stroke-width="2"')
    return _planet(30, 28, 15.5) + badge + _heart(43, 40.5, 0.3, INK)

@reg("lovely-planet-arcade", CYAN_DEEP)
def lovely_planet_arcade():
    body = path("M16 48.5C16 42.5 22 39.5 32 39.5C42 39.5 48 42.5 48 48.5Z", INK)
    face = rrect(22.5, 19.5, 19, 18, 4, INK)
    eyes = rrect(25.5, 26, 4, 4, 0.8, HOLE) + rrect(34.5, 26, 4, 4, 0.8, HOLE)
    hat = poly([(19, 22), (32, 12.5), (45, 22)], RED_SOFT, 2)
    return body + face + eyes + hat

@reg("lovers-in-a-dangerous-spacetime", PINK_DEEP)
def lovers():
    heart = _heart(32, 30.5, 1.05, INK)
    left = circle(25.5, 27, 3.8, HOLE) + rrect(22.5, 31.5, 6, 8, 2.5, HOLE)
    right = (rrect(34.5, 23, 8, 7, 2, HOLE) + line(38.5, 22.5, 38.5, 19, HOLE, 1.8)
             + rrect(35, 31.5, 7, 8, 2.5, HOLE))
    return heart + left + right

@small("libreoffice-base")
def lo_base_s():
    can = (rrect(21, 23, 21, 19, 6, HOLE) + stroke("M22 30Q31.5 33 41 30", INK, 3)
           + stroke("M22 36Q31.5 39 41 36", INK, 3))
    return _doc(can, PURPLE_SOFT)

@small("libreoffice-chart")
def lo_chart_s():
    bars = "".join(rrect(x, 42 - h, 6, h, 1.5, HOLE) for x, h in [(21.5, 9), (29, 17), (36.5, 12)])
    return _doc(bars, GREY_SOFT)

@small("libreoffice-draw")
def lo_draw_s():
    return _doc(circle(27, 28, 6, HOLE) + poly([(23, 43), (32, 31), (41, 43)], HOLE, 2), AMBER_SOFT)

@small("libreoffice-math")
def lo_math_s():
    return _doc(stroke("M20.5 31H23.5L27 40L31 24H42", HOLE, 3.2), PINK_SOFT)

@small("liferea")
def liferea_s():
    sheet = rrect(19, 13, 29, 30, 3, INK) + rrect(34, 24, 10, 3.5, 1.7, HOLE) + rrect(34, 31, 10, 3.5, 1.7, HOLE)
    return sheet + circle(24, 38, 10.5, HOLE) + circle(24, 38, 8, INK) + ell_c(24, 38, 3, 8, HOLE)

@small("lightworks")
def lightworks_s():
    head = path("M14.5 35C14 24 22 15.5 34 15C42 14.7 47.5 18.5 50 24L36 29.5L50 35"
                "C47.5 41 41 46 31 46C22 46 15 42 14.5 35Z", INK)
    return poly([(19, 21), (17.5, 11.5), (27, 16.5)], INK, 2) + head + circle(35, 21.5, 2.6, HOLE)

@small("lite")
def lite_s():
    out = ""
    for y, bars in [(16, [(24, 12, INK), (38, 8, PINK_SOFT)]), (26, [(24, 20, PINK_SOFT)]),
                    (36, [(24, 8, INK), (34, 10, PINK_SOFT)])]:
        out += rrect(15, y, 6, 5.5, 2.75, BLUE_GREY_LIGHT)
        for x, w, c in bars:
            out += rrect(x, y, w, 5.5, 2.75, c)
    return out

@small("live-usb-kernel-updater")
def live_usb_s():
    plug = f'<rect x="22.5" y="12.5" width="17" height="10" rx="1.5" fill="none" stroke="{INK}" stroke-width="3"/>'
    return plug + rrect(17.5, 22, 27, 25, 4, INK) + circle(43, 40, 9.5, PURPLE_LIGHT, f' stroke="{HOLE}" stroke-width="2"')

@small("lives")
def lives_s():
    film = rrect(14, 13, 30, 29, 3, INK) + rrect(21, 17, 16, 21, 2, HOLE)
    return film + circle(43, 40, 9.5, AMBER_DEEP, f' stroke="{HOLE}" stroke-width="2"')

@small("livewallpaper-config")
def livewallpaper_config_s():
    base = _screen(circle(22, 25, 4, HOLE) + circle(33, 22, 4, HOLE))
    return base + circle(43, 40, 9.5, PURPLE, f' stroke="{HOLE}" stroke-width="2"') + _ring(43, 40, 3.8, INK, 3)

@small("lovely-planet-2")
def lovely_planet_2_s():
    badge = circle(43, 40, 10, RED, f' stroke="{HOLE}" stroke-width="2"')
    return _planet(30, 28, 15.5) + badge + _heart(43, 40.5, 0.4, INK)

@small("lovers-in-a-dangerous-spacetime")
def lovers_s():
    return _heart(32, 30.5, 1.05, INK) + circle(26, 27, 4.5, HOLE) + rrect(34, 22.5, 9, 9, 2.5, HOLE)

@small("loginized")
def loginized_s():
    return rrect(13, 21.5, 38, 17, 5.5, INK) + "".join(circle(x, 30, 3.4, HOLE) for x in (21.5, 32, 42.5))

@small("linuxdcpp")
def linuxdcpp_s():
    sep = f' stroke="{HOLE}" stroke-width="2"'
    return (circle(25.5, 23.5, 10, INK, sep) + circle(28, 38, 8.5, DEEP_ORANGE_SOFT, sep)
            + circle(40.5, 30, 9, BLUE_GREY_DARK, sep))

@small("libinput-gestures")
def libinput_s():
    return (rrect(25.5, 13, 8, 26, 4, INK) + rrect(25.5, 29, 21, 19, 6.5, INK)
            + line(27, 40, 19.5, 32.5, INK, 6))

@small("lollypop")
def lollypop_s():
    blades = ""
    for k in range(5):
        a = -90 + k * 72
        p0, c0, p1 = pt(CX, CY, 6, a), pt(CX, CY, 13, a + 35), pt(CX, CY, 17, a + 55)
        p2, c1, p3 = pt(CX, CY, 17, a + 90), pt(CX, CY, 11, a + 60), pt(CX, CY, 6, a + 35)
        blades += path(f"M{f(p0[0])} {f(p0[1])}Q{f(c0[0])} {f(c0[1])} {f(p1[0])} {f(p1[1])}"
                       f"A17 17 0 0 1 {f(p2[0])} {f(p2[1])}Q{f(c1[0])} {f(c1[1])} {f(p3[0])} {f(p3[1])}Z", HOLE)
    return circle(CX, CY, 17, INK) + blades

@small("lplayer")
def lplayer_s():
    return (circle(CX, CY, 17, INK) + circle(CX, CY, 9, HOLE)
            + path("M32 22A8 8 0 0 0 32 38Z", RED) + path("M32 22A8 8 0 0 1 32 38Z", INK))

@small("lookit")
def lookit_s():
    cloud = (circle(23.5, 33, 8, INK) + circle(34, 27, 11, INK) + circle(43, 34.5, 6.5, INK)
             + rrect(16, 33, 33.5, 8, 4, INK))
    return cloud + _ring(33.5, 32, 6, HOLE, 3.6)

@small("liteide")
def liteide_s():
    swirl = path("M32 13.5A16.5 16.5 0 0 1 32 46.5A8.25 8.25 0 0 1 32 30A8.25 8.25 0 0 0 32 13.5Z", HOLE)
    return circle(CX, CY, 16.5, INK) + g(swirl, "rotate(-50 32 30)") + _ring(CX, CY, 16.5, INK, 2.6)

@small("liri")
def liri_s():
    return poly([(15, 15), (31, 26.5), (41.5, 20), (50, 22), (44.5, 26.5), (43, 36),
                 (33, 43), (15.5, 45), (26, 37.5), (23, 29)], INK, 3)
