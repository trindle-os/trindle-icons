# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 26: etr to ffmpeg."""
from lm import (
    AMBER, AMBER_DEEP, BLUE, BLUE_DEEP, BLUE_GREY_DARK, BROWN, circle, cpath, cut, CYAN_DARK,
    DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, f, g, GREY_DARK,
    GREY_DEEP, HOLE, INDIGO, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE,
    LIGHT_BLUE_SOFT, line, ORANGE, ORANGE_DARK, ORANGE_DEEP, ORANGE_LIGHT, ORANGE_SOFT, path,
    PINK_LIGHT, poly, pt, PURPLE_LIGHT, RED, RED_DARK, RED_DEEP, RED_SOFT, rrect, stroke,
    YELLOW_DARK,
)
from glyphs.kit import _gear, registry, _star

ICONS, SMALL, reg, small = registry()


@reg("etr", DEEP_ORANGE_DEEP)
def etr():
    body = path("M14 30C18 22.5 25 19.5 32 19.5C38 19.5 42 22.5 44 26L50 20.5"
                "V39.5L44 34C42 37.5 38 40.5 32 40.5C25 40.5 18 37.5 14 30Z", INK)
    gill = stroke("M28 23.5C29.8 27.5 29.8 32.5 28 36.5", HOLE, 2.4)
    return body + gill + circle(21.5, 28.5, 2.2, HOLE)


@reg("euro-truck-simulator-2", GREY_DARK)
def ets2():
    wheel = cut(cpath(30, 29, 15.5) + cpath(30, 29, 11.5), INK)
    spokes = "".join(line(*pt(30, 29, 3, a), *pt(30, 29, 12, a), INK, 2.4)
                     for a in range(-90, 270, 60))
    badge = circle(43, 41, 9.5, HOLE) + circle(43, 41, 7.5, ORANGE)
    two = stroke("M40 38.5C40 36.8 41.3 35.6 43 35.6C44.8 35.6 46 36.8 46 38.3"
                 "C46 40.6 41.5 42.5 40 46H46.3", INK, 2.4)
    return wheel + spokes + circle(30, 29, 3.8, INK) + badge + two


@reg("europa-universalis-IV", BROWN)
def europa():
    ring = f'<circle cx="32" cy="30" r="12.5" fill="none" stroke="{INK}" stroke-width="2.4"/>'
    small = poly(_star(32, 30, 11, 3.5, 4, -45), INK, 1)
    big = poly(_star(32, 30, 18, 4, 4, -90), INK, 1)
    return ring + small + big + circle(32, 30, 2, HOLE)


@reg("evelauncher", BLUE_GREY_DARK)
def evelauncher():
    top = poly([(16, 14), (48, 14), (48, 21), (24, 21), (24, 18), (16, 18)], INK, 1.5)
    mid = rrect(24, 26.5, 24, 7, 1, INK) + rrect(16, 26.5, 5, 7, 1, INK)
    bot = poly([(16, 42), (24, 42), (24, 39), (48, 39), (48, 46), (16, 46)], INK, 1.5)
    return top + mid + bot


@reg("fall-guys", BLUE)
def fall_guys():
    head = path("M16 32C16 21 23 14 32 14C41 14 48 21 48 32V41A6 6 0 0 1 42 47H22"
                "A6 6 0 0 1 16 41Z", INK)
    return head + rrect(23.5, 30, 4.5, 9, 2.25, HOLE) + rrect(36, 30, 4.5, 9, 2.25, HOLE)


@reg("factorio", ORANGE_DEEP)
def factorio():
    return _gear(32, 30, 17, 13, 8, INK, 0.45) + circle(32, 30, 6, HOLE)


@reg("fez", RED_DEEP)
def fez():
    return (rrect(29, 19, 20, 22, 1.5, INK) + rrect(21, 19, 8, 8, 1, AMBER) +
            rrect(14, 27, 7, 7, 1, AMBER) + rrect(21, 27, 8, 14, 1, RED_DARK))


@reg("exult", BLUE_DEEP)
def exult():
    loop = (f'<ellipse cx="32" cy="19.5" rx="5.2" ry="6.8" fill="none" '
            f'stroke="{INK}" stroke-width="4.4"/>')
    bar = line(20, 30, 44, 30, INK, 5)
    stem = poly([(28.5, 30), (35.5, 30), (34.5, 42), (32, 46.5), (29.5, 42)], INK, 1.5)
    return loop + bar + stem


