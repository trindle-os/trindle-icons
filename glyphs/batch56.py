# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 56: poedit to preferences-desktop-font.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
import math
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY,
    BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_SOFT, BROWN, circle, CX, CY, CYAN,
    CYAN_DEEP, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INK, LIGHT_BLUE,
    LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE_DARK, ORANGE_DEEP,
    ORANGE_SOFT, path, PINK_DARK, PINK_LIGHT, PINK_SOFT, poly, pt, PURPLE, RED, RED_DARK,
    RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke, TEAL,
)
from glyphs.kit import arc_b, registry, _ring

ICONS, SMALL, reg, small = registry()


def _badge(body, glyph):
    """Main mark shrunk up-left, a round badge bottom-right parted by a tile gap."""
    badge = circle(42.5, 40.5, 10, HOLE) + circle(42.5, 40.5, 8.3, INK) + glyph
    return g(body, "translate(29 27) scale(.86) translate(-32 -30)") + badge


TWO = stroke("M39.4 37.6C39.4 35.9 40.8 34.8 42.5 34.8C44.3 34.8 45.5 35.9 45.5 37.4"
             "C45.5 40 40 42.3 39.3 46.2H45.8", HOLE, 2.4)
R_ = stroke("M40 45.5V35.5H43.2C45.2 35.5 46.2 36.6 46.2 38.1C46.2 39.7 45.2 40.8 43.2 40.8H40"
            "M43.2 40.8L46.2 45.5", HOLE, 2.3)


@reg("poedit", ORANGE_DEEP)
def poedit():
    card = rrect(15, 13, 34, 34, 6, INK)
    kanji = stroke("M19.5 19.8L24.8 18.5M18.5 22.8H26M22.3 18.8V31M22.3 23.5L18.8 28.5"
                   "M22.3 23.5L25.8 27.5M28 20.5H33V27.5H28Z", HOLE, 2.2)
    yu = stroke("M30 34V44M30 39H34", HOLE, 2.6) + \
        f'<ellipse cx="38.5" cy="39" rx="3.3" ry="4.9" fill="none" stroke="{HOLE}" stroke-width="2.6"/>'
    return card + kanji + yu


@reg("poezio", BROWN)
def poezio():
    feather = path("M47 12C36 12.5 25.5 19.5 22.5 31.5C21.5 35.5 22 38.5 24 40.5"
                   "C34.5 37.5 44.5 28 47 12Z", INK)
    spine = stroke("M24.5 39.5L41.5 19", HOLE, 1.8)
    notch = stroke("M33 34L37.5 33.5M28 24.5L30.5 29", HOLE, 1.8)
    quill = line(17, 47, 26, 37, INK, 2.6)
    return feather + spine + notch + quill


@reg("pokerth", RED_DEEP)
def pokerth():
    chip = circle(CX, CY, 16.5, INK)
    stripes = "".join(g(rrect(29.5, 12.5, 5, 5, 1, HOLE), f"rotate({60 * k} 32 30)") for k in range(6))
    inner = circle(CX, CY, 11.3, HOLE) + circle(CX, CY, 9.6, INK)
    th = stroke("M24 25.5H30M27 25.5V35M33.5 25.5V35M39.5 25.5V35M33.5 30.2H39.5", HOLE, 2.6)
    return chip + stripes + inner + th


@reg("pokete", BLUE_GREY_DEEP)
def pokete():
    corners = stroke("M15 21V15H21M43 15H49V21M49 39V45H43M21 45H15V39", INK, 3)
    dashes = stroke("M27 15H30M34 15H37M27 45H30M34 45H37M15 28.5V31.5M49 28.5V31.5", INK, 3)
    eyes = rrect(22, 24.5, 6, 3.2, 1.6, INK) + rrect(36, 24.5, 6, 3.2, 1.6, INK)
    mouth = stroke("M25 34L27.8 37.5L30.6 34L33.4 37.5L36.2 34L39 37.5", INK, 2.4)
    return corners + dashes + eyes + mouth


