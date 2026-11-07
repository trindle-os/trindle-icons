# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 28: forkgram to fyi.zoey.Boop-GTK.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import arc_arrow_b, gear, registry

ICONS, SMALL, reg, small = registry()

@reg("forkgram", DEEP_PURPLE_LIGHT)
def forkgram():
    plane = poly([(15, 29), (47, 16.5), (41.5, 44), (32, 36.5), (27, 41), (26.5, 34)], INK, 2.5)
    fold = poly([(26.5, 34), (41, 22.5), (32, 36.5)], DEEP_PURPLE_DEEP, 1)
    return plane + fold

@reg("foursquare", PINK)
def foursquare():
    badge = poly([(19, 12.5), (46, 12.5), (42, 33), (33.5, 33), (24.5, 47.5), (19, 47.5)], INK, 3.5)
    f_ = stroke("M25.5 40V19H39.5", HOLE, 3.8) + stroke("M25.5 26.5H36", HOLE, 3.8)
    return badge + f_

@reg("franz", LIGHT_BLUE_DEEP)
def franz():
    tache = path("M32 31C29 26.5 24 26.5 21 29.5C19 31.5 16 31.5 13.5 29.5C13.5 35 18 38.5 22.5 38.5"
                 "C26.5 38.5 29.5 36.5 32 34.5C34.5 36.5 37.5 38.5 41.5 38.5C46 38.5 50.5 35 50.5 29.5"
                 "C48 31.5 45 31.5 43 29.5C40 26.5 35 26.5 32 31Z", INK)
    horn = path("M18 25C15 21 15 16 18 12.5C18.5 16.5 20.5 19.5 24 21.5Z", INK)
    return tache + horn + g(horn, "matrix(-1 0 0 1 64 0)")

def _forti():
    shield = path("M32 11.5L47 16V28.5C47 38.5 40.5 45 32 48.5C23.5 45 17 38.5 17 28.5V16Z", INK)
    cells = ""
    for y, row in [(19.5, [(21, 4.5), (27.5, 9), (38.5, 4.5)]),
                   (27, [(21, 6.5), (29.5, 5), (36.5, 6.5)]),
                   (34.5, [(22.5, 3), (27.5, 9), (38.5, 3)])]:
        cells += "".join(rrect(x, y, w, 5, 1.5, HOLE) for x, w in row)
    return shield + cells

@reg("forticlient", BLUE_DEEP)
def forticlient():
    return _forti()

@reg("forticlientsslvpn", RED_DEEP)
def forticlientsslvpn():
    return _forti()

@reg("fr.romainvigier.MetadataCleaner", DEEP_PURPLE_LIGHT)
def metadatacleaner():
    cx = 35
    prints = ""
    for r in (3.5, 8, 12.5):
        prints += stroke(f"M{f(cx - r)} {f(38 - r * .3)}V26A{f(r)} {f(r)} 0 0 1 {f(cx + r)} 26V{f(40 - r * .2)}", INK, 2.6)
    sponge = g(rrect(14, 34, 17, 12, 4, AMBER_LIGHT, f' stroke="{HOLE}" stroke-width="2"'), "rotate(-15 22.5 40)")
    holes = circle(19.5, 40, 1.4, AMBER_DEEP) + circle(25, 38.5, 1.4, AMBER_DEEP)
    return prints + sponge + holes

@reg("fslint_icon", GREY_DEEP)
def fslint():
    page = rrect(18, 12, 28, 36, 4, INK)
    lens = f'<circle cx="31" cy="27.5" r="6.5" fill="none" stroke="{HOLE}" stroke-width="3.4"/>'
    return page + lens + line(35.8, 32.3, 40.5, 37.5, HOLE, 4.2)

@reg("fwupd", DEEP_PURPLE)
def fwupd():
    chip = rrect(18, 12, 24, 31, 3.5, INK)
    pins = "".join(rrect(13.5, y, 6, 2.6, 1.3, INK) + rrect(40.5, y, 6, 2.6, 1.3, INK)
                   for y in (16, 22, 28))
    slots = "".join(line(x, 17, x, 29, HOLE, 2.2) for x in (25, 30, 35))
    badge = circle(41, 39.5, 10, HOLE) + circle(41, 39.5, 8.3, INK)
    arrow = arc_arrow_b(41, 39.5, 4.2, 150, 60, HOLE, 2.4, 2.6)
    return pins + chip + slots + badge + arrow

