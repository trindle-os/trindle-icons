# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 49: noson to onionshare80.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, BLUE_LIGHT, BLUE_SOFT, BROWN_SOFT, circle, cpath, cut, CX, CY, CYAN,
    CYAN_DARK, CYAN_DEEP, CYAN_SOFT, DEEP_ORANGE, DEEP_PURPLE_DARK, DEEP_PURPLE_LIGHT, f, g,
    GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK, INDIGO_LIGHT, INDIGO_SOFT, INK,
    LIGHT_BLUE, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE, ORANGE_DARK, ORANGE_DEEP, path,
    PINK, PINK_SOFT, poly, pt, PURPLE_DARK, RED, RED_DEEP, RED_LIGHT, rrect, stroke, TEAL,
)
from glyphs.kit import _gear_g, registry, _star_e

ICONS, SMALL, reg, small = registry()


def _arrow_arc(cx, cy, r, a0, a1, col, w, head=4.5):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1 - 12)
    arc = stroke(f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 0 1 {f(x1)} {f(y1)}", col, w)
    tip = pt(cx, cy, r, a1)
    b1, b2 = pt(cx, cy, r + head, a1 - 22), pt(cx, cy, r - head, a1 - 22)
    return arc + poly([tip, b1, b2], col, 1.5)


@reg("noson", DEEP_ORANGE)
def noson():
    return cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 11), INK) + circle(CX, CY, 7.5, INK)


@reg("nuclear", DEEP_PURPLE_LIGHT)
def nuclear():
    return (poly([(15.5, 17), (30.5, 17), (23, 30.5)], INK, 2.5) +
            poly([(33.5, 17), (48.5, 17), (41, 30.5)], INK, 2.5) +
            poly([(24.5, 33), (39.5, 33), (32, 46.5)], INK, 2.5))


@reg("nulloy", GREY_DARK)
def nulloy():
    top = path("M14 14C22 13 32 15 38 19.5C36.5 25 32.5 29 26.5 30C21 30 17 26.5 15.5 21Z", INK)
    bottom = path("M15 47C17 39.5 21 34.5 27.5 32.5C31.5 32 34.5 33 36 35C33 42 26 46 15 47Z", INK)
    feathers = "".join(path(f"M38 {y + 5}C40.5 {y + 1} 44 {y - 1} 48 {y - 1}"
                            f"C47 {y + 3} 44 {y + 6} 38 {y + 5}Z", INK) for y in (26, 33, 40))
    return top + bottom + circle(43.5, 17.5, 4.3, INK) + feathers


@reg("odio", PINK)
def odio():
    hs = [8, 14, 22, 28, 18, 26, 14, 8]
    return "".join(line(18 + 4 * i, CY - h / 2, 18 + 4 * i, CY + h / 2, INK, 2.8)
                   for i, h in enumerate(hs))


@reg("ocenaudio", AMBER_DEEP)
def ocenaudio():
    band = stroke("M17 33V29A15 15 0 0 1 47 29V33", INK, 3.6)
    cups = rrect(13.5, 28, 7, 14, 3, INK) + rrect(43.5, 28, 7, 14, 3, INK)
    head = path("M32 17C39 17 43 23 43 31C43 40 38 47 32 47C26 47 21 40 21 31C21 23 25 17 32 17Z", INK)
    eyes = line(25.5, 27, 30, 29, HOLE, 2.4) + line(38.5, 27, 34, 29, HOLE, 2.4)
    mouth = path("M25.5 34C29.5 32.5 34.5 32.5 38.5 34C38 40 35.5 43 32 43C28.5 43 26 40 25.5 34Z", HOLE)
    return band + cups + head + eyes + mouth


@reg("olivia", DEEP_PURPLE_LIGHT)
def olivia():
    band = stroke("M19.5 33V29A12.5 12.5 0 0 1 44.5 29V33", INK, 4)
    cups = rrect(14.5, 29, 10, 17, 4.5, INK) + rrect(39.5, 29, 10, 17, 4.5, INK)
    bars = rrect(20, 32.5, 2.6, 10, 1.3, HOLE) + rrect(41.4, 32.5, 2.6, 10, 1.3, HOLE)
    return band + cups + bars


