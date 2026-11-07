# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 12: calibre to chromium, drawn to match batch 1.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
import math
from lm import *
from glyphs.kit import _chrome_b, _gear_b, registry, _ring, _star_c

ICONS, SMALL, reg, small = registry()

def _sc(content, k, ox=32, oy=30):
    """Scale content drawn round (ox, oy) by k and centre it on (32, 30)."""
    return g(content, f"translate(32 30) scale({k}) translate({-ox} {-oy})")

def _badge(cx, cy, r, fill):
    """Round badge with a tile-coloured gap separating it from the mark."""
    return circle(cx, cy, r + 2.2, HOLE) + circle(cx, cy, r, fill)

def _book():
    cover = rrect(16, 12, 26, 34, 4, INK)
    spine = rrect(16, 12, 6, 34, 3, TEAL_SOFT)
    ribbon = poly([(31.5, 12), (36.5, 12), (36.5, 23), (34, 20.5), (31.5, 23)], HOLE, 1)
    return cover + spine + ribbon

@reg("calibre-ebook-edit", TEAL_DEEP)
def calibre_edit():
    badge = _badge(41.5, 39.5, 9.5, DEEP_PURPLE)
    return _book() + badge + _gear_b(41.5, 39.5, 4.6, INK, DEEP_PURPLE)

@reg("calibre-viewer", TEAL_DEEP)
def calibre_viewer():
    badge = _badge(41.5, 39.5, 9.5, RED_DEEP)
    eye = path("M34.5 39.5Q41.5 32.5 48.5 39.5Q41.5 46.5 34.5 39.5Z", INK) + circle(41.5, 39.5, 2.4, RED_DEEP)
    return _book() + badge + eye

@reg("call-of-duty", YELLOW_DARK)
def call_of_duty():
    return _star_c()

@reg("call-of-duty-2", YELLOW_DARK)
def call_of_duty_2():
    badge = _badge(42, 40, 9.5, DEEP_ORANGE_DEEP)
    two = stroke("M38.6 37A3.6 3.6 0 1 1 44.6 39.6L38.5 45H45.5", INK, 2.8)
    return _star_c(30, 29, 17) + badge + two

@reg("cantata", BLUE_DEEP)
def cantata():
    note = (circle(28.5, 36.5, 4.6, HOLE) + line(32.4, 36, 32.4, 19.5, HOLE, 3) +
            stroke("M32.4 19.5C35 22 40 22.5 39.5 28", HOLE, 3))
    return circle(CX, CY, 16.5, INK) + note

@reg("carla", RED_DEEP)
def carla():
    out = ""
    for y0 in (12.5, 31):
        out += rrect(15, y0, 34, 16.5, 3.5, INK) + circle(22.5, y0 + 8.25, 4.6, HOLE)
        for i, w in enumerate([8, 6, 10.5]):
            out += rrect(31, y0 + 3 + i * 4, w, 2.6, 1.3, HOLE)
    return out

@reg("carla-control", GREY_DARK)
def carla_control():
    return carla()

def _curves():
    c = (stroke("M22 17C33 17 31 31 42 31", INK, 3) +
         stroke("M22 30C33 30 31 44 42 44", INK, 3))
    ends = "".join(rrect(x - 4, y - 2.3, 8, 4.6, 2.3, INK)
                   for x, y in [(19, 17), (19, 30), (45, 31), (45, 44)])
    return c + ends

@reg("catia", RED_DARK)
def catia():
    return _curves()

@reg("catarina", RED_DARK)
def catarina():
    badge = _badge(42, 40, 9.5, INK)
    q = stroke("M38.7 37.3A3.4 3.4 0 1 1 43.3 40.4C42.3 40.9 42 41.5 42 42.5", HOLE, 2.6)
    return _sc(_curves(), .95, 30, 30) + badge + q + circle(42, 46, 1.6, HOLE)

