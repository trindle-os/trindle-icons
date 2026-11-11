# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 52: GNOME Circle and design tools, GTK demos, KDE Merkuro and friends."""
import math
from lm import (
    AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, BLUE_LIGHT, BLUE_SOFT, BROWN, circle, cpath, cut, CX, CY, CYAN_DEEP,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_SOFT, DEEP_PURPLE, f, g, GREY_DARK, GREY_DEEP, HOLE, INDIGO,
    INDIGO_DARK, INDIGO_LIGHT, INK, LIGHT_BLUE_DEEP, line, ORANGE, ORANGE_DARK, ORANGE_DEEP,
    path, PINK_DEEP, PINK_SOFT, poly, pt, PURPLE, PURPLE_DEEP, RED, RED_DEEP, RED_SOFT, rrect,
    stroke, TEAL, TEAL_DARK, TEAL_DEEP,
)
from glyphs.kit import arc_h, registry, _ring, star_g

ICONS, SMALL, reg, small = registry()


def heart(cx, cy, s, colour):
    d = ("M0 3.4C-1.2 2.5-4.2 .6-4.2-1.6A2.2 2.2 0 0 1 0-2.6"
         "A2.2 2.2 0 0 1 4.2-1.6C4.2 .6 1.2 2.5 0 3.4Z")
    return g(path(d, colour), f"translate({f(cx)} {f(cy)}) scale({f(s)})")


def arrow_r(cx, cy, s, colour, w):
    return (line(cx - s, cy, cx + s, cy, colour, w) +
            stroke(f"M{f(cx)} {f(cy - s)}L{f(cx + s)} {f(cy)}L{f(cx)} {f(cy + s)}", colour, w))


def dots4(cx, cy, gap, r, colour):
    return "".join(circle(cx + dx, cy + dy, r, colour)
                   for dx in (-gap, gap) for dy in (-gap, gap))


def _page(x0, y0, x1, y1):
    return rrect(x0, y0, x1 - x0, y1 - y0, 3, INK)


def _pencil(x0, y0, x1, y1, colour, w=5):
    """Pencil lying from tip (x0,y0) to end (x1,y1), outlined in HOLE."""
    a = math.atan2(y1 - y0, x1 - x0)
    tx, ty = x0 + 5 * math.cos(a), y0 + 5 * math.sin(a)
    nx, ny = -math.sin(a) * w / 2, math.cos(a) * w / 2
    tip = [(x0, y0), (tx + nx, ty + ny), (tx - nx, ty - ny)]
    out = stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", HOLE, w + 3.4)
    out += stroke(f"M{f(tx)} {f(ty)}L{f(x1)} {f(y1)}", colour, w)
    return out + poly(tip, colour, 1)


@reg("org.gnome.Snapshot", PURPLE)
def snapshot():
    body = cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 12.5), INK) + circle(CX, CY, 9.5, INK)
    glint = _ring(30.5, 28.5, 4.2, HOLE, 2) + circle(36.5, 34.5, 2.2, HOLE)
    return body + glint


@reg("org.gnome.Social", RED)
def social():
    horn = poly([(24, 24), (43, 15), (43, 45), (24, 36)], INK, 3)
    mouth = rrect(15, 23, 7, 14, 2.5, INK)
    rim = rrect(45.5, 12, 4, 36, 2, INK)
    handle = poly([(25, 38.5), (30, 39.5), (30, 47), (26.5, 47)], INK, 2)
    return horn + mouth + rim + handle


@reg("org.gnome.Software", BLUE_GREY_DEEP)
def gnome_software():
    handle = stroke("M25 21V16.5A3 3 0 0 1 28 13.5H36A3 3 0 0 1 39 16.5V21", INK, 3)
    bag = rrect(15, 20, 34, 27, 4.5, INK)
    shapes = (rrect(20.5, 31, 9, 9, 2, HOLE) + circle(38, 28.5, 4.3, HOLE) +
              poly([(42.5, 34.5), (42.5, 43), (35, 38.75)], HOLE, 1.5))
    return handle + bag + shapes


@reg("org.gnome.Solanum", RED)
def solanum():
    tomato = circle(32, 32, 15.5, INK)
    leaves = (line(32, 18.5, 25.5, 15.5, DEEP_ORANGE_SOFT, 3.4) + line(32, 18.5, 38.5, 15.5, DEEP_ORANGE_SOFT, 3.4) +
              line(32, 18.5, 32, 12, DEEP_ORANGE_SOFT, 3.4))
    needle = line(29, 35, 38, 26, HOLE, 3.4) + circle(29, 35, 3.6, HOLE) + circle(29, 35, 1.4, INK)
    return tomato + leaves + needle


@reg("org.gnome.SoundRecorder", RED_DEEP)
def sound_recorder():
    box = rrect(13, 17, 38, 26, 5, INK)
    rec = circle(23, 30, 5.5, HOLE)
    play = poly([(32, 25.5), (32, 34.5), (38, 30)], HOLE, 1.5)
    pause = rrect(40.5, 25, 2.8, 10, 1.2, HOLE) + rrect(44.5, 25, 2.8, 10, 1.2, HOLE)
    return box + rec + play + pause


@reg("org.gnome.Tau", TEAL_DEEP)
def tau():
    return (stroke("M17 23C18 19 21 17 25 17H46", INK, 5) +
            stroke("M32.5 17.5V37C32.5 42 35.5 44.5 40.5 43.5", INK, 5))


@reg("org.gnome.TextEditor", DEEP_ORANGE_DEEP)
def text_editor():
    page = _page(16, 12, 44, 48)
    blocks = rrect(20, 17, 16, 4.5, 1.5, HOLE) + rrect(20, 24, 11, 4.5, 1.5, HOLE)
    return page + blocks + _pencil(24, 44, 47, 21, DEEP_ORANGE_SOFT)