@reg("fr.romainvigier.zap", AMBER_DEEP)
def zap():
    return poly([(37.5, 11), (18.5, 33), (30.5, 33), (26.5, 49), (45.5, 25.5), (33.5, 25.5), (38, 11)], INK, 2.5)

@reg("foxit-reader", ORANGE_DEEP)
def foxit():
    s, e = pt(31, 31, 11.5, -58), pt(31, 31, 11.5, 28)
    ring = stroke(f"M{f(s[0])} {f(s[1])}A11.5 11.5 0 1 0 {f(e[0])} {f(e[1])}", INK, 7)
    tail = path("M34.5 17.5C39 15 43.5 14 48.5 11.5C48 18 46 23.5 41.5 27.5"
                "C41 24 39 21 34.5 17.5Z", INK)
    return ring + tail

@reg("freac", BLUE_GREY)
def freac():
    body = gear(32, 30, 17, 13, 9, INK)
    hole = circle(32, 30, 8.2, HOLE)
    note = (circle(30, 33.5, 2.7, INK) + line(31.8, 33.5, 31.8, 24, INK, 2.2)
            + stroke("M31.8 24.2C33.5 25 35.5 25.8 35.5 28.2", INK, 2.2))
    return body + hole + note

@reg("freedesktop", BLUE)
def freedesktop():
    links = line(22, 20, 42, 26, INK, 2.2) + line(22, 20, 28, 40, INK, 2.2) + line(42, 26, 28, 40, INK, 2.2)
    return (links + rrect(14, 13, 16, 13, 3, INK) + rrect(35, 20, 15, 12, 3, INK)
            + rrect(23.5, 36, 9, 8, 2.2, INK))

@reg("freedownloadmanager", LIGHT_BLUE_DEEP)
def fdm():
    box = stroke("M38 20.5V17A3 3 0 0 0 35 14H18A3 3 0 0 0 15 17V43A3 3 0 0 0 18 46H35A3 3 0 0 0 38 43V39.5", INK, 4)
    arrow = line(24, 30, 42, 30, INK, 5.5) + poly([(39.5, 20.5), (50, 30), (39.5, 39.5)], INK, 3)
    return box + arrow

@reg("freefilesync", BROWN_SOFT)
def freefilesync():
    return (arc_arrow_b(32, 30, 13, 195, 330, INK, 4.5, 5)
            + arc_arrow_b(32, 30, 13, 15, 150, INK, 4.5, 5))

@reg("frescobaldi", TEAL_DEEP)
def frescobaldi():
    pad = path("M14 39C14 33 22 29.5 32 29.5C42 29.5 50 33 50 39C50 44.5 42 48 32 48C22 48 14 44.5 14 39Z", TEAL_LIGHT)
    back = poly([pt(32, 31, 16 if k % 2 == 0 else 6.5, -78.75 + 22.5 * k) for k in range(16)], TEAL_SOFT, 2)
    front = poly([pt(32, 30, 13 if k % 2 == 0 else 5.5, -90 + 22.5 * k) for k in range(16)], INK, 2)
    return pad + back + front + circle(32, 30, 4, AMBER_LIGHT)

@reg("friture", DEEP_ORANGE_DEEP)
def friture():
    ring = f'<circle cx="37" cy="24" r="10.5" fill="none" stroke="{INK}" stroke-width="4.2"/>'
    return line(29.5, 31.5, 17, 44, INK, 6.5) + ring + circle(37, 24, 5.2, INK)

@reg("fspy", BLUE_GREY_DARK)
def fspy():
    arms = line(15, 16, 36.5, 29.5, RED_LIGHT, 3.6) + line(49, 16, 27.5, 29.5, DEEP_PURPLE_SOFT, 3.6)
    tri = stroke("M23.5 31H40.5L32 45Z", INK, 3.6)
    return arms + tri

@reg("fusion-icon", RED_DEEP)
def fusion():
    half = path("M37 11C24 12.5 14.5 21.5 17.5 31C19.5 37.5 28 39 31.5 33.5"
                "C34 29.5 30 25.5 26.5 28.5C25 22.5 28.5 16 37 11Z", INK)
    return g(half + g(half, "rotate(180 32 30)"), "translate(32 30) scale(1.12) translate(-32 -30)")

