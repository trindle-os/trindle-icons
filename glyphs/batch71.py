# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 71: urserver to vita3k.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the palette.
"""
from lm import *
from glyphs.kit import _gear_l, registry, _ring

ICONS, SMALL, reg, small = registry()

@reg("urserver", INDIGO_SOFT)
def urserver():
    return (circle(21, 40, 4.2, INK) + stroke("M17 27.5A14.5 14.5 0 0 1 33.5 44", INK, 4.6)
            + stroke("M17 16.5A25.5 25.5 0 0 1 44.5 44", INK, 4.6))

def _usb(col, s=1.0):
    trunk = line(32, 18, 32, 42, col, 3.2 * s)
    head = poly([(32, 11.5), (37, 18.5), (27, 18.5)], col, 1.5)
    left = stroke("M32 35L22.5 29V24.5", col, 3 * s) + circle(22.5, 23, 3.3, col)
    right = stroke("M32 31.5L41.5 26V21.5", col, 3 * s) + rrect(38.5, 17.5, 6, 6, 1, col)
    return trunk + head + left + right + circle(32, 43.5, 4.5, col)

@reg("usb", INDIGO)
def usb():
    return _usb(INK)

@reg("usb-creator", GREY_DARK)
def usb_creator():
    plug = rrect(21, 11, 16, 9, 2, INK) + rrect(24.5, 13.5, 3.5, 3, .6, HOLE) + rrect(30, 13.5, 3.5, 3, .6, HOLE)
    body = rrect(17, 19, 24, 27, 4, INK)
    badge = circle(41, 39, 9.5, BLUE_LIGHT) + stroke("M41 33.5V43.5M37 40L41 44L45 40", INK, 2.8)
    return plug + body + circle(41, 39, 11.5, HOLE) + badge

@reg("usbguard-icon", LIGHT_BLUE_DEEP)
def usbguard():
    shield = path("M17 14H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    gee = stroke("M38 22.5A8 8 0 1 0 39.5 31H32.5", HOLE, 4)
    return shield + gee

@reg("utilities-log-viewer", BLUE_GREY)
def log_viewer():
    sheet = rrect(15, 12, 28, 34, 3.5, INK)
    lines = "".join(rrect(19, y, w, 2.6, 1.3, HOLE) for y, w in
                    [(17, 20), (22, 14), (27, 20), (32, 10), (37, 16)])
    glass = circle(36.5, 32, 8.8, HOLE) + _ring(36.5, 32, 6.3, INK, 3.4)
    handle = line(41.5, 37, 47.5, 43, INK, 4.2)
    return sheet + lines + glass + handle

@reg("utilities-system-monitor", BLUE_GREY)
def system_monitor():
    return stroke("M14 32H20.5L24.5 21L30 42L35.5 16L40 36L43.5 28H50", INK, 4)

def _prompt(chev, bar):
    return stroke("M18 20L28 29.5L18 39", chev, 5) + rrect(31, 36.5, 16, 5, 2.5, bar)

@reg("utilities-terminal_su", RED)
def terminal_su():
    return _prompt(INK, INK)

@reg("utilities-x-terminal", BLUE_GREY_DARK)
def x_terminal():
    return _prompt(CYAN_LIGHT, CYAN_LIGHT)

@reg("utilities-tweak-tool", TEAL_DEEP)
def tweak_tool():
    gear = _gear_l(32, 27, 16, 12.5, 8, INK) + circle(32, 27, 7.5, HOLE)
    wrench = (stroke("M32 27V45", HOLE, 7.5) + stroke("M32 29V44", INK, 3.4)
              + path("M28.5 21.5V26.5L32 29L35.5 26.5V21.5A6 6 0 1 1 28.5 21.5Z", INK))
    return gear + wrench

@reg("utools", BLUE_GREY_DARK)
def utools():
    arm = rrect(25.8, 34.5, 5.2, 14, 2.6, INK) + rrect(33, 34.5, 5.2, 14, 2.6, INK)
    return "".join(g(arm, f"rotate({120 * k} 32 30)") for k in range(3))

@reg("utox", BLUE_GREY_DEEP)
def utox():
    lock = path("M22 22A10 10 0 0 1 42 22V27H45A3 3 0 0 1 48 30V45A3 3 0 0 1 45 48H19"
                "A3 3 0 0 1 16 45V30A3 3 0 0 1 19 27H22Z", INK)
    bubble = path("M32 13.5A5.8 5.8 0 0 1 34.5 24.5L35 27.5L31.5 25.3A5.8 5.8 0 0 1 32 13.5Z", HOLE)
    person = circle(32, 33.5, 3.6, HOLE) + path("M25.5 45A6.5 6 0 0 1 38.5 45Z", HOLE)
    return lock + bubble + person

@reg("vacuum", BLUE_GREY_DARK)
def vacuum():
    return stroke("M20.5 22.5L32 41L44.5 18", INK, 6.5) + circle(19, 19.5, 4.6, INK)

@reg("valheim", BROWN_DARK)
def valheim():
    v = poly([(15, 14), (26, 14), (24.5, 16.5), (32, 38), (39.5, 16.5), (38, 14), (49, 14),
              (45.5, 17), (33.5, 47), (30.5, 47), (18.5, 17)], ORANGE_LIGHT, 1.5)
    inner = poly([(24.5, 17.5), (28, 17.5), (32, 30), (32, 38)], ORANGE_DEEP, 1)
    return v + inner

@reg("valyriatear", BROWN_LIGHT)
def valyriatear():
    return stroke("M15.5 25C18 18.5 23.5 18 25 25L28 44C34 33 40 22 47.5 15.5"
                  "C44 17 40 17 38.5 21", INK, 4.4)

@reg("variety", ORANGE_DEEP)
def variety():
    screen = rrect(14, 13, 36, 27, 3.5, INK) + rrect(18, 17, 28, 19, 1.5, HOLE)
    hills = path("M18 33C22 27 26 26 30 30C34 25 40 22 46 26V36H18Z", INK) + circle(40, 22, 2.5, INK)
    stand = rrect(24, 43, 16, 4, 2, INK) + rrect(29.5, 39, 5, 5, 0, INK)
    return screen + hills + stand

@reg("vbam", DEEP_PURPLE)
def vbam():
    body = path("M22 18H42C48 18 51 21 51 27V33C51 39 48 42 42 42H22C16 42 13 39 13 33V27"
                "C13 21 16 18 22 18Z", INK)
    screen = rrect(24.5, 21.5, 15, 17, 1.5, HOLE)
    pad = rrect(15.5, 28.3, 7, 3.4, 1, HOLE) + rrect(17.3, 26.5, 3.4, 7, 1, HOLE)
    btns = circle(43.5, 32, 2.4, HOLE) + circle(47.3, 28.2, 2.4, HOLE)
    return body + screen + pad + btns

@reg("vdrift", BLUE_DEEP)
def vdrift():
    left = poly([(14, 15), (23, 15), (34, 45), (26.5, 45)], INK, 2)
    right = path("M34 45C36 34 40 22 50 16V25C44 29 40 36 37.5 45Z", BLUE_SOFT,
                 ' stroke="#6FBAF6" stroke-width="2" stroke-linejoin="round"')
    return left + right

@reg("vectr", GREY_DARK)
def vectr():
    return (poly([(16, 16), (26, 16), (33, 34), (30, 44)], INK, 2.5)
            + poly([(42, 16), (48, 16), (33.5, 45), (30.5, 40)], INK, 2))

@reg("veloren", BROWN_DEEP)
def veloren():
    box = rrect(15, 13, 34, 34, 7, LIGHT_BLUE_DEEP)
    v = path("M20 18H28.5L27 21L32 34L37 21L35.5 18H44L35 41.5H29Z", INK,
             f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return box + v

@reg("ventoy", BLUE_DEEP)
def ventoy():
    stick = rrect(18, 24, 24, 13, 3, INK) + rrect(41, 26.5, 9, 8, 1.2, INK)
    holes = rrect(44, 28, 2.4, 2, .4, HOLE) + rrect(44, 31.5, 2.4, 2, .4, HOLE)
    sym = (line(21.5, 30.5, 37, 30.5, HOLE, 2) + circle(21.5, 30.5, 1.9, HOLE)
           + stroke("M25 30.5L28 27H32M27 30.5L30 34H33", HOLE, 1.8))
    return g(stick + holes + sym, "rotate(-35 32 30)")

@reg("veracrypt", TEAL_DARK)
def veracrypt():
    v = poly([(14, 16), (21, 16), (29, 44), (23.5, 44)], LIGHT_BLUE_LIGHT, 1.5)
    c = poly([(29, 44), (37, 16), (50, 16), (48, 22), (41.5, 22), (38.5, 30),
              (41.5, 38), (49, 38), (51, 44)], INK, 1.5)
    return v + c

@reg("vesktop", PINK_LIGHT)
def vesktop():
    v = path("M14 14H21V29L25 33L25 38H21L14 31Z", INK) + rrect(24.5, 14, 5, 12, 0, INK)
    box = rrect(27, 25, 21, 21, 3, PINK_DARK) + rrect(29.5, 27.5, 16, 16, 1.5, INK)
    c = path("M34 31H42V34.5H37.5V36.5H42V40H34Z", PINK_DARK)
    return v + box + c

@reg("veusz", BLUE_DEEP)
def veusz():
    axes = stroke("M15.5 14V45H48.5", INK, 2.4)
    dots = "".join(circle(x, y, 1.6, INK) for x, y in [(37, 27), (40, 34), (44, 30), (43, 39), (35, 38)])
    v = line(21, 17, 27, 41, GREY_SOFT, 4.5) + line(27, 41, 38, 15, INK, 4.5)
    return axes + dots + v

@reg("veyon-configurator", GREY_DARK)
def veyon_configurator():
    return (rrect(15, 20, 34, 4.4, 2.2, INK) + circle(40, 22.2, 5.8, INK)
            + rrect(15, 35.5, 34, 4.4, 2.2, INK) + circle(24, 37.7, 5.8, INK))

@reg("veyon-master", BLUE_GREY_DARK)
def veyon_master():
    eye = path("M14.5 30C20 21 26 18.5 32 18.5C38 18.5 44 21 49.5 30C44 39 38 41.5 32 41.5"
               "C26 41.5 20 39 14.5 30Z", INK)
    return _ring(32, 30, 16.5, INK, 2.4) + eye + circle(32, 30, 5.2, HOLE)

@reg("viber", DEEP_PURPLE_LIGHT)
def viber():
    bubble = path("M32 13C42 13 47.5 17.5 47.5 28C47.5 38 42 42 33 42L27 47.5V41.8"
                  "C19.5 40 16.5 35.5 16.5 28C16.5 17.5 22 13 32 13Z", INK)
    phone = path("M24.5 22.5C25 21 26 20.8 27 21L29 24.8C29.1 25.4 28.5 26.3 28 26.8"
                 "C29 29.2 31 31.2 33.4 32.3C33.9 31.8 34.8 31.2 35.4 31.3L39 33.2"
                 "C39.2 34.2 38.8 35.2 37.5 35.7C33 37.2 23 27 24.5 22.5Z", HOLE)
    waves = (stroke("M33 20.5A6.5 6.5 0 0 1 39.5 27", HOLE, 2.2)
             + stroke("M33 16.5A10.5 10.5 0 0 1 43.5 27", HOLE, 2.2))
    return bubble + phone + waves

@reg("vibrantLinux", BLUE_GREY_DARK)
def vibrant():
    cols = [RED, ORANGE, YELLOW, LIGHT_BLUE_SOFT, CYAN, BLUE, PURPLE, PINK]
    out = ""
    for k, c in enumerate(cols):
        a0, a1 = -90 + 45 * k, -45 + 45 * k
        x0, y0 = pt(CX, CY, 16.5, a0)
        x1, y1 = pt(CX, CY, 16.5, a1)
        out += path(f"M{CX} {CY}L{f(x0)} {f(y0)}A16.5 16.5 0 0 1 {f(x1)} {f(y1)}Z", c)
    return out + circle(CX, CY, 7, WHITE)

def _vice(u, flag):
    u_ = path("M16 15H24V33A5 5 0 0 0 29 38H30V15H36V44H29A13 13 0 0 1 16 31Z", u)
    flags = (poly([(38, 22), (48.5, 22), (44.5, 26.5), (38, 26.5)], flag, 1)
             + poly([(38, 28.5), (44.5, 28.5), (48.5, 33), (38, 33)], flag, 1))
    return u_ + flags

@reg("vice-vsid", GREY_DARK)
def vice_vsid():
    pins = "".join(rrect(x, 9.5, 2.6, 3, .6, INK) + rrect(x, 47, 2.6, 3, .6, INK)
                   for x in (18, 23, 28, 33, 38, 43))
    return g(_vice(INK, INK), "translate(32 30) scale(.92) translate(-32 -30)") + pins

@reg("vice-x128", GREY_DEEP)
def vice_x128():
    return _vice(INK, INK)

@reg("vice-x64", BROWN_DEEP)
def vice_x64():
    return _vice(INK, BROWN_SOFT)

@reg("vice-x64dtv", RED_DEEP)
def vice_x64dtv():
    return _vice(INK, RED_SOFT)

@reg("vice-xcbm2", LIGHT_BLUE_DEEP)
def vice_xcbm2():
    return _vice(INK, RED_SOFT)

@reg("vice-xpet", BLUE_DEEP)
def vice_xpet():
    return _vice(INK, BLUE_SOFT)

@reg("vice-xplus4", BLUE_GREY_DEEP)
def vice_xplus4():
    return _vice(INK, BLUE_GREY_SOFT)

@reg("vice-xscpu64", BLUE_GREY_DARK)
def vice_xscpu64():
    return _vice(INK, BLUE_GREY_SOFT)

@reg("vice-xvic", ORANGE_DARK)
def vice_xvic():
    return _vice(INK, ORANGE_SOFT)

@reg("vico", GREY_DARK)
def vico():
    def plate(dy, col):
        return poly([(32, 14 + dy), (49, 26 + dy), (32, 38 + dy), (15, 26 + dy)], col, 3)
    keys = (line(24.5, 20.5, 36.5, 29, HOLE, 2) + line(29, 17.5, 41, 26, HOLE, 2)
            + line(19.5, 24, 28.5, 30.5, HOLE, 3.6) + line(27.5, 18, 35.5, 23.8, HOLE, 3.6))
    return plate(8, GREY_LIGHT) + plate(0, INK) + keys

@reg("victor-vran", BLUE_GREY_DARK)
def victor_vran():
    disc_ = circle(CX, CY, 16.5, INK)
    fig = (path("M24 21.5C27 20.5 37 20.5 40 21.5C38 22.5 36 22.8 35.5 23H28.5C28 22.8 26 22.5 24 21.5Z", HOLE,
                f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"')
           + rrect(28.5, 15.5, 7, 6.5, 2, HOLE)
           + path("M29 23H35V27L39.5 29L41 38L39 39L37.5 33V46.5H26.5V33L25 39L23 38L24.5 29L29 27Z", HOLE,
                  f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"'))
    return disc_ + fig

@reg("vidcutter", PURPLE_DEEP)
def vidcutter():
    film = rrect(14, 13, 30, 32, 3, INK)
    holes = "".join(rrect(x, y, 3.5, 3.5, .8, HOLE) for x in (16.5, 38) for y in (16.5, 23.5, 30.5, 37.5))
    frames = rrect(22.5, 16.5, 13, 11.5, 1.5, HOLE) + rrect(22.5, 30.5, 13, 11, 1.5, HOLE)
    badge = circle(42, 39, 11, HOLE) + circle(42, 39, 9, INDIGO_SOFT)
    sc = (line(38, 35, 45, 42.5, INK, 2.2) + line(46, 35, 39, 42.5, INK, 2.2)
          + _ring(38.5, 43, 2.2, INK, 1.8) + _ring(45.5, 43, 2.2, INK, 1.8))
    return film + holes + frames + badge + sc

@reg("videomass", CYAN_DEEP)
def videomass():
    strip = rrect(8, 23, 48, 14, 1.5, INK)
    holes = "".join(rrect(x, 24.8, 3, 2.6, .6, HOLE) + rrect(x, 32.6, 3, 2.6, .6, HOLE)
                    for x in (11, 17, 23, 29, 35, 41, 47, 53))
    frames = "".join(rrect(x, 28.3, 8.5, 3.4, .8, HOLE) for x in (12, 22.5, 33))
    return g(g(strip + holes + frames, "translate(32 30) scale(1.05 1.25) translate(-32 -30)"),
             "rotate(-40 32 30)")

@reg("vieb", RED_DEEP)
def vieb():
    return poly([(14.5, 15), (24, 15), (32, 33), (40, 15), (49.5, 15), (35, 45.5), (29, 45.5)], INK, 3)

@reg("vifm", BLUE_DEEP)
def vifm():
    v = stroke("M16 19L24 41L32 19", INK, 5)
    i = circle(41.5, 19.5, 3.2, INK) + rrect(38.8, 26, 5.4, 16, 2.7, INK)
    return v + i

@reg("viking", BLUE_DEEP)
def viking():
    tabs = "".join(g(rrect(27.5, 11.5, 9, 6, 2, INK), f"rotate({90 * k} 32 30)") for k in range(4))
    return tabs + circle(CX, CY, 14.5, INK) + circle(CX, CY, 10, HOLE) + circle(CX, CY, 7.2, INK)

@reg("vimeo", LIGHT_BLUE)
def vimeo():
    return path("M16 22.5L18 25C20.5 23.2 22 22.5 23 23.8C24.5 25.5 26.5 36 28.5 41"
                "C30 44.5 32 46 35 44C39.5 41 45.5 33 47.5 25.5C49.5 18 46.5 15 43 15"
                "C38.5 15 35.5 18 34 23.5C38 21.5 39.5 24 38 27C36.5 30 34.5 33 33 33"
                "C31.5 33 30.5 21 28.5 17.5C27 15 24.5 15 22 17Z", INK)

@reg("viper-browser", INDIGO_LIGHT)
def viper():
    globe = circle(28.5, 27, 14.5, INK)
    land = (path("M20 19C23 17 26 18 27 21C25 23 26 26 23 27C20 27 18.5 24 20 19Z", INDIGO_SOFT)
            + path("M30 29C33 28 36 30 35 34C34 37 31 39 30 36Z", INDIGO_SOFT)
            + path("M33 15.5C36 15 39 17 40 20C37 21 34 19 33 15.5Z", INDIGO_SOFT))
    badge = circle(40.5, 39.5, 10.5, HOLE) + circle(40.5, 39.5, 8.5, RED_LIGHT)
    slit = path("M40.5 32.5C43 35.5 43 43.5 40.5 46.5C38 43.5 38 35.5 40.5 32.5Z", BROWN_DARK)
    return globe + land + badge + slit

@reg("virt-manager", PINK_DARK)
def virt_manager():
    v = stroke("M13.5 22L18.5 38L23.5 22", INK, 3.6)
    m = stroke("M27 38V22L32.5 31L38 22V38", INK, 3.6) + stroke("M41.5 38V22L46 30L50.5 22V38", PINK_SOFT, 3.6)
    return g(v + m, "translate(32 30) scale(.95) translate(-32 -30)")

@reg("virustotal", INDIGO)
def virustotal():
    return stroke("M17 15H47V45H17L29.5 30Z", INK, 4.4)

@reg("visual-paradigm", RED_DEEP)
def visual_paradigm():
    diamond = g(rrect(17.5, 15.5, 29, 29, 6, INK), "rotate(45 32 30)")
    flag = g(path("M21 19H32V26H43V32H26V30H21Z", HOLE), "rotate(45 32 30)")
    return diamond + flag

@reg("visualvm", DEEP_ORANGE_DEEP)
def visualvm():
    links = (line(28, 31, 21, 16, INK, 2.4) + line(28, 31, 42, 23, INK, 2.4)
             + line(28, 31, 38, 42, INK, 2.4) + line(28, 31, 17, 38, INK, 2.4))
    nodes = (circle(28, 31, 7.5, INK) + circle(21, 16, 3.3, INK) + circle(42.5, 22.5, 5.2, INK)
             + circle(38.5, 42.5, 3, INK) + circle(17, 38.5, 2.5, INK))
    return links + nodes

@reg("vita3k", PURPLE_DEEP)
def vita3k():
    body = path("M20 18H44C51 18 53 23 51 30L48.5 38C47 42 44 43 41 43H23C20 43 17 42 15.5 38"
                "L13 30C11 23 13 18 20 18Z", INK)
    screen = rrect(22.5, 21, 19, 18.5, 2, AMBER)
    pad = rrect(15.5, 28.8, 5, 1.6, .5, HOLE) + rrect(17.2, 27, 1.6, 5, .5, HOLE)
    btns = "".join(circle(x, y, 1.3, HOLE) for x, y in [(46.5, 26.5), (46.5, 32), (44, 29.3), (49, 29.3)])
    return body + screen + pad + btns

@small("usb-creator")
def usb_creator_s():
    body = rrect(15, 11, 22, 34, 4, INK)
    badge = circle(41, 38, 12.5, HOLE) + circle(41, 38, 10.5, ORANGE_DEEP) + stroke("M41 31.5V44M36 39.5L41 44.5L46 39.5", INK, 3.4)
    return body + badge

@small("utilities-log-viewer")
def log_viewer_s():
    sheet = rrect(14, 11, 28, 35, 3.5, INK)
    lines = "".join(rrect(18, y, w, 4, 2, HOLE) for y, w in [(16, 20), (24, 12)])
    return sheet + lines + circle(36, 33, 10, HOLE) + _ring(36, 33, 6.5, INK, 4) + line(41.5, 38.5, 48, 45, INK, 5)

@small("ventoy")
def ventoy_s():
    return g(rrect(16, 23, 25, 15, 3.5, INK) + rrect(40, 25.5, 10, 10, 1.5, INK), "rotate(-35 32 30)")

@small("vidcutter")
def vidcutter_s():
    film = rrect(13, 12, 30, 33, 3, INK) + rrect(21, 16, 14, 25, 2, HOLE)
    badge = circle(42, 39, 11.5, HOLE) + circle(42, 39, 9.5, ORANGE_DEEP)
    return film + badge + line(38.5, 35.5, 45.5, 42.5, INK, 3) + line(45.5, 35.5, 38.5, 42.5, INK, 3)

@small("videomass")
def videomass_s():
    strip = rrect(4, 20, 56, 20, 2, INK)
    frames = "".join(rrect(x, 25, 11, 10, 1.5, HOLE) for x in (11, 26.5, 42))
    return g(g(strip + frames, "translate(32 30) scale(.8) translate(-32 -30)"), "rotate(-40 32 30)")

@small("vita3k")
def vita3k_s():
    body = path("M20 17H44C51 17 53 22 51 30L48.5 39C47 43 44 44 41 44H23C20 44 17 43 15.5 39"
                "L13 30C11 22 13 17 20 17Z", INK)
    return body + rrect(21.5, 20.5, 21, 20, 2, AMBER)

@small("veusz")
def veusz_s():
    return (stroke("M15.5 14V45H48.5", INK, 2.6) + line(21, 17, 27.5, 40, ORANGE_LIGHT, 5.5)
            + line(27.5, 40, 38, 16, INK, 5.5))

@small("virt-manager")
def virt_manager_s():
    return stroke("M14 21L21 40L28 21", INK, 5) + stroke("M34 40V21L41 32L48 21V40", INK, 5)

@small("vice-vsid")
def vice_vsid_s():
    return _vice(INK, INK)

@small("vico")
def vico_s():
    plate = poly([(32, 13), (50, 26), (32, 39), (14, 26)], INK, 3)
    return (poly([(32, 21), (50, 34), (32, 47), (14, 34)], GREY_LIGHT, 3) + plate
            + line(21, 23, 30, 29.5, HOLE, 4.5) + line(29, 17.5, 37, 23.3, HOLE, 4.5))

@small("viper-browser")
def viper_s():
    return (circle(28.5, 27, 14.5, INK) + circle(40.5, 39.5, 11.5, HOLE) + circle(40.5, 39.5, 9.5, RED_LIGHT)
            + path("M40.5 32C43.5 35.5 43.5 43.5 40.5 47C37.5 43.5 37.5 35.5 40.5 32Z", BROWN_DARK))

@small("vibrantLinux")
def vibrant_s():
    cols = [RED, ORANGE, YELLOW, ORANGE, CYAN, BLUE, PURPLE, PINK]
    out = ""
    for k, c in enumerate(cols):
        x0, y0 = pt(CX, CY, 17, -90 + 45 * k)
        x1, y1 = pt(CX, CY, 17, -45 + 45 * k)
        out += path(f"M{CX} {CY}L{f(x0)} {f(y0)}A17 17 0 0 1 {f(x1)} {f(y1)}Z", c)
    return out + circle(CX, CY, 6, WHITE)

@small("utilities-tweak-tool")
def tweak_tool_s():
    return (_gear_l(32, 28, 17, 13, 6, INK) + circle(32, 28, 7.5, HOLE)
            + rrect(29, 27, 6, 20, 3, INK))

@small("veyon-master")
def veyon_master_s():
    eye = path("M12 30C18 20 25 17 32 17C39 17 46 20 52 30C46 40 39 43 32 43"
               "C25 43 18 40 12 30Z", INK)
    return eye + circle(32, 30, 6.5, HOLE)

@small("utox")
def utox_s():
    lock = path("M22 22A10 10 0 0 1 42 22V27H45A3 3 0 0 1 48 30V45A3 3 0 0 1 45 48H19"
                "A3 3 0 0 1 16 45V30A3 3 0 0 1 19 27H22Z", INK)
    return (lock + circle(32, 20.5, 4.5, HOLE) + circle(32, 33, 4.2, HOLE)
            + path("M24.5 45.5A7.5 7 0 0 1 39.5 45.5Z", HOLE))

@small("viber")
def viber_s():
    bubble = path("M32 13C42 13 47.5 17.5 47.5 28C47.5 38 42 42 33 42L27 47.5V41.8"
                  "C19.5 40 16.5 35.5 16.5 28C16.5 17.5 22 13 32 13Z", INK)
    phone = path("M23.5 21.5C24 20 25.5 19.5 27 20L29.5 25C29.6 25.8 29 26.8 28.3 27.4"
                 "C29.5 30 31.5 32 34.2 33.3C34.8 32.6 35.8 32 36.6 32.1L41 34.5"
                 "C41.2 35.8 40.6 37 39 37.6C33.5 39.5 21.5 27 23.5 21.5Z", HOLE)
    return bubble + phone

@small("victor-vran")
def victor_vran_s():
    fig = (rrect(22, 19.5, 20, 4, 2, HOLE) + rrect(27.5, 13.5, 9, 8, 2.5, HOLE)
           + path("M27.5 23H36.5V27L41.5 29.5V47H22.5V29.5L27.5 27Z", HOLE))
    return circle(CX, CY, 17, INK) + fig