@reg("nostlan", PINK_SOFT)
def nostlan():
    outer = stroke("M44 17C35 12.5 20 15 16.5 26C13.5 36 20.5 45 31 45.5", INK, 4)
    right = stroke("M44.5 23C48.5 30 47.5 40 38 44", INK, 3.4)
    inner = stroke("M38.5 24C33 22 25 23.5 23.5 29", INK, 2.6)
    return outer + right + inner + path("M32 28a6 3.6 0 1 0 0.01 0Z", INK)


@reg("notable", ORANGE)
def notable():
    n = poly([(17, 14), (24, 14), (40, 35), (40, 14), (47, 14), (47, 46), (40, 46), (24, 25), (24, 38)], INK, 2)
    tip = poly([(17, 38), (24, 38), (20.5, 47)], INK, 1.5)
    return n + tip + line(17, 14, 17, 38, INK, 2)


@reg("notepadqq", BROWN_SOFT)
def notepadqq():
    book = rrect(16, 12, 32, 36, 4, INK) + rrect(16, 23.5, 32, 13, 0, HOLE)
    n = stroke("M19.5 33.5V27M19.5 29.5A2.7 2.7 0 0 1 24.9 29.5V33.5", INK, 2.2)
    q = "".join(f'<circle cx="{x}" cy="30.2" r="2.7" fill="none" stroke="{INK}" stroke-width="2.2"/>'
                + line(x + 2.7, 27.2, x + 2.7, 35, INK, 2.2) for x in (30.5, 39.5))
    return book + n + q


@reg("novprog", INDIGO_LIGHT)
def novprog():
    sheet = rrect(15, 13, 34, 34, 4, INK)
    bars = rrect(21, 26, 5.5, 16, 1.5, HOLE) + rrect(29.3, 32, 5.5, 10, 1.5, HOLE) + rrect(37.6, 19, 5.5, 23, 1.5, HOLE)
    return sheet + bars


@reg("nozbe", BLUE_LIGHT)
def nozbe():
    ring = f'<circle cx="31" cy="31" r="14.5" fill="none" stroke="{INK}" stroke-width="4.2"/>'
    tick = circle(31, 31, 6.5, INK)
    return ring + tick


@reg("np2", GREY_DEEP)
def np2():
    paws = circle(23, 44.5, 4.5, GREY_SOFT) + circle(41, 44.5, 4.5, GREY_SOFT)
    head = path("M17 20L19 12L26.5 17.5C30 16.8 34 16.8 37.5 17.5L45 12L47 20"
                "C48.5 23 49 26 49 29C49 37 41.5 42 32 42C22.5 42 15 37 15 29C15 26 15.5 23 17 20Z", INK)
    face = (rrect(23.5, 25, 3, 5, 1.5, HOLE) + rrect(37.5, 25, 3, 5, 1.5, HOLE) +
            poly([(29.5, 32), (34.5, 32), (32, 34.5)], HOLE, 1.2))
    return paws + head + face


@reg("numptyphysics", RED_LIGHT)
def numptyphysics():
    curve = stroke("M14.5 25C22 23 25 42 33 43C39 43.5 44 44 49 46", INK, 3.4)
    scribble = stroke("M36 30C33.5 24 37 16.5 42.5 16.5C47 16.5 48.5 21.5 46 25"
                      "C43.5 28.5 39 28 38.5 24.5C38 21.5 41 20 43 21.5", INK, 3.4)
    return curve + scribble


