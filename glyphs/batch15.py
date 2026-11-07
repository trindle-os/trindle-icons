# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 15: com.github.bartzaalberg.php-tester to com.github.huluti.Coulr.

Same rules as batch01: tile from the palette step nearest the brand
colour, mark in INK, HOLE for cut-throughs, any second shade another
palette step.
"""
from lm import *
from glyphs.kit import badge_c, gear_b, registry, ring_b

ICONS, SMALL, reg, small = registry()

def sheet(x0, y0, x1, y1, fold=6):
    return path(f"M{x0 + 3} {y0}H{x1 - fold}L{x1} {y0 + fold}V{y1 - 3}A3 3 0 0 1 {x1 - 3} {y1}"
                f"H{x0 + 3}A3 3 0 0 1 {x0} {y1 - 3}V{y0 + 3}A3 3 0 0 1 {x0 + 3} {y0}Z", INK)

@reg("com.github.bartzaalberg.php-tester", INDIGO_DEEP)
def php_tester():
    w = 3.4
    p1 = line(16.5, 25.5, 16.5, 40, INK, w) + ring_b(21, 29.5, 4.3, INK, w)
    h = (line(29, 19, 29, 34, INK, w) +
         stroke("M29 29.5C29 27 30.8 25.3 33.2 25.3C35.6 25.3 37.4 27 37.4 29.5V34", INK, w))
    p2 = line(42, 25.5, 42, 40, INK, w) + ring_b(46.5, 29.5, 4.3, INK, w)
    return g(p1 + h + p2, "translate(32 30) scale(.92) translate(-32.6 -29.5)")

@reg("com.github.bartzaalberg.snaptastic", DEEP_ORANGE_DEEP)
def snaptastic():
    def cube(cx, cy, s, top, left, right):
        h = s * .58
        t = [(cx, cy - 2 * h), (cx + s, cy - h), (cx, cy), (cx - s, cy - h)]
        l = [(cx - s, cy - h), (cx, cy), (cx, cy + 2 * h), (cx - s, cy + h)]
        r = [(cx + s, cy - h), (cx, cy), (cx, cy + 2 * h), (cx + s, cy + h)]
        return poly(t, top, 1.6) + poly(l, left, 1.6) + poly(r, right, 1.6)
    big = cube(29, 33, 13.5, INK, INK, DEEP_ORANGE_SOFT)
    seam = stroke("M15.5 25.2L29 33L42.5 25.2", HOLE, 1.6)
    small_ = poly([(42, 10), (50.5, 14.9), (50.5, 24.7), (42, 29.6), (33.5, 24.7), (33.5, 14.9)], HOLE, 3)
    small_ += cube(42, 20, 7, DEEP_ORANGE_SOFT, INK, DEEP_ORANGE_SOFT)
    return big + seam + small_

@reg("com.github.basjam.valacompiler", GREY_DEEP)
def valacompiler():
    w = 4.6
    return (stroke("M16 17L21.5 23L27 17", INK, w) + stroke("M37 23L42.5 17L48 23", INK, w) +
            stroke("M16 35V43H26", INK, w) + stroke("M37 43L42.5 37L48 43", INK, w))

@reg("com.github.bcedu.museic", BLUE_GREY_DEEP)
def museic():
    stems = stroke("M26 42V19L46 14V37", INK, 4)
    beam = path("M24 17.5L48 11.5V18L24 24Z", INK)
    heads = (g(path("M21.5 38a6 4.6 0 1 0 .01 0Z", INK), "rotate(-18 21.5 42.6)") +
             g(path("M41.5 33a6 4.6 0 1 0 .01 0Z", INK), "rotate(-18 41.5 37.6)"))
    return stems + beam + heads

@reg("com.github.bcedu.shutdownscheduler", GREY_DARK)
def shutdownscheduler():
    power = stroke("M23 19.5A13 13 0 1 0 35 19.5", INK, 4.2) + line(29, 14, 29, 27, INK, 4.2)
    clock = circle(41.5, 39.5, 10.5, HOLE) + circle(41.5, 39.5, 8.8, RED)
    hands = stroke("M41.5 34V39.5H46", INK, 2.6)
    return power + clock + hands

@reg("com.github.bcedu.valasimplehttpserver", DEEP_PURPLE)
def valasimplehttpserver():
    cloud = path("M21 44C16 44 13 40.5 13 36.5C13 32.5 16 29.5 20 29.3C21 23.5 26 19.5 32 19.5"
                 "C38 19.5 43 23.5 44 29.3C48 29.5 51 32.5 51 36.5C51 40.5 48 44 43 44Z", INK)
    up = poly([(26, 13), (33, 21.5), (29, 21.5), (29, 38), (23, 38), (23, 21.5), (19, 21.5)], PURPLE_LIGHT, 2)
    down = poly([(38, 47), (45, 38.5), (41, 38.5), (41, 22), (35, 22), (35, 38.5), (31, 38.5)], BLUE_DEEP, 2)
    return cloud + up + down

@reg("com.github.birros.WebArchives", BLUE_DEEP)
def webarchives():
    doc = sheet(17, 12, 47, 48, 8)
    globe = (ring_b(32, 31, 9.5, HOLE, 2.6) + line(22.5, 31, 41.5, 31, HOLE, 2.4) +
             f'<ellipse cx="32" cy="31" rx="4.2" ry="9.5" fill="none" stroke="{HOLE}" stroke-width="2.4"/>' +
             stroke("M24 25.5H40M24 36.5H40", HOLE, 2.2))
    return doc + globe

@reg("com.github.bleakgrey.tootle", BLUE_GREY)
def tootle():
    tube = rrect(14, 29, 24, 4.4, 2.2, INK) + rrect(19, 36, 20, 4, 2, INK)
    loop = stroke("M19 38C15 38 15 31 19 31", INK, 3)
    bell = path("M36 29.5L48 20.5C49.5 26 49.5 36 48 41.5L36 34Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    valves = "".join(rrect(x, 22, 3.6, 17, 1.6, INK) + rrect(x - 1, 20, 5.6, 3, 1.5, INK)
                     for x in (23, 28, 33))
    mouth = rrect(12, 28, 3.5, 6.4, 1.5, INK)
    return g(tube + loop + bell + valves + mouth, "translate(0 1)")

@reg("com.github.bleakgrey.transporter", PURPLE_DEEP)
def transporter():
    arcs = (stroke("M17.5 27A15 15 0 0 1 40 17", INK, 4) +
            poly([(38, 12.5), (45, 18.5), (37, 21.5)], INK, 1.5) +
            stroke("M46.5 33A15 15 0 0 1 24 43", INK, 4) +
            poly([(26, 47.5), (19, 41.5), (27, 38.5)], INK, 1.5))
    world = circle(32, 30, 9.5, INK)
    land = path("M29 22C33 22 35 24 33.5 26.5C32 29 36 30 36.5 33C37 36 34 38 31 38"
                "C33 35.5 32 33.5 29.5 33C27 32.5 26.5 29.5 28.5 27.5C30 26 28 24 29 22Z", PURPLE_LIGHT)
    return arcs + world + land

@reg("com.github.bluesabre.darkbar", BLUE_GREY_DARK)
def darkbar():
    win = rrect(14, 14, 36, 32, 5, INK)
    bar = rrect(14, 21, 36, 2.4, 0, HOLE)
    x = stroke("M18.5 16.2L21.5 19.2M21.5 16.2L18.5 19.2", HOLE, 1.8)
    tog = rrect(21, 29, 22, 11, 5.5, BLUE) + circle(37.5, 34.5, 4, HOLE)
    return win + bar + x + tog

@reg("com.github.calo001.fondo", BLUE_GREY_DARK)
def fondo():
    frame = rrect(16, 14, 32, 32, 8, INK)
    lens = circle(32, 30, 9, HOLE) + circle(32, 30, 6, INK)
    half = path("M36.2 25.8A6 6 0 0 1 27.8 34.2Z", BLUE_LIGHT) + path("M27.8 34.2A6 6 0 0 1 36.2 25.8Z", LIGHT_BLUE_LIGHT)
    return frame + lens + half + circle(32, 30, 2.5, HOLE)

@reg("com.github.candiedoperation.ordne", DEEP_PURPLE_LIGHT)
def ordne():
    return stroke("M18 14H46M18 46H46M22 14L32 30L22 46M42 14L32 30L42 46", INK, 3.6)

@reg("com.github.cassidyjames.clairvoyant", GREY_DARK)
def clairvoyant():
    ball = circle(CX, CY, 16.5, INK) + circle(CX, CY, 10.5, HOLE)
    eight = ring_b(32, 25.8, 3.2, INK, 2.8) + ring_b(32, 34, 4, INK, 2.8)
    return ball + eight

@reg("com.github.cassidyjames.dippi", RED_DEEP)
def dippi():
    screen = rrect(13, 14, 38, 26, 3, INK)
    tri = path("M20 37L47 17V37Z", HOLE)
    inner = path("M37 32.5L43 28V32.5Z", INK)
    stand = rrect(26, 43, 12, 4, 1.5, INK) + rrect(29.5, 39, 5, 5, 0, INK)
    return screen + tri + inner + stand

@reg("com.github.cassidyjames.ephemeral", DEEP_PURPLE_LIGHT)
def ephemeral():
    dial = ring_b(CX, CY, 15.5, INK, 3)
    red = poly([(44.5, 17.5), (35, 31.5), (30.5, 27)], RED, 1.5)
    white = poly([(19.5, 42.5), (30.5, 27), (35, 31.5)], INK, 1.5)
    return dial + white + red

@reg("com.github.cassidyjames.ideogram", AMBER_DEEP)
def ideogram():
    face = circle(CX, 29, 16, INK)
    eyes = f'<ellipse cx="26" cy="23.5" rx="2.4" ry="3.2" fill="{HOLE}"/><ellipse cx="38" cy="23.5" rx="2.4" ry="3.2" fill="{HOLE}"/>'
    mouth = path("M21 30H43C43 37 38 41.5 32 41.5C26 41.5 21 37 21 30Z", HOLE)
    return face + eyes + mouth

@reg("com.github.cassidyjames.palette", AMBER_DARK)
def palette():
    out = ""
    for ang, c in [(90, AMBER_DEEP), (60, AMBER_DEEP), (30, AMBER), (0, INK)]:
        out += g(rrect(13, 12, 12, 38, 6, c, f' stroke="{HOLE}" stroke-width="2.2"'), f"rotate({ang} 19 44)")
    return g(out + circle(19, 44, 2.8, HOLE), "translate(1 -1)")

@reg("com.github.cassidyjames.principles", GREY_DARK)
def principles():
    one = stroke("M17.5 19.5L22.5 15.5V44.5", INK, 6)
    zero = f'<ellipse cx="38.5" cy="30" rx="8.5" ry="12.5" fill="none" stroke="{INK}" stroke-width="5.5"/>'
    return one + zero

@reg("com.github.chasinglogic.tardis", BLUE_DEEP)
def tardis():
    shield = path("M17 15.5L32 11.5L47 15.5V29C47 38 40.5 44.5 32 48C23.5 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    lens = circle(33, 28, 8.5, HOLE) + circle(33, 28, 5, INK)
    tail = poly([(25, 30), (29, 34), (24.5, 37)], HOLE, 1.5)
    return shield + lens + tail

@reg("com.github.childishgiant.mixer", BLUE_GREY)
def mixer():
    out = ""
    for x, y in [(22, 23), (32, 36), (42, 28)]:
        out += line(x, 14, x, 46, INK, 2.6) + rrect(x - 4.5, y - 4, 9, 8, 2.2, INK)
    return out

@reg("com.github.cjfloss.envelope", AMBER_DARK)
def envelope():
    s = stroke("M40 21.5C38.5 19.5 35.5 18.5 32 18.5C27 18.5 24 21 24 24.5"
               "C24 31.5 40.5 28.5 40.5 36C40.5 39.5 37 41.5 32 41.5"
               "C28 41.5 25 40.5 23.5 38", INK, 4.4)
    bar = line(32, 13, 32, 47, INK, 4)
    return s + bar

@reg("com.github.coralynnmay.goodvibesapp", LIGHT_BLUE_DEEP)
def goodvibesapp():
    gg = stroke("M31 20.5C29.5 18.5 27.5 17.5 25 17.5C19 17.5 15.5 23.5 15.5 30"
                "C15.5 37.5 19 42 24.5 42C27 42 29 41 30 39.5L31.5 31H25", INK, 4)
    v = stroke("M34 18L39 42L49 18", INK, 4)
    return g(gg + v, "translate(32 30) skewX(-8) translate(-32 -30)")

@reg("com.github.coslyk.MoonPlayer", INDIGO)
def moonplayer():
    moon = circle(CX, CY, 16, INK)
    craters = (circle(25, 25.5, 4.2, INDIGO_SOFT) + circle(37, 35.5, 3.4, INDIGO_SOFT) +
               circle(38.5, 22.5, 2.2, INDIGO_SOFT) + circle(28.5, 37.5, 1.8, INDIGO_SOFT) +
               circle(44, 30, 1.6, INDIGO_SOFT))
    return moon + craters

@reg("com.github.cryptowyrm.copypastegrab", RED)
def copypastegrab():
    film = rrect(13, 16, 38, 28, 3, INK)
    holes = "".join(rrect(x, y, 3.4, 3, 1, HOLE) for x in (15.5, 45) for y in (19, 25, 31, 37))
    play = poly([(28, 23), (38.5, 30), (28, 37)], HOLE, 2.5)
    return film + holes + play

@reg("com.github.dahenson.agenda", BLUE_DEEP)
def agenda():
    return stroke("M17 20H47M17 30H47M17 40H33", INK, 6)

@reg("com.github.dail8859.NotepadNext", BROWN_LIGHT)
def notepadnext():
    doc = sheet(15, 11, 43, 46, 8)
    lines = "".join(rrect(19.5, y, w, 2.6, 1.3, HOLE) for y, w in [(20, 12), (25.5, 18), (31, 18), (36.5, 10)])
    plus = badge_c(41.5, 40, 9) + stroke("M41.5 35.5V44.5M37 40H46", HOLE, 3)
    return doc + lines + plus

@reg("com.github.danrabbit.harvey", CYAN_DEEP)
def harvey():
    book = rrect(15, 14, 34, 32, 4, INK) + line(22, 14.5, 22, 45.5, HOLE, 2.2)
    check = circle(36, 30, 8.5, HOLE) + circle(36, 30, 3.2, INK)
    return book + check

@reg("com.github.danrabbit.lookbook", DEEP_PURPLE_LIGHT)
def lookbook():
    book = rrect(17, 12, 30, 36, 4, INK) + line(23, 12.5, 23, 47.5, HOLE, 2.2)
    glass = ring_b(34, 27.5, 5.8, HOLE, 3.4) + line(38.5, 32, 43, 36.5, HOLE, 3.6)
    return book + glass

@reg("com.github.danrabbit.nimbus", LIGHT_BLUE)
def nimbus():
    return path("M21 41C16.5 41 13.5 37.5 13.5 33.5C13.5 29.5 16.5 26.5 20.5 26.3"
                "C21.5 20.5 26.5 17 32 17C38 17 42.5 21 43.5 26.3C47.5 26.5 50.5 29.5 50.5 33.5"
                "C50.5 37.5 47.5 41 43 41Z", INK)

@reg("com.github.davidmhewitt.clipped", ORANGE_DEEP)
def clipped():
    board = rrect(16, 14, 32, 34, 4, INK)
    paper = rrect(20, 18.5, 24, 26, 1.5, HOLE)
    lines = "".join(rrect(23, y, 18, 2.4, 1.2, INK) for y in (24, 29, 34, 39))
    clip = rrect(25, 11, 14, 7, 3, INK)
    return board + paper + lines + clip

@reg("com.github.davidmhewitt.torrential", BLUE)
def torrential():
    shaft = rrect(28, 12, 8, 22, 1.5, INK) + circle(28, 21, 3, INK) + circle(36, 25, 3, INK)
    head = poly([(17, 31), (47, 31), (32, 47)], INK, 3)
    return shaft + head

@reg("com.github.dbhowell.peeq", TEAL_DEEP)
def peeq():
    back = poly([(13, 46), (23, 29), (31, 46)], TEAL_SOFT, 2)
    front = poly([(21, 46), (36, 22), (51, 46)], INK, 2)
    cap = poly([(32.2, 28), (36, 22), (39.8, 28), (37.8, 26.5), (36, 29), (34.2, 26.5)], TEAL_SOFT, 1)
    flag = line(36, 23, 36, 12.5, INK, 2) + poly([(36.5, 12), (44, 12), (42, 14.8), (44, 17.5), (36.5, 17.5)], RED_LIGHT, 1)
    return back + front + cap + flag

@reg("com.github.diegoivanme.plano", BLUE_GREY)
def plano():
    body = rrect(18, 12, 28, 36, 4.5, INK)
    screen = rrect(21.5, 15.5, 21, 8, 2, HOLE)
    keys = "".join(rrect(21.5 + c * 6, 27 + r * 5.5, 4.5, 3.8, 1.2, HOLE) for r in range(3) for c in range(2))
    tall = rrect(34, 27, 8.5, 15, 1.5, RED)
    return body + screen + keys + tall

@reg("com.github.djaler.formatter", GREY_DARK)
def formatter():
    plug = rrect(21, 12, 22, 12, 2, INK) + rrect(25, 16, 4, 3.5, .5, HOLE) + rrect(35, 16, 4, 3.5, .5, HOLE)
    body = rrect(16, 24, 32, 23, 3, INK)
    slots = rrect(20, 29, 12, 2.4, 1.2, HOLE) + rrect(20, 34, 8, 2.4, 1.2, HOLE)
    badge_ = circle(42, 40, 10.5, HOLE) + circle(42, 40, 8.5, BLUE)
    arrow = stroke("M46.5 38.5A4.8 4.8 0 1 1 42 35.2", INK, 2.4) + poly([(41, 32.5), (44.8, 35.2), (41, 37.8)], INK, 1)
    return plug + body + slots + badge_ + arrow

@reg("com.github.donadigo.appeditor", BLUE_GREY_DEEP)
def appeditor():
    cog = gear_b(29.5, 27.5, 16, 12, INK) + circle(29.5, 27.5, 6, HOLE)
    pen = circle(41.5, 40, 10, HOLE) + circle(41.5, 40, 8, TEAL)
    pencil = g(rrect(39.8, 33.5, 3.4, 10, 1, INK) + poly([(39.8, 44.2), (43.2, 44.2), (41.5, 47)], INK, .8),
               "rotate(45 41.5 40)")
    return cog + pen + pencil

@reg("com.github.donadigo.eddy", PINK_DEEP)
def eddy():
    swirl = stroke("M40 22C37 17 30 16 25 19C19.5 22.5 18.5 30.5 22 36C25.5 41 32.5 41.5 36 38"
                   "C39 35 38.5 30 35 28.5C32 27 29 28.5 28.5 31", INK, 4.2)
    badge_ = circle(42.5, 19.5, 8.6, HOLE) + circle(42.5, 19.5, 7, INK) + \
        stroke("M42.5 15.5V23M39 19.8L42.5 23.3L46 19.8", HOLE, 2.4)
    return g(swirl, "translate(-2 3)") + badge_

@reg("com.github.efdos.mupengui", BLUE_DEEP)
def mupengui():
    pad = (rrect(13, 16, 38, 14, 6, INK) + rrect(13, 20, 10, 24, 5, INK) +
           rrect(27, 20, 10, 27, 5, INK) + rrect(41, 20, 10, 24, 5, INK))
    dpad = stroke("M18 23.5H24M21 20.5V26.5", HOLE, 2.4)
    btns = circle(42, 21.5, 1.6, HOLE) + circle(46, 21.5, 1.6, HOLE) + circle(44, 25, 1.6, HOLE) + circle(44, 18.2, 1.6, HOLE)
    stick = circle(32, 30.5, 3.6, HOLE) + circle(32, 30.5, 1.6, INK)
    return pad + dpad + btns + stick

@reg("com.github.elfenware.badger", BLUE_GREY_DEEP)
def badger():
    ears = circle(19.5, 18.5, 5.5, INK) + circle(44.5, 18.5, 5.5, INK)
    head = path("M32 15C42 15 48.5 22 48.5 30.5C48.5 39 41 46.5 32 46.5C23 46.5 15.5 39 15.5 30.5"
                "C15.5 22 22 15 32 15Z", INK)
    patches = (g(f'<ellipse cx="25" cy="31" rx="4.4" ry="6.2" fill="{HOLE}"/>', "rotate(35 25 31)") +
               g(f'<ellipse cx="39" cy="31" rx="4.4" ry="6.2" fill="{HOLE}"/>', "rotate(-35 39 31)"))
    eyes = circle(25.5, 30, 1.8, INK) + circle(38.5, 30, 1.8, INK)
    nose = f'<ellipse cx="32" cy="39" rx="3.2" ry="2.3" fill="{HOLE}"/>'
    return ears + head + patches + eyes + nose

@reg("com.github.elfenware.obliviate", GREY_DEEP)
def obliviate():
    disc_ = circle(CX, CY, 16.5, INK)
    dots = circle(23, 30, 3.6, HOLE) + circle(32, 30, 3.6, HOLE) + circle(41, 30, 3.6, GREY_SOFT)
    wand = line(19, 45, 46.5, 15, BROWN_DEEP, 2.6)
    return disc_ + dots + wand

@reg("com.github.eudaldgr.elements", BLUE)
def elements():
    h = stroke("M18 18V44M36 18V44M18 31H36", INK, 5)
    sup = stroke("M43 16.5L46 14V27", INK, 2.8)
    return h + sup

@reg("com.github.fabiocolacio.marker", AMBER_DARK)
def marker():
    doc = rrect(14, 12, 28, 34, 3, INK)
    lines = "".join(rrect(18, y, w, 2.6, 1.3, HOLE) for y, w in [(17, 15), (22.5, 20), (28, 12), (33.5, 17)])
    pen = g(rrect(28, 18, 9, 22, 2.5, AMBER, f' stroke="{HOLE}" stroke-width="2"') +
            poly([(28.5, 40), (36.5, 40), (34, 45), (31, 45)], AMBER, 1),
            "rotate(-45 32.5 34)")
    return doc + lines + g(pen, "translate(8 6)")

@reg("com.github.finefindus.eyedropper", BLUE_DEEP)
def eyedropper():
    bulb = rrect(38, 11, 10, 14, 5, INK)
    collar = rrect(33, 22, 20, 5, 2.5, INK)
    tube = rrect(39.5, 27, 7, 21, 2, INK) + rrect(41.5, 30, 3, 12, 1.5, HOLE)
    tip = line(43, 47, 43, 52, INK, 2.4)
    return g(bulb + collar + tube + tip, "rotate(45 43 30) translate(-11 1)")

@reg("com.github.gabutakut.gabutdm", DEEP_PURPLE_DEEP)
def gabutdm():
    a1 = stroke("M18 34A14.5 14.5 0 0 1 40 18", INK, 5) + poly([(38, 12.5), (46, 19), (37.5, 23)], INK, 1.5)
    a2 = stroke("M46 26A14.5 14.5 0 0 1 24 42", DEEP_ORANGE_LIGHT, 5) + poly([(26, 47.5), (18, 41), (26.5, 37)], DEEP_ORANGE_LIGHT, 1.5)
    hub = ring_b(32, 30, 5, AMBER, 3)
    return a1 + a2 + hub

@reg("com.github.gi_lom.dialect", ORANGE_DARK)
def dialect():
    back = g(rrect(31, 22, 19, 22, 3.5, ORANGE_LIGHT), "rotate(8 40 33)")
    back += stroke("M36.5 30.5H45.5M41 27.5C41 33 39 37 36.5 39", ORANGE_DARK, 2.2)
    card = poly([(15, 14), (30, 14), (35, 40), (28, 46), (20, 40)], INK, 3)
    d = stroke("M19.5 20.5V32H22.5C26 32 28 29.7 28 26.2C28 22.7 26 20.5 22.5 20.5Z", HOLE, 2.8)
    return back + card + d

@reg("com.github.gijsgoudzwaard.image-optimizer", RED_LIGHT)
def image_optimizer():
    frame = rrect(13, 14, 34, 28, 4, INK)
    scene = path("M16.5 38.5L25 29.5L31 35L35 31.5L43.5 38.5Z", HOLE) + circle(38, 22.5, 3.5, HOLE)
    cog = circle(42.5, 40, 10.5, HOLE) + gear_b(42.5, 40, 8, 6, INK) + circle(42.5, 40, 2.8, HOLE)
    return frame + scene + cog

@reg("com.github.hannesschulze.optimizer", BLUE_GREY_DEEP)
def optimizer():
    dial = path("M13.5 42A18.5 18.5 0 0 1 50.5 42Z", INK)
    ticks = "".join(line(*pt(32, 42, 14.5, a), *pt(32, 42, 11, a), HOLE, 2.4) for a in (-165, -130, -90, -50, -15))
    needle = poly([(30.5, 43.5), (41, 32), (33.5, 45)], RED_LIGHT, 1.5) + circle(32, 43, 3.2, RED_LIGHT)
    return g(dial + ticks + needle, "translate(0 -2)")

@reg("com.github.harisvsulaiman.pushy", BLUE_DEEP)
def pushy():
    base = path("M14 30V37C14 42 22 46 32 46C42 46 50 42 50 37V30Z", INK)
    top = f'<ellipse cx="32" cy="30" rx="18" ry="8" fill="{INK}"/>'
    rim = f'<ellipse cx="32" cy="30" rx="18" ry="8" fill="none" stroke="{HOLE}" stroke-width="1.8"/>'
    btn = (path("M22 22V28C22 31 26.5 33 32 33C37.5 33 42 31 42 28V22Z", BLUE_SOFT) +
           f'<ellipse cx="32" cy="22" rx="10" ry="4.5" fill="#6FBAF6"/>')
    return g(base + top + rim + btn, "translate(0 1)")

@reg("com.github.hezral.inspektor", CYAN_DEEP)
def inspektor():
    frame = rrect(14, 12, 36, 36, 6, INK) + rrect(18.5, 16.5, 27, 27, 3, HOLE)
    pat = ["X.X.X", ".X.XX", "XX.X.", ".XX.X", "X.XX."]
    cells = "".join(rrect(20.5 + c * 4.6, 18.5 + r * 4.6, 4.6, 4.6, 0, INK)
                    for r, row in enumerate(pat) for c, ch in enumerate(row) if ch == "X")
    return frame + cells

@reg("com.github.hugolabe.Wike", BLUE_GREY_DEEP)
def wike():
    w = stroke("M17 19L24.5 42L32 24L39.5 42L47 19", INK, 3.4)
    serifs = stroke("M13.5 18.5H21M28.5 22H35.5M43 18.5H50.5", INK, 2.4)
    return w + serifs

@reg("com.github.huluti.Coulr", DEEP_PURPLE_LIGHT)
def coulr():
    return stroke("M42.5 19C40.5 16 37 14.5 33 14.5C25.5 14.5 21 21 21 30C21 39 25.5 45.5 33 45.5"
                  "C37 45.5 40.5 44 42.5 41", INK, 7)

@small("com.github.birros.WebArchives")
def webarchives_s():
    return sheet(17, 12, 47, 48, 8) + ring_b(32, 31, 9, HOLE, 3.2) + line(23, 31, 41, 31, HOLE, 3)

@small("com.github.dail8859.NotepadNext")
def notepadnext_s():
    doc = sheet(15, 11, 43, 46, 8)
    lines = "".join(rrect(19, y, w, 4, 2, HOLE) for y, w in [(20, 14), (28, 18)])
    return doc + lines + badge_c(41.5, 40, 9.5) + stroke("M41.5 35V45M36.5 40H46.5", HOLE, 3.6)

@small("com.github.hezral.inspektor")
def inspektor_s():
    frame = rrect(14, 12, 36, 36, 6, INK) + rrect(19, 17, 26, 26, 3, HOLE)
    cells = "".join(rrect(21.5 + c * 7, 19.5 + r * 7, 7, 7, 0, INK)
                    for r, row in enumerate(["X.X", ".XX", "X.X"]) for c, ch in enumerate(row) if ch == "X")
    return frame + cells

@small("com.github.fabiocolacio.marker")
def marker_s():
    doc = rrect(14, 12, 28, 34, 3, INK)
    lines = "".join(rrect(18, y, w, 4, 2, HOLE) for y, w in [(17, 16), (25, 12)])
    pen = g(rrect(28, 18, 10, 22, 3, LIGHT_BLUE_SOFT, f' stroke="{HOLE}" stroke-width="2.4"'), "rotate(-45 32.5 34)")
    return doc + lines + g(pen, "translate(8 6)")

@small("com.github.efdos.mupengui")
def mupengui_s():
    pad = (rrect(13, 16, 38, 14, 6, INK) + rrect(13, 20, 10, 24, 5, INK) +
           rrect(27, 20, 10, 27, 5, INK) + rrect(41, 20, 10, 24, 5, INK))
    return pad + stroke("M17.5 23.5H24.5M21 20V27", HOLE, 3) + circle(44, 23, 2.6, HOLE)

@small("com.github.bartzaalberg.php-tester")
def php_tester_s():
    w = 2.8
    p1 = line(16.5, 25.5, 16.5, 40, INK, w) + ring_b(21, 29.5, 4.3, INK, w)
    h = (line(29, 19, 29, 34, INK, w) +
         stroke("M29 29.5C29 27 30.8 25.3 33.2 25.3C35.6 25.3 37.4 27 37.4 29.5V34", INK, w))
    p2 = line(42, 25.5, 42, 40, INK, w) + ring_b(46.5, 29.5, 4.3, INK, w)
    return g(p1 + h + p2, "translate(32 30) scale(.92) translate(-32.6 -29.5)")

@small("com.github.basjam.valacompiler")
def valacompiler_s():
    w = 3.6
    return (stroke("M16 17L21.5 23L27 17", INK, w) + stroke("M37 23L42.5 17L48 23", INK, w) +
            stroke("M16 35V43H26", INK, w) + stroke("M37 43L42.5 37L48 43", INK, w))

@small("com.github.bleakgrey.tootle")
def tootle_s():
    tube = rrect(13, 29, 26, 5, 2.5, INK)
    bell = path("M36 29.5L48 20.5C49.5 26 49.5 36 48 41.5L36 34Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    valves = "".join(rrect(x, 21, 4.5, 18, 2, INK) for x in (18, 25.5))
    return tube + bell + valves

@small("com.github.bleakgrey.transporter")
def transporter_s():
    arcs = (stroke("M17.5 27A15 15 0 0 1 40 17", INK, 4) +
            poly([(38, 12.5), (45, 18.5), (37, 21.5)], INK, 1.5) +
            stroke("M46.5 33A15 15 0 0 1 24 43", INK, 4) +
            poly([(26, 47.5), (19, 41.5), (27, 38.5)], INK, 1.5))
    return arcs + circle(32, 30, 8, INK)

@small("com.github.cassidyjames.clairvoyant")
def clairvoyant_s():
    ball = circle(CX, CY, 17, INK) + circle(CX, CY, 12, HOLE)
    return ball + ring_b(32, 25, 3.4, INK, 2.3) + ring_b(32, 34.3, 4.2, INK, 2.3)

@small("com.github.childishgiant.mixer")
def mixer_s():
    out = ""
    for x, y in [(20, 22), (32, 37), (44, 28)]:
        out += line(x, 13, x, 47, INK, 2) + rrect(x - 5.5, y - 4.5, 11, 9, 2.5, INK)
    return out

@small("com.github.djaler.formatter")
def formatter_s():
    plug = rrect(21, 12, 22, 12, 2, INK) + rrect(25, 16, 4.5, 4, .5, HOLE) + rrect(35, 16, 4.5, 4, .5, HOLE)
    body = rrect(16, 24, 32, 23, 3, INK)
    return plug + body + circle(42, 40, 11, HOLE) + circle(42, 40, 9, BLUE)

@small("com.github.donadigo.eddy")
def eddy_s():
    swirl = stroke("M40 22C37 17 30 16 25 19C19.5 22.5 18.5 30.5 22 36C25.5 41 32.5 41.5 36 38"
                   "C39 35 38.5 30 35 28.5", INK, 3.4)
    return g(swirl, "translate(-2 3)") + circle(43, 19, 9.5, HOLE) + circle(43, 19, 7.5, INK)

@small("com.github.gijsgoudzwaard.image-optimizer")
def image_optimizer_s():
    frame = rrect(13, 14, 34, 28, 4, INK)
    scene = path("M16.5 38.5L25 28L33 38.5Z", HOLE) + circle(37, 22.5, 4, HOLE)
    return frame + scene + circle(43, 40, 11, HOLE) + circle(43, 40, 8.5, INK) + circle(43, 40, 3.5, HOLE)

@small("com.github.hannesschulze.optimizer")
def optimizer_s():
    dial = path("M13 42A19 19 0 0 1 51 42Z", INK)
    ticks = "".join(line(*pt(32, 42, 15, a), *pt(32, 42, 11, a), HOLE, 2.6) for a in (-160, -90, -20))
    needle = poly([(30, 44), (42, 31), (34, 45.5)], RED_LIGHT, 2) + circle(32, 43, 3.6, RED_LIGHT)
    return g(dial + ticks + needle, "translate(0 -2)")
