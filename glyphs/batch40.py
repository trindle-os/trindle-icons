# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 40: kmymoney to kstars (mostly KDE apps and games)."""
import math
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DEEP, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_SOFT, BROWN, BROWN_DARK, BROWN_DEEP, circle, cut, CX, CY, CYAN_DEEP, CYAN_SOFT,
    DEEP_ORANGE_DEEP, DEEP_PURPLE, DEEP_PURPLE_LIGHT, f, g, GREY, GREY_DARK, GREY_DEEP,
    GREY_SOFT, HOLE, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, line,
    ORANGE, ORANGE_DARK, ORANGE_DEEP, ORANGE_LIGHT, path, PINK, poly, pt, PURPLE_LIGHT, RED,
    RED_DEEP, RED_LIGHT, rrect, stroke, TEAL_DEEP,
)
from glyphs.kit import registry

ICONS, SMALL, reg, small = registry()


def _knight():
    body = path("M19.5 44H45C46 35 44.5 26.5 39.5 20C36.5 16 32.5 13.5 29 13.5L27.5 10.5"
                "L24.5 14.5C20.5 17 17.5 21 15.5 26C14.5 29 17 31.5 20 30"
                "L27.5 26.5C27.5 32.5 21.5 36.5 19.5 44Z", INK)
    return body + rrect(16.5, 43, 31, 6, 3, INK) + circle(27.5, 19.5, 1.9, HOLE)


def _lizard():
    body = stroke("M39 19.5C30 16 21.5 21 21 30", INK, 7)
    tail = stroke("M21 30C21 39 28 44.5 36 44C42 43.5 46 40 47.5 35", INK, 4)
    tip = stroke("M47.5 35C48.5 32 47 30 45 30", INK, 2.6)
    head = g('<ellipse cx="42.5" cy="18.5" rx="6.5" ry="4.2" fill="INK"/>', "rotate(20 42.5 18.5)")
    legs = (stroke("M32 17L31 11.5L28.5 10.5", INK, 2.8) +
            stroke("M34.5 20L37 25L39.5 25.5", INK, 2.8) +
            stroke("M21.5 27L15.5 25L14.5 22.5", INK, 2.8) +
            stroke("M22.5 34L27.5 35.5L28.5 38.5", INK, 2.8))
    return body + tail + tip + head + legs + circle(43.5, 17, 1.4, HOLE)


def _komorebi():
    back = stroke("M17.5 42.5H40", INK, 2.4) + stroke("M16 38.5V22", INK, 2.4)
    pic = rrect(19, 15, 30, 24, 3.5, INK)
    ring = circle(42, 37.5, 7.5, HOLE) + circle(42, 37.5, 5.5, INK) + circle(42, 37.5, 3, HOLE)
    return g(back + pic + ring, "translate(-1 0)")


def _krusader():
    win = rrect(14, 14, 36, 32, 4, INK)
    bar = rrect(14, 14, 36, 4.5, 2, HOLE) + rrect(14, 14, 36, 6, 4, INK)
    split = line(14, 20, 50, 20, HOLE, 2, "butt")
    cur = poly([(26, 24), (38, 33.5), (32.5, 34), (35.5, 40.5), (32.5, 42), (29.5, 35.5), (26, 39)], HOLE, 1.6)
    return win + split + cur


@reg("kmymoney", AMBER_DEEP)
def kmymoney():
    ring = circle(CX, CY, 17, INK) + circle(CX, CY, 14, HOLE)
    k = stroke("M27 20V40", INK, 3.4) + stroke("M39 20L28 30L39 40", INK, 3.4)
    bars = line(21, 28.2, 43, 28.2, INK, 2.2) + line(21, 32.2, 43, 32.2, INK, 2.2)
    return ring + k + bars


@reg("knavalbattle", BLUE_GREY_DEEP)
def knavalbattle():
    eye = circle(32, 15.5, 4.8, INK) + circle(32, 15.5, 2, HOLE)
    shank = line(32, 20, 32, 46, INK, 3.6, "butt")
    bar = line(24, 25, 40, 25, INK, 3.2)
    arms = stroke("M17.5 34C19 42 25 46.5 32 46.5C39 46.5 45 42 46.5 34", INK, 3.6)
    tips = (poly([(14.5, 36), (18, 30), (21.5, 36)], INK, 1.5) +
            poly([(42.5, 36), (46, 30), (49.5, 36)], INK, 1.5))
    return eye + shank + bar + arms + tips


@reg("knights-game", BROWN_DEEP)
@reg("knights", GREY_DARK)
def knights():
    return _knight()