@reg("cantor", BLUE_GREY_DEEP)
def cantor():
    rad = stroke("M15.5 29L19 27.5L23 36.5L28 17.5H48", INK, 3.2)
    a = _ring(38, 29.5, 4.4, INK, 3.2) + line(42.4, 24, 42.4, 34, INK, 3.2)
    return rad + a + rrect(16, 40.5, 32, 3.6, 1.8, INK)

@reg("ch.x29a.playitslowly", PINK_DEEP)
def playitslowly():
    foot = rrect(14, 41, 34, 5, 2.5, INK)
    neck = rrect(41, 24, 7, 22, 3.5, INK)
    horns = (line(43, 25, 41.5, 16.5, INK, 2.4) + line(46.5, 25, 49, 17, INK, 2.4) +
             circle(41.5, 16.5, 2, INK) + circle(49, 17, 2, INK))
    shell = circle(27, 29.5, 14.8, HOLE) + circle(27, 29.5, 13, INK)
    spiral = stroke("M27 29.5A2.5 2.5 0 0 1 32 29.5A4 4 0 0 1 24 29.5"
                    "A5.5 5.5 0 0 1 35 29.5A7 7 0 0 1 21 29.5", HOLE, 2.2)
    return foot + neck + horns + shell + spiral

@reg("caption", BLUE)
def caption():
    c = stroke("M38.3 23.7A8.9 8.9 0 1 0 38.3 36.3", INK, 5.5)
    return _ring(CX, CY, 15.5, INK, 3) + c + circle(33, 30, 2.6, INK)

@reg("cardo", PURPLE_DEEP)
def cardo():
    pts = [(16, 32), (15, 22), (20.5, 27), (21.5, 16), (26, 24), (28, 13.5), (32, 22.5),
           (36, 13.5), (38, 24), (42.5, 16), (43.5, 27), (49, 22), (48, 32)]
    bowl = path("M16 30H48C48 40 41 46 32 46C23 46 16 40 16 30Z", INK)
    return poly(pts, INK, 2.5) + bowl