@reg("nutstore", ORANGE_DEEP)
def nutstore():
    cap = path("M15 27C15 19 22 15 32 15C42 15 49 19 49 27Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    stem = stroke("M32 15C33 13 35 12 37.5 11.5", INK, 3)
    body = path("M18.5 30.5H45.5C45.5 40 40 46 32 48.5C24 46 18.5 40 18.5 30.5Z", INK)
    return cap + stem + body


@reg("nutty", TEAL)
def nutty():
    globe = circle(30, 28, 15.5, INK)
    land = (path("M21 19C25 16.5 30 17.5 30.5 22C29 24.5 26.5 24 24.5 27.5C21.5 26 19.5 22 21 19Z", HOLE) +
            path("M33.5 29.5C37.5 28.5 41 31.5 39.5 35.5C37.5 38.5 35 40.5 32.5 41.5C31 37 30.5 32.5 33.5 29.5Z", HOLE))
    badge = circle(42, 40, 9, HOLE) + circle(42, 40, 7, INK)
    i = rrect(40.8, 38.5, 2.4, 6.5, 1.2, HOLE) + circle(42, 35.5, 1.5, HOLE)
    return globe + land + badge + i


@reg("nz.scuttlebutt.Patchwork", INDIGO)
def patchwork():
    stalks = line(24, 22, 22, 12.5, INK, 2.6) + line(30, 21, 31, 12, INK, 2.6)
    body = path("M31 30C33 22.5 40 20 45 22.5C49.5 25 51 31 49 36C47 40.5 42 43 37 42.5Z", INDIGO_SOFT)
    shell = path("M13 45C13 33 20 24.5 29 24.5C36 24.5 40.5 29 41 35V45Z", INK)
    patches = stroke("M21 45C20 39 21.5 33 25.5 28.5", HOLE, 2.2) + stroke("M30 45C29.5 39 30.5 34 34 30", HOLE, 2.2)
    horn = poly([(44, 29), (50, 26.5), (47, 31.5)], INK, 1.5)
    return stalks + body + horn + shell + patches


@reg("nsight", CYAN_DEEP)
def nsight():
    return circle(25, 30, 14, CYAN_DARK) + circle(36, 30, 14.5, HOLE) + circle(36, 30, 13, INK)


@reg("nvidia", BLUE_GREY_LIGHT)
def nvidia():
    eye = path("M13.5 30C18 23 25 19 34 18.5V14H49V46H34V41.5C25 41 18 37 13.5 30Z", INK)
    swirl = (stroke("M20 30C24 25 30 23.5 36 24.5C41 25.5 43.5 28 43.5 30"
                    "C41.5 33.5 37 36 32 36C29 36 27 34.5 27 32.5C27 30.5 29 29.5 31.5 29.5", HOLE, 2.4) +
             line(34, 18.5, 34, 22, HOLE, 2.2) + line(34, 38.5, 34, 41.5, HOLE, 2.2))
    return eye + swirl


@reg("nvim", GREY_DEEP)
def nvim():
    left = poly([(16, 19), (23.5, 12), (23.5, 48), (16, 41)], GREY_SOFT, 1.5)
    diag = poly([(23.5, 12), (29.5, 12), (40.5, 48), (34.5, 48)], INK, 1.5)
    right = poly([(40.5, 12), (48, 19), (48, 41), (40.5, 48)], INK, 1.5)
    return left + diag + right


@reg("nvtop", GREY_DARK)
def nvtop():
    box = (f'<rect x="15.5" y="13.5" width="33" height="33" rx="7" fill="none" '
           f'stroke="{INK}" stroke-width="3.6"/>')
    return box + stroke("M21.5 37V23L28 37V23", INK, 3) + stroke("M31 23L36.5 37L42.5 23", INK, 3)


@reg("nvvp", CYAN_DARK)
def nvvp():
    cols = [[INK, CYAN_SOFT, CYAN_SOFT], [INK, INK, CYAN_SOFT], [INK, CYAN, CYAN]]
    return "".join(rrect(16 + c * 11.5, 14 + r * 11.5, 9, 9, 2, cols[r][c])
                   for r in range(3) for c in range(3))


@reg("nwg-clipman", GREY_DEEP)
def nwg_clipman():
    clip = stroke("M36.5 23V40A5.5 5.5 0 0 1 25.5 40V17.5A4.7 4.7 0 0 1 34.9 17.5V37", INK, 3.4)
    return g(clip, "rotate(40 31 29)")


@reg("nwg-icon-picker", BLUE_GREY_DEEP)
def nwg_icon_picker():
    star = _star_e(20, 21, 6, 2.8, INK, 1.2)
    diamond = g(rrect(27.5, 16.5, 9, 9, 1.5, INK), "rotate(45 32 21)")
    square = rrect(39, 16, 10, 10, 2, INK)
    arrow = poly([(28, 29), (47, 37), (39.5, 39.5), (36, 47)], INK, 2.5)
    return star + diamond + square + arrow


@reg("nwg-panel", ORANGE_DEEP)
def nwg_panel():
    return stroke("M23 42V19M23 29C23 23.5 26.5 19.5 32 19.5C37.5 19.5 41 23.5 41 29V42", INK, 7)


@reg("nwg-readme-browser", LIGHT_BLUE_DEEP)
def nwg_readme():
    sheet = path("M21 11H36L45 20V46A3 3 0 0 1 42 49H21A3 3 0 0 1 18 46V14A3 3 0 0 1 21 11Z", INK)
    fold = path("M36 11V17A3 3 0 0 0 39 20H45Z", LIGHT_BLUE_SOFT)
    return sheet + fold + rrect(29, 21, 5, 14, 2.5, HOLE) + circle(31.5, 40.5, 2.8, HOLE)


@reg("nwg-shell", ORANGE_DEEP)
def nwg_shell():
    diamond = g(rrect(17.5, 15.5, 29, 29, 6, INK), "rotate(45 32 30)")
    return diamond + stroke("M37.5 20.5L26.5 27L37.5 33L26.5 39.5", HOLE, 3.8)


@reg("nwg-shell-config", ORANGE_DEEP)
def nwg_shell_config():
    on = rrect(15, 14, 34, 13, 6.5, INK) + circle(42.5, 20.5, 4.5, HOLE)
    off = rrect(15, 33, 34, 13, 6.5, ORANGE_DARK) + circle(21.5, 39.5, 4.5, INK)
    return on + off


@reg("nsm-legacy-gui", BLUE_GREY)
def nsm_legacy():
    return (stroke("M15 38V22L23 38V22", INK, 3.6) +
            stroke("M36 24.5C35 22.8 33.5 22 31.5 22C29 22 27.5 23.5 27.5 25.8"
                   "C27.5 30.5 36.5 29 36.5 34.2C36.5 36.6 34.5 38 32 38C30 38 28.5 37.2 27.5 35.5", INK, 3.6) +
            stroke("M40.5 38V22L45 31L49.5 22V38", INK, 3.6))


@reg("nsm-proxy", BLUE_GREY)
def nsm_proxy():
    return (stroke("M15 38V22H19.5A4.5 4.5 0 0 1 19.5 31H15", INK, 3.6) +
            stroke("M28 38V22H32.2A4.3 4.3 0 0 1 32.2 30.6H28M32 30.6L36.5 38", INK, 3.6) +
            stroke("M40.5 22L49.5 38M49.5 22L40.5 38", INK, 3.6))


@reg("null_team-48", LIGHT_BLUE)
def null_team():
    bubble = circle(32.5, 29, 16, INK) + poly([(19, 36), (15.5, 46.5), (27, 42.5)], INK, 2)
    phone = path("M26 24.5C26.5 23.2 27.5 22.8 28.5 23L30.2 26.8C30.3 27.4 29.7 28.3 29.2 28.8"
                 "C30.3 31.2 32.3 33.2 34.7 34.3C35.2 33.8 36.1 33.2 36.7 33.3L40.5 35"
                 "C40.7 36 40.3 37 39 37.5C34.5 39 24.5 29 26 24.5Z", HOLE)
    return bubble + g(phone, "translate(32.5 29) scale(1.25) translate(-33 -30.5)")


@reg("nym-vpn-app", INDIGO_SOFT)
def nym_vpn():
    return (rrect(16, 14, 32, 32, 6, INK) + rrect(23, 20.5, 5, 19, 1, HOLE) +
            rrect(36, 20.5, 5, 19, 1, HOLE) + poly([(23, 20.5), (28, 20.5), (41, 39.5), (36, 39.5)], HOLE))


@reg("obconf-qt", BLUE_DEEP)
def obconf():
    win = rrect(15, 13, 34, 34, 4.5, INK) + rrect(15, 20.5, 34, 2.4, 0, HOLE)
    return win + _gear_g(32, 34.5, 8.5, 6.2, 8, HOLE) + circle(32, 34.5, 2.8, INK)


@reg("obdautodoctor", BLUE_GREY_DARK)
def obdautodoctor():
    engine = (rrect(24, 15, 11, 4, 1, INK) + rrect(27.5, 17, 4, 5, 0, INK) +
              poly([(19, 21), (40, 21), (43.5, 25), (46, 25), (46, 22), (50, 22), (50, 40), (46, 40),
                    (46, 37), (43.5, 37), (39.5, 42), (22, 42), (19, 38)], INK, 2) +
              rrect(14, 27, 5, 8, 1, INK))
    bolt = poly([(35, 24), (27, 33), (32, 33), (29, 40.5), (38.5, 30), (33.5, 30), (37, 24)], HOLE, 1)
    return engine + bolt


@reg("ocaml", ORANGE_DEEP)
def ocaml():
    body = path("M15 31C15 25 18 18.5 22.5 18.5C26 18.5 26 24.5 28 24.5C30 24.5 30 17.5 34 17.5"
                "C38 17.5 38.5 25 40 25C41.5 25 41 16 45 15.5C47.5 15.3 49 17 50.5 19.5L47 21"
                "C45.5 22.5 45 26 44 30C43 33 40 35.5 36 35.5H22C18 35.5 15 34 15 31Z", INK)
    legs = (line(20, 33, 19, 46, INK, 3) + line(25, 34, 26, 46, INK, 3) +
            line(35, 34, 34, 46, INK, 3) + line(40.5, 33, 41.5, 46, INK, 3))
    return body + legs + line(15.5, 29, 14, 37, INK, 2.2)


@reg("ocrfeeder", BLUE_DEEP)
def ocrfeeder():
    lens = f'<circle cx="28.5" cy="27" r="11" fill="none" stroke="{INK}" stroke-width="4.4"/>'
    handle = line(37, 35.5, 46, 44.5, INK, 6)
    a = stroke("M24.5 32.5L28.5 21.5L32.5 32.5M26 28.5H31", INK, 2.6)
    return lens + handle + a


@reg("ocsstore", INDIGO_DARK)
def ocsstore():
    segs = "".join(g(stroke("M24.5 17A14.5 14.5 0 0 1 39.5 17", INK, 5.5), f"rotate({90 * k} 32 30)")
                   for k in range(4))
    return segs + rrect(24, 22, 16, 16, 3, INDIGO_SOFT)


@reg("octave", BLUE_DEEP)
def octave():
    ring = f'<circle cx="32" cy="30" r="13" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    sq = [(19, 30, 11), (41.2, 20.8, 7.5), (41.2, 39.2, 7.5)]
    return ring + "".join(rrect(x - s / 2, y - s / 2, s, s, 2, INK,
                                f' stroke="{HOLE}" stroke-width="2.2"') for x, y, s in sq)


@reg("octodad-dadliest-catch", AMBER_DEEP)
def octodad():
    head = path("M14 38C14 29 21 24 32 24C43 24 50 29 50 36.5C50 41 46.5 44 42 43"
                "C39 47 34 48.5 30 46C25 48.5 16.5 45.5 14 38Z", INK)
    eyes = (circle(25.5, 21, 7.5, HOLE) + circle(25.5, 21, 6, INK) + circle(27, 22, 2.4, HOLE) +
            circle(38.5, 20, 7.5, HOLE) + circle(38.5, 20, 6, INK) + circle(40, 21, 2.4, HOLE))
    tash = stroke("M22 35C26 38 30 37 32 34C34 37 38 38 42 35", HOLE, 2.6)
    return head + eyes + tash


@reg("octopi", ORANGE_DEEP)
def octopi():
    body = path("M18 30A14 14 0 0 1 46 30V45L42 41.5L38 45L34 41.5L30 45L26 41.5L22 45L18 41.5Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    eyes = (circle(25.5, 29, 4.5, HOLE) + circle(38.5, 29, 4.5, HOLE) +
            circle(26.5, 29, 2, INK) + circle(39.5, 29, 2, INK))
    return body + eyes


@reg("offensive-security", RED_DEEP)
def offsec():
    door = rrect(21, 11, 22, 29, 1.5, INK)
    man = (circle(32, 17, 2.8, HOLE) + rrect(29, 20.5, 6, 11, 2.5, HOLE) +
           rrect(29.3, 29, 2.3, 11, 1, HOLE) + rrect(32.4, 29, 2.3, 11, 1, HOLE))
    floor = poly([(21, 42.5), (43, 42.5), (49, 48), (15, 48)], INK, 1.5)
    return door + man + floor


@reg("office-address-book", BLUE)
def address_book():
    ring = f'<circle cx="31.5" cy="30" r="5" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    at = stroke("M36.5 24.5V32.5C36.5 36 41 36.5 43.5 33.5C45.5 30.5 45.5 26.5 44 23.5"
                "C41 16.5 33.5 14 26.5 16C19 18.5 15.5 26 17.5 34C20 42.5 30 46.5 39 43", INK, 3.6)
    return ring + at


