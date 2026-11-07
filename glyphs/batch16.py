# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 16: com.github.huluti.Curtail to com.github.phase1geo.minder.

Same rules as batch01: tile from the palette step nearest the brand
colour, mark in INK, HOLE for cut-throughs, any second shade another
palette step.
"""
import math
from lm import *
from glyphs.kit import arc_d, registry, ring_b, sector

ICONS, SMALL, reg, small = registry()

def halo(d, w, extra=6):
    """A stroke of tile colour under a stroked part, to part it from the mark."""
    return stroke(d, HOLE, w + extra)

def sheet(x0=18, x1=46, y0=11, y1=49, fold=8):
    return path(f"M{x0 + 3} {y0}H{x1 - fold}L{x1} {y0 + fold}V{y1 - 3}"
                f"A3 3 0 0 1 {x1 - 3} {y1}H{x0 + 3}A3 3 0 0 1 {x0} {y1 - 3}"
                f"V{y0 + 3}A3 3 0 0 1 {x0 + 3} {y0}Z", INK)

def book(left_extra="", right_extra=""):
    left = path("M31 18C26 14.5 20 14 14 15.5V44C20 42.5 26 43 31 46.5Z", INK)
    right = path("M33 18C38 14.5 44 14 50 15.5V44C44 42.5 38 43 33 46.5Z", INK)
    return left + right + left_extra + right_extra

def monitor(screen=""):
    body = rrect(13, 13, 38, 27, 4, INK)
    stand = rrect(24, 43, 16, 4, 2, INK) + rrect(29.5, 38, 5, 6, 0, INK)
    return body + stand + screen

@reg("com.github.huluti.Curtail", BLUE_GREY)
def curtail():

    bars = (line(21, 13, 43, 23, INK, 3.4) + line(43, 13, 21, 23, INK, 3.4))
    knob = circle(32, 18, 5, INK) + circle(32, 18, 2, HOLE)
    screw = rrect(29.5, 21, 5, 9, 1, INK) + rrect(22, 28.5, 20, 4.5, 2.25, INK)
    tray = path("M15 36H49V45A3 3 0 0 1 46 48H18A3 3 0 0 1 15 45Z", INK)
    arrow = stroke("M27 38.5L32 43L37 38.5", HOLE, 2.6)
    return bars + knob + screw + tray + arrow

@reg("com.github.jeremypw.gnonograms", DEEP_PURPLE)
def gnonograms():
    wave = path("M13 47C17 38 22 28 29 20C35 13.5 43 11.5 49.5 14.5"
                "C44 15 40.5 18.5 40.5 23.5C40.5 28 44 30.5 48 29"
                "C47.5 36 48.5 42 51 47Z", INK)
    foam = (circle(22, 43.5, 2.6, HOLE) + circle(30, 44, 2.6, HOLE) + circle(38, 43, 2.6, HOLE))
    return wave + foam

@reg("com.github.jeremyvaartjes.comgen", GREY_DEEP)
def comgen():
    return line(24, 44, 30, 16, INK, 5.5) + line(34, 44, 40, 16, INK, 5.5)

@reg("com.github.jmoerman.go-for-it", GREY_DEEP)
def go_for_it():
    face = circle(32, 30, 16.5, INK)
    hands = stroke("M32 20V30H42", HOLE, 3.4)
    return face + hands + circle(32, 30, 3, HOLE)

@reg("com.github.jms55.Sandbox", BROWN)
def sandbox():
    box = rrect(15, 13, 34, 34, 5, INK)
    cells = "".join(rrect(15 + 8.5 * c, 13 + 8.5 * r, 8.5, 8.5, 0, AMBER_LIGHT)
                    for r in range(4) for c in range(4) if (r + c) % 2 == 0 and (r, c) not in ((0, 0), (3, 3)))
    cells += path("M15 21.5V18A5 5 0 0 1 20 13H23.5V21.5Z", AMBER_LIGHT)
    cells += path("M40.5 38.5H49V42A5 5 0 0 1 44 47H40.5Z", AMBER_LIGHT)
    shovel = g(rrect(27, 30, 10, 12, 3.5, HOLE) + rrect(30.3, 17, 3.4, 15, 1.7, HOLE)
               + ring_b(32, 14.5, 3.2, HOLE, 2.6), "rotate(40 32 30)")
    return box + cells + shovel

@reg("com.github.johnfactotum.Foliate", TEAL_DEEP)
def foliate():
    leaf = g(path("M22.5 18C27 22 27 32 22.5 38C18 32 18 22 22.5 18Z", HOLE)
             + line(22.5, 25, 22.5, 42, HOLE, 2.2), "rotate(-20 22.5 30)")
    lines = "".join(rrect(36, y, 10, 2.4, 1.2, HOLE) for y in (21, 26, 31, 36))
    return book(leaf, lines)

@reg("com.github.johnfactotum.QuickLookup", ORANGE_DEEP)
def quicklookup():
    a = stroke("M17.5 36L22.5 22L27.5 36", HOLE, 2.6) + line(19.5, 31, 25.5, 31, HOLE, 2.4)
    mark = path("M38 15.5H45V33L41.5 29.5L38 33Z", RED)
    return book(a, mark)

@reg("com.github.joseexposito.touche", BLUE_GREY)
def touche():
    win = rrect(14, 13, 30, 25, 4, INK)
    gap = circle(41, 39, 12, HOLE)
    teeth = "".join(g(rrect(39, 27.5, 4, 23, 1.5, INK), f"rotate({45 * k} 41 39)") for k in range(4))
    gear = teeth + circle(41, 39, 8, INK) + circle(41, 39, 3.2, HOLE)
    return win + gap + gear

@reg("com.github.junrrein.PDFSlicer", RED_DEEP)
def pdfslicer():
    doc = sheet(24, 48, 11, 45)
    lines = "".join(rrect(29, y, 14, 2.4, 1.2, HOLE) for y in (19, 24, 29))
    blades = "M20.5 38L45 28.5M25 42.5L39.5 21.5"
    rings = "M17 39.5a3.6 3.6 0 1 0 0.01 0M24 46a3.6 3.6 0 1 0 0.01 0"
    gap = stroke(blades, HOLE, 8.5) + stroke(rings, HOLE, 8)
    sc = stroke(blades, INK, 3.4) + stroke(rings, INK, 2.8)
    return doc + lines + gap + sc

@reg("com.github.keyilan.swatches", AMBER_DEEP)
def swatches():
    card = rrect(16, 13, 32, 34, 5, INK)
    top = path("M16 33V18A5 5 0 0 1 21 13H43A5 5 0 0 1 48 18V33Z", AMBER_SOFT)
    return (card + top + rrect(21, 37, 18, 2.6, 1.3, HOLE) + rrect(21, 41.5, 11, 2.6, 1.3, HOLE))

@reg("com.github.kjlaw89.archetype", PURPLE)
def archetype():
    dots = "".join(circle(18 + 5.5 * k, 15, 2.2, INK) for k in range(3))
    a = stroke("M18 46L33 19L37 46", INK, 5) + line(25, 37, 36, 37, INK, 4)
    return dots + a

@reg("com.github.kjlaw89.webwatcher", BLUE_GREY_DEEP)
def webwatcher():
    globe = circle(29, 27, 14.5, INK)
    grid = (f'<ellipse cx="29" cy="27" rx="6" ry="14.5" fill="none" stroke="{HOLE}" stroke-width="2.2"/>'
            + line(14.5, 27, 43.5, 27, HOLE, 2.2))
    badge = circle(41, 39, 11.5, HOLE) + circle(41, 39, 9, DEEP_ORANGE)
    hands = stroke("M41 33.5V39.5H45.5", INK, 2.6)
    return globe + grid + badge + hands

@reg("com.github.kmal-kenneth.monilet", BLUE_GREY_DARK)
def monilet():
    track = arc_d(32, 31, 14, 135, 45 + 360, BLUE_GREY_LIGHT, 5)
    live = arc_d(32, 31, 14, 135, 270, INK, 5)
    return track + live

@reg("com.github.kmwallio.thiefmd", LIGHT_BLUE_DEEP)
def thiefmd():
    doc = sheet(15, 43, 11, 47)
    lines = (rrect(20, 18, 11, 2.6, 1.3, HOLE) + rrect(20, 23.5, 18, 2.6, 1.3, HOLE)
             + rrect(20, 29, 14, 2.6, 1.3, HOLE))
    back = path("M30 49L32 34L37 38H43L48 34L50 49Z", HOLE, f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')
    cat = poly([(31, 48), (32.5, 35), (37.5, 39), (43, 39), (48, 35), (49.5, 48)], INDIGO_DARK, 2)
    eyes = circle(37, 43.5, 1.9, INK) + circle(43.5, 43.5, 1.9, INK)
    return doc + lines + back + cat + eyes

@reg("com.github.lachhebo.Gabtag", RED)
def gabtag():
    disc = circle(27, 24, 12.5, INK) + circle(27, 24, 3.5, HOLE)
    card = rrect(13, 31, 32, 17, 4, HOLE) + rrect(15, 33, 28, 13, 3, INK)
    lines = rrect(19, 37, 14, 2.4, 1.2, HOLE) + rrect(19, 41, 9, 2.4, 1.2, HOLE)
    pen_d = "M49 14L36 34"
    pen = halo(pen_d, 4.5, 3.5) + stroke(pen_d, INK, 4.5)
    return disc + card + lines + pen

@reg("com.github.lafydev.animage", ORANGE_DEEP)
def animage():
    return path("M32 47C24 40 15 33 15 23.5C15 17.5 19.5 13.5 24.5 13.5C28 13.5 30.5 15.5 32 18"
                "C33.5 15.5 36 13.5 39.5 13.5C44.5 13.5 49 17.5 49 23.5C49 33 40 40 32 47Z", INK)

@reg("com.github.lainsce.aesop", GREY_DARK)
def aesop():
    roof = poly([(32, 12.5), (48, 20), (16, 20)], INK, 3)
    beam = rrect(17, 22, 30, 3.5, 1.2, INK)
    cols = "".join(rrect(x, 27, 5, 13, 1, INK) for x in (19.5, 29.5, 39.5))
    base = rrect(15, 42, 34, 5, 2, INK)
    return roof + beam + cols + base

@reg("com.github.lainsce.beemy", GREY_DEEP)
def beemy():
    face = path(sector(32, 40, 8, 25, 212, 328), INK)
    warn = path(sector(32, 40, 8, 25, 300, 328), RED_SOFT)
    needle = line(32, 40, 26, 22, HOLE, 2.6)
    bowl = stroke("M22 38L25.5 46H38.5L42 38", INK, 3.6)
    return face + warn + needle + circle(32, 40, 8, HOLE) + bowl

@reg("com.github.lainsce.coin", AMBER_DEEP)
def coin():
    return (circle(32, 30, 17, INK) + circle(32, 30, 12.5, HOLE)
            + rrect(29, 20, 6, 20, 3, INK))

@reg("com.github.lainsce.timetable", BLUE_DEEP)
def timetable():
    board = rrect(14, 13, 30, 32, 4, INK)
    cols = rrect(23, 13, 2.2, 32, 0, HOLE) + rrect(33, 13, 2.2, 32, 0, HOLE)
    badge = circle(41.5, 39, 11.5, HOLE) + circle(41.5, 39, 9, INK)
    hands = stroke("M41.5 33.5V39.5H46", HOLE, 2.6)
    return board + cols + badge + hands

@reg("com.github.lainsce.yishu", INDIGO_SOFT)
def yishu():
    return circle(32, 30, 17, "none", f' stroke="{INK}" stroke-width="6.5"') + circle(32, 30, 6, INK)

@reg("com.github.libresprite.LibreSprite", INDIGO_DEEP)
def libresprite():
    body = rrect(15, 13, 34, 34, 6, INK)
    chin = path("M15 38H49V41A6 6 0 0 1 43 47H21A6 6 0 0 1 15 41Z", INDIGO_SOFT)
    eyes = (stroke("M20 26L22.5 22.5H26.5L29 26", HOLE, 2.8) +
            stroke("M35 26L37.5 22.5H41.5L44 26", HOLE, 2.8))
    mouth = stroke("M21 30.5L24 33.5H40L43 30.5", HOLE, 2.8)
    return body + chin + eyes + mouth

@reg("com.github.liferooter.textpieces", RED)
def textpieces():
    blade = path("M15 23C15 16.5 21 13.5 29 15.5L39 22H15Z", INK)
    body = rrect(13, 24.5, 38, 12, 6, INK)
    cross = rrect(36, 29, 8.4, 3, 0.8, HOLE) + rrect(38.7, 26.3, 3, 8.4, 0.8, HOLE)
    return g(blade + body + cross, "rotate(-38 32 28)")

@reg("com.github.linuxhubit.catfacts", INDIGO_LIGHT)
def catfacts():
    pad = path("M32 29C37 29 43 36 43 41C43 45 39.5 46.5 36.5 45.5C34.5 45 33.5 44.5 32 44.5"
               "C30.5 44.5 29.5 45 27.5 45.5C24.5 46.5 21 45 21 41C21 36 27 29 32 29Z", INK)
    toes = "".join(g(f'<ellipse cx="{x}" cy="{y}" rx="3.6" ry="4.6" fill="{INK}"/>', f"rotate({r} {x} {y})")
                   for x, y, r in [(18, 26, -20), (26, 18.5, -8), (38, 18.5, 8), (46, 26, 20)])
    return pad + toes

@reg("com.github.linuxhubit.gitscover", BLUE_DEEP)
def gitscover():
    lenses = (ring_b(23, 19, 6.2, INK, 3.6) + ring_b(41, 19, 6.2, INK, 3.6) + rrect(29, 17.5, 6, 3, 1, INK))
    branch = stroke("M23 25.5V38M41 25.5C41 33 35 34 24 36.5", INK, 3.4)
    tip = ring_b(23, 43, 4.6, INK, 3.2)
    return lenses + branch + tip

@reg("com.github.linuxhubit.ppaextender", ORANGE_DEEP)
def ppaextender():
    backs = stroke("M17 15H47M16 19.5H48", INK, 2.6)
    folder = path("M14 26A3 3 0 0 1 17 23H26L29 26H47A3 3 0 0 1 50 29V44A3 3 0 0 1 47 47H17"
                  "A3 3 0 0 1 14 44Z", INK)
    return backs + folder

@reg("com.github.linuxhubit.shouldidoit", AMBER_DEEP)
def shouldidoit():
    cuff = rrect(15, 27, 7, 18, 2.5, INK)
    hand = path("M25 29L31.5 21C33 19 33.5 17 33.5 14.5C33.5 12.5 37.5 12.5 38.5 15.5"
                "C39.5 18.5 38.5 22 37.5 25H45.5C48 25 49.5 27 49 29.5L46.5 42"
                "C46 44 44.5 45 42.5 45H25Z", INK)
    return cuff + hand

@reg("com.github.louis77.tuner", PINK)
def tuner():
    body = rrect(14, 16, 36, 30, 6, INK)
    window = rrect(18.5, 20.5, 27, 8, 2, HOLE)
    ticks = "".join(rrect(x, 22.5, 1.6, 4, 0.8, INK) for x in (22, 26, 30, 36, 40))
    needle = rrect(33, 21, 2, 7, 0.8, PINK_SOFT)
    knob = circle(32, 38, 5, HOLE)
    return body + window + ticks + needle + knob

@reg("com.github.manexim.insomnia", CYAN_DEEP)
def insomnia():
    zz = stroke("M16 21H28L16 39H28M36 21H48L36 39H48", INK, 4.2)
    slash = "M44 13L20 47"
    return zz + halo(slash, 4, 4) + stroke(slash, INK, 4)

@reg("com.github.manexim.typewriter", DEEP_PURPLE_SOFT)
def typewriter():
    paper = rrect(21, 11, 22, 16, 2, INK)
    lines = rrect(24.5, 14.5, 8, 2.2, 1.1, HOLE) + rrect(24.5, 18.5, 12, 2.2, 1.1, HOLE)
    body = rrect(12, 21, 40, 26, 6, HOLE) + rrect(14, 23, 36, 24, 5, INK)
    keys = "".join(circle(19.5 + 5 * c, 29 + 5 * r, 1.8, HOLE) for r in range(2) for c in range(6))
    space = rrect(22, 39.5, 20, 3, 1.5, HOLE)
    return paper + lines + body + keys + space

@reg("com.github.maoschanz.DynamicWallpaperEditor", DEEP_PURPLE)
def dynamic_wallpaper():
    screen = rrect(16.5, 16.5, 31, 20, 2, HOLE)
    split = stroke("M22 36.5L41 16.5", INK, 3)
    sun = circle(41, 25, 3.2, INK) + "".join(line(*pt(41, 25, 5, 45 * k), *pt(41, 25, 6.8, 45 * k), INK, 1.6)
                                              for k in range(8))
    moon = path("M27 24.5A5 5 0 1 0 28 33A6 6 0 0 1 27 24.5Z", INK)
    return monitor(screen + split + moon + sun)

@reg("com.github.maoschanz.drawing", RED_DEEP)
def drawing():
    canvas = rrect(13, 17, 31, 28, 4, INK)
    squiggle = stroke("M18 38C18 32 22 31 23 34C24 37 27 36 27.5 32", HOLE, 2.4)
    d = "M48.5 13.5L31 33"
    crayon = halo(d, 5.5, 4) + stroke(d, INK, 5.5) + poly([(28.5, 31), (33, 35.5), (26.5, 38)], INK, 1.5)
    return canvas + squiggle + crayon

@reg("com.github.marbetschar.time-limit", BLUE_DEEP)
def time_limit():
    ring_ = arc_d(32, 30, 16.5, -90, 100, INK, 3)
    face = circle(32, 30, 11.5, INK)
    hand = line(32, 30, 27, 25, HOLE, 3)
    return ring_ + face + hand + circle(32, 30, 2, HOLE)

@reg("com.github.matfantinel.moneta", AMBER_DARK)
def moneta():
    card = g(rrect(16, 14, 30, 19, 3, INK), "rotate(-12 31 24)")
    gap = rrect(12, 24, 40, 23, 4, HOLE)
    note = rrect(14, 26, 36, 19, 3, INK)
    marks = (circle(32, 35.5, 4.5, HOLE) + circle(19.5, 35.5, 2, HOLE) + circle(44.5, 35.5, 2, HOLE))
    return card + gap + note + marks

@reg("com.github.mdh34.hackup", DEEP_ORANGE_LIGHT)
def hackup():
    return line(32, 48, 32, 22, INK, 5) + poly([(32, 11.5), (43, 25), (21, 25)], INK, 3)

@reg("com.github.mdh34.quickdocs", BLUE_GREY_DARK)
def quickdocs():
    return (stroke("M24 16H18V44H24", INK, 4.4) +
            stroke("M30 16H33C41 16 46 21.5 46 30C46 38.5 41 44 33 44H30", INK, 4.4))

@reg("com.github.mirkobrombin.football", INDIGO_LIGHT)
def football():
    ball = circle(32, 30, 17, INK)
    centre = poly([pt(32, 30, 6.5, -90 + 72 * k) for k in range(5)], HOLE, 1.5)
    patches = seams = ""
    for k in range(5):
        a = math.radians(-90 + 72 * k)
        ca, sa = math.cos(a), math.sin(a)

        def at(u, v):
            return 32 + u * ca - v * sa, 30 + u * sa + v * ca
        ins, ls, rs = (9.8, 0), (14.2, -6.4), (14.2, 6.4)
        outs = []
        for side in (-1, 1):
            b0, b1 = (14.2, 6.4 * side), (21.5, 3.9 * side)
            lo, hi = 0.0, 1.0
            for _ in range(30):
                m = (lo + hi) / 2
                u, v = b0[0] + m * (b1[0] - b0[0]), b0[1] + m * (b1[1] - b0[1])
                lo, hi = (m, hi) if u * u + v * v < 17 * 17 else (lo, m)
            outs.append((u, v))
        p = [at(*ins), at(*rs), at(*outs[1]), at(*outs[0]), at(*ls)]
        d = (f"M{f(p[0][0])} {f(p[0][1])}L{f(p[1][0])} {f(p[1][1])}L{f(p[2][0])} {f(p[2][1])}"
             f"A17 17 0 0 0 {f(p[3][0])} {f(p[3][1])}L{f(p[4][0])} {f(p[4][1])}Z")
        patches += path(d, HOLE, f' stroke="{HOLE}" stroke-width="1" stroke-linejoin="round"')
        seams += line(*at(6.5, 0), *at(9.8, 0), HOLE, 2.2)
        seams += line(*at(14.2, 6.4), *pt(32, 30, 17, -90 + 72 * k + 36), HOLE, 2.2)
    return ball + centre + patches + seams + ring_b(32, 30, 16.1, INK, 1.8)

@reg("com.github.mohelm97.screenrecorder", RED)
def screenrecorder():
    screen = rrect(17, 17, 30, 19, 2, HOLE)
    frame = (f'<rect x="20" y="20" width="24" height="13" rx="1.5" fill="none" stroke="{INK}" '
             'stroke-width="2.2" stroke-dasharray="3 2.2"/>')
    return monitor(screen + frame + circle(32, 26.5, 3.8, INK))

@reg("com.github.mubitosh.qrshare", GREY_DARK)
def qrshare():
    def finder(x, y):
        return cut(f"M{x} {y}h12v12h-12Z" + f"M{x + 2.6} {y + 2.6}v6.8h6.8v-6.8Z", INK) + rrect(x + 4.2, y + 4.2, 3.6, 3.6, 0.6, INK)
    out = finder(14, 12) + finder(38, 12) + finder(14, 36)
    blocks = [(29, 12), (29, 19), (14, 29), (22, 29), (29, 29), (38, 29), (45, 29),
              (29, 38), (38, 36), (45, 42), (38, 45), (29, 45)]
    out += "".join(rrect(x, y, 5, 5, 0.8, INK) for x, y in blocks)
    return out

@reg("com.github.muriloventuroso.easyssh", GREY_DARK)
def easyssh():
    dollar = (stroke("M26 18.5C24.5 16.8 23 16.5 21 16.5C18.5 16.5 16.5 18 16.5 20.5"
                     "C16.5 25.5 26 23.5 26 29C26 31.5 23.8 33 21 33C19 33 17.2 32.2 16 30.5", INK, 3.2)
              + line(21, 13, 21, 36.5, INK, 2.6))
    under = line(29, 36, 37, 36, INK, 3.2)
    caret = stroke("M39.5 25L44 20L48.5 25", INK, 3.2)
    swoosh = stroke("M16 44C26 46 38 45.5 48 41", INK, 3)
    return dollar + under + caret + swoosh

@reg("com.github.muriloventuroso.givemelyrics", PURPLE_LIGHT)
def givemelyrics():
    note = (g(f'<ellipse cx="24" cy="41" rx="6.5" ry="4.8" fill="{INK}"/>', "rotate(-20 24 41)")
            + rrect(27.8, 14, 3.2, 27, 1.2, INK)
            + path("M29.5 14C33 19 38 20 38.5 27C36.5 24.5 33.5 23 30 23Z", INK))
    lines = "".join(rrect(38, y, 10, 2.6, 1.3, INK) for y in (31, 36.5)) + rrect(34, 14, 14, 2.6, 1.3, INK)
    return note + lines + rrect(40, 19.5, 8, 2.6, 1.3, INK)

@reg("com.github.naaando.lyrics", DEEP_PURPLE)
def lyrics():
    rings = (ring_b(32, 30, 16, INK, 2.6, ' stroke-dasharray="9 3.5" stroke-linecap="round"')
             + ring_b(32, 30, 11, INK, 2.6, ' stroke-dasharray="6 3" stroke-linecap="round"'))
    play = poly([(29, 24.5), (37.5, 30), (29, 35.5)], INK, 2.5)
    return rings + play

@reg("com.github.neithern.g4music", BLUE_GREY_LIGHT)
def g4music():
    disc = circle(32, 30, 17, INK)
    grooves = arc_d(32, 30, 13.5, -80, 10, HOLE, 2.2) + arc_d(32, 30, 10, -70, 0, HOLE, 2.2)
    grooves += arc_d(32, 30, 13.5, 100, 190, HOLE, 2.2)
    return disc + grooves + circle(32, 30, 6, BLUE_GREY_DEEP) + circle(32, 30, 2.2, INK)

@reg("com.github.nick92.tranqil", PINK_DEEP)
def tranqil():
    disc = circle(32, 30, 17, INK)
    sun = circle(35, 27, 9, HOLE)
    land = path("M15.5 34.5C23 30 29.5 40 37.5 36C42 34 45 34.5 48.7 34"
                "A17 17 0 0 1 15.5 34.5Z", PINK_DARK)
    return disc + sun + land

@reg("com.github.padjis.ghistory", GREY_DEEP)
def ghistory():
    gg = stroke("M29.5 21.5C28 19.8 26 19 23.5 19C18.5 19 15 23.5 15 30C15 36.5 18.5 41 23.5 41"
                "C27 41 30 39 30 34.5V31.5H24", INK, 4.2)
    h = stroke("M37 17V41M37 32C37 28.5 39.5 26.5 42.5 26.5C45.5 26.5 48 28.5 48 32V41", INK, 4.2)
    return gg + h

@reg("com.github.paolostivanin.OTPClient", RED)
def otpclient():
    pill = rrect(12.5, 21, 39, 18, 9, INK)
    dial = ring_b(22, 30, 4.3, HOLE, 2.6)

    def ast(x):
        return "".join(line(*pt(x, 30, 3.6, a), *pt(x, 30, 3.6, a + 180), HOLE, 2.2) for a in (90, 30, -30))
    return pill + dial + ast(32.5) + ast(42)

@reg("com.github.parnold-x.timer", DEEP_PURPLE_LIGHT)
def timer():
    bells = circle(20, 17, 6, INK) + circle(44, 17, 6, INK)
    feet = line(22, 44, 19.5, 47, INK, 3.2) + line(42, 44, 44.5, 47, INK, 3.2)
    body = circle(32, 31, 16.5, HOLE) + circle(32, 31, 14.5, INK)
    dots = "".join(circle(*pt(32, 31, 10.5, 90 * k), 1.5, HOLE) for k in range(4))
    hands = stroke("M32 24.5V31L27 35", HOLE, 2.8)
    return bells + feet + body + dots + hands

@reg("com.github.peteruithoven.resizer", RED_LIGHT)
def resizer():
    pic = rrect(19, 19, 26, 22, 3, INK)
    scene = circle(38, 26, 3, HOLE) + path("M19 36L26 30L33 35L37 32L45 37V38A3 3 0 0 1 42 41H22A3 3 0 0 1 19 38Z", HOLE)
    arrows = (stroke("M20 18.5L13.5 12M13.5 18V12H19.5", INK, 3) +
              stroke("M44 41.5L50.5 48M50.5 42V48H44.5", INK, 3))
    return pic + scene + arrows

@reg("com.github.phase1geo.annotator", LIGHT_BLUE_DEEP)
def annotator():
    pic = rrect(13, 15, 32, 27, 4, INK)
    sun = circle(20.5, 22, 3.2, HOLE)
    sea = stroke("M16.5 34C20 31.5 23 31.5 26 34C29 36.5 32 36.5 35 34", HOLE, 2.4)
    d = "M49 18.5L36 34"
    pen = halo(d, 6, 4) + stroke(d, INK, 6) + poly([(33, 32), (38, 36.5), (31.5, 40)], INK, 1.5)
    under = rrect(18, 45, 15, 2.6, 1.3, INK)
    return pic + sun + sea + pen + under

@reg("com.github.phase1geo.minder", BLUE_GREY)
def minder():
    cloud = path("M20 40C15.5 40 13 37 13 33.5C13 30 15.5 27.5 18.5 27.5C18 22 22 18 27 18.5"
                 "C29 14.5 33 12.5 37.5 13.5C42 14.5 45 18.5 45 22.5C48.5 23.5 51 26.5 51 30.5"
                 "C51 36 47 40 42 40Z", INK)
    puffs = circle(21, 44.5, 2.8, INK) + circle(16, 48, 1.8, INK)
    nodes = (rrect(17.5, 28, 9, 5, 1.5, HOLE) + rrect(36, 21, 9, 5, 1.5, HOLE)
             + rrect(36, 31, 9, 5, 1.5, HOLE))
    links = stroke("M26 30.5H30M30 23.5V33.5M30 23.5H37M30 33.5H37", HOLE, 2)
    return cloud + puffs + nodes + links

@small("com.github.huluti.Curtail")
def curtail_s():
    top = rrect(18, 13, 28, 5, 2.5, INK) + rrect(29, 16, 6, 10, 1, INK)
    tray = path("M15 33H49V44A4 4 0 0 1 45 48H19A4 4 0 0 1 15 44Z", INK)
    return top + tray + stroke("M26 36.5L32 42L38 36.5", HOLE, 3.2)

@small("com.github.jms55.Sandbox")
def sandbox_s():
    box = rrect(15, 13, 34, 34, 5, INK)
    cells = (path("M15 30V18A5 5 0 0 1 20 13H32V30Z", AMBER_LIGHT) +
             path("M32 30H49V42A5 5 0 0 1 44 47H32Z", AMBER_LIGHT))
    shovel = g(rrect(26, 30, 12, 14, 4, HOLE) + rrect(30, 14, 4, 17, 2, HOLE), "rotate(40 32 30)")
    return box + cells + shovel

@small("com.github.johnfactotum.Foliate")
def foliate_s():
    leaf = g(path("M22.5 18C28 23 28 33 22.5 39C17 33 17 23 22.5 18Z", HOLE), "rotate(-20 22.5 30)")
    lines = "".join(rrect(36, y, 10, 3.6, 1.8, HOLE) for y in (22, 30))
    return book(leaf, lines)

@small("com.github.johnfactotum.QuickLookup")
def quicklookup_s():
    return book(stroke("M17 38L22.5 21L28 38", HOLE, 3.2), path("M37 15H46V35L41.5 30.5L37 35Z", RED))

@small("com.github.junrrein.PDFSlicer")
def pdfslicer_s():
    doc = sheet(24, 48, 11, 45)
    blades = "M20 38L45 27M25 43L38 21"
    return (doc + stroke(blades, HOLE, 8.5) + circle(18, 41, 6.5, HOLE) + stroke(blades, INK, 3.4)
            + circle(18, 41, 4.5, INK))

@small("com.github.lachhebo.Gabtag")
def gabtag_s():
    disc = circle(28, 24, 13, INK) + circle(28, 24, 4, HOLE)
    card = rrect(13, 31, 32, 18, 4, HOLE) + rrect(15, 33, 28, 14, 3, INK)
    return disc + card + rrect(19, 38, 14, 3.4, 1.7, HOLE)

@small("com.github.lainsce.beemy")
def beemy_s():
    face = path(sector(32, 40, 9, 25, 212, 328), INK)
    return face + line(32, 38, 26, 22, HOLE, 3.4) + stroke("M21 39L25 47H39L43 39", INK, 3.6)

@small("com.github.kjlaw89.webwatcher")
def webwatcher_s():
    globe = circle(29, 27, 14.5, INK) + line(14.5, 27, 43.5, 27, HOLE, 2.6)
    return globe + circle(41, 39, 12, HOLE) + circle(41, 39, 9.5, DEEP_ORANGE)

@small("com.github.joseexposito.touche")
def touche_s():
    win = rrect(14, 13, 30, 25, 4, INK)
    return win + circle(41, 39, 12.5, HOLE) + circle(41, 39, 9.5, INK) + circle(41, 39, 3.8, HOLE)

@small("com.github.lainsce.timetable")
def timetable_s():
    board = rrect(14, 13, 30, 32, 4, INK) + rrect(28, 13, 3, 32, 0, HOLE)
    return board + circle(41.5, 39, 12, HOLE) + circle(41.5, 39, 9.5, INK) + stroke("M41.5 34V39.5H45.5", HOLE, 2.6)

@small("com.github.liferooter.textpieces")
def textpieces_s():
    blade = path("M15 23C15 16.5 21 13.5 29 15.5L39 22H15Z", INK)
    body = rrect(13, 24.5, 38, 12, 6, INK)
    return g(blade + body + circle(40.5, 30.5, 3, HOLE), "rotate(-38 32 28)")

@small("com.github.manexim.insomnia")
def insomnia_s():
    return stroke("M19 18H45L19 42H45", INK, 5)

@small("com.github.manexim.typewriter")
def typewriter_s():
    paper = rrect(21, 11, 22, 16, 2, INK)
    body = rrect(12, 21, 40, 26, 6, HOLE) + rrect(14, 23, 36, 24, 5, INK)
    keys = "".join(rrect(19 + 9.5 * c, 29, 7, 4, 1.5, HOLE) for c in range(3))
    return paper + body + keys + rrect(22, 38, 20, 4, 2, HOLE)

@small("com.github.maoschanz.DynamicWallpaperEditor")
def dynamic_wallpaper_s():
    screen = rrect(17, 17, 30, 19, 2, HOLE)
    moon = path("M29 20A7 7 0 1 0 31 33A8 8 0 0 1 29 20Z", INK)
    return monitor(screen + moon + circle(41, 23.5, 3.5, INK))

@small("com.github.maoschanz.drawing")
def drawing_s():
    canvas = rrect(13, 17, 31, 28, 4, INK)
    d = "M48.5 13.5L31 33"
    return canvas + halo(d, 6.5, 4) + stroke(d, INK, 6.5) + poly([(28, 30.5), (33.5, 36), (26, 38.5)], INK, 1.5)

@small("com.github.matfantinel.moneta")
def moneta_s():
    return rrect(13, 19, 38, 24, 4, INK) + circle(32, 31, 6, HOLE)

@small("com.github.mirkobrombin.football")
def football_s():
    ball = circle(32, 30, 17, INK)
    centre = poly([pt(32, 30, 7, -90 + 72 * k) for k in range(5)], HOLE, 2)
    spokes = "".join(line(32, 30, *pt(32, 30, 17, -90 + 72 * k), HOLE, 2.4) for k in range(5))
    return ball + spokes + centre

@small("com.github.mohelm97.screenrecorder")
def screenrecorder_s():
    return monitor(rrect(17, 17, 30, 19, 2, HOLE) + circle(32, 26.5, 5.5, INK))

@small("com.github.mubitosh.qrshare")
def qrshare_s():
    def finder(x, y):
        return rrect(x, y, 13, 13, 2, INK) + rrect(x + 3.5, y + 3.5, 6, 6, 1, HOLE)
    return (finder(14, 12) + finder(37, 12) + finder(14, 35)
            + rrect(37, 35, 6, 6, 1, INK) + rrect(44, 42, 6, 6, 1, INK) + rrect(29, 29, 6, 6, 1, INK))

@small("com.github.muriloventuroso.easyssh")
def easyssh_s():
    dollar = (stroke("M26 19C24.5 17 23 16.5 21 16.5C18.5 16.5 16.5 18 16.5 20.5"
                     "C16.5 25.5 26 23.5 26 29C26 31.5 23.8 33 21 33C19 33 17.2 32.2 16 30.5", INK, 3.2))
    return dollar + line(30, 34, 38, 34, INK, 3.4) + stroke("M39 25L44 19.5L49 25", INK, 3.4)

@small("com.github.naaando.lyrics")
def lyrics_s():
    return ring_b(32, 30, 15.5, INK, 3) + poly([(28, 22.5), (39.5, 30), (28, 37.5)], INK, 2.5)

@small("com.github.neithern.g4music")
def g4music_s():
    return circle(32, 30, 17, INK) + circle(32, 30, 7, DEEP_PURPLE) + circle(32, 30, 2.5, INK)

@small("com.github.paolostivanin.OTPClient")
def otpclient_s():
    pill = rrect(12.5, 21, 39, 18, 9, INK)
    return pill + ring_b(22, 30, 4.3, HOLE, 2.6) + circle(33, 30, 2.6, HOLE) + circle(42, 30, 2.6, HOLE)

@small("com.github.parnold-x.timer")
def timer_s():
    bells = circle(20, 17, 6.5, INK) + circle(44, 17, 6.5, INK)
    body = circle(32, 31, 17, HOLE) + circle(32, 31, 15, INK)
    return bells + body + stroke("M32 23.5V31L26.5 35", HOLE, 3)

@small("com.github.peteruithoven.resizer")
def resizer_s():
    pic = rrect(19, 19, 26, 22, 3, INK) + circle(37.5, 27, 3.5, HOLE)
    arrows = (stroke("M20 18.5L13.5 12M13.5 18V12H19.5", INK, 3) +
              stroke("M44 41.5L50.5 48M50.5 42V48H44.5", INK, 3))
    return pic + arrows

@small("com.github.phase1geo.annotator")
def annotator_s():
    pic = rrect(13, 15, 32, 27, 4, INK) + circle(21, 23, 3.8, HOLE)
    d = "M49 18.5L36 34"
    return pic + halo(d, 6.5, 4) + stroke(d, INK, 6.5) + poly([(33, 31.5), (38.5, 36.5), (31, 40.5)], INK, 1.5)

@small("com.github.phase1geo.minder")
def minder_s():
    cloud = path("M20 40C15.5 40 13 37 13 33.5C13 30 15.5 27.5 18.5 27.5C18 22 22 18 27 18.5"
                 "C29 14.5 33 12.5 37.5 13.5C42 14.5 45 18.5 45 22.5C48.5 23.5 51 26.5 51 30.5"
                 "C51 36 47 40 42 40Z", INK)
    return cloud + circle(20, 45.5, 3.2, INK) + stroke("M22 30.5H29L36 24.5M29 30.5L36 34", HOLE, 3)

@small("com.github.kmwallio.thiefmd")
def thiefmd_s():
    doc = sheet(15, 43, 11, 47)
    lines = rrect(20, 18, 16, 3.4, 1.7, HOLE) + rrect(20, 25, 12, 3.4, 1.7, HOLE)
    back = path("M30 49L32 34L37 38H43L48 34L50 49Z", HOLE, f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')
    cat = poly([(31, 48), (32.5, 35), (37.5, 39), (43, 39), (48, 35), (49.5, 48)], INDIGO_DARK, 2)
    return doc + lines + back + cat
