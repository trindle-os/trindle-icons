# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 55: photolayoutseditor to podman-desktop.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import arc_c, _gear, _hex, registry, _ring

ICONS, SMALL, reg, small = registry()

def _magnifier(flip=False):
    lens = _ring(28.5, 26.5, 9.5, INK, 4.4) + line(35.5, 33.5, 45, 43, INK, 5.5)
    return g(lens, "translate(64 0) scale(-1 1)") if flip else lens

def _plasma_mark(colour, sx=1.0):
    """KDE Plasma: dots running down the left, a chevron to the right."""
    m = (circle(22.5, 21, 2.6, colour) + circle(24.5, 31, 2.6, colour) + circle(23, 40, 4, colour)
         + stroke("M33.5 21.5L42 30L33.5 38.5", colour, 5.2))
    return g(m, f"translate(32 30) scale({sx}) translate(-32 -30)") if sx != 1 else m

def _plex(w=1.0):
    return poly([(23.5, 13), (33.5, 13), (43, 30), (33.5, 47), (23.5, 47), (33, 30)], INK, 2.5 * w)

def _heart(cx, cy, rot):
    d = ("M32 30C28 26.5 21.5 22.5 21.5 17.5C21.5 14 24.3 11.5 27.3 11.5C29.4 11.5 31 12.7 32 14.5"
         "C33 12.7 34.6 11.5 36.7 11.5C39.7 11.5 42.5 14 42.5 17.5C42.5 22.5 36 26.5 32 30Z")
    return g(path(d, INK, f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"'),
             f"translate({f(cx)} {f(cy)}) rotate({rot} 32 30)")

@reg("photolayoutseditor", INDIGO_LIGHT)
def photolayoutseditor():
    frame = rrect(14, 15, 36, 30, 4, INK)
    sky = rrect(18, 19, 28, 22, 1.5, HOLE)
    sun = circle(38.5, 25.5, 3.6, INK)
    land = path("M18 35.5C22 32.5 26 32 30 34C34 36 39 33 46 34V41H18Z", INK)
    return frame + sky + sun + land

@reg("photopea", TEAL)
def photopea():
    return stroke("M22 46V28.5A10.5 10.5 0 1 1 32.5 39A6 6 0 0 1 26.5 33A6 6 0 0 1 32.5 27"
                  "A2.5 2.5 0 0 1 35 29.5", INK, 5)

@reg("phototonic", BLUE_DEEP)
def phototonic():
    frame = path("M18 14H46A3 3 0 0 1 49 17V37L39 47H18A3 3 0 0 1 15 44V17A3 3 0 0 1 18 14Z", INK)
    fold = path("M39 47V40A3 3 0 0 1 42 37H49Z", BLUE_SOFT)
    sky = rrect(19, 18, 26, 16, 1.5, HOLE)
    sun = circle(24.5, 23, 3, INK)
    boat = (poly([(34, 20), (34, 30.5), (27.5, 30.5)], INK, 1.5) + poly([(36, 22.5), (36, 30.5), (41, 30.5)], INK, 1.5)
            + path("M27 32H42L40 34H29Z", INK))
    return frame + fold + sky + sun + boat

@reg("picturama", DEEP_PURPLE_LIGHT)
def picturama():
    outer = poly(_hex(32, 30, 17.5), INK, 3)
    inner = poly(_hex(32, 30, 7.5), HOLE, 2)
    cuts = "".join(line(*pt(32, 30, 7.5, -90 + 60 * k + 30), *pt(32, 30, 18, -90 + 60 * k + 30), HOLE, 2)
                   for k in range(6))
    return outer + inner + cuts

@reg("piwigo", DEEP_ORANGE)
def piwigo():
    body = rrect(13.5, 19, 37, 26, 6, INK) + rrect(34, 15, 11, 6, 2, INK)
    lens = circle(30, 32.5, 9, HOLE) + circle(30, 32.5, 5.5, INK)
    return body + lens

@reg("pixeluvo", BLUE_DEEP)
def pixeluvo():
    bowl = stroke("M27.5 26C29 19 34 16 39.5 16C45 16 47 19.5 46 23.5C44.5 29 38.5 31.5 32 31", INK, 4.4)
    stem = stroke("M35.5 20L28 41C26.5 45 22.5 46.5 18.5 45", INK, 4.4)
    return bowl + stem

@reg("phpmyadmin", INDIGO_LIGHT)
def phpmyadmin():
    p = stroke("M15.5 37V23H19.5A4 4 0 0 1 19.5 31H15.5", INK, 3.6)
    m = stroke("M27 37V23L31.5 31L36 23V37", INK, 3.6)
    a = stroke("M39.5 37L43.5 23L47.5 37M40.8 32.5H46.2", ORANGE_LIGHT, 3.6)
    return p + m + a

@reg("phpstorm", PURPLE_LIGHT)
def phpstorm():
    box = rrect(16, 14, 32, 32, 2.5, INK)
    p = stroke("M21.5 32.5V20.5H25A3.5 3.5 0 0 1 25 27.5H21.5", HOLE, 3)
    s = stroke("M40 21.5C39 20.5 37.8 20.2 36.3 20.2C34.3 20.2 32.8 21.4 32.8 23.2"
               "C32.8 27 40.3 25.6 40.3 29.3C40.3 31.3 38.5 32.6 36.3 32.6C34.5 32.6 33.3 32 32.3 31", HOLE, 3)
    return box + p + s + rrect(21, 38, 12, 3.2, 0.6, HOLE)

@reg("pince", GREY_DARK)
def pince():
    return cut("M21 13H33C40 13 45 17.5 45 24.5C45 31.5 40 36 33 36H29.5V47H21Z"
               "M29.5 20.5V28.5H32.5C35 28.5 36.5 27 36.5 24.5C36.5 22 35 20.5 32.5 20.5Z", INK)

@reg("picom", CYAN_DEEP)
def picom():
    gear = _gear(32, 30, 17.5, 13.5, 8, INK, .5)
    p = _ring(33.5, 28, 5.5, HOLE, 3.8) + line(28, 28, 28, 42, HOLE, 3.8)
    return gear + p

@reg("pkgbrowser", ORANGE_DEEP)
def pkgbrowser():
    return g(_magnifier(), "translate(1.5 1)")

@reg("podman-desktop", DEEP_PURPLE)
def podman_desktop():
    hexa = poly(_hex(32, 30, 18.5, -90), INK, 3)
    box = rrect(20, 23, 24, 14, 3, HOLE)
    slots = "".join(rrect(23.5 + 5 * k, 26.5, 2.4, 5.5, 1.2, INK) for k in range(4))
    return hexa + box + slots + rrect(21, 39.5, 22, 2.6, 1.3, HOLE)

@reg("picard", PURPLE_DEEP)
def picard():
    left = poly([(32, 12), (32, 48), (16.4, 39), (16.4, 21)], INK, 2.5)
    right = poly([(32, 12), (47.6, 21), (47.6, 39), (32, 48)], DEEP_ORANGE_LIGHT, 2.5)
    tag = poly([(20, 23.5), (28.5, 23.5), (28.5, 37), (24.25, 41.5), (20, 37)], HOLE, 2)
    circuit = (circle(24.25, 28, 1.8, INK) + stroke("M31 28H36.5L41 23.5M36.5 28L42 31.5M33 28V34L39 39", INK, 2.2)
               + circle(41.5, 23, 2.2, INK) + circle(42.5, 32, 2.2, INK) + circle(39.5, 39.5, 2.2, INK))
    return left + right + tag + circuit

@reg("pidgin", PURPLE_DEEP)
def pidgin():
    tail = stroke("M34 12.5C44 15 48 25.5 44 34.5C40.5 42 31 46.5 21.5 46.5", PURPLE_SOFT, 6)
    return tail + circle(23.5, 31, 7.5, INK) + circle(40, 31, 7.5, INK)

def _pico():
    cells = [(0, 2, RED), (1, 1, ORANGE), (1, 2, INK), (1, 3, DEEP_ORANGE_SOFT),
             (2, 0, YELLOW), (2, 1, INK), (2, 2, INK), (2, 3, INK), (2, 4, PINK_SOFT),
             (3, 1, BROWN_SOFT), (3, 2, INK), (3, 3, BLUE_GREY_SOFT), (4, 2, BLUE)]
    s = 7
    return "".join(rrect(14.5 + c * s, 12.5 + r * s, s, s, 0.6, col) for r, c, col in cells)

@reg("pico-8", BLUE_GREY_DARK)
def pico_8():
    return _pico()

@reg("pico8", BLUE_GREY_DARK)
def pico8():
    return _pico()

@reg("pillars-of-eternity", TEAL_DEEP)
def pillars():
    rocks = path("M17 33L19.5 26L21.5 28L24 20L26.5 23L29 15L31.5 12.5L34.5 14L36 22L38.5 17.5"
                 "L41 23.5L43 21L45 27L47 33Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    ledge = rrect(13.5, 33, 37, 3.2, 1.6, INK)
    roots = (stroke("M20 36L26 44L32 38L38 44L44 36", INK, 2.2) + stroke("M26 44H38M32 38V47", INK, 2.2))
    return rocks + ledge + roots

@reg("pinball", INDIGO)
def pinball():
    back = circle(32, 30, 17, INDIGO_LIGHT)
    hill = path("M15.2 32.5C19 26 27 26.5 32.5 31C38 35.5 44 36 48.7 33"
                "A17 17 0 0 1 15.2 32.5Z", LIGHT_BLUE_SOFT)
    return back + hill + circle(39.5, 20.5, 3.6, INK)

@reg("pingus", BLUE_GREY_DARK)
def pingus():
    face = path("M14.5 29C14.5 21 21.5 19.5 32 25C42.5 19.5 49.5 21 49.5 29"
                "C49.5 40 41 47 32 47C23 47 14.5 40 14.5 29Z", INK)
    eyes = circle(24.5, 31, 3, HOLE) + circle(39.5, 31, 3, HOLE)
    beak = poly([(28.5, 36), (35.5, 36), (32, 41.5)], DEEP_ORANGE, 2)
    return face + eyes + beak

@reg("pioneer_install_icon", RED_DEEP)
def pioneer():
    return stroke("M43 20C40 31 35.5 41 27.5 41C21.5 41 19.5 36.5 20.5 31.5C21.5 25.5 26 21 31 21"
                  "C37.5 21 38.5 30 40.5 36C41.5 39.5 43 41 46.5 41", INK, 4.4)

@reg("pixel-piracy", LIGHT_BLUE)
def pixel_piracy():
    s = 4
    hair = [(1, 0), (3, 0), (5, 0), (7, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
    face = [(c, r) for r in (3, 4, 5, 6) for c in range(1, 8)]
    body = [(c, r) for r in (7, 8) for c in range(0, 9)]
    out = "".join(rrect(14 + c * s, 12 + r * s, s + .2, s + .2, 0, AMBER) for c, r in hair)
    out += "".join(rrect(14 + c * s, 12 + r * s, s + .2, s + .2, 0, INK) for c, r in face)
    out += "".join(rrect(14 + c * s, 12 + r * s, s + .2, s + .2, 0, RED_DEEP if c % 2 else INK) for c, r in body)
    eyes = rrect(14 + 2 * s, 12 + 4 * s, s, s, 0, BROWN_DARK) + rrect(14 + 6 * s, 12 + 4 * s, s, s, 0, BROWN_DARK)
    return g(out + eyes, "translate(-.5 0)")

@reg("pixelitor", BLUE_GREY_DEEP)
def pixelitor():
    return _ring(32, 22.5, 8.5, INK, 3) + _ring(25, 35, 8.5, INK, 3) + _ring(39, 35, 8.5, INK, 3)

@reg("pixelorama", DEEP_PURPLE_DARK)
def pixelorama():
    blocks = [(16, 14, 10, 10, INK), (26, 14, 12, 6, DEEP_PURPLE_SOFT), (38, 14, 10, 12, INK),
              (42, 26, 6, 10, DEEP_PURPLE_SOFT), (36, 36, 12, 10, INK), (26, 40, 10, 6, DEEP_PURPLE_SOFT),
              (16, 34, 10, 12, INK), (16, 24, 6, 10, DEEP_PURPLE_SOFT)]
    return "".join(rrect(x, y, w, h, 1.5, c) for x, y, w, h, c in blocks)

@reg("plague-inc-evolved", RED_DEEP)
def plague():
    out = ""
    for k in range(3):
        a = -90 + 120 * k
        x, y = pt(32, 31, 7.5, a)
        hx, hy = pt(32, 31, 10.2, a)
        out += circle(x, y, 9, INK) + circle(hx, hy, 6.8, HOLE)
    out += _ring(32, 31, 7.2, INK, 2.4) + circle(32, 31, 3.2, HOLE)
    gaps = "".join(line(*pt(32, 31, 3, a), *pt(32, 31, 9, a), HOLE, 1.8, "butt") for a in (-30, 90, 210))
    return out + gaps

@reg("planetary-annihilation-titans", DEEP_ORANGE_LIGHT)
def planetary():
    helm = poly([(17, 15), (47, 15), (47, 35), (39, 45), (25, 45), (17, 35)], INK, 3)
    t = rrect(24, 19.5, 16, 4, 1, HOLE) + rrect(30, 23, 4, 7, 0.8, HOLE)
    eyes = poly([(21.5, 27), (28, 33), (22.5, 33)], HOLE, 1.2) + poly([(42.5, 27), (36, 33), (41.5, 33)], HOLE, 1.2)
    mouth = rrect(27.5, 36, 9, 5, 1, HOLE)
    return helm + t + eyes + mouth

@reg("playonlinux", BLUE_DARK)
def playonlinux():
    d = 1.4
    return (_heart(-d, -d, -45) + _heart(d, -d, 45) + _heart(d, d, 135) + _heart(-d, d, 225))

@reg("plasmagik", AMBER_DEEP)
def plasmagik():
    pts = [pt(32, 31.5, 17.5 if k % 2 == 0 else 8, -90 + 36 * k) for k in range(10)]
    return poly(pts, INK, 4)

@reg("pinta", BLUE_GREY_DEEP)
def pinta():
    handle = line(46, 14, 30.5, 31, ORANGE_LIGHT, 3.6)
    ferrule = line(30.5, 31, 27.5, 34.5, INK, 4)
    tip = path("M27.5 33C24 33 21.5 36 21 39.5C20.8 41 19.5 42.3 17.5 43C22.5 44.5 28.5 42 29.5 37Z", INK)
    tube = (rrect(33, 28, 12, 17, 2.5, INK) + rrect(35, 22.5, 8, 5, 1.2, BLUE_LIGHT)
            + rrect(33, 36, 12, 3, 0, HOLE))
    return handle + ferrule + tip + tube

@reg("pizarra", BLUE_GREY_DARK)
def pizarra():
    def feather(rot):
        f_ = path("M32 44C27 36 26.5 24 32 12C37.5 24 37 36 32 44Z", INK)
        shaft = line(32, 18, 32, 42, HOLE, 1.6)
        return g(f_ + shaft, f"rotate({rot} 30 45)")
    return g(feather(-24) + feather(4) + feather(32), "translate(1 -1)")

@reg("pitivi", DEEP_PURPLE)
def pitivi():
    board = rrect(15, 24, 34, 22, 3, INK)
    clap = g(poly([(15, 17), (47, 17), (47, 21.5), (15, 21.5)], INK, 2), "rotate(-8 15 21.5)")
    stripes = "".join(g(line(x, 18, x - 3, 21, HOLE, 2.4), "rotate(-8 15 21.5)") for x in (24, 32, 40))
    track = (line(20, 36, 44, 36, HOLE, 2.6) + line(25, 31.5, 25, 36, HOLE, 2.6)
             + line(32, 31.5, 32, 36, HOLE, 2.6) + line(39, 31.5, 39, 36, HOLE, 2.6))
    return board + clap + stripes + track

@reg("pipal", PURPLE_LIGHT)
def pipal():
    head = circle(32, 20, 7.5, INK)
    body = path("M17 45C17 36 23 30 32 30C41 30 47 36 47 45Z", INK)
    laptop = rrect(24.5, 34, 15, 9.5, 1.5, HOLE) + rrect(13.5, 44, 37, 4, 2, INK)
    return head + body + laptop

@reg("pia-manager", GREY_DEEP)
def pia_manager():
    head = path("M20 27V23A12 12 0 0 1 44 23V27Z", INK)
    face = circle(27.5, 21.5, 1.8, HOLE) + circle(36.5, 21.5, 1.8, HOLE) + stroke("M28.5 24.5Q32 27 35.5 24.5", HOLE, 1.8)
    body = rrect(16, 29, 32, 19, 5, INK)
    key = circle(32, 36, 3, HOLE) + poly([(30.5, 37), (33.5, 37), (34.3, 43), (29.7, 43)], HOLE, 1)
    return head + face + body + key

@reg("pixiewps", RED_DEEP)
def pixiewps():
    wings = (path("M30.5 27C25 17.5 19.5 12.5 14 12.5C14.5 20 19.5 26.5 29 29.5Z", INK)
             + path("M29.5 30C23 29 17.5 31.5 15 36.5C21.5 37 26.5 35 30 32.5Z", INK))
    head = circle(35.5, 16.5, 4.3, INK)
    body = path("M33 21.5C30 23 28.5 27 29.5 31C30.5 35 29 38 27 41C27 44 30 46 34 46H44"
                "C45.5 46 46 44.5 45 43.5L40 41C39 39 40.5 36 39 32C38 29 39 25 37.5 22Z", INK)
    arm = stroke("M36.5 24L42.5 29L39.5 33", INK, 2.4)
    return wings + head + body + arm

@reg("plasmavault", BLUE_GREY_DEEP)
def plasmavault():
    folder = path("M17 15H26L29.5 18.5H44A3 3 0 0 1 47 21.5V43A3 3 0 0 1 44 46H20A3 3 0 0 1 17 43Z", INK)
    lock = stroke("M28.5 30V27.5A3.5 3.5 0 0 1 35.5 27.5V30", HOLE, 2.6) + rrect(26, 30, 12, 10, 2, HOLE)
    return folder + lock

@reg("plasma", CYAN_DEEP)
def plasma():
    return circle(32, 30, 17.5, INK) + _plasma_mark(HOLE, .78)

@reg("plasma-media-center", BLUE_DEEP)
def plasma_media_center():
    return poly([(24, 16), (46, 30), (24, 44)], INK, 4)

@reg("plasma-search", AMBER_DEEP)
def plasma_search():
    return g(_magnifier(True), "translate(-1.5 1)")

@reg("plasmadiscover", BLUE_LIGHT)
def plasmadiscover():
    handle = stroke("M26 20V15.5H38V20", INK, 3)
    bag = rrect(14, 19, 36, 28, 4, INK)
    return handle + bag + g(_plasma_mark(HOLE, .62), "translate(0 3.5)")

@reg("plasmafox", TEAL_DEEP)
def plasmafox():
    head = poly([(15, 12.5), (32, 22), (49, 12.5), (49, 33), (32, 48), (15, 33)], INK, 3)
    return head + g(_plasma_mark(HOLE, .55), "translate(0 3.5)")

@reg("plank", BLUE)
def plank():
    anchor = (_ring(32, 14.5, 2.6, INK, 2.4) + line(32, 17, 32, 32, INK, 2.8) + line(27, 21, 37, 21, INK, 2.6)
              + stroke("M23 26C23.5 30 27.5 32.5 32 32.5C36.5 32.5 40.5 30 41 26", INK, 2.6))
    dock = rrect(13, 37, 38, 11, 3, INK)
    tiles = "".join(rrect(17.5 + 10.5 * k, 39.5, 8, 6, 1.5, HOLE) for k in range(3))
    return anchor + dock + tiles

@reg("plex-htpc", AMBER_DEEP)
def plex_htpc():
    return _plex() + stroke("M27.5 16L36.5 30L27.5 44", HOLE, 2, ' stroke-dasharray="3 2.6"')

@reg("plexamp", AMBER_DEEP)
def plexamp():
    chev = "".join(stroke(f"M{f(x)} 19L{f(x + 8)} 30L{f(x)} 41", INK, 3) for x in (29, 34, 39))
    return chev + line(15, 30, 36, 30, INK, 3)

@reg("plexhometheater", AMBER_DEEP)
def plexhometheater():
    return _plex()

@reg("pling-store", ORANGE_DEEP)
def pling_store():
    handle = stroke("M25 20V17.5A7 7 0 0 1 39 17.5V20", INK, 3.4)
    bag = path("M16 20H48L46 43A4 4 0 0 1 42 47H22A4 4 0 0 1 18 43Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    p = stroke("M28.5 42V26H33A4.5 4.5 0 0 1 33 35H28.5", HOLE, 3.8)
    return handle + bag + p

@reg("pm.mirko.Atoms", DEEP_PURPLE)
def atoms():
    petals = "".join(circle(*pt(32, 30, 10.5, -90 + 60 * k), 6.5, INK) for k in range(6))
    return petals + circle(32, 30, 7, HOLE) + circle(32, 30, 5, AMBER)

@reg("pm.mirko.Twitz", BLUE_DEEP)
def twitz():
    return rrect(15, 13, 34, 34, 6, INK) + rrect(21.5, 20, 7, 20, 1.5, HOLE) + rrect(35.5, 20, 7, 20, 1.5, HOLE)

@reg("pocket", RED_LIGHT)
def pocket():
    body = path("M18 14H46A3 3 0 0 1 49 17V29C49 39 41.5 46 32 46C22.5 46 15 39 15 29V17A3 3 0 0 1 18 14Z", INK)
    return body + stroke("M24 25L32 33L40 25", HOLE, 4.4)

@reg("pocketcasts", RED)
def pocketcasts():
    outer = arc_c(32, 30, 14.5, 90, 360, INK, 4.4)
    inner = arc_c(32, 30, 7.5, 90, 360, INK, 4.4)
    return outer + inner

@reg("podcast", LIGHT_BLUE_DEEP)
def podcast():
    return (circle(21, 40, 4, INK) +
            stroke("M18.5 28.5A13 13 0 0 1 32.5 42.5", INK, 4.6) +
            stroke("M18.5 18A23.5 23.5 0 0 1 43 42.5", INK, 4.6))

@reg("poddr", ORANGE_DEEP)
def poddr():
    capsule = rrect(25.5, 11.5, 13, 23, 6.5, INK)
    half = path("M32 11.5A6.5 6.5 0 0 0 25.5 18V28A6.5 6.5 0 0 0 32 34.5Z", DEEP_ORANGE)
    holder = stroke("M20 26.5A12 12 0 0 0 44 26.5", INK, 3)
    stand = line(32, 38.5, 32, 45, INK, 3) + line(25, 46, 39, 46, INK, 3.2)
    return capsule + half + holder + stand

@small("phpmyadmin")
def phpmyadmin_s():
    p = stroke("M16 42V18H22A6 6 0 0 1 22 30H16", INK, 5)
    m = stroke("M31 42V18L39.5 31L48 18V42", INK, 5)
    return p + m

@small("phpstorm")
def phpstorm_s():
    box = rrect(15, 13, 34, 34, 3, INK)
    p = stroke("M23 35V20.5H29A5 5 0 0 1 29 30.5H23", HOLE, 5)
    return box + p + rrect(20, 39, 14, 4, 1, HOLE)

@small("picard")
def picard_s():
    left = poly([(32, 11), (32, 49), (15.5, 39.5), (15.5, 20.5)], INK, 2.5)
    right = poly([(32, 11), (48.5, 20.5), (48.5, 39.5), (32, 49)], DEEP_ORANGE_LIGHT, 2.5)
    tag = poly([(19.5, 22.5), (28.5, 22.5), (28.5, 37), (24, 42), (19.5, 37)], HOLE, 2)
    return left + right + tag + stroke("M32 29H37.5L42 24M37.5 29L42 34", INK, 3.2)

@small("phototonic")
def phototonic_s():
    frame = rrect(14, 14, 36, 32, 4, INK) + rrect(18.5, 18.5, 27, 23, 1.5, HOLE)
    boat = poly([(33, 21), (33, 34), (25, 34)], INK, 2) + poly([(35.5, 24), (35.5, 34), (41, 34)], INK, 2)
    return frame + boat + rrect(24, 36, 18, 3.5, 1.5, INK)

@small("photolayoutseditor")
def photolayoutseditor_s():
    frame = rrect(13, 14, 38, 32, 4, INK) + rrect(17.5, 18.5, 29, 23, 1.5, HOLE)
    return (frame + circle(38, 25.5, 4, INK)
            + path("M17.5 35C22 31.5 26 31 30 33.5C34 36 39 32.5 46.5 33.5V41.5H17.5Z", INK))

@small("picturama")
def picturama_s():
    return poly(_hex(32, 30, 17.5), INK, 3) + poly(_hex(32, 30, 7.5), HOLE, 2)

@small("pico-8")
def pico_8_s():
    return _pico()

@small("pillars-of-eternity")
def pillars_s():
    rocks = path("M16 34L19 26L22 29L25 19L28 23L31 12L35 13.5L37 22L40 17L43 24L45 21L48 34Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return rocks + rrect(13, 34, 38, 4.5, 2.2, INK) + stroke("M21 38L32 47L43 38", INK, 3.4)

@small("pixel-piracy")
def pixel_piracy_s():
    s = 6
    hair = poly([(14, 22), (14, 16), (19, 11), (24, 16), (32, 10), (40, 16), (45, 11), (50, 16), (50, 22)], AMBER)
    face = rrect(17, 22, 30, 16, 0, INK)
    body = rrect(14, 38, 36, 10, 0, RED_DEEP)
    eyes = rrect(22, 27, s, s, 0, BROWN_DARK) + rrect(36, 27, s, s, 0, BROWN_DARK)
    return hair + face + body + eyes

@small("pixelitor")
def pixelitor_s():
    return _ring(32, 22, 8.5, INK, 3.4) + _ring(24.5, 35.5, 8.5, INK, 3.4) + _ring(39.5, 35.5, 8.5, INK, 3.4)

@small("pixiewps")
def pixiewps_s():
    wings = path("M30 29C24 19 18 14 13 14C14 22 19 28 28 31Z", INK)
    head = circle(36, 16.5, 4.5, INK)
    body = path("M33 22C29.5 24 28.5 29 29.5 33C30 36 28.5 39 26.5 42C26.5 45 29.5 47 34 47H45"
                "C47 47 47.5 45 46 44L41 41.5C40 39 41.5 36 40 32C39 28.5 40 25 38.5 22Z", INK)
    return wings + head + body

@small("plague-inc-evolved")
def plague_s():
    out = ""
    for k in range(3):
        a = -90 + 120 * k
        out += circle(*pt(32, 31, 8, a), 9.5, INK) + circle(*pt(32, 31, 11.5, a), 6.5, HOLE)
    return out + circle(32, 31, 3.5, HOLE)

@small("planetary-annihilation-titans")
def planetary_s():
    helm = poly([(16, 14), (48, 14), (48, 35), (39.5, 46), (24.5, 46), (16, 35)], INK, 3)
    t = rrect(23, 19, 18, 5, 1, HOLE) + rrect(29.5, 23, 5, 7, 0.8, HOLE)
    eyes = poly([(20.5, 27), (28, 34), (21.5, 34)], HOLE, 1.5) + poly([(43.5, 27), (36, 34), (42.5, 34)], HOLE, 1.5)
    return helm + t + eyes + rrect(27, 37, 10, 5, 1, HOLE)

@small("plasmadiscover")
def plasmadiscover_s():
    bag = stroke("M26 20V15.5H38V20", INK, 3.4) + rrect(13, 19, 38, 29, 4, INK)
    m = circle(22, 29, 3, HOLE) + circle(22, 39, 3.6, HOLE) + stroke("M32 26L39 33L32 40", HOLE, 5)
    return bag + m

@small("plasmafox")
def plasmafox_s():
    head = poly([(14, 11.5), (32, 21.5), (50, 11.5), (50, 33), (32, 49), (14, 33)], INK, 3)
    return head + circle(24, 30, 2.8, HOLE) + circle(25, 39, 3.2, HOLE) + stroke("M32 27L38.5 33.5L32 40", HOLE, 4.6)

@small("plasma")
def plasma_s():
    m = (circle(22, 23, 3, HOLE) + circle(23.5, 37, 4, HOLE) + stroke("M33 21L42 30L33 39", HOLE, 5.5))
    return circle(32, 30, 18, INK) + m

@small("plank")
def plank_s():
    anchor = (line(32, 12, 32, 31, INK, 3.4) + line(26, 18, 38, 18, INK, 3.2)
              + stroke("M22 24.5C22.5 29.5 27 32 32 32C37 32 41.5 29.5 42 24.5", INK, 3.2))
    return anchor + rrect(12, 36, 40, 12, 3, INK) + rrect(19, 39.5, 8, 5.5, 1.5, HOLE) + rrect(37, 39.5, 8, 5.5, 1.5, HOLE)

@small("plex-htpc")
def plex_htpc_s():
    return _plex()

@small("plexamp")
def plexamp_s():
    chev = "".join(stroke(f"M{f(x)} 18L{f(x + 9)} 30L{f(x)} 42", INK, 3.6) for x in (29, 37))
    return chev + line(14, 30, 34, 30, INK, 3.6)

@small("pinta")
def pinta_s():
    handle = line(47, 13, 29, 33, ORANGE_LIGHT, 4.4)
    tip = path("M28 31C23.5 31 20.5 35 20 39.5C19.8 41 18.5 42.5 16.5 43.5C23 45 29.5 42 31 36Z", INK)
    tube = rrect(33, 27, 14, 19, 3, INK) + rrect(35.5, 21, 9, 6, 1.5, BLUE_LIGHT)
    return handle + tip + tube

@small("pizarra")
def pizarra_s():
    def feather(rot):
        return g(path("M32 45C26.5 36 26 24 32 11C38 24 37.5 36 32 45Z", INK), f"rotate({rot} 30 45)")
    return g(feather(-26) + feather(4) + feather(34), "translate(1 -1)")

@small("pitivi")
def pitivi_s():
    board = rrect(14, 25, 36, 22, 3, INK)
    clap = g(rrect(14, 15, 34, 6.5, 1.5, INK), "rotate(-8 14 21.5)")
    return board + clap + line(20, 37, 44, 37, HOLE, 3.6)

@small("pia-manager")
def pia_manager_s():
    head = path("M19 27V23A13 13 0 0 1 45 23V27Z", INK)
    face = circle(27, 21, 2.3, HOLE) + circle(37, 21, 2.3, HOLE)
    body = rrect(15, 29, 34, 19, 5, INK)
    key = circle(32, 36, 3.6, HOLE) + rrect(30, 37, 4, 7, 1, HOLE)
    return head + face + body + key

@small("pingus")
def pingus_s():
    face = path("M13.5 29C13.5 20.5 21 19 32 24.5C43 19 50.5 20.5 50.5 29"
                "C50.5 40.5 41.5 47.5 32 47.5C22.5 47.5 13.5 40.5 13.5 29Z", INK)
    return face + circle(24, 31, 3.6, HOLE) + circle(40, 31, 3.6, HOLE) + poly([(28, 36.5), (36, 36.5), (32, 42.5)], DEEP_ORANGE, 2)

@small("playonlinux")
def playonlinux_s():
    d = 1.6
    return (_heart(-d, -d, -45) + _heart(d, -d, 45) + _heart(d, d, 135) + _heart(-d, d, 225))

@small("pm.mirko.Atoms")
def atoms_s():
    petals = "".join(circle(*pt(32, 30, 10.5, -90 + 60 * k), 7, INK) for k in range(6))
    return petals + circle(32, 30, 6, AMBER)

@small("poddr")
def poddr_s():
    capsule = rrect(24.5, 10.5, 15, 24, 7.5, INK)
    half = path("M32 10.5A7.5 7.5 0 0 0 24.5 18V27A7.5 7.5 0 0 0 32 34.5Z", DEEP_ORANGE)
    holder = stroke("M19 26A13 13 0 0 0 45 26", INK, 3.6)
    return capsule + half + holder + line(32, 39, 32, 46, INK, 3.6) + line(24, 47, 40, 47, INK, 3.6)

@small("podman-desktop")
def podman_desktop_s():
    hexa = poly(_hex(32, 30, 19, -90), INK, 3)
    box = rrect(19, 22, 26, 16, 3, HOLE)
    slots = "".join(rrect(23.5 + 7 * k, 25.5, 3.2, 9, 1.6, INK) for k in range(3))
    return hexa + box + slots

@small("pocketcasts")
def pocketcasts_s():
    return arc_c(32, 30, 14.5, 90, 360, INK, 5.2) + circle(32, 30, 6, INK)