def _f1():
    ff = poly([(20, 18), (35, 18), (33.5, 24), (25, 24), (24.2, 27.5), (31, 27.5),
               (29.6, 33), (22.8, 33), (20.2, 43), (14, 43)], INK, 1.5)
    streaks = "".join(line(38 - 1.3 * i, 20 + 5.4 * i, 50 - 3 * (i % 2), 20 + 5.4 * i, INK, 3.4)
                      for i in range(5))
    return ff + streaks


@reg("f1-2017", AMBER)
@reg("f1-2015", RED)
def f1_2015():
    return _f1()


@reg("evernote", LIGHT_BLUE)
def evernote():
    head = path("M23 13H38C44.5 13 48 18 48 25V35.5C48 37.8 47 39.5 45.5 40.5V44.5"
                "C45.5 46.7 44 48 41.8 48H39.3C37.2 48 36.8 45.3 38.8 45.3H41V41.3"
                "C38.8 41.6 36.8 41 35.5 39.5C33 42 29.5 43 26 42C22 41 19.5 38 18.5 34"
                "C17.5 30 17.5 26 18 22.5L16 21V19.5L23 13Z", INK)
    corner = poly([(16, 19.5), (23, 13), (23, 19.5)], LIGHT_BLUE_SOFT, 1.2)
    ear = stroke("M30 19.5C33.5 24 33.5 30.5 29.5 34.5", HOLE, 2.4)
    return head + corner + ear + circle(41, 25, 2, HOLE)


@reg("facebook", BLUE_DEEP)
def facebook():
    return (stroke("M38 14.5H34.5C30.5 14.5 28.5 17 28.5 21V46.5", INK, 6.5) +
            line(22, 29.5, 38, 29.5, INK, 5.5))


@reg("fbmessenger", BLUE)
def fbmessenger():
    bubble = path("M32 14C22.5 14 15 21 15 30C15 35 17.5 39.5 21.5 42.5V48L27 45"
                  "C28.6 45.5 30.3 45.8 32 45.8C41.5 45.8 49 38.6 49 29.9C49 21 41.5 14 32 14Z", INK)
    zig = poly([(21.5, 34.5), (30, 25.5), (34.5, 30), (42.5, 25.5), (34, 34.5), (29.5, 30)], HOLE, 2)
    return bubble + zig


@reg("eu.scarpetta.QtWAW", ORANGE_DEEP)
def qtwaw():
    ring = cut(cpath(32, 28.5, 15.5) + cpath(32, 28.5, 10), INK)
    tail = poly([(27, 41), (37, 42), (26, 48.5)], INK, 2.5)
    return ring + tail


@reg("eureka", CYAN_DARK)
def eureka():
    top = poly([(20, 13), (43, 13), (43, 20), (27.5, 20), (27.5, 25), (39, 25),
                (39, 31), (20, 31)], INK, 1.5)
    bot = poly([(20, 33.5), (39, 33.5), (27.5, 42), (27.5, 47), (20, 47)], ORANGE_LIGHT, 1.5)
    return top + bot


@reg("everdo", ORANGE_DARK)
def everdo():
    return (stroke("M16.5 30.5L27 41", INK, 7.5) +
            stroke("M27 41L47.5 20", ORANGE_SOFT, 7.5))


@reg("eversion", ORANGE_DEEP)
def eversion():
    blob = "".join(circle(*pt(32, 30, 10.5, a), 7.2, INK) for a in range(0, 360, 60))
    blob += circle(32, 30, 11, INK)
    eyes = (f'<ellipse cx="26.5" cy="31" rx="3.2" ry="4.2" fill="{HOLE}"/>'
            f'<ellipse cx="37.5" cy="31" rx="3.2" ry="4.2" fill="{HOLE}"/>')
    return blob + eyes


@reg("excalidraw", INDIGO_LIGHT)
def excalidraw():
    pen = (line(20.5, 18.5, 38, 36, INK, 6.5) +
           poly([(35.5, 38.5), (40.5, 33.5), (45.5, 43.5)], INK, 2.5))
    gap = line(43.5, 18.5, 20.5, 41.5, HOLE, 10)
    ruler = line(43.5, 18.5, 20.5, 41.5, INK, 6)
    return pen + gap + ruler


