# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 70: tusk-app to urbanterror.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DARK, BLUE, BLUE_DEEP, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_SOFT,
    BLUE_LIGHT, BLUE_SOFT, BROWN, BROWN_DEEP, BROWN_SOFT, circle, CYAN_DEEP, DEEP_PURPLE,
    DEEP_PURPLE_LIGHT, f, g, GREY_DARK, GREY_DEEP, GREY_LIGHT, GREY_SOFT, HOLE, INDIGO_DARK,
    INDIGO_DEEP, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP, line, ORANGE, ORANGE_DARK, ORANGE_DEEP, path,
    PINK_DEEP, poly, pt, PURPLE, PURPLE_DEEP, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT,
    RED_SOFT, rrect, stroke, TEAL_LIGHT,
)
from glyphs.kit import arc, gear_m, registry, ring_b

ICONS, SMALL, reg, small = registry()


def hexa(cx, cy, r, start=-90):
    return [pt(cx, cy, r, start + 60 * k) for k in range(6)]


def _tux(body=INK, belly=HOLE, feet=AMBER):
    return (path("M32 12C38 12 41 17 41 23C41 26 42 28 44.5 32C47.5 37 48 41 46 43.5"
                 "L18 43.5C16 41 16.5 37 19.5 32C22 28 23 26 23 23C23 17 26 12 32 12Z", body)
            + path("M32 25C37.5 25 41 31 41 37C41 41.5 37 44 32 44C27 44 23 41.5 23 37"
                   "C23 31 26.5 25 32 25Z", belly)
            + circle(28.5, 19.5, 2.4, belly) + circle(35.5, 19.5, 2.4, belly)
            + circle(29, 20, 1.1, body) + circle(35, 20, 1.1, body)
            + path("M27.5 23.5C29.5 22 34.5 22 36.5 23.5C35.5 26 33.5 27 32 27"
                   "C30.5 27 28.5 26 27.5 23.5Z", feet)
            + path("M17.5 46C17.5 43 20 41.5 23 42L29 45C29.5 47.5 27 48.5 24 48Z", feet)
            + path("M46.5 46C46.5 43 44 41.5 41 42L35 45C34.5 47.5 37 48.5 40 48Z", feet))


@reg("tux", GREY_LIGHT)
def tux():
    return _tux()


@reg("tuxpuck", BLUE_GREY_SOFT)
def tuxpuck():
    return _tux(BLUE_GREY_DARK, INK)


@reg("tuxmath", RED)
def tuxmath():
    sums = line(26.5, 36, 30, 36, INK, 2.4) + stroke("M33.5 32.5L36 31V41", INK, 2.4)
    return _tux() + sums


@reg("tuxtype", RED_DEEP)
def tuxtype():
    a = ring_b(31, 36.5, 3.4, INK, 2.4) + line(34.4, 32.5, 34.4, 40.5, INK, 2.4)
    return _tux() + a


@reg("tuxguitar", BROWN)
def tuxguitar():
    neck = line(30, 37, 47, 24, AMBER, 2.6)
    body = (circle(25.5, 39.5, 5.8, AMBER) + circle(30.5, 35.5, 4.4, AMBER)
            + circle(27, 38.3, 1.9, HOLE))
    head = g(rrect(45, 21.5, 5, 3.4, 1.2, AMBER), "rotate(-37 47.5 23.2)")
    return _tux() + neck + body + head


@reg("tuxpaint", BLUE_LIGHT)
def tuxpaint():
    handle = line(38, 40, 48.5, 25, PINK_DEEP, 3.2)
    tip = path("M36 38.5C38 38 40 39.5 39.8 41.5C38.8 44.5 35.5 45.5 33 45"
               "C34.5 43.5 34 40 36 38.5Z", INK, f' stroke="{HOLE}" stroke-width="1.2"')
    return _tux() + handle + tip


@reg("tuxcut", BLUE_GREY_DARK)
def tuxcut():
    out = ""
    for s in (1, -1):
        m = "" if s == 1 else "translate(64 0) scale(-1 1)"
        blade = line(20, 14, 38.5, 38, INK, 2.6)
        hilt = line(39.5, 39.5, 44.5, 46, INK, 4)
        guard = line(35, 41.5, 41.5, 36.5, INK, 2.6)
        out += g(blade + hilt + guard, m) if m else blade + hilt + guard
    return out


