# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 30: git tools, gmail and the first run of gnome-* apps.

Same kit and rules as batch01: palette tile, mark in INK, HOLE for
cut-outs, mostly one colour.
"""
from lm import (
    AMBER_DARK, AMBER_DEEP, AMBER_SOFT, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_SOFT, circle, cut, CX, CY, CYAN_DARK, CYAN_DEEP,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE_DEEP, DEEP_PURPLE_SOFT,
    f, g, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DEEP, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP,
    line, ORANGE_DARK, ORANGE_DEEP, ORANGE_LIGHT, ORANGE_SOFT, path, PINK, poly, pt, PURPLE,
    PURPLE_DEEP, PURPLE_SOFT, RED, RED_DEEP, RED_SOFT, rrect, stroke, TEAL, TEAL_DEEP,
    YELLOW_LIGHT,
)
from glyphs.kit import _gear, registry, _ring, _star_b

ICONS, SMALL, reg, small = registry()


@reg("gitahead", CYAN_DARK)
def gitahead():
    dart = poly([(48, 12), (19, 23), (30, 30), (37, 46)], INK, 2.5)
    traces = (stroke("M28 33L21.5 37.5", INK, 2.4) + circle(19.5, 39, 2.6, INK) +
              stroke("M31.5 36L27.5 43", INK, 2.4) + circle(26.5, 45, 2.6, INK) +
              stroke("M25 31H18.5", INK, 2.4) + circle(16.5, 31, 2.6, INK))
    return dart + traces


@reg("gitblade", AMBER_DEEP)
def gitblade():
    diamond = g(rrect(17.5, 15.5, 29, 29, 6, INK), "rotate(45 32 30)")
    tree = (line(28, 21.5, 28, 38.5, HOLE, 2.8) +
            stroke("M28 27C28 30 30 31 37 31", HOLE, 2.8) +
            circle(28, 21.5, 3.2, HOLE) + circle(28, 38.5, 3.2, HOLE) + circle(37.5, 31, 3.2, HOLE))
    return diamond + tree


@reg("giteye", BLUE_DEEP)
def giteye():
    lens = rrect(14, 12, 27, 27, 7, INK)
    graph = (stroke("M20.5 20.5L27.5 27.5L34.5 20.5M27.5 27.5V33", HOLE, 2.6) +
             circle(20.5, 20.5, 2.8, HOLE) + circle(34.5, 20.5, 2.8, HOLE) + circle(27.5, 33, 2.8, HOLE))
    handle = line(38, 36, 47.5, 45.5, INK, 6.5)
    return lens + graph + handle


@reg("gitg", BLUE_GREY_DARK)
def gitg():
    left = stroke("M26 12V20C26 23 21 24 21 28V36C21 40 26 41 26 44V48", INK, 3.4)
    mid = line(32, 12, 32, 48, AMBER_SOFT, 3.4)
    right = stroke("M38 12V26C38 29 43 30 43 33V48", RED_SOFT, 3.4)
    nodes = (circle(21, 32, 3.8, INK) + circle(21, 32, 1.6, HOLE) +
             circle(32, 17, 3.8, AMBER_SOFT) + circle(32, 17, 1.6, HOLE) +
             circle(43, 36, 3.8, RED_SOFT) + circle(43, 36, 1.6, HOLE))
    return left + mid + right + nodes


def _octocat():
    head = path("M19 26C19 23 19.8 20.6 21 18.8L20.5 12.5C23.5 12.8 26.3 14.3 28 16"
                "C29.3 15.7 30.6 15.6 32 15.6C33.4 15.6 34.7 15.7 36 16"
                "C37.7 14.3 40.5 12.8 43.5 12.5L43 18.8C44.2 20.6 45 23 45 26"
                "C45 32.5 40 36 32 36C24 36 19 32.5 19 26Z", INK)
    neck = path("M27 34C27 39 26.5 43 25 47.5H39C37.5 43 37 39 37 34Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    tail = stroke("M26.5 42.5C21.5 43 21 38.5 16.5 38", INK, 3)
    return head + neck + tail


@reg("github-desktop", PURPLE_DEEP)
@reg("github", BLUE_GREY_DARK)
def github():
    return _octocat()


@reg("gitify", INDIGO_DEEP)
def gitify():
    return stroke("M43 18.5A14 14 0 1 0 46 31.5H34.5", INK, 6.2)


@reg("gitkraken", TEAL)
def gitkraken():
    a0, a1 = pt(CX, CY, 16, 125), pt(CX, CY, 16, 55)
    ring = stroke(f"M{f(a0[0])} {f(a0[1])}A16 16 0 1 1 {f(a1[0])} {f(a1[1])}", INK, 3)
    head = path("M32 16C36.5 16 39.5 19.5 39.5 24.5C39.5 28.5 37.5 31 36 32H28"
                "C26.5 31 24.5 28.5 24.5 24.5C24.5 19.5 27.5 16 32 16Z", INK)
    eyes = circle(28.8, 27, 1.7, HOLE) + circle(35.2, 27, 1.7, HOLE)
    arms = (stroke("M28.5 31.5C27.5 37 25 40 21 40.5", INK, 2.6) +
            stroke("M35.5 31.5C36.5 37 39 40 43 40.5", INK, 2.6) +
            stroke("M30.8 32V45", INK, 2.4) + stroke("M33.2 32V45", INK, 2.4))
    return ring + head + eyes + arms


@reg("gitlab", DEEP_ORANGE_DEEP)
def gitlab():
    body = poly([(32, 46), (15, 33.5), (20.5, 13.5), (25.5, 27), (38.5, 27),
                 (43.5, 13.5), (49, 33.5)], INK, 2.8)
    face = poly([(25.5, 27), (38.5, 27), (32, 46)], DEEP_ORANGE_SOFT, 1.5)
    return body + face


@reg("gitqlient", DEEP_ORANGE_LIGHT)
def gitqlient():
    stem = stroke("M31.5 47V34C31.5 31 32 29.5 33.5 28", INK, 3.2)
    left = path("M31 34.5C23.5 35.5 17.5 31 17 23.5C24 23 30 27 31 34.5Z", INK)
    right = path("M33 29.5C32.5 20.5 38.5 14 47 13C47.5 22 42 28.5 33 29.5Z", INK)
    return stem + left + right


@reg("gitter", PINK)
def gitter():
    return (line(19.5, 14, 19.5, 34, INK, 4.6) + line(27.8, 23, 27.8, 46, INK, 4.6) +
            line(36.2, 23, 36.2, 46, INK, 4.6) + line(44.5, 23, 44.5, 37, INK, 4.6))


@reg("gittyup", BLUE_DARK)
def gittyup():
    lines = stroke("M39 15L27 31L38 32L46 22", INK, 3.2)
    nodes = circle(27, 31, 3.8, INK) + circle(38, 32, 3.8, INK) + circle(46, 22, 3.8, INK)
    return lines + nodes + _star_b(20, 41, 6.5, AMBER_SOFT)


@reg("gksu", RED)
def gksu():
    return (circle(32, 20.5, 7, INK) +
            path("M18 44C18 35.5 24 30.5 32 30.5C40 30.5 46 35.5 46 44Z", INK,
                 f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"'))


@reg("glabels-3.0", ORANGE_DEEP)
def glabels():
    out = ""
    for r in range(3):
        for c in range(2):
            x, y = 15 + c * 18, 13 + r * 12
            out += (rrect(x, y, 16, 10, 2.5, INK) +
                    rrect(x + 3, y + 2.8, 9, 1.9, .95, HOLE) + rrect(x + 3, y + 5.6, 6, 1.9, .95, HOLE))
    return out


@reg("glade", ORANGE_DARK)
def glade():
    page = rrect(22, 11, 25, 32, 3.5, ORANGE_LIGHT)
    square = cut("M15 17V47H45Z" + "M20.5 30V41.5H32Z", INK)
    return page + square


@reg("gladish", LIGHT_BLUE)
def gladish():
    plate = (f'<ellipse cx="32" cy="39.5" rx="16" ry="7.5" fill="none" '
             f'stroke="{INK}" stroke-width="3"/>')
    head = '<ellipse cx="30" cy="39" rx="5.2" ry="3.4" fill="INK"/>'
    note = line(34.5, 38.5, 34.5, 13, INK, 3) + stroke("M35 13.5C39 15 41.5 18.5 41 23", INK, 3)
    return plate + head + note


@reg("glob2-icon", BLUE_DEEP)
def glob2():
    arms = "".join(line(31, 30, x, y, INK, 3.6)
                   for x, y in [(21, 17), (42, 18), (18, 35), (24, 44), (41, 42)])
    blobs = (circle(31, 30, 7.5, INK) + circle(21, 17, 4.5, INK) + circle(42, 18, 6.5, INK) +
             circle(18, 35, 4, INK) + circle(24, 44, 4.2, INK) + circle(41, 42, 5.5, INK))
    return arms + blobs


@reg("glyphr-studio-desktop", LIGHT_BLUE_DEEP)
def glyphr():
    bowl = _ring(31.5, 24.5, 8, INK, 5.6)
    tail = stroke("M39.5 24V33C39.5 40 35.5 44 30 44C26.5 44 24 42.8 22.5 41", INK, 5.6)
    return bowl + tail


def _gmail():
    return stroke("M17 44V20L32 32L47 20V44", INK, 6)


@reg("gmail-offline", GREY_DEEP)
@reg("gmail", RED)
def gmail():
    return _gmail()


@reg("gmic_qt", DEEP_PURPLE_DEEP)
def gmic_qt():
    crown = poly([(21, 21), (37, 21), (35.5, 40), (22.5, 40)], INK, 2.5)
    band = rrect(22, 33, 14, 3.4, .5, HOLE)
    brim = rrect(15, 40, 28, 5.5, 2.75, INK)
    return crown + band + brim + _star_b(43.5, 17, 6.5, INK) + _star_b(46, 30.5, 3.8, INK, .8)


@reg("gmtpicon", BLUE_DEEP)
def gmtpicon():
    body = rrect(20, 11, 24, 38, 5.5, INK)
    screen = rrect(23.5, 14.5, 17, 13, 2.5, HOLE)
    wheel = circle(32, 38.5, 7, HOLE) + circle(32, 38.5, 4, INK)
    return body + screen + wheel


@reg("gnac", PURPLE_SOFT)
def gnac():
    gear = _gear(32, 30, 17, 13, 8, INK, .5) + circle(32, 30, 9.5, HOLE)
    note = (circle(29.5, 34, 3.2, INK) + line(32.2, 34, 32.2, 23.5, INK, 2.4) +
            stroke("M32.2 23.5C35 24.5 36.5 26.5 36 29", INK, 2.4))
    return gear + note


@reg("gngeo", INDIGO)
def gngeo():
    out = ""
    for (cx, cy), c in [((24, 22), INK), ((40, 22), YELLOW_LIGHT), ((24, 38), YELLOW_LIGHT), ((40, 38), INK)]:
        out += circle(cx, cy, 8, c) + circle(cx, cy, 2.6, HOLE)
    return out


@reg("gnome-2048", ORANGE_DEEP)
def gnome_2048():
    sq = (rrect(15.5, 12.5, 15.5, 15.5, 3, INK) + rrect(33, 12.5, 15.5, 15.5, 3, ORANGE_SOFT) +
          rrect(15.5, 30, 15.5, 15.5, 3, INK) + rrect(33, 30, 15.5, 15.5, 3, INK))
    two = stroke("M19.8 17.8C20.5 16.6 21.8 16 23.2 16C25.2 16 26.6 17.2 26.6 19"
                 "C26.6 21 24 22.6 20 24.3H27", HOLE, 2.4)
    four = stroke("M25.3 41.5V34L19.6 39.2H27.2", HOLE, 2.4)
    eight = _ring(40.75, 35.2, 2.4, HOLE, 2.3) + _ring(40.75, 40.5, 2.9, HOLE, 2.3)
    return sq + two + four + eight


@reg("gnome-appfolders-manager", ORANGE_DARK)
def appfolders():
    panel = rrect(17, 12, 30, 36, 5, INK)
    cells = "".join(rrect(x, y, 8.5, 8, 1.8, HOLE)
                    for x, y in [(21.5, 16.5), (34, 16.5), (21.5, 27.5), (34, 27.5), (21.5, 38.5)])
    return panel + cells


@reg("gnome-boxes", BLUE_GREY_DEEP)
def gnome_boxes():
    o = [(19, 17), (45, 17), (45, 43), (19, 43)]
    i = [(26.5, 24.5), (37.5, 24.5), (37.5, 35.5), (26.5, 35.5)]
    frame = stroke("M19 17H45V43H19Z", INK, 3)
    inner = stroke("M26.5 24.5H37.5V35.5H26.5Z", INK, 2.4)
    diag = "".join(line(a[0], a[1], b[0], b[1], INK, 2.4) for a, b in zip(o, i))
    dots = "".join(circle(x, y, 4.6, INK) for x, y in o) + "".join(circle(x, y, 2.8, INK) for x, y in i)
    return frame + inner + diag + dots


@reg("gnome-break-timer", BLUE_GREY_DEEP)
def break_timer():
    face = circle(CX, CY, 16.5, INK) + circle(CX, CY, 12, HOLE)
    ticks = "".join(line(*pt(CX, CY, 13.6, a), *pt(CX, CY, 15.2, a), HOLE, 2.2, "butt")
                    for a in (-90, 0, 90, 180))
    hand = line(CX, CY, 37.5, 20.5, INK, 3.6) + circle(CX, CY, 3.2, INK)
    return face + ticks + hand


@reg("gnome-calculator", BLUE_GREY)
def gnome_calculator():
    body = rrect(18, 11, 28, 38, 5, INK)
    display = rrect(21.5, 14.5, 21, 7.5, 2, HOLE)
    keys = "".join(circle(x, y, 2.6, HOLE) for x in (25, 32) for y in (28, 35, 42))
    eq = rrect(36.5, 25.4, 5.2, 19.2, 2.6, DEEP_ORANGE_LIGHT)
    return body + display + keys + eq


@reg("gnome-characters", BLUE_DEEP)
def gnome_characters():
    sq = "".join(rrect(x, y, 16, 16, 3.5, INK) for x in (15, 33) for y in (12, 30))
    a = stroke("M18.5 24.5L23 15.5L27.5 24.5M20.2 21.3H25.8", HOLE, 2.3)
    face = (circle(41, 20, 5.2, HOLE) + circle(39.2, 19, 1, INK) + circle(42.8, 19, 1, INK) +
            stroke("M39 21.8C40.2 23 41.8 23 43 21.8", INK, 1.2))
    clover = "".join(circle(23 + dx, 38 + dy, 2.6, HOLE) for dx, dy in [(0, -2.6), (2.6, 0), (0, 2.6), (-2.6, 0)])
    wave = stroke("M36 39.5C37.5 36.5 39.5 36.5 41 38.5C42.5 40.5 44.5 40.5 46 37.5", HOLE, 2.3)
    return sq + a + face + clover + wave


@reg("gnome-chess", BLUE_GREY)
def gnome_chess():
    knight = path("M17.5 42.5C17.5 37 21 34 23.5 30.5C21 31.5 18.5 31 16.8 29.2L17.5 25"
                  "C20 21 23.5 17.5 26.8 16.2L26.2 12L30 14.8C36.5 15.8 40.5 22 39.5 31"
                  "C39 35.5 38.5 39 38.5 42.5Z", INK)
    base = rrect(14.5, 42, 27, 5.5, 2, INK)
    eye = circle(25.5, 21.8, 1.5, HOLE)
    pawn = (circle(41, 27.5, 5, GREY_SOFT) +
            path("M34.5 47.5C34.5 41.5 37.5 38 39 33.5H43C44.5 38 47.5 41.5 47.5 47.5Z", GREY_SOFT))
    outline = (f'<g stroke="{HOLE}" stroke-width="3" stroke-linejoin="round">' +
               circle(41, 27.5, 5, HOLE) +
               path("M34.5 47.5C34.5 41.5 37.5 38 39 33.5H43C44.5 38 47.5 41.5 47.5 47.5Z", HOLE) + "</g>")
    return knight + base + eye + outline + pawn


@reg("gnome-color-chooser", ORANGE_DEEP)
def color_chooser():
    bulb = rrect(26, 7, 12, 17, 6, INK)
    collar = rrect(21.5, 23, 21, 5, 2.5, INK)
    tube = path("M28 28H36V43L32 50L28 43Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    liquid = rrect(30.3, 31, 3.4, 11, 1.7, ORANGE_SOFT)
    return g(bulb + collar + tube + liquid, "rotate(45 32 30)")


@reg("gnome-commander", BLUE_GREY)
def gnome_commander():
    win = rrect(14, 13, 36, 34, 5, INK)
    bar = rrect(14, 19.5, 36, 2.4, 0, HOLE)
    split = rrect(30.8, 21, 2.4, 26, 0, HOLE)
    rows = "".join(rrect(x, y, w, 2.4, 1.2, HOLE)
                   for x in (18, 36.5) for y, w in [(26, 9), (31.5, 7), (37, 9)])
    return win + bar + split + rows


@reg("gnome-contacts", BLUE_DEEP)
def gnome_contacts():
    tabs = (rrect(40, 15, 7.5, 8, 2.5, BLUE_SOFT) + rrect(40, 25, 7.5, 8, 2.5, ORANGE_SOFT) +
            rrect(40, 35, 7.5, 8, 2.5, DEEP_ORANGE_LIGHT))
    book = rrect(16, 11, 28, 38, 4.5, INK)
    at = (_ring(30, 30, 3.7, HOLE, 2.6) +
          stroke("M33.7 26.2V31.5C33.7 34.2 37.8 34.2 37.8 30A7.8 7.8 0 1 0 34.5 36.4", HOLE, 2.6))
    return tabs + book + at


@reg("gnome-do", PURPLE)
def gnome_do():
    return _gear(32, 30, 17, 13, 8, INK, .55) + circle(32, 30, 7.5, HOLE)


@reg("gnome-firmware", CYAN_DEEP)
def gnome_firmware():
    pins = ""
    for k in range(4):
        v = 23.5 + k * 5.7
        pins += (line(v, 13, v, 18, INK, 2.4) + line(v, 42, v, 47, INK, 2.4) +
                 line(15, v - 1, 20, v - 1, INK, 2.4) + line(44, v - 1, 49, v - 1, INK, 2.4))
    chip = rrect(21, 17.5, 22, 25, 3.5, INK)
    core = rrect(25.5, 22, 13, 16, 2, HOLE) + rrect(28.5, 25, 7, 10, 1.5, INK)
    return pins + chip + core


@reg("gnome-klotski", ORANGE_DEEP)
def gnome_klotski():
    return (rrect(32.5, 12, 17, 17, 3, INK) + rrect(14.5, 30, 17, 17, 3, INK) +
            rrect(18, 15, 10.5, 10.5, 2.5, INK) + rrect(36, 34, 10.5, 10.5, 2.5, INK))


@reg("gnome-layout-switcher", TEAL_DEEP)
def layout_switcher():
    return (stroke("M15.5 35L21.5 41L26.5 34.8", INK, 3.4) + _ring(32, 30, 6.5, INK, 3.4) +
            stroke("M37.2 25L42.5 19.5L48.5 25", INK, 3.4))


@reg("gnome-logs", BLUE_GREY)
def gnome_logs():
    sheet = path("M22 15H41L47 21V44A3 3 0 0 1 44 47H22A3 3 0 0 1 19 44V18A3 3 0 0 1 22 15Z", INK)
    rows = "".join(rrect(x, y, w, 2.6, 1.3, HOLE) for x, y, w in
                   [(36, 24, 7), (36, 29.5, 7), (23, 35, 20), (23, 40.5, 14)])
    lens = circle(27, 25, 9.5, HOLE) + _ring(27, 25, 6.8, INK, 3) + line(21.8, 30.2, 15.5, 36.5, INK, 4.6)
    return sheet + rows + lens


@reg("gnome-mahjongg", AMBER_DARK)
def gnome_mahjongg():
    tiles = rrect(14.5, 13, 17, 34, 4, INK) + rrect(32.5, 13, 17, 34, 4, INK)
    che = (stroke("M18.5 19.5H27.5M19.8 24.5H26.2V33.5H19.8ZM19.8 29H26.2M23 16.5V42M18.5 38H27.5", HOLE, 2.2))
    quan = (stroke("M35.5 26.5H46.5M41 18.5V26.5C41 33 39 38 35.5 41.5M41.3 28C42.5 34 44.5 38 47 40.5", HOLE, 2.2) +
            circle(45, 20.5, 1.6, HOLE))
    return tiles + che + quan


@reg("gnome-mastermind", BLUE_GREY_DEEP)
def gnome_mastermind():
    cols = [INK, AMBER_SOFT, RED_SOFT, GREY_SOFT]
    out = circle(19, 17.5, 4.4, GREY_SOFT) + circle(27.5, 17.5, 1.8, INK) + circle(33.5, 17.5, 1.8, INK)
    out += circle(40.5, 17.5, 4.4, INK)
    for r, shift in [(1, 0), (2, 2)]:
        for c in range(4):
            out += circle(19 + c * 8.7, 17.5 + r * 11, 4.4, cols[(c + shift) % 4])
    return out


@reg("gnome-mines", BLUE_GREY_DEEP)
def gnome_mines():
    sq = (rrect(15, 12, 16.5, 16.5, 3, INK) + rrect(32.5, 12, 16.5, 16.5, 3, BLUE_GREY_SOFT) +
          rrect(15, 30, 16.5, 16.5, 3, INK) + rrect(32.5, 30, 16.5, 16.5, 3, INK))
    flag = line(20.5, 15.5, 20.5, 25, HOLE, 2.4) + poly([(21, 15.5), (27.5, 18.5), (21, 21.5)], HOLE, 1.5)
    one = stroke("M20.5 35.5L23.5 33.5V43M20.5 43H26.5", HOLE, 2.4)
    mine = (circle(40.75, 38.25, 4.2, HOLE) +
            "".join(line(*pt(40.75, 38.25, 3, a), *pt(40.75, 38.25, 6.3, a), HOLE, 2)
                    for a in range(0, 360, 45)))
    return sq + flag + one + mine


@reg("gnome-mplayer", DEEP_PURPLE_SOFT)
def gnome_mplayer():
    play = poly([(25, 14), (25, 34), (42, 24)], INK, 3.5)
    track = line(17, 43, 47, 43, INK, 2.6) + circle(36, 43, 4, INK)
    return play + track


@reg("gnome-mpv", BLUE_DEEP)
def gnome_mpv():
    film = cut("M19 12H45A4 4 0 0 1 49 16V44A4 4 0 0 1 45 48H19A4 4 0 0 1 15 44V16A4 4 0 0 1 19 12Z"
               "M23 15.5H41V44.5H23Z", INK)
    perfs = "".join(rrect(x, y, 3, 3.2, .8, HOLE) for x in (17.5, 43.5) for y in (16, 22.5, 29, 35.5, 42))
    btn = circle(32, 26, 7, INK) + poly([(30, 22.5), (30, 29.5), (35.5, 26)], HOLE, 1)
    slider = line(26, 39, 38, 39, INK, 2.4) + circle(29, 39, 2.6, INK)
    return film + perfs + btn + slider


@reg("gnome-nibbles", DEEP_ORANGE_DEEP)
def gnome_nibbles():
    cloud = (rrect(14, 24, 36, 20, 9, INK) + circle(27, 24.5, 9.5, INK) + circle(39, 27, 7, INK))
    snake = stroke("M41.5 23.5H29.5V30.5H41.5V37.5H22.5", HOLE, 3)
    return cloud + snake


@reg("gnome-pie", TEAL)
def gnome_pie():
    out = ""
    for k, r in enumerate([5.2, 4, 5, 3.6, 4.6, 3.8]):
        x, y = pt(CX, CY, 12, -60 + 60 * k)
        out += circle(x, y, r, INK if k != 0 else AMBER_SOFT)
    return out


@reg("gnome-power-statistics", AMBER_DEEP)
def power_stats():
    disc_ = circle(30, 27.5, 15, INK)
    bolt = poly([(31, 15), (22, 29.5), (29, 29.5), (27, 40), (37, 25), (30, 25)], HOLE, 1.2)
    badge = circle(41.5, 39.5, 9, HOLE) + circle(41.5, 39.5, 7, INK)
    info = circle(41.5, 36, 1.5, HOLE) + line(41.5, 39, 41.5, 43.3, HOLE, 2.6)
    return disc_ + bolt + badge + info


@reg("gnome-ppp", RED_DEEP)
def gnome_ppp():
    handset = (stroke("M17 21C22 14.5 42 14.5 47 21", INK, 5) +
               rrect(13.5, 19, 10, 6, 3, INK) + rrect(40.5, 19, 10, 6, 3, INK))
    body = poly([(24, 25), (40, 25), (45.5, 44), (18.5, 44)], INK, 3.5)
    dial = _ring(32, 35, 5.5, HOLE, 2.8) + line(34.5, 37.5, 37, 40, HOLE, 2.8)
    return handset + body + dial


@reg("gnome-robots", RED_DEEP)
def gnome_robots():
    head = circle(CX, CY, 16.5, INK)
    band = rrect(13.5, 24, 37, 12, 3, HOLE)
    eyes = "".join(circle(x, 30, 3.4, INK) for x in (24, 32, 40))
    return head + band + eyes


@reg("gnome-schedule", ORANGE_DEEP)
def gnome_schedule():
    face = circle(CX, CY, 16.5, INK)
    hands = (stroke("M25 23L32 30L39.5 22.5", HOLE, 3) + line(32, 30, 32, 42, HOLE, 1.8) +
             circle(CX, CY, 2.4, HOLE))
    return face + hands


@small("gitblade")
def gitblade_s():
    diamond = g(rrect(17, 15, 30, 30, 6, INK), "rotate(45 32 30)")
    return (diamond + line(28, 21, 28, 39, HOLE, 3.6) + stroke("M28 27C28 30.5 30.5 31.5 37 31.5", HOLE, 3.6) +
            circle(28, 21, 4, HOLE) + circle(28, 39, 4, HOLE) + circle(38, 31.5, 4, HOLE))


@small("giteye")
def giteye_s():
    graph = (stroke("M21 20.5L27.5 27L34 20.5M27.5 27V33.5", HOLE, 3.4) +
             circle(21, 20.5, 3.6, HOLE) + circle(34, 20.5, 3.6, HOLE) + circle(27.5, 33.5, 3.6, HOLE))
    return rrect(13, 11, 29, 29, 7, INK) + graph + line(39, 37, 48, 46, INK, 7.5)


@small("gitg")
def gitg_s():
    return (line(21, 12, 21, 48, INK, 4.4) + line(32, 12, 32, 48, AMBER_SOFT, 4.4) +
            line(43, 12, 43, 48, RED_SOFT, 4.4) + circle(21, 34, 5, INK) +
            circle(32, 20, 5, AMBER_SOFT) + circle(43, 38, 5, RED_SOFT))


@small("gitkraken")
def gitkraken_s():
    a0, a1 = pt(CX, CY, 17, 125), pt(CX, CY, 17, 55)
    ring = stroke(f"M{f(a0[0])} {f(a0[1])}A17 17 0 1 1 {f(a1[0])} {f(a1[1])}", INK, 3.2)
    head = path("M32 15C37.5 15 40.5 19 40.5 24.5C40.5 29 38.5 31.5 37 33H27"
                "C25.5 31.5 23.5 29 23.5 24.5C23.5 19 26.5 15 32 15Z", INK)
    arms = (stroke("M28 32C27 38 24.5 41 20 41.5", INK, 3.4) +
            stroke("M36 32C37 38 39.5 41 44 41.5", INK, 3.4) + line(32, 32, 32, 46, INK, 3.4))
    return ring + head + circle(28.5, 26.5, 2.2, HOLE) + circle(35.5, 26.5, 2.2, HOLE) + arms


@small("gittyup")
def gittyup_s():
    return (stroke("M39 14L26 30L38 32L46 21", INK, 4) + circle(26, 30, 4.6, INK) +
            circle(38, 32, 4.6, INK) + circle(46, 21, 4.6, INK) + _star_b(20, 41, 8, AMBER_SOFT, 2))


@small("glabels-3.0")
def glabels_s():
    return "".join(rrect(x, y, 16, 16, 3, INK) + rrect(x + 3.5, y + 6.5, 9, 3, 1.5, HOLE)
                   for x in (15, 33) for y in (13, 31))


@small("gladish")
def gladish_s():
    plate = (f'<ellipse cx="32" cy="40" rx="17" ry="7.5" fill="none" '
             f'stroke="{INK}" stroke-width="3.4"/>')
    head = '<ellipse cx="29.5" cy="39.5" rx="6" ry="4" fill="INK"/>'
    return plate + head + line(34.5, 39, 34.5, 13, INK, 3.4) + stroke("M35 13.5C39.5 15 42 18.5 41.5 23.5", INK, 3.4)


@small("gmic_qt")
def gmic_qt_s():
    crown = poly([(19, 19), (37, 19), (35.5, 39), (20.5, 39)], INK, 2.5)
    return crown + rrect(13, 39, 30, 7, 3.5, INK) + _star_b(44.5, 20, 7.5, INK, 2)


@small("gnac")
def gnac_s():
    gear = _gear(32, 30, 18, 14, 8, INK, .5) + circle(32, 30, 10.5, HOLE)
    return gear + circle(29, 34.5, 4, INK) + line(32.4, 34.5, 32.4, 22.5, INK, 3)


@small("gngeo")
def gngeo_s():
    return "".join(circle(cx, cy, 8.8, c) for (cx, cy), c in
                   [((23, 21), INK), ((41, 21), YELLOW_LIGHT), ((23, 39), YELLOW_LIGHT), ((41, 39), INK)])


@small("gnome-2048")
def gnome_2048_s():
    return (rrect(14.5, 11.5, 16.5, 16.5, 3, INK) + rrect(33, 11.5, 16.5, 16.5, 3, ORANGE_SOFT) +
            rrect(14.5, 30, 16.5, 16.5, 3, INK) + rrect(33, 30, 16.5, 16.5, 3, INK))


@small("gnome-boxes")
def gnome_boxes_s():
    o = [(18, 16), (46, 16), (46, 44), (18, 44)]
    return (stroke("M18 16H46V44H18Z", INK, 3.4) + "".join(circle(x, y, 5.6, INK) for x, y in o) +
            rrect(26, 24, 12, 12, 2, INK))


@small("gnome-break-timer")
def break_timer_s():
    return (circle(CX, CY, 17, INK) + circle(CX, CY, 12, HOLE) +
            line(CX, CY, 38, 20, INK, 4.2) + circle(CX, CY, 3.8, INK))


@small("gnome-calculator")
def gnome_calculator_s():
    return (rrect(17, 10, 30, 40, 5, INK) + rrect(21, 14, 22, 9, 2, HOLE) +
            "".join(rrect(x, y, 6.5, 6.5, 2, HOLE) for x in (21, 29.5) for y in (28, 38)) +
            rrect(38, 28, 5.5, 16.5, 2.75, DEEP_ORANGE_LIGHT))


@small("gnome-characters")
def gnome_characters_s():
    sq = "".join(rrect(x, y, 17, 17, 3.5, INK) for x in (14, 33) for y in (11, 30))
    return (sq + stroke("M18 24.5L22.5 15L27 24.5", HOLE, 3) + circle(41.5, 19.5, 4.6, HOLE) +
            stroke("M22.5 34V43.5M17.8 38.7H27.2", HOLE, 3) +
            stroke("M36 40C37.8 36.5 40 36.5 41.5 38.5C43 40.5 45 40.5 46.8 37", HOLE, 3))


@small("gnome-chess")
def gnome_chess_s():
    knight = path("M19 42.5C19 37 22.5 34 25 30.5C22.5 31.5 20 31 18.3 29.2L19 25"
                  "C21.5 21 25 17.5 28.3 16.2L27.7 12L31.5 14.8C38 15.8 42 22 41 31"
                  "C40.5 35.5 40 39 40 42.5Z", INK)
    return knight + rrect(16, 42, 27, 6, 2.5, INK)


@small("gnome-color-chooser")
def color_chooser_s():
    body = (rrect(25, 7, 14, 17, 7, INK) + rrect(20.5, 22.5, 23, 6, 3, INK) +
            path("M27 28H37V42L32 49.5L27 42Z", INK, f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"'))
    return g(body, "rotate(45 32 30)")


@small("gnome-commander")
def gnome_commander_s():
    return (rrect(13, 12, 38, 36, 5, INK) + rrect(13, 19.5, 38, 3.4, 0, HOLE) +
            rrect(30.3, 21, 3.4, 27, 0, HOLE))


@small("gnome-contacts")
def gnome_contacts_s():
    tabs = rrect(40, 15, 9, 9, 2.5, BLUE_SOFT) + rrect(40, 26, 9, 9, 2.5, ORANGE_SOFT) + rrect(40, 37, 9, 9, 2.5, DEEP_ORANGE_LIGHT)
    return tabs + rrect(15, 10, 29, 40, 4.5, INK) + _ring(29.5, 30, 6.5, HOLE, 3.4) + circle(29.5, 30, 2.2, HOLE)


@small("gnome-firmware")
def gnome_firmware_s():
    pins = ""
    for v in (23, 32, 41):
        pins += (line(v, 12, v, 18, INK, 3.2) + line(v, 42, v, 48, INK, 3.2) +
                 line(14, v - 2, 20, v - 2, INK, 3.2) + line(44, v - 2, 50, v - 2, INK, 3.2))
    return pins + rrect(19.5, 16.5, 25, 27, 3.5, INK) + rrect(25, 22, 14, 16, 2, HOLE)


@small("gnome-layout-switcher")
def layout_switcher_s():
    return (stroke("M14.5 35L21 41.5L26 34.5", INK, 4) + _ring(32, 30, 7, INK, 4) +
            stroke("M37.5 24.5L43 19L49.5 25", INK, 4))


@small("gnome-logs")
def gnome_logs_s():
    sheet = path("M22 14H41L48 21V45A3 3 0 0 1 45 48H22A3 3 0 0 1 19 45V17A3 3 0 0 1 22 14Z", INK)
    rows = rrect(23, 36, 21, 3.6, 1.8, HOLE) + rrect(36, 28, 8, 3.6, 1.8, HOLE)
    lens = circle(27, 24, 10.5, HOLE) + _ring(27, 24, 7, INK, 4) + line(21.5, 29.5, 15, 36, INK, 6)
    return sheet + rows + lens


@small("gnome-mahjongg")
def gnome_mahjongg_s():
    tiles = rrect(13.5, 12, 18, 36, 4, INK) + rrect(32.5, 12, 18, 36, 4, INK)
    che = stroke("M22.5 16.5V43.5M18 20H27M19 25.5H26V33.5H19ZM18 39H27", HOLE, 2.8)
    quan = stroke("M35.5 26H47.5M41.5 17.5V26C41.5 33.5 39 38.5 35.5 42M41.8 28C43 34.5 45 38.5 47.5 41.5", HOLE, 2.8)
    return tiles + che + quan


@small("gnome-mastermind")
def gnome_mastermind_s():
    cols = [INK, AMBER_SOFT, RED_SOFT, GREY_SOFT, INK, AMBER_SOFT]
    return "".join(circle(20 + (k % 3) * 12, 23.5 + (k // 3) * 13, 5.6, cols[k]) for k in range(6))


@small("gnome-mines")
def gnome_mines_s():
    sq = (rrect(14, 11, 17, 17, 3, INK) + rrect(33, 11, 17, 17, 3, BLUE_GREY_SOFT) +
          rrect(14, 30, 17, 17, 3, INK) + rrect(33, 30, 17, 17, 3, INK))
    flag = line(19.5, 14.5, 19.5, 25, HOLE, 3) + poly([(20, 14.5), (27.5, 18), (20, 21.5)], HOLE, 1.5)
    return sq + flag + circle(41.5, 38.5, 5.5, HOLE)


@small("gnome-mplayer")
def gnome_mplayer_s():
    return (poly([(24, 12), (24, 34), (43, 23)], INK, 3.5) + line(16, 43, 48, 43, INK, 3.4) +
            circle(36, 43, 5, INK))


@small("gnome-mpv")
def gnome_mpv_s():
    film = cut("M19 11H45A4 4 0 0 1 49 15V45A4 4 0 0 1 45 49H19A4 4 0 0 1 15 45V15A4 4 0 0 1 19 11Z"
               "M23.5 14.5H40.5V45.5H23.5Z", INK)
    perfs = "".join(rrect(x, y, 3.5, 5, 1, HOLE) for x in (17.25, 43.25) for y in (16, 27.5, 39))
    return film + perfs + poly([(28, 22), (28, 38), (38.5, 30)], INK, 2.5)


@small("gnome-nibbles")
def gnome_nibbles_s():
    cloud = rrect(13, 23, 38, 22, 10, INK) + circle(27, 24, 10.5, INK) + circle(40, 27, 7.5, INK)
    return cloud + stroke("M42 23H29V31H42V38.5H22", HOLE, 3.8)


@small("gnome-power-statistics")
def power_stats_s():
    disc_ = circle(30, 27, 16, INK)
    bolt = poly([(31.5, 14), (21.5, 29.5), (29, 29.5), (26.5, 41), (38, 24.5), (30.5, 24.5)], HOLE, 1.5)
    badge = circle(42, 40, 10, HOLE) + circle(42, 40, 8, INK) + line(42, 36.5, 42, 43.5, HOLE, 3.2)
    return disc_ + bolt + badge


@small("gnome-ppp")
def gnome_ppp_s():
    handset = stroke("M16 21C21.5 14 42.5 14 48 21", INK, 6) + rrect(12.5, 18.5, 11, 7, 3.5, INK) + rrect(40.5, 18.5, 11, 7, 3.5, INK)
    body = poly([(23.5, 24.5), (40.5, 24.5), (46.5, 45), (17.5, 45)], INK, 3.5)
    return handset + body + _ring(32, 35.5, 5.8, HOLE, 3.4)


@small("gnome-robots")
def gnome_robots_s():
    return (circle(CX, CY, 17, INK) + rrect(12.5, 23, 39, 14, 3.5, HOLE) +
            "".join(circle(x, 30, 4.2, INK) for x in (23, 32, 41)))


@small("gnome-schedule")
def gnome_schedule_s():
    return circle(CX, CY, 17, INK) + stroke("M24.5 22.5L32 30L40 22", HOLE, 3.8)
