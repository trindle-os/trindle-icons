# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 11: bootstrap-studio to calf.

Same rules as batch01: tile from the palette step nearest the brand
colour, mark in INK, HOLE for cut-throughs, any second shade another
palette step.
"""
from lm import *
from glyphs.kit import gear_b, registry, ring_b
from glyphs.kit import shared_brave

ICONS, SMALL, reg, small = registry()

def pixels(rows, x0, y0, u, colour):
    """Pixel art: one rect per horizontal run of X in each row."""
    out = ""
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            if row[c] == "X":
                s = c
                while c < len(row) and row[c] == "X":
                    c += 1
                out += rrect(x0 + s * u - .2, y0 + r * u - .2, (c - s) * u + .4, u + .4, 0, colour)
            else:
                c += 1
    return out

@reg("bootstrap-studio", PURPLE_DEEP)
def bootstrap_studio():
    return (rrect(24, 12, 25, 25, 4.5, PINK_SOFT) + rrect(20, 16, 25, 25, 4.5, PURPLE_SOFT)
            + rrect(15, 21, 26, 26, 4.5, INK))

@reg("boxy-svg", BLUE_DEEP)
def boxy_svg():
    hexa = poly([pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)], INK, 3)
    rays = "".join(line(*pt(CX, CY, 3, 22.5 + 45 * k), *pt(CX, CY, 8.5, 22.5 + 45 * k), HOLE, 3.2)
                   + circle(*pt(CX, CY, 9, 22.5 + 45 * k), 2.6, HOLE) for k in range(8))
    return hexa + rays + circle(CX, CY, 3.6, HOLE)

@reg("bpython", BLUE_DEEP)
def bpython():
    b = stroke("M19.5 13V35.5H25.5A5.5 5.5 0 0 0 25.5 24.5H19.5", INK, 5)
    p = stroke("M35 46.5V24.5H41A5.5 5.5 0 0 1 41 35.5H35", BLUE_SOFT, 5)
    return b + p

def _pixb():
    rows = ["XXXX.", "XX.XX", "XX.XX", "XXXX.", "XX.XX", "XX.XX", "XXXX."]
    return pixels(rows, 19.5, 12.5, 5, INK)

@reg("bpytop", CYAN_DARK)
def bpytop():
    return _pixb()

@reg("btop", RED_DEEP)
def btop():
    return _pixb()

def _brackets():
    frame = rrect(14, 12, 36, 36, 6, INK) + rrect(18.5, 16.5, 27, 27, 3, HOLE)
    left = path("M22 20.5H29.5V25H26.5V35H29.5V39.5H22Z", INK)
    right = path("M42 20.5H34.5V25H37.5V35H34.5V39.5H42Z", INK)
    return frame + left + right

@reg("brackets", BLUE)
def brackets():
    return _brackets()

@reg("brackets-electron", DEEP_ORANGE)
def brackets_electron():
    return _brackets()

@reg("braindump", ORANGE_DEEP)
def braindump():
    bulb = path("M32 11A12.5 12.5 0 0 1 39 34C38 35 38 36 38 37.5H26C26 36 26 35 25 34"
                "A12.5 12.5 0 0 1 32 11Z", INK)
    bolt = poly([(33.5, 15), (26.5, 26), (31.5, 26), (30, 33), (37.5, 22), (32.5, 22)], HOLE, 1.4)
    base = rrect(25.5, 39.5, 13, 3.2, 1.6, INK) + rrect(27, 44, 10, 3.2, 1.6, INK)
    return bulb + bolt + base

def _brave():
    return shared_brave()

@reg("brave-browser-dev", BLUE_DEEP)
def brave_dev():
    return _brave()

@reg("brave-browser-nightly", PURPLE)
def brave_nightly():
    return _brave()

@reg("btrfs-assistant", ORANGE_DEEP)
def btrfs_assistant():
    wheel = gear_b(CX, CY, 18, 14, INK) + circle(CX, CY, 10.5, HOLE)
    tree = (stroke("M27 24.5V35.5M27 30H37V35.5", INK, 2.6)
            + rrect(24, 21.5, 6, 5.5, 1.8, INK) + rrect(24, 33, 6, 5.5, 1.8, INK)
            + rrect(34, 33, 6, 5.5, 1.8, INK))
    return wheel + tree

@reg("btsync-gui", LIGHT_BLUE_DEEP)
def btsync():
    top = stroke("M18.5 26A14 14 0 0 1 43 21", INK, 4)
    bot = stroke("M45.5 34A14 14 0 0 1 21 39", INK, 4)
    heads = (poly([(46.5, 15.5), (47, 25), (38.5, 22.5)], INK, 2)
             + poly([(17.5, 44.5), (17, 35), (25.5, 37.5)], INK, 2))
    return top + bot + heads

@reg("bubblemail", INDIGO_DEEP)
def bubblemail():
    bubble = (rrect(14, 20, 30, 21, 6, INK)
              + poly([(20, 38), (27, 38), (19.5, 46)], INK, 2.5))
    env = rrect(29, 11.5, 21, 15, 3, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    flap = stroke("M31.5 14.5L39.5 20.5L47.5 14.5", HOLE, 2.2)
    return bubble + env + flap

@reg("buho", PURPLE_LIGHT)
def buho():
    frame = rrect(18, 12, 28, 36, 4.5, INK)
    bands = "".join(rrect(21.5, 15.5 + 6 * k, 21, 5, 1, c) for k, c in
                    enumerate([BLUE_SOFT, PURPLE_SOFT, PINK_SOFT, AMBER_SOFT, INK]))
    return frame + bands

@reg("builder", AMBER_DEEP)
def builder():
    base = rrect(16, 44, 20, 4, 1.5, INK)
    column = rrect(21, 31, 10, 14, 1.5, INK)
    arm = line(26, 31, 40, 18, INK, 6)
    joint = circle(26, 31, 9, INK) + circle(26, 31, 5, HOLE)
    elbow = circle(40, 18, 5.5, INK) + circle(40, 18, 2.2, HOLE)
    claw = stroke("M43.5 21.5L47 25M44.5 22.5L50 22V16.5M47 25L45.5 29.5", INK, 2.6)
    return base + column + arm + joint + elbow + claw

@reg("buka", INDIGO_DEEP)
def buka():
    pages = (path("M31 19C27 16 21 15.5 15 16.5V42C21 41 27 41.5 31 44Z", INK)
             + path("M33 19C37 16 43 15.5 49 16.5V42C43 41 37 41.5 33 44Z", INK))
    inner = (path("M28.5 21.5C25.5 19.8 22 19.3 18 19.8V38.5C22 38.2 25.5 38.8 28.5 40Z", HOLE)
             + path("M35.5 21.5C38.5 19.8 42 19.3 46 19.8V38.5C42 38.2 38.5 38.8 35.5 40Z", HOLE))
    return pages + inner

@reg("bulky", BLUE_GREY_DEEP)
def bulky():
    box = rrect(14.5, 22, 34, 16, 3, "none", f' stroke="{INK}" stroke-width="3"')
    bar = rrect(18.5, 26, 14, 8, 1.5, INK)
    gap = rrect(35, 18, 8, 24, 0, HOLE)
    beam = (line(39, 16, 39, 44, INK, 3.2) + line(34.5, 16, 43.5, 16, INK, 3.2)
            + line(34.5, 44, 43.5, 44, INK, 3.2))
    return box + bar + gap + beam

@reg("bum", DEEP_ORANGE_DEEP)
def bum():
    return (gear_b(CX, CY, 17.5, 13.5, INK) + circle(CX, CY, 10.5, HOLE)
            + stroke("M32 22.8A7.2 7.2 0 1 0 39.2 30", AMBER_LIGHT, 2.6)
            + circle(CX, CY, 5.8, INK))

@reg("burp", DEEP_ORANGE)
def burp():
    body = rrect(15, 13, 34, 34, 5, INK)
    left = path("M20 13H32V47H20A5 5 0 0 1 15 42V18A5 5 0 0 1 20 13Z", DEEP_ORANGE_DARK)
    bolt = stroke("M37.5 15V25.5L32.5 30.5H40.5L35.5 36V45", HOLE, 3)
    return body + left + bolt

@reg("buttercup-desktop", TEAL_LIGHT)
def buttercup():
    body = (circle(26, 23, 11, INK) + rrect(15, 23, 23, 24, 7, INK)
            + circle(40, 35.5, 10.5, INK) + rrect(26, 36, 20, 11, 7, INK))
    dome = path("M18.5 26.5A7.5 7.5 0 0 1 33.5 26.5Z", HOLE)
    key = circle(26.5, 35, 3.3, HOLE) + rrect(24.8, 35, 3.4, 7.5, 1.7, HOLE)
    return body + dome + key

@reg("bwfmetaedit", LIGHT_BLUE_DEEP)
def bwfmetaedit():
    sheet = path("M18 12H38L48 22V45A3 3 0 0 1 45 48H18A3 3 0 0 1 15 45V15A3 3 0 0 1 18 12Z", INK)
    fold = path("M38 12V19A3 3 0 0 0 41 22H48Z", LIGHT_BLUE_SOFT)
    fa = stroke("M20 31V21H26.5M20 26H25.5M29 31L32.5 21L36 31M30.2 27.5H34.8", HOLE, 2.4)
    dgi = stroke("M20 44V34H22.5C25.5 34 27 36 27 39C27 42 25.5 44 22.5 44Z"
                 "M36.5 35C35.8 34.3 35 34 34 34C31.5 34 30 36 30 39C30 42 31.5 44 34 44"
                 "C35.5 44 36.8 43.3 36.8 41V39.5H34.5M40.5 34V44", HOLE, 2.4)
    return sheet + fold + fa + dgi

@reg("byobu", DEEP_ORANGE_LIGHT)
def byobu():
    win = rrect(13.5, 15, 37, 30, 4, INK)
    split = rrect(35, 15, 2.2, 30, 0, HOLE)
    dollar = (stroke("M27 22.5C26 21.5 24.5 21 23 21C20.5 21 19 22.3 19 24C19 28 27.5 26 27.5 30.5"
                     "C27.5 32.5 25.8 33.5 23.2 33.5C21.5 33.5 19.8 33 18.5 31.8", HOLE, 2.6)
              + line(23.2, 18.5, 23.2, 36, HOLE, 2.4))
    under = rrect(29, 32, 4, 2.6, 0.8, HOLE)
    return win + split + dollar + under

@reg("box", BLUE_DEEP)
def box():
    b = stroke("M14.5 20V38.5M14.5 32.5A6 6 0 1 0 26.5 32.5A6 6 0 1 0 14.5 32.5", INK, 3.6)
    o = ring_b(35, 32.5, 6, INK, 3.6)
    x = stroke("M44 16L50 22M50 16L44 22", INK, 3.4)
    return b + o + x

@reg("brosix", BLUE)
def brosix():
    rim = ring_b(CX, CY, 15.5, INK, 2.8)
    disc = circle(CX, CY, 12, INK)
    b = stroke("M29 23V37H34A3.5 3.5 0 0 0 34 30H29M29 30H33.5A3.5 3.5 0 0 0 33.5 23H29", HOLE, 3)
    bars = line(22.5, 26.5, 25.5, 26.5, HOLE, 2.4) + line(22.5, 33.5, 25.5, 33.5, HOLE, 2.4)
    return rim + disc + b + bars

@reg("browser360-beta", PURPLE_LIGHT)
def browser360():
    e = stroke("M22.5 31H41.5C41.5 24.5 37.5 20.5 32 20.5C26.5 20.5 22.5 25 22.5 31"
               "C22.5 37 26.5 41.5 32 41.5C35.5 41.5 38.5 40 40.5 37.5", INK, 5)
    swoosh = stroke("M17.5 46C14.5 40 18.5 29 27 21C35 13.5 44 11 47.5 14.5", INK, 3)
    return swoosh + e

@reg("cacher", BLUE_DEEP)
def cacher():
    return (circle(CX, CY, 16.5, INK)
            + stroke("M24.5 24.5L19.5 30L24.5 35.5M39.5 24.5L44.5 30L39.5 35.5M34.5 22L29.5 38", HOLE, 3.4))

@reg("cache", AMBER_DEEP)
def cache():
    return poly([(36, 11), (21, 32.5), (30.5, 32.5), (27.5, 49), (43, 26.5), (33.5, 26.5), (37.5, 11)], INK, 2)

def _vault():
    disc = circle(CX, CY, 16.5, INK)
    mark = (path("M24.5 44.5L26.5 19C27 13.5 31.5 13 33.5 17L44 41L41.5 42.5L31.5 22.5L29.5 45.5Z", HOLE,
                 f' stroke="{HOLE}" stroke-width="1.2" stroke-linejoin="round"'))
    return disc + mark

@reg("borderlands", RED_DEEP)
def borderlands():
    return _vault()

@reg("borderlands-2", RED_DARK)
def borderlands2():
    return _vault()

@reg("borderlands-the-pre-sequel", BLUE_DEEP)
def borderlands_tps():
    return _vault()

@reg("boswars", ORANGE_DARK)
def boswars():
    turret = path("M22 25A8 7.5 0 0 1 38 25Z", INK)
    barrel = rrect(35, 20, 15, 3.4, 1.7, INK)
    hull = poly([(14, 27), (46, 27), (44, 33), (16, 33)], INK, 2)
    tracks = rrect(16, 34.5, 32, 10, 5, INK)
    wheels = "".join(circle(x, 39.5, 2.6, HOLE) for x in (21.5, 28, 34.5, 41))
    return turret + barrel + hull + tracks + wheels

@reg("bovo", BLUE_DEEP)
def bovo():
    grid = (line(26, 13, 26, 47, INK, 3) + line(38, 13, 38, 47, INK, 3)
            + line(15, 24, 49, 24, INK, 3) + line(15, 36, 49, 36, INK, 3))
    o1 = ring_b(20, 18.5, 3.2, BLUE_SOFT, 2.4)
    o2 = ring_b(44, 41.5, 3.2, BLUE_SOFT, 2.4)
    x = stroke("M29.5 26.5L34.5 32.5M34.5 26.5L29.5 32.5", RED_SOFT, 2.6)
    return grid + o1 + o2 + x

def _bridge(post_l=INK, post_r=INK):
    posts = rrect(13.5, 13, 5.5, 34, 2.5, post_l) + rrect(45, 13, 5.5, 34, 2.5, post_r)
    truss = stroke("M21.5 37.5H42.5M21.5 37.5L32 23.5L42.5 37.5M32 23.5V37.5", INK, 2.8)
    nodes = "".join(circle(x, y, 3.8, INK) for x, y in [(21.5, 37.5), (32, 37.5), (42.5, 37.5), (32, 23.5)])
    return posts + truss + nodes

@reg("bridge-constructor", LIGHT_BLUE)
def bridge_constructor():
    return _bridge()

@reg("bridge-constructor-medieval", GREY_DEEP)
def bridge_medieval():
    posts = rrect(13.5, 13, 5.5, 34, 2.5, INK) + rrect(45, 13, 5.5, 34, 2.5, INK)
    deck = stroke("M19 30.5Q32 36 45 30.5", INK, 2.8)
    nodes = "".join(circle(x, y, 3.8, INK) for x, y in [(23, 32.3), (32, 33.3), (41, 32.3)])
    return posts + deck + nodes

@reg("bridge-constructor-playground", CYAN_DEEP)
def bridge_playground():
    return _bridge()

@reg("bridge-constructor-portal", BLUE_GREY)
def bridge_portal():
    return _bridge(DEEP_ORANGE_LIGHT, LIGHT_BLUE_LIGHT)

@reg("bridge-constructor-stunts", TEAL_DEEP)
def bridge_stunts():
    post = rrect(13.5, 13, 5.5, 34, 2.5, INK)
    ramp = stroke("M21.5 42L46 30", INK, 2.8)
    nodes = circle(21.5, 42, 3.8, INK) + circle(46, 30, 3.8, INK)
    wheel = f' stroke="{HOLE}" stroke-width="1.5"'
    car = g(rrect(28, 21, 18, 6, 2.5, INK) + rrect(32, 16.5, 9, 6, 2.5, INK)
            + circle(32, 27.5, 3.2, INK, wheel) + circle(42, 27.5, 3.2, INK, wheel), "rotate(-26 37 30)")
    return post + ramp + nodes + car

@reg("broforce", BLUE_GREY_DEEP)
def broforce():
    back = circle(CX, 32, 12.5, BLUE_GREY_SOFT)
    star = poly([pt(CX, 31, 18 if k % 2 == 0 else 7.2, -90 + 36 * k) for k in range(10)], INK, 1.5)
    shade = "".join(poly([(CX, 31), pt(CX, 31, 18, -90 + 72 * k), pt(CX, 31, 7.2, -54 + 72 * k)],
                         BLUE_GREY_SOFT, 0.5) for k in range(5))
    return back + star + shade

@reg("broken-age", BLUE_GREY_DARK)
def broken_age():
    left = path("M20 13H32V47H20A4 4 0 0 1 16 43V17A4 4 0 0 1 20 13Z", INK)
    right = path("M32 13H44A4 4 0 0 1 48 17V43A4 4 0 0 1 44 47H32Z", BLUE_GREY_LIGHT)
    girl = (circle(25, 20.5, 3.4, HOLE) + path("M22 25H28L30 38H26.5V44H24.5V38H20Z", HOLE))
    boy = (circle(39, 20.5, 3.4, INK) + rrect(36.2, 24.5, 5.6, 12.5, 2, INK)
           + rrect(36.4, 35, 2.2, 9.5, 1.1, INK) + rrect(39.4, 35, 2.2, 9.5, 1.1, INK))
    return left + right + girl + boy

@reg("broken-sword", RED_DARK)
def broken_sword():
    arm = "M29 30L26.5 13.5Q32 16 37.5 13.5L35 30Z"
    return "".join(path(arm, INK, f' transform="rotate({90 * k} 32 30)"') for k in range(4)) + circle(CX, CY, 4, INK)

@reg("bsnes", DEEP_PURPLE)
def bsnes():
    return (circle(35, 21, 7, INK) + circle(45, 29.5, 6.5, DEEP_PURPLE_SOFT)
            + f'<ellipse cx="21" cy="33.5" rx="7.5" ry="4.5" fill="{INK}" transform="rotate(-8 21 33.5)"/>'
            + f'<ellipse cx="35" cy="40.5" rx="7.5" ry="4.5" fill="#9C7EC8" transform="rotate(-8 35 40.5)"/>')

@reg("bugdom", INDIGO_SOFT)
def bugdom():
    antennae = stroke("M26 21C23 15 19 13 15.5 14M38 21C41 15 45 13 48.5 14", INK, 2.8)
    head = f'<ellipse cx="32" cy="33" rx="13" ry="14.5" fill="{INK}"/>'
    eyes = (circle(27, 29.5, 5, HOLE) + circle(37, 29.5, 5, HOLE)
            + circle(28, 30.5, 2.4, INK) + circle(36, 30.5, 2.4, INK))
    smile = stroke("M28 40Q32 42.5 36 40", HOLE, 2.4)
    return antennae + head + eyes + smile

@reg("bzflag", RED_DEEP)
def bzflag():
    treads = rrect(16, 20, 7, 27, 2.5, INK) + rrect(41, 20, 7, 27, 2.5, INK)
    body = rrect(24.5, 24, 15, 20, 3, INK)
    turret = circle(32, 34, 5.5, HOLE) + circle(32, 34, 3.5, INK)
    barrel = rrect(29.8, 11.5, 4.4, 20, 2.2, INK, f' stroke="{HOLE}" stroke-width="1.6"')
    return treads + body + barrel + turret

@reg("ca.andyholmes.Valent", BLUE_GREY_DARK)
def valent():
    phone = rrect(20, 11, 24, 38, 5, INK)
    screen = rrect(22.5, 16.5, 19, 25, 1.5, HOLE)
    speaker = rrect(28, 13, 8, 1.8, 0.9, HOLE)
    button = rrect(29.5, 43.5, 5, 3, 1.5, HOLE)
    return phone + screen + speaker + button

@reg("ca.edestcroix.Recordbox", BLUE_DEEP)
def recordbox():
    disc = circle(CX, CY, 16.5, INK)
    shade = path("M32 30L32 13.5A16.5 16.5 0 0 0 16.4 35.4Z", BLUE_SOFT)
    label = circle(CX, CY, 7.5, HOLE) + circle(CX, CY, 2, INK)
    return disc + shade + label

@reg("ca.hamaluik.Timecop", CYAN_DEEP)
def timecop():
    shield = path("M32 11.5C35.5 14 40 14.5 46 13.5V29C46 38 40 44 32 48.5C24 44 18 38 18 29V13.5"
                  "C24 14.5 28.5 14 32 11.5Z", INK)
    glass = (rrect(25, 20, 14, 2.8, 1.4, HOLE) + rrect(25, 38.5, 14, 2.8, 1.4, HOLE)
             + path("M27 23H37L32.6 30.3L37 38H27L31.4 30.3Z", HOLE))
    return shield + glass

@reg("cadence", RED_DARK)
def cadence():
    out = ""
    for a in (-90, 30, 150):
        tip = pt(CX, 30, 11.5, a)
        l = pt(CX, 30, 3, a - 90)
        r = pt(CX, 30, 3, a + 90)
        out += circle(*tip, 6, INK) + poly([l, pt(*tip, 5, a - 60), pt(*tip, 5, a + 60), r], INK, 1)
    return out + circle(CX, 30, 4.5, INK) + circle(CX, 30, 2, HOLE)

@reg("caffeine", BROWN)
def caffeine():
    steam = "".join(stroke(f"M{x} 21C{x - 2.5} 18.5 {x + 2.5} 16 {x} 12.5", INK, 2.4) for x in (25, 32, 39))
    cup = path("M19 25H45V35A10 10 0 0 1 35 45H29A10 10 0 0 1 19 35Z", INK)
    handle = rrect(13.5, 28, 7.5, 7, 3.5, "none", f' stroke="{INK}" stroke-width="3"')
    return steam + handle + cup

@reg("caja-actions", LIGHT_BLUE_DEEP)
def caja_actions():
    tabs = rrect(20, 12, 24, 6, 2, LIGHT_BLUE_SOFT) + rrect(18, 15.5, 28, 6, 2, LIGHT_BLUE_LIGHT)
    drawer = rrect(15, 19, 34, 26, 4, INK)
    handle = rrect(21, 27, 11, 3.2, 1.6, HOLE)
    badge = circle(42.5, 41.5, 9, LIGHT_BLUE_DARK) + gear_b(42.5, 41.5, 6.8, 5, INK, 6) + circle(42.5, 41.5, 2.2, LIGHT_BLUE_DARK)
    return tabs + drawer + handle + badge

@reg("calf", GREY_DARK)
def calf():
    face = path("M18 20A8 8 0 0 1 26 12H38A8 8 0 0 1 46 20V38C46 44 41 47 32 47C23 47 18 44 18 38Z", INK)
    patch = path("M38 12A8 8 0 0 1 46 20V27C42 27 38.5 23.5 38.5 19.5C38.5 16 37 14 35 12Z", HOLE)
    eyes = (circle(26.5, 28, 5.5, INK, f' stroke="{HOLE}" stroke-width="1.8"')
            + circle(37.5, 28, 5.5, INK, f' stroke="{HOLE}" stroke-width="1.8"')
            + circle(28.5, 29, 2.4, HOLE) + circle(35.5, 29, 2.4, HOLE))
    mouth = stroke("M20.5 44V40.5A5.5 5.5 0 0 1 31.5 40.5V42A5.5 5.5 0 0 1 43.5 40.5V44".replace(
        "V42A5.5 5.5 0 0 1 43.5", "A6 6 0 0 1 43.5"), RED_SOFT, 4)
    return face + patch + eyes + mouth

@small("borderlands")
def borderlands_s():
    return circle(CX, CY, 17, INK) + path("M23 45L25.5 19C26 12.5 31.5 12 34 16.5L45.5 41.5L41 44L32 25L30 46Z", HOLE)

SMALL["borderlands-2"] = SMALL["borderlands-the-pre-sequel"] = borderlands_s

@small("boxy-svg")
def boxy_svg_s():
    hexa = poly([pt(CX, CY, 18, -90 + 60 * k) for k in range(6)], INK, 3)
    rays = "".join(line(*pt(CX, CY, 3, 30 + 60 * k), *pt(CX, CY, 9, 30 + 60 * k), HOLE, 4) for k in range(6))
    return hexa + rays

@small("bovo")
def bovo_s():
    grid = (line(26, 13, 26, 47, INK, 3.4) + line(38, 13, 38, 47, INK, 3.4)
            + line(15, 24, 49, 24, INK, 3.4) + line(15, 36, 49, 36, INK, 3.4))
    return grid + stroke("M29.5 26.5L34.5 33.5M34.5 26.5L29.5 33.5", RED_SOFT, 3)

def _brackets_s():
    frame = rrect(13, 11, 38, 38, 6, INK) + rrect(19, 17, 26, 26, 2.5, HOLE)
    return (frame + path("M22 20H30V25H27V35H30V40H22Z", INK)
            + path("M42 20H34V25H37V35H34V40H42Z", INK))

SMALL["brackets"] = SMALL["brackets-electron"] = _brackets_s

@small("broforce")
def broforce_s():
    return circle(CX, 32, 12.5, BLUE_GREY_SOFT) + poly(
        [pt(CX, 31, 18.5 if k % 2 == 0 else 8, -90 + 36 * k) for k in range(10)], INK, 1.5)

@small("broken-age")
def broken_age_s():
    left = path("M20 12H32V48H20A4 4 0 0 1 16 44V16A4 4 0 0 1 20 12Z", INK)
    right = path("M32 12H44A4 4 0 0 1 48 16V44A4 4 0 0 1 44 48H32Z", BLUE_GREY_LIGHT)
    return (left + right + circle(24.5, 20, 4, HOLE) + path("M21 25.5H28L30.5 44H19Z", HOLE)
            + circle(40, 20, 4, INK) + rrect(36.5, 25.5, 7, 18.5, 2.5, INK))

@small("brosix")
def brosix_s():
    return circle(CX, CY, 17, INK) + stroke(
        "M28 21.5V38.5H34A4 4 0 0 0 34 30H28M28 30H33.5A4.2 4.2 0 0 0 33.5 21.5H28", HOLE, 3.2)

@small("browser360-beta")
def browser360_s():
    e = stroke("M21 31H43C43 23.5 38.5 19 32 19C25.5 19 21 24 21 31"
               "C21 38 25.5 43 32 43C36 43 39.5 41.5 41.5 38.5", INK, 5.5)
    return e + stroke("M16.5 46C13 38 20 25 30 18C37 13 44.5 11 48 13.5", INK, 3)

@small("bubblemail")
def bubblemail_s():
    bubble = rrect(13, 21, 30, 21, 6, INK) + poly([(19, 39), (27, 39), (18.5, 47)], INK, 2.5)
    return bubble + rrect(29, 11, 22, 16, 3, INK, f' stroke="{HOLE}" stroke-width="3"') + stroke(
        "M32.5 15L40 20.5L47.5 15", HOLE, 2.4)

@small("bugdom")
def bugdom_s():
    antennae = stroke("M26 21C23 15 19 13 15.5 14M38 21C41 15 45 13 48.5 14", INK, 3)
    head = f'<ellipse cx="32" cy="33" rx="14" ry="15" fill="{INK}"/>'
    return antennae + head + circle(26.5, 30, 5.5, HOLE) + circle(37.5, 30, 5.5, HOLE)

@small("buho")
def buho_s():
    frame = rrect(17, 11, 30, 38, 4.5, INK)
    return frame + "".join(rrect(21, 15 + 10.5 * k, 22, 8, 1.5, c)
                           for k, c in enumerate([BLUE_SOFT, PINK_SOFT, AMBER_SOFT]))

@small("builder")
def builder_s():
    return (rrect(15, 43, 22, 5, 2, INK) + rrect(20.5, 31, 11, 13, 1.5, INK)
            + line(26, 31, 41, 17, INK, 7) + circle(26, 31, 10, INK) + circle(26, 31, 5, HOLE)
            + circle(41, 17, 6, INK) + stroke("M44 21L49 26", INK, 3.4))

@small("buka")
def buka_s():
    return (path("M31 18C27 15 21 14.5 14 15.5V43C21 42 27 42.5 31 45Z", INK)
            + path("M33 18C37 15 43 14.5 50 15.5V43C43 42 37 42.5 33 45Z", INK)
            + path("M27.5 22C25 20.8 22 20.5 19 20.8V37.5C22 37.3 25 37.8 27.5 38.8Z", HOLE)
            + path("M36.5 22C39 20.8 42 20.5 45 20.8V37.5C42 37.3 39 37.8 36.5 38.8Z", HOLE))

@small("bulky")
def bulky_s():
    box = rrect(13, 21, 37, 18, 3, "none", f' stroke="{INK}" stroke-width="3.2"')
    return (box + rrect(17.5, 25.5, 14, 9, 1.5, INK) + rrect(34.5, 17, 9, 26, 0, HOLE)
            + line(39, 15, 39, 45, INK, 3.4) + line(34, 15, 44, 15, INK, 3.4) + line(34, 45, 44, 45, INK, 3.4))

@small("bum")
def bum_s():
    return gear_b(CX, CY, 18, 14, INK) + circle(CX, CY, 9.5, HOLE) + circle(CX, CY, 6, INK)

@small("burp")
def burp_s():
    return (rrect(14, 12, 36, 36, 5, INK) + path("M19 12H30V48H19A5 5 0 0 1 14 43V17A5 5 0 0 1 19 12Z", DEEP_ORANGE_DARK)
            + stroke("M38.5 14V25L33 31H42L36.5 37V46", HOLE, 3.4))

@small("buttercup-desktop")
def buttercup_s():
    body = (circle(26, 23, 11, INK) + rrect(15, 23, 23, 24, 7, INK)
            + circle(40, 35.5, 10.5, INK) + rrect(26, 36, 20, 11, 7, INK))
    return body + path("M18 27A8 8 0 0 1 34 27Z", HOLE) + circle(27, 37, 4, HOLE)

@small("bwfmetaedit")
def bwfmetaedit_s():
    sheet = path("M18 11H38L49 22V46A3 3 0 0 1 46 49H18A3 3 0 0 1 15 46V14A3 3 0 0 1 18 11Z", INK)
    return sheet + stroke("M20.5 42V24H29M20.5 33H27.5M31.5 42L36.5 24L41.5 42M33 36.5H40", HOLE, 3)

@small("byobu")
def byobu_s():
    return (rrect(13, 14, 38, 32, 4, INK) + rrect(36, 14, 3, 32, 0, HOLE)
            + stroke("M30 21.5C28.5 20.3 27 20 25 20C21.8 20 19.5 21.7 19.5 24C19.5 29 30 27 30 32"
                     "C30 34.5 28 36 25 36C23 36 20.5 35.3 19 34", HOLE, 3)
            + line(24.8, 16.5, 24.8, 39.5, HOLE, 2.6))

@small("bzflag")
def bzflag_s():
    return (rrect(15, 20, 8, 28, 2.5, INK) + rrect(41, 20, 8, 28, 2.5, INK)
            + rrect(25, 24, 14, 20, 3, INK) + rrect(29.5, 11, 5, 20, 2.5, INK))

@small("ca.hamaluik.Timecop")
def timecop_s():
    shield = path("M32 11C35.5 13.5 40 14 47 13V29C47 38 40.5 44.5 32 49C23.5 44.5 17 38 17 29V13"
                  "C24 14 28.5 13.5 32 11Z", INK)
    return shield + path("M25 19H39V22.5L33.5 30.3L39 38V41.5H25V38L30.5 30.3L25 22.5Z", HOLE)

@small("cacher")
def cacher_s():
    return circle(CX, CY, 17, INK) + stroke("M24.5 23.5L18.5 30L24.5 36.5M39.5 23.5L45.5 30L39.5 36.5", HOLE, 3.6)

@small("caffeine")
def caffeine_s():
    steam = "".join(stroke(f"M{x} 20C{x - 2.5} 17.5 {x + 2.5} 15 {x} 11.5", INK, 2.6) for x in (27, 37))
    cup = path("M18 24H46V35A10 10 0 0 1 36 45H28A10 10 0 0 1 18 35Z", INK)
    return steam + rrect(12.5, 27, 8.5, 8, 4, "none", f' stroke="{INK}" stroke-width="3.2"') + cup

@small("caja-actions")
def caja_actions_s():
    drawer = rrect(13, 16, 36, 28, 4, INK) + rrect(19, 24, 12, 4, 2, HOLE)
    return drawer + circle(43, 41, 10, ORANGE_DARK) + gear_b(43, 41, 7.5, 5.5, INK, 6) + circle(43, 41, 2.4, ORANGE_DARK)

@small("calf")
def calf_s():
    face = path("M17 20A8 8 0 0 1 25 12H39A8 8 0 0 1 47 20V38C47 44 42 48 32 48C22 48 17 44 17 38Z", INK)
    eyes = circle(26, 27, 4, HOLE) + circle(38, 27, 4, HOLE)
    mouth = stroke("M21 44V40.5A5.5 5.5 0 0 1 32 40.5A5.5 5.5 0 0 1 43 40.5V44", RED_SOFT, 4.5)
    return face + eyes + mouth

@small("btrfs-assistant")
def btrfs_s():
    return (gear_b(CX, CY, 18.5, 14.5, INK) + circle(CX, CY, 10.5, HOLE)
            + stroke("M27 24V35.5H37", INK, 3.4) + circle(37, 35.5, 3, INK) + circle(27, 24, 3, INK))

@small("ca.edestcroix.Recordbox")
def recordbox_s():
    return (circle(CX, CY, 17, INK) + path("M32 30L32 13A17 17 0 0 0 16 36Z", BLUE_SOFT)
            + circle(CX, CY, 8, HOLE) + circle(CX, CY, 2.6, INK))