def _freeoffice(letter):
    frame = f'<rect x="14.5" y="12.5" width="35" height="35" rx="3.5" fill="none" stroke="{INK}" stroke-width="2.4"/>'
    corner = rrect(18, 41, 3.5, 3.5, 1, INK)
    return frame + corner + letter

@reg("freeoffice-planmaker", BLUE_GREY)
def fo_planmaker():
    return _freeoffice(stroke("M27 40V20.5H33.5A5.5 5.5 0 0 1 33.5 31.5H27", INK, 5))

@reg("freeoffice-presentations", ORANGE_DEEP)
def fo_presentations():
    return _freeoffice(stroke("M37.5 23C36.5 21 34.5 20 32 20C28.8 20 26.5 21.8 26.5 24.5"
                              "C26.5 30 37.8 28.5 37.8 34.5C37.8 37.8 35.3 40 32 40"
                              "C29.3 40 27.2 39 26 37", INK, 4.6))

@reg("freeoffice-textmaker", RED_DEEP)
def fo_textmaker():
    return _freeoffice(stroke("M23.5 20.5H40.5M32 20.5V40", INK, 5))

@reg("freeplane", ORANGE_DEEP)
def freeplane():
    body = circle(29, 32, 14.5, INK)
    stripes = (stroke("M17 24C22 26 25 32 24 45", HOLE, 3.4)
               + stroke("M24.5 18C30 21 33.5 28 33 40", HOLE, 3.4))
    eyes = (circle(37, 24, 7.2, HOLE) + circle(37, 24, 5.6, INK) + circle(36, 25, 2.6, HOLE)
            + circle(46.5, 19.5, 5.5, HOLE) + circle(46.5, 19.5, 4, INK) + circle(46, 20.5, 2, HOLE))
    grin = stroke("M36 36C39 37.5 42 36.5 44 34", HOLE, 2.4)
    return body + stripes + eyes + grin

@reg("fritzing", RED_DEEP)
def fritzing():
    f_ = stroke("M39.5 17.5C38 15 36 14 33.5 14C30 14 28 16.5 28 20V35", INK, 5)
    bar = line(21.5, 24.5, 35, 24.5, INK, 5)
    ring = f'<circle cx="28" cy="41" r="5" fill="none" stroke="{INK}" stroke-width="4"/>'
    return f_ + bar + ring

@reg("freecad", RED_DEEP)
def freecad():
    f_ = poly([(16, 12), (41, 12), (41, 19.5), (24.5, 19.5), (24.5, 26), (36, 26), (36, 33),
               (24.5, 33), (24.5, 48), (16, 48)], INK, 2)
    cog = circle(40.5, 39.5, 11.5, HOLE) + gear(40.5, 39.5, 9.5, 7, 8, BLUE_SOFT, rounding=1.5)
    return f_ + cog + circle(40.5, 39.5, 3, HOLE)

@reg("freetube", RED_DEEP)
def freetube():
    return (rrect(16, 13, 7.5, 34, 3.75, INK) + rrect(16, 13, 31, 7.5, 3.75, INK)
            + poly([(29.5, 26), (46.5, 35), (29.5, 44)], INK, 3.5))

@reg("freezer", PINK_DEEP)
def freezer():
    body = rrect(19, 11.5, 26, 37, 5, INK)
    shelves = "".join(line(19, y, 45, y, HOLE, 2.2, "butt") for y in (21, 30, 39.5))
    handles = line(24, 14.8, 24, 17.8, HOLE, 2.2) + line(24, 24.3, 24, 27, HOLE, 2.2)
    return body + shelves + handles

@reg("frostwire", LIGHT_BLUE_DEEP)
def frostwire():
    w1 = stroke("M13.5 31C17.5 26.5 21.5 26.5 25.5 31S33.5 35.5 38.5 31S46.5 26.5 50.5 31", INK, 2.4)
    w2 = stroke("M13.5 31C17.5 35.5 21.5 35.5 25.5 31S33.5 26.5 38.5 31S46.5 35.5 50.5 31", INK, 2.4)
    barbs = (line(25, 15, 37, 45, INK, 2.8) + line(39, 15, 27, 45, INK, 2.8)
             + line(29.5, 38, 34.5, 24, INK, 2.8))
    return w1 + w2 + barbs

