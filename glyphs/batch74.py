# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 74: world-of-tanks to xiaomitool.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DARK, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, circle, cpath, cut, CX, CY, DEEP_ORANGE, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE_LIGHT, f, g, GREY_DARK, GREY_DEEP, HOLE, INDIGO,
    INDIGO_LIGHT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, line, ORANGE_DARK,
    ORANGE_DEEP, path, poly, pt, PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DARK,
    RED_DEEP, rrect, stroke, TEAL, TEAL_DEEP,
)
from glyphs.kit import registry, _star_b

ICONS, SMALL, reg, small = registry()


DIGITS = {
    "2": "M-3.2 -2.3C-3.2 -4 -1.8 -5 0 -5C1.9 -5 3.2 -3.8 3.2 -2.2C3.2 .8 -3.3 2 -3.3 5H3.4",
    "3": "M-3 -5H3L-.5 -1C2 -1 3.5 .4 3.5 2.2C3.5 4 2 5 0 5C-1.5 5 -2.8 4.3 -3.3 3.3",
    "4": "M1.6 5.2V-5L-3.6 2H3.8",
}


def digit(ch, x, y, scale, colour, w):
    return g(stroke(DIGITS[ch], colour, w / scale), f"translate({f(x)} {f(y)}) scale({f(scale)})")


@reg("world-of-tanks", GREY_DARK)
def world_of_tanks():
    shield = path("M15 15.5A3 3 0 0 1 18 12.5H46A3 3 0 0 1 49 15.5L47.5 34"
                  "C47 40 41 45 32 48.5C23 45 17 40 16.5 34Z", INK)
    bar = rrect(21, 18, 22, 6.5, 1.5, HOLE)
    stem = poly([(28.5, 24), (35.5, 24), (34.8, 40.5), (32, 43.5), (29.2, 40.5)], HOLE, 1)
    return shield + bar + stem


@reg("worldofpadman", ORANGE_DEEP)
def worldofpadman():
    bubble = rrect(12.5, 15, 39, 27, 12, INK) + poly([(38, 39), (48, 48), (32, 41.5)], INK, 2)
    w = stroke("M17.5 23L20.3 34.5L23.5 27L26.7 34.5L29.5 23", HOLE, 2.6)
    o = circle(34.8, 30.5, 3.4, "none", f' stroke="{HOLE}" stroke-width="2.6"')
    p = stroke("M41.3 36V23.5H44A3.6 3.6 0 0 1 44 30.7H41.3", HOLE, 2.6)
    return bubble + w + o + p


