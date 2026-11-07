# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 23: distributor logos S-Z, DJV to dotTrace.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import arc, registry, ring_b
from glyphs.kit import shared_steam

ICONS, SMALL, reg, small = registry()

def arcs(cx, cy, r, a0, a1, colour, w, cap="round"):
    return (f'<path d="{arc(cx, cy, r, a0, a1)}" fill="none" stroke="{colour}" '
            f'stroke-width="{f(w)}" stroke-linecap="{cap}"/>')

HEART = ("M32 43C22 36 17 30.5 17 24.5C17 20 20.5 17 24.5 17C27.5 17 30.5 18.5 32 21.5"
         "C33.5 18.5 36.5 17 39.5 17C43.5 17 47 20 47 24.5C47 30.5 42 36 32 43Z")

@reg("distributor-logo-salentos", INDIGO_LIGHT)
def salentos():
    hexa = [pt(CX, CY, 17, -90 + 60 * k) for k in range(6)]
    cube = poly(hexa, INK, 3)
    top, ur, lr, bot, ll, ul = hexa
    seams = stroke(f"M{f(ul[0])} {f(ul[1])}L32 30L{f(ur[0])} {f(ur[1])}M32 30V{f(bot[1])}", HOLE, 2.4)
    return cube + seams

@reg("distributor-logo-simply", BLUE)
def simply():
    s = stroke("M29.5 22.5C28 20.5 26 20 24 20C20.5 20 18.5 22 18.5 24.8"
               "C18.5 30.5 30 28.5 30 34.8C30 38 27.5 40 24 40C21.5 40 19 39 17.5 37", INK, 4.6)
    return s + stroke("M36.5 20V40H46.5", INK, 4.6)

@reg("distributor-logo-smartos", LIGHT_BLUE_DEEP)
def smartos():
    return (rrect(16, 14.5, 20, 17, 3.5, "none", f' stroke="{INK}" stroke-width="4"') +
            rrect(28, 28.5, 20, 17, 3.5, "none", f' stroke="{INK}" stroke-width="4"'))

@reg("distributor-logo-solus", BLUE_DARK)
def solus():
    water = path("M17.5 39A16 16 0 0 0 46.5 39Z", BLUE_LIGHT)
    main = path("M30 11.5C25 20 20 29 16.5 36H30Z", INK)
    mid = path("M33.5 19C35.5 25 37 30.5 37.5 36H33.5Z", INK)
    jib = path("M40 25.5C43 29 45.5 32.5 47 35.5L41 36C41 32.5 40.8 29 40 25.5Z", INK)
    hull = path("M15 37.5H49C47.5 40 45 41 42 41H22C19 41 16.5 40 15 37.5Z", INK)
    return water + main + mid + jib + hull

@reg("distributor-logo-steamos", PURPLE_LIGHT)
def steamos():
    return shared_steam()

@reg("distributor-logo-trueos", RED_DEEP)
def trueos():
    outer = path("M32 11C33 18 44 23 44 34C44 41.5 38.5 47 32 47C25.5 47 20 41.5 20 34"
                 "C20 28 24 25 26 19.5C27.5 23.5 28.5 25.5 30 27C31.5 22 32.5 17 32 11Z", INK)
    inner = path("M32 27C33.5 32 37.5 34 37.5 38.5C37.5 41.5 35 44 32 44C29 44 26.5 41.5 26.5 38.5"
                 "C26.5 36 28 34.5 29.5 32.5C30.3 34 30.8 34.5 31.3 35C32 32.5 32.4 30 32 27Z", HOLE)
    return outer + inner

@reg("distributor-logo-tuxedo-os", RED_DEEP)
def tuxedo():
    z = stroke("M15 17H44L21 43H49", INK, 4.6)
    return z + line(24.5, 22.5, 37, 40, INK, 4.2)

def _ubuntu(cx, cy, k=1.0):
    out = ring_b(cx, cy, 10.5 * k, INK, 4.6 * k)
    for a in (180, -60, 60):
        x, y = pt(cx, cy, 15.2 * k, a)
        out += circle(x, y, 6.2 * k, HOLE) + circle(x, y, 4.2 * k, INK)
    return out