@reg("forza-horizon-5", PINK_LIGHT)
def forza():
    blade = poly([(13.5, 28.5), (23.5, 19.5), (50.5, 19.5), (46.5, 25.5), (25.5, 25.5)], INK, 1.8)
    bars = (poly([(14, 41), (22.5, 29), (30, 29), (22.5, 41)], INK, 1.8)
            + poly([(26, 41), (32.5, 29), (38, 29), (32, 41)], INK, 1.8)
            + poly([(35.5, 41), (41, 29), (45.5, 29), (40.5, 41)], INK, 1.8))
    return blade + bars

@reg("four-in-a-row", BLUE_DEEP)
def four_in_a_row():
    board = [".YW.", "YWW.", "WYYW", "YWYY"]
    out = ""
    for r, row in enumerate(board):
        for c, ch in enumerate(row):
            col = {".": BLUE_DARK, "W": INK, "Y": AMBER_LIGHT}[ch]
            out += circle(18.5 + 9 * c, 16.5 + 9 * r, 3.9, col)
    return out

@reg("fran-bow", BLUE_GREY_DARK)
def fran_bow():
    hair = path("M16 38V26C16 17 22.5 12 32 12C41.5 12 48 17 48 26V38"
                "C45.5 36.5 43.5 37.5 41.5 36L40.5 40H23.5L22.5 36C20.5 37.5 18.5 36.5 16 38Z", INK)
    body = path("M22 49C22 45 26 43 32 43C38 43 42 45 42 49Z", INK)
    eyes = circle(26, 29.5, 3.4, HOLE) + circle(38, 29.5, 3.4, HOLE)
    tears = line(25.5, 33.5, 25.5, 37, RED_DEEP, 2.2) + line(38.5, 33.5, 38.5, 36.5, RED_DEEP, 2.2)
    return hair + body + eyes + tears

@reg("freeciv-client", AMBER_DARK)
def freeciv_client():
    return _freeciv()

def _freeciv():
    globe = circle(32, 30, 14.5, INK)
    land = (path("M22 21C25 18 29 19 30 22C31 25 27 27 28 30C29 33 24 34 21.5 31C19 28 19.5 23.5 22 21Z", AMBER_DEEP)
            + path("M35 18C39 17.5 43 20 43 23.5C43 26 40 26.5 38 25C36 23.5 33 21 35 18Z", AMBER_DEEP)
            + path("M36 34C39 32 43 33 42.5 36.5C42 39.5 38 41.5 35.5 40C33.5 38.5 33.5 35.5 36 34Z", AMBER_DEEP))
    band = ('<ellipse cx="32" cy="32.5" rx="18" ry="5.2" transform="rotate(-10 32 32.5)" '
            f'fill="none" stroke="{HOLE}" stroke-width="5.5"/>'
            '<ellipse cx="32" cy="32.5" rx="18" ry="5.2" transform="rotate(-10 32 32.5)" '
            f'fill="none" stroke="{INK}" stroke-width="2.6"/>')
    return globe + land + band

@reg("freeciv-server", AMBER_DARK)
def freeciv_server():
    world = g(_freeciv(), "translate(29 28) scale(.86) translate(-32 -30)")
    badge = circle(42.5, 40, 9.5, HOLE) + gear(42.5, 40, 7.6, 5.6, 8, INK, rounding=1) + circle(42.5, 40, 2.3, HOLE)
    return world + badge

def _doom():
    d = stroke("M14 22V38H17.5Q21.5 38 21.5 30Q21.5 22 17.5 22Z", INK, 3.2)
    o1 = f'<rect x="24.5" y="22" width="7" height="16" rx="3.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    o2 = f'<rect x="34.5" y="22" width="7" height="16" rx="3.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    m = stroke("M44.5 38V22L47.25 30L50 22V38", INK, 3.2)
    return d + o1 + o2 + m

@reg("freedoom1", INDIGO)
def freedoom1():
    return _doom()

@reg("freedoom2", RED_DEEP)
def freedoom2():
    return _doom()

@reg("freedroid", RED)
def freedroid():
    st = poly([pt(32, 30, (19 if k in (0, 4) else 18.5) if k % 2 == 0 else 6, -90 + 45 * k) for k in range(8)], INK, 1.5)
    band = f'<ellipse cx="32" cy="30" rx="13.5" ry="9" fill="{INK}" stroke="{HOLE}" stroke-width="2.4"/>'
    digits = (f'<rect x="20.5" y="25" width="5.5" height="10" rx="2.75" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
              f'<rect x="28.5" y="25" width="5.5" height="10" rx="2.75" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
              + stroke("M37 26.8L39.8 25V35", HOLE, 2.6))
    return st + band + digits

