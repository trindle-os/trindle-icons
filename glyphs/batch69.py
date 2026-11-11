# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 69: tomahawk to turtleart."""
import math
from lm import (
    AMBER, AMBER_DEEP, BLACK, BLUE, BLUE_DEEP, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_LIGHT,
    BLUE_SOFT, BROWN_DARK, circle, CX, CY, CYAN, CYAN_DEEP, DEEP_PURPLE_LIGHT, f, g, GREY,
    GREY_DARK, GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INDIGO_SOFT, INK, LIGHT_BLUE,
    LIGHT_BLUE_DEEP, line, ORANGE, ORANGE_LIGHT, path, PINK, PINK_DARK, PINK_SOFT, poly, pt,
    PURPLE_DEEP, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, rrect, stroke, TEAL, YELLOW, YELLOW_DARK,
    YELLOW_SOFT,
)
from glyphs.kit import gear_l, registry

ICONS, SMALL, reg, small = registry()


@reg("tomahawk", RED)
def tomahawk():
    return (circle(CX, CY, 16.5, INK) + poly([(24, 21), (24, 39), (36, 30)], HOLE, 3)
            + rrect(36.5, 20, 5.5, 20, 2.5, HOLE))


@reg("tomato", RED_DEEP)
def tomato():
    fruit = path("M32 18C42 17 49 24 49 32.5C49 41 41.5 47.5 32 47.5C22.5 47.5 15 41 15 32.5"
                 "C15 24 22 17 32 18Z", INK)
    leaves = "".join(g(path("M32 21C34.5 17 40 15.5 45 17C41.5 21.5 36 22.5 32 21Z", AMBER),
                       f"rotate({a} 32 21)") for a in (0, 180, -35))
    stem = stroke("M32 21V13.5", AMBER, 3)
    return fruit + leaves + stem


@reg("tomb-raider", GREY_DARK)
def tomb_raider():
    t = stroke("M14.5 22H29.5M22 22V39", INK, 5)
    r = stroke("M34.5 39V22H40.5C43.5 22 45.5 24 45.5 26.8C45.5 29.6 43.5 31.5 40.5 31.5H34.5"
               "M40 31.5L46.5 39", INK, 5)
    return t + r


@reg("toolbox", TEAL)
def toolbox():
    out = ""
    for dx, dy in [(-7, -8), (0, 0), (7, 8)]:
        slab = rrect(20 + dx, 25 + dy, 24, 10, 2.5, INK) + rrect(24 + dx, 28.8 + dy, 16, 2.4, 1.2, HOLE)
        out += g(slab, f"rotate(-40 {32 + dx} {30 + dy})")
    return out


def _tor_browser():
    left = path("M32 14A16 16 0 0 0 32 46Z", INK)
    arcs = (stroke("M32 15.3A14.7 14.7 0 0 1 32 44.7", INK, 2.6) +
            stroke("M32 20.5A9.5 9.5 0 0 1 32 39.5", INK, 2.6))
    dot = path("M32 25.5A4.5 4.5 0 0 1 32 34.5Z", INK)
    return left + arcs + dot


@reg("tor-browser-nightly", BLUE_DEEP)
@reg("tor-browser-alpha", TEAL)
def tor_browser_alpha():
    return _tor_browser()


def _pillar(x):
    return poly([(x - 4.5, 21), (x + 4.5, 21), (x + 2.5, 25), (x + 2.5, 42), (x + 4.5, 46),
                 (x - 4.5, 46), (x - 2.5, 42), (x - 2.5, 25)], INK, 1.5)


@reg("torchlight-2", BLUE_DEEP)
def torchlight_2():
    t = poly([(23, 13), (25, 16), (44, 16), (48, 13), (47.5, 20), (35, 20), (35, 42), (37, 46),
              (27, 46), (29, 42), (29, 20), (24, 20), (22.5, 16)], ORANGE_LIGHT, 1.5)
    return _pillar(19) + _pillar(45) + t


@reg("torcs", RED_DEEP)
def torcs():
    flag = path("M14 13C22 17 32 19 44 18.5C41 22.5 33 24 25 24.5L22.5 40C19 36 17 30 17.5 24"
                "C17 20 15.5 16 14 13Z", INK)
    wheel = (circle(37, 37, 11, INK) + circle(37, 37, 6, HOLE) +
             path("M37 37V33A4 4 0 1 1 33 37Z", INK))
    return flag + wheel


