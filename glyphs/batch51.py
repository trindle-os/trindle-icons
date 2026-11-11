# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 51: F-Droid Repomaker to GNOME Simple Scan."""
import math
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_LIGHT, AMBER_SOFT, BLUE_DARK, BLUE_DEEP, BLUE_GREY,
    BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_LIGHT, BLUE_SOFT, BROWN_LIGHT, circle,
    CX, CY, CYAN_DARK, CYAN_DEEP, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_SOFT,
    DEEP_PURPLE, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, f, g, GREY, GREY_DARK, HOLE, INDIGO,
    INDIGO_DEEP, INDIGO_SOFT, INK, LIGHT_BLUE_DEEP, line, ORANGE_DARK, ORANGE_DEEP, path, poly,
    pt, PURPLE, PURPLE_LIGHT, RED, RED_DEEP, RED_SOFT, rrect, stroke,
)
from glyphs.kit import arc_g, ellipse_g, registry, _ring

ICONS, SMALL, reg, small = registry()


@reg("org.fdroid.Repomaker", BLUE_DEEP)
def repomaker():
    head = rrect(19, 13, 26, 9.5, 4.5, INK) + circle(25.5, 17.7, 1.9, HOLE) + circle(38.5, 17.7, 1.9, HOLE)
    ant = line(21.5, 14, 18.5, 11, INK, 2.2) + line(42.5, 14, 45.5, 11, INK, 2.2)
    box = rrect(17, 25, 30, 23, 4, INK) + _ring(32, 36.5, 6.2, HOLE, 2.8)
    return head + ant + box


@reg("org.flozz.yoga-image-optimizer", CYAN_DEEP)
def yoga():
    ears = (poly([(22, 27), (13.5, 23), (19.5, 36)], INK, 3) +
            poly([(42, 27), (50.5, 23), (44.5, 36)], INK, 3))
    head = circle(32, 32, 12.5, INK)
    knot = circle(32, 14.5, 3.6, INK) + line(32, 17, 32, 21, INK, 2.4)
    face = (circle(27.3, 30, 2.3, HOLE) + circle(36.7, 30, 2.3, HOLE) +
            path("M27.3 35H36.7A4.7 4.7 0 0 1 27.3 35Z", HOLE))
    return ears + head + knot + face


@reg("org.fn2006.PollyMC", AMBER_DARK)
def pollymc():
    px = "".join(rrect(x, y, 6, 6, 0.8, INK) for x, y in [(20, 11), (32, 11), (26, 17), (38, 17)])
    body = path("M20 23H44V29H26V48H20Z", INK)
    block = rrect(29, 32, 15, 16, 1, AMBER)
    return px + body + block


FOOYIN_RIGHT = [(32, 18), (35.5, 12), (37.5, 18), (42.5, 13.5), (42.5, 20), (49, 18), (45.5, 26.5), (49, 30), (43, 33.5), (41, 41.5), (35, 46.5), (32, 45)]


@reg("org.fooyin.fooyin", BLUE_GREY_DARK)
def fooyin():
    right = FOOYIN_RIGHT
    pts = right + [(64 - x, y) for x, y in reversed(right[1:-1])]
    head = poly(pts, INK, 2)
    eyes = (poly([(35, 29), (42.5, 26.5), (40.5, 32)], HOLE, 1.5) +
            poly([(29, 29), (21.5, 26.5), (23.5, 32)], HOLE, 1.5))
    mouth = stroke("M28 38.5L32 36.5L36 38.5", HOLE, 2.2)
    return head + eyes + mouth


@reg("org.freedesktop.Bustle", BLUE_GREY)
def bustle():
    stubs = "".join(line(x, 20, x, 29, INK, 2.6) for x in (19, 32, 45))
    stubs += line(25.5, 29, 25.5, 38, INK, 2.6) + line(38.5, 29, 38.5, 38, INK, 2.6)
    bar = rrect(14, 27.2, 36, 3.6, 1.8, INK)
    dots = "".join(circle(x, y, 5, INK) for x, y in
                   [(19, 19), (32, 19), (45, 19), (25.5, 40), (38.5, 40)])
    return stubs + bar + dots


@reg("org.freedesktop.Piper", BROWN_LIGHT)
def piper():
    frame = f'<rect x="18" y="12" width="28" height="20" rx="2.5" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    spring = "".join(line(x, 26, x, 34, INK, 2.4) for x in (27, 30.5, 34))
    cheese = poly([(22, 38), (44, 34), (44, 47), (22, 47)], AMBER_LIGHT, 2)
    holes = circle(28, 42.5, 2, HOLE) + circle(38, 40, 1.7, HOLE)
    return frame + spring + cheese + holes


@reg("org.freedesktop.Tuhi", BLUE_DARK)
def tuhi():
    pen = poly([(27, 12), (37, 12), (37, 34), (32, 46), (27, 34)], INK, 2.5)
    cutl = line(32, 14, 32, 33, HOLE, 2.2)
    leaf = path("M40 42C40 33 44 28 50 26C50 35 47 40 40 42Z", BLUE_SOFT)
    return pen + cutl + leaf


