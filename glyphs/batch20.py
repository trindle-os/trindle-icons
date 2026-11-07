# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 20: darktable to desktop-environment-kde.

Same rules as batch01: tile is the palette step nearest the brand colour,
mark in INK, HOLE for cut-outs, any second shade from the palette.
"""
import math
from lm import *
from glyphs.kit import _gear, _jb, registry, _star
from glyphs.kit import shared_kde_s

ICONS, SMALL, reg, small = registry()

def _cloud(cx, cy, k, fill):
    d = (f"M{f(cx - 12 * k)} {f(cy + 6 * k)}A6 6 0 0 1 {f(cx - 10 * k)} {f(cy - 4 * k)}"
         f"A9 9 0 0 1 {f(cx + 7 * k)} {f(cy - 5 * k)}A6.5 6.5 0 0 1 {f(cx + 12 * k)} {f(cy + 6 * k)}Z")
    return path(d, fill, f' stroke="{fill}" stroke-width="{f(2 * k)}" stroke-linejoin="round"')

def _heart(cx, cy, s):
    d = (f"M{f(cx)} {f(cy + 14 * s)}L{f(cx - 12.5 * s)} {f(cy + 1.5 * s)}"
         f"A7.2 7.2 0 0 1 {f(cx)} {f(cy - 8.5 * s)}A7.2 7.2 0 0 1 {f(cx + 12.5 * s)} {f(cy + 1.5 * s)}Z")
    return d

@reg("darktable", BLUE_GREY_DARK)
def darktable():
    blades = "".join(line(*pt(CX, CY, 5.5, 60 * k), *pt(CX, CY, 17, 60 * k + 62), HOLE, 2.2)
                     for k in range(6))
    hexa = poly([pt(CX, CY, 6, 60 * k + 30) for k in range(6)], HOLE, 1)
    return circle(CX, CY, 16.5, INK) + blades + hexa

@reg("deepin-draw", INDIGO_LIGHT)
def deepin_draw():
    pal = cut("M31 14C20 14 14 21 14 30C14 39 21 46 30 46C34 46 35 43 33.5 41"
              "C32 38.5 33.5 36 36.5 36H41C46 36 49 33 49 28C49 20 41 14 31 14Z"
              + cpath(22, 26, 2.6) + cpath(24.5, 37, 2.6) + cpath(30.5, 20.5, 2.6), INK)
    brush = (line(38, 34, 47, 13, HOLE, 6.5) + line(38.5, 33, 47, 13.5, INK, 3) +
             path("M34.5 33L39.5 35.5L36 42.5C34.5 44 32 44 31.5 42.5Z", INK,
                  f' stroke="{HOLE}" stroke-width="1.6" stroke-linejoin="round"'))
    return pal + brush

@reg("de.haeckerfelix.Fragments", BLUE_DEEP)
def fragments():
    tile = rrect(17, 15, 30, 30, 5, INK)
    grid = "".join(line(v, 15, v, 45, HOLE, 2.2, "butt") + line(17, v - 2, 47, v - 2, HOLE, 2.2, "butt")
                   for v in (27, 37))
    return g(tile + grid, "rotate(45 32 30)")

@reg("delir", PURPLE_DEEP)
def delir():
    spire = poly([(33, 11.5), (39, 33), (41.5, 47), (33, 40.5), (24.5, 47), (27, 33)], INK, 2)
    return spire + line(33, 20, 33, 34, HOLE, 2.4)

@reg("denemo", ORANGE_DEEP)
def denemo():
    d = stroke("M20 15H27C37 15 43 21 43 30C43 39 37 45 27 45H20Z", INK, 5.5)
    badge = circle(41, 40, 10, HOLE) + circle(41, 40, 8, INK)
    note = circle(39, 43, 2.6, HOLE) + line(41.2, 43, 41.2, 35, HOLE, 2.2) + line(41.2, 35, 44, 36.5, HOLE, 2.2)
    return d + badge + note

@reg("deflemask", BLUE_GREY_DARK)
def deflemask():
    mask = path("M32 12C22 12 17 18 17 27C17 38 24 47 32 47C40 47 47 38 47 27C47 18 42 12 32 12Z", INK)
    half = path("M32 12C42 12 47 18 47 27C47 38 40 47 32 47Z", BLUE_GREY_SOFT)
    eyes = (poly([(21, 26), (29, 27.5), (27, 30.5), (22, 29.5)], HOLE, 1.5) +
            rrect(35, 26, 8, 4.5, 1, HOLE))
    mouth = rrect(28, 39, 8, 2.6, 1.3, HOLE) + circle(32, 34, 1.6, HOLE)
    return mask + half + eyes + mouth

@reg("datagrip", PINK_DEEP)
def datagrip():
    dg = (stroke("M20.5 19.5V29.5H23A5 5 0 0 0 23 19.5Z", HOLE, 3) +
          stroke("M40.5 21A5 5 0 1 0 41 27.5V25H37.5", HOLE, 3))
    return _jb(dg)

@reg("dataspell", BLUE_DEEP)
def dataspell():
    ds = (stroke("M20.5 19.5V29.5H23A5 5 0 0 0 23 19.5Z", HOLE, 3) +
          stroke("M41.5 20.5C40.5 19.5 39.2 19.2 38 19.2C36 19.2 34.5 20.3 34.5 22"
                 "C34.5 25.5 41.8 23.5 41.8 27.2C41.8 29 40.2 30 38 30C36.5 30 35 29.4 34.2 28.3", HOLE, 3))
    return _jb(ds)

def _cyl(x, y, w, h, n, fill, gap):
    rx, ry = w / 2, w / 5
    d = (f"M{f(x)} {f(y + ry)}A{f(rx)} {f(ry)} 0 0 1 {f(x + w)} {f(y + ry)}"
         f"V{f(y + h - ry)}A{f(rx)} {f(ry)} 0 0 1 {f(x)} {f(y + h - ry)}Z")
    out = path(d, fill)
    band = (h - 2 * ry) / n
    for k in range(1, n):
        yy = y + ry + band * k
        out += stroke(f"M{f(x)} {f(yy - ry)}A{f(rx)} {f(ry)} 0 0 0 {f(x + w)} {f(yy - ry)}", gap, 2)
    return out + stroke(f"M{f(x)} {f(y + ry)}A{f(rx)} {f(ry)} 0 0 0 {f(x + w)} {f(y + ry)}", gap, 2)

@reg("datamodeler", BLUE_GREY)
def datamodeler():
    db = _cyl(14, 13, 27, 32, 3, INK, HOLE)
    badge = rrect(31, 29, 19, 19, 4, HOLE) + rrect(33, 31, 15, 15, 3, BLUE_LIGHT)
    nodes = (rrect(35, 33, 4.5, 4, .8, INK) + rrect(42, 33, 4.5, 4, .8, INK) +
             rrect(35, 40, 4.5, 4, .8, INK) + line(39, 35, 42, 35, INK, 1.6) +
             line(37.2, 37, 37.2, 40, INK, 1.6))
    return db + badge + nodes

@reg("datastudio", LIGHT_BLUE_DEEP)
def datastudio():
    db = _cyl(15, 12, 20, 24, 2, INK, HOLE)
    table = rrect(26, 26, 23, 21, 3.5, HOLE) + rrect(28, 28, 19, 17, 2.5, INK)
    cells = "".join(rrect(30 + c * 8, 31 + r * 6.5, 6.5, 4.5, 1, HOLE) for r in range(2) for c in range(2))
    return db + table + cells

@reg("dconf-editor", BLUE_GREY)
def dconf_editor():
    win = rrect(14, 15, 36, 30, 4, INK) + rrect(14, 23, 36, 2.2, 0, HOLE)
    top = (line(20, 20.5, 21.5, 17.5, HOLE, 2) + rrect(25, 18, 3, 2.4, .6, HOLE) +
           rrect(32, 17.8, 13, 2.4, 1.2, HOLE))
    rows = rrect(18.5, 30, 10, 2.6, 1.3, HOLE) + rrect(18.5, 36, 6.5, 2.6, 1.3, HOLE)
    tog = rrect(33, 30.5, 13, 8, 4, BLUE) + circle(42, 34.5, 3, INK)
    return win + top + rows + tog

@reg("de.rwth_aachen.ient.YUView", TEAL_DEEP)
def yuview():
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 13, HOLE) +
            poly([(28, 22), (40.5, 30), (28, 38)], INK, 3))

@reg("de.unifreiburg.ellipticcurve", BLUE_GREY)
def ellipticcurve():
    curve = stroke("M38 12.5C34 17 30 21 25 23C18.5 25.5 18.5 34.5 25 37C30 39 34 43 38 47.5", INK, 3.2)
    badge = circle(40, 38, 10.5, HOLE) + circle(40, 38, 8.5, INK)
    pen = line(36.5, 41.5, 43, 35, HOLE, 3) + poly([(34.5, 43.5), (35, 40.5), (37.5, 43)], HOLE)
    return curve + badge + pen

@reg("deadbeef", BLUE_GREY)
def deadbeef():
    return stroke("M23 30V15L43 30L23 45", INK, 5)

@reg("davinci-panels", BLUE_GREY_DARK)
def davinci_panels():
    ring = "".join(stroke(f"M{f(pt(CX, CY, 14, a + 6)[0])} {f(pt(CX, CY, 14, a + 6)[1])}"
                          f"A14 14 0 0 1 {f(pt(CX, CY, 14, a + 84)[0])} {f(pt(CX, CY, 14, a + 84)[1])}",
                          c, 4.4) for a, c in [(-90, AMBER), (0, PURPLE_SOFT), (90, BLUE), (180, RED)])
    return ring + circle(CX, CY, 8, INK)

@reg("dash-qt", BLUE_DEEP)
def dash_qt():
    d = path("M23 17H42C46 17 48 20 47 24L44.5 35C43.5 40 40 43 35 43H16.5L18.5 36.5H37L39.5 24H21Z", INK)
    dash = poly([(18.5, 27), (31, 27), (29.5, 32.5), (17, 32.5)], INK)
    return d + dash

@reg("davmail", AMBER_DEEP)
def davmail():
    return poly([(35, 11.5), (22, 33), (31, 33), (27, 48.5), (42, 26), (33, 26)], INK, 2.5)

@reg("de.schmidhuberj.Flare", BLUE_DEEP)
def flare():
    bub = path("M20 15H44A5 5 0 0 1 49 20V36A5 5 0 0 1 44 41H43V48L35 41H20A5 5 0 0 1 15 36V20A5 5 0 0 1 20 15Z", INK)
    return bub + poly(_star(32, 28.5, 8.5, 3.8), HOLE, 2)

@reg("de.schmidhuberj.tubefeeder", RED_DEEP)
def tubefeeder():
    return stroke("M20 14.5L46 30L20 45.5Z", INK, 5.5) + line(20, 14.5, 20, 45.5, INK, 7)

@reg("deltachat", BLUE_GREY_DARK)
def deltachat():
    bub = path("M32 13.5A16.5 16.5 0 1 0 43 42.3L48.5 46.5L47 37.5A16.5 16.5 0 0 0 32 13.5Z", INK)
    delta = (f'<circle cx="31.5" cy="35" r="6" fill="none" stroke="{HOLE}" stroke-width="3"/>' +
             stroke("M37.5 18.5C34 16 27 16.5 27.5 20.5C28 24 33.5 25.5 35.5 29.5", HOLE, 3))
    return bub + delta

@reg("deluge", BLUE_DARK)
def deluge():
    drop = path("M32 11C26 19 17 26 17 34C17 42 24 47.5 32 47.5C40 47.5 47 42 47 34C47 26 38 19 32 11Z", INK)
    swirl = stroke("M36 27.5C30.5 26 24.5 29.5 24.5 35.5C24.5 40 28.5 42 32.5 41.5C36 41 39 38 38 34", HOLE, 3.4)
    return drop + swirl

@reg("deskreen", AMBER_DEEP)
def deskreen():
    return cut("M19 14H31C41.5 14 47 20.5 47 30C47 39.5 41.5 46 31 46H19Z"
               "M27 22V38H30.5C36 38 38.5 34.5 38.5 30C38.5 25.5 36 22 30.5 22Z", INK)

@reg("deezer", DEEP_PURPLE_LIGHT)
def deezer():
    out = ""
    for x in range(16, 50, 4):
        cx = 24.5 if x < 32 else 39.5
        dx = min(abs(x - cx), 7.9)
        top = 22 - math.sqrt(8 ** 2 - dx ** 2) if abs(x - cx) < 8 else 22
        bot = 45 - abs(x - 32) * 1.1
        if x == 32:
            top = 23
        out += line(x, top + 1.2, x, bot - 1.2, INK, 2.6)
    return out

@reg("datovka", BLUE_DARK)
def datovka():
    d = cut("M21 14H31C41.5 14 47 20.5 47 30C47 39.5 41.5 46 31 46H19L21 39H31C36 39 39 35 39 30"
            "C39 25 36 21 31 21H23Z", INK)
    arrow = poly([(17, 27), (29, 27), (29, 22.5), (36, 30), (29, 37.5), (29, 33), (17, 33)], INK, 1.5)
    return d + arrow

@reg("dde-introduction", CYAN_DEEP)
def dde_introduction():
    heart = path(_heart(32, 29, 1.25), INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    fingers = "".join(line(29 + 4 * k, 40 - 1.5 * k, 37 + 4 * k, 31 - 1.5 * k, HOLE, 2.2) for k in range(3))
    return heart + fingers

@reg("deepin-remote-assistance", TEAL_LIGHT)
def deepin_remote():
    heart = stroke(_heart(30.5, 28, 1.15), INK, 3.6)
    fingers = "".join(line(35 + 3.5 * k, 34 - 3.5 * k, 44 + 3 * k, 25 - 3.5 * k, INK, 3) for k in range(2))
    return heart + fingers

@reg("deepin-cloud-print-configurator", BLUE_DEEP)
def deepin_cloud_print():
    cloud = _cloud(32, 24, 1.3, INK)
    slot = rrect(15, 29, 34, 3.2, 1.6, HOLE)
    paper = rrect(20, 31, 24, 16, 2, INK) + "".join(rrect(23.5, y, w, 2.4, 1.2, HOLE) for y, w in
                                                    [(35, 17), (40, 12)])
    return cloud + slot + paper

@reg("deepin-cloud-scan-config-helper", BLUE)
def deepin_cloud_scan():
    doc = rrect(19, 12, 26, 36, 3, INK)
    lines = rrect(23, 16, 14, 2.4, 1.2, HOLE)
    scan = rrect(13, 21, 38, 6, 3, HOLE) + rrect(14.5, 22.5, 35, 3, 1.5, INK)
    cloud = _cloud(32, 38, .8, HOLE)
    return doc + lines + scan + cloud

@reg("deepin-feedback", LIGHT_BLUE)
def deepin_feedback():
    bub = path("M32 14C41.5 14 49 20 49 28C49 36 41.5 42 32 42C29.5 42 27.5 41.7 25.5 41L17 46L19 38.5"
               "C16.5 35.8 15 32 15 28C15 20 22.5 14 32 14Z", INK)
    lines = "".join(rrect(22, y, 20, 3, 1.5, HOLE) for y in (21.5, 26.5, 31.5))
    return bub + lines

@reg("deepin-launcher", BLUE)
def deepin_launcher():
    return "".join(rrect(x, y, 14, 14, 4, INK) for x in (16, 34) for y in (14, 32))

@reg("deepin-manual", TEAL)
def deepin_manual():
    book = rrect(17, 12, 30, 36, 3.5, INK) + line(23, 12, 23, 48, HOLE, 2.2)
    wrench = (path("M29 20V25.5C29 28 30.5 30 32.5 30.5V44.5H37.5V30.5C39.5 30 41 28 41 25.5V20"
                   "H38V25H32V20Z", HOLE, f' stroke="{HOLE}" stroke-width="1" stroke-linejoin="round"'))
    return book + wrench

@reg("deepin-movie", BLUE_DEEP)
def deepin_movie():
    film = rrect(14, 14, 36, 32, 4, INK)
    holes = "".join(rrect(17.5 + 6 * k, y, 3.5, 3, .7, HOLE) for k in range(5) for y in (16.5, 40.5))
    return film + holes + poly([(28, 23.5), (38.5, 30), (28, 36.5)], HOLE, 2.5)

@reg("deepin-repair-tools", GREY_DEEP)
def deepin_repair():
    wrench = (line(20, 42, 38, 24, INK, 4) +
              cut(cpath(41, 21, 6.5) + "M39 13L45 13L49 19L46 21L41 17Z", INK))
    wrench = (line(20, 42, 37, 25, INK, 4) + circle(41, 21, 6.5, INK) +
              rrect(40, 13, 6, 8, 2, HOLE, ' transform="rotate(45 43 17)"') + circle(20, 42, 1.3, HOLE))
    hammer = (line(44, 44, 26, 26, INK, 4) +
              g(rrect(15, 14, 17, 7.5, 2, INK), "rotate(-45 23.5 17.75) translate(0 0)"))
    return wrench + g(hammer, "translate(0 0)")

@reg("deepin-toggle-desktop", TEAL_DEEP)
def deepin_toggle():
    return (rrect(13, 15, 38, 30, 4, INK) + rrect(17.5, 19.5, 5, 5, 1.2, HOLE) +
            rrect(17.5, 27, 5, 5, 1.2, HOLE) + rrect(17.5, 36, 29, 5, 2, HOLE))

@reg("deepin-voice-note", BLUE_GREY_DEEP)
def deepin_voice():
    mic = rrect(25, 11, 14, 23, 7, INK)
    cup = stroke("M19.5 28C19.5 35.5 25 40.5 32 40.5C39 40.5 44.5 35.5 44.5 28", INK, 3.4)
    return mic + cup + line(32, 40.5, 32, 46, INK, 3.4) + line(25, 47, 39, 47, INK, 3.4)

@reg("de.gunibert.Hackgregator", ORANGE_DEEP)
def hackgregator():
    book = path("M14 14H29L32 17L35 14H50V45H36L32 48L28 45H14Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    page = rrect(19, 18.5, 26, 22, 1.5, HOLE)
    h = line(26.5, 23, 26.5, 36, INK, 3.4) + line(37.5, 23, 37.5, 36, INK, 3.4) + line(26.5, 29.5, 37.5, 29.5, INK, 3.4)
    return book + page + h

@reg("de.haeckerfelix.Shortwave", ORANGE_DEEP)
def shortwave():
    ant = line(22, 21, 44, 12.5, INK, 2.6)
    body = rrect(13, 20, 38, 27, 4, INK)
    grill = circle(26, 33.5, 9, HOLE) + "".join(
        line(26 - w, y, 26 + w, y, INK, 1.8, "butt") for y, w in
        [(28, 7.5), (31.7, 9), (35.4, 9), (39.1, 7.5)])
    knob = circle(42.5, 27, 2.6, HOLE) + "".join(rrect(x, y, 2.8, 2.8, .7, HOLE)
                                                 for x in (39.5, 43) for y in (33, 37.5))
    return ant + body + grill + knob

@reg("dbeaver", BROWN)
def dbeaver():
    ears = circle(20, 18, 5, INK) + circle(44, 18, 5, INK)
    head = path("M32 14C42 14 48 21 48 31C48 41 41 47 32 47C23 47 16 41 16 31C16 21 22 14 32 14Z", INK)
    eyes = circle(25, 27, 3, HOLE) + circle(39, 27, 3, HOLE)
    snout = rrect(26, 32, 12, 7, 3.5, HOLE)
    nose = path("M29 32.5H35C35 35 33.5 36.5 32 36.5C30.5 36.5 29 35 29 32.5Z", INK)
    teeth = rrect(29.5, 39, 5, 5, 1, HOLE) + line(32, 39.5, 32, 43.5, INK, 1)
    return ears + head + eyes + snout + nose + teeth

@reg("deja-dup", GREY_DARK)
def deja_dup():
    safe = rrect(15, 12, 34, 36, 4, INK)
    hinge = rrect(12.5, 18, 5, 6, 1.5, INK) + rrect(12.5, 36, 5, 6, 1.5, INK)
    dial = circle(33, 30, 10, HOLE) + circle(33, 30, 7, INK) + circle(33, 30, 2.6, HOLE)
    spokes = "".join(line(*pt(33, 30, 3, a), *pt(33, 30, 7, a), HOLE, 2) for a in (-90, 30, 150))
    return safe + hinge + dial + spokes

@reg("darwinia", GREY_DEEP)
def darwinia():
    return path("M29 11H35V18H46V24H35V30H42V49H36V39H28V49H22V30H29V24H18V18H29Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')

@reg("day-of-the-tentacle-remastered", PURPLE_DEEP)
def dott():
    body = path("M17 48C17 30 21 13 32 13C43 13 47 30 47 48Z", INK)
    eye = circle(32, 31, 8.5, HOLE) + circle(32, 31, 4.8, INK)
    brow = stroke("M20 22.5C25 20 28 20.5 32 22.5C36 20.5 39 20 44 22.5", HOLE, 3.2)
    return body + eye + brow

@reg("ddaynormandy", DEEP_PURPLE_LIGHT)
def ddaynormandy():
    return poly(_star(32, 31, 18, 7.2), INK, 2)

@reg("dead-cells", CYAN_DEEP)
def dead_cells():
    flame = path("M30 11.5C23 17 18.5 24.5 19.5 33C20.5 41.5 26.5 47.5 33.5 47.5"
                 "C41 47.5 46 42 46 35C46 29.5 43 25.5 38.5 23C39.5 27 38.5 30.5 35 31.5"
                 "C29.5 28.5 26.5 21.5 30 11.5Z", INK)
    flick = path("M39.5 15C43 17.5 44.5 21 43.5 24C42 21.5 40 20 38 19.5C39 18 39.5 16.5 39.5 15Z", INK)
    star = poly(_star(33, 38.5, 6, 1.6, 4), HOLE, 1)
    return flame + flick + star

@reg("dead-island", RED_DEEP)
def dead_island():
    trunk = stroke("M32 22C31 30 31.5 38 34.5 47", INK, 4)
    fronds = (path("M32 22C27 16 20 15 14 18C20 18 25 20 28 24Z", INK) +
              path("M32 22C37 16 44 15 50 18C44 18 39 20 36 24Z", INK) +
              path("M32 22C26 22 20 25 17 30C22 27.5 27 26 31 25.5Z", INK) +
              path("M32 22C38 22 44 25 47 30C42 27.5 37 26 33 25.5Z", INK) +
              path("M32 22C30 17 30.5 13 33 10C32.5 14 33.5 18 34 22Z", INK))
    return trunk + fronds

@reg("dead-or-alive-6", RED)
def doa6():
    return stroke("M45 16H28C21.5 16 17.5 20.5 17 27L16.5 34C16.5 40 20 44 26 44H37"
                  "C43 44 47 40 47 35C47 30 43.5 27 38.5 27H19", INK, 6)

@reg("defcon", RED_DARK)
def defcon():
    blades = ""
    for a in (-90, 30, 150):
        o1, o2 = pt(CX, CY, 17, a - 30), pt(CX, CY, 17, a + 30)
        i1, i2 = pt(CX, CY, 6, a + 30), pt(CX, CY, 6, a - 30)
        blades += path(f"M{f(i2[0])} {f(i2[1])}L{f(o1[0])} {f(o1[1])}A17 17 0 0 1 {f(o2[0])} {f(o2[1])}"
                       f"L{f(i1[0])} {f(i1[1])}A6 6 0 0 0 {f(i2[0])} {f(i2[1])}Z", INK)
    return blades + circle(CX, CY, 3.6, INK)

@reg("deltarune", INDIGO_DARK)
def deltarune():
    heart = path(_heart(32, 25, 1.45), INK, f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    orb = circle(32, 22, 3.2, HOLE)
    wings = (path("M28 22C25 19 20 18 17.5 19.5C20 21 22 23.5 22.5 26C24.5 24.5 26.5 23.5 28 22Z", HOLE) +
             path("M36 22C39 19 44 18 46.5 19.5C44 21 42 23.5 41.5 26C39.5 24.5 37.5 23.5 36 22Z", HOLE))
    tris = (poly([(24.5, 33), (27, 29), (29.5, 33)], HOLE, 1) + poly([(34.5, 33), (37, 29), (39.5, 33)], HOLE, 1) +
            poly([(29, 36), (35, 36), (32, 40.5)], HOLE, 1))
    return heart + orb + wings + tris

@reg("dassault-systemes.draftsight", CYAN_DEEP)
def draftsight():
    tri = poly([(30.5, 11.5), (49, 47), (30.5, 47)], INK, 2.5)
    s = stroke("M41 30C39.8 28.5 38.2 28 36.8 28C35 28 33.5 29 33.5 30.8C33.5 34.5 41.5 33 41.5 37.5"
               "C41.5 39.5 39.8 41 37.2 41C35.5 41 34 40.2 33 39", HOLE, 2.6)
    d = path("M24 14C13 21 12 38 20 47H27.5C20 39 19.5 24 24 14Z", INK)
    return d + tri + s

@reg("desktop-environment-gnome", ORANGE_DARK)
def gnome():
    sole = path("M36 22C44 22 48 29 46.5 36C45 43 39 48 33 47.5C28 47 27.5 43 25.5 40"
                "C23 36.5 22 33 24 28.5C26 24.5 30.5 22 36 22Z", INK)
    toes = circle(38.5, 13.5, 5, INK) + circle(28, 15.5, 3.6, INK) + circle(21.5, 21, 3, INK) + circle(18.5, 28, 2.6, INK)
    return sole + toes

@reg("desktop-environment-kde", BLUE_DEEP)
def kde():
    gear = _gear(CX, CY, 17, 13.5, 9, INK, .45) + circle(CX, CY, 10, HOLE)
    k = (line(28, 23, 28, 37.5, INK, 3.4) + line(29, 30.5, 37, 22.5, INK, 3.4) +
         line(31.5, 29, 37.5, 37.5, INK, 3.4))
    return gear + k

@small("darktable")
def darktable_s():
    blades = "".join(line(*pt(CX, CY, 6, 120 * k), *pt(CX, CY, 17, 120 * k + 62), HOLE, 3)
                     for k in range(3))
    return circle(CX, CY, 16.5, INK) + blades + circle(CX, CY, 6, HOLE)

@small("deja-dup")
def deja_dup_s():
    return (rrect(15, 12, 34, 36, 4, INK) + circle(33, 30, 10, HOLE) + circle(33, 30, 6.5, INK) +
            rrect(12.5, 18, 5, 6, 1.5, INK) + rrect(12.5, 36, 5, 6, 1.5, INK))

@small("deltarune")
def deltarune_s():
    heart = path(_heart(32, 25, 1.45), INK, f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return (heart + circle(32, 23, 4, HOLE) +
            poly([(27, 31), (37, 31), (32, 39)], HOLE, 2))

@small("desktop-environment-kde")
def kde_s():
    return shared_kde_s()

@small("de.haeckerfelix.Shortwave")
def shortwave_s():
    return (line(22, 21, 44, 12.5, INK, 3) + rrect(13, 20, 38, 27, 4, INK) +
            circle(26, 33.5, 8.5, HOLE) + line(19.5, 33.5, 32.5, 33.5, INK, 3, "butt") +
            circle(42.5, 28, 3, HOLE) + rrect(39.5, 35, 6, 6, 1.2, HOLE))

@small("dconf-editor")
def dconf_s():
    return (rrect(14, 15, 36, 30, 4, INK) + rrect(14, 23, 36, 3, 0, HOLE) +
            rrect(18.5, 31.5, 9, 4, 2, HOLE) + rrect(32, 29.5, 15, 10, 5, BLUE) +
            circle(42, 34.5, 3.6, INK))