@reg("org.gnome.Totem", BLUE_DEEP)
def totem():
    tri = poly([(21, 14), (46, 30), (21, 46)], INK, 6)
    band = stroke("M29.5 18.5V41.5", HOLE, 2.2) + stroke("M37.5 23.5V36.5", HOLE, 2.2)
    return tri + band


@reg("org.gnome.Tour", RED_DEEP)
def tour():
    env = path("M32 11.5C23.5 11.5 17 17.5 17 25.5C17 32.5 23 37.5 27 40.5H37"
               "C41 37.5 47 32.5 47 25.5C47 17.5 40.5 11.5 32 11.5Z", INK)
    stripes = (stroke("M32 12C27 15.5 25.5 22 26 28C26.5 33.5 28 38 29 40", HOLE, 2.2) +
               stroke("M32 12C37 15.5 38.5 22 38 28C37.5 33.5 36 38 35 40", HOLE, 2.2))
    basket = rrect(27.5, 42.5, 9, 5.5, 1.8, INK)
    return env + stripes + basket


@reg("org.gnome.Usage", BLUE_GREY_DARK)
def usage():
    screen = rrect(17, 14, 30, 32, 5, BLUE_GREY)
    pulse = stroke("M13 31H23.5L27.5 22.5L32.5 39L36.5 27.5L39 31H51", INK, 4)
    return screen + pulse


def _quote(cx, cy, colour):
    return (circle(cx, cy, 5.5, colour) +
            stroke(f"M{f(cx + 4)} {f(cy)}C{f(cx + 4.5)} {f(cy + 7)} {f(cx + 1)} {f(cy + 11)} {f(cx - 3.5)} {f(cy + 13)}",
                   colour, 4.4))


@reg("org.gnome.World.Citations", DEEP_PURPLE)
def citations():
    return _quote(23.5, 23, INK) + _quote(39, 23, INK)


@reg("org.gnome.World.Highscore", AMBER_DEEP)
def highscore():
    body = rrect(18.5, 11, 27, 38, 4, INK)
    screen = rrect(22, 15, 20, 15, 2, HOLE)
    pad = rrect(21.5, 37, 10, 3.4, 1.2, HOLE) + rrect(24.8, 33.7, 3.4, 10, 1.2, HOLE)
    btns = circle(37, 40.5, 2.4, HOLE) + circle(41.5, 36.5, 2.4, HOLE)
    return body + screen + pad + btns


@reg("org.gnome.World.Iotas", ORANGE_DEEP)
def iotas():
    book = rrect(17, 11, 30, 36, 3.5, INK)
    spine = line(41.5, 11, 41.5, 47, HOLE, 2.2, "butt")
    ribbon = poly([(22, 40), (27, 40), (27, 50), (24.5, 47.8), (22, 50)], ORANGE_DARK, 1)
    return book + spine + ribbon


@reg("org.gnome.World.PikaBackup", PURPLE)
def pika_backup():
    stack = (stroke("M18.5 36.5A13.5 6 0 0 0 45.5 36.5", INK, 3.4) +
             stroke("M18.5 42A13.5 6 0 0 0 45.5 42", INK, 3.4))
    disc = circle(32, 26, 14, INK)
    hands = stroke("M32 20.5V26.5L36 29", HOLE, 2.6)
    loop = stroke(arc_h(32, 26, 9, -150, 200), HOLE, 2.2)
    ax, ay = pt(32, 26, 9, -150)
    head = poly([(ax - 3.2, ay - 0.5), (ax + 1.6, ay - 2.6), (ax + 0.8, ay + 2.8)], HOLE, 1)
    return stack + disc + hands + loop + head


@reg("org.gnome.baobab", BLUE_DEEP)
def baobab():
    x0, y0 = pt(CX, CY, 16, 0)
    x1, y1 = pt(CX, CY, 16, -90)
    main = path(f"M32 30L{f(x0)} {f(y0)}A16 16 0 1 1 {f(x1)} {f(y1)}Z", INK)
    split = line(32, 30, *pt(32, 30, 17, 145), HOLE, 2.2)
    wedge = path("M34.5 27.5V11.5A16 16 0 0 1 50.5 27.5Z", BLUE_SOFT)
    return main + split + wedge


@reg("org.gnome.design.AppIconPreview", BLUE_GREY_DEEP)
def app_icon_preview():
    frame = rrect(13, 17, 38, 26, 5, INK)
    right = rrect(32, 20, 16, 20, 3, HOLE)
    lens = circle(38, 30, 7.5, INK) + circle(38, 30, 5, BLUE)
    return frame + right + lens


@reg("org.gnome.design.BannerViewer", RED_DEEP)
def banner_viewer():
    flaps = (poly([(14, 22), (21, 22), (21, 42), (14, 42), (17, 32)], RED_SOFT, 2) +
             poly([(50, 22), (43, 22), (43, 42), (50, 42), (47, 32)], RED_SOFT, 2))
    banner = rrect(19, 13, 26, 31, 3, INK)
    roll = line(19, 38.5, 45, 38.5, HOLE, 2)
    stars = star_g(32, 21, 4.8, 2.1, HOLE) + star_g(26, 30.5, 4.8, 2.1, HOLE) + star_g(38, 30.5, 4.8, 2.1, HOLE)
    return flaps + banner + roll + stars


@reg("org.gnome.design.Contrast", BLUE_GREY_DARK)
def contrast():
    dial = _ring(CX, CY, 15, INK, 3) + path("M32 16.5A13.5 13.5 0 0 1 32 43.5Z", INK)
    dropper = (stroke("M23.5 39.5L43.5 19.5", HOLE, 9) + line(24.5, 38.5, 36, 27, INK, 3.4) +
               line(37.5, 25.5, 42.5, 20.5, INK, 6.2) + line(32.6, 24.6, 38.4, 30.4, INK, 2.6))
    return dial + dropper