@reg("castle-crashers", RED_DEEP)
def castle_crashers():
    helm = path("M17 16Q17 12 21 12H27L32 17L37 12H43Q47 12 47 16V37L32 48L17 37Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    cross = rrect(17, 24, 30, 10, 2, HOLE) + rrect(29, 20, 6, 29, 2, HOLE)
    eyes = (path("M19.5 26L28 29V31.5H19.5Z", INK) + path("M44.5 26L36 29V31.5H44.5Z", INK))
    return helm + cross + eyes

@reg("cataclysm-dda", INDIGO)
def cataclysm():
    z = stroke("M20 17H43L21 42H44", INK, 5.5)
    drips = (rrect(25, 17, 3, 7.5, 1.5, INK) + circle(26.5, 26.5, 1.8, INK) +
             rrect(35, 17, 3, 5, 1.5, INK) + rrect(27, 42, 3, 5.5, 1.5, INK) +
             rrect(38, 42, 3, 4, 1.5, INK) + circle(39.5, 48.3, 1.6, INK))
    return z + drips

@reg("catfish", BROWN_LIGHT)
def catfish():
    head = path("M15.5 23L17 13L25.5 19.5H38.5L47 13L48.5 23C50 35 42 46 32 46"
                "C22 46 14 35 15.5 23Z", INK)
    hat = g(rrect(26, 18, 27, 4, 2, BROWN_DARK) +
            path("M31 19C31 12.5 33.5 10.5 39.5 10.5C45.5 10.5 48 12.5 48 19Z", BROWN_DARK),
            "rotate(10 39.5 18)")
    eyes = (path("M21 30Q25 26 29 30Q25 33.5 21 30Z", HOLE) +
            path("M35 30Q39 26 43 30Q39 33.5 35 30Z", HOLE))
    mono = _ring(25, 30, 6, BLUE_DEEP, 2.4)
    nose = poly([(29.5, 36), (34.5, 36), (32, 39)], HOLE, 1.5)
    tache = stroke("M25 42Q28.5 38.5 32 41Q35.5 38.5 39 42", HOLE, 2.4)
    return head + hat + eyes + mono + nose + tache

@reg("cats-are-liquid", LIGHT_BLUE_LIGHT)
def cats_are_liquid():
    eyes = stroke("M17.5 27L23.5 21L29.5 27", INK, 4) + stroke("M34.5 27L40.5 21L46.5 27", INK, 4)
    mouth = stroke("M18 36Q25 42.5 32 36Q39 42.5 46 36", INK, 3.8)
    return eyes + mouth

@reg("cave-story", INDIGO_DEEP)
def cave_story():
    face = rrect(17, 21, 29, 24, 8, INK)
    eyes = rrect(23.5, 28, 4, 9, 2, HOLE) + rrect(35.5, 28, 4, 9, 2, HOLE)
    cap = (path("M18 25C18 16.5 24 13 32 13C40 13 45 16 45.5 21.5H50.5V25.5H18Z", RED) +
           circle(24, 18.5, 1.8, INK) + circle(38, 18.5, 1.8, INK))
    return face + eyes + cap

@reg("caveexpress-icon", BROWN)
def caveexpress():
    roof = poly([(14, 20.5), (24, 14), (32, 17), (40, 14), (50, 20.5), (32, 23)], LIGHT_BLUE_SOFT, 3)
    posts = rrect(20, 22, 4.5, 21, 2, INK) + rrect(39.5, 22, 4.5, 21, 2, INK)
    beam = rrect(16, 21.5, 32, 5, 2.5, INK)
    crate = rrect(27, 29, 10, 10, 1.5, ORANGE_SOFT)
    base = rrect(16, 40, 32, 5, 2.5, INK)
    return posts + beam + crate + base + roof

def _bone(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    px, py = -dy / n * 2, dx / n * 2
    out = line(x1, y1, x2, y2, INK, 3.6, "butt")
    for x, y in [(x1, y1), (x2, y2)]:
        out += circle(x + px, y + py, 2.5, INK) + circle(x - px, y - py, 2.5, INK)
    return out

@reg("cavepacker-icon", BROWN)
def cavepacker():
    frame = (_bone(18, 14.5, 46, 14.5) + _bone(18, 45.5, 46, 45.5) +
             _bone(16.5, 16, 16.5, 44) + _bone(47.5, 16, 47.5, 44))
    crate = rrect(22.5, 20, 19, 20, 1.5, INK)
    planks = line(23, 26.7, 41, 26.7, HOLE, 2) + line(23, 33.3, 41, 33.3, HOLE, 2)
    return frame + crate + planks

@reg("cawbird", PURPLE_DARK)
def cawbird():
    head = circle(32, 28, 16, PURPLE)
    eyes = (circle(25, 25, 6, INK) + circle(39, 25, 6, INK) +
            circle(26.8, 26, 3, PURPLE_DARK) + circle(40.8, 26, 3, PURPLE_DARK))
    beak = path("M27.5 32H36.5C36.5 39 34 44 32 49C30 44 27.5 39 27.5 32Z", INK)
    return head + eyes + beak

@reg("cc3d", BLUE_DEEP)
def cc3d():
    c1 = stroke("M26.5 16.8A5.5 5.5 0 1 0 26.5 25.2", INK, 3.4)
    c2 = stroke("M42.5 16.8A5.5 5.5 0 1 0 42.5 25.2", INK, 3.4)
    three = stroke("M18 33.5H26L22 38A3.9 3.9 0 1 1 18 43.5", INK, 3.4)
    d = stroke("M35 33.5V45H38A5.75 5.75 0 0 0 38 33.5Z", INK, 3.4)
    return c1 + c2 + three + d

@reg("cdbaby", GREY_DARK)
def cdbaby():
    return (poly([(16, 13), (30, 21), (16, 29)], INK, 2.5) +
            poly([(35, 22), (49, 30), (35, 38)], INK, 2.5) +
            poly([(16, 31), (30, 39), (16, 47)], INK, 2.5))

@reg("cdogs-sdl", BROWN_DEEP)
def cdogs():
    beret = rrect(18, 12, 28, 8, 1.5, RED) + rrect(40, 15, 6, 7, 1, RED)
    face = rrect(20, 20, 24, 26, 2, INK)
    shades = rrect(20, 25.5, 24, 5, 1, HOLE)
    nose = rrect(30, 31, 4, 5, 1, BROWN_SOFT)
    mouth = rrect(27, 39, 10, 2.8, 1, HOLE)
    return face + shades + nose + mouth + beret

@reg("celeste", RED_DEEP)
def celeste():
    u, x0, y0 = 3.2, 16, 13
    rows = {2: (1, 8), 3: (0, 10), 4: (0, 10), 5: (0, 10), 6: (1, 8), 7: (2, 6), 8: (3, 4), 9: (4, 2)}
    out = ""
    for r, (c, n) in rows.items():
        out += rrect(x0 + c * u, y0 + r * u, n * u, u + .05, 0, INK)
    out += rrect(x0 + 2 * u, y0 + u, 6 * u, u, 0, LIGHT_BLUE_SOFT) + rrect(x0 + 4 * u, y0, 2 * u, u, 0, LIGHT_BLUE_SOFT)
    for c, r in [(2, 3), (6, 3), (4, 5), (8, 5), (2, 6), (5, 7)]:
        out += rrect(x0 + c * u + .8, y0 + r * u + .8, u - 1.6, u - 1.6, 0, HOLE)
    return out

@reg("celestia", INDIGO_DARK)
def celestia():
    planet = circle(28.5, 34, 13.5, INK)
    sun = circle(41, 19.5, 8.6, HOLE) + circle(41, 19.5, 6.6, AMBER_LIGHT) + circle(41, 19.5, 2.8, INK)
    moon = circle(45.5, 42.5, 5, HOLE) + circle(45.5, 42.5, 3.4, INK)
    return planet + sun + moon

@reg("cemu", LIGHT_BLUE_DEEP)
def cemu():
    return stroke("M41.5 20.5A13.4 13.4 0 1 0 41.5 39.5", INK, 6.5)

@reg("cen64-qt", ORANGE_DEEP)
def cen64():
    frame = stroke("M18 40V26.5A4 4 0 0 1 22 22.5H27V26H37V22.5H42A4 4 0 0 1 46 26.5V40", INK, 4)
    dots = "".join(circle(x, 33, 2.6, INK) for x in (24.5, 29.5, 34.5, 39.5))
    return frame + dots

@reg("cerebro", DEEP_PURPLE_DEEP)
def cerebro():
    def hexc(r, w, col):
        v = [pt(CX, CY, r, a) for a in (-30, -90, 210, 150, 90, 30)]
        d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in v)
        return stroke(d, col, w)
    return hexc(15, 5, INK) + hexc(7.5, 3.6, PURPLE_SOFT)

@reg("cervisia", RED_LIGHT)
def cervisia():
    out = ""
    for x, y, w in [(15, 16, 16), (33, 16, 16), (15, 26, 4), (21, 26, 17), (40, 26, 9),
                    (15, 36, 16), (33, 36, 16)]:
        out += rrect(x, y, w, 8, 2, INK)
    return out

@reg("cewl", TEAL_DEEP)
def cewl():
    head = circle(32, 17.5, 6, INK)
    torso = path("M21.5 36C21.5 28 25.5 25 32 25C38.5 25 42.5 28 42.5 36Z", INK)
    laptop = rrect(25, 29.5, 14, 10, 1.5, HOLE) + rrect(26.8, 31.2, 10.4, 6.6, 1, INK)
    legs = rrect(15, 39, 34, 8.5, 4.25, INK)
    return head + torso + legs + laptop

@reg("charles-proxy", BLUE_DEEP)
def charles():
    body = circle(32, 35, 11.5, INK)
    neck = path("M26 17.5H38L37.5 27H26.5Z", INK)
    rim = rrect(24, 13, 16, 4.6, 2.3, INK)
    spout = poly([(24.5, 13.5), (18, 12.5), (26, 19)], INK, 2)
    handle = stroke("M38 19.5C46.5 19.5 47.5 29.5 42 32", INK, 3.4)
    petals = "".join(circle(*pt(32, 35.5, 4.4, -90 + 72 * k), 3, HOLE) for k in range(5))
    return body + neck + rim + spout + handle + petals + circle(32, 35.5, 2.6, AMBER_LIGHT)

@reg("checkbox", DEEP_ORANGE_DEEP)
def checkbox():
    cx, cy = 29, 28
    rings = _ring(cx, cy, 9.5, INK, 4.2)
    for a in (180, -60, 60):
        x, y = pt(cx, cy, 13.2, a)
        rings += circle(x, y, 5.6, HOLE) + circle(x, y, 3.8, INK)
    badge = _badge(42, 40.5, 9.5, DEEP_PURPLE)
    return rings + badge + _gear_b(42, 40.5, 4.6, INK, DEEP_PURPLE)

@reg("checkra1n", GREY_DARK)
def checkra1n():
    apple = path("M32 19.5C28 17 20 17.5 18 25.5C16 33.5 21 45.5 26.5 46.5C29 47 30 45.5 32 45.5"
                 "C34 45.5 35 47 37.5 46.5C43 45.5 48 33.5 46 26.5C44 18.5 36 17 32 19.5Z", INK)
    bite = circle(49, 30.5, 5, HOLE)
    leaf = path("M31.5 17.5C31.5 13.5 34.5 11.5 38.5 11.5C38.5 15 36 17.5 31.5 17.5Z", INK)
    king = (rrect(25.5, 39.5, 13, 3.4, 1.4, HOLE) + path("M28.5 39.5L30 31H34L35.5 39.5Z", HOLE) +
            rrect(27.5, 28.5, 9, 3, 1.3, HOLE) + circle(32, 25.8, 3, HOLE) +
            line(32, 19.8, 32, 23, HOLE, 2.2) + line(30.2, 21.2, 33.8, 21.2, HOLE, 2.2))
    return apple + bite + leaf + king

@reg("cheese", PURPLE_DEEP)
def cheese():
    photo = rrect(15, 13, 34, 34, 5, INK)
    grin = path("M18.5 27C24 33 40 33 45.5 27C44.5 38 37 42.5 32 42.5C27 42.5 19.5 38 18.5 27Z", HOLE)
    teeth = "".join(rrect(x - 1.5, 31, 3, 4, 1, INK) for x in (24, 28.7, 33.4, 38.1))
    brows = stroke("M20 21Q24 18.5 28 21", HOLE, 2.6) + stroke("M36 21Q40 18.5 44 21", HOLE, 2.6)
    return photo + grin + teeth + brows

@reg("cherrytree", RED_DEEP)
def cherrytree():
    stems = (stroke("M23 37C24 27 29 18 39 13", AMBER, 3) +
             stroke("M40 34C38 27 37 20 39 13", AMBER, 3))
    back = circle(40.5, 36, 8.3, INK)
    front = circle(23.5, 39, 10.3, HOLE) + circle(23.5, 39, 8.3, INK)
    return stems + back + front

@reg("chess", BROWN_DEEP)
def chess():
    board = rrect(15, 13, 17, 17, 3, BROWN_LIGHT) + rrect(32, 30, 17, 17, 3, BROWN_LIGHT)
    rook = (rrect(21, 40, 22, 6, 2, INK) + path("M25 23H39L38 40H26Z", INK) +
            rrect(22, 14, 20, 10, 2, INK) + rrect(27, 13, 3.5, 5.5, 1, HOLE) +
            rrect(33.5, 13, 3.5, 5.5, 1, HOLE))
    rook = rook.replace('"HOLE"', '"#91746A"')
    return board + rook

@reg("chiaki", YELLOW)
def chiaki():
    band = poly([(14, 26), (26.5, 26), (28, 21), (32, 24.5), (36, 21), (37.5, 26), (50, 26),
                 (50, 35), (37, 35), (32, 44), (27, 35), (14, 35)], INK, 2)
    eyes = rrect(26.5, 28.5, 3, 5, 1.2, HOLE) + rrect(34.5, 28.5, 3, 5, 1.2, HOLE)
    wifi = (stroke("M28.5 17.5A5 5 0 0 1 35.5 17.5", INK, 2.4) +
            stroke("M25.5 14.5A9.2 9.2 0 0 1 38.5 14.5", INK, 2.4))
    return band + eyes + wifi

@reg("child-of-light", INDIGO_DARK)
def child_of_light():
    rim = _ring(CX, CY, 16, INK, 2.4)
    x = line(21, 19, 43, 41, INK, 2.6) + line(43, 19, 21, 41, INK, 2.6)
    rays = "".join(line(*pt(32, 20, 2.5, 45 * k), *pt(32, 20, 5, 45 * k), INK, 1.8) for k in range(8))
    sun = circle(32, 20, 2.6, INK) + rays
    frown = stroke("M26.5 43A6 6 0 0 1 37.5 43", INK, 2.6)
    leaves = (circle(22, 30, 2, INK) + circle(42, 30, 2, INK))
    return rim + x + sun + frown + leaves

@reg("chirp", CYAN_DEEP)
def chirp():
    plate = rrect(13, 24, 38, 12, 4, INK)
    screws = circle(17.5, 30, 2.2, HOLE) + circle(46.5, 30, 2.2, HOLE)
    shell = poly([(21, 20.5), (43, 20.5), (40.5, 39.5), (23.5, 39.5)], INK, 3)
    shell = poly([(21, 20.5), (43, 20.5), (40.5, 39.5), (23.5, 39.5)], HOLE, 7) + shell
    pins = ("".join(circle(25 + 3.5 * i, 27, 1.7, HOLE) for i in range(5)) +
            "".join(circle(26.75 + 3.5 * i, 33, 1.7, HOLE) for i in range(4)))
    return plate + shell + pins + screws

@reg("chkrootkit", BLUE_GREY)
def chkrootkit():
    disc_ = circle(27, 27, 13.5, INK)
    p = path("M32 30H41A6.5 6.5 0 0 1 41 43H37V48H32Z", INK,
             f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"')
    return disc_ + p + rrect(36.5, 34, 4.5, 5, 1.2, HOLE)

def _cone():
    cone = poly([(22, 29), (42, 29), (32, 48)], INK, 3)
    rim = rrect(19, 27, 26, 4.4, 2.2, INK)
    scoop = path("M19 29C17.5 21.5 22.5 17.5 27 17C27.5 13.5 30.5 11 34.5 10.5"
                 "C34.5 13.5 37 15.5 39.5 17.5C44 19 46.5 23.5 45 29Z", BROWN_DEEP)
    return cone + scoop + rim

@reg("chocolate-doom", ORANGE_DEEP)
def chocolate_doom():
    return _cone()

@reg("chocolate-doom-setup", ORANGE_DEEP)
def chocolate_doom_setup():
    badge = _badge(42.5, 40.5, 9.5, RED_DEEP)
    return _sc(_cone(), .95, 30, 30) + badge + _gear_b(42.5, 40.5, 4.6, INK, RED_DEEP)

@reg("choqok", BROWN_SOFT)
def choqok():
    body = path("M16 40C14 28 20 18.5 32 18.5C44 18.5 50 28 48 40C47.3 44 44.5 46 40.5 46"
                "H23.5C19.5 46 16.7 44 16 40Z", INK)
    tuft = poly([(28.5, 20), (32, 13), (35.5, 20)], INK, 2)
    wink = stroke("M21 29Q24.5 25.5 28 29", HOLE, 2.6)
    eye = circle(40, 28.5, 4.8, HOLE) + circle(40, 28.5, 2.3, INK)
    beak = poly([(28.5, 34), (35.5, 34), (32, 39)], AMBER, 2)
    return body + tuft + wink + eye + beak

@reg("christmas-tree", CYAN_DARK)
def christmas_tree():
    tree = (poly([(32, 17), (40.5, 26), (23.5, 26)], INK, 3) +
            poly([(32, 21.5), (43.5, 34), (20.5, 34)], INK, 3) +
            poly([(32, 28), (46.5, 44), (17.5, 44)], INK, 3))
    star = poly([pt(32, 15.5, 5.5 if k % 2 == 0 else 2.4, -90 + 36 * k) for k in range(10)], AMBER_LIGHT, 1.2)
    balls = "".join(circle(x, y, 1.9, HOLE) for x, y in [(29, 24), (36, 31), (26, 32), (32, 39), (40, 41), (23, 41)])
    return tree + balls + star

def _grid():
    return "".join(rrect(18.5 + 10 * c, 16.5 + 10 * r, 7, 7, 2, INK) for r in range(3) for c in range(3))

@reg("chrome-app-list", BROWN_LIGHT)
def chrome_app_list():
    return _grid()

@reg("chromium-app-list", BLUE_LIGHT)
def chromium_app_list():
    return _grid()

@reg("chrome-ieailfmhaghpphfffooibmlghaeopach-Default", RED)
def chrome_paint():
    pal = cut(cpath(31, 30, 16.5) + cpath(37.5, 38.5, 3.6), INK)
    dots = "".join(circle(x, y, 3, HOLE) for x, y in [(23, 25), (30, 20.5), (38.5, 22.5), (22.5, 33.5)])
    brush = line(31, 41, 45.5, 25.5, PINK_SOFT, 3.4) + poly([(45, 24.5), (49.5, 19.5), (47.5, 26)], PINK_SOFT, 2)
    brush = line(31, 41, 45.5, 25.5, HOLE, 7) + brush
    return pal + dots + brush

@reg("chrome-remote-desktop", BLUE_DARK)
def chrome_remote():
    back = rrect(22, 13, 27, 21, 3, INK) + rrect(25, 16, 21, 15, 1.5, HOLE)
    front = rrect(13.5, 21.5, 30, 24, 3.5, HOLE) + rrect(15, 23, 27, 21, 3, INK)
    return back + front + _chrome_b(28.5, 33.5, 7.5, HOLE, INK, 1.4)

@reg("chrome-store", BLUE_DEEP)
def chrome_store():
    handle = stroke("M25 21V17A4 4 0 0 1 29 13H35A4 4 0 0 1 39 17V21", INK, 3.2)
    bag = rrect(15, 20, 34, 27, 4, INK)
    return handle + bag + _chrome_b(32, 34.5, 9, HOLE, INK, 1.6)

@small("carla")
def carla_s():
    out = ""
    for y0 in (12, 31):
        out += rrect(14, y0, 36, 17.5, 3.5, INK) + circle(22, y0 + 8.75, 5, HOLE)
        out += rrect(31, y0 + 3.5, 12, 4, 2, HOLE) + rrect(31, y0 + 10, 8, 4, 2, HOLE)
    return out

@small("carla-control")
def carla_control_s():
    return carla_s()

@small("chirp")
def chirp_s():
    plate = rrect(13, 24, 38, 12, 4, INK)
    shell = poly([(21, 20.5), (43, 20.5), (40.5, 39.5), (23.5, 39.5)], INK, 3)
    pins = "".join(circle(x, 27, 2.3, HOLE) for x in (26, 32, 38)) + \
        "".join(circle(x, 33.5, 2.3, HOLE) for x in (29, 35))
    return plate + shell + pins

@small("celeste")
def celeste_s():
    u, x0, y0 = 3.2, 16, 13
    rows = {2: (1, 8), 3: (0, 10), 4: (0, 10), 5: (0, 10), 6: (1, 8), 7: (2, 6), 8: (3, 4), 9: (4, 2)}
    out = "".join(rrect(x0 + c * u, y0 + r * u, n * u, u + .05, 0, INK) for r, (c, n) in rows.items())
    return out + rrect(x0 + 2 * u, y0, 6 * u, 2 * u, 0, LIGHT_BLUE_SOFT)

@small("checkra1n")
def checkra1n_s():
    apple = path("M32 19.5C28 17 20 17.5 18 25.5C16 33.5 21 45.5 26.5 46.5C29 47 30 45.5 32 45.5"
                 "C34 45.5 35 47 37.5 46.5C43 45.5 48 33.5 46 26.5C44 18.5 36 17 32 19.5Z", INK)
    leaf = path("M31.5 17.5C31.5 13.5 34.5 11.5 38.5 11.5C38.5 15 36 17.5 31.5 17.5Z", INK)
    king = (rrect(25, 38.5, 14, 4.5, 2, HOLE) + path("M28 39L30 29H34L36 39Z", HOLE) +
            circle(32, 26, 4, HOLE))
    return apple + circle(49, 30.5, 5, HOLE) + leaf + king

@small("child-of-light")
def child_of_light_s():
    return (_ring(CX, CY, 16, INK, 3) + line(21, 19, 43, 41, INK, 3.4) +
            line(43, 19, 21, 41, INK, 3.4) + circle(32, 20, 4, INK))

@small("cheese")
def cheese_s():
    photo = rrect(15, 13, 34, 34, 5, INK)
    grin = path("M18.5 25C24 32 40 32 45.5 25C44.5 38 37 43 32 43C27 43 19.5 38 18.5 25Z", HOLE)
    return photo + grin + rrect(22, 30, 20, 5, 1.5, INK)

@small("chrome-remote-desktop")
def chrome_remote_s():
    back = rrect(22, 12, 28, 21, 3, INK) + rrect(25, 15, 22, 15, 1.5, HOLE)
    front = rrect(12.5, 20.5, 32, 26, 3.5, HOLE) + rrect(14, 22, 29, 23, 3, INK)
    return back + front + circle(28.5, 33.5, 6.5, HOLE) + circle(28.5, 33.5, 2.8, INK)

@small("chrome-store")
def chrome_store_s():
    handle = stroke("M25 21V17A4 4 0 0 1 29 13H35A4 4 0 0 1 39 17V21", INK, 3.2)
    bag = rrect(15, 20, 34, 27, 4, INK)
    return handle + bag + circle(32, 34.5, 8, HOLE) + circle(32, 34.5, 3.5, INK)

@small("cantor")
def cantor_s():
    rad = stroke("M14 30L22 38L28 16H49", INK, 3.6)
    return rad + _ring(39, 28, 4.8, INK, 3.4) + line(43.8, 22.5, 43.8, 34, INK, 3.4)

@small("chkrootkit")
def chkrootkit_s():
    return circle(26, 26, 13, INK) + path("M31 29H41A7 7 0 0 1 41 43H37V49H31Z", INK,
                                          f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')

@small("cc3d")
def cc3d_s():
    c1 = stroke("M28 16A6 6 0 1 0 28 25", INK, 4)
    c2 = stroke("M44 16A6 6 0 1 0 44 25", INK, 4)
    three = stroke("M17 33H26L22 37.5A4.3 4.3 0 1 1 17 44", INK, 4)
    d = stroke("M35 33V46H38.5A6.5 6.5 0 0 0 38.5 33Z", INK, 4)
    return c1 + c2 + three + d