@reg("torguard", DEEP_PURPLE_LIGHT)
def torguard():
    shackle = stroke("M23 30V22.5A9 9 0 0 1 41 22.5V30", INK, 4.2)
    cloud = (circle(22, 37.5, 7.5, INK) + circle(33, 32, 10, INK) + circle(43, 37.5, 6.5, INK)
             + rrect(14.5, 37, 35, 9, 4.5, INK))
    arcs = "".join(stroke(f"M22 {44 - r}A{r} {r} 0 0 1 {22 + r} 44", HOLE, 2.4) for r in (5, 10, 15))
    return shackle + cloud + arcs


@reg("toribash", RED)
def toribash():
    dots = circle(32, 16, 4.8, INK) + circle(21.5, 16.5, 2.8, INK) + circle(42.5, 16.5, 2.8, INK)
    body = circle(34, 31, 10.5, INK) + circle(17, 31, 2.2, INK)
    limb = stroke("M32 19V41", RED_DARK, 5.5) + circle(33, 42.5, 5.5, RED_DARK)
    return dots + body + limb


@reg("torii-srs", BLUE_DEEP)
def torii():
    top = path("M13 14.5Q32 19 51 14.5L49.5 20.5Q32 23.5 14.5 20.5Z", INK,
               f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    beam = rrect(16, 27, 32, 4, 1.5, INK)
    posts = rrect(20, 21, 4.5, 26.5, 1.5, INK) + rrect(39.5, 21, 4.5, 26.5, 1.5, INK)
    mid = rrect(29.8, 21, 4.4, 7, 1, INK)
    return top + beam + posts + mid


@reg("tormessenger", GREY_DEEP)
def tormessenger():
    bubble = circle(33, 29, 16, INK) + poly([(19, 35), (16, 47), (27, 42)], INK, 2.5)
    p = (f'<circle cx="34.5" cy="27" r="5.8" fill="none" stroke="{HOLE}" stroke-width="4.2"/>'
         + line(28.7, 27, 28.7, 41, HOLE, 4.2))
    return bubble + p


@reg("torrenttools", DEEP_PURPLE_LIGHT)
def torrenttools():
    cog = gear_l(CX, CY, 13.5, 8, 5.5, 3.5, INK, 22.5)
    inner = circle(CX, CY, 9.5, HOLE)
    arcs = (stroke("M36 36.5A7 7 0 1 1 38.5 28", INK, 2.4) +
            stroke("M33.5 33.5A3.5 3.5 0 1 1 35.5 29.5", INK, 2.4))
    return cog + inner + arcs


@reg("torrserver", BROWN_DARK)
def torrserver():
    disc = circle(CX, CY, 16, INK)
    t = stroke("M22.5 20.5H33M27.8 20.5V30", HOLE, 3.8)
    s = stroke("M42 34C40.8 32.5 39.5 32 37.5 32C35 32 33.5 33.3 33.5 35.2C33.5 39.5 42.3 37.5 42.3 42"
               "C42.3 44 40.5 45 38 45C36 45 34.3 44.3 33 43", HOLE, 3.6)
    bolt = poly([(46, 11), (30, 30.5), (35.5, 30.5), (18, 49), (38, 27), (32.5, 27)], ORANGE, 1.5)
    return disc + t + s + bolt


@reg("tortoisehg", GREY_DARK)
def tortoisehg():
    body = (rrect(27, 10.5, 10, 12, 5, INK) +
            "".join(circle(x, y, 5, INK) for x, y in [(19, 20), (45, 20), (19, 41), (45, 41)]))
    shell = circle(32, 31, 15, HOLE) + circle(32, 31, 13, INK)
    hg = stroke("M22.5 25V37M22.5 31H29.5M29.5 25V37", HOLE, 3) + (
        f'<circle cx="37.5" cy="29.5" r="3.3" fill="none" stroke="{HOLE}" stroke-width="2.8"/>'
        + stroke("M40.8 28V36C40.8 39 38 40 35 38.8", HOLE, 2.8))
    return body + shell + hg


@reg("total-war", RED_DARK)
def total_war():
    crown = poly([(15, 19), (23.5, 30), (32, 15), (40.5, 30), (49, 19), (49, 44), (15, 44)], INK, 2)
    gems = "".join(g(rrect(x - 2.4, 36.5 - 2.4, 4.8, 4.8, 0.8, HOLE), f"rotate(45 {x} 36.5)")
                   for x in (22.5, 32, 41.5))
    return crown + gems


@reg("totally-accurate-battle-simulator", BLUE_GREY_DARK)
def tabs():
    blue = poly([(32, 13), (24.5, 13), (17, 30), (24.5, 47), (32, 47)], INDIGO, 3)
    red = poly([(32, 13), (39.5, 13), (47, 30), (39.5, 47), (32, 47)], RED, 3)
    eyes = (circle(25.5, 27, 5.8, INK) + circle(38.5, 27, 5.8, INK) +
            circle(27, 28, 2.8, BLACK) + circle(40, 28, 2.8, BLACK))
    return blue + red + eyes


@reg("touchpad-indicator", GREY_DARK)
def touchpad():
    pad = rrect(15, 13, 34, 34, 5, INK)
    buttons = rrect(18.5, 36.5, 12.5, 7, 2, HOLE) + rrect(33, 36.5, 12.5, 7, 2, HOLE)
    ticks = "".join(rrect(40, y, 5.5, 2.2, 1.1, HOLE) for y in (16.5, 20.5, 24.5, 28.5))
    return pad + buttons + ticks


@reg("trackma", LIGHT_BLUE_DEEP)
def trackma():
    head = (circle(33, 33, 14, INK) + poly([(38, 11), (46.5, 24), (32, 22)], INK, 3) +
            poly([(13, 22), (27, 20.5), (21, 32)], INK, 3))
    eyes = circle(27, 34, 2.7, HOLE) + circle(39.5, 31, 2.7, HOLE)
    mouth = stroke("M29.5 41.5C31.5 43.5 33.5 40.5 35.5 42", HOLE, 2.2)
    return head + eyes + mouth


@reg("trackmania-nations-forever", GREY)
def trackmania():
    return (stroke("M14 22H24M19 22V38", INK, 4) + stroke("M28 38V22L32.8 30L37.6 22V38", INK, 4)
            + stroke("M42 38V22L50 38V22", INK, 4))


@reg("tracktion", BLUE_GREY_DEEP)
def tracktion():
    cog = gear_l(CX, CY, 13, 6, 9, 5, INK)
    return cog + stroke("M25 23.5H39M32 23.5V38", HOLE, 5)


@reg("tracktion-download-manager", BLUE_DEEP)
def tracktion_dm():
    return circle(CX, CY, 16.5, INK) + gear_l(CX, CY, 8.5, 8, 4.4, 3, HOLE, 22.5)


@reg("transmageddon", BLUE_GREY_DEEP)
def transmageddon():
    film = rrect(15, 11, 25, 34, 3, INK)
    holes = "".join(rrect(17.5, y, 3.2, 3.2, 0.8, HOLE) for y in (14.5, 20.5, 26.5, 32.5, 38.5))
    frame = rrect(23.5, 14.5, 13.5, 27, 1.5, HOLE)
    badge = circle(41, 40, 10.5, HOLE) + circle(41, 40, 8.8, INK)
    arrow = (stroke("M45.2 40A4.2 4.2 0 1 1 43.6 36.7", HOLE, 2.4) +
             poly([(42, 34), (46.5, 34.5), (44.5, 38.5)], HOLE, 1))
    return film + holes + frame + badge + arrow


def _transmission():
    lid = rrect(13.5, 12, 37, 8, 4, INK)
    body = rrect(16.5, 22, 31, 25, 3, INK)
    arrow = rrect(29, 22, 6, 9, 0, HOLE) + poly([(22, 30), (42, 30), (32, 40.5)], HOLE, 2)
    return lid + body + arrow


@reg("transmission", RED)
def transmission():
    return _transmission()


@reg("transmission-remote-gtk", RED_DEEP)
def transmission_remote():
    badge = circle(43, 40, 10.5, HOLE) + circle(43, 40, 8.8, INK)
    rss = (circle(39.5, 43.5, 1.8, HOLE) + stroke("M38.5 38A5.5 5.5 0 0 1 45 44.5", HOLE, 2.2) +
           stroke("M38.5 33.5A10 10 0 0 1 49.5 44.5", HOLE, 2.2))
    return _transmission() + badge + rss


@reg("trashindicator", CYAN_DEEP)
def trashindicator():
    lid = rrect(14.5, 15, 35, 5, 2.5, INK) + rrect(27, 11, 10, 6, 2, INK)
    can = poly([(17.5, 23), (46.5, 23), (43.5, 47), (20.5, 47)], INK, 2.5)
    slots = "".join(rrect(x, 27, 3.2, 15.5, 1.6, HOLE) for x in (24, 30.4, 36.8))
    return lid + can + slots


@reg("trelby", PURPLE_DEEP)
def trelby():
    body = poly([(15, 16), (42, 12), (49, 20), (25, 48), (16, 48)], INK, 3)
    band = poly([(16, 36), (37, 30), (34.5, 33.5), (16, 40)], HOLE, 1)
    flap = poly([(49, 20), (50, 25.5), (29, 48), (25, 48)], PURPLE_SOFT, 2)
    return body + band + flap


@reg("trello", LIGHT_BLUE_DEEP)
def trello():
    return (rrect(14, 12, 36, 36, 6, INK) + rrect(18.5, 16.5, 11.5, 26.5, 3, HOLE)
            + rrect(34, 16.5, 11.5, 16, 3, HOLE))


@reg("tresorit", BLUE_GREY_DEEP)
def tresorit():
    cube = poly([(32, 12), (48, 20.5), (48, 38.5), (32, 47), (16, 38.5), (16, 20.5)], INK, 3)
    band = poly([(16, 24), (35.5, 13.8), (40.5, 16.4), (16, 29.5)], CYAN, 1)
    edges = stroke("M16 20.5L32 29L48 20.5M32 29V47", HOLE, 2.2)
    return cube + band + edges


@reg("tribler", RED)
def tribler():
    head = circle(28.5, 17, 5, INK) + circle(36.5, 18.5, 4.2, INK) + rrect(28, 14.5, 9, 7, 3, INK)
    body = path("M26 25.5H33.5C33.5 33 36 39.5 41 44.5C39.5 46.5 37.5 47 35.5 46"
                "C32.5 42.5 30.8 38.5 29.8 34C28.8 39.5 26.5 44 22.5 47.5C20.5 47.5 19.3 46.5 19.5 44.5"
                "C24 39 26 32.5 26 25.5Z", INK)
    return head + body


@reg("trilium", LIGHT_BLUE_DEEP)
def trilium():
    leaf = path("M0 0C5 -8 15 -9.5 21 0C15 9.5 5 8 0 0Z", INK) + stroke("M2 0H16", HOLE, 2.2)
    return "".join(g(leaf, f"translate({f(x)} {f(y)}) rotate({a})")
                   for x, y, a in [(30, 30, 190), (33.5, 29, -40), (32, 32.5, 95)])


@reg("trillian", PINK_DARK)
def trillian():
    out = ""
    for x, y in [(25.5, 23.5), (38.5, 36.5)]:
        out += circle(x, y, 11.5, INK)
    for x, y in [(25.5, 23.5), (38.5, 36.5)]:
        out += (f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
                + circle(x + 2.3, y - 2.3, 3.2, HOLE))
    return out


@reg("trimage", BLUE_DEEP)
def trimage():
    cone = path("M42 12L14 37C24 46 38 50 50 47Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    lines = stroke("M42 13L27 44", HOLE, 2.4) + stroke("M42 13L39 48", HOLE, 2.4)
    return cone + lines


def _t_serif():
    return path("M15 13H49V22.5C47.5 19 45 17.8 40.5 17.8H35.5V41.5C35.5 44 37 45.3 39.5 45.5V48H24.5"
                "V45.5C27 45.3 28.5 44 28.5 41.5V17.8H23.5C19 17.8 16.5 19 15 22.5Z", INK,
                f' stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"')


@reg("trine", AMBER_DEEP)
def trine():
    return _t_serif()


@reg("trine2", AMBER_DEEP)
def trine2():
    two = stroke("M40.5 36.5C40.5 34 42.5 32.5 45 32.5C47.5 32.5 49.3 34.2 49.3 36.4"
                 "C49.3 39.5 45.5 42.5 41 47H50", INK, 3.4)
    return g(_t_serif(), "translate(28 30) scale(.85) translate(-32 -30)") + two


@reg("trine3", DEEP_PURPLE_LIGHT)
def trine3():
    three = stroke("M40.8 34C41.8 32.8 43.2 32.3 45 32.3C47.4 32.3 49 33.8 49 35.8C49 38 47.2 39.5 44.5 39.5"
                   "C47.3 39.5 49.4 41 49.4 43.4C49.4 45.8 47.4 47.4 44.8 47.4C42.9 47.4 41.3 46.8 40.3 45.5",
                   INK, 3.4)
    return g(_t_serif(), "translate(28 30) scale(.85) translate(-32 -30)") + three


@reg("trinity-desktop", GREY_DARK)
def trinity():
    out = ""
    for k in range(34):
        th = 0.55 * k
        r = 2.2 + 0.46 * k
        x, y = CX + r * math.cos(th - 1.2), CY + r * math.sin(th - 1.2)
        out += circle(x, y, 1.2 + 0.045 * k, INK)
    return out


@reg("trojita", BLUE_DEEP)
def trojita():
    flap = poly([(14, 27), (32, 13), (50, 27)], INK, 2.5)
    card = rrect(19.5, 16.5, 25, 19, 2.5, HOLE)
    at = (f'<circle cx="32" cy="25.5" r="3" fill="none" stroke="{INK}" stroke-width="2.4"/>'
          + stroke("M35 24.5V27C35 29 37.5 29 38 27A6.3 6.3 0 1 0 35.5 30.8", INK, 2.4))
    pocket = path("M14 28L32 39L50 28V44A3 3 0 0 1 47 47H17A3 3 0 0 1 14 44Z", INK)
    return flap + card + at + pocket


@reg("true-combat-elite", GREY_DARK)
def true_combat_elite():
    petals = ""
    for s in (-1, 1):
        px = 32 + s * 3
        for a in (-62, -38, -14, 14, 38, 62):
            ang = (180 - a) if s < 0 else a
            x, y = pt(px, 30, 11.5, ang)
            petals += g(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="6.5" ry="2.6" fill="{YELLOW_DARK}"/>',
                        f"rotate({f(ang)} {f(x)} {f(y)})")
    tc = "M22 22H30M26 22V39M41.5 24.5C40.5 22.8 39.2 22 37.3 22C34.8 22 33.2 24 33.2 27V34C33.2 37 34.8 39 37.3 39C39.2 39 40.5 38.2 41.5 36.5"
    return petals + stroke(tc, HOLE, 8) + stroke(tc, INK, 4.2)


@reg("truecrypt", INDIGO_DARK)
def truecrypt():
    lit = {(0, 2), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (4, 2), (2, 4), (3, 4), (4, 3),
           (2, 0), (0, 4)}
    out = rrect(14, 12, 36, 36, 6, INDIGO)
    for r in range(5):
        for c in range(5):
            out += circle(19.2 + c * 6.4, 17.2 + r * 6.4, 2.4, INK if (r, c) in lit else INDIGO_SOFT)
    return out


@reg("tumblr", BLUE_GREY_DARK)
def tumblr():
    return stroke("M29.5 13V35.5C29.5 41 32 43.5 36.5 43.5H41M23.5 23.5H39", INK, 6.5)


@reg("tumiki-fighters", BLUE_GREY_DARK)
def tumiki():
    tri = poly([(29, 13), (29, 28), (15, 28)], YELLOW, 3)
    tri_in = poly([(26, 19.5), (26, 25), (20.5, 25)], YELLOW_SOFT, 1.5)
    sq = ""
    for (x, y), c, ci in [((34.5, 13.5), BLUE_LIGHT, BLUE_SOFT), ((14.5, 33.5), BLUE, BLUE_SOFT),
                          ((34.5, 33.5), PINK, PINK_SOFT)]:
        sq += rrect(x, y, 15, 15, 3, c) + rrect(x + 3.5, y + 3.5, 8, 8, 1.5, ci)
    return tri + tri_in + sq


@reg("tupitube.desk", BLUE_DEEP)
def tupitube():
    return path("M16 47C21 32 31 19 44 12C38 19.5 34 25.5 31.5 30C37 26 43.5 23.5 51 23"
                "C44 27 37.5 32.5 32 37.5C37.5 36.5 43 38 47 42C39 41.5 28 42.5 19.5 48Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')


@reg("turbowarp", RED)
def turbowarp():
    t = "M20.5 20.5H43.5M32 20.5V40"
    return stroke(t, INK, 13) + stroke(t, HOLE, 8) + stroke(t, INK, 2.6)


@reg("turtleart", LIGHT_BLUE)
def turtleart():
    limbs = (circle(32, 13.5, 5, INK) +
             "".join(circle(x, y, 4.5, INK) for x, y in [(18.5, 21), (45.5, 21), (19.5, 42), (44.5, 42)]))
    shell = circle(32, 31, 15, HOLE) + circle(32, 31, 13, INK)
    pent = [pt(32, 31, 5.5, -90 + 72 * k) for k in range(5)]
    pat = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pent) + "Z", HOLE, 2.3)
    pat += "".join(stroke(f"M{f(x)} {f(y)}L{f(pt(32, 31, 12, -90 + 72 * k)[0])} {f(pt(32, 31, 12, -90 + 72 * k)[1])}",
                          HOLE, 2.3) for k, (x, y) in enumerate(pent))
    return g(limbs + shell + pat, "rotate(-12 32 30)")


@small("trackmania-nations-forever")
def trackmania_s():
    return stroke("M14 21H27M20.5 21V40", INK, 5) + stroke("M32 40V21L39 32L46 21V40", INK, 5)


@small("trinity-desktop")
def trinity_s():
    out = ""
    for k in range(12):
        th = 0.95 * k
        r = 3 + 1.15 * k
        x, y = CX + r * math.cos(th - 1.2), CY + r * math.sin(th - 1.2)
        out += circle(x, y, 1.9 + 0.12 * k, INK)
    return out


@small("truecrypt")
def truecrypt_s():
    lit = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}
    out = rrect(14, 12, 36, 36, 6, INDIGO)
    for r in range(3):
        for c in range(3):
            out += circle(21 + c * 11, 19 + r * 11, 4, INK if (r, c) in lit else INDIGO_SOFT)
    return out


