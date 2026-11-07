# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 67: system-suspend to the-sims-4.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import ellipse_i, registry, ring_b

ICONS, SMALL, reg, small = registry()

def oval(cx, cy, rx, ry, fill):
    d, fl = ellipse_i(cx, cy, rx, ry, fill)
    return path(d, fl)

@reg("system-suspend", CYAN)
def system_suspend():
    return ring_b(CX, CY, 15, INK, 4.6) + rrect(22.5, 27.25, 19, 5.5, 2.75, INK)

@reg("system-suspend-hibernate", DEEP_PURPLE)
def system_hibernate():
    return ring_b(CX, CY, 15, INK, 4.6) + circle(CX, CY, 5.2, INK)

@reg("system-switch-user", INDIGO)
def system_switch_user():
    up = line(25, 45, 25, 20, INK, 4.2) + poly([(25, 13), (32, 22), (18, 22)], INK, 2.5)
    down = line(39, 15, 39, 40, INK, 4.2) + poly([(39, 47), (46, 38), (32, 38)], INK, 2.5)
    return up + down

@reg("system-users", TEAL)
def system_users():
    head = circle(32, 20.5, 7.5, INK)
    body = path("M17 45C17 37 23.5 32 32 32C40.5 32 47 37 47 45Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return head + body

@reg("system76-driver", BROWN_DARK)
def system76():
    seven = stroke("M15.5 17H28.5L19.5 42", INK, 4)
    six = stroke("M45 15.5C39 18.5 33.5 25 32.8 33", INK, 4) + ring_b(40, 35.5, 7.2, INK, 4)
    return seven + six + rrect(33, 45.5, 15, 3.6, 1.8, ORANGE)

@reg("tabletop-simulator", BLUE_GREY_DARK)
def tabletop_simulator():
    spade = path("M28 19.5C24.5 23.5 21 25.5 21 29C21 32 24.5 33.5 27 31.5L25.5 36H30.5L29 31.5"
                 "C31.5 33.5 35 32 35 29C35 25.5 31.5 23.5 28 19.5Z", HOLE)
    card = g(rrect(16, 13, 24, 32, 3.5, INK) + spade, "rotate(-8 28 29)")
    die = rrect(33, 31, 16, 16, 4, BLUE_LIGHT, f' stroke="{HOLE}" stroke-width="2"')
    pips = "".join(circle(x, y, 1.6, INK) for x, y in
                   [(37, 35), (45, 35), (41, 39), (37, 43), (45, 43)])
    return card + die + pips

@reg("tagainijisho", BLUE_DEEP)
def tagainijisho():
    bars = line(18, 16, 46, 16, INK, 4.2) + line(16, 44, 48, 44, INK, 4.2)
    kanji = stroke("M29.5 16.5L25.5 30H39.5L37 43.5", INK, 4.2) + stroke("M32.5 23H40.5L39.5 30", INK, 4.2)
    return bars + kanji

@reg("taisei", TEAL_DARK)
def taisei():
    swoosh = stroke("M43 14C31 11 19.5 17 19.5 27C19.5 37 28 44.5 45 44.5", TEAL_SOFT, 2.6)
    t = (stroke("M34 16V36.5C34 40.5 36 42 40 41.5", INK, 4.4) +
         line(28, 24.5, 40.5, 24.5, INK, 4.2))
    return swoosh + t

@reg("tamtam-app", INDIGO_LIGHT)
def tamtam():
    bubble = path("M33 14A15 15 0 1 1 25.5 42L16.5 45.5L18.9 34.1A15 15 0 0 1 33 14Z", INK,
                  f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    smile = path("M23.5 28.5H42.5A9.5 8.5 0 0 1 23.5 28.5Z", HOLE)
    return bubble + smile

@reg("tandem", BLUE)
def tandem():
    return (poly([(18.5, 20), (29, 15.5), (29, 40), (18.5, 44.5)], INK, 3) +
            poly([(35, 20), (45.5, 15.5), (45.5, 40), (35, 44.5)], INK, 3))

@reg("tanglet", BLUE_DEEP)
def tanglet():
    return g(rrect(15, 13, 34, 34, 8, INK) + stroke("M23.5 22.5H40.5M32 22.5V39", HOLE, 5.2),
             "rotate(-10 32 30)")

@reg("tartube", PURPLE_LIGHT)
def tartube():
    return circle(CX, CY, 16.5, INK) + poly([(27.5, 21.5), (40.5, 30), (27.5, 38.5)], RED, 3)

@reg("taskbar", BLUE_DEEP)
def taskbar():
    return "".join(rrect(15, y, 8, 7.5, 2.2, INK) + rrect(26, y, 23, 7.5, 2.5, INK)
                   for y in (15.5, 26.25, 37))

@reg("tauonmb", PURPLE)
def tauonmb():
    disc = circle(CX, CY, 16.5, INK)
    arcs = (stroke("M20.2 37.5A13 13 0 0 1 19.4 25", PURPLE_SOFT, 5) +
            stroke("M43.8 22.5A13 13 0 0 1 44.6 35", PURPLE_SOFT, 5))
    return disc + arcs + circle(CX, CY, 5, HOLE) + circle(CX, CY, 2, INK)

@reg("taxi", AMBER)
def taxi():
    s, x0 = 6.5, 15.75
    return "".join(rrect(x0 + c * s, 23.5 + r * s, s, s, 0.6, INK)
                   for r in range(2) for c in range(5) if (r + c) % 2 == 0)

@reg("tc", DEEP_PURPLE)
def tc():
    back = rrect(13.5, 14, 22, 17, 5, INK) + poly([(18, 30), (17.5, 37), (24, 30)], INK, 2)
    front = (rrect(28.5, 21, 22, 17, 5, INK, f' stroke="{HOLE}" stroke-width="2.4"') +
             poly([(45.5, 38.5), (46, 45), (39.5, 38.5)], INK, 2))
    return back + front

@reg("tdeprintfax", BLUE_GREY_DEEP)
def tdeprintfax():
    body = rrect(13.5, 13, 37, 24, 4, INK)
    screen = rrect(18, 17.5, 13, 7, 1.5, BLUE_LIGHT)
    keys = "".join(circle(x, y, 1.7, HOLE) for x in (36.5, 41, 45.5) for y in (19, 24))
    slot = rrect(18, 29.5, 28, 2.6, 1.3, HOLE)
    paper = rrect(19.5, 34, 25, 14, 2, INK, f' stroke="{HOLE}" stroke-width="2"')
    lines = rrect(23.5, 38.5, 17, 2.4, 1.2, HOLE) + rrect(23.5, 42.5, 11, 2.4, 1.2, HOLE)
    return body + screen + keys + slot + paper + lines

@reg("tdewalletmanager", RED_DEEP)
def tdewalletmanager():
    wallet = rrect(13.5, 14, 34, 32, 5, INK)
    stitch = (f'<rect x="17" y="17.5" width="27" height="25" rx="3" fill="none" stroke="{HOLE}" '
              'stroke-width="2.2" stroke-dasharray="3.2 2.4"/>')
    clasp = rrect(38, 25, 13, 10, 3.5, RED_DARK) + circle(43.5, 30, 2, INK)
    return wallet + stitch + clasp

def _tf(rot):
    cross = g(line(CX, 13, CX, 47, HOLE, 5, "butt") + line(15, CY, 49, CY, HOLE, 5, "butt"),
              f"rotate({rot} 32 30)")
    return (circle(CX, CY, 16.5, INK) + cross +
            circle(CX, CY, 6, HOLE))

@reg("team-fortress-classic", AMBER_DEEP)
def tfc():
    return _tf(0)

@reg("team-fortress2", DEEP_ORANGE_DEEP)
def tf2():
    return _tf(22)

@reg("team-fortress2-classified", BROWN)
def tf2_classified():
    return _tf(-24)

@reg("teamcity", DEEP_PURPLE_DARK)
def teamcity():
    sq = rrect(15, 13, 34, 34, 4, INK)
    t = stroke("M20.5 20H29M24.75 20V32", HOLE, 3.6)
    c = stroke("M42 22C41 20.6 39.7 20 38.2 20C35 20 33 22.5 33 26C33 29.5 35 32 38.2 32"
               "C39.7 32 41 31.4 42 30", HOLE, 3.6)
    return sq + t + c + rrect(20, 37.5, 12, 3.6, 1.8, HOLE)

@reg("teams-for-linux", INDIGO)
def teams():
    people = (circle(43.5, 18.5, 4.2, INDIGO_SOFT) + rrect(38, 25, 12, 17, 5, INDIGO_SOFT) +
              circle(33, 16.5, 5.5, DEEP_PURPLE_SOFT) + rrect(25, 24, 18, 22, 8, DEEP_PURPLE_SOFT))
    plate = rrect(13.5, 21.5, 19, 19, 3.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    return people + plate + stroke("M18 27H28M23 27V36", HOLE, 3.4)

@reg("teamspeak3", INDIGO_DARK)
def teamspeak():
    band = stroke("M17 32A15 15 0 0 1 47 32", INK, 3.6)
    cups = rrect(13, 29, 7.5, 13, 3.5, INK) + rrect(43.5, 29, 7.5, 13, 3.5, INK)
    head = circle(32, 34, 11, INK)
    eyes = (poly([(24.5, 31), (30, 33.5), (29, 36.5), (25, 34.5)], HOLE, 1.2) +
            poly([(39.5, 31), (34, 33.5), (35, 36.5), (39, 34.5)], HOLE, 1.2))
    mic = stroke("M47 40C45.5 45 41 47.5 36 47", INK, 2.6)
    return band + cups + head + eyes + mic

@reg("teamviewer", BLUE)
def teamviewer():
    arrow = poly([(18, 30), (25.5, 22.5), (25.5, 27), (38.5, 27), (38.5, 22.5), (46, 30),
                  (38.5, 37.5), (38.5, 33), (25.5, 33), (25.5, 37.5)], HOLE, 1.5)
    return circle(CX, CY, 16.5, INK) + arrow

@reg("technic-launcher", BLUE_DEEP)
def technic():
    rim = ring_b(CX, CY, 15.5, INK, 3.6)
    jaw = stroke("M27 17.5V21C27 23.2 29 24.5 32 24.5C35 24.5 37 23.2 37 21V17.5", INK, 3.4)
    shaft = rrect(29.5, 24, 5, 19, 2.5, INK)
    prongs = line(24.5, 31, 29.5, 31, INK, 2.6) + line(24.5, 36.5, 29.5, 36.5, INK, 2.6)
    return rim + jaw + shaft + prongs

@reg("teeworlds", AMBER_DEEP)
def teeworlds():
    body = circle(32, 27.5, 14.5, INK)
    feet = rrect(15, 38.5, 16, 8.5, 4.25, ORANGE_DARK) + rrect(33, 38.5, 16, 8.5, 4.25, ORANGE_DARK)
    eyes = oval(28.5, 25, 2.3, 4, BROWN_DARK) + oval(36, 25, 2.3, 4, BROWN_DARK)
    return body + feet + eyes

@reg("tegaki-recognize", GREY_SOFT)
def tegaki():
    return (line(16.5, 21, 47.5, 21, INK, 4) + line(32, 13, 32, 47, INK, 4) +
            stroke("M30.5 22C27.5 30 23 36 16.5 40.5", INK, 4) +
            stroke("M33.5 22C36.5 30 41 36 47.5 40.5", INK, 4) +
            line(26, 38, 38, 38, INK, 4))

@reg("tekken-7", RED)
def tekken():
    seven = poly([(16, 17), (49, 17), (47.5, 23.5), (31.5, 44), (22.5, 44), (37.5, 24.5), (14.5, 24.5)],
                 INK, 2.5)
    return seven + line(13, 21, 42, 21, HOLE, 2.2, "butt")

@reg("tellico", BLUE_GREY_DARK)
def tellico():
    return (rrect(25, 13, 24, 7, 2, YELLOW_LIGHT) + rrect(15, 22.5, 24, 7, 2, RED_LIGHT) +
            rrect(24, 32, 24, 7, 2, BLUE_LIGHT) + rrect(16, 41.5, 24, 7, 2, BLUE_GREY_SOFT))

@reg("tenacity", RED_DEEP)
def tenacity():
    box = rrect(14, 12, 36, 36, 6, INK)
    plus = (rrect(27.5, 16, 9, 28, 1, HOLE) + rrect(18, 25.5, 28, 9, 1, HOLE) +
            rrect(27.5, 16, 4.5, 4.5, 0, INK) + rrect(41.5, 30, 4.5, 4.5, 0, INK))
    return box + plus

@reg("terminator", RED_DEEP)
def terminator():
    box = rrect(14, 13, 36, 34, 4.5, INK)
    split = line(32, 13, 32, 47, HOLE, 2.6, "butt") + line(14, 30, 50, 30, HOLE, 2.6, "butt")
    txt = "".join(rrect(x, y, w, 2.6, 1.3, HOLE) for x, y, w in
                  [(18, 17.5, 10), (18, 22, 7), (36, 35, 10), (36, 39.5, 7)])
    return box + split + txt

@reg("terminus", BLUE_GREY_DARK)
def terminus():
    return poly([(18, 16), (47, 30), (18, 44), (18, 36.5), (32, 30), (18, 23.5)], INK, 3)

@reg("termius-app", INDIGO_DARK)
def termius():
    cloud = (circle(24, 33, 8.5, INK) + circle(34, 25, 11, INK) + circle(42, 34, 7.5, INK) +
             rrect(15.5, 32, 34, 12, 6, INK))
    prompt = stroke("M25.5 28.5L30 32L25.5 35.5", HOLE, 2.8) + line(33, 37, 39.5, 37, HOLE, 2.8)
    return cloud + prompt

@reg("terraria", BLUE_GREY)
def terraria():
    crown = "".join(circle(x, y, r, INK) for x, y, r in
                    [(27, 20, 7), (36, 18, 7.5), (41, 26, 6.5), (23, 27, 6.5), (32, 27, 7.5)])
    trunk = poly([(29, 31), (35, 31), (36.5, 47), (27.5, 47)], BROWN_SOFT, 1.5)
    branch = stroke("M35 39L40 35.5", BROWN_SOFT, 2.4)
    leaves = circle(19.5, 38, 3.2, INK) + circle(42.5, 34.5, 3, INK)
    return trunk + branch + crown + leaves

@reg("terratech", LIGHT_BLUE_DEEP)
def terratech():
    sq = rrect(19, 17, 26, 26, 5, INK)
    x = stroke("M26.5 24.5L37.5 35.5M37.5 24.5L26.5 35.5", HOLE, 4.6)
    tips = (poly([(28, 14.5), (36, 14.5), (32, 10.5)], INK, 1.5) +
            poly([(28, 45.5), (36, 45.5), (32, 49.5)], INK, 1.5) +
            poly([(16.5, 26), (16.5, 34), (12.5, 30)], INK, 1.5) +
            poly([(47.5, 26), (47.5, 34), (51.5, 30)], INK, 1.5))
    return sq + x + tips

@reg("tetrio-desktop", PURPLE_DEEP)
def tetrio():
    t = rrect(14, 14, 25, 7.5, 1.5, INK) + rrect(22.75, 14, 7.5, 32, 1.5, INK)
    hook = stroke("M36 29H46.5V41H39.5", CYAN_LIGHT, 5)
    return t + hook

@reg("tetzle", BLUE_DEEP)
def tetzle():
    out = ""
    for r in range(3):
        for c in range(3):
            if (r, c) == (0, 2):
                continue
            colour = INK if r < 2 else AMBER
            out += rrect(16 + c * 11.5, 16 + r * 11.5, 9.5, 9.5, 2.2, colour)
    return out + g(rrect(39, 11, 9.5, 9.5, 2.2, INK), "rotate(12 43.75 15.75)")

def _tex(colour, w=3.8):
    t = stroke("M14.5 21H24.5M19.5 21V37", colour, w)
    e = stroke("M34.5 25.5H27.5V41H34.5M27.5 33H33", colour, w)
    x = stroke("M38 21L49 37M49 21L38 37", colour, w)
    return t + e + x

@reg("texmaker", DEEP_PURPLE_LIGHT)
def texmaker():
    return _tex(INK)

@reg("texstudio", INDIGO_DEEP)
def texstudio():
    return _tex(YELLOW_LIGHT)

@reg("textadept", AMBER_DEEP)
def textadept():
    egg = g(oval(33, 31, 16, 10, INK), "rotate(-38 33 31)")
    t = stroke("M34 22V35.5C34 38 35.5 39 38 38.5", HOLE, 3.2) + line(29.5, 27, 38.5, 27, HOLE, 3.2)
    dot = line(20, 17.5, 26.5, 34, RED, 2.2) + circle(19.5, 16.5, 3.2, RED)
    return egg + t + dot

@reg("textosaurus", DEEP_ORANGE_DEEP)
def textosaurus():
    plates = "".join(poly([(x - s * .55, yb), (x, yb - s), (x + s * .55, yb)], INK, 1.5)
                     for x, yb, s in [(20.5, 33, 5), (26, 29.5, 7), (32, 28, 8), (38, 29, 6.5), (43, 31.5, 4.5)])
    body = path("M13 41C18 37.5 20 30 31 29C39 28.5 42.5 31 45 33.5C47.5 33 50.5 34 51 36.5"
                "C51.5 39 48.5 39.8 45.5 39.5L43.5 40V45H39.5V41.5H28.5V45H24.5V40.5"
                "C20 40.5 16.5 41.5 13 41Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return plates + body + circle(46.5, 35.8, 1.4, HOLE)

@reg("the-binding-of-isaac-rebirth", PINK_DEEP)
def isaac():
    body = rrect(25, 36, 14, 11, 4.5, INK)
    head = circle(32, 26, 14, INK)
    eyes = circle(26.5, 26, 3.8, HOLE) + circle(37.5, 26, 3.8, HOLE)
    tears = line(25, 30.5, 25, 39, BLUE_LIGHT, 3) + line(39, 30.5, 39, 39, BLUE_LIGHT, 3)
    mouth = stroke("M29 34.5C31 33 33 33 35 34.5", HOLE, 2.2)
    return body + head + eyes + tears + mouth

@reg("the-cave", TEAL_LIGHT)
def the_cave():
    the = (stroke("M15.5 15H21M18.25 15V21", INK, 2.2) + stroke("M23.5 15V21M28 15V21M23.5 18H28", INK, 2.2) +
           stroke("M34.5 15H30.5V21H34.5M30.5 18H33.5", INK, 2.2))
    c = stroke("M21.5 28.5C20.5 26.5 19 26 17.5 26C15.5 26 14 28.5 14 33C14 37.5 15.5 40 17.5 40"
               "C19 40 20.5 39.5 21.5 37.5", INK, 3.4)
    a = stroke("M23.5 40L27.5 26L31.5 40M25 35H30", INK, 3.4)
    v = stroke("M33.5 26L37.5 40L41.5 26", INK, 3.4)
    e = stroke("M50 26H44.5V40H50M44.5 33H49", INK, 3.4)
    return the + c + a + v + e

@reg("the-elder-scrolls-v-skyrim", BLUE_GREY_DARK)
def skyrim():
    frame = stroke("M32 11.5L45 21V39L32 48.5L19 39V21Z", INK, 3)
    head = poly([(29.5, 19), (32, 15.5), (34.5, 19), (32, 23)], INK, 1.5)
    neck = rrect(30.5, 21, 3, 19, 1.5, INK)
    wing = "M31 25C27 22.5 24 23.5 23 28C25.5 27 27.5 27.5 28.5 29.5C26 30 24.5 32 25 35.5C27 33 29 32.5 31 33.5Z"
    wings = path(wing, INK) + g(path(wing, INK), "matrix(-1 0 0 1 64 0)")
    tail = stroke("M32 39.5C29 41.5 29.5 44.5 33 44.5", INK, 2.4)
    return frame + head + neck + wings + tail

@reg("the-escapists-2", BROWN)
def escapists():
    face = rrect(19, 23, 26, 22, 4, INK)
    band = rrect(18, 24, 28, 4.5, 1.8, RED)
    hair = poly([(16, 27), (17.5, 17), (24, 12.5), (34, 11.5), (44, 14.5), (49, 22), (46, 25),
                 (40, 21.5), (35, 24.5), (29, 21.5), (23, 25), (18.5, 25)], BROWN_DARK, 2)
    eyes = rrect(24.5, 31.5, 3.2, 5.5, 1, HOLE) + rrect(36.3, 31.5, 3.2, 5.5, 1, HOLE)
    return face + band + hair + eyes

@reg("the-long-dark", BLUE_GREY_DARK)
def the_long_dark():
    return poly([(21, 13), (43, 13), (43, 20), (36, 21.5), (35.5, 47), (29, 47), (29, 21.5),
                 (24, 22.5), (21, 25.5)], INK, 2.5)

def _plumbob(facet):
    left = poly([(32, 11), (21.5, 30), (32, 49)], INK, 2)
    right = poly([(32, 11), (42.5, 30), (32, 49)], facet, 2)
    return left + right

@reg("the-sims-3", TEAL_LIGHT)
def sims3():
    return _plumbob(AMBER)

@reg("the-sims-4", LIGHT_BLUE_DEEP)
def sims4():
    return _plumbob(LIGHT_BLUE_SOFT)

def _tf_s(rot):
    cross = g(line(CX, 12, CX, 48, HOLE, 5.5, "butt") + line(14, CY, 50, CY, HOLE, 5.5, "butt"),
              f"rotate({rot} 32 30)")
    return circle(CX, CY, 16.5, INK) + cross + circle(CX, CY, 6.5, HOLE)

@small("team-fortress-classic")
def tfc_s():
    return _tf_s(0)

@small("team-fortress2")
def tf2_s():
    return _tf_s(22)

@small("team-fortress2-classified")
def tf2_classified_s():
    return _tf_s(-24)

@small("tc")
def tc_s():
    back = rrect(12.5, 13, 24, 18, 5, INK) + poly([(17, 30), (16.5, 37), (24, 30)], INK, 2)
    front = rrect(28, 22, 24, 18, 5, INK, f' stroke="{HOLE}" stroke-width="3"')
    return back + front

@small("teams-for-linux")
def teams_s():
    people = circle(42, 17.5, 5.5, DEEP_PURPLE_SOFT) + rrect(32, 25, 19, 19, 7, DEEP_PURPLE_SOFT)
    plate = rrect(12, 19, 24, 24, 4, INK, f' stroke="{HOLE}" stroke-width="2"')
    return people + plate + stroke("M18 25.5H30M24 25.5V37", HOLE, 4)

@small("teamspeak3")
def teamspeak_s():
    band = stroke("M17 32A15 15 0 0 1 47 32", INK, 3.6)
    cups = rrect(12.5, 29, 8, 14, 3.5, INK) + rrect(43.5, 29, 8, 14, 3.5, INK)
    head = circle(32, 34, 11.5, INK)
    eyes = rrect(24.5, 31.5, 6, 4, 1.5, HOLE) + rrect(33.5, 31.5, 6, 4, 1.5, HOLE)
    return band + cups + head + eyes

@small("tabletop-simulator")
def tabletop_s():
    spade = path("M28 20C24 24 20.5 26 20.5 29.5C20.5 32.5 24 34 27 32L25 37H31L29 32"
                 "C32 34 35.5 32.5 35.5 29.5C35.5 26 32 24 28 20Z", HOLE)
    card = g(rrect(15, 12, 26, 34, 4, INK) + spade, "rotate(-8 28 29)")
    die = rrect(32, 30, 18, 18, 4.5, BLUE_LIGHT, f' stroke="{HOLE}" stroke-width="2.4"')
    return card + die + circle(36.5, 34.5, 2.2, INK) + circle(45.5, 43.5, 2.2, INK)

@small("tagainijisho")
def tagainijisho_s():
    bars = line(18, 15, 46, 15, INK, 4.4) + line(16, 45, 48, 45, INK, 4.4)
    return bars + stroke("M30 16L25.5 30H39.5L37 44", INK, 4.4)

@small("tauonmb")
def tauonmb_s():
    arcs = stroke("M20.2 37.5A13 13 0 0 1 19.4 25", PURPLE_SOFT, 6) + \
        stroke("M43.8 22.5A13 13 0 0 1 44.6 35", PURPLE_SOFT, 6)
    return circle(CX, CY, 17, INK) + arcs + circle(CX, CY, 5.5, HOLE)

def _tex_s(colour):
    return (stroke("M14.5 18H29.5M22 18V40", colour, 4.4) +
            stroke("M48 24.5H36V44H48M36 34H46", colour, 4.4))

@small("texmaker")
def texmaker_s():
    return _tex_s(INK)

@small("texstudio")
def texstudio_s():
    return _tex_s(YELLOW_LIGHT)

@small("the-cave")
def the_cave_s():
    return stroke("M43 20C40.5 16.5 37.5 15 33.5 15C25 15 19.5 21.5 19.5 30C19.5 38.5 25 45 33.5 45"
                  "C37.5 45 40.5 43.5 43 40", INK, 5)

@small("the-elder-scrolls-v-skyrim")
def skyrim_s():
    frame = stroke("M32 11L45.5 20.5V39.5L32 49L18.5 39.5V20.5Z", INK, 3)
    body = poly([(32, 16.5), (35, 21), (33.5, 23), (33.5, 42), (30.5, 42), (30.5, 23), (29, 21)], INK, 1.5)
    wings = poly([(31, 25), (23.5, 25), (28, 34), (31, 32)], INK, 1.5) + \
        poly([(33, 25), (40.5, 25), (36, 34), (33, 32)], INK, 1.5)
    return frame + body + wings

@small("textadept")
def textadept_s():
    egg = g(oval(33, 31, 17, 11, INK), "rotate(-38 33 31)")
    t = stroke("M34.5 21V35.5C34.5 38 36 39 38.5 38.5", HOLE, 3.6) + line(29, 26.5, 39.5, 26.5, HOLE, 3.6)
    return egg + t + circle(18.5, 15.5, 3.8, RED)

@small("tdeprintfax")
def tdeprintfax_s():
    body = rrect(13, 12, 38, 25, 4, INK)
    screen = rrect(18, 17, 16, 8, 2, BLUE_LIGHT)
    paper = rrect(19, 33, 26, 15, 2, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    return body + screen + rrect(18, 29.5, 28, 3, 1.5, HOLE) + paper + rrect(23, 39.5, 18, 3.2, 1.6, HOLE)

@small("tdewalletmanager")
def tdewallet_s():
    return rrect(13, 13, 34, 34, 5, INK) + rrect(37, 24, 15, 12, 4, RED_DARK) + circle(44, 30, 2.5, INK)

@small("terminator")
def terminator_s():
    box = rrect(14, 13, 36, 34, 4.5, INK)
    return box + line(32, 13, 32, 47, HOLE, 3, "butt") + line(14, 30, 50, 30, HOLE, 3, "butt") + \
        rrect(18, 18, 10, 3, 1.5, HOLE) + rrect(36, 35, 10, 3, 1.5, HOLE)

@small("technic-launcher")
def technic_s():
    rim = ring_b(CX, CY, 15.5, INK, 3.6)
    jaw = stroke("M26.5 17V21C26.5 23.5 29 25 32 25C35 25 37.5 23.5 37.5 21V17", INK, 4)
    return rim + jaw + rrect(29, 24, 6, 20, 3, INK)

@small("terratech")
def terratech_s():
    sq = rrect(17.5, 15.5, 29, 29, 5.5, INK)
    x = stroke("M26 24L38 36M38 24L26 36", HOLE, 5)
    tips = (poly([(28.5, 13), (35.5, 13), (32, 9.5)], INK, 1.5) +
            poly([(28.5, 47), (35.5, 47), (32, 50.5)], INK, 1.5))
    return sq + x + tips

@small("termius-app")
def termius_s():
    cloud = (circle(24, 33, 9, INK) + circle(34, 24.5, 11.5, INK) + circle(42, 34, 8, INK) +
             rrect(15, 32, 35, 13, 6.5, INK))
    return cloud + stroke("M27 27L32.5 32L27 37", HOLE, 3.2)

@small("tetzle")
def tetzle_s():
    out = "".join(rrect(17 + c * 15, 17 + r * 15, 12.5, 12.5, 3, INK if r == 0 else LIGHT_BLUE_SOFT)
                  for r in range(2) for c in range(2) if (r, c) != (0, 1))
    return out + g(rrect(33, 12, 12.5, 12.5, 3, INK), "rotate(12 39.25 18.25)")

@small("textosaurus")
def textosaurus_s():
    plates = "".join(poly([(x - s * .6, yb), (x, yb - s), (x + s * .6, yb)], INK, 1.5)
                     for x, yb, s in [(23, 31.5, 7), (31, 28.5, 9), (39, 29.5, 7)])
    body = path("M13 41C18 37.5 20 30 31 29C39 28.5 42.5 31 45 33.5C47.5 33 50.5 34 51 36.5"
                "C51.5 39 48.5 39.8 45.5 39.5L43.5 40V45H39V41.5H29V45H24.5V40.5"
                "C20 40.5 16.5 41.5 13 41Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return plates + body

@small("tenacity")
def tenacity_s():
    return rrect(13, 11, 38, 38, 6, INK) + rrect(27, 16, 10, 28, 1, HOLE) + rrect(18, 25, 28, 10, 1, HOLE)

@small("teeworlds")
def teeworlds_s():
    body = circle(32, 27.5, 15, INK)
    feet = rrect(15, 39.5, 15, 8, 4, ORANGE_DARK) + rrect(34, 39.5, 15, 8, 4, ORANGE_DARK)
    return body + feet + oval(27.5, 25, 3, 5, BROWN_DARK) + oval(37, 25, 3, 5, BROWN_DARK)

@small("tegaki-recognize")
def tegaki_s():
    return (line(16, 21, 48, 21, INK, 3.6) + line(32, 12, 32, 48, INK, 3.6) +
            stroke("M30 22.5C27 30 23 35.5 16.5 40", INK, 3.6) +
            stroke("M34 22.5C37 30 41 35.5 47.5 40", INK, 3.6))

@small("terraria")
def terraria_s():
    crown = "".join(circle(x, y, r, INK) for x, y, r in [(26, 22, 8.5), (38, 21, 8.5), (32, 27, 9)])
    return poly([(28.5, 32), (35.5, 32), (37, 48), (27, 48)], BROWN_SOFT, 1.5) + crown

@small("the-binding-of-isaac-rebirth")
def isaac_s():
    head = circle(32, 27, 16, INK)
    eyes = circle(25.5, 27, 4.8, HOLE) + circle(38.5, 27, 4.8, HOLE)
    tears = line(23.5, 32, 23.5, 42, BLUE_LIGHT, 3.4) + line(40.5, 32, 40.5, 42, BLUE_LIGHT, 3.4)
    return head + eyes + tears

@small("the-escapists-2")
def escapists_s():
    face = rrect(18, 23, 28, 23, 4, INK)
    hair = poly([(15, 28), (17, 16), (25, 11.5), (36, 11), (45, 14), (49.5, 22), (46, 26), (18, 26)],
                BROWN_DARK, 2)
    band = rrect(17, 25, 30, 5, 2, RED)
    eyes = rrect(24, 33, 4, 6, 1.2, HOLE) + rrect(36, 33, 4, 6, 1.2, HOLE)
    return face + hair + band + eyes

@small("taisei")
def taisei_s():
    swoosh = stroke("M43 14C31 11 19.5 17 19.5 27C19.5 37 28 44.5 45 44.5", TEAL_SOFT, 3)
    return swoosh + stroke("M34 15V36.5C34 40.5 36 42 40 41.5", INK, 4.6) + line(27.5, 24, 41, 24, INK, 4.4)