@reg("polari", BLUE_DEEP)
def polari():
    back = rrect(27, 23, 23, 18, 5, BLUE_SOFT) + poly([(42, 39), (49, 39), (49, 46)], BLUE_SOFT, 2)
    gap = rrect(12.2, 11.2, 25.6, 22.6, 6.5, HOLE) + poly([(17, 30), (24, 30), (15.5, 38.5)], HOLE, 5.5)
    front = rrect(14, 13, 22, 19, 5, INK) + poly([(17.5, 30), (23, 30), (16.5, 36.5)], INK, 2)
    hash_ = stroke("M22.5 17.5V28M27.5 17.5V28M19 20.5H31M19 25H31", HOLE, 2.4)
    return back + gap + front + hash_


@reg("polo", BLUE_GREY_DARK)
def polo():
    stem = stroke("M27.5 45C29.5 37 30.5 27 29 18", INK, 4.2)
    bowl = stroke("M20 24C23.5 16 34.5 13.5 40.5 16C46.5 18.5 45 28 36.5 30.5"
                  "C33.5 31.5 30.5 31.5 28.5 31", INK, 4.2)
    return stem + bowl


@reg("polychromatic", ORANGE_DARK)
def polychromatic():
    kb = rrect(13, 13, 31, 18, 3.5, INK)
    keys = "".join(rrect(16.5 + c * 5, 16.5 + r * 5, 3, 2.8, .8, HOLE) for r in range(2) for c in range(5))
    space = rrect(19, 26.5, 19, 2.6, 1.2, HOLE)
    cable = stroke("M44 22C49.5 22 50.5 30 46.5 33C42.5 36 35.5 33 31 37", INK, 2.4)
    mouse = g(rrect(21.5, 34, 10, 14, 5, INK) + line(26.5, 36.5, 26.5, 39.5, HOLE, 2), "rotate(30 26.5 41)")
    return kb + keys + space + cable + mouse


@reg("polychromatic-controller", DEEP_PURPLE_LIGHT)
def polychromatic_ctl():
    out = ""
    for y, kx in [(22, 38), (38, 25)]:
        out += rrect(15, y - 2.5, 34, 5, 2.5, DEEP_PURPLE) + rrect(15, y - 2.5, kx - 15, 5, 2.5, INK)
        out += circle(kx, y, 7, HOLE) + circle(kx, y, 5.3, INK)
    return out


@reg("polyphone", ORANGE_DEEP)
def polyphone():
    stem = line(32, 29, 32, 46, INK, 3)
    leaves = (path("M31 29C26.5 29 22.5 25.5 22.5 21C27 20.5 31 24 31 29Z", INK) +
              path("M33 27C33 21 37 16.5 42.5 17C42.5 23 38.5 27 33 27Z", INK))
    arcs = (stroke("M20 22A13 13 0 0 0 20 38M44 22A13 13 0 0 1 44 38", INK, 3) +
            stroke("M15 17.5A19 19 0 0 0 15 42.5M49 17.5A19 19 0 0 1 49 42.5", INK, 3))
    return stem + leaves + arcs


@reg("pomodoneapp", PINK_LIGHT)
def pomodone():
    return rrect(16, 14, 32, 32, 8.5, INK) + rrect(22, 20, 20, 20, 4.5, PINK_DARK)


@reg("pop-shop", ORANGE_DEEP)
def pop_shop():
    fins = (poly([(26.5, 30), (20, 40), (26, 40)], INK, 2.5) +
            poly([(37.5, 30), (44, 40), (38, 40)], INK, 2.5))
    body = path("M32 11C37.5 16 39.5 25 38.5 38H25.5C24.5 25 26.5 16 32 11Z", INK)
    window = circle(32, 24, 3.3, HOLE)
    flame = poly([(28, 41), (36, 41), (32, 48.5)], ORANGE_SOFT, 2)
    return fins + body + window + flame