@reg("distributor-logo-ubuntu", DEEP_ORANGE)
def ubuntu():
    return _ubuntu(33.5, 30)

@reg("distributor-logo-ubuntu-budgie", BLUE_GREY_DARK)
def ubuntu_budgie():
    out = ""
    for a in (-55, 65, 185):
        x, y = pt(CX, CY, 9.5, a)
        bx, by = pt(x, y, 6.2, a + 140)
        out += circle(x, y, 7.4, INK) + circle(bx, by, 2.8, HOLE)
    return out

@reg("distributor-logo-ubuntu-mate", CYAN_DEEP)
def ubuntu_mate():
    cx, cy = 31, 30
    out = ""
    for a0, a1 in [(-160, -77), (-41, 41), (77, 160)]:
        out += arcs(cx, cy, 14, a0, a1, INK, 2.8) + arcs(cx, cy, 8.5, a0 + 4, a1 - 4, INK, 2.8)
    for a in (180, -59, 59):
        x, y = pt(cx, cy, 14, a)
        out += poly([(x - 3.5, y - 4.6), (x - 3.5, y + 4.6), (x + 4.8, y)], INK, 1.6)
    return out

@reg("distributor-logo-ubuntu-studio", LIGHT_BLUE_DEEP)
def ubuntu_studio():
    out = ring_b(CX, CY, 4.6, INK, 3.4)
    out += arcs(CX, CY, 10.5, -145, 145, INK, 3.2) + arcs(CX, CY, 10.5, 168, 192, INK, 3.2)
    out += (arcs(CX, CY, 16.2, -110, -45, INK, 3.2) + arcs(CX, CY, 16.2, 45, 110, INK, 3.2) +
            arcs(CX, CY, 16.2, 168, 192, INK, 3.2))
    return out

@reg("distributor-logo-ultimate-edition", GREY_DEEP)
def ultimate_edition():
    rim = arcs(CX, CY, 15.5, -15, -65 + 360, INK, 3.6)
    u = stroke("M20.5 23.5V31.5A4.25 4.25 0 0 0 29 31.5V23.5", INK, 3.2)
    e = stroke("M42.5 23.5H34.5V36H42.5M34.5 29.8H41", INK, 3.2)
    return rim + u + e