@reg("kolf", INDIGO_LIGHT)
def kolf():
    ball = circle(CX, CY, 16, INK)
    dots = ""
    for r, n, off in [(0, 1, 0), (6.5, 6, 0), (12, 10, 18)]:
        for k in range(n):
            x, y = pt(CX, CY, r, off + 360 / n * k)
            dots += circle(x, y, 1.9, HOLE)
    return ball + dots


@reg("kollision", BLUE_DEEP)
def kollision():
    return circle(25, 36, 10, INK) + circle(40.5, 20.5, 8, RED_LIGHT)


@reg("konquest", ORANGE_DARK)
def konquest():
    planet = circle(CX, CY, 11.5, INK)
    ell = ('<ellipse cx="32" cy="30" rx="18.5" ry="5" fill="none" stroke="INK" stroke-width="3" '
           'transform="rotate(-20 32 30)"/>')
    gap = g(stroke("M13.5 30A18.5 5 0 0 0 50.5 30", HOLE, 6.5), "rotate(-20 32 30)")
    front = g(stroke("M13.5 30A18.5 5 0 0 0 50.5 30", INK, 3), "rotate(-20 32 30)")
    return ell + planet + gap + front


@reg("kpatience", RED_DEEP)
def kpatience():
    card = g(rrect(19, 12, 26, 36, 4, INK), "rotate(6 32 30)")
    heart = path("M32 39C26 34.5 22.5 31 22.5 27C22.5 24 24.8 22 27.3 22C29.3 22 31 23.2 32 25"
                 "C33 23.2 34.7 22 36.7 22C39.2 22 41.5 24 41.5 27C41.5 31 38 34.5 32 39Z", HOLE)
    return card + g(heart, "rotate(6 32 30)")


@reg("kreversi", PURPLE_LIGHT)
def kreversi():
    ring = circle(CX, CY, 16.5, INK) + circle(CX, CY, 14.2, HOLE)
    half = path("M32 15.8A14.2 14.2 0 0 1 32 44.2A7.1 7.1 0 0 1 32 30A7.1 7.1 0 0 0 32 15.8Z", INK)
    return ring + half + circle(32, 22.9, 3, HOLE) + circle(32, 37.1, 3, INK)


@reg("ksame", RED_DEEP)
def ksame():
    ring = circle(CX, CY, 16.5, INK) + circle(CX, CY, 14.3, HOLE)
    wedges = ""
    for k in range(4):
        a0 = -90 - 22.5 + 90 * k
        p0, p1 = pt(CX, CY, 14.3, a0), pt(CX, CY, 14.3, a0 + 45)
        wedges += path(f"M32 30L{f(p0[0])} {f(p0[1])}A14.3 14.3 0 0 1 {f(p1[0])} {f(p1[1])}Z", INK)
    return ring + wedges + circle(CX, CY, 4.5, HOLE)


@reg("kshisen", AMBER_DARK)
def kshisen():
    tile = rrect(17, 12, 30, 37, 4.5, INK)
    box = rrect(22.5, 22, 19, 12, 2, HOLE) + rrect(25.5, 25, 13, 6, 1, INK)
    stem = line(32, 16.5, 32, 44.5, HOLE, 3.2)
    return tile + box + stem


@reg("ksirk", BROWN)
def ksirk():
    barrel = line(17.5, 22, 44, 28, INK, 7)
    muzzle = line(45, 25, 43.5, 31.5, INK, 3)
    trail = line(27, 34, 47.5, 45, INK, 3.4)
    wheel = circle(26, 34, 9, INK) + circle(26, 34, 6.2, HOLE)
    spokes = "".join(line(*pt(26, 34, 6.5, a), *pt(26, 34, 6.5, a + 180), INK, 2) for a in (0, 60, 120))
    return barrel + muzzle + trail + wheel + spokes + circle(26, 34, 2.5, INK)


@reg("ksnakeduel", ORANGE_DEEP)
def ksnakeduel():
    one = stroke("M22 26H33.5V19H40.5V14H47", INK, 3.4)
    two = stroke("M47 45H23V37.5H40.5V31H22", INK, 3.4)
    return one + two + circle(47, 14, 2.6, INK) + circle(22, 31, 2.6, INK)


@reg("kspaceduel", BROWN_DARK)
def kspaceduel():
    planet = circle(CX, CY, 16, ORANGE)
    craters = (path("M20 22C23 19 27 21 26 24.5C25 28 20.5 27 20 22Z", ORANGE_DEEP) +
               path("M34 18C38 16 41 19 39.5 22C38 24 34.5 23 34 18Z", ORANGE_DEEP) +
               path("M26 34C31 32 35 36 32 40C29.5 43 24 40 26 34Z", ORANGE_DEEP) +
               circle(41.5, 33, 3.2, ORANGE_DEEP))
    return planet + craters