@reg("popcorn-time", RED_DEEP)
def popcorn_time():
    cloud = (circle(23, 24, 6, INK) + circle(32, 19.5, 7.5, INK) + circle(41, 24, 6, INK) +
             rrect(18, 22, 28, 8, 3, INK))
    bucket = poly([(18, 32), (46, 32), (42.5, 47), (21.5, 47)], INK, 2)
    stripes = line(27.5, 33.5, 28.5, 46, HOLE, 2.4) + line(36.5, 33.5, 35.5, 46, HOLE, 2.4)
    face = circle(27.5, 23.5, 1.8, HOLE) + circle(36.5, 23.5, 1.8, HOLE) + stroke("M29.5 27Q32 29 34.5 27", HOLE, 1.8)
    return cloud + bucket + stripes + face


@reg("popout3d", RED_LIGHT)
def popout3d():
    frame = rrect(13, 17, 38, 17, 4.5, INK)
    lenses = rrect(16.5, 20.5, 13.5, 10, 2.5, RED_DEEP) + rrect(34, 20.5, 13.5, 10, 2.5, CYAN)
    notch = path("M28 34C28 31.5 29.8 30 32 30C34.2 30 36 31.5 36 34Z", HOLE)
    hills = stroke("M15 43L21.5 38.5L27.5 42L34.5 37.5L41 41.5L49 38", INK, 3)
    return frame + lenses + notch + hills


def _aperture(cx=CX, cy=CY, r=16.5, w=2, n=8):
    ri = r * .43
    blades = ""
    for k in range(n):
        a = -80 + 360 / n * k
        x0, y0 = pt(cx, cy, ri, a)
        L = math.sqrt(r * r - ri * ri)
        dx, dy = math.cos(math.radians(a + 90)), math.sin(math.radians(a + 90))
        blades += line(x0, y0, x0 + dx * L, y0 + dy * L, HOLE, w, "butt")
    return circle(cx, cy, r, INK) + blades + circle(cx, cy, ri, HOLE)


@reg("portal-prelude", GREY_DARK)
@reg("portal-reloaded", BLUE_DEEP)
@reg("portal-revolution", RED_DEEP)
@reg("portal", BLUE_DEEP)
def portal():
    return _aperture()


@reg("portal-stories-mel", BLUE_DEEP)
def portal_mel():
    out = _aperture()
    r = 16.5
    for y in (16, 21.5, 27):
        edge = max(abs(y - CY), abs(y + 3.2 - CY))
        x0 = CX - math.sqrt(r * r - edge * edge) + .4
        out += rrect(x0, y, CX + 2 - x0, 3.2, 0, DEEP_ORANGE_LIGHT)
    return out


@reg("portal2", BLUE)
def portal2():
    return _badge(_aperture(), TWO)