@reg("org.freedesktop.adriconf", BLUE_GREY_DEEP)
def adriconf():
    d = stroke("M15 17V43H19C25 43 28 38 28 30C28 22 25 17 19 17Z", INK, 4)
    r = stroke("M32 43V17H36.5C40.5 17 42.5 19.5 42.5 23C42.5 26.5 40.5 29 36.5 29H32M36.5 29L42.5 43", INK, 4)
    i = line(48, 17, 48, 43, INK, 4)
    return d + r + i


@reg("org.gabmus.gfeeds", ORANGE_DEEP)
def gfeeds():
    page = rrect(14, 14, 36, 32, 4, INK)
    lines = "".join(rrect(18, y, w, 3, 1.5, HOLE) for y, w in [(19, 12), (25, 10), (31, 12), (37, 9)])
    rss = (circle(35.5, 39, 2.3, HOLE) + stroke(arc_g(35.5, 39, 6.5, -90, 0), HOLE, 2.6) +
           stroke(arc_g(35.5, 39, 11, -90, 0), HOLE, 2.6))
    return page + lines + rss


@reg("org.gabmus.giara", DEEP_ORANGE)
def giara():
    flask = path("M28.5 13H35.5V21C42 23.5 46 28.5 46 34.5C46 42 39.5 47 32 47"
                 "C24.5 47 18 42 18 34.5C18 28.5 22 23.5 28.5 21Z", INK)
    rim = rrect(26, 11, 12, 3.6, 1.8, INK)
    swoosh = stroke("M19.5 34.5C26 29.5 36 38.5 44.5 32.5", HOLE, 2.6)
    return flask + rim + swoosh