@reg("exodus", DEEP_PURPLE_DEEP)
def exodus():
    left = stroke("M29 16.5H23L16.5 30L23 43.5H29", INK, 5) + line(23.5, 30, 28, 30, INK, 5)
    right = stroke("M35 16.5H41L47.5 30L41 43.5H35", INK, 5) + line(36, 30, 40.5, 30, INK, 5)
    return left + right


@reg("expandrive", RED)
def expandrive():
    petal = path("M32 30C27.5 25 26.5 17.5 31 13C37 13.5 41 19 39 25.5C37 28 34.5 29.5 32 30Z", INK)
    return "".join(g(petal, f"rotate({72 * k} 32 30)") for k in range(5)) + circle(32, 30, 2.4, HOLE)


@reg("factor", AMBER)
def factor():
    ring = f'<circle cx="32" cy="30" r="16.5" fill="none" stroke="{INK}" stroke-width="2.4"/>'
    head = path("M17 38C18 28 24.5 21.5 33 21C39 20.5 44.5 22 48.5 25.5L48 28.5L43 29"
                "L47 31.5L44.5 33.5C40.5 33.5 37 34.5 34 37L32.5 45.5C27 46.5 21.5 44 17 38Z", INK)
    return ring + head + circle(37.5, 25, 1.8, HOLE)


FALKON_HEAD = path('M15 43C16 28 26 17 40 16.5C44 16.4 47.5 18 49.5 21L44 22.5C45.3 24.5 45.3 27 44 29C38.5 27.5 32 29.5 27.5 34.5C24.5 38 22 42.5 20.5 46.5Z', INK)


@reg("falkon", DEEP_PURPLE_LIGHT)
def falkon():
    head = FALKON_HEAD
    streaks = (stroke("M24 37C28 31.5 33 29 38 29", HOLE, 2.2) +
               stroke("M20.5 42.5C24 36 28 33.5 33 33", HOLE, 2.2))
    return head + streaks + circle(40, 21, 1.9, HOLE)


@reg("ferdium", DEEP_PURPLE_LIGHT)
def ferdium():
    wing = path("M14 24C19 23 24.5 30 32 30C39.5 30 45 23 50 24C48.5 32 42 38 37 38"
                "L32 34.5L27 38C22 38 15.5 32 14 24Z", INK)
    return wing


@reg("fcitx-sogoupinyin", DEEP_ORANGE)
def sogou():
    s = stroke("M38.5 22C36.5 20 34.5 19.5 32 19.5C28 19.5 25.5 21.5 25.5 24.5"
               "C25.5 30.5 38.5 28.5 38.5 35C38.5 38 35.5 40.5 32 40.5"
               "C29 40.5 26.5 39.5 24.5 37.5", HOLE, 5)
    return circle(32, 30, 16.5, INK) + s


@reg("ffmpeg", PURPLE_LIGHT)
def ffmpeg():
    return stroke("M17 16H27L17 26V35L36 16H47V20L22 44H33L47 30V44H38", INK, 4.6)


@reg("ettercap", INDIGO_DEEP)
def ettercap():
    e = stroke("M21 31H43C43 23 38 17.5 32 17.5C25 17.5 20.5 23.5 20.5 30.5"
               "C20.5 38 25.5 43 32.5 43C36.5 43 39.5 41.5 42 39", INK, 5.5)
    return g(e, "translate(32 30) skewX(-14) translate(-32 -30)")


def _sheet(fold):
    sheet = path("M20 11H37L46 20V46A3 3 0 0 1 43 49H20A3 3 0 0 1 17 46V14A3 3 0 0 1 20 11Z", INK)
    return sheet + path("M37 11V17A3 3 0 0 0 40 20H46Z", fold)


@reg("eu.scarpetta.PDFMixTool", RED)
def pdfmixtool():
    hammer = line(24.5, 43, 36, 30, HOLE, 3.2) + g(rrect(31, 23.5, 11, 5.5, 1.5, HOLE), "rotate(45 36.5 26.25)")
    wrench = (line(39.5, 43, 28.5, 31, HOLE, 3.2) + circle(26.5, 28.5, 4.2, HOLE) +
              g(rrect(21, 25.3, 5, 2.8, 1, INK), "rotate(45 23.5 26.7)"))
    return _sheet(RED_SOFT) + hammer + wrench