@reg("ksquares", GREY_DARK)
def ksquares():
    lines = (line(18, 38, 32, 38, INK, 3.2) + line(32, 38, 32, 23, INK, 3.2) +
             line(32, 23, 46, 23, INK, 3.2))
    dots = "".join(circle(x, y, 4, INK) for x, y in [(18, 38), (32, 38), (32, 23), (46, 23)])
    faint = "".join(circle(x, y, 2.2, GREY) for x, y in [(18, 23), (46, 38)])
    return faint + lines + dots


@reg("knemo", LIGHT_BLUE_DEEP)
def knemo():
    globe = circle(CX, CY, 16.5, INK)
    land = (path("M20.5 19C24 16 28 15 31 15.8C30 18.5 27.5 19 26.5 21.5C29 23 28 26.5 25 27"
                 "C22.5 27.5 22 30.5 19 30.5C17 27 17.5 22 20.5 19Z", HOLE) +
            path("M35 17C40.5 18 45 22 46.5 27.5C44 27 42 25 39.5 26.5C37 28 38.5 31.5 36 33"
                 "C33 34.5 30.5 32 31 29.5C31.5 27 34.5 26.5 34 23.5C33.5 21 32 19 35 17Z", HOLE) +
            path("M29 37.5C32 36 35 38 34.5 41C34 43.5 31 45 28.5 44.8C28 42 26.5 39 29 37.5Z", HOLE))
    return globe + land


@reg("knowte", BLUE_DEEP)
def knowte():
    pen = poly([(38, 15.5), (46.5, 24), (27, 43.5), (18.5, 35)], INK, 2.5)
    tip = poly([(17.5, 37.5), (25, 45), (15, 47.5)], INK, 2)
    return pen + tip + line(35.5, 21, 41, 26.5, HOLE, 2, "butt")


@reg("koala", GREY_DEEP)
def koala():
    ears = circle(18.5, 21, 7.5, INK) + circle(45.5, 21, 7.5, INK)
    inner = circle(18.5, 21, 3.6, GREY_SOFT) + circle(45.5, 21, 3.6, GREY_SOFT)
    head = path("M32 15C41 15 45.5 21 45.5 29C45.5 38.5 40 45 32 45C24 45 18.5 38.5 18.5 29"
                "C18.5 21 23 15 32 15Z", INK)
    nose = path("M32 21C35 21 36.3 25 36.3 30C36.3 35 34.5 37.5 32 37.5C29.5 37.5 27.7 35 27.7 30"
                "C27.7 25 29 21 32 21Z", GREY_DARK)
    eyes = circle(24.5, 29, 2.4, GREY_DARK) + circle(39.5, 29, 2.4, GREY_DARK)
    return ears + inner + head + nose + eyes


@reg("kodelife", BLUE_GREY_DARK)
def kodelife():
    sq = rrect(15, 13, 34, 34, 5, INK)
    k = stroke("M22 18V42", HOLE, 4) + stroke("M42.5 17.5L25 30L42.5 42.5", HOLE, 4)
    return sq + k


@reg("kolourpaint", AMBER_DARK)
def kolourpaint():
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.5, HOLE) +
            circle(CX, CY, 10, ORANGE_LIGHT) + circle(CX, CY, 5.5, RED))


@reg("komodo-edit", GREY_DEEP)
@reg("komodo", ORANGE_DEEP)
def komodo():
    return _lizard()


@reg("komorebi-wallpaper-creator", LIGHT_BLUE_DEEP)
@reg("komorebi", DEEP_PURPLE_LIGHT)
def komorebi():
    return _komorebi()


@reg("kompare", TEAL_DEEP)
def kompare():
    top = rrect(18, 12, 28, 17, 3.5, INK)
    bot = rrect(18, 31.5, 28, 17, 3.5, INK)
    lines = "".join(rrect(22.5, y, 19, 2.6, 1.3, HOLE) for y in (16.5, 21.5, 36, 41))
    return top + bot + lines