@reg("portfolio", LIGHT_BLUE_DEEP)
def portfolio():
    area = path("M14 46V37L21 30.5L27 35L34.5 23L39.5 27.5L49 15V46Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    low = path("M15 45V42.5C20.5 39.5 26 40 32 41.5C38 43 43 40.5 48 38V45Z", LIGHT_BLUE_DARK)
    return area + low


@reg("portmaster", BLUE_GREY_DARK)
def portmaster():
    ring = _ring(CX, CY, 16, INK, 3.2)
    mid = "".join(arc_b(CX, CY, 10.5, a0, a1, INK, 3.2) for a0, a1 in [(60, 130), (148, 218), (236, 306)])
    inner = arc_b(CX, CY, 5, 90, 330, INK, 3)
    return ring + mid + inner


@reg("portproton", CYAN_DEEP)
def portproton():
    ring = _ring(CX, CY, 11, CYAN_SOFT, 3.4)
    balls = ""
    for a, r in [(-145, 6.2), (-25, 5.2), (85, 5.2)]:
        x, y = pt(CX, CY, 11, a)
        balls += circle(x, y, r + 1.6, HOLE) + circle(x, y, r, INK)
    return ring + balls


def _postal():
    p = path("M17.5 13.5H34C43.5 13.5 48.5 18.5 48.5 25.5C48.5 32.5 43.5 37 34 37H30.5V42.5"
             "C30.5 44.5 31.5 45.5 33.5 46V47.5H16.5V46C19 45.5 20.5 44.5 20.5 42.5V18"
             "C20.5 16.5 19.5 15.5 17.5 15Z", INK)
    counter = path("M30.5 18.5C37.5 19 41 22 41 25.5C41 29 37.5 32 30.5 32.5C34 29 34 22 30.5 18.5Z", HOLE)
    return p + counter


@reg("postal", RED_DEEP)
def postal():
    return _postal()


@reg("postal-2", RED_DARK)
def postal_2():
    return _badge(_postal(), TWO)


@reg("postal-redux", RED)
def postal_redux():
    return _badge(_postal(), R_)


@reg("postman", DEEP_ORANGE)
def postman():
    disc = circle(CX, CY, 16.5, INK)
    body = poly([(33, 23.5), (41, 27.5), (29, 38.5), (24, 35.5)], HOLE, 2.5)
    head = circle(38, 20, 5.2, HOLE) + path("M35.2 19.5A2.9 2.9 0 0 1 40.8 19.5Z", INK)
    jet = poly([(23, 36.5), (28.5, 40), (17, 44.5)], HOLE, 2)
    return disc + body + head + jet


@reg("postr", BLUE_GREY_DARK)
def postr():
    dots = circle(21.5, 26, 7, INK) + circle(37.5, 26, 7, PINK_SOFT)
    badge = circle(42.5, 40.5, 10, HOLE) + circle(42.5, 40.5, 8.3, DEEP_PURPLE_SOFT)
    arrow = stroke("M42.5 45.5V36.5M38.5 40L42.5 36L46.5 40", INK, 2.6)
    return dots + badge + arrow


@reg("powder-player", BLUE_GREY_DARK)
def powder_player():
    hexa = [pt(CX, CY, 16.5, -90 + 60 * k) for k in range(6)]
    frame = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexa) + "Z", INK, 3.4)
    dots = "".join(circle(32 + (j - i / 2) * 5.6, 20.5 + i * 5.4, 2.2, INK)
                   for i in range(4) for j in range(i + 1))
    return frame + dots


@reg("poweriso-gui", AMBER_DARK)
def poweriso():
    disc = circle(CX, CY, 16.5, INK)
    inner = circle(CX, CY, 9.5, AMBER_SOFT) + _ring(CX, CY, 5.3, AMBER_DARK, 3) + circle(CX, CY, 2.5, HOLE)
    slash = (line(*pt(CX, CY, 10.5, -50), *pt(CX, CY, 17, -50), HOLE, 2.4, "butt") +
             line(*pt(CX, CY, 10.5, 130), *pt(CX, CY, 17, 130), HOLE, 2.4, "butt"))
    return disc + inner + slash


@reg("powermanga", RED_DEEP)
def powermanga():
    wings = path("M13.5 35C17.5 27.5 25.5 26.5 32 29.5C38.5 26.5 46.5 27.5 50.5 35"
                 "C44.5 37 38.5 36.5 32 38.5C25.5 36.5 19.5 37 13.5 35Z", RED_SOFT)
    body = path("M32 11C37.5 17 39.5 28 38.5 38.5C36.5 43 27.5 43 25.5 38.5C24.5 28 26.5 17 32 11Z", INK)
    cockpit = f'<ellipse cx="32" cy="32" rx="2.8" ry="4.4" fill="{HOLE}"/>'
    flame = path("M26.5 42.5C29 45 35 45 37.5 42.5C36.5 46.5 34.5 48.5 32 48.5C29.5 48.5 27.5 46.5 26.5 42.5Z", AMBER)
    return wings + body + cockpit + flame


