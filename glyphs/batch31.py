# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 31: gnome-subtitles to gpk-prefs."""
import math
from lm import (
    AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT, BROWN, BROWN_LIGHT, circle, cpath,
    cut, DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_SOFT, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK, INDIGO_SOFT, INK,
    LIGHT_BLUE, LIGHT_BLUE_DARK, line, ORANGE_DARK, ORANGE_DEEP, ORANGE_SOFT, path, PINK_DARK,
    poly, pt, PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DEEP, RED_LIGHT, rrect, stroke,
    TEAL, TEAL_DEEP, YELLOW_DARK,
)
from glyphs.kit import arc, _chrome, _doc, ellipse_d, gear_c, _jb, pie_b, registry, ring_b
from glyphs.kit import shared_lo_writer

ICONS, SMALL, reg, small = registry()


def _grid3(skip=(), centre=None):
    out = ""
    for r in range(3):
        for c in range(3):
            if (c, r) in skip:
                continue
            fill = centre if (c, r) == (1, 1) and centre else INK
            out += rrect(14 + c * 12.5, 12 + r * 12.5, 11, 11, 2.2, fill)
    return out


def _tri(w=3):
    return path("M19.5 14.5L46.5 30L19.5 45.5Z", INK,
                f' stroke="{INK}" stroke-width="{w}" stroke-linejoin="round"')


@reg("gnome-subtitles", BLUE_DEEP)
def subtitles():
    bubble = path("M19 14H45A4 4 0 0 1 49 18V36A4 4 0 0 1 45 40H40L35 46.5L32.5 40H19"
                  "A4 4 0 0 1 15 36V18A4 4 0 0 1 19 14Z", INK)
    lines = "".join(rrect(21, y, w, 3, 1.5, HOLE) for y, w in [(20, 22), (25.5, 22), (31, 15)])
    return bubble + lines


@reg("gnome-sudoku", BLUE_DEEP)
def sudoku():
    three = stroke("M29.4 27.2H34.6L31.8 30.3C33.8 30.3 35 31.3 35 32.8C35 34.3 33.7 35.2 32.1 35.2"
                   "C30.9 35.2 29.9 34.8 29.2 34", HOLE, 2.3)
    return _grid3(centre=INK).replace('fill="INK"', f'fill="{BLUE_LIGHT}"') + rrect(26.5, 24.5, 11, 11, 2.2, INK) + three


@reg("gnome-taquin", BLUE)
def taquin():
    return _grid3(skip=[(0, 2)]) + ring_b(32, 30, 11.5, HOLE, 2.8)


@reg("gnome-tetravex", PURPLE_DEEP)
def tetravex():
    left = poly([(16, 14), (32, 30), (16, 46)], PURPLE_SOFT)
    right = poly([(48, 14), (32, 30), (48, 46)], PURPLE_SOFT)
    body = rrect(16, 14, 32, 32, 3.5, INK) + left + right + line(17, 15, 47, 45, HOLE, 1.6) + line(47, 15, 17, 45, HOLE, 1.6)
    two = g(stroke("M-2.2 -2.1Q-2 -3.5 0 -3.5Q2.3 -3.5 2.3 -1.5Q2.3 0 -2.3 3.5H2.5", HOLE, 2.2),
            "translate(22 30)")
    five = g(stroke("M2.3 -3.5H-1.8L-2.2 -.2Q-1 -.8 0 -.8Q2.5 -.8 2.5 1.3Q2.5 3.5 0 3.5Q-1.5 3.5 -2.4 2.6",
                    HOLE, 2.2), "translate(42 30)")
    six = g(stroke("M1.8 -3.5Q-2.2 -2.8 -2.2 1.3", HOLE, 2.2) + ring_b(0, 1.3, 2.1, HOLE, 2.2),
            "translate(32 20.5)")
    seven = g(stroke("M-2.3 -3.5H2.5L-.3 3.5", HOLE, 2.2), "translate(32 39.5)")
    return body + two + five + six + seven