@reg("office-calendar", RED)
def office_calendar():
    page = rrect(15, 15, 34, 32, 4.5, INK) + rrect(15, 21.5, 34, 2.4, 0, HOLE)
    rings = rrect(21, 11.5, 3.6, 7, 1.8, INK) + rrect(40.4, 11.5, 3.6, 7, 1.8, INK)
    cells = "".join(rrect(18.5 + c * 7, 27 + r * 6.5, 5, 4.5, 1, HOLE)
                    for r in range(3) for c in range(4) if (r, c) != (1, 2))
    return page + rings + cells + circle(34, 35.3, 2.8, HOLE)


@reg("okteta", BLUE_GREY_DEEP)
def okteta():
    sheet = rrect(16, 12, 26, 34, 3.5, INK)
    bits = ""
    for r in range(5):
        for c in range(3):
            if (r + c) % 2:
                bits += rrect(20.5 + c * 6.5, 16.5 + r * 5.5, 2.2, 4, 1.1, HOLE)
            else:
                bits += (f'<rect x="{f(19.8 + c * 6.5)}" y="{f(16.5 + r * 5.5)}" width="3.6" height="4" '
                         f'rx="1.5" fill="none" stroke="{HOLE}" stroke-width="1.4"/>')
    badge = circle(41, 40, 9, HOLE) + circle(41, 40, 7.5, RED)
    pencil = line(37.5, 43.5, 44, 37, INK, 3)
    return sheet + bits + badge + pencil