@reg("evince", RED_DEEP)
def evince():
    doc = rrect(16.5, 13, 31, 35, 4, INK)
    lines = "".join(rrect(20.5, y, w, 3, 1.5, HOLE) for y, w in
                    [(17.5, 20), (24, 9), (30, 9), (36, 23), (42, 15)])
    pic = rrect(32.5, 23.5, 11, 10, 2, HOLE)
    e = stroke("M35.5 29H41C41 26.6 39.6 25.5 38.1 25.5C36.3 25.5 35.3 27 35.3 28.7"
               "C35.3 30.6 36.5 31.8 38.3 31.8C39.4 31.8 40.2 31.3 40.8 30.6", INK, 1.6)
    return doc + lines + pic + e


@reg("evnc", BLUE)
def evnc():
    tabs = "".join(rrect(x, y, 7, 7, 2.5, INK) for x in (13, 44) for y in (16, 37))
    frame = rrect(16.5, 15, 31, 30, 3, INK)
    return (tabs + frame + rrect(20.5, 19, 23, 22, 1.5, HOLE) +
            rrect(23.5, 22, 17, 16, 1, INK))


@reg("evolution", BLUE_DEEP)
def evolution():
    letter = rrect(19, 13, 22, 16, 2, INK) + rrect(22.5, 17, 15, 2.6, 1.3, HOLE)
    env = rrect(14, 21, 32, 23, 3.5, INK)
    flap = stroke("M16.5 24L30 33.5L43.5 24", HOLE, 2.6)
    clock = circle(44, 40, 9.5, HOLE) + circle(44, 40, 7.5, INK)
    hands = stroke("M44 35.8V40L46.8 42", HOLE, 2.2)
    return g(letter + env + flap + clock + hands, "translate(-1 0)")


@reg("evtest-qt", ORANGE_DEEP)
def evtest():
    base = rrect(14, 34, 36, 12, 3.5, INK)
    btns = rrect(17, 31, 6, 4, 1.5, INK) + rrect(41, 31, 6, 4, 1.5, INK)
    stick = line(32, 20, 32, 34, INK, 4.4) + rrect(28, 31.5, 8, 3.5, 1.2, INK)
    return base + btns + stick + circle(32, 18, 6.5, INK)


@reg("exaile", INDIGO_SOFT)
def exaile():
    return circle(32, 30, 16.5, INK) + poly([(28, 22), (41, 30), (28, 38)], HOLE, 4)


@reg("exmplayer", GREY_DARK)
def exmplayer():
    clap = rrect(15, 14, 34, 7, 2, INK)
    stripes = "".join(line(x, 20, x + 4, 15, HOLE, 2.2, "butt") for x in (19.5, 27.5, 35.5, 43.5))
    body = rrect(15, 23.5, 34, 23, 3, INK)
    play = poly([(28.5, 29), (38, 35), (28.5, 41)], HOLE, 2.5)
    return clap + stripes + body + play


@reg("exploit-db", BLUE_GREY_DARK)
def exploit_db():
    legs = "".join(stroke(d, INK, 2.4) for d in (
        "M29 30C24 25 21 22 16 22", "M29 32C24 30 19 31 15 34",
        "M30 34C26 36 23 40 21 45", "M31 28C28 23 27 18 23 14"))
    legs += g(legs, "translate(63 0) scale(-1 1)")
    body = (f'<ellipse cx="31.5" cy="37" rx="6" ry="8" fill="{INK}"/>' +
            circle(31.5, 27.5, 4.5, INK))
    return legs + body


@reg("extraterm", AMBER_DEEP)
def extraterm():
    return stroke("M18 20L28 29L18 38", INK, 5) + rrect(31, 36, 15, 5, 2.5, INK)


@reg("f3d", INDIGO_DEEP)
def f3d():
    top = poly([(38, 13), (22, 34), (33, 34)], INK, 2.5)
    bot = poly([(30.5, 26.5), (42, 26.5), (26, 47)], ORANGE_LIGHT, 2.5)
    return top + bot


@reg("famitracker", GREY_DARK)
def famitracker():
    return (stroke("M17 44V17H29.5", INK, 6) + line(17, 30, 27, 30, INK, 6) +
            line(33, 17, 48, 17, INK, 6) + line(40.5, 17, 40.5, 44, INK, 6))


@reg("far2l", INDIGO)
def far2l():
    out = rrect(14, 13, 17, 34, 2.5, INK) + rrect(33, 13, 17, 34, 2.5, INK)
    for x in (17.5, 36.5):
        out += "".join(rrect(x, y, 10, 3.5, 1.2, HOLE) for y in (17.5, 24.5, 31.5, 38.5))
    return out