@reg("org.gnome.design.Emblem", GREY_DARK)
def emblem():
    c = [(24.5, 22.5), (39.5, 22.5), (24.5, 37.5), (39.5, 37.5)]
    discs = "".join(circle(x, y, 7.3, INK) for x, y in c)
    back = line(21, 22.5, 28, 22.5, HOLE, 2.4) + stroke("M24 19.5L21 22.5L24 25.5", HOLE, 2.4)
    bee = rrect(36.8, 18.5, 5.4, 3.4, 1.2, HOLE) + rrect(36.8, 23, 5.4, 3.4, 1.2, HOLE)
    ban = _ring(24.5, 37.5, 3.8, HOLE, 2) + line(21.8, 34.8, 27.2, 40.2, HOLE, 2)
    plus = line(39.5, 34, 39.5, 41, HOLE, 2.4) + line(36, 37.5, 43, 37.5, HOLE, 2.4)
    return discs + back + bee + ban + plus


@reg("org.gnome.design.IconLibrary", BLUE_GREY_DEEP)
def icon_library():
    book = rrect(16, 12, 32, 35, 3.5, INK)
    spine = line(21.5, 12, 21.5, 47, HOLE, 2, "butt")
    cross = line(21.5, 29.5, 48, 29.5, HOLE, 2, "butt") + line(34.8, 12, 34.8, 47, HOLE, 2, "butt")
    icons = (heart(28.2, 21, 1.15, HOLE) + _ring(41.4, 21, 3, HOLE, 2) +
             dots4(28.2, 38.2, 2.3, 1.5, HOLE) + arrow_r(41.4, 38.2, 3.2, HOLE, 2.2))
    return book + spine + cross + icons


@reg("org.gnome.design.Lorem", RED_DEEP)
def lorem():
    corners = (stroke("M14 19V14H19", INK, 3) + stroke("M45 14H50V19", INK, 3) +
               stroke("M14 41V46H19", INK, 3) + stroke("M45 46H50V41", INK, 3))
    ell = stroke("M20 18.5V28H26", INK, 3.2)
    text = (rrect(29.5, 18.5, 14.5, 2.8, 1.4, INK) + rrect(29.5, 25, 14.5, 2.8, 1.4, INK) +
            rrect(20, 32, 24, 2.8, 1.4, INK) + rrect(20, 38.5, 17, 2.8, 1.4, INK))
    return corners + ell + text


@reg("org.gnome.design.SymbolicPreview", BLUE_GREY)
def symbolic_preview():
    return (heart(23.5, 21.5, 1.65, INK) + _ring(40.5, 21.5, 4.6, INK, 3.2) +
            arrow_r(23.5, 38.5, 5, INK, 3.2) + dots4(40.5, 38.5, 3.4, 2.3, INK))


@reg("org.gnome.design.Typography", GREY_DARK)
def typography():
    return path("M16 13H48V23H45.5C45 19.5 43.5 18 40 18H35.5V41.5C35.5 43 36.5 43.5 39.5 43.5V47"
                "H24.5V43.5C27.5 43.5 28.5 43 28.5 41.5V18H24C20.5 18 19 19.5 18.5 23H16Z", INK)


@reg("org.gnome.design.VectorSlicer", BLUE_DEEP)
def vector_slicer():
    box = (f'<rect x="14.5" y="16" width="29" height="30" rx="3" fill="none" stroke="{INK}" '
           'stroke-width="2.4" stroke-dasharray="4.2 3"/>')
    knife = (stroke("M22 43L47.5 17.5", HOLE, 9) + line(35.5, 29.5, 47, 18, INK, 5.5) +
             poly([(22.5, 42.5), (31.5, 30.5), (35, 34)], INK, 1.5))
    return box + knife


@reg("org.gnome.dfeet", BLUE_GREY_DARK)
def dfeet():
    lens = circle(36, 24.5, 11, INK)
    foot = path("M0-5.8a2.4 3.4 0 1 0 .01 0Z", HOLE) + circle(0, 3.4, 1.9, HOLE)
    feet = g(foot, "translate(32.8 23.2) rotate(45)") + g(foot, "translate(39.2 26.8) rotate(45)")
    handle = line(27.5, 33, 18, 42.5, INK, 6)
    return lens + feet + handle


@reg("org.gnome.dspy", BROWN)
def dspy():
    crown = path("M22 23L24.5 14C25.2 11.8 27.5 11.2 29.3 12.5L32 14.3L34.7 12.5"
                 "C36.5 11.2 38.8 11.8 39.5 14L42 23Z", INK)
    brim = rrect(13, 22, 38, 4.6, 2.3, INK)
    specs = (rrect(19.5, 30, 10.5, 6.5, 3, INK) + rrect(34, 30, 10.5, 6.5, 3, INK) +
             line(29, 31.8, 35, 31.8, INK, 2.2))
    collar = poly([(16.5, 48.5), (26, 40.5), (31, 48.5)], INK, 2) + poly([(47.5, 48.5), (38, 40.5), (33, 48.5)], INK, 2)
    return crown + brim + specs + collar


def _a2(cx, cy, colour, w):
    """Two-storey a."""
    d = (f"M{f(cx - 4)} {f(cy - 4)}C{f(cx - 3)} {f(cy - 5.6)} {f(cx - 1)} {f(cy - 6.2)} {f(cx + .6)} {f(cy - 6.2)}"
         f"C{f(cx + 3.2)} {f(cy - 6.2)} {f(cx + 4.3)} {f(cy - 4.8)} {f(cx + 4.3)} {f(cy - 2.2)}V{f(cy + 5.8)}"
         f"M{f(cx + 4.3)} {f(cy - .4)}C{f(cx)} {f(cy - .8)} {f(cx - 4.5)} {f(cy + .2)} {f(cx - 4.5)} {f(cy + 2.9)}"
         f"C{f(cx - 4.5)} {f(cy + 4.8)} {f(cx - 3)} {f(cy + 5.6)} {f(cx - 1.2)} {f(cy + 5.6)}"
         f"C{f(cx + 1.6)} {f(cy + 5.6)} {f(cx + 4.3)} {f(cy + 3.5)} {f(cx + 4.3)} {f(cy + .5)}")
    return stroke(d, colour, w)