@reg("tuxedo-control-center", GREY_DARK)
def tuxedo_cc():
    swing = stroke(arc(32, 30, 17, 118, 262), RED, 3.6)
    z = stroke("M22.5 18H43.5L25 41.5H46", INK, 4)
    return swing + z + line(29, 23, 38.5, 36.5, INK, 3.6)


@reg("tuxedo-webfai-creator", RED_DEEP)
def tuxedo_webfai():
    plug = (rrect(25, 11, 14, 9, 2, INK) + rrect(28, 13.5, 2.8, 2.8, 0.6, HOLE)
            + rrect(33.2, 13.5, 2.8, 2.8, 0.6, HOLE))
    body = rrect(18, 19, 28, 30, 5.5, INK)
    loop = stroke(arc(32, 34.5, 7, 200, 520 - 50), HOLE, 3.2)
    head = poly([(22.5, 31.5), (26, 27.5), (29, 32.5)], HOLE, 1.5)
    return plug + body + loop + head


@reg("tvtime", GREY_DARK)
def tvtime():
    return (rrect(14, 14, 36, 27, 4, INK) + rrect(18, 18, 28, 19, 2, HOLE)
            + rrect(25, 43.5, 14, 3.6, 1.8, INK))


@reg("tw.ddnet.ddnet", ORANGE_DEEP)
def ddnet():
    body = circle(32, 28, 15, INK)
    eyes = (path("M28 21.5a2.3 4.2 0 1 0 0.01 0Z", HOLE) +
            path("M36 21.5a2.3 4.2 0 1 0 0.01 0Z", HOLE))
    feet = (path("M17 44.5C17 41 21 39.5 25.5 39.5C30 39.5 32 41.5 32 44C32 46.5 29 47.5 25 47.5"
                 "C20.5 47.5 17 46.5 17 44.5Z", BROWN_DEEP) +
            path("M32 44.5C32 41 36 39.5 40.5 39.5C45 39.5 47 41.5 47 44C47 46.5 44 47.5 40 47.5"
                 "C35.5 47.5 32 46.5 32 44.5Z", BROWN_DEEP))
    return body + eyes + feet


_BIRD = ("M49 18.5C47.8 19 46.6 19.4 45.3 19.5C46.6 18.7 47.6 17.5 48 16"
         "C46.8 16.7 45.4 17.2 44 17.5C42.8 16.2 41.1 15.5 39.3 15.5"
         "C35.7 15.5 32.8 18.4 32.8 22C32.8 22.5 32.9 23 33 23.5"
         "C27.6 23.2 22.9 20.7 19.7 16.8C19.1 17.8 18.8 18.9 18.8 20.1"
         "C18.8 22.3 19.9 24.3 21.7 25.5C20.6 25.5 19.6 25.2 18.8 24.7V24.8"
         "C18.8 28 21 30.6 24 31.2C23.4 31.3 22.9 31.4 22.3 31.4"
         "C21.9 31.4 21.5 31.4 21.1 31.3C21.9 33.9 24.4 35.8 27.2 35.9"
         "C25 37.6 22.2 38.7 19.1 38.7C18.6 38.7 18 38.7 17.5 38.6"
         "C20.4 40.5 23.8 41.5 27.4 41.5C39.3 41.5 45.8 31.7 45.8 23.2V22.4"
         "C47 21.4 48.2 20.1 49 18.5Z")


def _bird(colour, cx=32, cy=30, k=1.0):
    return g(path(_BIRD, colour), f"translate({f(cx)} {f(cy)}) scale({f(k)}) translate(-33.25 -28.5)")


@reg("twitter", LIGHT_BLUE)
def twitter():
    return _bird(INK, k=1.12)


@reg("tweetdeck", BLUE_DEEP)
def tweetdeck():
    bubble = rrect(14, 14, 36, 28, 6, INK) + poly([(27, 40), (37, 40), (32, 46.5)], INK, 2)
    return bubble + _bird(HOLE, 32, 28.5, 0.72)