@reg("fasttracker2", INDIGO_LIGHT)
def fasttracker2():
    ff = stroke("M15 43V18H25", INK, 4.4) + line(15, 29.5, 22.5, 29.5, INK, 4.4)
    t = stroke("M29 21V38.5C29 41.5 30.5 43 33 43", INK, 4.2) + line(25.5, 27.5, 33, 27.5, INK, 4.2)
    ii = (line(39.5, 18, 39.5, 43, INK, 4) + line(46, 18, 46, 43, INK, 4) +
          line(37, 18, 48.5, 18, INK, 3.6) + line(37, 43, 48.5, 43, INK, 3.6))
    return ff + t + ii


@reg("fbreader", RED_DEEP)
def fbreader():
    pages = rrect(14, 16, 17, 30, 2.5, INK) + rrect(33, 16, 17, 30, 2.5, INK)
    lines = "".join(rrect(x, y, 10, 2.6, 1.3, HOLE) for x in (17.5, 36.5) for y in (22, 28, 34, 40))
    mark = poly([(38.5, 13), (44.5, 13), (44.5, 27), (41.5, 24), (38.5, 27)], RED_SOFT, 1.5)
    return pages + lines + mark


@reg("fceux", GREY_DEEP)
def fceux():
    lid = rrect(14, 16, 36, 13, 3, INK)
    body = rrect(14, 31, 36, 14, 3, INK)
    label = rrect(18, 20.5, 14, 4, 1.5, RED)
    ridges = "".join(rrect(36, y, 10, 2.4, 1, HOLE) for y in (19, 23.5))
    ports = rrect(18, 36.5, 6, 3.5, 1.2, HOLE) + rrect(26, 36.5, 6, 3.5, 1.2, HOLE)
    return lid + body + label + ridges + ports


def _feather(dx=0, dy=0):
    vane = path("M47 13C47.5 26 40 37.5 26 39.5H21.5C22.5 25 32 15 47 13Z", INK)
    rachis = stroke("M44 16.5C36 23 29.5 30.5 24.5 37", HOLE, 2.2)
    notch = line(40.5, 32, 36, 29, HOLE, 2.2)
    quill = line(23, 38, 17, 47, INK, 3)
    return g(vane + rachis + notch + quill, f"translate({dx} {dy})")


@reg("feather", DEEP_ORANGE_DEEP)
def feather():
    return _feather(0, 0)


@reg("featherpad", BLUE_DEEP)
@reg("feathernotes", AMBER_DEEP)
def feathernotes():
    return g(_feather(0, 0), "translate(32 12) scale(.82) translate(-32 -12)") + rrect(15, 42, 34, 6, 2, INK)


@reg("feedindicator", GREY_DARK)
def feedindicator():
    outer = f'<circle cx="32" cy="30" r="14.5" fill="none" stroke="{INK}" stroke-width="4"/>'
    arc = stroke("M32 15.5A14.5 14.5 0 0 1 46.5 30", ORANGE, 4.4)
    inner = f'<circle cx="32" cy="30" r="7" fill="none" stroke="{INK}" stroke-width="4"/>'
    return outer + arc + inner


@reg("feh", RED_DEEP)
def feh():
    ff = stroke("M15 42V18H23.5", INK, 4.6) + line(15, 30, 22, 30, INK, 4.6)
    e = stroke("M36.5 18H28V42H36.5", INK, 4.6) + line(28, 30, 35, 30, INK, 4.6)
    h = line(41, 18, 41, 42, INK, 4.6) + line(49, 18, 49, 42, INK, 4.6) + line(41, 30, 49, 30, INK, 4.6)
    return ff + e + h


@reg("feishin", BLUE_GREY_DARK)
def feishin():
    roof = stroke("M15 41L32 19L49 41", INK, 6)
    eye = circle(32, 30, 6, INK) + circle(32, 30, 2.6, HOLE)
    return roof + eye + line(32, 34, 32, 40, INK, 3.4)


@reg("fern-wifi-cracker", YELLOW_DARK)
def fern():
    arcs = ""
    for r in (8, 14):
        a = stroke(f"M{f(32 - r * .7)} {f(27 - r * .7)}A{r} {r} 0 0 0 {f(32 - r * .7)} {f(27 + r * .7)}", INK, 3.2)
        arcs += a + g(a, "translate(64 0) scale(-1 1)")
    return arcs + circle(32, 27, 3.6, INK) + line(32, 30, 32, 47, INK, 3.6)