@reg("org.gnome.font-viewer", PURPLE_DEEP)
def font_viewer():
    single = _ring(38.8, 38.5, 4.6, INK, 3.4) + line(43.4, 33.5, 43.4, 43.8, INK, 3.4)
    return (_a2(23.5, 22.5, INK, 2.6) + _a2(39.5, 22.5, INK, 3.8) +
            _a2(23.5, 38.5, INK, 3) + single)


@reg("org.gnome.gitlab.Cowsay", GREY_DEEP)
def cowsay():
    w = 2.5
    top = (stroke("M15.5 20.5L18.5 15.5L21.5 20.5", INK, w) + line(23.5, 21.5, 29.5, 21.5, INK, w) +
           stroke("M31.5 20.5L34.5 15.5L37.5 20.5", INK, w))
    mid = (stroke("M17 25C14.5 27.8 14.5 32.2 17 35", INK, w) + _ring(22.5, 30, 3, INK, w) +
           _ring(30, 30, 3, INK, w) + stroke("M35.5 25C38 27.8 38 32.2 35.5 35", INK, w) +
           line(40.5, 25, 46.5, 35, INK, w))
    bot = (stroke("M17 37C14.5 39.8 14.5 44.2 17 47", INK, w) + line(20, 46, 32.5, 46, INK, w) +
           stroke("M35.5 37C38 39.8 38 44.2 35.5 47", INK, w) + line(40.5, 37, 46.5, 47, INK, w))
    return g(top + mid + bot, "translate(1.5 -1.5)")


@reg("org.gnome.gitlab.YaLTeR.Identity", CYAN_DEEP)
def identity():
    win = rrect(14, 13, 36, 34, 4, INK)
    slider = rrect(18, 16, 28, 3.6, 1.8, HOLE) + circle(29, 17.8, 3.4, INK) + circle(29, 17.8, 1.6, HOLE)
    pic = rrect(17.5, 23.5, 29, 20, 2, HOLE)
    corner = poly([(46.5, 32.5), (46.5, 43.5), (35.5, 43.5)], INK, 1)
    return win + slider + pic + corner


@reg("org.gnome.gitlab.YaLTeR.VideoTrimmer", BLUE_DEEP)
def video_trimmer():
    film = rrect(21, 13.5, 22, 33, 2.5, INK)
    holes = "".join(rrect(23.5 + 4.6 * k, y, 3, 2.6, .8, HOLE) for k in range(4) for y in (16, 41.4))
    frame = line(21, 30, 43, 30, HOLE, 2, "butt")
    br = stroke("M18.5 12H15V48H18.5", INK, 3.2) + stroke("M45.5 12H49V48H45.5", INK, 3.2)
    return film + holes + frame + br


@reg("org.gnome.gitlab.ilhooq.Bookup", INDIGO_LIGHT)
def bookup():
    book = rrect(17, 11, 29, 38, 4, INK)
    label = rrect(21, 17, 13, 7.5, 2, HOLE)
    edge = line(20, 43.5, 35, 43.5, HOLE, 2)
    strap = rrect(37.5, 9.5, 4.8, 41, 2, INDIGO_DARK)
    return book + label + edge + strap


@reg("org.gnome.gitlab.somas.Apostrophe", GREY_DARK)
def apostrophe():
    board = rrect(13, 17, 38, 27, 5, INK)
    keys = ""
    for r, y in enumerate((21, 27.5)):
        for k in range(5):
            col = ORANGE if (r, k) == (1, 4) else HOLE
            keys += rrect(16.5 + 6.6 * k, y, 4.8, 4.2, 1.2, col)
    keys += rrect(16.5, 34, 4.8, 4.2, 1.2, HOLE) + rrect(23.1, 34, 18.1, 4.2, 1.2, HOLE)
    keys += rrect(42.9, 34, 4.8, 4.2, 1.2, HOLE)
    return board + keys


@reg("org.gnunet.Messenger", BLUE_GREY_LIGHT)
def gnunet_messenger():
    bubble = path("M18 13H46A4 4 0 0 1 50 17V38A4 4 0 0 1 46 42H26L16.5 48.5L19 42H18"
                  "A4 4 0 0 1 14 38V17A4 4 0 0 1 18 13Z", INK)
    horns = stroke("M20.5 18.5C21.5 23 23.5 24.5 26.5 24.5H37.5C40.5 24.5 42.5 23 43.5 18.5", HOLE, 2.6)
    face = stroke("M26.5 24.5L30 36H34L37.5 24.5", HOLE, 2.6) + stroke("M29.5 27L32 30.5L34.5 27", HOLE, 2.2)
    return bubble + horns + face


@reg("org.gtk.Demo4", BLUE_DARK)
def gtk_demo():
    top = poly([(32, 12.5), (47, 20.5), (32, 28.5), (17, 20.5)], INK, 2.5)
    left = poly([(17, 20.5), (32, 28.5), (32, 47), (17, 39)], BLUE_SOFT, 2.5)
    right = poly([(47, 20.5), (32, 28.5), (32, 47), (47, 39)], BLUE, 2.5)
    return top + left + right