@small("true-combat-elite")
def true_combat_elite_s():
    petals = ""
    for s in (-1, 1):
        for a in (-45, 0, 45):
            ang = (180 - a) if s < 0 else a
            x, y = pt(32 + s * 3, 30, 12.5, ang)
            petals += g(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="6.5" ry="3.4" fill="{YELLOW_DARK}"/>',
                        f"rotate({f(ang)} {f(x)} {f(y)})")
    tc = "M21 21H30M25.5 21V40M42.5 24C41.5 22 40 21 38 21C35 21 33.5 23.5 33.5 27V34C33.5 37.5 35 40 38 40C40 40 41.5 39 42.5 37"
    return petals + stroke(tc, HOLE, 9) + stroke(tc, INK, 5)


@small("transmageddon")
def transmageddon_s():
    film = rrect(14, 11, 26, 34, 3, INK) + rrect(22, 15, 14, 26, 1.5, HOLE)
    badge = circle(42, 40, 11, HOLE) + circle(42, 40, 9.5, INK)
    arrow = stroke("M46.5 40A4.5 4.5 0 1 1 44.8 36.5", HOLE, 3) + poly([(42.5, 33.5), (48, 34), (45.5, 39)], HOLE, 1)
    return film + badge + arrow


@small("transmission-remote-gtk")
def transmission_remote_s():
    badge = circle(43, 40, 11, HOLE) + circle(43, 40, 9.5, INK)
    rss = circle(39.5, 43.5, 2.2, HOLE) + stroke("M38.5 36.5A7.5 7.5 0 0 1 46.5 44.5", HOLE, 3)
    return _transmission() + badge + rss