@reg("konqueror", BLUE_DEEP)
def konqueror():
    teeth = "".join(g(rrect(29, 11.5, 6, 7, 1.8, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    gear = circle(CX, CY, 15, INK) + circle(CX, CY, 12, HOLE) + circle(CX, CY, 10, INK)
    land = (path("M24.5 25C27 22 30.5 21 32.5 22C31.5 24 29 24.5 29.5 27C30 29.5 27 31 24.5 30"
                 "C23.5 28.5 23.5 26.5 24.5 25Z", HOLE) +
            path("M36 24C38.5 25.5 40 28.5 39.8 32C38 31.5 36.5 32.5 36 35C35.5 37 33 38 31.5 37"
                 "C31 34.5 32.5 33 34 32C35.5 31 34 27.5 36 24Z", HOLE))
    return teeth + gear + land


@reg("kontact", ORANGE_DEEP)
def kontact():
    head = circle(32, 22.5, 7, INK)
    body = path("M17.5 45C17.5 36.5 23.5 32 32 32C40.5 32 46.5 36.5 46.5 45Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return head + body


@reg("kontact-import-wizard", AMBER_DEEP)
def kontact_import():
    back = poly([(15, 27), (32, 15), (49, 27)], INK, 3)
    card = rrect(20.5, 13, 23, 24, 2.5, INK) + rrect(20.5, 13, 23, 24, 2.5, "none",
                                                     f' stroke="{HOLE}" stroke-width="2"')
    arrow = poly([(32, 16.5), (37.5, 22.5), (34.2, 22.5), (34.2, 29), (29.8, 29), (29.8, 22.5), (26.5, 22.5)], HOLE, 1)
    env = path("M15 28L32 39L49 28V45A3 3 0 0 1 46 48H18A3 3 0 0 1 15 45Z", INK,
               f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    return back + card + arrow + env


@reg("kontena-lens", BLUE_DEEP)
def kontena_lens():
    sq = rrect(15, 13, 34, 34, 5, INK)
    r, half = 6.5, 15.5
    blades = ""
    for k in range(6):
        a = 90 + 60 * k
        vx, vy = pt(CX, CY, r, a)
        d = math.radians(a + 120)
        dx, dy = math.cos(d), math.sin(d)
        ts = [t for t in ((half - (vx - CX)) / dx if dx > 1e-9 else None,
                          (-half - (vx - CX)) / dx if dx < -1e-9 else None,
                          (half - (vy - CY)) / dy if dy > 1e-9 else None,
                          (-half - (vy - CY)) / dy if dy < -1e-9 else None) if t is not None]
        t = min(ts)
        blades += line(vx, vy, vx + dx * t, vy + dy * t, HOLE, 2.2, "butt")
    hexa = poly([pt(CX, CY, r, 90 + 60 * k) for k in range(6)], HOLE)
    return sq + blades + hexa


@reg("konversation", LIGHT_BLUE_DEEP)
def konversation():
    bubble = path("M32 13.5A16 16 0 1 1 22.5 42.5L15 46.5L17.5 38.5A16 16 0 0 1 32 13.5Z", INK)
    horn = poly([(22.5, 25), (30, 25), (40, 19.5), (40, 38.5), (30, 33), (22.5, 33)], HOLE, 2)
    handle = line(26.5, 33.5, 27.5, 39.5, HOLE, 3.2)
    return bubble + horn + handle + rrect(40.5, 26.5, 4, 5, 1.5, HOLE)


@reg("koodo-reader", BLUE_GREY_DARK)
def koodo_reader():
    k = stroke("M21.5 17V43", INK, 5.5) + stroke("M37 20.5L25 31.5L37.5 43", INK, 5.5)
    mark = path("M38 11H47V26L42.5 22.5L38 26Z", AMBER,
                f' stroke="{AMBER}" stroke-width="1.5" stroke-linejoin="round"')
    return k + mark


@reg("kopete", LIGHT_BLUE_LIGHT)
def kopete():
    bubble = path("M32 13A17 16 0 1 1 41 43.5L44.5 49L35.5 46A17 16 0 0 1 32 13Z", INK)
    face = (circle(21.5, 24.5, 2.6, HOLE) + rrect(20, 28, 13, 5.5, 2.75, HOLE) +
            cut("M36 17.5A12.5 12.5 0 1 1 36 42.5A10 12.5 0 1 0 36 17.5Z", HOLE))
    return bubble + face


@reg("kopia-ui", BLUE)
def kopia_ui():
    cloud = path("M21 43C16 43 13 39.5 13 35.5C13 31.5 16 28.5 20 28.5C20.5 21.5 26 16.5 32.5 16.5"
                 "C38.5 16.5 43 20.5 44.5 26C48.5 26.5 51 30 51 34.5C51 39 47.5 43 43 43Z", INK)
    arrow = poly([(32, 21.5), (37, 30), (34, 30), (34, 43), (30, 43), (30, 30), (27, 30)], HOLE, 1.5)
    return cloud + arrow


@reg("korganizer", TEAL_DEEP)
def korganizer():
    sheet = rrect(17, 14, 30, 34, 3.5, INK)
    top = rrect(15, 11, 34, 6.5, 3, INK) + line(17, 18.7, 47, 18.7, HOLE, 1.6, "butt")
    ring = circle(22.5, 27, 3.2, HOLE) + circle(22.5, 27, 1.4, INK)
    lines = (rrect(28, 25.7, 14, 2.6, 1.3, HOLE) + rrect(21, 33, 21, 2.6, 1.3, HOLE) +
             rrect(21, 38, 21, 2.6, 1.3, HOLE) + rrect(21, 43, 14, 2.6, 1.3, HOLE))
    return sheet + top + ring + lines


@reg("kotatogram", DEEP_PURPLE)
def kotatogram():
    return path("M32 26C35 21.5 40 20 43.5 23C46.5 25.5 48.5 29 51 29C49.5 35 44 38 38.5 36.5"
                "C35.5 35.7 33.5 33.5 32 31.5C30.5 33.5 28.5 35.7 25.5 36.5C20 38 14.5 35 13 29"
                "C15.5 29 17.5 25.5 20.5 23C24 20 29 21.5 32 26Z", INK)


@reg("kphotoalbum", BLUE_GREY_DARK)
def kphotoalbum():
    body = rrect(13.5, 19, 37, 27, 4.5, INK) + rrect(24, 14.5, 16, 7, 2.5, INK)
    lens = circle(32, 32.5, 9, HOLE) + circle(32, 32.5, 6.2, INK) + circle(32, 32.5, 3.4, BLUE_GREY_SOFT)
    return body + lens + circle(44.5, 24.5, 1.8, HOLE)


@reg("kpicosim", INDIGO_LIGHT)
def kpicosim():
    sq = rrect(16, 14, 32, 32, 4, INK)
    tri = path("M20 14H44.5L16 42.5V18A4 4 0 0 1 20 14Z", INDIGO_SOFT)
    return sq + tri


@reg("kpovmodeler", CYAN_DEEP)
def kpovmodeler():
    cyl = (rrect(14, 25, 17, 20, 2, INK) +
           '<ellipse cx="22.5" cy="45" rx="8.5" ry="3" fill="INK"/>' +
           f'<ellipse cx="22.5" cy="25" rx="8.5" ry="3" fill="{CYAN_SOFT}"/>')
    cone = path("M40 13L50.5 43.5A10.5 3.8 0 0 1 29.5 43.5Z", INK,
                f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    return cyl + cone


@reg("krdc", BLUE_DEEP)
def krdc():
    win = rrect(13, 14, 32, 27, 4, INK) + rrect(16.5, 20, 25, 17.5, 2, HOLE)
    side = rrect(19, 22.5, 4, 3, 1, INK) + rrect(19, 27.5, 4, 3, 1, INK)
    badge = circle(41.5, 39.5, 10.5, HOLE) + circle(41.5, 39.5, 8.8, INK)
    waves = (stroke("M37.5 37.5A6 6 0 0 1 43.5 43.5", HOLE, 2.2) +
             stroke("M37.5 33.5A10 10 0 0 1 47.5 43.5", HOLE, 2.2) + circle(38.5, 42.5, 1.7, HOLE))
    return win + side + badge + g(waves, "translate(-.5 -1.5)")


@reg("krecipes", BROWN)
def krecipes():
    pot = path("M14 23H44V38C44 43 40 46 35 46H23C18 46 14 43 14 38Z", INK)
    rim = f'<ellipse cx="29" cy="22" rx="16" ry="5" fill="INK"/><ellipse cx="29" cy="22" rx="12.5" ry="3" fill="{ORANGE_LIGHT}"/>'
    card = rrect(35, 29, 16, 18, 3, RED, f' stroke="{HOLE}" stroke-width="2"')
    lines = "".join(rrect(38.5, y, 9, 2.4, 1.2, INK) for y in (33.5, 37.5, 41.5))
    return pot + rim + card + lines


@reg("kregexpeditor", BLUE)
def kregexpeditor():
    frame = rrect(14, 13, 36, 34, 4.5, INK) + rrect(17.5, 21, 29, 22.5, 2, HOLE)
    blocks = (rrect(20.5, 24, 7, 11, 1.5, INK) + rrect(36.5, 24, 7, 11, 1.5, INK) +
              rrect(26.5, 31, 12, 9.5, 1.5, INK, f' stroke="{HOLE}" stroke-width="1.8"'))
    return frame + blocks


@reg("krename", BLUE_DEEP)
def krename():
    back = rrect(13.5, 25, 22, 22, 3.5, INK)
    a = stroke("M19 42.5L24.5 29.5L30 42.5", HOLE, 3) + line(21, 38, 28, 38, HOLE, 2.6)
    front = rrect(28.5, 12.5, 22, 22, 3.5, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    b = stroke("M35.5 17.5V29.5H40.5C42.5 29.5 44 28.2 44 26.4C44 24.6 42.5 23.5 40.5 23.5"
               "C42.3 23.5 43.3 22.4 43.3 20.6C43.3 18.8 42 17.5 40 17.5Z", HOLE, 2.8)
    b += line(35.5, 23.5, 40.5, 23.5, HOLE, 2.6)
    return back + a + front + b


@reg("krfb", BLUE)
def krfb():
    links = line(22, 30, 40.5, 20, INK, 3.2) + line(22, 30, 40.5, 40, INK, 3.2)
    return links + circle(22, 30, 6, INK) + circle(40.5, 20, 6, INK) + circle(40.5, 40, 6, INK)


@reg("krita", PINK)
def krita():
    wheel = circle(30, 32, 15.5, INK)
    swoosh = stroke("M17.5 36C22 42 31 44.5 38.5 40", HOLE, 3)
    brush = (line(15, 14, 36, 33, HOLE, 7) + line(15, 14, 36, 33, INK, 3.6) +
             path("M34 30.5C37.5 28.5 42 29 44 31.5C46 34 45 38 46.5 40.5C42 41.5 36.5 40 34.5 37"
                  "C33 35 32.5 32.5 34 30.5Z", INK, f' stroke="{HOLE}" stroke-width="1.8"'))
    return wheel + swoosh + brush


@reg("kronometer", LIGHT_BLUE_DEEP)
def kronometer():
    crown = g(rrect(14.5, 12, 8, 5.5, 2, INK), "rotate(-45 18.5 14.75)")
    face = circle(32.5, 31.5, 16, INK) + circle(32.5, 31.5, 12.5, HOLE) + circle(32.5, 31.5, 10.5, INK)
    dots = "".join(circle(*pt(32.5, 31.5, 7.5, a), 1.6, HOLE) for a in (0, 90, 180, 270))
    hand = line(32.5, 31.5, 37, 26, HOLE, 2.4) + circle(32.5, 31.5, 2.8, HOLE)
    return crown + face + dots + hand


@reg("kruler", AMBER_DEEP)
def kruler():
    ruler = rrect(19, 12, 26, 36, 3.5, INK)
    ticks = "".join(line(45, y, 45 - (10 if i % 2 == 0 else 6), y, HOLE, 2.2, "butt")
                    for i, y in enumerate(range(17, 45, 5)))
    return g(ruler + ticks, "rotate(-35 32 30)")


@reg("krusader_user", INDIGO_LIGHT)
@reg("krusader_root", RED_DEEP)
def krusader_root():
    return _krusader()


@reg("ksnip", DEEP_ORANGE_DEEP)
def ksnip():
    bar = poly([(16, 13), (27, 13), (27, 47), (16, 47)], INK)
    cuts = line(16, 13, 27, 30, HOLE, 1.8, "butt") + line(16, 47, 27, 30, HOLE, 1.8, "butt")
    up = poly([(29.5, 30), (47, 13), (47, 26)], INK, 1)
    down = poly([(29.5, 30), (47, 47), (47, 34)], INK, 1)
    return bar + cuts + up + down


@reg("kstars", BLUE_GREY_DARK)
def kstars():
    tube = g(rrect(16.5, 21, 31, 9, 4, INK) + rrect(13.5, 19.5, 7, 12, 2.5, INK), "rotate(28 32 26)")
    legs = (line(32, 32, 32, 48, INK, 3) + line(32, 36, 21.5, 47.5, INK, 3) +
            line(32, 36, 42.5, 47.5, INK, 3))
    return legs + circle(32, 32, 3.5, INK) + tube


@small("kolf")
def kolf_s():
    dots = "".join(circle(*pt(CX, CY, 7.5, 30 + 60 * k), 2.6, HOLE) for k in range(6))
    return circle(CX, CY, 16, INK) + dots + circle(CX, CY, 2.6, HOLE)


@small("kontena-lens")
def kontena_lens_s():
    sq = rrect(15, 13, 34, 34, 5, INK)
    return sq + poly([pt(CX, CY, 8, 90 + 60 * k) for k in range(6)], HOLE, 1.5)


@small("korganizer")
def korganizer_s():
    sheet = rrect(17, 12, 30, 36, 4, INK)
    lines = "".join(rrect(21.5, y, 21, 3.6, 1.8, HOLE) for y in (22, 30, 38))
    return sheet + lines


@small("kshisen")
def kshisen_s():
    tile = rrect(17, 12, 30, 37, 4.5, INK)
    return tile + rrect(22, 23, 20, 10, 2, HOLE) + line(32, 17, 32, 44, HOLE, 3.6)


@small("kmymoney")
def kmymoney_s():
    k = stroke("M26 17V43", INK, 5) + stroke("M41 17L28 30L41 43", INK, 5)
    return k + line(19, 30, 45, 30, INK, 3.6)


@small("knemo")
def knemo_s():
    land = (path("M18 21C22 16 28 14.5 31 15.5C30 20 27 21 26 25C24 29 21 30 17 30C16.5 27 16.5 24 18 21Z", HOLE) +
            path("M36 16C42 17.5 46.5 23 47.5 29C44 29 41 29 39 32C37.5 35 34 35 32.5 32C31 29 35 26 34.5 22Z", HOLE))
    return circle(CX, CY, 16.5, INK) + land


@small("koala")
def koala_s():
    ears = circle(18, 20, 7.5, INK) + circle(46, 20, 7.5, INK)
    head = circle(32, 31, 14.5, INK)
    nose = rrect(27.5, 22, 9, 15, 4.5, HOLE)
    return ears + head + nose


@small("knowte")
def knowte_s():
    return poly([(39, 14.5), (47.5, 23), (26, 44.5), (15, 47.5), (18, 36.5)], INK, 2.5)


@small("komorebi")
def komorebi_s():
    return rrect(15, 15, 34, 28, 4, INK) + circle(42, 38, 8.5, HOLE) + circle(42, 38, 5.5, INK)


@small("komorebi-wallpaper-creator")
def komorebi_wc_s():
    return komorebi_s()


@small("konqueror")
def konqueror_s():
    teeth = "".join(g(rrect(28.5, 11, 7, 8, 2, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    return teeth + circle(CX, CY, 15, INK) + circle(CX, CY, 7, HOLE)


@small("konquest")
def konquest_s():
    ell = ('<ellipse cx="32" cy="30" rx="18.5" ry="5.5" fill="none" stroke="INK" stroke-width="3.4" '
           'transform="rotate(-20 32 30)"/>')
    gap = g(stroke("M13.5 30A18.5 5.5 0 0 0 50.5 30", HOLE, 7.5), "rotate(-20 32 30)")
    front = g(stroke("M13.5 30A18.5 5.5 0 0 0 50.5 30", INK, 3.4), "rotate(-20 32 30)")
    return ell + circle(CX, CY, 12, INK) + gap + front


@small("kontact-import-wizard")
def kontact_import_s():
    env = rrect(14, 22, 36, 25, 4, INK)
    arrow = poly([(32, 10), (41, 20), (36, 20), (36, 33), (28, 33), (28, 20), (23, 20)], INK, 2)
    return env + stroke("M17 27L32 36L47 27", HOLE, 3) + arrow


@small("konversation")
def konversation_s():
    bubble = path("M32 13.5A16 16 0 1 1 22.5 42.5L15 46.5L17.5 38.5A16 16 0 0 1 32 13.5Z", INK)
    return bubble + poly([(22.5, 24.5), (29, 24.5), (41, 18), (41, 40), (29, 33.5), (22.5, 33.5)], HOLE, 2)


@small("kopete")
def kopete_s():
    bubble = path("M32 13A17 16 0 1 1 41 43.5L44.5 49L35.5 46A17 16 0 0 1 32 13Z", INK)
    return bubble + rrect(19.5, 26.5, 14, 6, 3, HOLE) + cut(
        "M36 16.5A13 13.5 0 1 1 36 43.5A9.5 13.5 0 1 0 36 16.5Z", HOLE)


@small("kphotoalbum")
def kphotoalbum_s():
    body = rrect(13, 19, 38, 28, 5, INK) + rrect(24, 14, 16, 8, 3, INK)
    return body + circle(32, 32.5, 8.5, HOLE) + circle(32, 32.5, 4.5, INK)


@small("kpovmodeler")
def kpovmodeler_s():
    cyl = rrect(13.5, 22, 18, 25, 5, INK)
    cone = path("M40.5 12L51 45H30Z", INK, f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"')
    return cyl + cone


@small("krdc")
def krdc_s():
    win = rrect(13, 14, 32, 27, 4, INK) + rrect(17, 21, 24, 16, 2, HOLE)
    return win + circle(42, 40, 10.5, HOLE) + circle(42, 40, 8.5, INK)


@small("krecipes")
def krecipes_s():
    pot = path("M13 22H45V38C45 43 41 46.5 36 46.5H22C17 46.5 13 43 13 38Z", INK)
    lid = rrect(11, 15, 36, 6, 3, INK)
    return pot + lid + rrect(34, 29, 17, 19, 3, RED, f' stroke="{HOLE}" stroke-width="2.4"')


@small("kregexpeditor")
def kregexpeditor_s():
    return (rrect(14, 13, 36, 34, 4.5, INK) + rrect(18.5, 22, 27, 20.5, 2, HOLE) +
            rrect(22.5, 26, 8, 12.5, 2, INK) + rrect(34, 26, 8, 12.5, 2, INK))


@small("krename")
def krename_s():
    back = rrect(13.5, 25, 22, 22, 4, INK)
    front = rrect(27.5, 12, 23, 23, 4, INK, f' stroke="{HOLE}" stroke-width="3"')
    b = stroke("M35 17.5V29.5H40.5C42.5 29.5 44 28.2 44 26.4C44 24.6 42.5 23.5 40.5 23.5"
               "C42.3 23.5 43.3 22.4 43.3 20.6C43.3 18.8 42 17.5 40 17.5Z", HOLE, 3.2)
    return back + front + b


@small("kreversi")
def kreversi_s():
    half = path("M32 13.5A16.5 16.5 0 0 1 32 46.5A8.25 8.25 0 0 1 32 30A8.25 8.25 0 0 0 32 13.5Z", INK)
    ring = circle(CX, CY, 16.5, INK) + circle(CX, CY, 14, HOLE)
    return ring + half


@small("krita")
def krita_s():
    wheel = circle(30, 32, 15.5, INK)
    brush = line(15, 14, 36, 34, HOLE, 8) + line(15, 14, 36, 34, INK, 4.2)
    tip = path("M33.5 30C37.5 27.5 42.5 28.5 44.5 32C46.5 35 45 38.5 47 41.5C42 42.5 36.5 41 34 37.5"
               "C32.5 35 32 32 33.5 30Z", INK, f' stroke="{HOLE}" stroke-width="2.4"')
    return wheel + brush + tip


@small("kronometer")
def kronometer_s():
    crown = g(rrect(14, 11.5, 9, 6.5, 2.5, INK), "rotate(-45 18.5 14.75)")
    face = circle(32.5, 31.5, 16, INK) + circle(32.5, 31.5, 11.5, HOLE)
    return crown + face + line(32.5, 31.5, 37.5, 25.5, INK, 3) + circle(32.5, 31.5, 3.5, INK)


@small("kruler")
def kruler_s():
    ruler = rrect(19, 12, 26, 36, 3.5, INK)
    ticks = "".join(line(45, y, 45 - (11 if i % 2 == 0 else 6), y, HOLE, 3, "butt")
                    for i, y in enumerate(range(18, 45, 7)))
    return g(ruler + ticks, "rotate(-35 32 30)")


def _krusader_s():
    win = rrect(14, 14, 36, 32, 4, INK) + line(14, 21, 50, 21, HOLE, 2.6, "butt")
    return win + poly([(25, 25), (40, 36), (33, 37), (25, 43)], HOLE, 2)


@small("krusader_user")
@small("krusader_root")
def krusader_root_s():
    return _krusader_s()


@small("ksame")
def ksame_s():
    wedges = ""
    for k in range(4):
        a0 = -90 - 22.5 + 90 * k
        p0, p1 = pt(CX, CY, 16.5, a0), pt(CX, CY, 16.5, a0 + 45)
        wedges += path(f"M32 30L{f(p0[0])} {f(p0[1])}A16.5 16.5 0 0 1 {f(p1[0])} {f(p1[1])}Z", INK)
    ring = circle(CX, CY, 16.5, INK) + circle(CX, CY, 13.5, HOLE)
    return ring + wedges + circle(CX, CY, 4.5, HOLE)


@small("ksirk")
def ksirk_s():
    barrel = line(16.5, 21, 45, 28, INK, 8)
    wheel = circle(26, 35, 10, INK) + circle(26, 35, 5, HOLE)
    return barrel + line(28, 36, 47.5, 46, INK, 4) + wheel


@small("ksnip")
def ksnip_s():
    bar = rrect(15, 13, 12, 34, 1.5, INK)
    up = poly([(29, 30), (48, 12.5), (48, 27)], INK, 1.5)
    down = poly([(29, 30), (48, 47.5), (48, 33)], INK, 1.5)
    return bar + up + down


@small("kspaceduel")
def kspaceduel_s():
    return (circle(CX, CY, 16.5, ORANGE) + circle(25, 24, 4.5, ORANGE_DEEP) +
            circle(38, 36, 5, ORANGE_DEEP))


@small("ksquares")
def ksquares_s():
    lines = line(17, 39, 32, 39, INK, 4) + line(32, 39, 32, 21, INK, 4) + line(32, 21, 47, 21, INK, 4)
    return lines + "".join(circle(x, y, 5, INK) for x, y in [(17, 39), (32, 39), (32, 21), (47, 21)])


@small("kstars")
def kstars_s():
    tube = g(rrect(14, 20, 34, 11, 5, INK), "rotate(28 32 26)")
    legs = line(32, 33, 21, 47.5, INK, 3.4) + line(32, 33, 43, 47.5, INK, 3.4)
    return legs + tube