@reg("okular", BLUE_DEEP)
def okular():
    page = rrect(19, 12, 26, 36, 3.5, INK)
    lines = "".join(rrect(23, y, w, 2.4, 1.2, HOLE) for y, w in [(18, 18), (23, 18), (28, 14), (33, 18)])
    arc = stroke("M14.5 44C21 32 32 21 48 16", HOLE, 7) + stroke("M14.5 44C21 32 32 21 48 16", BLUE_SOFT, 3.4)
    return page + lines + arc


@reg("ollydbg", RED_DEEP)
def ollydbg():
    arms = [(-115, 15, 5), (-60, 13, 4), (-5, 17, 4.5), (60, 16, 5), (130, 15, 4.5), (185, 17, 4.5)]
    out = circle(CX, CY, 7.5, INK)
    for a, r, w in arms:
        x, y = pt(CX, CY, r, a)
        out += line(CX, CY, x, y, INK, w) + circle(x, y, w * .75, INK)
    return out


@reg("olympus", DEEP_PURPLE_DARK)
def olympus():
    mount = poly([(14.5, 44), (32, 15), (49.5, 44)], INK, 3.5)
    return mount + _gear_g(32, 35.5, 6.8, 5, 8, HOLE) + circle(32, 35.5, 2.2, INK)