@reg("ff-password-exporter", PINK_LIGHT)
def ffpass():
    box = stroke("M33 16H22A6 6 0 0 0 16 22V40A6 6 0 0 0 22 46H40A6 6 0 0 0 46 40V35", INK, 5)
    arrow = stroke("M26 38C26 30 31 25.5 39 25.5", INK, 5.5)
    head = poly([(38, 17), (48.5, 25.5), (38, 34)], INK, 2.5)
    return box + arrow + head


@reg("ffado", RED_DEEP)
def ffado():
    arms = (line(32, 31, 23.5, 21.5, INK, 3.4) + line(32, 31, 40.5, 21.5, INK, 3.4) +
            line(32, 31, 32, 36, INK, 3.4))
    ends = circle(22, 19.5, 4.8, INK) + g(rrect(38, 15, 8.5, 8.5, 1.5, INK), "rotate(45 42.25 19.25)")
    bars = rrect(25, 37, 14, 3.6, 1.5, INK) + rrect(25, 42.5, 14, 3.6, 1.5, INK)
    return arms + ends + bars


@small("euro-truck-simulator-2")
def ets2_s():
    wheel = cut(cpath(30, 29, 15.5) + cpath(30, 29, 10.5), INK)
    spokes = "".join(line(*pt(30, 29, 3, a), *pt(30, 29, 11, a), INK, 3.2)
                     for a in range(-90, 270, 120))
    return wheel + spokes + circle(30, 29, 4, INK) + circle(43, 41, 9.5, HOLE) + circle(43, 41, 7.5, ORANGE)


@small("evince")
def evince_s():
    doc = rrect(16.5, 13, 31, 35, 4, INK)
    lines = "".join(rrect(20.5, y, w, 4, 2, HOLE) for y, w in [(18, 23), (26, 9), (34, 23), (41, 14)])
    return doc + lines + rrect(33, 25, 10.5, 6, 2, HOLE)


@small("exploit-db")
def exploit_db_s():
    legs = "".join(stroke(d, INK, 3) for d in (
        "M29 30C24 25 21 22 16 21", "M30 34C25 35 21 39 19 45"))
    legs += g(legs, "translate(63 0) scale(-1 1)")
    return legs + f'<ellipse cx="31.5" cy="36" rx="7" ry="9" fill="{INK}"/>' + circle(31.5, 26, 5, INK)


@small("fceux")
def fceux_s():
    return (rrect(14, 16, 36, 13, 3, INK) + rrect(14, 31, 36, 14, 3, INK) +
            rrect(18, 20.5, 15, 5, 2, RED) + rrect(18, 36, 14, 4.5, 2, HOLE))


@small("fasttracker2")
def fasttracker2_s():
    return (stroke("M17 44V17H29", INK, 5.5) + line(17, 30, 26, 30, INK, 5.5) +
            line(38, 17, 38, 44, INK, 5) + line(46, 17, 46, 44, INK, 5))


@small("europa-universalis-IV")
def europa_s():
    return poly(_star(32, 30, 18, 5, 4, -90), INK, 1.5) + circle(32, 30, 2.4, HOLE)


@small("falkon")
def falkon_s():
    head = FALKON_HEAD
    return head + circle(40, 21, 2.4, HOLE)


@small("far2l")
def far2l_s():
    out = rrect(14, 13, 17, 34, 2.5, INK) + rrect(33, 13, 17, 34, 2.5, INK)
    for x in (17.5, 36.5):
        out += "".join(rrect(x, y, 10, 5, 2, HOLE) for y in (18, 27.5, 37))
    return out


@small("etr")
def etr_s():
    body = path("M14 30C18 22.5 25 19.5 32 19.5C38 19.5 42 22.5 44 26L50 20.5"
                "V39.5L44 34C42 37.5 38 40.5 32 40.5C25 40.5 18 37.5 14 30Z", INK)
    return body + circle(22.5, 28.5, 3, HOLE)


@small("eu.scarpetta.PDFMixTool")
def pdfmixtool_s():
    return (_sheet(RED_SOFT) + line(24, 42, 39, 25, HOLE, 4.5) + line(40, 42, 25, 25, HOLE, 4.5))