@reg("distributor-logo-vanilla-os", ORANGE_DEEP)
def vanilla_os():
    petal = "M32 30C28 24.5 27.5 17.5 32 12C36.5 17.5 36 24.5 32 30Z"
    out = "".join(g(path(petal, INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"'),
                    f"rotate({72 * k} 32 31)") for k in range(5))
    return out + circle(32, 31, 3, HOLE) + circle(32, 31, 1.4, INK)

@reg("distributor-logo-void", LIGHT_BLUE_DEEP)
def void():
    upper = arcs(CX, CY, 12.5, -128, 38, INK, 5.2, "butt")
    lower = arcs(CX, CY, 12.5, 52, 218, LIGHT_BLUE_SOFT, 5.2, "butt")
    return upper + lower + circle(CX, CY, 5.4, INK)

@reg("distributor-logo-voyager", DEEP_ORANGE_DEEP)
def voyager():
    return rrect(22, 13, 5.8, 34, 1.5, INK) + rrect(22, 41.2, 21, 5.8, 1.5, INK)

@reg("distributor-logo-windows", BLUE_DEEP)
def windows():
    panes = [[(16, 17), (30, 15.1), (30, 29), (16, 29)],
             [(32.5, 14.7), (48, 12.5), (48, 29), (32.5, 29)],
             [(16, 31.5), (30, 31.5), (30, 45.4), (16, 43.5)],
             [(32.5, 31.5), (48, 31.5), (48, 48), (32.5, 45.8)]]
    return "".join(poly(p, INK, 1) for p in panes)

@reg("distributor-logo-zorin", LIGHT_BLUE)
def zorin():
    lx = lambda y: 21.5 - (y - 14) * .5 if y <= 30 else 13.5 + (y - 30) * .5
    rx = lambda y: 64 - lx(y)
    cap = poly([(21.5, 14), (42.5, 14), (rx(19.2), 19.2), (lx(19.2), 19.2)], INK, 1.2)
    z = poly([(lx(22), 22), (rx(22), 22), (rx(25.5), 25.5), (24, 34.5), (rx(34.5), 34.5),
              (rx(38), 38), (lx(38), 38), (lx(34.5), 34.5), (40, 25.5), (lx(25.5), 25.5)], INK, 1.2)
    foot = poly([(lx(40.8), 40.8), (rx(40.8), 40.8), (42.5, 46), (21.5, 46)], INK, 1.2)
    return cap + z + foot

@reg("djv", BLUE_GREY_DEEP)
def djv():
    holes = "".join(circle(*pt(CX, CY, 9.2, -90 + 72 * k), 4.2, HOLE) for k in range(5))
    return circle(CX, CY, 16.5, INK) + holes + circle(CX, CY, 1.8, HOLE)

@reg("dk.tangramgames.mrrescue", RED_DEEP)
def mrrescue():
    helmet = path("M19.5 26C19.5 18.5 25 14 32 14C39 14 44.5 18.5 44.5 26Z", INK)
    spike = poly([(29.5, 15), (32, 10.5), (34.5, 15)], INK, 2)
    brim = rrect(16, 24.5, 32, 4, 2, INK)
    mask = path("M20.5 31H43.5V36.5C43.5 42.5 38.5 46.5 32 46.5C25.5 46.5 20.5 42.5 20.5 36.5Z", INK)
    lenses = (poly([pt(26.5, 35, 3.8, 30 + 60 * k) for k in range(6)], HOLE, 1) +
              poly([pt(37.5, 35, 3.8, 30 + 60 * k) for k in range(6)], HOLE, 1))
    filt = circle(32, 41, 3.4, HOLE) + circle(32, 41, 1.6, INK)
    return helmet + spike + brim + mask + lenses + filt

@reg("dmanager", BLUE_DEEP)
def dmanager():
    hexa = poly([pt(CX, CY, 17, -90 + 60 * k) for k in range(6)], INK, 3)
    d = ring_b(29.5, 34, 5, HOLE, 3.4) + line(34.5, 20.5, 34.5, 39, HOLE, 3.4)
    return hexa + d

@reg("dmd-doc", RED_DEEP)
def dmd_doc():
    d = stroke("M19.5 18V42H25A10.5 12 0 0 0 25 18Z", INK, 5.4)
    return d + circle(45, 19.5, 4, INK)

@reg("dnfdragora", RED_LIGHT)
def dnfdragora():
    h = [pt(CX, CY, 16, -90 + 60 * k) for k in range(6)]
    top, ur, lr, bot, ll, ul = h
    outline = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in h) + "Z", INK, 3.2)
    y = stroke(f"M{f(ul[0])} {f(ul[1])}L32 30L{f(ur[0])} {f(ur[1])}M32 30V{f(bot[1])}", INK, 3.2)
    tape = stroke("M25 18L38.5 26V33", INK, 3.2)
    return outline + y + tape

@reg("dockbarx", BLUE_DEEP)
def dockbarx():
    win = rrect(17, 13, 30, 21, 3, INK) + rrect(17, 18, 30, 2.4, 0, HOLE)
    dock = rrect(14, 38, 36, 10, 3, INK)
    items = rrect(18.5, 40.5, 7, 5, 1.5, HOLE) + circle(32, 43, 2.8, HOLE) + rrect(38.5, 40.5, 7, 5, 1.5, HOLE)
    return win + dock + items