@reg("omnetpp", CYAN_DARK)
def omnetpp():
    board = rrect(15, 15, 32, 32, 3, INK)
    trail = stroke("M16.5 45C27 40 35 31 43 21", HOLE, 2.6)
    ball = circle(44.5, 17.5, 7, HOLE) + circle(44.5, 17.5, 5.5, INK)
    return board + trail + ball


@reg("omnishell", BLUE_GREY)
def omnishell():
    rings = "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="none" stroke="{INK}" stroke-width="3"/>'
                    for x, y in [(21.5, 19.5), (42.5, 19.5), (21.5, 40.5), (42.5, 40.5)])
    bars = (line(26, 19.5, 26, 40.5, INK, 3) + line(38, 19.5, 38, 40.5, INK, 3) +
            line(21.5, 24, 42.5, 24, INK, 3) + line(21.5, 36, 42.5, 36, INK, 3))
    return rings + bars


@reg("onboard", BLUE)
def onboard():
    keys = (rrect(15, 13, 15, 15, 3, INK) + rrect(33, 13, 15, 15, 3, BLUE_DARK) +
            rrect(15, 31, 15, 15, 3, BLUE_DARK) + rrect(33, 31, 15, 15, 3, INK))
    o = f'<circle cx="22.5" cy="20.5" r="4" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
    b = stroke("M37.5 33.5V43.5H41.5A2.6 2.6 0 0 0 41.5 38.3H37.5M37.5 38.3H41A2.4 2.4 0 0 0 41 33.5H37.5", HOLE, 2.4)
    return keys + o + b