@reg("gnome-todo", BROWN)
def todo():
    board = rrect(17.5, 15, 29, 33, 4, INK)
    clip = rrect(25, 11.5, 14, 7, 3, INK) + rrect(27.5, 17.5, 9, 2.2, 1.1, HOLE)
    rows = ""
    for y in (26, 33, 40):
        rows += circle(24.5, y, 2, HOLE)
        rows += line(31.5, y, 41.5, y, HOLE, 2.6)
    return board + clip + rows


@reg("gnome-tweak-tool", BLUE_GREY)
def tweak():
    on = rrect(15, 14, 34, 14, 7, INK) + circle(42, 21, 4.6, HOLE)
    off = (rrect(16.3, 33.3, 31.4, 11.4, 5.7, "none", f' stroke="{INK}" stroke-width="2.6"')
           + circle(23, 39, 4.6, INK))
    return on + off


@reg("gnome-twitch", DEEP_PURPLE_LIGHT)
def twitch():
    box = path("M20 13H47V34L39 42H32L26 48V42H17V17Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return box + rrect(28, 21, 3.6, 10, 1.8, HOLE) + rrect(37, 21, 3.6, 10, 1.8, HOLE)


@reg("gnome-twofactorauth", BLUE_GREY_DEEP)
def twofactor():
    shackle = stroke("M24.5 27V21A7.5 7.5 0 0 1 39.5 21V27", INK, 4.4)
    body = circle(32, 34.5, 12.5, INK) + circle(32, 34.5, 8, HOLE)
    needle = poly([pt(32, 34.5, 2.6, 135), pt(27, 29.5, 0, 0), pt(32, 34.5, 2.6, -45)], RED_LIGHT, 1.2)
    return shackle + body + needle + circle(32, 34.5, 2.8, RED_LIGHT)


@reg("gnome-video-arcade", AMBER_DEEP)
def video_arcade():
    cab = rrect(19, 11.5, 26, 37, 3.5, INK)
    marquee = line(19, 17.5, 45, 17.5, HOLE, 1.8, "butt")
    screen = rrect(23, 21, 18, 12.5, 2, HOLE)
    panel = line(19, 37.5, 45, 37.5, HOLE, 1.8, "butt")
    ctrl = circle(26, 42.5, 2.3, HOLE) + circle(33, 42.5, 1.7, HOLE) + circle(38, 42.5, 1.7, HOLE)
    return cab + marquee + screen + panel + ctrl


@reg("gns3", DEEP_PURPLE_DEEP)
def gns3():
    body = path("M15 34C15 24 23 17 33 16L41 15.5C46 15.5 49.5 18.5 49.5 22.5C49.5 26.5 46.5 28.5 43 28.5"
                "H39.5C37.5 33 33 36.5 28 37C23 37.5 19 36.5 15 34Z", INK)
    eye = circle(41.5, 21.5, 5, HOLE) + circle(42.2, 21.5, 2.5, INK)
    tail = stroke("M16.5 33C15.5 41 20.5 46.5 27 46.5C32.5 46.5 35.5 43 34 40C32.8 37.8 29.5 38.3 29.5 41", INK, 4)
    return body + eye + tail


@reg("gnubg", LIGHT_BLUE_DARK)
def gnubg():
    pts = ""
    for k in range(5):
        x = 14.5 + k * 7
        c = INK if k % 2 == 0 else RED_LIGHT
        pts += poly([(x, 12), (x + 7, 12), (x + 3.5, 19.5)], c, 1)
        c2 = RED_LIGHT if k % 2 == 0 else INK
        pts += poly([(x, 48), (x + 7, 48), (x + 3.5, 40.5)], c2, 1)
    gnu = stroke("M25.2 25.5A5 5.3 0 1 0 25.8 31H22.6M29.2 35.3V24.7L35.2 35.3V24.7"
                 "M39.2 24.7V31.8A3.5 3.5 0 0 0 46.2 31.8V24.7", INK, 2.6)
    return pts + gnu


@reg("gnumeric", BLUE_DEEP)
def gnumeric():
    sheet = rrect(16, 16, 32, 28, 3.5, INK)
    cells = "".join(rrect(19 + c * 9.2, 19 + r * 8, 7.6, 6.2, 1, HOLE)
                    for r in range(3) for c in range(3))
    return sheet + cells


@reg("gnvim", TEAL_DEEP)
def gnvim():
    return stroke("M44 17.5H24.5L19 23V37L24.5 42.5H39.5L45 37V30H33.5", INK, 5.6)


@reg("goa-account-ubuntusso", DEEP_ORANGE_DEEP)
def ubuntusso():
    u = stroke("M21.5 15.5V31.5A10.5 10.5 0 0 0 42.5 31.5V15.5", INK, 6)
    one = stroke("M29 21.5L32.5 18V35", INK, 3.6)
    return u + one


GODOT_HEAD = circle(22.5, 19.5, 5, INK) + circle(32, 17, 5, INK) + circle(41.5, 19.5, 5, INK) + rrect(14, 19, 36, 21, 8, INK) + rrect(17, 33, 30, 13, 4, INK)


@reg("godot", BLUE_DEEP)
def godot():
    head = (GODOT_HEAD)
    eyes = ""
    for x in (24, 40):
        eyes += circle(x, 29, 6, HOLE) + circle(x, 29, 4.6, INK) + circle(x + .6, 29.5, 2.2, HOLE)
    mouth = stroke("M17 39.5H24V42.5H28V39.5H36V42.5H40V39.5H47", HOLE, 1.8)
    return head + eyes + mouth


@reg("gogland", TEAL)
def gogland():
    go = (stroke("M28.7 20.3A6 6 0 1 0 30.5 24.5H26.5", HOLE, 3.4) + ring_b(39.5, 24.5, 5.6, HOLE, 3.4))
    return _jb(go)


@reg("goland", INDIGO)
def goland():
    return gogland()


@reg("golly", AMBER_DEEP)
def golly():
    cells = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    glider = "".join(rrect(19 + c * 9, 17 + r * 9, 8, 8, 1.8, INK) for c, r in cells)
    frame = rrect(14.5, 12.5, 35, 35, 5, "none", f' stroke="{INK}" stroke-width="2.4" stroke-dasharray="3 2.4"')
    return frame + glider


@reg("goobox", BLUE_GREY)
def goobox():
    disc = cut(cpath(29.5, 28, 15.5) + cpath(29.5, 28, 3.5), INK) + ring_b(29.5, 28, 7, HOLE, 1.6)
    badge = circle(42, 40, 9, HOLE) + circle(42, 40, 7.5, PURPLE_SOFT)
    note = (circle(40.5, 43, 2.3, INK) + line(42.3, 43, 42.3, 35.8, INK, 1.8, "butt")
            + stroke("M42.3 36Q44.5 36.5 45 38.5", INK, 1.8))
    return disc + badge + note


@reg("goodvibes", ORANGE_DEEP)
def goodvibes():
    body = rrect(14, 16, 36, 29, 5, INK)
    tuner = rrect(18.5, 20.5, 27, 4.5, 2.25, HOLE) + rrect(30, 19.5, 3, 6.5, 1.2, RED)
    speaker = circle(24, 35.5, 5.5, HOLE)
    dots = "".join(circle(35.5 + c * 4.6, 31 + r * 4.6, 1.6, HOLE) for r in range(3) for c in range(3))
    return body + tuner + speaker + dots


@reg("google", BLUE)
def google():
    return stroke("M41.4 20.6A13.3 13.3 0 1 0 45.3 30H32.5", INK, 5.6)


@reg("google-agenda", BLUE)
def google_agenda():
    cal = path("M20 14H44A5 5 0 0 1 49 19V39L41 47H20A5 5 0 0 1 15 42V19A5 5 0 0 1 20 14Z", INK)
    fold = poly([(41.5, 39.5), (48.5, 39.5), (41.5, 46.5)], BLUE_SOFT, 1)
    three = stroke("M22.5 23.5H29.2L26 27.8C28.2 27.8 29.8 29.1 29.8 31.4C29.8 33.8 28 35.2 25.7 35.2"
                   "C24.2 35.2 23 34.6 22.2 33.6", HOLE, 3)
    one = stroke("M35 26L38.5 23.5V35.5", HOLE, 3)
    return cal + fold + three + one


@reg("google-chat", BLUE_DEEP)
def google_chat():
    back = path("M28 13H46A4 4 0 0 1 50 17V29A4 4 0 0 1 46 33H44V38L39 33H28A4 4 0 0 1 24 29V17"
                "A4 4 0 0 1 28 13Z", BLUE_SOFT)
    front = path("M19 20H34A4 4 0 0 1 38 24V36A4 4 0 0 1 34 40H22L15 46.5V24A4 4 0 0 1 19 20Z", INK,
                 f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    return back + front


@reg("google-chrome-beta", BLUE_DEEP)
def chrome_beta():
    logo = g(_chrome(), "translate(32 23.5) scale(.68) translate(-32 -30)")
    band = rrect(16.5, 37.5, 31, 11.5, 4, INK)
    beta = stroke("M20.5 40.5V46H23.2Q24.9 46 24.9 44.6Q24.9 43.2 23.2 43.2H20.5M20.5 40.5H22.9"
                  "Q24.5 40.5 24.5 41.85Q24.5 43.2 22.9 43.2M31.4 40.5H27.6V46H31.4M27.6 43.25H30.6"
                  "M33.4 40.5H38.4M35.9 40.5V46M40 46L42.5 40.5L45 46M41 44H44", HOLE, 2)
    return logo + band + beta


@reg("google-chrome-unstable", RED_DEEP)
def chrome_unstable():
    return _chrome()


@reg("google-contacts", BLUE_DEEP)
def google_contacts():
    head = circle(32, 20, 7.5, INK)
    body = path("M17 44C17 36 23 31 32 31C41 31 47 36 47 44Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return head + body


@reg("google-docs", BLUE)
def google_docs():
    return shared_lo_writer()


@reg("google-drive", BROWN_LIGHT)
def google_drive():
    edge = f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"'
    left = path("M26.5 13L32 22.5L20 43.5L14.5 34Z", INK, edge)
    right = path("M26.5 13H37.5L49.5 34H38.5Z", INK, edge)
    bottom = path("M26 34H49.5L44 43.5H20.5Z", INK, edge)
    return left + right + bottom


@reg("google-earth-pro", BLUE_DEEP)
def google_earth():
    globe = circle(32, 30, 16, INK)
    swoosh = (stroke("M18 37C22 27 33 20.5 45 21.5", HOLE, 2.4) +
              stroke("M22.5 43C27 34.5 36.5 29.5 47.5 30.5", HOLE, 2.4))
    return globe + swoosh


@reg("google-maps", RED_DEEP)
def google_maps():
    pin = path("M32 48C27 41 18 33 18 25A14 14 0 0 1 46 25C46 33 37 41 32 48Z", INK)
    return pin + circle(32, 25, 5.5, HOLE)


@reg("google-meet", ORANGE_DARK)
def google_meet():
    body = path("M21 18H35A3 3 0 0 1 38 21V39A3 3 0 0 1 35 42H17A3 3 0 0 1 14 39V25Z", INK)
    lens = path("M38 26L46.5 19.5C48 18.4 50 19.4 50 21.2V38.8C50 40.6 48 41.6 46.5 40.5L38 34Z", INK)
    return body + lens + rrect(20.5, 24.5, 11, 11, 1.5, HOLE)


@reg("google-photos", DEEP_ORANGE_DEEP)
def google_photos():
    petal = path("M32 30H15.5A8.25 8.25 0 0 1 32 30Z", INK)
    alt = path("M32 30H15.5A8.25 8.25 0 0 1 32 30Z", DEEP_ORANGE_SOFT)
    return "".join(g(petal if k % 2 == 0 else alt, f"rotate({90 * k} 32 30)") for k in range(4))


@reg("google-play", TEAL)
def google_play():
    cuts = stroke("M19.5 14.5L36 30L19.5 45.5M41 26.6L36 30L41 33.4", HOLE, 1.8)
    return _tri() + cuts


@reg("google-play-music-desktop-player", DEEP_ORANGE)
def gpmdp():
    return _tri(4) + circle(29, 30, 7.5, HOLE) + circle(29, 30, 4, INK)


@reg("google-slides", AMBER_DEEP)
def google_slides():
    frame = rrect(21.5, 26, 21, 15, 2.5, HOLE) + rrect(24.5, 29, 15, 9, 1, INK)
    return _doc(frame, AMBER_SOFT)


@reg("google-tasks-desktop", BLUE)
def google_tasks():
    return (circle(32, 30, 16, INK) + line(29, 37, 41.5, 23.5, HOLE, 4.6)
            + circle(23, 31, 3, HOLE))


@reg("google-translate", BLUE)
def google_translate():
    back = rrect(29, 19, 21, 28, 4, BLUE_SOFT)
    wen = (line(40.5, 27, 40.5, 28.8, BLUE_DARK, 2.4) + line(35, 31, 46, 31, BLUE_DARK, 2.4)
           + stroke("M37 34Q40.5 40.5 46 43.2M44.5 34Q41.5 40.5 36 43.2", BLUE_DARK, 2.4))
    front = rrect(14, 13, 23, 25, 4, INK, f' stroke="{HOLE}" stroke-width="1.8"')
    gg = stroke("M29 21.6A5.3 5.3 0 1 0 30.8 25.7H25.8", HOLE, 2.8)
    return back + wen + front + gg


@reg("google-webdesigner", ORANGE_DEEP)
def google_webdesigner():
    sep = f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"'
    q = (pie_b(32, 30, 15.5, 90, 180, INK, sep) + pie_b(32, 30, 15.5, 180, 270, INK, sep)
         + pie_b(32, 30, 15.5, 0, 90, INK, sep) + pie_b(34, 28, 13.5, 270, 360, ORANGE_SOFT, sep))
    return q + circle(32, 30, 6.5, HOLE) + circle(32, 30, 4, INK)


@reg("gootool", PURPLE_LIGHT)
def gootool():
    ball = circle(32, 31, 15.5, INK)
    eyes = ""
    for x in (25, 39):
        eyes += circle(x, 25, 5, HOLE) + circle(x + .8, 25.8, 2.2, INK)
    return ball + eyes


@reg("goterminal", PINK_DARK)
def goterminal():
    dollar = g(stroke("M27 18.5C26 17.5 24.5 17 23 17C20.5 17 19 18.2 19 20C19 24 27.5 22.5 27.5 27"
                      "C27.5 29 25.5 30 23 30C21 30 19.5 29.4 18.5 28.3", AMBER_SOFT, 2.8)
               + line(23, 14.5, 23, 32.5, AMBER_SOFT, 2.6), "translate(0 7.5)")
    return dollar + rrect(32, 36.5, 14, 4, 2, INK)


@reg("gottet", BLUE_DARK)
def gottet():
    def cell(c, r, col):
        return rrect(15 + c * 8.7, 13 + r * 8.7, 7.6, 7.6, 1.6, col)
    out = "".join(cell(c, r, INK) for c, r in [(0, 0), (1, 0), (0, 1), (1, 1)])
    out += "".join(cell(c, r, RED_LIGHT) for c, r in [(2, 1), (1, 2), (2, 2), (3, 2)])
    out += "".join(cell(c, r, BLUE_SOFT) for c, r in [(0, 2), (0, 3), (1, 3), (2, 3)])
    return out


@reg("goverlay", GREY_DARK)
def goverlay():
    front = rrect(16.5, 14.5, 23, 23, 2.5, "none", f' stroke="{INK}" stroke-width="3.2"')
    backs = stroke("M44 21V41.5H23", INK, 3.2) + stroke("M49 26V46.5H28", INK, 3.2)
    return front + backs


def _cube(cx, cy, s):
    w, h = s * .87, s / 2
    edge = f' stroke="{HOLE}" stroke-width="1" stroke-linejoin="round"'
    top = path(f"M{f(cx)} {f(cy - h)}L{f(cx + w)} {f(cy)}L{f(cx)} {f(cy + h)}L{f(cx - w)} {f(cy)}Z", INK, edge)
    left = path(f"M{f(cx - w)} {f(cy)}L{f(cx)} {f(cy + h)}L{f(cx)} {f(cy + h + s)}L{f(cx - w)} {f(cy + s)}Z",
                INDIGO_SOFT, edge)
    right = path(f"M{f(cx + w)} {f(cy)}L{f(cx)} {f(cy + h)}L{f(cx)} {f(cy + h + s)}L{f(cx + w)} {f(cy + s)}Z",
                 INDIGO, edge)
    return top + left + right


@reg("goxel", INDIGO_DARK)
def goxel():
    return _cube(24.5, 31.5, 8.6) + _cube(39.5, 31.5, 8.6) + _cube(32, 18.5, 8.6)


@reg("gp", YELLOW_DARK)
def gp():
    return (pie_b(17.5, 45.5, 30, 270, 360, INK) + pie_b(17.5, 45.5, 20, 270, 360, RED_DEEP)
            + pie_b(17.5, 45.5, 10, 270, 360, BLUE_GREY_DARK))


@reg("gpa", BLUE_GREY)
def gpa():
    def key(col):
        return (ring_b(32, 18, 6.2, col, 3.8) + line(32, 24.2, 32, 46, col, 3.8)
                + line(32, 38, 37, 38, col, 3.4) + line(32, 43.5, 36, 43.5, col, 3.4))
    return g(key(BLUE_GREY_SOFT), "rotate(-28 32 30)") + g(key(INK), "rotate(28 32 30)")


@reg("gpaint", DEEP_PURPLE_DEEP)
def gpaint():
    puddle = ellipse_d(28, 45.5, 13, 2.8, PURPLE_SOFT)
    handle = line(47.5, 12.5, 36.5, 25.5, INK, 4.4)
    ferrule = line(37, 25, 32.5, 30, DEEP_PURPLE_SOFT, 6, "butt")
    tip = path("M29.5 28L35 33.5C32 39 27 43 20 45C21 38 25 32 29.5 28Z", INK)
    return puddle + handle + ferrule + tip


@reg("gparted", BLUE_GREY_DEEP)
def gparted():
    disc = circle(32, 30, 16, INK)
    platter = circle(32, 30, 11, HOLE) + pie_b(32, 30, 11, -90, 150, INK) + circle(32, 30, 3, HOLE)
    arm = line(19.5, 43.5, 27, 36, HOLE, 3)
    return disc + g(platter, "") + arm


@reg("gpdftext", GREY_DARK)
def gpdftext():
    pencil = (line(38.5, 25.5, 27.5, 36.5, HOLE, 5, "butt")
              + poly([(29.3, 38.3), (25.7, 34.7), (24.3, 39.7)], HOLE, 1))
    return _doc(pencil, GREY_SOFT)


@reg("gpk-log", ORANGE_SOFT)
def gpk_log():
    arrow = line(24, 13, 24, 32, INK, 4.6) + poly([(16.5, 30), (31.5, 30), (24, 39)], INK, 2.2)
    card = rrect(33, 30, 16, 18, 3, INK)
    lines = "".join(line(36.5, y, 45.5, y, HOLE, 2.2) for y in (35, 39, 43))
    return arrow + card + lines


def _arrow_arc(cx, cy, r, a0, a1, col, w):
    ex, ey = pt(cx, cy, r, a1)
    t = math.radians(a1)
    tx, ty = -math.sin(t), math.cos(t)
    nx, ny = math.cos(t), math.sin(t)
    head = poly([(ex + 4.5 * tx, ey + 4.5 * ty), (ex + 4 * nx, ey + 4 * ny), (ex - 4 * nx, ey - 4 * ny)], col, 1.5)
    return stroke(arc(cx, cy, r, a0, a1), col, w) + head


@reg("gpk-prefs", ORANGE_DEEP)
def gpk_prefs():
    arrows = _arrow_arc(32, 30, 14, 200, 320, INK, 3.6) + _arrow_arc(32, 30, 14, 20, 140, INK, 3.6)
    return arrows + gear_c(32, 30, 5.2, INK, HOLE)


@small("gnome-tetravex")
def tetravex_s():
    return (rrect(16, 14, 32, 32, 3.5, INK) + poly([(16, 14), (32, 30), (16, 46)], PURPLE_SOFT)
            + poly([(48, 14), (32, 30), (48, 46)], PURPLE_SOFT)
            + line(17, 15, 47, 45, HOLE, 2) + line(47, 15, 17, 45, HOLE, 2))


@small("gnome-sudoku")
def sudoku_s():
    return _grid3(centre=INK).replace('fill="INK"', f'fill="{BLUE_LIGHT}"') + rrect(26.5, 24.5, 11, 11, 2.2, INK)


@small("gnome-taquin")
def taquin_s():
    return _grid3(skip=[(0, 2)])


@small("gnome-todo")
def todo_s():
    board = rrect(17, 14, 30, 34, 4, INK) + rrect(25, 11, 14, 6, 3, INK)
    rows = "".join(circle(25.5, y, 2.2, HOLE) + line(33, y, 42, y, HOLE, 2.6)
                   for y in (26, 38))
    return board + rows


@small("gnome-tweak-tool")
def tweak_s():
    return (rrect(15, 13, 34, 15, 7.5, INK) + circle(41.5, 20.5, 5, HOLE)
            + rrect(15, 32, 34, 15, 7.5, BLUE_GREY_SOFT) + circle(22.5, 39.5, 5, INK))


@small("gnome-twofactorauth")
def twofactor_s():
    return (stroke("M24.5 27V21A7.5 7.5 0 0 1 39.5 21V27", INK, 4) + circle(32, 34.5, 13, INK)
            + circle(32, 34.5, 7, HOLE) + circle(32, 34.5, 4, RED_LIGHT))


@small("gnome-video-arcade")
def video_arcade_s():
    return (rrect(18, 11, 28, 38, 4, INK) + rrect(22, 18, 20, 15, 2.5, HOLE)
            + circle(26, 41, 2.8, HOLE) + circle(36, 41, 2.8, HOLE))


@small("gnubg")
def gnubg_s():
    out = ""
    for k in range(4):
        x = 14 + k * 9
        out += poly([(x, 13), (x + 9, 13), (x + 4.5, 26)], INK if k % 2 == 0 else RED_LIGHT, 1.5)
        out += poly([(x, 47), (x + 9, 47), (x + 4.5, 34)], RED_LIGHT if k % 2 == 0 else INK, 1.5)
    return out


@small("gnumeric")
def gnumeric_s():
    return rrect(15, 14, 34, 32, 4, INK) + "".join(
        rrect(19 + c * 14, 18 + r * 13, 12, 11, 1.5, HOLE) for r in range(2) for c in range(2))


@small("godot")
def godot_s():
    head = (GODOT_HEAD)
    eyes = circle(24, 29, 5.5, HOLE) + circle(40, 29, 5.5, HOLE)
    return head + eyes + line(19, 41, 45, 41, HOLE, 2.4)


def _go_s():
    return (rrect(14, 12, 36, 36, 4, INK)
            + stroke("M28.3 18.8A7 7 0 1 0 30 26H25", HOLE, 2.8) + ring_b(40.5, 26, 6.2, HOLE, 2.8)
            + rrect(19, 39, 14, 4, 2, HOLE))


@small("goland")
@small("gogland")
def gogland_s():
    return _go_s()


@small("golly")
def golly_s():
    cells = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    return "".join(rrect(15 + c * 12, 13 + r * 12, 10, 10, 2, INK) for c, r in cells)


@small("goobox")
def goobox_s():
    return (cut(cpath(30, 28.5, 16.5) + cpath(30, 28.5, 4), INK)
            + circle(42, 40, 9.5, HOLE) + circle(42, 40, 7.5, LIGHT_BLUE))


@small("goodvibes")
def goodvibes_s():
    body = rrect(14, 15, 36, 31, 5, INK)
    dots = "".join(circle(37 + c * 7, 32 + r * 7, 2.4, HOLE) for r in range(2) for c in range(2))
    return body + rrect(18, 19, 28, 5, 2.5, HOLE) + circle(24.5, 35.5, 6, HOLE) + dots


@small("google-agenda")
def google_agenda_s():
    cal = path("M20 14H44A5 5 0 0 1 49 19V39L41 47H20A5 5 0 0 1 15 42V19A5 5 0 0 1 20 14Z", INK)
    return cal + stroke("M22 21.5H29.5L26 26.3C28.5 26.3 30.3 27.8 30.3 30.4C30.3 33.1 28.2 34.6 25.7 34.6"
                        "C24 34.6 22.7 34 21.8 33M36 24L40 21V35", HOLE, 2.8)


@small("google-chrome-beta")
def chrome_beta_s():
    return g(_chrome(), "translate(32 24.5) scale(.78) translate(-32 -30)") + rrect(17, 40, 30, 7.5, 3.75, INK)


@small("google-translate")
def google_translate_s():
    back = rrect(28, 19, 22, 29, 4, BLUE_SOFT) + stroke("M35 33H46M37 36Q41 42 46 44M45 36Q41 42 36 44", BLUE_DARK, 2.4)
    front = rrect(13, 12, 25, 26, 4, INK, f' stroke="{HOLE}" stroke-width="2"')
    return back + front + stroke("M30.5 20.5A6 6 0 1 0 32 25.5H26.5", HOLE, 2.6)


@small("google-webdesigner")
def google_webdesigner_s():
    sep = f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"'
    return (pie_b(32, 30, 16, 90, 180, INK, sep) + pie_b(32, 30, 16, 180, 270, INK, sep)
            + pie_b(32, 30, 16, 0, 90, INK, sep) + pie_b(34, 28, 14, 270, 360, ORANGE_SOFT, sep))


@small("gootool")
def gootool_s():
    return circle(32, 31, 16, INK) + circle(24.5, 26, 5.5, HOLE) + circle(39.5, 26, 5.5, HOLE)


@small("goxel")
def goxel_s():
    return _cube(32, 20, 15)


@small("gpa")
def gpa_s():
    key = (ring_b(32, 18, 6.5, INK, 4) + line(32, 24.5, 32, 46, INK, 4)
           + line(32, 39, 38, 39, INK, 4))
    return g(key, "rotate(28 32 30)")


@small("gparted")
def gparted_s():
    return (circle(32, 30, 16.5, INK) + circle(32, 30, 11, HOLE) + pie_b(32, 30, 11, -90, 150, INK)
            + circle(32, 30, 3, HOLE))


@small("gpk-log")
def gpk_log_s():
    arrow = line(23, 12, 23, 30, INK, 5) + poly([(14.5, 28), (31.5, 28), (23, 38)], INK, 2.5)
    card = rrect(32, 29, 18, 19, 3, INK)
    return arrow + card + line(36, 35, 46, 35, HOLE, 2.6) + line(36, 42, 46, 42, HOLE, 2.6)


@small("gpk-prefs")
def gpk_prefs_s():
    return (_arrow_arc(32, 30, 13.5, 200, 320, INK, 3.4) + _arrow_arc(32, 30, 13.5, 20, 140, INK, 3.4)
            + circle(32, 30, 4.5, INK))