@small("toolbox")
def toolbox_s():
    return "".join(g(rrect(19 + dx, 25 + dy, 26, 10, 3, INK), f"rotate(-40 {32 + dx} {30 + dy})")
                   for dx, dy in [(-7.5, -8.5), (0, 0), (7.5, 8.5)])


@small("trilium")
def trilium_s():
    leaf = path("M0 0C5 -9 15 -10.5 21 0C15 10.5 5 9 0 0Z", INK)
    return "".join(g(leaf, f"translate({f(x)} {f(y)}) rotate({a})")
                   for x, y, a in [(30, 30, 190), (33.5, 29, -40), (32, 32.5, 95)])


@small("torguard")
def torguard_s():
    shackle = stroke("M23 30V22A9 9 0 0 1 41 22V30", INK, 5)
    cloud = (circle(22, 37.5, 7.5, INK) + circle(33, 32, 10, INK) + circle(43, 37.5, 6.5, INK)
             + rrect(14.5, 37, 35, 9, 4.5, INK))
    arcs = "".join(stroke(f"M22 {44 - r}A{r} {r} 0 0 1 {22 + r} 44", HOLE, 3.2) for r in (6, 13))
    return shackle + cloud + arcs


@small("tortoisehg")
def tortoisehg_s():
    body = (rrect(27, 10, 10, 12, 5, INK) +
            "".join(circle(x, y, 5.5, INK) for x, y in [(18.5, 19.5), (45.5, 19.5), (18.5, 41.5), (45.5, 41.5)]))
    shell = circle(32, 31, 15.5, HOLE) + circle(32, 31, 13.5, INK)
    return body + shell + stroke("M26 24.5V37.5M26 31H38M38 24.5V37.5", HOLE, 4)