@reg("onionshare80", PURPLE_DARK)
def onionshare():
    return (circle(CX, CY, 16.5, INK) + _arrow_arc(CX, CY, 10, 195, 340, HOLE, 3.8, 5) +
            _arrow_arc(CX, CY, 10, 15, 160, HOLE, 3.8, 5))


@small("notepadqq")
def notepadqq_s():
    return rrect(16, 12, 32, 36, 4, INK) + rrect(16, 24, 32, 11, 0, HOLE)


@small("nsm-legacy-gui")
def nsm_legacy_s():
    return (stroke("M17 40V20L29 40V20", INK, 4.4) +
            stroke("M47 23C45.5 20.8 43.5 20 41 20C37.5 20 35.5 22 35.5 25"
                   "C35.5 31 47 29 47 35C47 38.2 44.5 40 41 40C38.5 40 36.5 39 35 37", INK, 4.4))


@small("nsm-proxy")
def nsm_proxy_s():
    return (stroke("M17 40V20H23A5.5 5.5 0 0 1 23 31H17", INK, 4.4) +
            stroke("M34.5 40V20H40.5A5.3 5.3 0 0 1 40.5 30.6H34.5M40 30.6L46 40", INK, 4.4))


@small("okteta")
def okteta_s():
    sheet = rrect(16, 12, 26, 34, 3.5, INK)
    bits = "".join(rrect(20.5 + c * 8, 17 + r * 8, 3, 5, 1.5, HOLE) for r in range(3) for c in range(2))
    return sheet + bits + circle(41, 40, 10, HOLE) + circle(41, 40, 8.5, RED)


@small("office-calendar")
def office_calendar_s():
    page = rrect(15, 15, 34, 32, 4.5, INK) + rrect(15, 21.5, 34, 3, 0, HOLE)
    cells = "".join(rrect(19 + c * 9.5, 28 + r * 8, 7, 5.5, 1.2, HOLE) for r in range(2) for c in range(3))
    return page + cells