@reg("freedroidrpg", CYAN_DARK)
def freedroidrpg():
    rods = line(20, 21, 14.5, 15.5, INK, 2.4) + line(44, 21, 49.5, 15.5, INK, 2.4)
    knobs = circle(14.5, 15.5, 3, INK) + circle(49.5, 15.5, 3, INK)
    head = rrect(18, 16, 28, 29, 9, INK) + rrect(28.5, 12.5, 7, 5, 1.5, INK)
    eyes = circle(26, 27.5, 3.2, HOLE) + circle(38, 27.5, 3.2, HOLE)
    beak = poly([(24.5, 34), (39.5, 34), (32, 41.5)], ORANGE, 3)
    return rods + knobs + head + eyes + beak

@reg("freegish", RED_DEEP)
def freegish():
    blob = path("M13 38C13 24.5 21 17 32 17C43 17 51 24.5 51 38C51 42.5 46 44 32 44C18 44 13 42.5 13 38Z", INK)
    eye = path("M18.5 35C20 30 24.5 28.5 29.5 31.5L27.5 35.5C26.5 36.5 19.5 36.5 18.5 35Z", HOLE)
    return blob + eye + g(eye, "matrix(-1 0 0 1 64 0)")

@reg("freeorion", BLUE_DARK)
def freeorion():
    ring = f'<circle cx="32" cy="30" r="11" fill="none" stroke="#6FBAF6" stroke-width="4.5"/>'
    pts = [pt(32, 30, (18 if k in (0, 4) else 17) if k % 2 == 0 else 3.2, -90 + 45 * k) for k in range(8)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
    return (ring + path(d, "none", f' stroke="{HOLE}" stroke-width="5" stroke-linejoin="round"')
            + poly(pts, INK, 1))

@reg("freetennis", YELLOW_DARK)
def freetennis():
    ball = circle(32, 30, 16, INK)
    seams = (stroke("M20.5 18.5C27 24.5 27 35.5 20.5 41.5", HOLE, 3)
             + stroke("M43.5 18.5C37 24.5 37 35.5 43.5 41.5", HOLE, 3))
    return ball + seams

@reg("frogatto", GREY_DEEP)
def frogatto():
    head = path("M14 37C14 29.5 20 27 32 27C44 27 50 29.5 50 37C50 44.5 43 47.5 32 47.5C21 47.5 14 44.5 14 37Z", INK)
    eyes = ""
    for x in (24, 40):
        eyes += (f'<ellipse cx="{x}" cy="21.5" rx="7.5" ry="9.5" fill="{INK}" stroke="{HOLE}" stroke-width="2.2"/>'
                 + circle(x + 1.5, 23.5, 2.8, HOLE))
    mouth = stroke("M21 39Q24.5 36 28 39T35 39T42 39", HOLE, 2.4)
    return head + eyes + mouth

@reg("frogr", CYAN_DEEP)
def frogr():
    legs = "".join(stroke(d, INK, 3.6) for d in [
        "M25 24L18.5 20.5L18 15", "M39 24L45.5 20.5L46 15",
        "M25 38L18 41.5V47", "M39 38L46 41.5V47"])
    body = rrect(22, 17, 20, 28, 9.5, INK)
    eyes = "".join(circle(x, 17.5, 5, HOLE) + circle(x, 17.5, 3.6, INK) + circle(x, 17.5, 1.8, PURPLE)
                   for x in (26, 38))
    return legs + body + eyes

@reg("frozen-bubble", PURPLE_DEEP)
def frozen_bubble():
    body = path("M19.5 24C21 15.5 29 12 37.5 13.5C46 15 51 23 50 32C49 42 42 47.5 33 47.5"
                "C25 47.5 20.5 42 20.5 34Z", PURPLE_SOFT)
    belly = f'<ellipse cx="28.5" cy="37" rx="7.5" ry="9" fill="{INK}"/>'
    beak = poly([(14, 27), (21.5, 24), (25, 30), (18.5, 32.5)], AMBER_LIGHT, 3)
    eyes = (circle(22.5, 20, 4.5, INK) + circle(31.5, 19, 5.2, INK)
            + circle(23, 20.5, 2, HOLE) + circle(32.5, 19.5, 2.3, HOLE))
    return body + belly + beak + eyes

@reg("fs-uae-arcade", INDIGO_DARK)
def fs_uae_arcade():
    rows = ["..###..", ".#####.", "##.#.##", "#######", ".#...#.", "#.....#"]
    u = 5
    out = ""
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "#":
                out += rrect(14.5 + c * u - .15, 15 + r * u - .15, u + .3, u + .3, .6, INK)
    return out

@reg("fs-uae-launcher", PURPLE_DEEP)
def fs_uae_launcher():
    back = stroke("M14 33L23 21L32 33", YELLOW, 5)
    front = stroke("M23 33L32 21L41 33", INK, 5)
    fs = (stroke("M37.5 47V38H42.5M37.5 42.5H41.5", INK, 2.4)
          + stroke("M49.5 38.8C49 38.2 48 37.8 47 37.8C45.5 37.8 44.5 38.8 44.5 40C44.5 42.8 50 41.8 50 44.8"
                   "C50 46.1 48.8 47 47.2 47C46 47 45 46.5 44.4 45.8", INK, 2.4))
    return back + front + fs

@reg("ftb-app", BLUE_GREY_DARK)
def ftb():
    f_ = stroke("M14.5 43V25H22.5M14.5 33.5H21", INK, 4)
    t = stroke("M24.5 17H36.5M30.5 17V37", INK, 4)
    b = stroke("M40 25H44.5A4 4 0 0 1 44.5 33H40M40 25V43H45A5 5 0 0 0 45 33H40", INK, 4)
    return f_ + t + b

@reg("ftl-faster-than-light", GREY_DARK)
def ftl():
    return (stroke("M15 40V20H23.5M15 30H21.5", INK, 4.6)
            + stroke("M26.5 20H38M32.25 20V40", INK, 4.6)
            + stroke("M41.5 20V40H49.5", INK, 4.6))

@reg("full-throttle-remastered", BROWN)
def full_throttle():
    f_ = (stroke("M22.5 15V45", INK, 4.6) + stroke("M17.5 14H31.5V19", INK, 3)
          + stroke("M22.5 29H28.5M28.5 26.5V31.5", INK, 3) + stroke("M18 46.5H27", INK, 3))
    t = (stroke("M34.5 19V14H49V19", INK, 3) + stroke("M41.75 15V45", INK, 4.6)
         + stroke("M37.25 46.5H46.25", INK, 3))
    return f_ + t

def _arrow(cx, cy, rot, fill):
    a = poly([(0, -5.5), (5.3, 0), (2.4, 0), (2.4, 5), (-2.4, 5), (-2.4, 0), (-5.3, 0)], fill, 2)
    return g(a, f"translate({f(cx)} {f(cy)}) rotate({rot})")

@reg("funkin", PINK_DEEP)
def funkin():
    return "".join(_arrow(16 + 10.67 * k, 30, rot, INK) for k, rot in enumerate((-90, 180, 0, 90)))

@reg("fuse", BLUE_GREY_DARK)
def fuse():
    zx = stroke("M14.5 14H23.5L14.5 26H23.5", INK, 3.4) + stroke("M27.5 14L36.5 26M36.5 14L27.5 26", INK, 3.4)
    cols = [RED, AMBER, BROWN_SOFT, LIGHT_BLUE]
    stripes = "".join(line(22 + 6 * k, 49, 50, 21 + 6 * k, c, 4.4, "butt") for k, c in enumerate(cols))
    return zx + stripes

@reg("fyi.zoey.Boop-GTK", DEEP_PURPLE)
def boop():
    back = rrect(14, 12, 20, 20, 5, AMBER_SOFT)
    mid = rrect(21.5, 19, 20, 20, 6, ORANGE, f' stroke="{HOLE}" stroke-width="2.4"')
    front = circle(39.5, 37.5, 10.5, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    return back + mid + front

def _forti_s():
    shield = path("M32 11L48 15.5V28.5C48 39 41 45.5 32 49C23 45.5 16 39 16 28.5V15.5Z", INK)
    cells = "".join(rrect(x, y, w, 6, 2, HOLE) for y, row in
                    [(19, [(21, 5), (29, 6), (38, 5)]), (29, [(22.5, 7.5), (34, 7.5)])]
                    for x, w in row)
    return shield + cells

@small("forticlient")
def forticlient_s():
    return _forti_s()

@small("forticlientsslvpn")
def forticlientsslvpn_s():
    return _forti_s()

@small("four-in-a-row")
def four_in_a_row_s():
    board = ["YW.", "WYW", "YWY"]
    return "".join(circle(20 + 12 * c, 18 + 12 * r, 5.3, {".": BLUE_DARK, "W": INK, "Y": AMBER_LIGHT}[ch])
                   for r, row in enumerate(board) for c, ch in enumerate(row))

@small("fr.romainvigier.MetadataCleaner")
def metadatacleaner_s():
    prints = "".join(stroke(f"M{f(34 - r)} 40V27A{f(r)} {f(r)} 0 0 1 {f(34 + r)} 27V40", INK, 3)
                     for r in (4, 11))
    return prints + g(rrect(13, 34, 17, 12, 4, AMBER_LIGHT, f' stroke="{HOLE}" stroke-width="2.4"'), "rotate(-15 21.5 40)")

@small("freedroid")
def freedroid_s():
    st = poly([pt(32, 30, 19 if k % 2 == 0 else 6, -90 + 45 * k) for k in range(8)], INK, 1.5)
    band = f'<ellipse cx="32" cy="30" rx="12.5" ry="8.5" fill="{INK}" stroke="{HOLE}" stroke-width="2.4"/>'
    return st + band + stroke("M30 26.8L33.5 24.5V35.5", HOLE, 3)

@small("freefilesync")
def freefilesync_s():
    return (arc_arrow_b(32, 30, 12, 200, 320, INK, 4.5, 6.5)
            + arc_arrow_b(32, 30, 12, 20, 140, INK, 4.5, 6.5))

@small("freedoom1")
def freedoom1_s():
    return _doom_s()

@small("freedoom2")
def freedoom2_s():
    return _doom_s()

def _doom_s():
    d = stroke("M13.5 21V39H17.5Q22 39 22 30Q22 21 17.5 21Z", INK, 2.6)
    o1 = f'<rect x="24.5" y="21" width="7" height="18" rx="3.5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
    o2 = f'<rect x="34" y="21" width="7" height="18" rx="3.5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
    return d + o1 + o2 + stroke("M44 39V21L47.25 30L50.5 21V39", INK, 2.6)

@small("frostwire")
def frostwire_s():
    w = stroke("M13 31C17.5 26 22 26 26 31S34.5 36 38.5 31S46.5 26 51 31", INK, 3)
    return w + line(25, 15, 37, 45, INK, 3.2) + line(39, 15, 27, 45, INK, 3.2)

@small("fs-uae-launcher")
def fs_uae_launcher_s():
    return (stroke("M13 30L20 39L32 16", YELLOW, 5.5)
            + stroke("M24 30L31 39L43 16", INK, 5.5))

@small("funkin")
def funkin_s():
    return "".join(g(_arrow(0, 0, rot, INK), f"translate({x} {y}) scale(1.45)")
                   for x, y, rot in [(22, 21, -90), (42, 21, 180), (22, 40, 0), (42, 40, 90)])

@small("fwupd")
def fwupd_s():
    chip = rrect(15, 11, 27, 32, 4, INK)
    badge = circle(41, 39, 11.5, HOLE) + circle(41, 39, 9.5, INK)
    return chip + badge + arc_arrow_b(41, 39, 4.8, 150, 60, HOLE, 2.6, 3)

@small("freeorion")
def freeorion_s():
    pts = [pt(32, 30, 19 if k % 2 == 0 else 4, -90 + 45 * k) for k in range(8)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
    ring = f'<circle cx="32" cy="30" r="11" fill="none" stroke="#6FBAF6" stroke-width="5"/>'
    return (ring + path(d, "none", f' stroke="{HOLE}" stroke-width="5" stroke-linejoin="round"')
            + poly(pts, INK, 1))

@small("fuse")
def fuse_s():
    zx = stroke("M13.5 13H24L13.5 27H24", INK, 3.4) + stroke("M28 13L38 27M38 13L28 27", INK, 3.4)
    cols = [RED, AMBER, BLUE_GREY_LIGHT, LIGHT_BLUE]
    return zx + "".join(line(24 + 7 * k, 50, 51, 23 + 7 * k, c, 5, "butt") for k, c in enumerate(cols))