@small("eversion")
def eversion_s():
    blob = "".join(circle(*pt(32, 30, 8.5, a), 9, INK) for a in (45, 135, 225, 315))
    return blob + circle(26.5, 31, 4, HOLE) + circle(37.5, 31, 4, HOLE)


@small("evolution")
def evolution_s():
    env = rrect(13, 17, 32, 24, 3.5, INK) + stroke("M16 21L29 30.5L42 21", HOLE, 3.2)
    return env + circle(44, 40, 10, HOLE) + circle(44, 40, 8, INK) + stroke("M44 35.5V40.5L47 42.5", HOLE, 3)


@small("exmplayer")
def exmplayer_s():
    return (rrect(15, 14, 34, 7, 2, INK) + rrect(15, 24, 34, 22, 3, INK) +
            poly([(28, 29), (39, 35), (28, 41)], HOLE, 2.5))


@small("ffmpeg")
def ffmpeg_s():
    return stroke("M18 17H30L18 30V43L46 17V30L34 43H46", INK, 6)


@small("fern-wifi-cracker")
def fern_s():
    a = stroke("M22.5 19.5A13.5 13.5 0 0 0 22.5 34.5", INK, 4.4)
    return a + g(a, "translate(64 0) scale(-1 1)") + circle(32, 27, 4.5, INK) + line(32, 30, 32, 47, INK, 4.4)


@small("ff-password-exporter")
def ffpass_s():
    box = stroke("M31 16H22A6 6 0 0 0 16 22V40A6 6 0 0 0 22 46H40A6 6 0 0 0 46 40V36", INK, 6)
    return box + stroke("M26 38C26 30 31 26 38 26", INK, 6.5) + poly([(37, 17), (48.5, 26), (37, 35)], INK, 3)


@small("feh")
def feh_s():
    ff = stroke("M19 43V17H30", INK, 6.5) + line(19, 30, 28, 30, INK, 6.5)
    e = stroke("M46 17H36V43H46", INK, 6.5) + line(36, 30, 44, 30, INK, 6.5)
    return ff + e


@small("f1-2015")
def f1_2015_s():
    ff = poly([(20, 18), (35, 18), (33.5, 24), (25, 24), (24.2, 27.5), (31, 27.5),
               (29.6, 33), (22.8, 33), (20.2, 43), (14, 43)], INK, 2)
    return ff + "".join(line(38 - 2 * i, 21 + 9 * i, 49, 21 + 9 * i, INK, 5) for i in range(3))


SMALL["f1-2017"] = f1_2015_s


@small("factor")
def factor_s():
    head = path("M15 40C16 28 23.5 20.5 33 20C39.5 19.5 45.5 21.5 50 25.5L49.5 29L44 30"
                "L48.5 32.5L45.5 35C41 35 37.5 36 34 39L32.5 47C26 48 19.5 45.5 15 40Z", INK)
    return head + circle(38, 25, 2.6, HOLE)


def _feather_s():
    vane = path("M47 13C47.5 26 40 37.5 26 39.5H21.5C22.5 25 32 15 47 13Z", INK)
    return vane + stroke("M43 17.5C36 23.5 30 30.5 25 37", HOLE, 3) + line(23, 38, 17, 47, INK, 4)


@small("feather")
def feather_s():
    return _feather_s()


@small("feathernotes")
def feathernotes_s():
    return g(_feather_s(), "translate(32 12) scale(.82) translate(-32 -12)") + rrect(15, 41, 34, 7, 2.5, INK)


SMALL["featherpad"] = feathernotes_s


@small("feedindicator")
def feedindicator_s():
    outer = f'<circle cx="32" cy="30" r="14" fill="none" stroke="{INK}" stroke-width="5"/>'
    return outer + stroke("M32 16A14 14 0 0 1 46 30", ORANGE, 5.5) + circle(32, 30, 5.5, INK)


@small("fbreader")
def fbreader_s():
    pages = rrect(14, 16, 17, 30, 2.5, INK) + rrect(33, 16, 17, 30, 2.5, INK)
    lines = "".join(rrect(x, y, 10, 4, 2, HOLE) for x in (17.5, 36.5) for y in (29, 37))
    return pages + lines + poly([(37.5, 13), (45.5, 13), (45.5, 26), (41.5, 22.5), (37.5, 26)], RED_SOFT, 1.5)