@reg("powersploit", BLUE_DEEP)
def powersploit():
    return stroke("M17 20.5L27 29.5L17 38.5", INK, 5) + rrect(30, 35.5, 17, 5, 2.5, INK)


@reg("pppoeconf", ORANGE_DARK)
def pppoeconf():
    hand = stroke("M19 22C25 16 39 16 45 22", INK, 5) + \
        rrect(13, 19.5, 10, 6.5, 3, INK) + rrect(41, 19.5, 10, 6.5, 3, INK)
    body = poly([(24, 27), (40, 27), (45, 45), (19, 45)], INK, 3)
    dial = _ring(32, 36, 4.8, HOLE, 2.6) + line(34.5, 38.5, 37, 41, HOLE, 2.6)
    return hand + body + dial


@reg("ppsspp", LIGHT_BLUE_DEEP)
def ppsspp():
    out = ""
    for k in range(4):
        piece = poly([(33.5, 25.5), (46.5, 25.5), (50, 33), (37, 33)], INK, 2.5)
        out += g(piece, f"rotate({-20 + 90 * k} 32 30)")
    return out


@reg("praat", PINK_LIGHT)
def praat():
    ring = arc_b(CX, CY, 14, -120, 190, INK, 5.5)
    bubble = path("M32.5 20.5A9.5 9.5 0 1 1 27 37.8L21.5 40L23.5 34.5A9.5 9.5 0 0 1 32.5 20.5Z", INK)
    return ring + bubble


@reg("pragha", BLUE_DEEP)
def pragha():
    bowl = stroke("M21 20C25 15.5 34 13.5 40 15.5C46.5 18 45.5 26.5 38.5 29.5C35 31 31 31 28.5 29.5", INK, 3.8)
    stem = stroke("M31.5 18.5C31.5 28.5 30 38 26 43.5C23.5 46.5 19.5 46 19.5 43C19.5 40.5 22.5 39.5 26 40.5", INK, 3.8)
    return bowl + stem


@reg("prboom-plus", RED_DARK)
def prboom():
    rs = [16.5, 10, 15, 9.5, 17, 11, 14.5, 9, 16, 10.5, 15.5, 9.5]
    pts = [pt(CX, CY, r, -80 + 30 * k) for k, r in enumerate(rs)]
    splat = poly(pts, INK, 3)
    plus = rrect(28.5, 21.5, 7, 17, 2, HOLE) + rrect(23.5, 26.5, 17, 7, 2, HOLE)
    return splat + plus


def _sliders(track, fill, knobs):
    out = ""
    for x, ky in zip((21, 32, 43), knobs):
        out += rrect(x - 2.2, 13, 4.4, 34, 2.2, track)
        if fill:
            out += rrect(x - 2.2, ky, 4.4, 47 - ky, 2.2, fill)
        out += circle(x, ky, 6, HOLE) + circle(x, ky, 4.5, INK)
    return out


@reg("preferences", BLUE_DEEP)
def preferences():
    return _sliders(BLUE_DARK, None, (19, 36, 31))


@reg("preferences-desktop", BLUE_GREY)
def preferences_desktop():
    return _sliders(BLUE_GREY_DARK, BLUE_GREY_SOFT, (19, 36, 31))


@reg("preferences-desktop-accessibility", INDIGO)
def pd_accessibility():
    disc = circle(CX, CY, 16.5, INK)
    man = (circle(32, 19.5, 3.2, HOLE) + line(21.5, 25.5, 42.5, 25.5, HOLE, 3.2) +
           rrect(29.5, 24.5, 5, 10.5, 1.5, HOLE) +
           line(30, 34, 30, 42, HOLE, 3) + line(34, 34, 34, 42, HOLE, 3))
    return disc + man


@reg("preferences-desktop-activities", INDIGO_DARK)
def pd_activities():
    return rrect(15, 13, 34, 14, 3.5, INK) + rrect(15, 31, 34, 16, 3.5, INDIGO)