@reg("tweet-tray", BLUE)
def tweet_tray():
    feather = path("M46 13C33.5 14 22.5 23.5 21.5 38C24.5 32.5 29.5 30 35.5 29"
                   "C32 28.3 29.5 27.8 28.5 27.5C34.5 25 42 23.5 46 13Z", INK)
    return feather + line(22.5, 36, 18, 46, INK, 2.8)


@reg("twitter-x", BLUE_GREY_DARK)
def twitter_x():
    band = poly([(16, 14), (24.5, 14), (48, 46), (39.5, 46)], INK, 2)
    slit = line(20.5, 16, 43.5, 44, HOLE, 1.8)
    thin = line(46, 14.5, 35.8, 26, INK, 3) + line(28.5, 34, 18, 45.5, INK, 3)
    return band + slit + thin


@reg("twinkle", DEEP_PURPLE_LIGHT)
def twinkle():
    pts = [pt(32, 31, 17.5 if k % 2 == 0 else 8, -90 + 36 * k) for k in range(10)]
    return poly(pts, INK, 3.5) + circle(32, 32, 5.2, HOLE)


@reg("twupic", GREY_DARK)
def twupic():
    hx = poly(hexa(32, 30, 17.5, -90), INK, 4)
    inf = stroke("M32 30C29 26 27 24.5 24.5 24.5A5.5 5.5 0 0 0 24.5 35.5C27 35.5 29 34 32 30"
                 "C35 26 37 24.5 39.5 24.5A5.5 5.5 0 0 1 39.5 35.5C37 35.5 35 34 32 30Z", HOLE, 3.2)
    return hx + inf


@reg("type-rider", CYAN_DEEP)
def type_rider():
    ramp = poly([(14, 40), (47, 22), (47, 29.5), (14, 47)], INK, 2)
    riders = circle(24, 30.5, 4.3, INK) + circle(33.5, 25.5, 4.3, INK)
    star = "".join(line(*pt(44, 15, 3.8, a), *pt(44, 15, -3.8, a), INK, 2.2) for a in (90, 30, 150))
    return ramp + riders + star


@reg("typecatcher", GREY_DEEP)
def typecatcher():
    cloud = (circle(23.5, 32, 8, INK) + circle(34, 25.5, 10.5, INK) + circle(42.5, 33, 7, INK)
             + rrect(15.5, 30, 34, 13, 6.5, INK))
    a = stroke("M28 41V32A4 4 0 0 1 36 32V41M28 36H36", HOLE, 3)
    return cloud + a


@reg("typora", GREY_SOFT)
def typora():
    return (rrect(17, 14, 30, 5, 1, INK) + rrect(17, 14, 4, 10, 1.2, INK)
            + rrect(43, 14, 4, 10, 1.2, INK) + rrect(29.3, 14, 5.4, 31, 1, INK)
            + rrect(24, 42, 16, 4.2, 1.2, INK))


@reg("ubiquity-kde", GREY_DEEP)
def ubiquity():
    arrow = rrect(28.5, 12, 7, 14, 1.5, INK) + poly([(21, 25), (43, 25), (32, 36)], INK, 2.5)
    track = line(19, 43.5, 45, 43.5, INK, 2.6)
    knobs = circle(19.5, 43.5, 3.6, INK) + circle(30, 43.5, 3.6, INK) + ring_b(44, 43.5, 2.8, INK, 2.2)
    return arrow + track + knobs


@reg("ubuntu-tweak", AMBER_DARK)
def ubuntu_tweak():
    arcs = "".join(stroke(arc(32, 30, 16, a + 18, a + 102), INK, 3.4) for a in (-90, 30, 150))
    return arcs + gear_m(32, 30, 9.5, INK, HOLE, 8, 3.6)