@reg("org.gtk.WidgetFactory4", BLUE_GREY)
def widget_factory():
    rows = rrect(15, 13, 34, 9.5, 3, INK) + rrect(15, 25.5, 34, 9.5, 3, INK) + rrect(15, 38, 34, 9.5, 3, INK)
    drop = rrect(19, 16.5, 15, 2.6, 1.3, HOLE) + poly([(39.5, 16.3), (45, 16.3), (42.25, 19.5)], HOLE, 1)
    spin = (rrect(19, 29, 11, 2.6, 1.3, HOLE) + line(34, 30.3, 38, 30.3, HOLE, 2.2) +
            line(41, 30.3, 46, 30.3, HOLE, 2.2) + line(43.5, 27.8, 43.5, 32.8, HOLE, 2.2))
    btn = rrect(25, 41.5, 14, 2.6, 1.3, HOLE)
    return rows + drop + spin + btn


@reg("org.gustavoperedo.FontDownloader", INDIGO_LIGHT)
def font_downloader():
    a = stroke("M15.5 45L26.5 15L37.5 45", INK, 5) + line(20.5, 35, 32.5, 35, INK, 4)
    arrow = line(44, 24, 44, 43, INK, 4) + stroke("M38.5 37.5L44 43L49.5 37.5", INK, 4)
    return a + arrow


@reg("org.homelinuxserver.vance.biblereader-symbolic", INDIGO)
def biblereader():
    book = rrect(18, 11, 28, 38, 4, INK)
    spine = line(23, 11, 23, 49, HOLE, 2.2, "butt")
    cross = rrect(32.5, 16.5, 4.6, 26, 1.5, HOLE) + rrect(26.5, 23, 16.6, 4.6, 1.5, HOLE)
    return book + spine + cross


@reg("org.horizon_eda.HorizonEDA", BLUE_GREY_DARK)
def horizon_eda():
    out = _ring(CX, CY, 16, INK, 2.6) + circle(32, 21, 4.6, BLUE_LIGHT)
    for y in (30.5, 35.5, 40.5):
        hw = math.sqrt(12.5 ** 2 - (y + 1.3 - CY) ** 2)
        out += rrect(32 - hw, y, 2 * hw, 2.8, 1.4, INK)
    return out


@reg("org.kde.Ikona", PINK_DEEP)
def ikona():
    rolls = rrect(14, 12, 7.5, 35, 3.75, INK) + rrect(42.5, 12, 7.5, 35, 3.75, INK)
    sheet = rrect(20.5, 16, 23, 28, 1.5, PINK_SOFT)
    lens = circle(32, 30, 8, INK) + circle(32, 30, 5.2, HOLE)
    return sheet + rolls + lens


@reg("org.kde.audiotube", RED)
def audiotube():
    out = _ring(CX, CY, 13.5, INK, 3) + line(13, 30, 18.5, 30, INK, 3) + line(45.5, 30, 51, 30, INK, 3)
    for x, h in [(26, 12), (29.3, 16), (32.6, 10), (35.9, 7), (39, 3.5)]:
        out += line(x, 30 - h / 2, x, 30 + h / 2, INK, 2.4)
    return out


@reg("org.kde.dolphin", BLUE_DEEP)
def dolphin():
    back = path("M14 18A3 3 0 0 1 17 15H26L29.5 18.5H47A3 3 0 0 1 50 21.5V43A3 3 0 0 1 47 46H17"
                "A3 3 0 0 1 14 43Z", INK)
    return back + line(14, 25, 50, 25, HOLE, 2.2, "butt")


@reg("org.kde.kalendar", LIGHT_BLUE_DEEP)
def kalendar():
    tabs = rrect(20, 12.5, 10, 3.6, 1.8, INK) + rrect(34, 12.5, 10, 3.6, 1.8, INK)
    cells = "".join(rrect(x, y, 12, 12, 2.5, INK) for x in (19, 33) for y in (20, 34))
    check = circle(25, 40, 2, HOLE)
    return tabs + cells + check


@reg("org.kde.karp", RED_DEEP)
def karp():
    book = rrect(16, 11, 29, 37, 3.5, INK)
    spine = line(20.5, 11, 20.5, 48, HOLE, 2, "butt")
    leaves = (path("M24 17C29 16.5 33 21 33 27C29 26 25 22.5 24 17Z", RED_SOFT) +
              path("M26 30C29 28 33.5 28.5 36 31.5C32 33 28.5 32.5 26 30Z", RED_SOFT))
    return book + spine + leaves + _pencil(30, 43, 49, 22, INK, 4.6)


@reg("org.kde.kasts", INDIGO)
def kasts():
    arcs = "".join(stroke(arc_h(32, 21, r, 200, 340), INK, 2.6) for r in (6.5, 11, 15.5))
    top = circle(32, 21, 3, INK)
    tower = stroke("M32 25L24.5 47M32 25L39.5 47", INK, 2.8) + stroke("M27.2 39H36.8M28.5 35L35 43M35.5 35L29 43", INK, 2.2)
    return arcs + top + tower


@reg("org.kde.kontrast", TEAL_DARK)
def kontrast():
    face = _ring(CX, CY, 15.2, INK, 2.6) + path("M32 14.8A15.2 15.2 0 0 1 32 45.2Z", INK)
    a = (stroke("M22.5 43L32 16", INK, 4.4) + stroke("M32 16L41.5 43", HOLE, 4.4) +
         line(26, 34.5, 32, 34.5, INK, 3.6, "butt") + line(32, 34.5, 38, 34.5, HOLE, 3.6, "butt"))
    return face + a


