# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 47: mx-codecs to net.imput.helium.

Same kit and rules as batch01: one INK mark per tile, HOLE for cut lines,
any second shade a palette step of the tile's own hue.
"""
from lm import *
from glyphs.kit import _gear_f, registry

ICONS, SMALL, reg, small = registry()

def _badge(cx, cy, r=9.5):
    """A round badge in the corner, parted from the main mark by a tile gap."""
    return circle(cx, cy, r + 2, HOLE) + circle(cx, cy, r, INK)

def _plus(cx, cy, r=9.5):
    s = r * .5
    return _badge(cx, cy, r) + stroke(f"M{f(cx - s)} {f(cy)}H{f(cx + s)}M{f(cx)} {f(cy - s)}V{f(cy + s)}", HOLE, 3)

def _gear_badge(cx, cy, r=9.5):
    return (_badge(cx, cy, r) + _gear_f(cx, cy, r * .66, HOLE, 7) +
            circle(cx, cy, r * .22, INK))

def _outline(d, w):
    """A tile-coloured edge under a stroke so it parts from what it crosses."""
    return stroke(d, HOLE, w + 3) + stroke(d, INK, w)

@reg("mx-codecs", BLUE_DEEP)
def mx_codecs():
    strip = rrect(16, 12, 32, 36, 4, INK)
    holes = "".join(rrect(x, y, 3.4, 4, 1, HOLE) for x in (18.5, 42.1) for y in (15.5, 23.5, 31.5, 39.5))
    arrow = rrect(29, 16, 6, 12, 1.5, HOLE) + poly([(23.5, 26), (40.5, 26), (32, 36)], HOLE, 2.5)
    base = rrect(25, 39, 14, 3, 1.5, HOLE)
    return strip + holes + arrow + base

@reg("mx-conky", BLUE)
def mx_conky():
    panel = rrect(15, 13, 34, 34, 4, INK)
    side = rrect(22, 13, 2.4, 34, 0, HOLE)
    dots = "".join(rrect(17.2, y, 3.2, 3.2, .8, HOLE) for y in (17, 23, 29))
    block = rrect(31, 18, 12, 10, 2, HOLE)
    bar = rrect(28, 34, 16, 3, 1.5, HOLE)
    return panel + side + dots + block + bar

@reg("mx-datetime", RED_DEEP)
def mx_datetime():
    page = rrect(14, 13, 32, 32, 4, INK)
    band = rrect(14, 20, 32, 2.4, 0, HOLE)
    rings = circle(21, 16.5, 1.6, HOLE) + circle(39, 16.5, 1.6, HOLE)
    cells = "".join(rrect(18 + c * 7.5, 25.5 + r * 6.5, 5, 4.5, 1, HOLE)
                    for r in range(3) for c in range(3))
    clock = (_badge(42, 40, 9.5) +
             stroke("M42 34.5V40.5H46.5", HOLE, 2.6))
    return page + band + rings + cells + clock

@reg("mx-live-usb-maker", ORANGE_DARK)
def mx_live_usb():
    plug = rrect(22, 11, 14, 11, 2, INK)
    slots = rrect(25, 14, 3, 3, .6, HOLE) + rrect(30, 14, 3, 3, .6, HOLE)
    body = rrect(18, 23.5, 22, 25, 4, INK)
    label = rrect(22, 29, 11, 2.6, 1.3, HOLE) + rrect(22, 34, 8, 2.6, 1.3, HOLE)
    return plug + slots + body + label + _plus(42, 40)

@reg("mx-network-assistant", PURPLE_DEEP)
def mx_network():
    body = rrect(14, 13, 32, 30, 4, INK)
    socket = poly([(19, 18), (41, 18), (41, 32), (35.5, 32), (35.5, 37), (24.5, 37),
                   (24.5, 32), (19, 32)], HOLE, 1.5)
    pins = "".join(rrect(x, 18, 2.2, 4.5, .5, INK) for x in (22.5, 26.5, 30.5, 34.5))
    return body + socket + pins + _gear_badge(43, 40)

@reg("mx-packageinstaller", BROWN_LIGHT)
def mx_package():
    box = rrect(15, 13, 30, 32, 4, INK)
    tape = rrect(27, 13, 6, 5, 0, HOLE)
    ring = f'<circle cx="30" cy="30" r="7.5" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
    arrow = stroke("M30 25.5V33M26.8 30L30 33.2L33.2 30", HOLE, 2.6)
    return box + tape + ring + arrow + _plus(43, 40)

@reg("mx-qsi", LIGHT_BLUE_DEEP)
def mx_qsi():
    mon = rrect(13, 13, 38, 27, 3.5, INK)
    ring = f'<circle cx="32" cy="26.5" r="8.5" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
    i = circle(32, 22.3, 1.7, HOLE) + stroke("M32 26.2V31", HOLE, 3)
    stand = rrect(27, 39, 10, 5, 0, INK) + rrect(21, 43.5, 22, 3.5, 1.75, INK)
    return mon + ring + i + stand

@reg("mx-repo-manager", BLUE)
def mx_repo():
    stem = rrect(23, 12, 10, 18, 2.5, INK)
    head = poly([(15, 28), (41, 28), (28, 44)], INK, 3.5)
    return stem + head + _gear_badge(43, 40)

@reg("mx-select-sound", ORANGE_DEEP)
def mx_sound():
    bracket = stroke("M16 12V46", INK, 3.2)
    card = rrect(19, 19, 26, 20, 3, INK)
    chip = rrect(23, 23, 9, 9, 1.5, HOLE)
    pins = "".join(rrect(x, 36.5, 2.4, 2.5, .4, HOLE) for x in (22, 26, 30, 34))
    note = (circle(40, 43.5, 2.6, HOLE) + stroke("M42.3 43.5V35.5L46 36.8", HOLE, 2.4))
    return bracket + card + chip + pins + _badge(42, 40) + note

@reg("mx-snapshot", BLUE_DEEP)
def mx_snapshot():
    mon = rrect(13, 13, 34, 25, 3.5, INK)
    screen = rrect(16.5, 16.5, 27, 18, 1.5, HOLE)
    stand = rrect(25, 37, 10, 5, 0, INK) + rrect(19, 41.5, 22, 3.5, 1.75, INK)
    cx, cy = 42, 38
    blades = "".join(line(*pt(cx, cy, 3, a), *pt(cx, cy, 8.2, a + 55), HOLE, 2.2)
                     for a in range(0, 360, 60))
    return mon + screen + stand + _badge(cx, cy, 10) + blades

@reg("mx-tools", CYAN_DEEP)
def mx_tools():
    mountain = poly([(14, 48), (27, 36), (31, 39.5), (37, 34), (50, 48)], INK, 2)
    wrench = (_outline("M20.5 18.5L39 37", 4.2) + circle(19.5, 17.5, 6, INK) +
              g(rrect(17.5, 10, 4, 7, 1, HOLE), "rotate(-45 19.5 17.5)"))
    hammer = (_outline("M42 19L24 37", 3.8) +
              g(rrect(35, 14.5, 14, 6, 1.8, INK), "rotate(45 42 17.5)"))
    return mountain + wrench + hammer

@reg("mx-tweak", BLUE_GREY_DEEP)
def mx_tweak():
    win = rrect(14, 13, 36, 34, 4, INK)
    side = rrect(22, 13, 2.4, 34, 0, HOLE)
    dots = "".join(rrect(16.4, y, 3.4, 3.4, .8, HOLE) for y in (17, 23, 29, 41))
    arrow = stroke("M27.5 20H33C38 20 41 23 41 28V31", HOLE, 3.2)
    head = poly([(36, 30), (46, 30), (41, 37)], HOLE, 2)
    return win + side + dots + arrow + head

@reg("mx-updater", ORANGE_DEEP)
def mx_updater():
    inside = poly([(18, 26), (32, 20), (46, 26), (32, 32)], ORANGE_DARK, 2)
    front = poly([(18, 26), (32, 32), (32, 48), (18, 42)], INK, 2.5)
    side = poly([(32, 32), (46, 26), (46, 42), (32, 48)], INK, 2.5)
    seam = line(32, 32.5, 32, 48, HOLE, 1.6)
    edge = f' stroke="{HOLE}" stroke-width="1.6" stroke-linejoin="round"'
    lflap = path("M18 26L32 20L27 11.5L13.5 17.5Z", INK, edge)
    rflap = path("M32 20L46 26L50.5 17.5L37 11.5Z", INK, edge)
    return inside + lflap + rflap + front + side + seam

@reg("mx-user", BLUE_DEEP)
def mx_user():
    back = circle(25, 19.5, 5.5, INK) + path(
        "M13.5 38C13.5 31 18.5 27.5 25 27.5C31.5 27.5 36.5 31 36.5 38Z", INK)
    edge = f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"'
    front = (circle(39, 28, 5.5, INK, edge) +
             path("M27.5 47.5C27.5 40.5 32.5 36.5 39 36.5C45.5 36.5 50.5 40.5 50.5 47.5Z", INK, edge))
    front_fill = circle(39, 28, 5.5, INK) + path(
        "M27.5 47.5C27.5 40.5 32.5 36.5 39 36.5C45.5 36.5 50.5 40.5 50.5 47.5Z", INK)
    return back + front + front_fill

@reg("mx-welcome", ORANGE_DARK)
def mx_welcome():
    head = circle(32, 16.5, 4.5, INK)
    torso = rrect(27.5, 23, 9, 13, 2.5, INK)
    legs = stroke("M29.7 34V46.5M34.3 34V46.5", INK, 3.8)
    arms = stroke("M28 25.5L20.5 23L17 15.5M36 25.5L43.5 23L47 15.5", INK, 3.6)
    return head + torso + legs + arms

@reg("mynotes", AMBER_DEEP)
def mynotes():
    note = path("M19 13H45A3 3 0 0 1 48 16V35L37 46H19A3 3 0 0 1 16 43V16A3 3 0 0 1 19 13Z", INK)
    fold = path("M48 35L39.5 35.8Q37.6 36 37.4 38L37 46Z", AMBER_SOFT,
                ' stroke="#FFD65D" stroke-width="1.5" stroke-linejoin="round"')
    return note + fold

@reg("myrulib", BROWN)
def myrulib():
    book = rrect(18, 12, 28, 36, 3.5, INK)
    spine = rrect(23, 12, 2.4, 36, 0, HOLE)
    mark = poly([(34, 12), (41, 12), (41, 26), (37.5, 22.5), (34, 26)], HOLE, 1.2)
    return book + spine + mark

@reg("myspace", INDIGO_DEEP)
def myspace():
    edge = f' stroke="{HOLE}" stroke-width="2.4"'
    small = circle(19.5, 25, 3.8, INK) + rrect(15.5, 30.5, 8, 13, 3.5, INK)
    mid = circle(28.5, 21.5, 4.8, INK, edge) + rrect(23, 28.5, 11, 17, 4.5, INK, edge)
    big = circle(40, 18.5, 6.2, INK, edge) + rrect(33, 27.5, 14.5, 20.5, 6, INK, edge)
    return small + mid + big

@reg("mysql-workbench", BLUE_DARK)
def mysql_workbench():
    body = path("M14 20.5C19 15 28 14.5 34 19C40 23.5 43.5 30 44.5 37.5L49.5 41.5"
                "L43.5 41.5L42 47.5L39.5 40.5C37.5 33 33 27.5 27 24.5C22.5 22.5 18 22.5 14 20.5Z", INK)
    fin = poly([(29, 17), (33.5, 11.5), (35, 20)], INK, 2)
    flipper = poly([(26, 23.5), (27, 30.5), (31, 25.5)], INK, 1.5)
    eye = circle(20.5, 19.5, 1.3, HOLE)
    return body + fin + flipper + eye

@reg("mystiq", INDIGO_LIGHT)
def mystiq():
    cam = rrect(13, 18, 28, 24, 5, INK)
    lens = poly([(40, 26), (50, 20), (50, 40), (40, 34)], INK, 3)
    play = poly([(23, 23.5), (33, 30), (23, 36.5)], HOLE, 2.5)
    return cam + lens + play

@reg("mytourbook", DEEP_ORANGE)
def mytourbook():
    ring = cut(cpath(34, 27, 15) + cpath(34, 27, 7.5), INK)
    d = "M14 48L14.5 39.5C17 41 20 40.5 22 38.5L25.5 41.5C29 42.5 33 43 35.5 45L35.5 48Z"
    shoe = (path(d, HOLE, f' stroke="{HOLE}" stroke-width="4.8" stroke-linejoin="round"') +
            path(d, BLUE_DARK))
    return ring + shoe

@reg("naev", INDIGO_DEEP)
def naev():
    ship = poly([(32, 10.5), (35.5, 24), (45, 36), (45, 41.5), (35.5, 37.5), (34.5, 45),
                 (29.5, 45), (28.5, 37.5), (19, 41.5), (19, 36), (28.5, 24)], INK, 2)
    cockpit = poly([(32, 20), (33.8, 28), (30.2, 28)], HOLE, 1.2)
    return g(ship + cockpit, "rotate(40 32 29)")

@reg("narcissu-1st-2nd", BLUE_GREY_DARK)
def narcissu():
    n = poly([(16, 20), (38, 20), (45, 25), (46, 27), (46, 41), (37, 41), (37, 29),
              (27, 29), (27, 41), (18, 41), (18, 26), (16, 26)], INK, 2)
    return n

@reg("nasc", LIGHT_BLUE_DEEP)
def nasc():
    sigma = stroke("M37 17H21L29.5 30L21 43H37", INK, 4.4)
    bar = rrect(42, 11, 4, 38, 2, INK)
    return sigma + bar

@reg("natron", GREY_DARK)
def natron():
    hexa = poly([pt(32, 30, 17, a) for a in range(0, 360, 60)], INK, 3)
    n = poly([(24, 38), (24, 23), (27, 20), (37, 32), (37, 21), (40, 21), (40, 37),
              (37, 40), (27, 28), (27, 38)], HOLE, 1.5)
    return hexa + n

def _drawer(y, h):
    return rrect(18, y, 28, h, 3, INK) + rrect(28.5, y + h / 2 - 1.3, 7, 2.6, 1.3, HOLE)

@reg("nautilus", BLUE)
def nautilus():
    return _drawer(12, 11) + _drawer(24.5, 11) + _drawer(37, 11)

@reg("nautilus-alt", BLUE_DEEP)
def nautilus_alt():
    cab = rrect(18, 12, 28, 36, 4, INK)
    lines = rrect(18, 23.5, 28, 1.8, 0, HOLE) + rrect(18, 35.5, 28, 1.8, 0, HOLE)
    handles = "".join(rrect(28.5, y, 7, 2.6, 1.3, HOLE) for y in (16.5, 28.5, 40.5))
    return cab + lines + handles

@reg("navalbattle", BLUE_LIGHT)
def navalbattle():
    boat = poly([(14, 29), (22, 29), (26, 20), (32, 26), (38, 20), (42, 29), (50, 29),
                 (44, 41), (20, 41)], INK, 3)
    fold = stroke("M22 29L32 34L42 29", HOLE, 2.2)
    return boat + fold

@reg("naver-whale", CYAN_DEEP)
def naver_whale():
    bubble = circle(32, 30, 16, INK) + poly([(17, 36), (24, 44), (14.5, 47)], INK, 2)
    sky = path("M16.96 35.47A16 16 0 0 1 43.31 18.69C38 27 28 33.5 16.96 35.47Z", BLUE_DARK)
    stars = circle(26, 23, 1.2, INK) + circle(34, 19.5, 1, INK) + circle(22, 29, .9, INK)
    eye = circle(29, 38.5, 1.6, BLUE_DARK)
    return bubble + sky + stars + eye

def _navicat():
    lear = path("M17 31C15 21 21 13 32 12C28 17 27.5 22 29 26Z", INK)
    rear = path("M40 26C40 20 42 15.5 46 13C49.5 17.5 50 24 48 31Z", INK)
    d = ("M14.5 37C14.5 28 23 24 32.5 24C42 24 49.5 28.5 49.5 36"
         "C49.5 43 42 47.5 32 47.5C22 47.5 14.5 44 14.5 37Z")
    body = path(d, HOLE, f' stroke="{HOLE}" stroke-width="5" stroke-linejoin="round"') + path(d, INK)
    return lear + rear + body

@reg("navicat", BLUE_GREY)
def navicat():
    return _navicat()

@reg("navicat-postgresql", CYAN_DEEP)
def navicat_pg():
    return _navicat()

@reg("navit", GREY_DARK)
def navit():
    road = rrect(17, 11, 20, 38, 3, INK)
    dashes = "".join(rrect(25.8, y, 2.4, 6, 1.2, HOLE) for y in (14, 23, 32, 41))
    cx, cy = 42, 38
    target = (_badge(cx, cy, 9.5) +
              f'<circle cx="{cx}" cy="{cy}" r="4.8" fill="none" stroke="{HOLE}" stroke-width="2.4"/>' +
              circle(cx, cy, 1.8, HOLE) +
              stroke(f"M{cx} {cy - 8}V{cy - 6.5}M{cx} {cy + 6.5}V{cy + 8}"
                     f"M{cx - 8} {cy}H{cx - 6.5}M{cx + 6.5} {cy}H{cx + 8}", HOLE, 2.4))
    return road + dashes + target

@reg("nbteditor", BROWN)
def nbteditor():
    n = stroke("M16.5 35V17L28 35V17", INK, 3.8)
    t = stroke("M31 14H47M39 14V33", INK, 3.8)
    b = stroke("M26 32V47H32.5A3.75 3.75 0 0 0 32.5 39.5H26M26 39.5H31.8A3.75 3.75 0 0 0 31.8 32H26", INK, 3.4)
    return n + t + b

@reg("nbtexplorer", GREY_DEEP)
def nbtexplorer():
    parts = [(29.5, 12, 5, 37), (18, 22, 12, 4), (18, 22, 4, 9), (34, 18, 11, 4),
             (41, 12, 4, 10), (20, 31, 10, 4), (34, 30, 12, 4), (42, 30, 4, 9),
             (24, 26, 4, 5), (34, 39, 8, 4)]
    return "".join(rrect(x, y, w, h, .8, INK) for x, y, w, h in parts)

@reg("ncrack", GREY_SOFT)
def ncrack():
    body = path("M22 30C25 26 33 26 37 29C40 31.5 40 36 36.5 38C33 40 25 40 22 37Z", INK)
    head = circle(21, 33.5, 4, INK)
    tail = stroke("M37 31C44 31 47 24 44 18.5C42 15 37.5 15 36.5 19", INK, 3.8)
    sting = poly([(35, 17), (39, 20), (34.5, 22)], INK, 1.5)
    claws = stroke("M19 31L16 25.5M19 36.5L16 41", INK, 2.8) + stroke(
        "M13 23.5A4.2 4.2 0 1 1 19.5 21.5M13 43A4.2 4.2 0 1 0 19.5 45", INK, 2.8)
    legs = stroke("M26 38L24 44M30 39L29.5 45.5M34 38.5L35.5 44.5", INK, 2.2)
    return body + head + tail + sting + claws + legs

@reg("ndisgtk", RED_DEEP)
def ndisgtk():
    gear = _gear_f(32, 30, 17.5, INK, 8)
    face = circle(32, 30, 10, HOLE)
    ring = f'<circle cx="32" cy="30" r="6.3" fill="none" stroke="{INK}" stroke-width="2.4"/>'
    mast = stroke("M32 30V39", INK, 2.6)
    return gear + face + ring + circle(32, 30, 2.4, INK) + mast

@reg("ndm", RED)
def ndm():
    n = stroke("M21 46V18H33C37.5 18 40 20.5 40 25V33", INK, 6)
    head = poly([(32.5, 32), (47.5, 32), (40, 42)], INK, 3)
    return n + head

@reg("negibox", ORANGE_DARK)
def negibox():
    stem = rrect(26.5, 11, 11, 18, 2.5, INK)
    head = poly([(15, 27), (49, 27), (32, 46)], INK, 3.5)
    return stem + head

@reg("nekopara", PINK_DARK)
def nekopara():
    pad = path("M32 28.5C38.5 28.5 44.5 36 44.5 41C44.5 45 40.5 46.5 32 46"
               "C23.5 46.5 19.5 45 19.5 41C19.5 36 25.5 28.5 32 28.5Z", INK)
    toes = (circle(18.5, 28, 4.3, INK) + circle(26, 18.5, 4.8, INK) +
            circle(38, 18.5, 4.8, INK) + circle(45.5, 28, 4.3, INK))
    return pad + toes

@reg("nemiver", BLUE_GREY_LIGHT)
def nemiver():
    nozzle = rrect(28.5, 11, 7, 5.5, 1.5, INK)
    cap = rrect(24, 17.5, 16, 5.5, 2.5, INK)
    can = rrect(20, 24.5, 24, 24, 5, INK)
    bug = (path("M32 31.5C35 31.5 36.5 34 36.5 37.5C36.5 41 34.5 43.5 32 43.5"
                "C29.5 43.5 27.5 41 27.5 37.5C27.5 34 29 31.5 32 31.5Z", HOLE) +
           circle(32, 29.5, 2.3, HOLE) +
           stroke("M27.5 35L24 33M27.5 38.5L23.5 38.5M28 41.5L24.5 44"
                  "M36.5 35L40 33M36.5 38.5L40.5 38.5M36 41.5L39.5 44", HOLE, 2.2))
    return nozzle + cap + can + bug

def _nero():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="4.6"/>'
    flame = path("M32 42C26 42 23 38 23 34C23 29 27 26 28 21C31 24 31 27 30 29"
                 "C33 27 35 23 34 18C39 22 41 28 41 34C41 38 38 42 32 42Z", INK)
    core = path("M32 42C29.5 42 28 40 28 38C28 35.5 30 34 31 32C33 34 36 35.5 36 38"
                "C36 40 34.5 42 32 42Z", HOLE)
    return ring + g(flame + core, "translate(32 31) scale(.78) translate(-32 -30)")

@reg("nerolinux", RED)
def nerolinux():
    return _nero()

@reg("nerolinuxexpress", GREY_DEEP)
def nerolinuxexpress():
    return _nero()

@reg("net.bartkessels.getit", BLUE_DEEP)
def getit():
    left = poly([(14, 22), (24, 13.5), (24, 30.5)], INK, 2.5) + rrect(22, 17.5, 20, 9, 2, INK)
    right = rrect(22, 33.5, 20, 9, 2, INK) + poly([(40, 29.5), (50, 38), (40, 46.5)], INK, 2.5)
    return left + right

@reg("net.baseart.Glide", BLUE_GREY_DARK)
def glide():
    board = rrect(15, 22, 34, 25, 3, INK)
    top = g(rrect(15, 13, 34, 6, 1.5, INK), "rotate(-8 15 19)")
    stripes = g("".join(poly([(x, 13), (x + 4, 13), (x + 1, 19), (x - 3, 19)], HOLE)
                        for x in (21, 29, 37, 45)), "rotate(-8 15 19)")
    play = poly([(28, 28), (38, 34.5), (28, 41)], HOLE, 2.5)
    return board + top + stripes + play

@reg("net.christianbeier.Gromit-MPX", RED_DEEP)
def gromit():
    return stroke("M43 18C37 12 23 13 19 25C16 35 22 44 31 44C37 44 41 40 42 34L33.5 33", INK, 5)

@reg("net.daase.journable", BLUE_GREY)
def journable():
    page = rrect(15, 15, 30, 31, 4, INK)
    rings = "".join(stroke(f"M{x} 12V19", INK, 2.4) + circle(x, 19.5, 1.4, HOLE) for x in (20, 26, 32, 38))
    rows = "".join(rrect(18.5, y, 20, 2, 1, HOLE) for y in (25, 31, 37))
    pd = "M47.5 25L30.5 43"
    pencil = (stroke(pd, HOLE, 8) + stroke(pd, INK, 4.8) +
              poly([(28, 45.5), (29.2, 40.5), (33, 44.5)], INK, 1.2))
    return page + rings + rows + pencil

def _mic(dx, h):
    top = 12 + (22 - h)
    d_u = f"M{f(16 + dx)} {f(top + h - 7)}V{f(top + h - 4)}C{f(16 + dx)} {f(top + h + 2)} {f(19.5 + dx)} {f(top + h + 5)} {f(24.5 + dx)} {f(top + h + 5)}C{f(29.5 + dx)} {f(top + h + 5)} {f(33 + dx)} {f(top + h + 2)} {f(33 + dx)} {f(top + h - 4)}V{f(top + h - 7)}"
    stem = f"M{f(24.5 + dx)} {f(top + h + 5)}V45.5M{f(18 + dx)} 45.5H{f(31 + dx)}"
    out = rrect(19 + dx, top, 11, h, 5.5, HOLE, f' stroke="{HOLE}" stroke-width="3"')
    out += stroke(d_u + stem, HOLE, 5.6)
    out += rrect(19 + dx, top, 11, h, 5.5, INK) + stroke(d_u + stem, INK, 2.6)
    return out

@reg("net.danigm.loop", PINK)
def loop():
    return _mic(14, 14) + _mic(7, 17) + _mic(0, 20)

@reg("net.danigm.timetrack", BLUE_GREY_DARK)
def timetrack():
    ring = f'<circle cx="32" cy="30" r="16" fill="none" stroke="{INK}" stroke-width="3.4"/>'
    x1, y1 = pt(32, 30, 11.5, -90)
    x2, y2 = pt(32, 30, 11.5, -25)
    wedge = path(f"M32 30L{f(x1)} {f(y1)}A11.5 11.5 0 0 1 {f(x2)} {f(y2)}Z", INK)
    hands = stroke("M32 30L25 39M32 30L22.5 27", INK, 2.6)
    return ring + wedge + hands + circle(32, 30, 2.4, INK)

@reg("net.davidotek.pupgui2", LIGHT_BLUE_DEEP)
def pupgui2():
    arrow = stroke("M32 16V48M19.5 27L32 14.5L44.5 27", INK, 5)
    zig = stroke("M24.5 38L28 34.5L31 37.5L34.5 34L37.5 37L40.5 34", ORANGE, 2.4)
    return arrow + stroke("M24.5 38L28 34.5L31 37.5L34.5 34L37.5 37L40.5 34", HOLE, 5) + zig

@reg("net.imput.helium", INDIGO)
def helium():
    return "".join(line(*pt(32, 30, 3, a), *pt(32, 30, 16, a), INK, 3.4)
                   for a in range(0, 360, 45))

def _plus_s(cx, cy, r=11):
    s = r * .55
    return _badge(cx, cy, r) + stroke(f"M{f(cx - s)} {f(cy)}H{f(cx + s)}M{f(cx)} {f(cy - s)}V{f(cy + s)}", HOLE, 4)

def _gear_s(cx, cy, r=11):
    return _badge(cx, cy, r) + _gear_f(cx, cy, r * .7, HOLE, 6) + circle(cx, cy, r * .25, INK)

@small("mx-datetime")
def mx_datetime_s():
    page = rrect(14, 13, 30, 30, 4, INK) + rrect(14, 21, 30, 3.5, 0, HOLE)
    return page + _badge(42, 40, 11) + stroke("M42 33.5V40.5H47.5", HOLE, 3.6)

@small("mx-live-usb-maker")
def mx_live_usb_s():
    plug = rrect(21, 11, 14, 11, 2, INK) + rrect(24, 14.5, 3.5, 3.5, .6, HOLE) + rrect(29, 14.5, 3.5, 3.5, .6, HOLE)
    return plug + rrect(17, 24, 22, 24, 4, INK) + _plus_s(42, 40)

@small("mx-network-assistant")
def mx_network_s():
    body = rrect(13, 13, 32, 30, 4, INK)
    socket = poly([(18, 18), (40, 18), (40, 31), (34.5, 31), (34.5, 36), (23.5, 36),
                   (23.5, 31), (18, 31)], HOLE, 1.5)
    return body + socket + _gear_s(43, 40)

@small("mx-packageinstaller")
def mx_package_s():
    box = rrect(14, 13, 30, 32, 4, INK)
    arrow = stroke("M28 18V32M22.5 27L28 32.5L33.5 27", HOLE, 4)
    return box + arrow + _plus_s(43, 40)

@small("mx-qsi")
def mx_qsi_s():
    mon = rrect(13, 12, 38, 29, 3.5, INK)
    i = circle(32, 18.5, 2.8, HOLE) + stroke("M32 25V35", HOLE, 5)
    stand = rrect(27, 40, 10, 4, 0, INK) + rrect(20, 43.5, 24, 4, 2, INK)
    return mon + i + stand

@small("mx-repo-manager")
def mx_repo_s():
    return rrect(21, 12, 11, 18, 2.5, INK) + poly([(13, 28), (40, 28), (26.5, 44)], INK, 3.5) + _gear_s(43, 40)

@small("mx-select-sound")
def mx_sound_s():
    card = stroke("M15 12V46", INK, 4) + rrect(18, 17, 26, 20, 3, INK) + rrect(22, 21, 9, 9, 1.5, HOLE)
    note = circle(39.5, 44, 3.2, HOLE) + stroke("M42.3 44V34.5L47 36", HOLE, 3.2)
    return card + _badge(42, 40, 11) + note

@small("mx-snapshot")
def mx_snapshot_s():
    mon = rrect(12, 12, 34, 26, 3.5, INK) + rrect(16.5, 16.5, 25, 17, 1.5, HOLE)
    stand = rrect(19, 40, 20, 4, 2, INK)
    hexa = poly([pt(42, 39, 4.5, a) for a in range(30, 390, 60)], HOLE, 1)
    return mon + stand + _badge(42, 39, 11) + hexa

@small("mx-tools")
def mx_tools_s():
    mountain = poly([(13, 48), (32, 34), (51, 48)], INK, 2)
    x = _outline("M20 18L41 39", 5) + _outline("M44 18L23 39", 5)
    return mountain + x + circle(19, 17, 6.5, INK) + g(rrect(33, 13, 16, 7, 2, INK), "rotate(45 41 16.5)")

@small("mx-tweak")
def mx_tweak_s():
    win = rrect(13, 13, 38, 34, 4, INK) + rrect(21, 13, 3, 34, 0, HOLE)
    arrow = stroke("M28 20H33C38.5 20 41.5 23 41.5 28.5V30", HOLE, 4.5)
    return win + arrow + poly([(35, 29), (48, 29), (41.5, 38)], HOLE, 2)

@small("mx-updater")
def mx_updater_s():
    inside = poly([(18, 26), (32, 20), (46, 26), (32, 32)], ORANGE_DARK, 2)
    body = poly([(18, 26), (32, 32), (46, 26), (46, 42), (32, 48), (18, 42)], INK, 2.5)
    edge = f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"'
    return (inside + path("M18 26L32 20L27 11.5L13.5 17.5Z", INK, edge) +
            path("M32 20L46 26L50.5 17.5L37 11.5Z", INK, edge) + body)

@small("myspace")
def myspace_s():
    edge = f' stroke="{HOLE}" stroke-width="3.4"'
    small_ = circle(19, 25, 4.2, INK) + rrect(14.5, 31, 9, 13, 4, INK)
    mid = circle(28.5, 21, 5.2, INK, edge) + rrect(22.5, 28.5, 12, 17.5, 5, INK, edge)
    big = circle(40.5, 18, 6.5, INK, edge) + rrect(33.5, 27, 15, 21, 6.5, INK, edge)
    return small_ + mid + big

@small("nautilus-alt")
def nautilus_alt_s():
    cab = rrect(17, 12, 30, 36, 4, INK)
    lines = rrect(17, 23.5, 30, 2.6, 0, HOLE) + rrect(17, 35.5, 30, 2.6, 0, HOLE)
    handles = "".join(rrect(27, y, 10, 3.6, 1.8, HOLE) for y in (16, 28, 40.5))
    return cab + lines + handles

@small("navit")
def navit_s():
    road = rrect(15, 11, 21, 38, 3, INK)
    dashes = "".join(rrect(23.8, y, 3.6, 8, 1.8, HOLE) for y in (14, 27))
    t = (_badge(42, 38, 11) +
         f'<circle cx="42" cy="38" r="5" fill="none" stroke="{HOLE}" stroke-width="3.2"/>')
    return road + dashes + t

@small("nbteditor")
def nbteditor_s():
    return stroke("M14.5 44V18L28 44V18", INK, 5) + stroke("M32 18H50M41 18V44", INK, 5)

@small("nbtexplorer")
def nbtexplorer_s():
    parts = [(28.5, 12, 7, 37), (16, 21, 13, 5.5), (16, 21, 5.5, 11), (35, 17, 11, 5.5),
             (40.5, 11, 5.5, 11), (35, 31, 13, 5.5)]
    return "".join(rrect(x, y, w, h, 1, INK) for x, y, w, h in parts)

@small("ncrack")
def ncrack_s():
    body = path("M21 30C25 25.5 34 25.5 38 29C41 31.5 41 36.5 37 39C33 41 25 41 21 37.5Z", INK)
    tail = stroke("M37 31C44.5 31 47.5 23.5 44 18C42 15 37 15 36 19", INK, 4.5)
    claws = stroke("M20 31L15 23.5M20 37L15 43.5", INK, 4)
    return body + circle(20, 34, 4.5, INK) + tail + claws + poly([(34, 16.5), (40, 20), (34, 23)], INK, 1.5)

@small("ndisgtk")
def ndisgtk_s():
    return _gear_f(32, 30, 18, INK, 6) + circle(32, 30, 9.5, HOLE) + circle(32, 30, 4, INK)

@small("nemiver")
def nemiver_s():
    body = rrect(27.5, 11, 9, 6, 1.5, INK) + rrect(23, 17.5, 18, 6, 2.5, INK) + rrect(19, 25, 26, 24, 5, INK)
    bug = (path("M32 31C36 31 38 34 38 38C38 42 35.5 45 32 45C28.5 45 26 42 26 38C26 34 28 31 32 31Z", HOLE))
    return body + bug

def _nero_s():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="5.5"/>'
    flame = path("M32 42C26 42 23 38 23 34C23 29 27 26 28 21C31 24 31 27 30 29"
                 "C33 27 35 23 34 18C39 22 41 28 41 34C41 38 38 42 32 42Z", INK)
    return ring + g(flame, "translate(32 31) scale(.72) translate(-32 -30)")

@small("nerolinux")
def nerolinux_s():
    return _nero_s()

@small("nerolinuxexpress")
def nerolinuxexpress_s():
    return _nero_s()

@small("net.baseart.Glide")
def glide_s():
    board = rrect(14, 22, 36, 26, 3, INK)
    top = g(rrect(14, 12.5, 36, 7, 2, INK) +
            "".join(poly([(x, 12.5), (x + 5, 12.5), (x + 1, 19.5), (x - 4, 19.5)], HOLE) for x in (24, 36)),
            "rotate(-8 14 19)")
    return board + top + poly([(27, 28), (39, 35), (27, 42)], HOLE, 2.5)

@small("net.daase.journable")
def journable_s():
    page = rrect(14, 15, 31, 32, 4, INK)
    rings = "".join(stroke(f"M{x} 11.5V18", INK, 3.4) for x in (21, 29, 37))
    pd = "M48 24L31 43"
    return page + rings + stroke(pd, HOLE, 10) + stroke(pd, INK, 6) + poly([(27.5, 47), (29, 40.5), (34, 45.5)], INK, 1.2)

@small("net.danigm.loop")
def loop_s():
    return _mic(12, 16) + _mic(0, 20)

@small("net.danigm.timetrack")
def timetrack_s():
    ring = f'<circle cx="32" cy="30" r="16" fill="none" stroke="{INK}" stroke-width="4.4"/>'
    x1, y1 = pt(32, 30, 11, -90)
    x2, y2 = pt(32, 30, 11, -10)
    wedge = path(f"M32 30L{f(x1)} {f(y1)}A11 11 0 0 1 {f(x2)} {f(y2)}Z", INK)
    return ring + wedge + stroke("M32 30L24.5 39", INK, 3.6)

@small("net.davidotek.pupgui2")
def pupgui2_s():
    return stroke("M32 17V48M18 28L32 14L46 28", INK, 6.5)

@small("net.imput.helium")
def helium_s():
    return "".join(line(*pt(32, 30, 4, a), *pt(32, 30, 17, a), INK, 4.4)
                   for a in range(-90, 270, 60))

@small("natron")
def natron_s():
    hexa = poly([pt(32, 30, 18, a) for a in range(0, 360, 60)], INK, 3)
    return hexa + stroke("M25 39V21L39 39V21", HOLE, 5)