@reg("preferences-desktop-animations", BLUE)
def pd_animations():
    cx, cy = 36.5, 24
    burst = circle(cx, cy, 9, BLUE_SOFT) + "".join(circle(*pt(cx, cy, 8.5, 22.5 + 45 * k), 4, BLUE_SOFT) for k in range(8))
    wand = line(16.5, 45.5, 30, 32, HOLE, 7) + line(16.5, 45.5, 30.5, 31.5, INK, 4)
    star = poly([pt(cx, cy, 9.5 if k % 2 == 0 else 4.2, -90 + 36 * k) for k in range(10)], INK, 2)
    return burst + wand + star


@reg("preferences-desktop-color", BLUE_GREY_DARK)
def pd_color():
    cols = [RED, PURPLE, LIGHT_BLUE, TEAL, AMBER, DEEP_ORANGE]
    return "".join(circle(*pt(CX, CY, 7.5, -150 + 60 * k), 8.8, c) for k, c in enumerate(cols))


@reg("preferences-desktop-cursors", GREY_DEEP)
def pd_cursors():
    return poly([(20, 12.5), (20, 42), (27, 35.5), (32.5, 46.5), (38, 44), (32.5, 33), (42, 33)], INK, 3)


@reg("preferences-desktop-default-applications", ORANGE_DARK)
def pd_default_apps():
    star = poly([pt(CX, 31, 17.5 if k % 2 == 0 else 8.3, -90 + 36 * k) for k in range(10)], INK, 3)
    a = stroke("M27 38.5L32 25L37 38.5M28.8 34H35.2", HOLE, 3)
    return star + a


@reg("preferences-desktop-display", BLUE_GREY)
def pd_display():
    frame = rrect(13, 13, 38, 27, 4, INK) + rrect(16.5, 16.5, 31, 20, 2, BLUE_GREY_DARK)
    stand = rrect(29.5, 39, 5, 5, 0, INK) + rrect(24, 43, 16, 4, 2, INK)
    return frame + stand


@reg("preferences-desktop-emoticons", AMBER_DEEP)
def pd_emoticons():
    face = circle(CX, CY, 16.5, INK)
    eyes = circle(26, 25, 2.5, HOLE) + circle(38, 25, 2.5, HOLE)
    smile = stroke("M24.5 33.5C28 39 36 39 39.5 33.5", HOLE, 3)
    return face + eyes + smile


@reg("preferences-desktop-font", GREY_DEEP)
def pd_font():
    return (stroke("M26.5 45C29.5 38 31 25 33 17.5C34 14.5 37 13 40.5 13.5H46", INK, 4) +
            stroke("M26.5 45C25 47 21.5 47.5 19.5 45.5", INK, 4) +
            stroke("M24 29.5H38", INK, 3.6))


@small("poedit")
def poedit_s():
    card = rrect(14, 12, 36, 36, 6, INK)
    yu = stroke("M21 21V39M21 30H28", HOLE, 3.6) + \
        f'<ellipse cx="36" cy="30" rx="6" ry="8.5" fill="none" stroke="{HOLE}" stroke-width="3.6"/>'
    return card + yu


@small("poezio")
def poezio_s():
    feather = path("M47 12C36 12.5 25.5 19.5 22.5 31.5C21.5 35.5 22 38.5 24 40.5"
                   "C34.5 37.5 44.5 28 47 12Z", INK)
    return feather + line(17, 47, 26, 37, INK, 3.2) + stroke("M25 39L40 21", HOLE, 2.4)


@small("pokerth")
def pokerth_s():
    chip = circle(CX, CY, 17.5, INK)
    th = stroke("M19.5 22.5H29.5M24.5 22.5V38M34 22.5V38M44 22.5V38M34 30.2H44", HOLE, 4)
    return chip + th