@reg("org.gabmus.hydrapaper", CYAN_DARK)
def hydrapaper():
    back = rrect(14, 12, 24, 20, 3, INK)
    mid = rrect(19, 17, 25, 21, 3, CYAN_SOFT, f' stroke="{HOLE}" stroke-width="2"')
    front = path("M27 23H49V39L42 46H27A3 3 0 0 1 24 43V26A3 3 0 0 1 27 23Z", INK,
                 f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    fold = path("M49 39H45A3 3 0 0 0 42 42V46Z", CYAN_SOFT)
    return back + mid + front + fold


def _page(fold):
    sheet = path("M21 12H37L45 20V45A3 3 0 0 1 42 48H21A3 3 0 0 1 18 45V15A3 3 0 0 1 21 12Z", INK)
    return sheet + path("M37 12V17A3 3 0 0 0 40 20H45Z", fold)


@reg("org.gabmus.mdwriter", RED_DEEP)
def mdwriter():
    lines = "".join(rrect(22, y, w, 2.8, 1.4, HOLE) for y, w in [(18, 12), (23.5, 19), (29, 14)])
    m = stroke("M22.5 43V35L26 39L29.5 35V43", HOLE, 2.6)
    arrow = line(36.5, 35, 36.5, 43, HOLE, 2.6) + stroke("M33.5 40L36.5 43L39.5 40", HOLE, 2.6)
    return _page(RED_SOFT) + lines + m + arrow


@reg("org.gabmus.notorious", BLUE_DEEP)
def notorious():
    page = rrect(17, 12, 30, 36, 4, INK)
    chev = stroke("M21.5 15.5L24.5 18.5L21.5 21.5", HOLE, 2.4)
    panel = rrect(21, 25, 22, 19, 2, HOLE)
    lines = "".join(line(24.5, y, 24.5 + w, y, INK, 2.2) for y, w in [(30, 13), (34.5, 15), (39, 9)])
    return page + chev + panel + lines


@reg("org.gabmus.whatip", CYAN_DEEP)
def whatip():
    tag = path("M14 19A4 4 0 0 1 18 15H40L50 30L40 45H18A4 4 0 0 1 14 41Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    hole = circle(43, 30, 2.3, HOLE)
    tree = (rrect(23.5, 17, 7, 7, 1, HOLE) + line(27, 23, 27, 28.5, HOLE, 2.2) +
            stroke("M21 34V28.5H33V34", HOLE, 2.2) +
            rrect(17.5, 33, 7, 7, 1, HOLE) + rrect(29.5, 33, 7, 7, 1, HOLE))
    return tag + hole + tree


@reg("org.gnode.NixView", INDIGO_DEEP)
def nixview():
    return (line(28, 33, 17.5, 43.5, DEEP_ORANGE_SOFT, 5.5) + _ring(35.5, 25.5, 10, INK, 5.5) +
            circle(35.5, 25.5, 5.5, INDIGO_SOFT))


@reg("org.gnome.Adwaita1.Demo", BLUE_DEEP)
def adwaita_demo():
    diamond = g(rrect(17.5, 15.5, 29, 29, 5, INK), "rotate(45 32 30)")
    folds = (poly([(19.5, 30), (32, 30), (32, 42.5)], BLUE_SOFT, 1.5) +
             poly([(32, 17.5), (38.5, 24), (32, 24)], BLUE_SOFT, 1.5))
    return diamond + folds


@reg("org.gnome.Calls", INDIGO_SOFT)
def calls():
    cord = stroke("M40.5 18C42.5 31 36 40.5 22 41.5", INK, 6)
    return cord + ellipse_g(40.5, 18.5, 5.5, 7.5, INK, -8) + ellipse_g(22.5, 40.5, 7.5, 5.5, INK, -8)


@reg("org.gnome.Connections", BLUE_DARK)
def connections():
    globe = circle(28.5, 33, 13.5, INK)
    route = (f'<path d="M18.5 35C22 41.5 30 42 33 36C35 32 38.5 33.5 40 37" fill="none" '
             f'stroke="{HOLE}" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="0 4.2"/>')
    win = rrect(32, 11, 18, 15, 3.5, BLUE_LIGHT, f' stroke="{HOLE}" stroke-width="2.2"')
    cursor = poly([(37.5, 14.5), (45, 19.5), (41.5, 20.2), (39.5, 23.5)], INK, 1.2)
    return globe + route + win + cursor


@reg("org.gnome.Console", BLUE_GREY_DEEP)
def console():
    return stroke("M18 20.5L27.5 29.5L18 38.5", INK, 5) + rrect(31, 35.5, 16, 5, 2.5, INK)


@reg("org.gnome.Crosswords", GREY_DARK)
def crosswords():
    sq = rrect(14, 12, 17, 17, 2.5, INK) + rrect(33, 12, 17, 17, 2.5, INK) + rrect(33, 31, 17, 17, 2.5, INK)
    gl = stroke("M26.5 17.5A5 5 0 1 0 27 23.5H23", HOLE, 2.6)
    nl = stroke("M37.5 25V16L45.5 25V16", HOLE, 2.6)
    return sq + gl + nl


@reg("org.gnome.Decibels", DEEP_PURPLE_LIGHT)
def decibels():
    tri = poly([(20, 14.5), (47.5, 30), (20, 45.5)], INK, 6)
    bars = "".join(line(x, 30 - h, x, 30 + h, HOLE, 2.6) for x, h in
                   [(21.5, 0.01), (25.5, 3), (29.5, 7), (33.5, 3.5), (37.5, 0.01)])
    return tri + bars


@reg("org.gnome.Dictionary", ORANGE_DARK)
def dictionary():
    book = rrect(17, 12, 30, 32, 3.5, INK)
    pages = line(20, 39, 44, 39, HOLE, 2.2)
    ribbon = poly([(35, 43), (41, 43), (41, 49), (38, 46.5), (35, 49)], INK, 1)
    a1 = stroke("M20.5 34L25.5 19L30.5 34M22.3 29H28.7", HOLE, 2.8)
    a2 = _ring(37.5, 29.5, 3.8, HOLE, 2.6) + line(41.3, 25, 41.3, 34, HOLE, 2.6)
    return book + pages + ribbon + a1 + a2


@reg("org.gnome.DiskUtility", GREY_DARK)
def diskutility():
    body = rrect(17, 11, 28, 37, 4.5, INK)
    platter = circle(31, 26, 10, HOLE)
    wrench = (line(31, 26, 46, 43, HOLE, 9) + line(31, 26, 46, 43, INK, 4.6) +
              circle(31, 26, 6, INK) + circle(29.5, 24.5, 2.8, HOLE))
    return body + platter + wrench


@reg("org.gnome.Eolie", BLUE_DEEP)
def eolie():
    pts = []
    for k in range(16):
        a = -90 + 22.5 * k
        r = (17.5 if k % 4 == 0 else 12 if k % 4 == 2 else 7.5)
        pts.append(pt(CX, CY, r, a))
    return poly(pts, INK, 1.5) + circle(CX, CY, 8, HOLE) + circle(CX, CY, 6, INK) + circle(CX, CY, 3, HOLE)


def _globe():
    return (circle(CX, CY, 16.5, INK) +
            f'<ellipse cx="32" cy="30" rx="7" ry="16.5" fill="none" stroke="{HOLE}" stroke-width="2.4"/>' +
            line(15.5, 30, 48.5, 30, HOLE, 2.4))


@reg("org.gnome.Epiphany.Canary", AMBER_DEEP)
@reg("org.gnome.Epiphany", BLUE_DEEP)
def epiphany():
    return _globe()


@reg("org.gnome.Extensions", BLUE_GREY_LIGHT)
def extensions():
    body = rrect(17, 20, 25, 25, 3, INK) + circle(29.5, 17, 4.8, INK) + circle(45, 32.5, 4.8, INK)
    return body + circle(17, 32.5, 3.8, HOLE) + circle(29.5, 45, 3.8, HOLE)


def _fonts():
    a = _ring(22, 21, 4.3, INK, 2.6) + line(26.3, 16.5, 26.3, 25.5, INK, 2.6)
    b = line(36.5, 12, 36.5, 30.5, INK, 4.4) + _ring(41.2, 25.3, 4.6, INK, 4)
    c = stroke("M32 36.5C30.5 34 28 33 25.5 33C20.5 33 17 37.5 17 42C17 45.5 19.5 47.5 23 47.5"
               "C25.5 47.5 27.5 46.5 29 44.5", INK, 3.2)
    return a + b + c


@reg("org.gnome.FontViewer", PURPLE)
@reg("org.gnome.FontManager", GREY_DARK)
def fontmanager():
    return _fonts()


@reg("org.gnome.Fractal", LIGHT_BLUE_DEEP)
def fractal():
    bubble = rrect(15, 12, 34, 29, 7, INK) + poly([(26, 39), (34, 39), (30, 46)], INK, 2)
    d = ""
    for i in range(0, 61):
        th = i * 0.16
        r = 1.2 + 1.35 * th
        x, y = 32 + r * math.cos(th + 1), 26.5 + r * math.sin(th + 1)
        d += ("M" if i == 0 else "L") + f"{f(x)} {f(y)}"
    return bubble + stroke(d, HOLE, 2.6)


@reg("org.gnome.GTG", BLUE_DEEP)
def gtg():
    board = rrect(17, 15, 30, 33, 4, INK)
    clip = rrect(25, 10.5, 14, 8, 2.5, HOLE) + rrect(26.5, 12, 11, 5, 1.5, INK)
    rows = "".join(circle(24.5, y, 2, HOLE) +
                   line(31.5, y, 42, y, HOLE, 2.8) for y in (25, 32.5, 40))
    return board + clip + rows


@reg("org.gnome.Gtranslator", BLUE_GREY)
def gtranslator():
    a = stroke("M15.5 47L21.5 31L27.5 47M17.8 41.5H25.2", INK, 3)
    om = stroke("M36 27.5H39.5C36.5 25.5 35 23 35 20C35 15.5 38 13 42 13C46 13 49 15.5 49 20"
                "C49 23 47.5 25.5 44.5 27.5H48", INK, 2.8)
    arr1 = stroke("M18 26C18 19 23 15 29.5 15", INK, 2.8) + stroke("M26.5 11.5L30 15L26.5 18.5", INK, 2.8)
    arr2 = stroke("M46 33C46 40 41 44.5 34.5 44.5", INK, 2.8) + stroke("M37.5 41L34 44.5L37.5 48", INK, 2.8)
    return a + om + arr1 + arr2


@reg("org.gnome.Keysign", RED_DEEP)
def keysign():
    seal = circle(CX, CY, 13.5, INK) + "".join(
        circle(*pt(CX, CY, 13.2, 18 * k * 2), 4.2, INK) for k in range(10))
    inner = _ring(CX, CY, 10, HOLE, 2.2)
    key = circle(32, 27.5, 3.2, HOLE) + rrect(30.6, 28, 2.8, 8, 1.2, HOLE)
    return seal + inner + key


@reg("org.gnome.Loupe", INDIGO)
def loupe():
    pic = rrect(20, 12, 29, 29, 3.5, INK)
    sun = circle(43, 18, 2.6, HOLE)
    lens = circle(31, 28, 10, HOLE) + circle(31, 28, 7.3, INK)
    handle = line(23.5, 35.5, 16, 43, HOLE, 8) + line(23.5, 35.5, 16, 43, INK, 4.6)
    return pic + sun + lens + handle


@reg("org.gnome.Music", AMBER_DARK)
def music():
    screws = "".join(circle(*pt(CX, CY, 14.4, 45 + 90 * k), 1.5, HOLE) for k in range(4))
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.3, HOLE) + circle(CX, CY, 10, INK) +
            circle(CX, CY, 3.6, HOLE) + screws)