@reg("ubuntustudio-controls", BLUE_GREY_DARK)
def ubuntustudio():
    return (circle(32, 30, 4, INK) + stroke(arc(32, 30, 9.5, -60, 215), INK, 3.4)
            + stroke(arc(32, 30, 15.5, -80, 190), INK, 3.4)
            + stroke(arc(32, 30, 15.5, 205, 240), INK, 3.4)
            + stroke(arc(32, 30, 9.5, 232, 262), INK, 3.4))


@reg("ue4editor", INDIGO_DARK)
def ue4():
    rim = ring_b(32, 30, 16.5, INK, 2.6)
    u = stroke("M25.5 22V33C25.5 36.5 28 38.5 31 38.5C33.5 38.5 35 37.5 36.5 35.5", INK, 4.2)
    stem = line(38.5, 20.5, 38.5, 39.5, INK, 4.2)
    flag = poly([(21.5, 23.5), (27.5, 19), (27.5, 24)], INK, 1.5)
    return rim + u + stem + flag


@reg("uget", PURPLE_SOFT)
def uget():
    box = stroke("M47 21V20C47 16.5 45 14.5 41.5 14.5H30C26.5 14.5 24.5 16.5 24.5 20V42"
                 "C24.5 45.5 26.5 47.5 30 47.5H41.5C45 47.5 47 45.5 47 42", INK, 4)
    hook = stroke("M16 22V34C16 37 17.5 39 20.5 39H24", INK, 4)
    arrow = rrect(33.5, 20, 7, 12, 1.2, INK) + poly([(29, 31), (45, 31), (37, 41)], INK, 2)
    return box + hook + arrow


@reg("uk.me.doof.Lander", RED_DEEP)
def lander():
    ship = path("M32 11.5C35.5 14 37.5 18.5 37.5 24V30L48 39.5V44L37.5 40.5L36.5 44H27.5L26.5 40.5"
                "L16 44V39.5L26.5 30V24C26.5 18.5 28.5 14 32 11.5Z", INK)
    cockpit = stroke("M29.8 29V24.5A2.2 2.2 0 0 1 34.2 24.5V29", HOLE, 2.4)
    return ship + cockpit + rrect(28.5, 45.5, 7, 3.2, 1.6, INK)


@reg("ukuu", BROWN_SOFT)
def ukuu():
    a1 = stroke(arc(32, 30, 12, 195, 320), INK, 4.2)
    a2 = stroke(arc(32, 30, 12, 15, 140), INK, 4.2)
    h1 = poly([(38, 17.5), (47.5, 20.5), (40.5, 27)], INK, 2)
    h2 = poly([(26, 42.5), (16.5, 39.5), (23.5, 33)], INK, 2)
    return a1 + a2 + h1 + h2


@reg("ulauncher", BLUE_DEEP)
def ulauncher():
    right = stroke("M32 43.5A10.5 10.5 0 0 0 42.5 33V13.5", BLUE_SOFT, 6.5)
    left = stroke("M21.5 17.5V33A10.5 10.5 0 0 0 32 43.5", INK, 6.5)
    return right + left


@reg("umbrello", RED_DEEP)
def umbrello():
    man = (circle(20, 16.5, 4, INK) + line(20, 20, 20, 31, INK, 2.6) + line(14.5, 24.5, 25.5, 24.5, INK, 2.6)
           + stroke("M15 39L20 31L25 39", INK, 2.6))
    link = line(23.5, 19.5, 38, 35, INK, 2.6)
    oval = path("M40 34.5a8.5 5.5 0 1 0 0.01 0Z", INK)
    return man + link + g(oval, "translate(0 0)")


@reg("umlet_logo", RED_DEEP)
def umlet():
    return ring_b(32, 30, 13.5, INK, 6) + rrect(13, 26, 38, 8, 2.5, INDIGO_DEEP)


@reg("ums", LIGHT_BLUE_DEEP)
def ums():
    orb = (g(path("M32 23.5a15.5 6.5 0 1 0 0.01 0Z", "none",
                  f' stroke="{INK}" stroke-width="2.6"'), "rotate(35 32 30)")
           + g(path("M32 23.5a15.5 6.5 0 1 0 0.01 0Z", "none",
                    f' stroke="{INK}" stroke-width="2.6"'), "rotate(-35 32 30)"))
    dots = circle(32, 30, 3.4, INK) + circle(*pt(32, 30, 15.5, 35), 3, INK) + circle(*pt(32, 30, 15.5, 145), 3, INK)
    return orb + dots