@small("turtleart")
def turtleart_s():
    limbs = (circle(32, 13, 5.5, INK) +
             "".join(circle(x, y, 5, INK) for x, y in [(18, 20.5), (46, 20.5), (19, 42.5), (45, 42.5)]))
    shell = circle(32, 31, 15.5, HOLE) + circle(32, 31, 13.5, INK)
    pent = [pt(32, 31, 6, -90 + 72 * k) for k in range(5)]
    pat = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pent) + "Z", HOLE, 3)
    return g(limbs + shell + pat, "rotate(-12 32 30)")


@small("trillian")
def trillian_s():
    out = circle(25, 23, 12, INK) + circle(39, 37, 12, INK)
    return out + circle(25, 23, 5.5, HOLE) + circle(39, 37, 5.5, HOLE)


@small("torrserver")
def torrserver_s():
    return circle(CX, CY, 16.5, INK) + poly([(44, 12), (29, 31), (35, 31), (20, 48), (39, 27), (33, 27)],
                                            ORANGE, 2.5)


@small("torrenttools")
def torrenttools_s():
    cog = gear_l(CX, CY, 13.5, 8, 6.5, 4, INK, 22.5)
    return cog + circle(CX, CY, 8.5, HOLE) + stroke("M35.5 35A5 5 0 1 1 37 28", INK, 3.2)


@small("trojita")
def trojita_s():
    flap = poly([(14, 27), (32, 13), (50, 27)], INK, 2.5)
    card = rrect(19.5, 16.5, 25, 19, 2.5, HOLE) + circle(32, 25, 4, INK)
    pocket = path("M14 28L32 39L50 28V44A3 3 0 0 1 47 47H17A3 3 0 0 1 14 44Z", INK)
    return flap + card + pocket


@small("touchpad-indicator")
def touchpad_s():
    pad = rrect(14, 12, 36, 36, 5.5, INK)
    return pad + rrect(18, 35.5, 13, 8.5, 2.5, HOLE) + rrect(33, 35.5, 13, 8.5, 2.5, HOLE) + \
        rrect(39.5, 16, 6.5, 3.2, 1.6, HOLE) + rrect(39.5, 23, 6.5, 3.2, 1.6, HOLE)


@small("tracktion-download-manager")
def tracktion_dm_s():
    return circle(CX, CY, 16.5, INK) + gear_l(CX, CY, 8.5, 6, 5.5, 3.5, HOLE)