@reg("worms", AMBER)
def worms():
    out = ""
    for a in (-150, -30, 90):
        p0, p1 = pt(CX, CY, 6, a - 30), pt(CX, CY, 17, a - 30)
        p2, p3 = pt(CX, CY, 17, a + 30), pt(CX, CY, 6, a + 30)
        out += path(f"M{f(p0[0])} {f(p0[1])}L{f(p1[0])} {f(p1[1])}A17 17 0 0 1 {f(p2[0])} {f(p2[1])}"
                    f"L{f(p3[0])} {f(p3[1])}A6 6 0 0 0 {f(p0[0])} {f(p0[1])}Z", INK,
                    f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return out + circle(CX, CY, 3.8, INK)


@reg("worms-armageddon", RED_DARK)
def worms_armageddon():
    cap = path("M19 27C15 27 13.5 23.5 15.5 21C16 17 19.5 15 23 16C25 12.5 29 11.5 32 13"
               "C35 11.5 39 12.5 41 16C44.5 15 48 17 48.5 21C50.5 23.5 49 27 45 27Z", INK)
    stem = path("M27.5 26H36.5L35.5 40H28.5Z", INK)
    ring = rrect(24, 31, 16, 4.5, 2.25, INK)
    base = path("M17 46.5C17 42 23 39.5 32 39.5C41 39.5 47 42 47 46.5Z", INK)
    return cap + stem + ring + base


@reg("wyrmsun", GREY_DEEP)
def wyrmsun():
    return stroke("M18 15C14.5 24 15 41 24 41C28.5 41 30.5 36.5 32 30"
                  "C33.5 36.5 35.5 41 40 41C49 41 49.5 24 46 15", INK, 5.5)


@reg("x-plane", LIGHT_BLUE_DARK)
def x_plane():
    return (poly([(14, 16), (22, 16), (32, 26), (42, 16), (50, 16), (37, 30), (50, 44),
                  (42, 44), (32, 34), (22, 44), (14, 44), (27, 30)], INK, 2.5))


@reg("x-rebirth", AMBER)
def x_rebirth():
    return (poly([(16, 15), (26, 15), (48, 45), (38, 45)], INK, 2) +
            poly([(41, 15), (48, 15), (24, 45), (17, 45)], INK, 2))


def _x_series(n):
    x = (poly([(13.5, 13.5), (22.5, 13.5), (41, 40), (32, 40)], INK, 2.5) +
         poly([(42, 13.5), (48, 13.5), (24, 40), (18, 40)], INK, 2))
    badge = circle(42.5, 41, 10.5, HOLE) + circle(42.5, 41, 8.5, INK)
    return x + badge + digit(n, 42.5, 41, .9, HOLE, 2.8)


@reg("x2-the-threat", PURPLE_DEEP)
def x2():
    return _x_series("2")


@reg("x3-reunion", BLUE_DEEP)
@reg("x3-terran-conflict", AMBER_DARK)
@reg("x3-albion-prelude", DEEP_ORANGE_DEEP)
def x3_ap():
    return _x_series("3")


@reg("x4-foundations", AMBER_DARK)
def x4():
    return _x_series("4")


@reg("xash3d", AMBER_DARK)
def xash3d():
    ring = cut(cpath(CX, CY, 17.5) + cpath(CX, CY, 14), INK)
    x = (poly([(22.5, 20), (29, 20), (41.5, 40), (35, 40)], INK, 2) +
         poly([(37, 20), (41.5, 20), (27, 40), (22.5, 40)], INK, 2))
    return ring + x


@reg("xbox", ORANGE_DARK)
def xbox():
    r = 17.5

    def rim(a0, a1):
        p0, p1 = pt(CX, CY, r, a0), pt(CX, CY, r, a1)
        return (f"M{f(p0[0])} {f(p0[1])}A{r} {r} 0 0 1 {f(p1[0])} {f(p1[1])}",
                f"{f(p0[0])} {f(p0[1])}")
    top, t0 = rim(-121, -59)
    right, r0 = rim(-36, 40)
    bottom, b0 = rim(54, 126)
    left, l0 = rim(140, 216)
    return (path(top + f"Q32 21.5 {t0}Z", INK) + path(right + f"Q34 30 {r0}Z", INK) +
            path(left + f"Q30 30 {l0}Z", INK) +
            path(bottom + f"Q22.5 32.5 32 26.5Q41.5 32.5 {b0}Z", INK))


@reg("xcom-2", LIGHT_BLUE)
def xcom2():
    shield = poly([(18, 13.5), (46, 13.5), (50, 23), (40, 47), (24, 47), (14, 23)], INK, 4)
    two = stroke("M25.5 24.5C25.5 20.8 28.5 18.5 32 18.5C35.8 18.5 38.5 21 38.5 24.5"
                 "C38.5 31 25.5 33.5 25.5 41H39", HOLE, 5)
    return shield + two


@reg("xcom-enemy-unknown", INDIGO)
def xcom_eu():
    shield = poly([(32, 11.5), (48, 19), (47, 37), (32, 48.5), (17, 37), (16, 19)], INK, 3)
    x = stroke("M23 20.5L41 39M41 20.5L23 39", HOLE, 4.5)
    return shield + x


@reg("xenia", LIGHT_BLUE_DARK)
def xenia():
    top = [(32, 15.5), (51, 28.5), (32, 41.5), (13, 28.5)]
    pins = ""
    for t in (.3, .7):
        a = (13 + 19 * t, 28.5 + 13 * t)
        b = (32 + 19 * t, 41.5 - 13 * t)
        pins += line(a[0], a[1], a[0], a[1] + 6, INK, 3) + line(b[0], b[1], b[0], b[1] + 6, INK, 3)
    chip = poly(top, INK, 3.5)
    x = stroke("M24.5 24L39.5 33M39.5 24L24.5 33", HOLE, 3.8)
    return pins + chip + x


@reg("xemu", GREY_DARK)
def xemu():
    return circle(CX, CY, 17.5, INK) + stroke("M24.5 21.5L39.5 38.5M39.5 21.5L24.5 38.5", HOLE, 5)


@reg("wps-office-etmain", INDIGO_LIGHT)
def wps_et():
    return stroke("M42 17.5H25A6.25 6.25 0 0 0 25 30H39A6.25 6.25 0 0 1 39 42.5H22", INK, 5.5)


@reg("wps-office-pdfmain", RED_DEEP)
def wps_pdf():
    return stroke("M29 30H36A6.25 6.25 0 0 0 36 17.5H35A6.25 6.25 0 0 0 28.75 23.75"
                  "V36.25A6.25 6.25 0 0 1 22.5 42.5", INK, 5.5)


@reg("wps-office-wppmain", DEEP_ORANGE)
def wps_wpp():
    return stroke("M24 44V17.5H36A7.25 7.25 0 0 1 36 32H24", INK, 5.5)


@reg("wps-office-wpsmain", BLUE)
def wps_wps():
    return stroke("M16.5 18L24.5 42L32 25L39.5 42L47.5 18", INK, 5.5)


@reg("wps-office2019-kprometheus", BLUE_DEEP)
def wps2019():
    hexa = poly([pt(CX, CY, 18, -90 + 60 * k) for k in range(6)], INK, 4)
    w = stroke("M21.5 24L26.5 37.5L32 28L37.5 37.5L42.5 24", HOLE, 3.6)
    return hexa + w


@reg("wunderlist", RED_DEEP)
def wunderlist():
    ribbon = poly([(20, 12.5), (44, 12.5), (44, 47.5), (32, 40), (20, 47.5)], INK, 3)
    return ribbon + _star_b(32, 26.5, 8.5, HOLE, 1.5)


@reg("write_stylus", INDIGO)
def write_stylus():
    body = rrect(-17, -5.5, 24, 11, 3, INK)
    band = rrect(4, -5.5, 3, 11, 0, HOLE)
    tip = poly([(8.5, -5.5), (18, 0), (8.5, 5.5)], INK, 2)
    return g(body + band + tip, "translate(31 29) rotate(40)")


@reg("xampp", ORANGE_DEEP)
def xampp():
    rings = (circle(24, 21, 5.5, "none", f' stroke="{INK}" stroke-width="6"') +
             circle(40, 39, 5.5, "none", f' stroke="{INK}" stroke-width="6"'))
    band = stroke("M34.5 21A5.5 5.5 0 1 1 43.5 25.3L20.5 34.7A5.5 5.5 0 1 0 29.5 39", INK, 6)
    return rings + band


@reg("wpa_gui", GREY_DARK)
def wpa_gui():
    a1, b1 = pt(CX, 28, 15.5, 130), pt(CX, 28, 15.5, 50)
    a2, b2 = pt(CX, 28, 9, 130), pt(CX, 28, 9, 50)
    arcs = (stroke(f"M{f(a1[0])} {f(a1[1])}A15.5 15.5 0 1 1 {f(b1[0])} {f(b1[1])}", INK, 4) +
            stroke(f"M{f(a2[0])} {f(a2[1])}A9 9 0 1 1 {f(b2[0])} {f(b2[1])}", INK, 4))
    return arcs + circle(CX, 28, 3.6, INK) + line(CX, 28, CX, 47, INK, 3.6)


@reg("wpscrackgui", BLUE_GREY_DEEP)
def wpscrackgui():
    ctr = (27, 38)
    arcs = ""
    for r in (9, 16.5):
        a, b = pt(*ctr, r, 225), pt(*ctr, r, 315)
        arcs += stroke(f"M{f(a[0])} {f(a[1])}A{r} {r} 0 0 1 {f(b[0])} {f(b[1])}", INK, 4)
    arcs += circle(*ctr, 3, INK)
    badge = circle(41, 38.5, 11.5, HOLE) + circle(41, 38.5, 9.5, INK)
    key = (circle(37, 38.5, 3.4, HOLE) + line(38, 38.5, 46.5, 38.5, HOLE, 2.6) +
           line(45.5, 38.5, 45.5, 42, HOLE, 2.6))
    return arcs + badge + key


@reg("wxcas", BLUE_DEEP)
def wxcas():
    return (rrect(15.5, 15, 33, 30, 4.5, INK) +
            stroke("M19.5 31H25L28.5 23.5L33 38L36.5 31H44.5", HOLE, 3.2))


@reg("wxglade", BLUE_GREY)
def wxglade():
    frame = rrect(14, 14, 36, 32, 4.5, INK)
    corner = rrect(18, 18, 6, 6, 1.5, RED)
    title = rrect(26.5, 18, 19.5, 6, 1.5, HOLE)
    canvas = rrect(18, 26.5, 28, 10.5, 1.5, HOLE)
    feet = rrect(18, 39.5, 13, 3, 1.5, AMBER) + rrect(33, 39.5, 13, 3, 1.5, PURPLE_SOFT)
    return frame + corner + title + canvas + feet


@reg("x-tile", BLUE_GREY_DEEP)
def x_tile():
    tiles = "".join(rrect(x, y, 16, 16, 3.5, INK) for x in (15, 33) for y in (13, 31))
    return tiles + stroke("M20 18L44 42M44 18L20 42", HOLE, 3.8)


@reg("x2goclient", LIGHT_BLUE_DEEP)
def x2goclient():
    x = line(25, 18, 42, 42, INK, 5.5, "butt") + line(42, 18, 25, 42, INK, 2.6, "butt")
    serifs = (line(20.5, 17, 29, 17, INK, 2.6) + line(38.5, 17, 46, 17, INK, 2.6) +
              line(20.5, 43, 29, 43, INK, 2.6) + line(38, 43, 46.5, 43, INK, 2.6))
    speed = "".join(line(13, y, 22 - abs(y - 30) * .35, y, INK, 2.4) for y in (23, 28, 33, 38))
    return x + serifs + speed


@reg("xcas", DEEP_PURPLE_LIGHT)
def xcas():
    out = ""
    for k in range(6):
        a = -90 + 60 * k
        e = pt(CX, CY, 16.5, a)
        out += line(CX, CY, *e, INK, 3.2)
        b = pt(CX, CY, 9.5, a)
        for s in (-50, 50):
            out += line(*b, *pt(*b, 5.5, a + s), INK, 3)
    return out + circle(CX, CY, 3.5, INK)


@reg("xclicker", BLUE_GREY_LIGHT)
def xclicker():
    mouse = poly([(26, 12.5), (38, 12.5), (43, 22), (43, 38), (38, 47.5), (26, 47.5),
                  (21, 38), (21, 22)], INK, 4)
    return mouse + line(CX, 17.5, CX, 25.5, HOLE, 3.2)


@reg("xcos", RED_DEEP)
def xcos():
    box = rrect(13.5, 14.5, 37, 31, 4.5, INK)
    screen = rrect(17.5, 18.5, 18, 23, 2, HOLE)
    pulse = stroke("M19.5 30.5H23L25 26L28.5 35L30.5 30.5H33.5", INK, 2.4)
    keys = circle(43, 22.5, 3.2, HOLE) + circle(43, 31, 2.2, HOLE) + circle(43, 37.5, 2.2, HOLE)
    return box + screen + pulse + keys


@reg("xdman", LIGHT_BLUE_DEEP)
def xdman():
    bowl = path("M13.5 31H50.5A18.5 18.5 0 0 1 13.5 31Z", INK)
    arrow_o = stroke("M32 13V38M23.5 30L32 38.5L40.5 30", HOLE, 10)
    arrow = stroke("M32 13V38M23.5 30L32 38.5L40.5 30", INK, 5)
    top = stroke("M16 26A16.5 16.5 0 0 1 24 15.5M48 26A16.5 16.5 0 0 0 40 15.5", INK, 3)
    return top + bowl + arrow_o + arrow


def _monitor(inner):
    frame = rrect(13.5, 13.5, 37, 27, 4, INK)
    screen = rrect(17, 17, 30, 20, 2, HOLE)
    stand = rrect(29, 40, 6, 4, 0, INK) + rrect(23.5, 43.5, 17, 3.5, 1.75, INK)
    return frame + screen + stand + inner


@reg("xfce-system-lock", GREY_DARK)
def xfce_lock():
    lock = (stroke("M28.5 26.5V24.5A3.5 3.5 0 0 1 35.5 24.5V26.5", INK, 2.6) +
            rrect(26, 26, 12, 8.5, 2, INK))
    return _monitor(lock)


@reg("xfce4-cpugraph-plugin", TEAL)
def xfce_cpugraph():
    return _monitor(stroke("M19.5 28H25L27.5 22.5L31 33L34 28H44.5", INK, 2.8))


@reg("xfce4-eyes", BLUE_GREY)
def xfce_eyes():
    e1 = circle(23.5, 29, 10, INK) + circle(21, 28, 3.2, HOLE)
    e2 = circle(38.5, 31.5, 14, HOLE) + circle(38.5, 31.5, 12.5, INK) + circle(35.5, 30.5, 4, HOLE)
    return e1 + e2


def _fsguard():
    card = rrect(19, 12.5, 26, 35, 5, INK)
    p = stroke("M26.5 38V27A5.5 5.5 0 1 1 32 32.5H29", HOLE, 3.8)
    return card + p


@reg("xfce4-fsguard-plugin", GREY_DEEP)
def xfce_fsguard():
    return _fsguard()


@reg("xfce4-fsguard-plugin-warning", GREY_DEEP)
def xfce_fsguard_w():
    badge = circle(42.5, 40.5, 11, HOLE) + circle(42.5, 40.5, 9, RED)
    bang = line(42.5, 35.5, 42.5, 41, INK, 3.2) + circle(42.5, 45, 1.7, INK)
    return g(_fsguard(), "translate(-4 0)") + badge + bang


@reg("xfce4-sample-plugin", ORANGE_DEEP)
def xfce_sample():
    face = circle(CX, CY, 17.5, INK)
    eyes = circle(26, 26, 2.8, HOLE) + circle(38, 26, 2.8, HOLE)
    smile = stroke("M24 33.5C28 39.5 36 39.5 40 33.5", HOLE, 3.2)
    return face + eyes + smile


@reg("xfce4-session", BLUE_GREY_DARK)
def xfce_session():
    flame = path("M28.5 39H35.5C35.5 43 34 46 32 48.5C30 46 28.5 43 28.5 39Z", DEEP_ORANGE_LIGHT)
    body = path("M32 11.5C38 16.5 40 24.5 38.5 38H25.5C24 24.5 26 16.5 32 11.5Z", INK)
    fins = (poly([(25.5, 29), (19, 36.5), (19, 42), (25.5, 38)], INK, 2) +
            poly([(38.5, 29), (45, 36.5), (45, 42), (38.5, 38)], INK, 2))
    window = circle(CX, 25, 3.8, HOLE)
    return flame + fins + body + window


@reg("xfce4-statusnotifier-plugin", PURPLE_LIGHT)
def xfce_statusnotifier():
    return (circle(CX, CY, 17.5, INK) + circle(CX, 21.5, 3, HOLE) +
            line(CX, 28, CX, 40, HOLE, 5))


def _panel(items):
    return cut("M17.5 14H46.5A4 4 0 0 1 50.5 18V42A4 4 0 0 1 46.5 46H17.5A4 4 0 0 1 13.5 42V18"
               "A4 4 0 0 1 17.5 14Z" + "M17 17.5V36H47V17.5Z", INK) + items


@reg("xfce4-systray", BLUE_DEEP)
def xfce_systray():
    return _panel("".join(circle(x, 41, 1.9, HOLE) for x in (35.5, 40.5, 45.5)))


@reg("xfce4-taskbar", BLUE_DEEP)
def xfce_taskbar():
    return _panel(rrect(17.5, 39, 9, 4, 1.5, HOLE) + rrect(28.5, 39, 9, 4, 1.5, HOLE))


@reg("xfe", INDIGO_LIGHT)
def xfe():
    back = path("M14 18A3 3 0 0 1 17 15H25.5L29.5 19H47A3 3 0 0 1 50 22V43A3 3 0 0 1 47 46H17"
                "A3 3 0 0 1 14 43Z", INK)
    return back + line(14.5, 25.5, 49.5, 25.5, HOLE, 2.4)


@reg("xfwm4", BLUE)
def xfwm4():
    back = rrect(25, 13.5, 25, 20, 3.5, INK) + rrect(28, 19, 19, 11.5, 1.5, HOLE)
    front = rrect(12.5, 24, 28.5, 24.5, 4.5, HOLE) + rrect(14, 25.5, 25.5, 21.5, 3.5, INK)
    x = stroke("M22.5 32L31 40.5M31 32L22.5 40.5", HOLE, 3.4)
    return back + front + x


@reg("xhydra", TEAL_DEEP)
def xhydra():
    body = path("M21 41C21 35.5 26 32 32 32C38 32 42 35 43 39.5L38 42.5H24Z", INK)
    tail = stroke("M40 41C45 41.5 48 44 45 47H50", INK, 3.6) + poly([(49, 44.2), (52, 47), (49, 49.8)], INK, 1.2)
    legs = stroke("M25 41L21.5 46.5M35 42L36 47", INK, 3.4)
    necks = stroke("M27 35C22 31 20 27 22.5 22M32 33C31 27 31.5 22 33.5 18M37 35C41.5 31 43.5 28 42 23.5", INK, 4)
    heads = (path("M25.5 20C24 17 21 16 18 17.5L13.5 20L18 21.5L15 23.5L20 24C23 24.5 26 23 25.5 20Z", INK) +
             path("M36.5 16C35 13 32 12 29 13.5L24.5 16L29 17.5L26 19.5L31 20C34 20.5 37 19 36.5 16Z", INK) +
             path("M39 21.5C40.5 18.5 43.5 17.5 46.5 19L51 21.5L46.5 23L49.5 25L44.5 25.5C41.5 26 38.5 24.5 39 21.5Z", INK))
    return tail + legs + body + necks + heads


@reg("xiaomitool", DEEP_ORANGE)
def xiaomitool():
    n = ('<path d="M17 46V18.5H31A5 5 0 0 1 36 23.5V46" fill="none" stroke="INK" '
         'stroke-width="5" stroke-linejoin="miter"/>')
    stem = rrect(24, 26, 5, 20, 0, INK)
    i = rrect(42, 16, 5, 30, 0, INK)
    return n + stem + i


@small("worldofpadman")
def worldofpadman_s():
    bubble = rrect(12.5, 14, 39, 29, 12, INK) + poly([(38, 40), (48, 48), (32, 42.5)], INK, 2)
    return bubble + stroke("M20 21L24.5 36L32 26L39.5 36L44 21", HOLE, 4)


@small("wps-office2019-kprometheus")
def wps2019_s():
    hexa = poly([pt(CX, CY, 18.5, -90 + 60 * k) for k in range(6)], INK, 4)
    return hexa + stroke("M21 23.5L26.5 38L32 28.5L37.5 38L43 23.5", HOLE, 4.4)


def _x_small(n):
    return (poly([(13, 13), (24, 13), (51, 47), (40, 47)], INK, 3) +
            poly([(43, 13), (51, 13), (24, 47), (16, 47)], INK, 2.5))


for _n, _d in [("x2-the-threat", "2"), ("x3-albion-prelude", "3"), ("x3-reunion", "3"),
               ("x3-terran-conflict", "3"), ("x4-foundations", "4")]:
    SMALL[_n] = (lambda d: lambda: _x_small(d))(_d)


@small("x2goclient")
def x2goclient_s():
    return (line(21, 16, 44, 44, INK, 6.5) + line(44, 16, 21, 44, INK, 4) +
            line(13, 25, 18, 25, INK, 3) + line(13, 35, 18, 35, INK, 3))


@small("xcos")
def xcos_s():
    box = rrect(13.5, 14.5, 37, 31, 4.5, INK)
    screen = rrect(17.5, 18.5, 19, 23, 2, HOLE)
    pulse = stroke("M19.5 31H22.5L25.5 25L29 36L31 31H34.5", INK, 3)
    return box + screen + pulse + circle(43.5, 24, 3.5, HOLE) + circle(43.5, 35, 3.5, HOLE)


@small("xfce-system-lock")
def xfce_lock_s():
    frame = rrect(13, 13.5, 38, 27.5, 4, INK) + rrect(17, 17.5, 30, 19.5, 2, HOLE)
    stand = rrect(22, 43, 20, 4.5, 2.25, INK)
    lock = (stroke("M28 27V24.5A4 4 0 0 1 36 24.5V27", INK, 3) + rrect(25.5, 26, 13, 9, 2, INK))
    return frame + stand + lock


@small("xfce4-cpugraph-plugin")
def xfce_cpugraph_s():
    frame = rrect(13, 13.5, 38, 27.5, 4, INK) + rrect(17, 17.5, 30, 19.5, 2, HOLE)
    stand = rrect(22, 43, 20, 4.5, 2.25, INK)
    return frame + stand + stroke("M19.5 28H24.5L27.5 21.5L31.5 34L34.5 28H44.5", INK, 3.2)


@small("xfce4-systray")
def xfce_systray_s():
    return _panel("".join(circle(x, 41, 2.3, HOLE) for x in (36, 42.5)))


@small("xfce4-taskbar")
def xfce_taskbar_s():
    return _panel(rrect(17.5, 38.5, 11, 5, 2, HOLE))


@small("xhydra")
def xhydra_s():
    body = path("M17 46C17 38.5 22 34 30 34C38 34 44 37.5 46.5 43.5C47.2 45.2 46 46.5 44.5 46.5H18"
                "C17.5 46.5 17 46.3 17 46Z", INK)
    necks = (stroke("M24 37C21 31 18 26 20.5 18", INK, 5) +
             stroke("M31 36C31 29 31 23 33 15", INK, 5) +
             stroke("M38 37C41 32 44 28 43 21", INK, 5))
    heads = circle(21, 17.5, 4, INK) + circle(33.5, 14.5, 4, INK) + circle(43.5, 20.5, 4, INK)
    return body + necks + heads


@small("wxglade")
def wxglade_s():
    frame = rrect(14, 14, 36, 32, 4.5, INK)
    return (frame + rrect(18, 18, 7, 7, 1.5, RED) + rrect(28, 18, 18, 7, 1.5, HOLE) +
            rrect(18, 28.5, 28, 13.5, 1.5, HOLE))


@small("xampp")
def xampp_s():
    rings = (circle(23, 20, 6, "none", f' stroke="{INK}" stroke-width="5.5"') +
             circle(41, 40, 6, "none", f' stroke="{INK}" stroke-width="5.5"'))
    band = stroke("M35 20A6 6 0 1 1 44.9 24.5L19.1 35.5A6 6 0 1 0 29 40", INK, 5.5)
    return rings + band


@small("wpscrackgui")
def wpscrackgui_s():
    ctr = (26, 38)
    arcs = ""
    for r in (9.5, 18):
        a, b = pt(*ctr, r, 225), pt(*ctr, r, 315)
        arcs += stroke(f"M{f(a[0])} {f(a[1])}A{r} {r} 0 0 1 {f(b[0])} {f(b[1])}", INK, 4.5)
    badge = circle(41, 38, 12.5, HOLE) + circle(41, 38, 10, INK)
    return arcs + circle(*ctr, 3.5, INK) + badge + circle(38, 38, 4, HOLE) + line(40, 38, 47, 38, HOLE, 3.5)


@small("xcas")
def xcas_s():
    out = "".join(line(CX, CY, *pt(CX, CY, 17, -90 + 60 * k), INK, 4.2) for k in range(6))
    return out + circle(CX, CY, 5, INK)


@small("xash3d")
def xash3d_s():
    ring = cut(cpath(CX, CY, 18) + cpath(CX, CY, 15), INK)
    return ring + stroke("M25 22L39 38M39 22L25 38", INK, 5)


@small("xenia")
def xenia_s():
    chip = poly([(32, 14), (51, 27.5), (32, 41), (13, 27.5)], INK, 3.5)
    pins = line(22.5, 35, 22.5, 42, INK, 4) + line(41.5, 35, 41.5, 42, INK, 4)
    return pins + chip + stroke("M24 23L40 32M40 23L24 32", HOLE, 4.2)


@small("xfce4-fsguard-plugin-warning")
def xfce_fsguard_w_s():
    card = rrect(14, 12.5, 25, 34, 5, INK)
    badge = circle(41, 39, 13, HOLE) + circle(41, 39, 10.5, RED)
    return card + badge + line(41, 33, 41, 39.5, INK, 4) + circle(41, 44.5, 2.2, INK)


@small("xfwm4")
def xfwm4_s():
    back = rrect(24, 12.5, 27, 22, 4, INK)
    front = rrect(11, 22, 31, 28, 5.5, HOLE) + rrect(13, 24, 27, 24, 4, INK)
    return back + front + stroke("M21.5 31L31.5 41M31.5 31L21.5 41", HOLE, 4)


@small("xiaomitool")
def xiaomitool_s():
    n = ('<path d="M16 47V17.5H30.5A5.5 5.5 0 0 1 36 23V47" fill="none" stroke="INK" '
         'stroke-width="6" stroke-linejoin="miter"/>')
    return n + rrect(23, 26, 6, 21, 0, INK) + rrect(42, 14.5, 6, 32.5, 0, INK)