@reg("org.gnome.NetworkDisplays", DEEP_PURPLE_LIGHT)
def networkdisplays():
    mon = rrect(14, 13, 36, 25, 3.5, INK) + rrect(24, 41, 16, 4.5, 2.25, INK) + rrect(30, 37, 4, 5, 0, INK)
    wifi = (circle(32, 32.5, 2.2, HOLE) + stroke(arc_g(32, 33, 6, -135, -45), HOLE, 2.6) +
            stroke(arc_g(32, 33, 11, -135, -45), HOLE, 2.6))
    return mon + wifi


@reg("org.gnome.Notes", AMBER_DEEP)
def notes():
    note = path("M18 13H46A3 3 0 0 1 49 16V36L38 47H18A3 3 0 0 1 15 44V16A3 3 0 0 1 18 13Z", INK)
    fold = path("M49 36H41A3 3 0 0 0 38 39V47Z", AMBER_SOFT)
    bars = rrect(20, 18.5, 24, 5, 1.5, HOLE) + rrect(20, 27, 24, 5, 1.5, HOLE)
    return note + fold + bars


@reg("org.gnome.OfficeRunner", PURPLE_LIGHT)
def officerunner():
    body = (stroke("M33.5 21L29.5 32", INK, 5) +
            stroke("M33 22L26 23.5L24 29.5", INK, 3.6) +
            stroke("M33 22L38 28L43.5 24", INK, 3.6) +
            stroke("M29.5 32L36 37.5L34.5 46", INK, 4) +
            stroke("M29.5 32L24.5 39L16.5 39", INK, 4))
    return body + circle(38.5, 15, 3.8, INK)