@small("okular")
def okular_s():
    page = rrect(19, 12, 26, 36, 3.5, INK)
    lines = "".join(rrect(23, y, 18, 3.5, 1.7, HOLE) for y in (18, 25))
    arc = stroke("M14.5 44C21 32 32 21 48 16", HOLE, 8) + stroke("M14.5 44C21 32 32 21 48 16", BLUE_SOFT, 4)
    return page + lines + arc


@small("nvvp")
def nvvp_s():
    cols = [[INK, CYAN_SOFT], [INK, CYAN]]
    return "".join(rrect(15 + c * 18, 13 + r * 18, 16, 16, 3, cols[r][c]) for r in range(2) for c in range(2))


@small("nvtop")
def nvtop_s():
    box = (f'<rect x="14.5" y="12.5" width="35" height="35" rx="7" fill="none" '
           f'stroke="{INK}" stroke-width="3.4"/>')
    return box + stroke("M24.5 39V21L39.5 39V21", INK, 4)


@small("nwg-icon-picker")
def nwg_icon_picker_s():
    return rrect(15, 13, 13, 13, 3, INK) + poly([(26, 26), (48, 35.5), (39, 38.5), (35, 48)], INK, 3)


@small("ocrfeeder")
def ocrfeeder_s():
    lens = f'<circle cx="28" cy="26.5" r="10.5" fill="none" stroke="{INK}" stroke-width="5"/>'
    return lens + line(36.5, 35, 46, 44.5, INK, 7)


@small("nulloy")
def nulloy_s():
    top = path("M14 13C22 12 32 14 39 19C37.5 25 33 29.5 26.5 30.5C21 30.5 16.5 26.5 15 21Z", INK)
    bottom = path("M14 48C16 40 21 34.5 28 33C32 32.5 35.5 33.5 37.5 35.5C34 43 26.5 47 14 48Z", INK)
    return top + bottom + circle(44, 18, 5, INK) + path("M39 37C41 31 45 28 50 27C49.5 33 45.5 37 39 37Z", INK)


@small("ocenaudio")
def ocenaudio_s():
    band = stroke("M17 33V29A15 15 0 0 1 47 29V33", INK, 3.6)
    cups = rrect(13, 27, 8, 15, 3.5, INK) + rrect(43, 27, 8, 15, 3.5, INK)
    head = path("M32 16C39.5 16 43 22.5 43 31C43 40 38 47 32 47C26 47 21 40 21 31C21 22.5 24.5 16 32 16Z", INK)
    mouth = path("M25 32C29.5 30.5 34.5 30.5 39 32C38.5 39.5 35.5 43 32 43C28.5 43 25.5 39.5 25 32Z", HOLE)
    return band + cups + head + mouth


@small("odio")
def odio_s():
    return "".join(line(17 + 7.5 * i, CY - h / 2, 17 + 7.5 * i, CY + h / 2, INK, 3.6)
                   for i, h in enumerate([10, 20, 28, 20, 10]))


@small("nuclear")
def nuclear_s():
    return (poly([(14.5, 16), (30, 16), (22.25, 29.5)], INK, 2) +
            poly([(34, 16), (49.5, 16), (41.75, 29.5)], INK, 2) +
            poly([(24.25, 33), (39.75, 33), (32, 46.5)], INK, 2))


@small("omnishell")
def omnishell_s():
    rings = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
                    for x, y in [(20, 18), (44, 18), (20, 42), (44, 42)])
    bars = (line(25, 18, 25, 42, INK, 2.6) + line(39, 18, 39, 42, INK, 2.6) +
            line(20, 23, 44, 23, INK, 2.6) + line(20, 37, 44, 37, INK, 2.6))
    return rings + bars


@small("onionshare80")
def onionshare_s():
    return (circle(CX, CY, 17, INK) + _arrow_arc(CX, CY, 9.5, 200, 330, HOLE, 3.4, 6) +
            _arrow_arc(CX, CY, 9.5, 20, 150, HOLE, 3.4, 6))