@reg("org.kde.kwatchgnupg", LIGHT_BLUE_DEEP)
def kwatchgnupg():
    wing = path("M14 47C16.5 33 28 17.5 50.5 11C45.5 16 42 20 39.5 23.5C43 23 47 22.5 50.5 22.5"
                "C46 27 42 29.5 38.5 31.5C42.5 32 46.5 32.5 50.5 33C43.5 40.5 30 46 14 47Z", INK)
    cuts = (stroke("M19 43C26 35.5 33.5 29 40.5 24.5", HOLE, 2.2) +
            stroke("M21.5 44.5C28 39 34 34.5 39.5 32", HOLE, 2.2))
    return wing + cuts


@reg("org.kde.marknote", TEAL)
def marknote():
    page = _page(15, 12, 42, 48)
    band = line(15, 19.5, 42, 19.5, HOLE, 2.2, "butt")
    lines = "".join(rrect(19, y, w, 2.8, 1.4, HOLE) for y, w in [(24.5, 19), (30, 19), (35.5, 13), (41, 8)])
    return page + band + lines + _pencil(31, 45, 49, 27, INK, 4.6)


@reg("org.kde.merkuro.calendar", ORANGE_DEEP)
def merkuro_calendar():
    body = rrect(14, 15, 36, 32, 4.5, INK)
    rings = (line(23, 11, 23, 18, HOLE, 6.8) + line(23, 11.5, 23, 17.5, INK, 3.4) +
             line(41, 11, 41, 18, HOLE, 6.8) + line(41, 11.5, 41, 17.5, INK, 3.4))
    band = line(14, 22.5, 50, 22.5, HOLE, 2, "butt")
    cells = ""
    for r, y in enumerate((27.5, 36)):
        for k in range(4):
            x = 18 + 7.5 * k
            if (r, k) == (1, 2):
                cells += circle(x + 2.75, y + 2.75, 3.6, HOLE)
            else:
                cells += rrect(x, y, 5.5, 5.5, 1.3, HOLE)
    return body + band + rings + cells