@reg("org.gnome.Papers", RED_DEEP)
def papers():
    back = g(rrect(18, 13, 25, 33, 3, RED_SOFT), "rotate(-12 30 30)")
    sheet = path("M23 12H38L46 20V45A3 3 0 0 1 43 48H23A3 3 0 0 1 20 45V15A3 3 0 0 1 23 12Z", INK)
    fold = path("M38 12V17A3 3 0 0 0 41 20H46Z", RED_SOFT)
    lines = (rrect(24, 17, 10, 3.2, 1.6, HOLE) + rrect(24, 22.5, 7, 3.2, 1.6, HOLE) +
             "".join(line(25, y, 41, y, HOLE, 2.4) for y in (30, 35, 40)))
    return back + sheet + fold + lines


@reg("org.gnome.Passbook", AMBER_DARK)
def passbook():
    book = rrect(17, 12, 30, 36, 3.5, INK) + line(22.5, 12, 22.5, 48, HOLE, 2.2) + line(22.5, 43.5, 47, 43.5, HOLE, 2)
    key = (_ring(30, 28, 4.3, HOLE, 3.2) + line(34.3, 28, 43.5, 28, HOLE, 3.2) +
           line(39.5, 28, 39.5, 32.5, HOLE, 2.8) + line(43, 28, 43, 32.5, HOLE, 2.8))
    return book + key


@reg("org.gnome.PasswordSafe", DEEP_PURPLE)
def passwordsafe():
    safe = rrect(16, 13, 32, 34, 4.5, INK)
    hinges = rrect(18.5, 18, 3.4, 7, 1.5, HOLE) + rrect(18.5, 35, 3.4, 7, 1.5, HOLE)
    dial = _ring(34, 30, 8.5, HOLE, 3)
    key = circle(34, 28, 2.4, HOLE) + rrect(32.8, 28, 2.4, 6, 0.8, HOLE)
    return safe + hinges + dial + key


@reg("org.gnome.Photos", DEEP_ORANGE)
def photos():
    outer = poly([pt(CX, CY, 17, -90 + 60 * k) for k in range(6)], INK, 3)
    inner = [pt(CX, CY, 5.5, -90 + 60 * k) for k in range(6)]
    blades = ""
    for k in range(6):
        x0, y0 = inner[k]
        px, py = inner[k - 1]
        dx, dy = x0 - px, y0 - py
        n = math.hypot(dx, dy)
        blades += line(x0, y0, x0 + dx / n * 14, y0 + dy / n * 14, HOLE, 2.2, "butt")
    return outer + blades + poly(inner, HOLE, 1)


@reg("org.gnome.Pinpoint", PURPLE)
def pinpoint():
    screen = rrect(13, 15, 38, 29, 4, INK)
    pointer = poly([(28.5, 44), (28.5, 30), (32, 22), (35.5, 30), (35.5, 44)], HOLE, 1.5)
    return screen + pointer


@reg("org.gnome.Podcasts", RED)
def podcasts():
    tape = rrect(14, 14, 36, 31, 4, INK)
    window = rrect(18, 20.5, 28, 10, 2.5, HOLE)
    reels = circle(24.5, 25.5, 2.8, INK) + circle(39.5, 25.5, 2.8, INK) + rrect(28.5, 23.5, 7, 4, 1, INK)
    foot = poly([(21, 45.2), (24, 37.5), (40, 37.5), (43, 45.2)], HOLE, 1.5)
    return tape + window + reels + foot


@reg("org.gnome.Ptyxis", BLUE_GREY_DARK)
def ptyxis():
    frame = rrect(14, 13, 36, 33, 6, INK)
    return frame + stroke("M20.5 21.5L27.5 28.5L20.5 35.5", HOLE, 4.2) + rrect(31, 34, 12, 4.2, 2.1, HOLE)


@reg("org.gnome.Reversi", AMBER_DARK)
def reversi():
    board = rrect(14, 12, 36, 36, 4.5, INK)
    grid = line(32, 12, 32, 48, HOLE, 2.2) + line(14, 30, 50, 30, HOLE, 2.2)
    discs = (circle(23, 21, 6, HOLE) + circle(41, 39, 6, HOLE) +
             _ring(41, 21, 5, HOLE, 2.4) + _ring(23, 39, 5, HOLE, 2.4))
    return board + grid + discs