def _docker(s, pitch, rows):
    whale = path("M13.5 31.5H45.5C46.5 29 48.5 27.5 51 28C50.5 30 49.5 31.5 47.5 32.5"
                 "C45 41 38 46.5 28.5 46.5C20 46.5 15 40.5 13.5 31.5Z", INK)
    boxes = ""
    for r, cols in enumerate(rows):
        y = 30.5 - s - r * pitch
        for c in cols:
            boxes += rrect(16.5 + c * pitch, y, s, s, .8, INK)
    return whale + boxes + circle(21.5, 37.5, 1.6, HOLE)

@reg("docker-desktop", BLUE_DEEP)
def docker():
    return _docker(4, 4.8, [range(5), range(1, 4), [3]])

@reg("dockstation", LIGHT_BLUE)
def dockstation():
    water = path("M15.5 30C20 26.5 24 26.5 28.5 29C33 31.5 37 32 41 29.5C44 27.8 46.5 27.8 48.5 29.5"
                 "A16.5 16.5 0 0 1 15.5 30Z", INK)
    bubbles = circle(38, 39, 3, HOLE) + circle(25.5, 36, 2, HOLE)
    return ring_b(CX, CY, 15.3, INK, 2.6) + water + bubbles

@reg("document-viewer", BLUE_GREY)
def document_viewer():
    sheet = path("M20 11H37L46 20V46A3 3 0 0 1 43 49H20A3 3 0 0 1 17 46V14A3 3 0 0 1 20 11Z", INK)
    fold = path("M37 11V17A3 3 0 0 0 40 20H46Z", BLUE_GREY_SOFT)
    pic = rrect(21, 16, 12, 11, 2, HOLE) + poly([(22.5, 25.5), (26.5, 20.5), (29, 23.5), (31.5, 21.5), (31.5, 25.5)], INK, 1)
    lines = "".join(rrect(21, y, w, 2.6, 1.3, HOLE) for y, w in [(31, 21), (36, 21), (41, 14)])
    return sheet + fold + pic + lines

@reg("dods", INDIGO_LIGHT)
def dods():
    star = poly([pt(32, 20.5, 9.5 if k % 2 == 0 else 4, -90 + 36 * k) for k in range(10)], INK, 1.5)
    cross = ""
    for k in range(4):
        arm = poly([(30.8, 38), (33.2, 38), (35.8, 30.5), (28.2, 30.5)], INK, 1.2)
        cross += g(arm, f"rotate({90 * k} 32 38.5)")
    return star + cross + circle(32, 38.5, 2, INK)

def _ddlc_heart(cx, cy, k):
    return g(path(HEART, INK), f"translate({cx} {cy}) scale({k}) translate(-32 -30)")

@reg("doki-doki-literature-club", PINK_SOFT)
def ddlc():
    return ring_b(CX, CY, 15.5, INK, 3.2) + _ddlc_heart(32, 30.5, .66)

@reg("doki-doki-literature-club-plus", PINK_LIGHT)
def ddlc_plus():
    base = ring_b(29, 27.5, 13.5, INK, 3) + _ddlc_heart(29, 28, .56)
    badge = circle(42.5, 41, 10, HOLE) + circle(42.5, 41, 8, INK)
    plus = line(42.5, 36.8, 42.5, 45.2, HOLE, 3) + line(38.3, 41, 46.7, 41, HOLE, 3)
    return base + badge + plus