@reg("unciv", BLUE_GREY_DARK)
def unciv():
    d = 11.2
    out = poly(hexa(32, 30, 5.4, -90), INK, 1.5)
    for k in range(6):
        cx, cy = pt(32, 30, d, 60 * k)
        out += poly(hexa(cx, cy, 5.4, -90), INK if k % 2 == 0 else BLUE_GREY_SOFT, 1.5)
    return out


@reg("undertale", BLUE_GREY_DARK)
def undertale():
    rows = [".XX.XX.", "XXXXXXX", "XXXXXXX", ".XXXXX.", "..XXX..", "...X..."]
    p, x0, y0 = 5, 14.5, 15
    out = ""
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            if row[c] == "X":
                s = c
                while c < len(row) and row[c] == "X":
                    c += 1
                out += rrect(x0 + s * p, y0 + r * p, (c - s) * p, p + 0.05, 0, RED)
            else:
                c += 1
    return out


@reg("unison-gtk", ORANGE_DEEP)
def unison():
    u = stroke("M23 24V33A9 9 0 0 0 41 33V24", INK, 6)
    heads = (poly([(16.5, 25), (29.5, 25), (23, 14.5)], INK, 2)
             + poly([(34.5, 25), (47.5, 25), (41, 14.5)], INK, 2))
    return u + heads


def _unity(k=1.0):
    r = 16.5
    hx = hexa(32, 30.5, r, -90)
    outline = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hx) + "Z", INK, 4.2 * k)
    y = "".join(line(32, 30.5, *hx[i], INK, 4.2 * k) for i in (1, 3, 5))
    return outline + y


@reg("unityhub", GREY_SOFT)
@reg("unity-editor-icon", BLUE_GREY_DARK)
def unity_editor():
    return _unity()


@reg("unity-tweak-tool", PURPLE_DEEP)
def unity_tweak():
    u = stroke("M20.5 15V29A8.5 8.5 0 0 0 37.5 29V15", INK, 6.5)
    badge = circle(40.5, 39, 10.5, HOLE) + gear_m(40.5, 39, 8.5, INK, HOLE, 8, 3)
    return u + badge


@reg("unknown-horizons", BLUE_GREY_DEEP)
def unknown_horizons():
    hull = path("M13.5 37.5H50.5C49 42.5 45.5 45.5 40 45.5H22C18 45.5 15 42 13.5 37.5Z", INK)
    mast = line(33, 14, 33, 37, INK, 2.2)
    sail1 = path("M31 17C24.5 22 21.5 28.5 22 35H31Z", INK)
    sail2 = path("M35 19C40.5 23 44 28.5 44 35H35Z", INK)
    flag = poly([(34, 12), (41.5, 14.5), (34, 17)], RED_SOFT, 1)
    return hull + mast + sail1 + sail2 + flag


@reg("uno-calculator", BLUE_DEEP)
def uno_calc():
    plus = line(18.5, 21.5, 29.5, 21.5, INK, 3.6) + line(24, 16, 24, 27, INK, 3.6)
    minus = line(34.5, 21.5, 45.5, 21.5, INK, 3.6)
    times = line(20, 34, 28, 42, INK, 3.6) + line(28, 34, 20, 42, INK, 3.6)
    eq = line(34.5, 35, 45.5, 35, INK, 3.6) + line(34.5, 41, 45.5, 41, INK, 3.6)
    return plus + minus + times + eq