@reg("org.gnome.Settings", GREY_DARK)
def settings():
    teeth = "".join(g(rrect(28.5, 12.5, 7, 8, 1.8, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    return teeth + circle(CX, CY, 13, INK) + circle(CX, CY, 6.5, HOLE)


@reg("org.gnome.Shell.CaptivePortal", DEEP_ORANGE_DEEP)
def captiveportal():
    hexa = poly([pt(CX, CY, 17, -90 + 60 * k) for k in range(6)], INK, 4)
    wifi = (circle(32, 36, 2.6, HOLE) + stroke(arc_g(32, 36.5, 7, -140, -40), HOLE, 3) +
            stroke(arc_g(32, 36.5, 12.5, -140, -40), HOLE, 3))
    return hexa + wifi


@reg("org.gnome.Showtime", DEEP_PURPLE_DEEP)
def showtime():
    tri = poly([(20, 14), (47.5, 30), (20, 46)], INK, 5.5)
    arcs = (stroke(arc_g(40, 39.5, 8, 180, 270), HOLE, 2.4) +
            stroke(arc_g(40, 39.5, 14, 180, 270), HOLE, 2.4) + line(17, 39.5, 40, 39.5, HOLE, 2.4))
    return tri + arcs


@reg("org.gnome.SimpleScan", CYAN_DEEP)
def simplescan():
    frame = f'<rect x="19" y="11" width="26" height="38" rx="4" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    paper = rrect(23.5, 15.5, 17, 29, 2, INK)
    bar = rrect(12, 26.5, 40, 8, 4, HOLE) + rrect(13, 28, 38, 5, 2.5, INK)
    return frame + paper + bar


@small("org.fdroid.Repomaker")
def repomaker_s():
    head = rrect(17, 11, 30, 11.5, 5, INK) + circle(25, 16.7, 2.7, HOLE) + circle(39, 16.7, 2.7, HOLE)
    return head + rrect(16, 25, 32, 24, 4.5, INK) + _ring(32, 37, 6, HOLE, 3.6)


@small("org.flozz.yoga-image-optimizer")
def yoga_s():
    ears = (poly([(22, 26), (13, 22), (19.5, 37)], INK, 3) +
            poly([(42, 26), (51, 22), (44.5, 37)], INK, 3))
    return (ears + circle(32, 31, 14, INK) + circle(26.5, 28.5, 3, HOLE) + circle(37.5, 28.5, 3, HOLE) +
            path("M26.5 34.5H37.5A5.5 5.5 0 0 1 26.5 34.5Z", HOLE))


@small("org.fooyin.fooyin")
def fooyin_s():
    right = FOOYIN_RIGHT
    pts = right + [(64 - x, y) for x, y in reversed(right[1:-1])]
    eyes = (poly([(34, 28), (43.5, 25), (41, 33)], HOLE, 2) +
            poly([(30, 28), (20.5, 25), (23, 33)], HOLE, 2))
    return poly(pts, INK, 2) + eyes


@small("org.freedesktop.Bustle")
def bustle_s():
    stubs = "".join(line(x, 20, x, 30, INK, 3) for x in (18, 32, 46))
    stubs += line(25, 30, 25, 40, INK, 3) + line(39, 30, 39, 40, INK, 3)
    dots = "".join(circle(x, y, 6, INK) for x, y in [(18, 18), (32, 18), (46, 18), (25, 41), (39, 41)])
    return stubs + rrect(13, 27.5, 38, 5, 2.5, INK) + dots


@small("org.freedesktop.Piper")
def piper_s():
    frame = f'<rect x="18" y="12" width="28" height="19" rx="2.5" fill="none" stroke="{INK}" stroke-width="4.4"/>'
    return frame + poly([(20, 38), (45, 33), (45, 47), (20, 47)], AMBER_LIGHT, 2)


@small("org.freedesktop.adriconf")
def adriconf_s():
    d = stroke("M15 16V44H19.5C26 44 29 38.5 29 30C29 21.5 26 16 19.5 16Z", INK, 5)
    r = stroke("M35 44V16H40C44.5 16 47 19 47 23C47 27 44.5 30 40 30H35M40 30L47.5 44", INK, 5)
    return d + r


@small("org.gabmus.gfeeds")
def gfeeds_s():
    return (rrect(14, 13, 36, 34, 5, INK) + circle(23, 38, 3.6, HOLE) +
            stroke(arc_g(23, 38, 10.5, -90, 0), HOLE, 4) + stroke(arc_g(23, 38, 18, -90, 0), HOLE, 4))


@small("org.gabmus.mdwriter")
def mdwriter_s():
    m = stroke("M22 42V27L27 34L32 27V42", HOLE, 3.6)
    arrow = line(38.5, 26, 38.5, 42, HOLE, 3.6) + stroke("M34.5 37.5L38.5 42L42.5 37.5", HOLE, 3.6)
    return _page(RED_SOFT) + m + arrow


@small("org.gabmus.notorious")
def notorious_s():
    return (rrect(16, 11, 32, 38, 4.5, INK) + stroke("M21 15L24.5 18.5L21 22", HOLE, 3.4) +
            rrect(20.5, 26, 23, 19, 2.5, HOLE))


@small("org.gabmus.whatip")
def whatip_s():
    tag = path("M14 19A4 4 0 0 1 18 15H40L50 30L40 45H18A4 4 0 0 1 14 41Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    tree = (rrect(22, 17, 10, 8, 1.5, HOLE) + stroke("M21.5 34V29H32.5V34", HOLE, 3) +
            line(27, 24, 27, 29, HOLE, 3) + rrect(17, 33, 9, 9, 1.5, HOLE) + rrect(28, 33, 9, 9, 1.5, HOLE))
    return tag + tree


@small("org.gnome.Connections")
def connections_s():
    globe = circle(28, 34, 14, INK)
    win = rrect(30, 9.5, 21, 18, 4, BLUE_LIGHT, f' stroke="{HOLE}" stroke-width="2.4"')
    return globe + win + poly([(36, 13.5), (46, 19.5), (41.5, 20.5), (39, 25)], INK, 1.5)


@small("org.gnome.Crosswords")
def crosswords_s():
    return (rrect(14, 12, 17, 17, 3, INK) + rrect(33, 12, 17, 17, 3, INK) + rrect(33, 31, 17, 17, 3, INK) +
            rrect(14, 31, 17, 17, 3, GREY))


@small("org.gnome.Decibels")
def decibels_s():
    tri = poly([(20, 14.5), (47.5, 30), (20, 45.5)], INK, 6)
    return tri + "".join(line(x, 30 - h, x, 30 + h, HOLE, 3.4) for x, h in [(23.5, 3), (29.5, 7), (35.5, 3)])


@small("org.gnome.Dictionary")
def dictionary_s():
    book = rrect(17, 11, 30, 33, 4, INK)
    ribbon = poly([(35, 43), (41, 43), (41, 49), (38, 46.5), (35, 49)], INK, 1)
    return book + ribbon + stroke("M23.5 38L32 17L40.5 38M26.3 31H37.7", HOLE, 4.4)


@small("org.gnome.DiskUtility")
def diskutility_s():
    return (rrect(16, 10, 30, 38, 5, INK) + circle(31, 26, 11, HOLE) +
            line(31, 26, 46, 43, HOLE, 11) + line(31, 26, 46, 43, INK, 6) +
            circle(31, 26, 7, INK) + circle(29.5, 24.5, 3.3, HOLE))


@small("org.gnome.Eolie")
def eolie_s():
    pts = [pt(CX, CY, 17.5 if k % 2 == 0 else 7, -90 + 45 * k) for k in range(8)]
    return poly(pts, INK, 2.5) + circle(CX, CY, 6.5, HOLE) + circle(CX, CY, 3.2, INK)


def _globe_s():
    return (circle(CX, CY, 17, INK) +
            f'<ellipse cx="32" cy="30" rx="7" ry="17" fill="none" stroke="{HOLE}" stroke-width="3"/>' +
            line(15, 30, 49, 30, HOLE, 3))


@small("org.gnome.Epiphany.Canary")
@small("org.gnome.Epiphany")
def epiphany_s():
    return _globe_s()


def _fonts_s():
    a = _ring(22.5, 33, 6, INK, 4) + line(28.5, 25.5, 28.5, 40.5, INK, 4)
    b = line(35.5, 14, 35.5, 40.5, INK, 4.6) + _ring(41.5, 33, 6, INK, 4.4)
    return a + b


@small("org.gnome.FontViewer")
@small("org.gnome.FontManager")
def fontmanager_s():
    return _fonts_s()


@small("org.gnome.Fractal")
def fractal_s():
    bubble = rrect(14, 11, 36, 31, 7, INK) + poly([(25, 40), (34, 40), (29.5, 47)], INK, 2)
    d = ""
    for i in range(0, 41):
        th = i * 0.18
        r = 1.5 + 1.75 * th
        x, y = 32 + r * math.cos(th + 1), 26.5 + r * math.sin(th + 1)
        d += ("M" if i == 0 else "L") + f"{f(x)} {f(y)}"
    return bubble + stroke(d, HOLE, 3.4)


@small("org.gnome.GTG")
def gtg_s():
    board = rrect(16, 14, 32, 35, 4.5, INK) + rrect(25, 10, 14, 7, 2.5, INK)
    rows = "".join(circle(24.5, y, 2.6, HOLE) +
                   line(33, y, 43, y, HOLE, 3.6) for y in (26, 38))
    return board + rows


@small("org.gnome.Gtranslator")
def gtranslator_s():
    a = stroke("M14 44L21 25L28 44M16.8 37.5H25.2", INK, 4)
    om = stroke("M34 44H38.5C35 41.5 33.5 38 33.5 34.5C33.5 29 37 25.5 42 25.5C47 25.5 50.5 29 50.5 34.5"
                "C50.5 38 49 41.5 45.5 44H50", INK, 3.6)
    return g(a + om, "translate(0 -3)")


@small("org.gnome.Keysign")
def keysign_s():
    seal = circle(CX, CY, 13.5, INK) + "".join(
        circle(*pt(CX, CY, 13.2, 36 * k), 4.2, INK) for k in range(10))
    return seal + circle(32, 26.5, 4.2, HOLE) + rrect(30, 27, 4, 10, 1.5, HOLE)


@small("org.gnome.Loupe")
def loupe_s():
    pic = rrect(19, 11, 31, 31, 4, INK)
    lens = circle(31, 27, 11, HOLE) + circle(31, 27, 7.3, INK)
    handle = line(23, 35, 15, 44, HOLE, 9) + line(23, 35, 15, 44, INK, 5)
    return pic + lens + handle


@small("org.gnome.Music")
def music_s():
    return circle(CX, CY, 17, INK) + circle(CX, CY, 12, HOLE) + circle(CX, CY, 9.5, INK) + circle(CX, CY, 4, HOLE)


@small("org.gnome.NetworkDisplays")
def networkdisplays_s():
    mon = rrect(13, 12, 38, 27, 4, INK) + rrect(23, 42, 18, 5, 2.5, INK)
    return mon + circle(32, 32, 3, HOLE) + stroke(arc_g(32, 33.5, 9, -135, -45), HOLE, 3.6)


@small("org.gnome.Notes")
def notes_s():
    note = path("M18 13H46A3 3 0 0 1 49 16V36L38 47H18A3 3 0 0 1 15 44V16A3 3 0 0 1 18 13Z", INK)
    return note + path("M49 36H41A3 3 0 0 0 38 39V47Z", AMBER_SOFT) + \
        rrect(19.5, 18.5, 25, 6, 2, HOLE) + rrect(19.5, 28.5, 25, 6, 2, HOLE)


@small("org.gnome.Papers")
def papers_s():
    sheet = path("M22 11H38L47 20V45A3 3 0 0 1 44 48H22A3 3 0 0 1 19 45V14A3 3 0 0 1 22 11Z", INK)
    fold = path("M38 11V17A3 3 0 0 0 41 20H47Z", RED_SOFT)
    return sheet + fold + rrect(23.5, 17, 11, 4.4, 2.2, HOLE) + \
        "".join(line(25, y, 41, y, HOLE, 3.4) for y in (30, 38))


@small("org.gnome.Passbook")
def passbook_s():
    book = rrect(16, 11, 32, 38, 4, INK) + line(21.5, 11, 21.5, 49, HOLE, 2.8)
    key = _ring(30, 30, 5, HOLE, 4) + line(35, 30, 44, 30, HOLE, 4) + line(41, 30, 41, 35.5, HOLE, 3.6)
    return book + key


@small("org.gnome.PasswordSafe")
def passwordsafe_s():
    return (rrect(15, 12, 34, 36, 5, INK) + _ring(32, 30, 9.5, HOLE, 4) +
            circle(32, 28, 3, HOLE) + rrect(30.5, 28, 3, 7, 1, HOLE))


@small("org.gnome.Photos")
def photos_s():
    outer = poly([pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)], INK, 3)
    inner = [pt(CX, CY, 6, -90 + 60 * k) for k in range(6)]
    blades = ""
    for k in range(6):
        x0, y0 = inner[k]
        px, py = inner[k - 1]
        dx, dy = x0 - px, y0 - py
        n = math.hypot(dx, dy)
        blades += line(x0, y0, x0 + dx / n * 14, y0 + dy / n * 14, HOLE, 2.8, "butt")
    return outer + blades + poly(inner, HOLE, 1)


@small("org.gnome.Podcasts")
def podcasts_s():
    return (rrect(13, 13, 38, 33, 4.5, INK) + rrect(17.5, 19.5, 29, 11, 3, HOLE) +
            circle(24.5, 25, 3.2, INK) + circle(39.5, 25, 3.2, INK) +
            poly([(20, 46.2), (23.5, 37.5), (40.5, 37.5), (44, 46.2)], HOLE, 1.5))


@small("org.gnome.Ptyxis")
def ptyxis_s():
    return (rrect(13, 12, 38, 35, 6, INK) + stroke("M20 21L28 28.5L20 36", HOLE, 5) +
            rrect(31, 33, 13, 5, 2.5, HOLE))


@small("org.gnome.Reversi")
def reversi_s():
    board = rrect(13, 11, 38, 38, 5, INK)
    grid = line(32, 11, 32, 49, HOLE, 3) + line(13, 30, 51, 30, HOLE, 3)
    return board + grid + circle(22.5, 20.5, 6.5, HOLE) + circle(41.5, 39.5, 6.5, HOLE)


@small("org.gnome.Shell.CaptivePortal")
def captiveportal_s():
    hexa = poly([pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)], INK, 4)
    return (hexa + circle(32, 37, 3.4, HOLE) + stroke(arc_g(32, 37.5, 8.5, -140, -40), HOLE, 4) +
            stroke(arc_g(32, 37.5, 15, -135, -45), HOLE, 4))


@small("org.gnome.Showtime")
def showtime_s():
    tri = poly([(20, 14), (47.5, 30), (20, 46)], INK, 5.5)
    return tri + stroke(arc_g(40, 40, 11, 180, 270), HOLE, 3.6) + line(17, 40, 40, 40, HOLE, 3.4)


@small("org.gnome.SimpleScan")
def simplescan_s():
    frame = f'<rect x="18.5" y="10.5" width="27" height="39" rx="4.5" fill="none" stroke="{INK}" stroke-width="4.2"/>'
    return frame + rrect(11, 25, 42, 10, 5, HOLE) + rrect(12, 27, 40, 6, 3, INK)