@reg("org.kde.merkuro.contact", INDIGO_LIGHT)
def merkuro_contact():
    head = circle(32, 21, 7.8, INK)
    body = path("M16.5 46C16.5 37 23 32 32 32C41 32 47.5 37 47.5 46Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return head + body


@reg("org.kde.merkuro.mail", BLUE)
def merkuro_mail():
    env = rrect(13, 16.5, 38, 27, 4, INK)
    flap = stroke("M14.5 19L32 31.5L49.5 19", HOLE, 2.8)
    return env + flap


@small("org.gnome.Snapshot")
def snapshot_s():
    return (cut(cpath(CX, CY, 17) + cpath(CX, CY, 12), INK) + circle(CX, CY, 8.5, INK) +
            circle(29.5, 27.5, 3, HOLE))


@small("org.gnome.Social")
def social_s():
    return rrect(14, 22.5, 8.5, 15, 3, INK) + poly([(25.5, 23), (47, 13), (47, 47), (25.5, 37)], INK, 3)


@small("org.gnome.Software")
def gnome_software_s():
    handle = stroke("M24.5 21V16A3 3 0 0 1 27.5 13H36.5A3 3 0 0 1 39.5 16V21", INK, 3.4)
    return handle + rrect(14, 20, 36, 28, 5, INK) + rrect(19, 29, 11, 11, 2.5, HOLE) + circle(40, 34.5, 5.5, HOLE)


@small("org.gnome.Solanum")
def solanum_s():
    leaves = line(32, 18, 25, 14.5, DEEP_ORANGE_SOFT, 4) + line(32, 18, 39, 14.5, DEEP_ORANGE_SOFT, 4)
    return circle(32, 32, 16, INK) + leaves + line(28, 36, 38.5, 25.5, HOLE, 4.5) + circle(28, 36, 4.2, HOLE)


@small("org.gnome.SoundRecorder")
def sound_recorder_s():
    return (rrect(12, 16, 40, 28, 5, INK) + circle(23, 30, 6.5, HOLE) +
            poly([(34, 23), (34, 37), (44.5, 30)], HOLE, 2))


@small("org.gnome.TextEditor")
def text_editor_s():
    return _page(15, 11, 44, 48) + _pencil(22, 45, 48, 19, DEEP_ORANGE_SOFT, 6.5)


@small("org.gnome.Tour")
def tour_s():
    env = path("M32 10.5C23 10.5 16 17 16 25.5C16 33 22.5 38 27 41H37"
               "C41.5 38 48 33 48 25.5C48 17 41 10.5 32 10.5Z", INK)
    return env + stroke("M32 12V40", HOLE, 3) + rrect(26.5, 43.5, 11, 6, 2, INK)


@small("org.gnome.World.Highscore")
def highscore_s():
    return (rrect(17, 10, 30, 40, 4.5, INK) + rrect(21, 14.5, 22, 16, 2, HOLE) +
            rrect(20.5, 37, 12, 4.6, 1.5, HOLE) + rrect(24.2, 33.3, 4.6, 12, 1.5, HOLE) +
            circle(39.5, 39, 3.4, HOLE))


@small("org.gnome.World.PikaBackup")
def pika_backup_s():
    return (stroke("M18 39A14 6.5 0 0 0 46 39", INK, 4.4) + circle(32, 25.5, 15, INK) +
            stroke("M32 17.5V26L37.5 30", HOLE, 3.6))


@small("org.gnome.design.AppIconPreview")
def app_icon_preview_s():
    return (rrect(12, 16, 40, 28, 5, INK) + rrect(31, 19.5, 17.5, 21, 3, HOLE) +
            circle(39, 30, 8.5, INK) + circle(39, 30, 5.5, BLUE))


@small("org.gnome.design.BannerViewer")
def banner_viewer_s():
    flaps = (poly([(13, 22), (20, 22), (20, 43), (13, 43), (16.5, 32.5)], RED_SOFT, 2) +
             poly([(51, 22), (44, 22), (44, 43), (51, 43), (47.5, 32.5)], RED_SOFT, 2))
    return flaps + rrect(18.5, 12, 27, 33, 3, INK) + star_g(32, 28, 9, 3.9, HOLE, 1.5)


@small("org.gnome.design.Contrast")
def contrast_s():
    return (_ring(CX, CY, 15, INK, 3.4) + path("M32 16A14 14 0 0 1 32 44Z", INK) +
            stroke("M22.5 40.5L43 20", HOLE, 10) + line(23.5, 39.5, 42, 21, INK, 5))


@small("org.gnome.design.Emblem")
def emblem_s():
    discs = "".join(circle(x, y, 8, INK) for x, y in [(23.5, 21.5), (40.5, 21.5), (23.5, 38.5), (40.5, 38.5)])
    return (discs + line(19.5, 21.5, 27.5, 21.5, HOLE, 3) + line(40.5, 34.5, 40.5, 42.5, HOLE, 3) +
            line(36.5, 38.5, 44.5, 38.5, HOLE, 3))


@small("org.gnome.design.IconLibrary")
def icon_library_s():
    return (rrect(15, 11, 34, 37, 4, INK) + line(15, 29.5, 49, 29.5, HOLE, 3, "butt") +
            line(32, 11, 32, 48, HOLE, 3, "butt") + heart(23.5, 20.5, 1.6, HOLE) + circle(40.5, 38.5, 3.8, HOLE))


@small("org.gnome.design.Lorem")
def lorem_s():
    corners = (stroke("M13 19V13H19", INK, 3.6) + stroke("M45 13H51V19", INK, 3.6) +
               stroke("M13 41V47H19", INK, 3.6) + stroke("M45 47H51V41", INK, 3.6))
    return corners + rrect(20, 20, 24, 4.4, 2.2, INK) + rrect(20, 28, 24, 4.4, 2.2, INK) + rrect(20, 36, 16, 4.4, 2.2, INK)


@small("org.gnome.design.SymbolicPreview")
def symbolic_preview_s():
    return (heart(22.5, 21.5, 2.1, INK) + _ring(41.5, 21, 5.3, INK, 3.8) +
            arrow_r(22.5, 39, 6, INK, 3.8) + dots4(41.5, 39, 4, 2.9, INK))


@small("org.gnome.design.VectorSlicer")
def vector_slicer_s():
    box = (f'<rect x="13.5" y="15" width="31" height="32" rx="3" fill="none" stroke="{INK}" '
           'stroke-width="3" stroke-dasharray="7 4"/>')
    return box + stroke("M21 44.5L48.5 17", HOLE, 11) + line(22.5, 43, 47, 18.5, INK, 6)


@small("org.gnome.dfeet")
def dfeet_s():
    return (circle(36.5, 24, 12.5, INK) + circle(33, 27.5, 3, HOLE) + circle(40, 20.5, 3, HOLE) +
            line(27, 33.5, 17, 43.5, INK, 7))


@small("org.gnome.dspy")
def dspy_s():
    crown = path("M21.5 24L24.5 13C25.2 10.8 27.5 10.2 29.3 11.5L32 13.3L34.7 11.5"
                 "C36.5 10.2 38.8 10.8 39.5 13L42.5 24Z", INK)
    specs = rrect(17.5, 31, 12.5, 8.5, 4, INK) + rrect(34, 31, 12.5, 8.5, 4, INK) + line(29, 34, 35, 34, INK, 3)
    return crown + rrect(12, 22.5, 40, 5.5, 2.75, INK) + specs + poly([(18, 49), (32, 42), (46, 49)], INK, 2)


@small("org.gnome.font-viewer")
def font_viewer_s():
    return g(_a2(0, 0, INK, 2.6), "translate(23 30) scale(1.55)") + g(_a2(0, 0, INK, 3.2), "translate(41 30) scale(1.55)")


@small("org.gnome.gitlab.Cowsay")
def cowsay_s():
    return (stroke("M18 18C13.5 23.5 13.5 36.5 18 42", INK, 3.6) + _ring(25, 30, 4.8, INK, 3.6) +
            _ring(38, 30, 4.8, INK, 3.6) + stroke("M45 18C49.5 23.5 49.5 36.5 45 42", INK, 3.6))


@small("org.gnome.gitlab.YaLTeR.Identity")
def identity_s():
    return (rrect(13, 12, 38, 36, 4.5, INK) + rrect(17, 15.5, 30, 4, 2, HOLE) +
            rrect(17, 23.5, 30, 21, 2, HOLE) + poly([(47, 32), (47, 44.5), (34.5, 44.5)], INK, 1))


@small("org.gnome.gitlab.YaLTeR.VideoTrimmer")
def video_trimmer_s():
    holes = "".join(rrect(24 + 6 * k, y, 4, 3.4, 1, HOLE) for k in range(3) for y in (16, 40.6))
    return (rrect(21, 12.5, 22, 35, 2.5, INK) + holes + stroke("M18 11H14V49H18", INK, 3.6) +
            stroke("M46 11H50V49H46", INK, 3.6))


@small("org.gnome.gitlab.ilhooq.Bookup")
def bookup_s():
    return (rrect(16, 10, 30, 40, 4, INK) + rrect(20, 16, 14, 9, 2, HOLE) +
            rrect(37, 8.5, 6, 43, 2.5, INDIGO_DARK))


@small("org.gnome.gitlab.somas.Apostrophe")
def apostrophe_s():
    keys = "".join(rrect(17 + 10.5 * k, 21.5, 8, 6.5, 1.5, ORANGE if k == 2 else HOLE) for k in range(3))
    return rrect(12, 16, 40, 28, 5, INK) + keys + rrect(17, 32, 29, 6.5, 1.5, HOLE)


@small("org.gnunet.Messenger")
def gnunet_messenger_s():
    bubble = path("M18 12H46A4 4 0 0 1 50 16V38A4 4 0 0 1 46 42H26L15.5 49L18.5 42H18"
                  "A4 4 0 0 1 14 38V16A4 4 0 0 1 18 12Z", INK)
    return (bubble + stroke("M20 17C21 22.5 23.5 24 27 24H37C40.5 24 43 22.5 44 17", HOLE, 3.4) +
            stroke("M26.5 24L32 37L37.5 24", HOLE, 3.4))


@small("org.gtk.WidgetFactory4")
def widget_factory_s():
    rows = rrect(14, 12, 36, 10.5, 3.5, INK) + rrect(14, 25, 36, 10.5, 3.5, INK) + rrect(14, 38, 36, 10.5, 3.5, INK)
    return (rows + poly([(37, 15.5), (45, 15.5), (41, 19.5)], HOLE, 1.5) + line(41, 27.5, 41, 33, HOLE, 3) +
            line(38.2, 30.25, 43.8, 30.25, HOLE, 3) + rrect(24, 41.5, 16, 3.5, 1.75, HOLE))


@small("org.gustavoperedo.FontDownloader")
def font_downloader_s():
    return (stroke("M14.5 46L26 14L37.5 46", INK, 6) + line(19.5, 36, 32.5, 36, INK, 4.4) +
            line(45, 22, 45, 44, INK, 4.6) + stroke("M39 38L45 44L51 38", INK, 4.6))


@small("org.homelinuxserver.vance.biblereader-symbolic")
def biblereader_s():
    return (rrect(17, 10, 30, 40, 4, INK) + rrect(29.5, 15, 6, 30, 2, HOLE) +
            rrect(22, 22, 21, 6, 2, HOLE))


@small("org.horizon_eda.HorizonEDA")
def horizon_eda_s():
    out = _ring(CX, CY, 16, INK, 3.2) + circle(32, 20.5, 5, BLUE_LIGHT)
    for y in (30, 37.5):
        hw = math.sqrt(12.2 ** 2 - (y + 1.9 - CY) ** 2)
        out += rrect(32 - hw, y, 2 * hw, 3.8, 1.9, INK)
    return out


@small("org.kde.Ikona")
def ikona_s():
    return (rrect(20, 15, 24, 30, 1.5, PINK_SOFT) + rrect(12.5, 11, 9, 37, 4.5, INK) +
            rrect(42.5, 11, 9, 37, 4.5, INK) + circle(32, 30, 8.5, INK) + circle(32, 30, 5, HOLE))


@small("org.kde.audiotube")
def audiotube_s():
    out = _ring(CX, CY, 14, INK, 3.6) + line(12, 30, 18, 30, INK, 3.6) + line(46, 30, 52, 30, INK, 3.6)
    for x, h in [(26.5, 12), (32, 16), (37.5, 8)]:
        out += line(x, 30 - h / 2, x, 30 + h / 2, INK, 3.4)
    return out


@small("org.kde.kalendar")
def kalendar_s():
    cells = "".join(rrect(x, y, 14, 14, 3, INK) for x in (17, 33) for y in (16, 32))
    return cells + circle(24, 39, 2.4, HOLE)


@small("org.kde.karp")
def karp_s():
    leaf = path("M22 16C28 15.5 32.5 21 32.5 28C28 27 23 22.5 22 16Z", RED_SOFT)
    return rrect(15, 10, 31, 39, 4, INK) + leaf + _pencil(29, 44, 50, 21, INK, 6)


@small("org.kde.kasts")
def kasts_s():
    arcs = "".join(stroke(arc_h(32, 21, r, 205, 335), INK, 3.4) for r in (8, 14.5))
    return (arcs + circle(32, 21, 3.6, INK) + stroke("M32 25L23.5 48M32 25L40.5 48", INK, 3.6) +
            line(27, 39, 37, 39, INK, 3))


@small("org.kde.kontrast")
def kontrast_s():
    face = _ring(CX, CY, 15.5, INK, 3.4) + path("M32 14.5A15.5 15.5 0 0 1 32 45.5Z", INK)
    return (face + stroke("M22.5 44L32 15.5", INK, 5.5) + stroke("M32 15.5L41.5 44", HOLE, 5.5) +
            line(26, 35, 32, 35, INK, 4.4, "butt") + line(32, 35, 38, 35, HOLE, 4.4, "butt"))


@small("org.kde.kwatchgnupg")
def kwatchgnupg_s():
    wing = path("M13 48C15.5 33 27.5 16.5 51 10C46 16 42.5 20.5 40 24C43.5 23.5 47.5 23 51 23"
                "C45 30.5 34 45 13 48Z", INK)
    return wing + stroke("M19.5 42.5C26.5 35 33.5 29.5 40.5 25.5", HOLE, 3)


@small("org.kde.marknote")
def marknote_s():
    return (_page(14, 11, 42, 49) + line(14, 19, 42, 19, HOLE, 3, "butt") +
            rrect(18.5, 25, 18, 4, 2, HOLE) + rrect(18.5, 32.5, 11, 4, 2, HOLE) +
            _pencil(30, 46, 50, 26, INK, 6))


@small("org.kde.merkuro.calendar")
def merkuro_calendar_s():
    rings = (line(23, 10, 23, 18, HOLE, 8) + line(23, 10.5, 23, 17.5, INK, 4) +
             line(41, 10, 41, 18, HOLE, 8) + line(41, 10.5, 41, 17.5, INK, 4))
    cells = "".join(rrect(18 + 10 * k, y, 7.5, 7, 1.5, HOLE) for k in range(3) for y in (26, 36)
                    if not (k == 2 and y == 36))
    check = circle(42, 40, 3, HOLE)
    return rrect(13, 14, 38, 34, 5, INK) + line(13, 21.5, 51, 21.5, HOLE, 2.4, "butt") + rings + cells + check