@small("pokete")
def pokete_s():
    corners = stroke("M14 21V14H21M43 14H50V21M50 39V46H43M21 46H14V39", INK, 3.4)
    eyes = rrect(21, 23.5, 8, 4, 2, INK) + rrect(35, 23.5, 8, 4, 2, INK)
    mouth = stroke("M24 33L28 38L32 33L36 38L40 33", INK, 3)
    return corners + eyes + mouth


@small("polari")
def polari_s():
    back = rrect(28, 23, 22, 19, 5, LIGHT_BLUE_SOFT)
    gap = rrect(11, 10, 28, 26, 7, HOLE)
    front = rrect(13, 12, 24, 22, 5.5, INK) + poly([(17, 32), (23, 32), (15.5, 39)], INK, 2)
    return back + gap + front + stroke("M21.5 16V30M28.5 16V30M17 19.5H33M17 26.5H33", HOLE, 3)


@small("polyphone")
def polyphone_s():
    stem = line(32, 29, 32, 46, INK, 3.6)
    leaves = (path("M31 29C26 29 21.5 25 21.5 20C26.5 19.5 31 23.5 31 29Z", INK) +
              path("M33 27C33 20.5 37.5 15.5 43.5 16C43.5 22.5 39 27 33 27Z", INK))
    arcs = stroke("M16.5 19A15 15 0 0 0 16.5 41M47.5 19A15 15 0 0 1 47.5 41", INK, 3.6)
    return stem + leaves + arcs


@small("popout3d")
def popout3d_s():
    frame = rrect(12, 18, 40, 22, 5, INK)
    lenses = rrect(16, 22, 14, 12, 3, RED_DEEP) + rrect(34, 22, 14, 12, 3, CYAN)
    notch = path("M27.5 40C27.5 36.5 29.5 35 32 35C34.5 35 36.5 36.5 36.5 40Z", HOLE)
    return frame + lenses + notch


@small("polychromatic")
def polychromatic_s():
    kb = rrect(12, 12, 33, 19, 4, INK) + rrect(16, 17, 25, 3.5, 1.5, HOLE) + rrect(19, 24, 19, 3.5, 1.5, HOLE)
    cable = stroke("M45 22C50.5 22 51 31 47 33.5C43 36 36 33 32 36", INK, 3)
    mouse = g(rrect(20.5, 33, 12, 15, 6, INK), "rotate(30 26.5 41)")
    return kb + cable + mouse


@small("powder-player")
def powder_player_s():
    hexa = [pt(CX, CY, 17, -90 + 60 * k) for k in range(6)]
    frame = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexa) + "Z", INK, 3.4)
    dots = "".join(circle(32 + (j - i / 2) * 8.5, 21.5 + i * 8, 3.4, INK)
                   for i in range(3) for j in range(i + 1))
    return frame + dots


@small("portmaster")
def portmaster_s():
    return (_ring(CX, CY, 16, INK, 3.6) +
            "".join(arc_b(CX, CY, 9.5, a0, a1, INK, 3.6) for a0, a1 in [(60, 170), (195, 305)]))


@small("popcorn-time")
def popcorn_time_s():
    cloud = circle(23, 23, 6.5, INK) + circle(32, 19, 8, INK) + circle(41, 23, 6.5, INK) + rrect(17, 21, 30, 9, 3, INK)
    bucket = poly([(17, 32), (47, 32), (43, 47), (21, 47)], INK, 2)
    return cloud + bucket + line(32, 34, 32, 45.5, HOLE, 3.4)


for _n in ("portal", "portal-prelude", "portal-reloaded", "portal-revolution"):
    SMALL[_n] = lambda: _aperture(r=17.5, w=3, n=6)


@small("portal2")
def portal2_s():
    return _badge(_aperture(r=17.5, w=3, n=6), TWO)


@small("preferences-desktop-color")
def pd_color_s():
    cols = [RED, LIGHT_BLUE, AMBER]
    return "".join(circle(*pt(CX, CY, 7, -90 + 120 * k), 10, c) for k, c in enumerate(cols))