@reg("unsplash", BLUE_GREY_DARK)
def unsplash():
    return rrect(25.5, 13.5, 13, 9, 1, INK) + path("M16 29H25.5V37.5H38.5V29H48V46.5H16Z", INK,
                                                  f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')


@reg("unturned", ORANGE_DARK)
def unturned():
    eyes = rrect(17, 24, 7, 5, 1, INK) + rrect(40, 24, 7, 5, 1, INK)
    mouth = rrect(18, 34, 28, 7, 1.5, INK) + rrect(24, 31, 16, 4.5, 1, RED)
    teeth = rrect(23, 36, 3.5, 2.8, 0.5, HOLE) + rrect(30.25, 36, 3.5, 2.8, 0.5, HOLE) + rrect(37.5, 36, 3.5, 2.8, 0.5, HOLE)
    return eyes + mouth + teeth


@reg("uplink", INDIGO_DEEP)
def uplink():
    frame = rrect(15, 17, 34, 30, 7, INK) + rrect(20, 22, 24, 20, 4, HOLE)
    tab = rrect(26.5, 12, 11, 9, 2.5, INK)
    u = stroke("M26.5 22V31.5A5.5 5.5 0 0 0 37.5 31.5V22", INK, 4)
    return frame + tab + u


@reg("upload-pictures", RED_LIGHT)
def upload_pictures():
    frame = rrect(13, 14, 32, 26, 4, INK)
    scene = poly([(16.5, 36.5), (24, 28), (29, 33), (33, 29.5), (41.5, 36.5)], HOLE, 1.5) + circle(37, 20.5, 3.2, HOLE)
    badge = circle(42, 40, 10.5, HOLE) + circle(42, 40, 8.5, INK)
    arrow = line(42, 44.5, 42, 36.5, HOLE, 3) + stroke("M38 39.5L42 35.5L46 39.5", HOLE, 3)
    return frame + scene + badge + arrow


@reg("upscayl", BLUE_DEEP)
def upscayl():
    px = "".join(rrect(15 + c * 5.5, 16 + r * 5.5, 4.5, 4.5, 1, BLUE_SOFT)
                 for r in range(5) for c in range(2) if (r + c) % 2 == 0)
    bar = line(32, 12.5, 32, 47.5, INK, 3)
    knob = circle(32, 30, 8.5, INK)
    arrows = (poly([(26.5, 30), (30.5, 26.5), (30.5, 33.5)], HOLE, 1)
              + poly([(37.5, 30), (33.5, 26.5), (33.5, 33.5)], HOLE, 1))
    right = stroke("M36 16H44A4 4 0 0 1 48 20V40A4 4 0 0 1 44 44H36", INK, 2.6)
    return px + right + bar + knob + arrows


@reg("upsource", DEEP_PURPLE)
def upsource():
    box = rrect(16, 14, 32, 32, 2.5, INK)
    u = stroke("M21 20.5V27.5A3.5 3.5 0 0 0 28 27.5V20.5", HOLE, 3)
    p = stroke("M32.5 32V20.5H36.5A3 3 0 0 1 36.5 26.5H32.5", HOLE, 3)
    return box + u + p + rrect(21, 38, 12, 3.2, 0.6, HOLE)


@reg("upwork", ORANGE_DEEP)
def upwork():
    u = stroke("M14.5 21V30A5.5 5.5 0 0 0 25.5 30V21", INK, 4.4)
    link = stroke("M25.5 23C28.5 28 31.5 31.5 36 32.5", INK, 4)
    p = ring_b(42, 29, 6.3, INK, 4.2) + line(35.7, 29, 34, 44, INK, 4.4)
    return u + link + p


@reg("uqm", PURPLE)
def uqm():
    ship = (rrect(15, 26, 34, 8, 3, INK) + rrect(19, 17, 6, 26, 2.5, INK) + rrect(39, 17, 6, 26, 2.5, INK))
    tips = (rrect(19, 14, 6, 5, 2, ORANGE) + rrect(19, 41, 6, 5, 2, ORANGE)
            + rrect(39, 14, 6, 5, 2, ORANGE) + rrect(39, 41, 6, 5, 2, ORANGE))
    core = rrect(28.5, 27.5, 7, 5, 1.5, HOLE)
    return g(ship + tips + core, "rotate(-45 32 30)")


@reg("urbanterror", BLUE_DEEP)
def urbanterror():
    out = ""
    for a, x in ((-22, 21), (0, 32), (22, 43)):
        card = rrect(x - 4, 16, 8, 24, 2.5, INK) + rrect(x - 2.2, 19, 4.4, 14, 1, HOLE)
        out += g(card + rrect(x - 4, 42, 8, 3.4, 1.4, INK), f"rotate({a} {x} 30)")
    return out


@reg("tusk-app", TEAL_LIGHT)
def tusk():
    return rrect(20, 18, 24, 24, 6, INK)


@reg("tutanota-desktop", RED_DARK)
def tutanota():
    road = path("M41 12.5C44.5 17 38 20 30.5 21C23.5 22 20.5 24 23 27C26.5 31 38 31.5 38 37.5"
                "C38 42 29 45 15 47.5H28C38.5 46.5 46 42.5 45 36.5C44 30.5 32.5 28.5 30 26.5"
                "C28.5 25 35.5 24 39.5 22C43.5 20 43.5 15.5 41 12.5Z", INK)
    return road


def _tux_s(body=INK, belly=HOLE, feet=AMBER):
    return (path("M32 11C38.5 11 41.5 16.5 41.5 23C41.5 26 43 28.5 45.5 32.5C48.5 37.5 48.5 41.5 46.5 44"
                 "L17.5 44C15.5 41.5 15.5 37.5 18.5 32.5C21 28.5 22.5 26 22.5 23C22.5 16.5 25.5 11 32 11Z", body)
            + path("M32 26C38 26 41.5 32 41.5 37.5C41.5 42 37.5 45 32 45C26.5 45 22.5 42 22.5 37.5"
                   "C22.5 32 26 26 32 26Z", belly)
            + path("M26.5 22C29 20.5 35 20.5 37.5 22C36.5 25 34 26.5 32 26.5C30 26.5 27.5 25 26.5 22Z", feet)
            + path("M16.5 46.5C16.5 43 19.5 41.5 23 42L30 45.5C30.5 48.5 27.5 49.5 24 49Z", feet)
            + path("M47.5 46.5C47.5 43 44.5 41.5 41 42L34 45.5C33.5 48.5 36.5 49.5 40 49Z", feet))


@small("tux")
def tux_s():
    return _tux_s()


@small("tuxpuck")
def tuxpuck_s():
    return _tux_s(BLUE_GREY_DARK, INK)


@small("tuxmath")
def tuxmath_s():
    return _tux_s() + line(25.5, 37, 29.5, 37, INK, 3) + stroke("M33.5 33L36.5 31.5V42", INK, 3)


@small("tuxtype")
def tuxtype_s():
    return _tux_s() + ring_b(30.5, 37.5, 3.8, INK, 3) + line(34.5, 33, 34.5, 42, INK, 3)


@small("tuxguitar")
def tuxguitar_s():
    return (_tux_s() + line(30, 37, 47, 24, AMBER, 3.4) + circle(25.5, 39.5, 6.5, AMBER)
            + circle(31, 35, 4.8, AMBER))


@small("tuxpaint")
def tuxpaint_s():
    return _tux_s() + line(35, 43, 48.5, 24, PINK_DEEP, 4)


@small("tuxcut")
def tuxcut_s():
    return line(19, 14, 45, 46, INK, 4) + line(45, 14, 19, 46, INK, 4)


@small("tuxedo-control-center")
def tuxedo_cc_s():
    return (stroke(arc(32, 30, 18, 125, 255), RED, 4.4)
            + stroke("M21.5 16.5H44L24.5 43H47", INK, 5))


@small("tuxedo-webfai-creator")
def tuxedo_webfai_s():
    plug = rrect(25, 10, 14, 10, 2, INK)
    body = rrect(17, 18, 30, 31, 6, INK)
    loop = stroke(arc(32, 34, 8, 200, 470), HOLE, 4)
    head = poly([(20.5, 31.5), (25, 26.5), (28.5, 32.5)], HOLE, 1.5)
    return plug + body + loop + head


@small("tweetdeck")
def tweetdeck_s():
    bubble = rrect(12, 12, 40, 31, 7, INK) + poly([(26, 41), (38, 41), (32, 48)], INK, 2)
    return bubble + _bird(HOLE, 32, 27.5, 0.88)


@small("twupic")
def twupic_s():
    hx = poly(hexa(32, 30, 18, -90), INK, 4)
    inf = stroke("M32 30C29 25.5 27 24 24 24A6 6 0 0 0 24 36C27 36 29 34.5 32 30"
                 "C35 25.5 37 24 40 24A6 6 0 0 1 40 36C37 36 35 34.5 32 30Z", HOLE, 4)
    return hx + inf


@small("typecatcher")
def typecatcher_s():
    cloud = (circle(23, 32, 8.5, INK) + circle(34, 25, 11, INK) + circle(43, 33, 7.5, INK)
             + rrect(14.5, 30, 36, 14, 7, INK))
    return cloud + stroke("M27 42V32A5 5 0 0 1 37 32V42M27 37H37", HOLE, 4)


@small("ubuntu-tweak")
def ubuntu_tweak_s():
    arcs = "".join(stroke(arc(32, 30, 17, a + 22, a + 98), INK, 3.6) for a in (-90, 30, 150))
    return arcs + gear_m(32, 30, 10.5, INK, HOLE, 6, 4)


@small("ubuntustudio-controls")
def ubuntustudio_s():
    return (circle(32, 30, 5, INK) + stroke(arc(32, 30, 15, -70, 200), INK, 4.4))


@small("ue4editor")
def ue4_s():
    u = stroke("M23.5 18V33C23.5 38 27 41 31 41C34 41 36 39.5 37.5 37", INK, 5)
    return ring_b(32, 30, 17.5, INK, 3) + u + line(40, 17, 40, 42, INK, 5)


@small("uget")
def uget_s():
    box = stroke("M46 21V20C46 16 44 14 40 14H24C20 14 18 16 18 20V41C18 45 20 47 24 47H40"
                 "C44 47 46 45 46 41", INK, 4.4)
    arrow = rrect(28.5, 18, 7, 13, 1.5, INK) + poly([(23, 29), (41, 29), (32, 40)], INK, 2.5)
    return box + arrow


@small("umbrello")
def umbrello_s():
    man = (circle(20, 17, 5, INK) + line(20, 21, 20, 32, INK, 3.4) + stroke("M14.5 40.5L20 32L25.5 40.5", INK, 3.4))
    return man + line(24, 20, 38, 35, INK, 3.4) + path("M41 33.5a9 6.5 0 1 0 0.01 0Z", INK)


@small("upload-pictures")
def upload_pictures_s():
    frame = rrect(12, 13, 32, 26, 4, INK)
    scene = poly([(15.5, 35.5), (23, 26), (31, 35.5)], HOLE, 1.5)
    badge = circle(42, 39.5, 11.5, HOLE) + circle(42, 39.5, 9.5, INK)
    arrow = line(42, 45, 42, 35.5, HOLE, 3.6) + stroke("M37.5 39L42 34.5L46.5 39", HOLE, 3.6)
    return frame + scene + badge + arrow


@small("upscayl")
def upscayl_s():
    px = "".join(rrect(14 + c * 7, 15 + r * 7, 6, 6, 1, BLUE_SOFT)
                 for r in range(5) for c in range(2) if (r + c) % 2 == 0)
    return (px + line(32, 11, 32, 49, INK, 3.6) + circle(32, 30, 10, INK)
            + poly([(25.5, 30), (30.5, 25.5), (30.5, 34.5)], HOLE, 1)
            + poly([(38.5, 30), (33.5, 25.5), (33.5, 34.5)], HOLE, 1))


@small("upsource")
def upsource_s():
    box = rrect(15, 13, 34, 34, 3, INK)
    u = stroke("M20.5 20V28A4 4 0 0 0 28.5 28V20", HOLE, 4)
    p = stroke("M33 34V20H37A3.8 3.8 0 0 1 37 27.5H33", HOLE, 4)
    return box + u + p + rrect(20, 38.5, 13, 4, 1, HOLE)


@small("urbanterror")
def urbanterror_s():
    out = ""
    for a, x in ((-22, 20.5), (0, 32), (22, 43.5)):
        out += g(rrect(x - 4.5, 15, 9, 31, 3, INK), f"rotate({a} {x} 30)")
    return out
