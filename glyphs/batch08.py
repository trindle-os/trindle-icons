# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 8: ark-game to autoremesher.

Same rules as batch01: tile from the palette step nearest the brand
colour, mark in INK, HOLE for cut-throughs, any second shade another
palette step.
"""
import math
from lm import *
from glyphs.kit import badge_b, ellipse_b, registry, _ring

ICONS, SMALL, reg, small = registry()

@reg("ark-game", BLUE_GREY_DEEP)
def ark_game():
    a = stroke("M17 45L32 15L47 45", INK, 6.5)
    return a + rrect(27, 32, 5.5, 13, 1.5, INK) + poly([(28.5, 21), (35.5, 21), (32, 15)], BLUE_LIGHT, 3)

@reg("armagetronad", AMBER_DEEP)
def armagetronad():
    out = _ring(CX, CY, 15, INK, 3.2)
    for k in range(6):
        a = 60 * k
        x0, y0 = pt(CX, CY, 5, a)
        cx_, cy_ = pt(CX, CY, 11, a + 25)
        x1, y1 = pt(CX, CY, 14, a + 70)
        out += stroke(f"M{f(x0)} {f(y0)}Q{f(cx_)} {f(cy_)} {f(x1)} {f(y1)}", INK, 3.2)
    return out + circle(CX, CY, 4.5, INK)

@reg("armello", AMBER_DARK)
def armello():
    pts = []
    for k in range(10):
        a = -115 + 29 * k
        pts += [pt(35, 29.5, 17, a + 9), pt(35, 29.5, 11.5, a + 20)]
    mane = poly(pts, INK, 1.5)
    face = path("M31 14L24 16.5L19 21L16 25L13 27.5L14.5 30.5L18 30.5L16.5 33.5L20.5 35.5"
                "L21 39.5L26 40.5L29 45L33 44C29.5 38 28.5 26 31 14Z", INK,
                f' stroke="{HOLE}" stroke-width="2.2" stroke-linejoin="round"')
    eye = poly([(21, 24), (27, 22.5), (25.5, 26)], HOLE, 1)
    return mane + face + eye

@reg("armitage", CYAN_DEEP)
def armitage():
    hair = path("M17 45V29C17 19 23.5 13.5 32 13.5C40.5 13.5 47 19 47 29V45"
                "L43.5 41L41 45H23L20.5 41Z", INK)
    face = path("M22 30Q27 30 29 25Q33 30 36 25Q37 30 42 30V35"
                "C42 40.5 37.5 44 32 44C26.5 44 22 40.5 22 35Z", DEEP_ORANGE_SOFT)
    smile = stroke("M28 36.5Q32 40 36 36.5", INK, 2.4)
    ears = (g(rrect(12.5, 10.5, 9, 9, 2.5, INK), "rotate(-12 17 15)") +
            g(rrect(42.5, 10.5, 9, 9, 2.5, INK), "rotate(12 47 15)") +
            circle(17, 15, 2.2, AMBER_DARK) + circle(47, 15, 2.2, AMBER_DARK))
    return hair + face + smile + ears

@reg("assaultcube", RED_DEEP)
def assaultcube():
    r = [16.5, 12, 15, 11.5, 17, 12.5, 15.5, 11, 16, 12, 15, 11.5]
    splat = poly([pt(CX, CY, r[k], -90 + 30 * k) for k in range(12)], INK, 3)
    hexa = [pt(CX, CY, 9.5, -90 + 60 * k) for k in range(6)]
    cube = poly(hexa, HOLE, 1.5)
    top = poly([hexa[0], hexa[1], (CX, CY), hexa[5]], RED_SOFT, 1.5)
    return splat + cube + top

@reg("astromenace", INDIGO_DEEP)
def astromenace():
    body = path("M15 22C20 18 26 19 29.5 24C33 17 40 14.5 47 16.5C42.5 18.5 40 21 39 24"
                "C44.5 26.5 48 32 48.5 40C44.5 34.5 40.5 32 36 32C32.5 35 30 39 29.5 45"
                "C26 38 19.5 31.5 15 22Z", INK)
    eye = g(f'<ellipse cx="33" cy="28" rx="2.2" ry="4" fill="{HOLE}"/>', "rotate(35 33 28)")
    return body + eye

@reg("atari-vault", PURPLE)
def atari_vault():
    side = path("M23.5 13H27.5V28C27.5 37 23 43.5 15.5 47H13.5C19.5 41.5 23.5 35 23.5 26Z", INK)
    return (rrect(29.8, 13, 4.4, 34, 1, INK) + side +
            g(side, "translate(64 0) scale(-1 1)"))

@reg("atlauncher", GREY_DARK)
def atlauncher():
    hexa = [pt(CX, CY, 17, -90 + 60 * k) for k in range(6)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexa) + "Z"
    letters = (stroke("M20.5 38V26.5Q20.5 23.5 23.5 23.5H25.5Q28.5 23.5 28.5 26.5V38M20.5 31H28.5",
                      GREY_SOFT, 3.2) +
               stroke("M32.5 23.5H43.5M38 23.5V38", GREY_SOFT, 3.2))
    return stroke(d, INK, 3.4) + letters

@reg("atom-rpg", BROWN)
def atom_rpg():
    swoosh = cut("M16 30a16 8 0 1 0 32 0a16 8 0 1 0 -32 0Z"
                 "M20 31.5a12.5 5 0 1 0 25 0a12.5 5 0 1 0 -25 0Z", INK)
    return (g(swoosh, "rotate(40 32 30)") + g(swoosh, "rotate(-40 32 30) scale(-1 1) translate(-64 0)")
            + circle(CX, CY, 3.6, INK))

@reg("audiosurf", BLUE_GREY)
def audiosurf():
    ship = poly([(32, 11), (35.5, 21), (40, 24), (47.5, 31), (47.5, 37), (16.5, 37), (16.5, 31),
                 (24, 24), (28.5, 21)], INK, 2.5)
    fin = stroke("M30 20V29M34 20V29", HOLE, 2)
    base = rrect(18, 35, 28, 11, 5.5, INK)
    pods = circle(24.5, 40.5, 2.6, HOLE) + circle(32, 40.5, 2.6, HOLE) + circle(39.5, 40.5, 2.6, HOLE)
    return ship + fin + base + pods

@reg("audiosurf-2", PURPLE_DEEP)
def audiosurf_2():
    tower = rrect(26.5, 12, 11, 14, 2.5, INK) + rrect(30.5, 14.5, 3, 8, 1.5, HOLE)
    body = poly([(19, 25), (45, 25), (48.5, 37), (15.5, 37)], INK, 3)
    wheels = ""
    for x, r in [(20, 5), (44, 5), (32, 6)]:
        wheels += circle(x, 41.5, r + 1.6, HOLE) + circle(x, 41.5, r, INK) + circle(x, 41.5, r * .42, HOLE)
    return tower + body + wheels

def _speaker():
    return (circle(CX, CY, 16, INK) + circle(CX, CY, 12.5, HOLE) +
            circle(CX, CY, 9.5, INK) + circle(CX, CY, 4, HOLE))

@reg("arts", GREY_DEEP)
def arts():
    return _speaker()

@reg("artsbuilder", GREY_DEEP)
def artsbuilder():
    wrench = (line(41.5, 40, 41.5, 46, INK, 3.2) + circle(41.5, 38, 4, INK) +
              rrect(40, 32.5, 3, 5, 1, TEAL))
    return (g(_speaker(), "translate(29 27) scale(.85) translate(-32 -30)") +
            badge_b(41.5, 40, TEAL) + wrench)

@reg("artscontrol", GREY_DEEP)
def artscontrol():
    teeth = "".join(g(rrect(40.2, 33.5, 2.6, 13, 1, INK), f"rotate({45 * k} 41.5 40)") for k in range(4))
    gear = teeth + circle(41.5, 40, 4.6, INK) + circle(41.5, 40, 2, PURPLE_LIGHT)
    return (g(_speaker(), "translate(29 27) scale(.85) translate(-32 -30)") +
            badge_b(41.5, 40, PURPLE_LIGHT) + gear)

@reg("asunder", GREY_DEEP)
def asunder():
    disc = circle(CX, CY, 16.5, INK) + circle(CX, CY, 8.5, HOLE) + circle(CX, CY, 6.5, INK) + circle(CX, CY, 3, HOLE)
    crack = stroke("M34.5 13L29.5 19.5L34.5 21.5L31 27", HOLE, 2.4)
    return disc + crack

@reg("atunes", BLUE)
def atunes():
    head = g(f'<ellipse cx="26" cy="39.5" rx="7" ry="5.8" fill="{INK}"/>', "rotate(-20 26 39.5)")
    stem = rrect(29.5, 13, 4, 27, 2, INK)
    flag = path("M31 13C35 18 42.5 19 43.5 27C43.8 29.5 42.5 30.5 41.2 30.5C40 25.5 36 23.5 31 23.5Z", INK)
    return head + stem + flag

@reg("audacious", BLUE_GREY_DEEP)
def audacious():
    hook = stroke("M23.5 22C25.5 19.5 28.5 18.5 31.5 18.5C36.5 18.5 39.5 21.5 39.5 26.5V42", INK, 5.5)
    bowl = (f'<ellipse cx="30.5" cy="35" rx="8.5" ry="7" fill="{INK}"/>' +
            f'<ellipse cx="31" cy="35" rx="3.5" ry="2.8" fill="{HOLE}"/>')
    return hook + bowl

@reg("audacium", DEEP_PURPLE)
def audacium():
    bands = (stroke("M15 42L49 20", DEEP_PURPLE_LIGHT, 5) + stroke("M16 34L42 15", DEEP_PURPLE_SOFT, 5))
    return bands + stroke("M20 44L32 16L44 44", INK, 5.5)

@reg("audience", RED_DEEP)
def audience():
    play = poly([(25, 15), (42, 26), (25, 37)], INK, 3.5)
    track = line(15.5, 44, 38, 44, INK, 2.8) + line(38, 44, 48.5, 44, RED_SOFT, 2.8)
    return play + track + circle(38, 44, 4, INK)

@reg("audio-recorder", INDIGO)
def audio_recorder():
    cap = rrect(25, 12, 14, 23, 7, INK)
    holder = stroke("M19 28A13 13 0 0 0 45 28", INK, 3.4)
    return cap + holder + line(32, 41, 32, 46, INK, 3.4) + line(24.5, 47, 39.5, 47, INK, 3.4)

@reg("audiobook", TEAL_DEEP)
def audiobook():
    book = rrect(16, 12, 26, 35, 3, INK) + line(21, 12, 21, 47, HOLE, 2)
    mark = poly([(33, 12), (38, 12), (38, 21), (35.5, 19), (33, 21)], HOLE, 1)
    spk = (poly([(36.5, 37.5), (39, 37.5), (42.5, 34.5), (42.5, 45.5), (39, 42.5), (36.5, 42.5)], INK, 1) +
           stroke("M45 37A4 4 0 0 1 45 43", INK, 2))
    return book + mark + badge_b(41, 40, RED) + spk

@reg("auryo", BLUE_DEEP)
def auryo():
    band = stroke("M19 36V30A13 13 0 0 1 45 30V36", INK, 4)
    return band + _ring(19, 40.5, 4.5, INK, 3.4) + _ring(45, 40.5, 4.5, INK, 3.4)

@reg("around", DEEP_ORANGE)
def around():
    lens = path("M32 21.52A11 11 0 0 1 32 38.48A11 11 0 0 1 32 21.52Z", DEEP_ORANGE_DARK)
    return circle(25, 30, 11, INK) + circle(39, 30, 11, INK) + lens

@reg("artikulate", LIGHT_BLUE_DEEP)
def artikulate():
    bubble = rrect(15, 12.5, 34, 29, 6, INK) + poly([(35, 40), (44, 40), (42.5, 47.5)], INK, 2)
    globe = circle(32, 27, 10, HOLE)
    lines = (ellipse_b(32, 27, 4.2, 10, INK, 2.2) + line(22, 27, 42, 27, INK, 2.2, "butt"))
    return bubble + globe + lines

@reg("asbru-cm", BLUE_DARK)
def asbru_cm():
    frame = rrect(15, 13, 34, 34, 5, INK) + rrect(20, 18, 24, 24, 3, DEEP_ORANGE_LIGHT)
    bub = stroke("M25 23H39V34H33L30 37.5V34H25Z", INK, 2.6)
    return frame + bub

@reg("asc-de", BLUE_DEEP)
def asc_de():
    out = ""
    for y in (38, 30, 22):
        d = f"M32 {y - 8}L48 {y}L32 {y + 8}L16 {y}Z"
        out += path(d, INK, f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"')
    return out

@reg("asciidocfx", RED)
def asciidocfx():
    tri = poly([(32, 13), (48, 45), (16, 45)], INK, 4)
    return tri + poly([(32, 28), (37, 39), (27, 39)], HOLE, 1.5)

@reg("asciiportal", ORANGE_DEEP)
def asciiportal():
    u, rows = 4, []
    for r in range(8):
        yc = 14 + r * u + u / 2
        cells = [c for c in range(8) if math.hypot(16 + c * u + u / 2 - CX, yc - CY) <= 16.5]
        rows.append((16 + cells[0] * u, 16 + (cells[-1] + 1) * u))
    d = f"M{rows[0][1]} 14"
    for r, (x0, x1) in enumerate(rows):
        d += f"H{x1}V{14 + (r + 1) * u}"
    for r in range(7, -1, -1):
        d += f"H{rows[r][0]}V{14 + r * u}"
    out = path(d + "Z", INK)
    v = [pt(CX, CY, 6, -90 + 60 * k) for k in range(7)]
    out += poly(v[:6], HOLE)
    for k in range(6):
        (x0, y0), (x1, y1) = v[k + 1], v[k]
        dd = math.hypot(x1 - x0, y1 - y0)
        out += line(x1, y1, x1 + (x1 - x0) / dd * 8, y1 + (y1 - y0) / dd * 8, HOLE, 2.4, "square")
    return out

@reg("aseprite", PURPLE_DEEP)
def aseprite():
    body = rrect(16, 13, 32, 32, 7, INK)
    chin = path("M16 36H48V38A7 7 0 0 1 41 45H23A7 7 0 0 1 16 38Z", PURPLE_SOFT)
    eyes = rrect(24, 20, 4.5, 11, 2.25, HOLE) + rrect(35.5, 20, 4.5, 11, 2.25, HOLE)
    return body + chin + eyes

def _aspia():
    back = rrect(26, 13.5, 23, 18, 3, INK)
    front = rrect(15, 23.5, 26, 21, 3, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    prompt = stroke("M20 30L23.5 33L20 36", HOLE, 2.4) + line(26, 37.5, 31, 37.5, HOLE, 2.4)
    return back + front + prompt

@reg("aspia_client", BLUE_DEEP)
def aspia_client():
    return _aspia()

@reg("aspia_console", BLUE_GREY_DEEP)
def aspia_console():
    return _aspia()

def _astah():
    hook = stroke("M21 23.5C22.5 21 25 20 28 20C31.5 20 34 22 34 26V41.5", INK, 4.2)
    bowl = f'<ellipse cx="27" cy="35" rx="6.3" ry="5.6" fill="none" stroke="{INK}" stroke-width="4.2"/>'
    slash = line(38.5, 20, 48.5, 32.5, INK, 4.2) + line(26, 11.5, 27, 15.5, INK, 3)
    return hook + bowl + slash

for _n, _t in [("astah_community", AMBER_DEEP), ("astah_gsn", INDIGO_LIGHT),
               ("astah_professional", PINK_LIGHT), ("astah_sysml", PURPLE_LIGHT),
               ("astah_uml", BLUE), ("astah_viewer", LIGHT_BLUE_DEEP)]:
    reg(_n, _t)(_astah)

@reg("athens", GREY_SOFT)
def athens():
    br = stroke("M17.5 17H13.5V43H17.5", INK, 2.6) + stroke("M22.5 17H19.5V43H22.5", INK, 2.6)
    a = stroke("M27.5 42L32 19L36.5 42", INK, 3) + line(29, 35, 35, 35, INK, 2.6)
    return br + g(br, "translate(64 0) scale(-1 1)") + a

def _board():
    out = rrect(15, 13, 34, 34, 4, INK)
    for x in (22, 42):
        out += line(x, 13, x, 47, HOLE, 2, "butt")
    for y in (20, 40):
        out += line(15, y, 49, y, HOLE, 2, "butt")
    for v in (27, 32, 37):
        out += line(v, 13, v, 20, HOLE, 2, "butt") + line(v, 40, v, 47, HOLE, 2, "butt")
        out += line(15, v - 2, 22, v - 2, HOLE, 2, "butt") + line(42, v - 2, 49, v - 2, HOLE, 2, "butt")
    return out

@reg("atlantik", BLUE_DEEP)
def atlantik():
    return _board()

@reg("atlantikdesigner", LIGHT_BLUE_DEEP)
def atlantikdesigner():
    pencil = line(37.5, 44.5, 45.5, 36.5, INK, 3.6) + poly([(35.5, 46.5), (36.5, 42.5), (39.5, 45.5)], INK, 1)
    return (g(_board(), "translate(28.5 26.5) scale(.85) translate(-32 -30)") +
            badge_b(41.5, 40.5, ORANGE_DEEP) + pencil)

def _atom(stars=False):
    out = "".join(ellipse_b(CX, CY, 16, 6.2, INK, 2.6, a) for a in (0, 60, 120))
    out += circle(CX, CY, 3.4, INK)
    if stars:
        for x, y, r in [(46.5, 15.5, 3.2), (17, 45, 2.6), (48, 43.5, 2.2)]:
            out += poly([(x, y - r), (x + r * .3, y - r * .3), (x + r, y), (x + r * .3, y + r * .3),
                         (x, y + r), (x - r * .3, y + r * .3), (x - r, y), (x - r * .3, y - r * .3)], INK, .8)
    return out

@reg("atom", PURPLE_SOFT)
def atom():
    return _atom()

@reg("atom-beta", AMBER_DEEP)
def atom_beta():
    return _atom()

@reg("atom-nightly", PURPLE_DEEP)
def atom_nightly():
    return _atom(True)

@reg("atomic", BLUE_DEEP)
def atomic():
    return stroke("M20 44L29.5 18.5Q32 13 34.5 18.5L44 44", INK, 5.5) + circle(32, 35.5, 3.2, INK)

@reg("au.edu.uq.esys.escript", BLUE_DEEP)
def escript():
    pts = [(16, 24), (22, 17), (30, 19.5), (36, 14), (44, 18), (48.5, 27), (45, 37),
           (38, 44.5), (29, 41.5), (20, 45), (15, 36)]
    blob = poly(pts, INK, 3)
    mesh = stroke("M22 17L26 31L30 19.5L38 27L44 18M26 31L38 27L45 37M26 31L29 41.5L38 27M15 36L26 31L16 24",
                  HOLE, 1.8)
    return blob + mesh

@reg("augur", DEEP_PURPLE_DEEP)
def augur():
    tri = stroke("M32 13L48.5 43H15.5Z", INK, 2.8)
    c = (32, 33)
    spokes = (line(32, 13, 32, 28, INK, 2.6) + line(15.5, 43, 28, 35.5, INK, 2.6) +
              line(48.5, 43, 36, 35.5, INK, 2.6))
    return tri + spokes + _ring(c[0], c[1], 4.6, INK, 2.6)

@reg("aurees", PURPLE_LIGHT)
def aurees():
    arcs = ""
    for a in (-90, 30, 150):
        x0, y0 = pt(CX, CY, 14.5, a + 10)
        x1, y1 = pt(CX, CY, 14.5, a + 110)
        arcs += stroke(f"M{f(x0)} {f(y0)}A14.5 14.5 0 0 1 {f(x1)} {f(y1)}", INK, 4.6)
    return arcs + circle(CX, CY + .5, 4.6, INK)

@reg("authpass", INDIGO)
def authpass():
    head = poly([(14.5, 18), (27, 18), (34, 26), (34, 36), (14.5, 36)], INK, 3)
    shaft = rrect(30, 26.5, 20, 7, 2, INK)
    teeth = rrect(40, 31, 4, 9, 1.2, INK) + rrect(46, 31, 4, 6.5, 1.2, INK)
    return head + shaft + teeth + circle(22, 27, 3.2, HOLE)

@reg("authy", RED)
def authy():
    links = (rrect(15, 24.5, 20, 11, 5.5, "none", f' stroke="{INK}" stroke-width="4"') +
             rrect(29, 24.5, 20, 11, 5.5, "none", f' stroke="{INK}" stroke-width="4"'))
    return g(links, "rotate(-45 32 30)")

@reg("autoremesher", BLUE_GREY_DEEP)
def autoremesher():
    head = path("M14.5 31C14.5 27.5 17 25.5 21 25.5C25.5 25 29 22.5 33 21.5L37 16.5L39.5 19.5"
                "L42.5 15.5L44.5 21.5C45.5 26 47.5 30.5 50 34.5V45L43.5 47L37.5 36"
                "C32.5 36.5 26 37.5 21 37.5C17 37.5 14.5 35 14.5 31Z", INK)
    return head + circle(37.5, 25, 1.8, HOLE) + circle(17.5, 30, 1.2, HOLE)

def _atom_s():
    return "".join(ellipse_b(CX, CY, 16, 6.5, INK, 3, a) for a in (0, 60, 120)) + circle(CX, CY, 4, INK)

for _n in ("atom", "atom-beta", "atom-nightly"):
    small(_n)(_atom_s)

def _board_s():
    out = rrect(15, 13, 34, 34, 4, INK)
    for v in (23.5, 40.5):
        out += line(v, 13, v, 47, HOLE, 3, "butt") + line(15, v - 2, 49, v - 2, HOLE, 3, "butt")
    return out

@small("atlantik")
def atlantik_s():
    return _board_s()

@small("atlantikdesigner")
def atlantikdesigner_s():
    return (g(_board_s(), "translate(28.5 26.5) scale(.85) translate(-32 -30)") +
            badge_b(41.5, 40.5, ORANGE_DEEP) + line(37.5, 44.5, 45.5, 36.5, INK, 3.6))

@small("athens")
def athens_s():
    br = stroke("M20 16H15V44H20", INK, 3.2)
    a = stroke("M24.5 43L32 17L39.5 43", INK, 4) + line(27.5, 35, 36.5, 35, INK, 3.4)
    return br + g(br, "translate(64 0) scale(-1 1)") + a

@small("asunder")
def asunder_s():
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 5, HOLE) +
            stroke("M35 12L29 20L35 22.5L31 27", HOLE, 3))

def _aspia_s():
    back = rrect(27, 13, 22, 18, 3, INK)
    front = rrect(14, 23, 27, 22, 3, INK, f' stroke="{HOLE}" stroke-width="3"')
    return back + front + stroke("M20 29.5L24.5 34L20 38.5", HOLE, 3.2)

small("aspia_client")(_aspia_s)
small("aspia_console")(_aspia_s)

@small("au.edu.uq.esys.escript")
def escript_s():
    pts = [(16, 24), (22, 17), (30, 19.5), (36, 14), (44, 18), (48.5, 27), (45, 37),
           (38, 44.5), (29, 41.5), (20, 45), (15, 36)]
    return poly(pts, INK, 3) + stroke("M22 17L28 33L44 18M15 36L28 33L38 44.5", HOLE, 2.4)

@small("augur")
def augur_s():
    return stroke("M32 12L49 43H15Z", INK, 3.2) + circle(32, 33, 4.5, INK)

@small("audiobook")
def audiobook_s():
    book = rrect(16, 12, 26, 35, 3, INK) + line(21.5, 12, 21.5, 47, HOLE, 2.6)
    return book + badge_b(41, 40, RED) + poly([(36.5, 37), (40, 37), (44, 33.5), (44, 46.5), (40, 43), (36.5, 43)], INK, 1)

@small("armagetronad")
def armagetronad_s():
    out = _ring(CX, CY, 15, INK, 3.4)
    for k in range(4):
        a = 90 * k
        x0, y0 = pt(CX, CY, 5, a)
        cx_, cy_ = pt(CX, CY, 11, a + 30)
        x1, y1 = pt(CX, CY, 14, a + 80)
        out += stroke(f"M{f(x0)} {f(y0)}Q{f(cx_)} {f(cy_)} {f(x1)} {f(y1)}", INK, 3.6)
    return out + circle(CX, CY, 5, INK)

@small("asciiportal")
def asciiportal_s():
    return circle(CX, CY, 16.5, INK) + poly([pt(CX, CY, 7.5, -90 + 60 * k) for k in range(6)], HOLE)

@small("atom-rpg")
def atom_rpg_s():
    return ellipse_b(CX, CY, 15, 6.5, INK, 3.4, 40) + ellipse_b(CX, CY, 15, 6.5, INK, 3.4, -40) + circle(CX, CY, 4, INK)

@small("atlauncher")
def atlauncher_s():
    hexa = [pt(CX, CY, 17, -90 + 60 * k) for k in range(6)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexa) + "Z"
    return stroke(d, INK, 3.6) + stroke("M25 38V25H39V38M25 31.5H39", BLUE_SOFT, 3.6)

def _speaker_s():
    return circle(CX, CY, 16, INK) + circle(CX, CY, 10, HOLE) + circle(CX, CY, 5.5, INK)

small("arts")(_speaker_s)

@small("artsbuilder")
def artsbuilder_s():
    return (g(_speaker_s(), "translate(28 26) scale(.85) translate(-32 -30)") +
            circle(41.5, 40.5, 12, HOLE) + circle(41.5, 40.5, 10.5, TEAL) +
            line(41.5, 38, 41.5, 47, INK, 3.4) + circle(41.5, 37.5, 4.2, INK))

@small("artscontrol")
def artscontrol_s():
    return (g(_speaker_s(), "translate(28 26) scale(.85) translate(-32 -30)") +
            circle(41.5, 40.5, 12, HOLE) + circle(41.5, 40.5, 10.5, PURPLE_LIGHT) + circle(41.5, 40.5, 5, INK))

@small("audiosurf-2")
def audiosurf_2_s():
    tower = rrect(26, 11, 12, 14, 2.5, INK)
    body = poly([(18, 24), (46, 24), (49, 38), (15, 38)], INK, 3)
    return tower + body + circle(22, 42, 6, INK) + circle(42, 42, 6, INK)