@reg("doki-doki-mod-manager", PINK_DEEP)
def ddlc_mods():
    teeth = "".join(g(rrect(29, 11.5, 6, 8, 1.5, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    return teeth + circle(CX, CY, 13.5, INK) + g(path(HEART, HOLE), "translate(32 30.5) scale(.5) translate(-32 -30)")

@reg("dolphin-emu", BLUE_DEEP)
def dolphin_emu():
    body = path("M12.5 31C16 26 21 23 27 21.5C36 19.5 45 24 49 33C50 36 50.5 40 50 44"
                "C47.5 39 45 35 41 32.5C36 29.5 30 29 25 30.5C21 31.5 17 33 14 35"
                "C13.5 33.5 13 32.5 12.5 31Z", INK)
    fin = path("M29.5 21.8C30.5 18 33 15 37 14C36 16.5 36 19 37 21.5Z", INK)
    flipper = path("M29 30C28 33.5 25.5 36 22 37C23.5 34.5 24 32.5 24 30.8Z", INK)
    return body + fin + flipper

def _wilson(face_ext=""):
    face = path("M21 24C21 34 25 44.5 32 46C39 44.5 43 34 43 24Z", INK)
    hair = path("M18.5 29L14 22.5L19.5 21.5L15.5 13.5L23.5 16L25.5 9.5L30.5 14L34.5 8.5L37.5 14.5"
                "L43.5 10.5L42.5 17L50 16.5L45 22.5L48.5 28.5L42.5 26L32 24.5L21.5 26Z", INK,
                f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"')
    brows = stroke("M24.5 30L29 31.5M39.5 30L35 31.5", HOLE, 2.2)
    eyes = circle(27.5, 34.5, 1.6, HOLE) + circle(36.5, 34.5, 1.6, HOLE)
    mouth = stroke("M29.5 41H34", HOLE, 2.2)
    return face + hair + brows + eyes + mouth

@reg("dont-starve", BLUE_GREY_DEEP)
def dont_starve():
    return _wilson()

@reg("dont-starve-together", ORANGE_DARK)
def dont_starve_together():
    return _wilson()

@reg("dooble", INDIGO_DEEP)
def dooble():
    left = [(22, 18), (25.5, 21), (26.8, 25), (26.3, 27.5), (29, 31.3), (27.4, 32.4), (28, 34),
            (26.6, 35.4), (27.6, 37), (26.2, 39), (25.2, 42), (22, 43.5)]
    right = [(64 - x, y) for x, y in reversed(left)]
    stem = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in left + right) + "Z"
    vase = path(stem, INK, f' stroke="{INK}" stroke-width="1" stroke-linejoin="round"')
    return vase + rrect(17, 14.5, 30, 4.6, 2.3, INK) + rrect(20, 42, 24, 4.6, 2.3, INK)

def _doom(y0):
    out = ""
    x = 13.6
    tall, short = (y0, 19), (y0 + 1.5, 15.5)
    for ch in "DOOM":
        yy, h = tall if ch in "DM" else short
        if ch == "D":
            out += poly([(x, yy), (x + 5.5, yy), (x + 7.6, yy + 2.5), (x + 7.6, yy + h - 2.5),
                         (x + 5.5, yy + h), (x, yy + h)], INK, .8)
            out += rrect(x + 2.7, yy + 3.6, 2.2, h - 7.2, 1.1, HOLE)
            x += 7.6
        elif ch == "O":
            out += rrect(x, yy, 7.6, h, 1.8, INK) + rrect(x + 2.7, yy + 3.4, 2.2, h - 6.8, 1.1, HOLE)
            x += 7.6
        else:
            w = 9.8
            out += poly([(x, yy), (x + 3, yy), (x + w / 2, yy + 5), (x + w - 3, yy), (x + w, yy),
                         (x + w, yy + h), (x + w - 2.8, yy + h), (x + w - 2.8, yy + 8),
                         (x + w / 2, yy + 11), (x + 2.8, yy + 8), (x + 2.8, yy + h), (x, yy + h)], INK, .8)
            x += w
        x += 1.6
    return out

@reg("doom", DEEP_ORANGE_DARK)
def doom():
    return _doom(20.5)

@reg("doom-eternal", RED_DARK)
def doom_eternal():
    bar = rrect(18, 41.5, 28, 3.6, 1.8, INK) + g(rrect(29.5, 38.5, 5, 5, 1, INK), "rotate(45 32 41)")
    return _doom(16) + bar

@reg("doom3", RED_DEEP)
def doom3():
    p = [pt(CX, 31, 15.5, 90 + 72 * k) for k in range(5)]
    order = [p[(2 * k) % 5] for k in range(5)]
    star = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in order) + "Z", INK, 2.6)
    return ring_b(CX, 31, 16.3, INK, 2.4) + star

@reg("doomseeker", RED_DEEP)
def doomseeker():
    d = path("M17 16H32A14 14 0 0 1 32 44H17Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return d + rrect(11, 27, 27, 6, 3, HOLE)

@reg("door-kickers", BLUE_GREY_DEEP)
def door_kickers():
    head = circle(28.5, 16.5, 3.8, INK) + path("M24.2 16.5A4.3 4.3 0 0 1 32.8 16.5Z", INK)
    torso = poly([(23.5, 22), (32, 22), (30.5, 34), (22, 34)], INK, 3)
    pack = rrect(18.5, 22, 5, 10, 2, INK)
    arms = stroke("M30 24.5L38 23", INK, 3.4)
    rifle = line(31, 21.5, 50, 21.5, INK, 2.4) + line(40.5, 22, 40.5, 25.5, INK, 2.4)
    legs = stroke("M28.5 32.5L37 34L37.5 44.5", INK, 4.6) + stroke("M24.5 32.5L24 44L16.5 44.5", INK, 4.6)
    return head + torso + pack + arms + rifle + legs

@reg("dopamine", INDIGO_LIGHT)
def dopamine():
    return ring_b(31, 32, 11.8, INK, 4.6) + line(42.7, 32, 42.7, 14, INK, 4.6) + circle(31, 32, 4, INK)

_FONT = {
    "D": ["110", "101", "101", "101", "110"],
    "O": ["111", "101", "101", "101", "111"],
    "S": ["111", "100", "111", "001", "111"],
    "B": ["110", "101", "110", "101", "110"],
    "X": ["101", "101", "010", "101", "101"],
}

def _pixtext(lines, x0, y0, c, gap, lgap, fill):
    d = ""
    for li, word in enumerate(lines):
        for ci, ch in enumerate(word):
            for r, row in enumerate(_FONT[ch]):
                for k, bit in enumerate(row):
                    if bit == "1":
                        x = x0 + ci * (3 * c + gap) + k * c
                        y = y0 + li * (5 * c + lgap) + r * c
                        d += f"M{f(x)} {f(y)}h{f(c)}v{f(c)}h{f(-c)}Z"
    return path(d, fill)

def _dosbox():
    screen = rrect(14.5, 11.5, 35, 37, 4, INK)
    return screen + _pixtext(["DOS", "BOX"], 17, 14, 3, 2, 3, HOLE)

@reg("dosbox", ORANGE_DARK)
def dosbox():
    return _dosbox()

@reg("dosbox-ece", CYAN_DEEP)
def dosbox_ece():
    return _dosbox()

@reg("dosbox-staging", BLUE_GREY)
def dosbox_staging():
    return _dosbox()

@reg("dosbox-x", DEEP_PURPLE)
def dosbox_x():
    return _dosbox()

@reg("dota-underlords", GREY_DARK)
def dota_underlords():
    left = poly([(16, 14), (25, 23), (16, 32)], INK, 2)
    right = poly([(48, 46), (39, 37), (48, 28)], INK, 2)
    a = poly([(16, 38), (37, 14), (44, 14), (16, 45)], INK, 1.5)
    b = poly([(20, 46), (48, 15), (48, 22), (27, 46)], INK, 1.5)
    return left + right + a + b

@reg("dota2", RED_DEEP)
def dota2():
    s, x0, y0 = 34, 15, 13
    P = lambda pts: [(x0 + u * s, y0 + v * s) for u, v in pts]
    sq = rrect(x0, y0, s, s, 4, INK)
    band = poly(P([(.12, .25), (.25, .12), (.88, .75), (.75, .88)]), HOLE, 1)
    tr = poly(P([(.58, .12), (.88, .12), (.88, .42)]), HOLE, 1)
    bl = poly(P([(.12, .58), (.12, .88), (.42, .88)]), HOLE, 1)
    return sq + band + tr + bl

_LETTERS = {
    "D": lambda x: f"M{x} 18.5V30.5H{x + 3.5}A5 6 0 0 0 {x + 3.5} 18.5Z",
    "C": lambda x: f"M{x + 8.4} 20.3A5 6 0 1 0 {x + 8.4} 28.7",
    "M": lambda x: f"M{x} 30.5V18.5L{x + 4.5} 25L{x + 9} 18.5V30.5",
    "P": lambda x: f"M{x} 30.5V18.5H{x + 4.5}A3.5 3.5 0 0 1 {x + 4.5} 25.5H{x}",
    "T": lambda x: f"M{x - .5} 18.5H{x + 9.5}M{x + 4.5} 18.5V30.5",
}

def _dot(second):
    sq = rrect(15, 13, 34, 34, 3, INK)
    letters = stroke(_LETTERS["D"](20.5) + _LETTERS[second](33), HOLE, 3.2)
    return sq + letters + rrect(20.5, 38.5, 12, 3.2, 1.6, HOLE)

@reg("dotcover", DEEP_ORANGE_LIGHT)
def dotcover():
    return _dot("C")

@reg("dotmemory", DEEP_PURPLE_LIGHT)
def dotmemory():
    return _dot("M")

@reg("dotpeek", TEAL_LIGHT)
def dotpeek():
    return _dot("P")

@reg("dottrace", PINK_DEEP)
def dottrace():
    return _dot("T")

@small("docker-desktop")
def docker_s():
    return _docker(5.4, 6.4, [range(4), [2]])

@small("distributor-logo-ubuntu-mate")
def ubuntu_mate_s():
    cx, cy = 31, 30
    out = "".join(arcs(cx, cy, 13, a0, a1, INK, 3.6) for a0, a1 in [(-158, -80), (-38, 38), (80, 158)])
    for a in (180, -59, 59):
        x, y = pt(cx, cy, 13.5, a)
        out += poly([(x - 4, y - 5.2), (x - 4, y + 5.2), (x + 5.4, y)], INK, 1.6)
    return out

@small("distributor-logo-ubuntu-studio")
def ubuntu_studio_s():
    return ring_b(CX, CY, 5, INK, 4) + arcs(CX, CY, 13, -140, 140, INK, 4)

@small("distributor-logo-ultimate-edition")
def ultimate_edition_s():
    rim = arcs(CX, CY, 16, -15, -65 + 360, INK, 3.6)
    u = stroke("M19.5 22V31.5A4.75 4.75 0 0 0 29 31.5V22", INK, 3.6)
    e = stroke("M44 22H35V37.5H44M35 29.8H42.5", INK, 3.6)
    return rim + u + e

def _dosbox_s():
    return rrect(13, 18.5, 38, 23, 4, INK) + _pixtext(["DOS"], 15, 21.5, 3.4, 1.7, 0, HOLE)

for _n in ("dosbox", "dosbox-ece", "dosbox-staging", "dosbox-x"):
    small(_n)(_dosbox_s)

@small("doom3")
def doom3_s():
    p = [pt(CX, 31, 16.5, 90 + 72 * k) for k in range(5)]
    order = [p[(2 * k) % 5] for k in range(5)]
    return stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in order) + "Z", INK, 3.4)

@small("dnfdragora")
def dnfdragora_s():
    h = [pt(CX, CY, 16.5, -90 + 60 * k) for k in range(6)]
    top, ur, lr, bot, ll, ul = h
    outline = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in h) + "Z", INK, 3.6)
    return outline + stroke(f"M{f(ul[0])} {f(ul[1])}L32 30L{f(ur[0])} {f(ur[1])}M32 30V{f(bot[1])}", INK, 3.6)

@small("dockstation")
def dockstation_s():
    water = path("M15.5 30C20 26.5 24 26.5 28.5 29C33 31.5 37 32 41 29.5C44 27.8 46.5 27.8 48.5 29.5"
                 "A16.5 16.5 0 0 1 15.5 30Z", INK)
    return ring_b(CX, CY, 15, INK, 3.2) + water + circle(36, 38.5, 3.6, HOLE)
