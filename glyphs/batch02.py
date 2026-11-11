# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 2: numbered apps, 4K tools and the Adobe letter marks.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette. Letters and digits are round-capped strokes
from the small stroke alphabet below, never text.
"""
import math
from lm import (
    AMBER_DARK, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_LIGHT,
    BLUE_SOFT, BROWN, BROWN_DARK, BROWN_DEEP, circle, cpath, cut, CX, CY, CYAN_DARK, CYAN_DEEP,
    DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_ORANGE_SOFT, DEEP_PURPLE,
    DEEP_PURPLE_DARK, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_DEEP, HOLE,
    INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_SOFT, INK, LIGHT_BLUE, line, ORANGE_DARK,
    ORANGE_DEEP, path, PINK_DEEP, poly, pt, PURPLE, PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED,
    RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke, TEAL, TEAL_DEEP, YELLOW_DARK,
)
from glyphs.kit import registry

ICONS, SMALL, reg, small = registry()


_GLYPHS = {
    "A": (14, "M0 0L7 -22L14 0M3.2 -7.5H10.8"),
    "B": (12, "M0 0V-22H6A5.2 5.2 0 0 1 6 -11.6H0M6 -11.6H6.4A5.8 5.8 0 0 1 6.4 0H0Z"),
    "C": (12.5, "M12.5 -19C11 -21 9.2 -22 7.2 -22C2.8 -22 0 -17.5 0 -11"
                "C0 -4.5 2.8 0 7.2 0C9.2 0 11 -1 12.5 -3"),
    "D": (13, "M0 0V-22H5C10 -22 13 -17.5 13 -11C13 -4.5 10 0 5 0Z"),
    "E": (11, "M11 -22H0V0H11M0 -11H9"),
    "F": (11, "M11 -22H0V0M0 -11H9"),
    "I": (0, "M0 0V-22"),
    "K": (12, "M0 -22V0M12 -22L1.5 -10M5.5 -13.5L12 0"),
    "L": (10, "M0 -22V0H10"),
    "M": (16, "M0 0V-22L8 -8L16 -22V0"),
    "O": (13, "M6.5 -22C2.8 -22 0 -17.5 0 -11C0 -4.5 2.8 0 6.5 0"
              "C10.2 0 13 -4.5 13 -11C13 -17.5 10.2 -22 6.5 -22Z"),
    "P": (12, "M0 0V-22H6A6 6 0 0 1 6 -10H0"),
    "T": (13, "M0 -22H13M6.5 -22V0"),
    "b": (12, "M0 -22V0M0 -7.5A6 7.5 0 1 0 12 -7.5A6 7.5 0 1 0 0 -7.5"),
    "c": (10, "M10 -12.5C9 -14.2 7.5 -15 5.8 -15C2.3 -15 0 -12 0 -7.5"
              "C0 -3 2.3 0 5.8 0C7.5 0 9 -0.8 10 -2.5"),
    "d": (12, "M12 -22V0M12 -7.5A6 7.5 0 1 0 0 -7.5A6 7.5 0 1 0 12 -7.5"),
    "e": (12, "M0.5 -7.5H12C12 -12 9.5 -15 6 -15C2.5 -15 0 -12 0 -7.5"
              "C0 -3 2.5 0 6.3 0C8.5 0 10.3 -0.8 11.5 -2.3"),
    "h": (11, "M0 0V-22M0 -9.5C0 -13 2.5 -15 5.5 -15C9 -15 11 -13 11 -9.5V0"),
    "i": (0, "M0 0V-14", [(0, -21)]),
    "l": (0, "M0 -22V0"),
    "n": (11, "M0 0V-15M0 -9.5C0 -13 2.5 -15 5.5 -15C9 -15 11 -13 11 -9.5V0"),
    "r": (8, "M0 0V-15M0 -8.5C0 -12.5 3 -15 8 -15"),
    "s": (10, "M9.8 -13C8.8 -14.4 7.2 -15 5.2 -15C2.5 -15 0.4 -13.5 0.4 -11"
              "C0.4 -5.5 10 -9.5 10 -4C10 -1.5 8 0 5 0C3 0 1.2 -0.8 0 -2.2"),
    "u": (11, "M0 -15V-5.5C0 -2 2.2 0 5.5 0C8.8 0 11 -2 11 -5.5M11 -15V0"),
    "w": (16, "M0 -15L3.8 0L8 -11L12.2 0L16 -15"),
    "0": (12, "M6 -22C2.5 -22 0 -17.5 0 -11C0 -4.5 2.5 0 6 0"
              "C9.5 0 12 -4.5 12 -11C12 -17.5 9.5 -22 6 -22Z"),
    "1": (6, "M0 -17L6 -22V0"),
    "2": (12, "M0.5 -17C1.5 -20.5 4 -22 6.5 -22C9.5 -22 12 -20 12 -16.5C12 -12 6 -7 0 0H12"),
    "4": (13, "M9.5 0V-22L0 -6H13"),
    "6": (12, "M10.5 -20.8C9.5 -21.6 8 -22 6.5 -22C2.5 -22 0 -17 0 -10C0 -3.5 2.5 0 6 0"
              "C9.5 0 12 -2.5 12 -6.5C12 -10.5 9.5 -13 6 -13C3 -13 0.8 -11.2 0 -8.5"),
    "7": (12, "M0 -22H12L4 0"),
    "8": (12, "M6 -11.6C2.8 -11.6 0.6 -13.8 0.6 -16.8C0.6 -19.8 3 -22 6 -22"
              "C9 -22 11.4 -19.8 11.4 -16.8C11.4 -13.8 9.2 -11.6 6 -11.6Z"
              "M6 -11.6C2.5 -11.6 0 -9.2 0 -5.8C0 -2.4 2.5 0 6 0"
              "C9.5 0 12 -2.4 12 -5.8C12 -9.2 9.5 -11.6 6 -11.6Z"),
}


def word(text, colour=INK, base=41, h=22, sw=4.4, gap=7.5, maxw=29.5, cx=CX):
    """Letters as round-capped strokes, centred on cx. h is the cap
    height; the word shrinks if its centre-line width passes maxw."""
    ws = [_GLYPHS[c][0] for c in text]
    width = sum(ws) + gap * (len(text) - 1)
    s = h / 22
    if width * s > maxw:
        s = maxw / width
    x = cx - width * s / 2
    out = ""
    for c, w in zip(text, ws):
        spec = _GLYPHS[c]
        body = stroke(spec[1], colour, sw / s)
        for dx, dy in (spec[2] if len(spec) > 2 else []):
            body += circle(dx, dy, sw * 0.62 / s, colour)
        out += g(body, f"translate({f(x)} {f(base)}) scale({f(s)})")
        x += (w + gap) * s
    return out


def _cloud():
    return (circle(24.5, 30, 8, INK) + circle(35, 25, 11, INK) + circle(43.5, 33.5, 6.5, INK)
            + rrect(14, 31, 36, 14, 7, INK))


def _hexagon(cx, cy, r):
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in (pt(cx, cy, r, 60 * k) for k in range(6))) + "Z"


@reg("010editor", ORANGE_DEEP)
def ed010():
    leaf = path("M14 46C13.5 28 25 14.5 50 13C50.5 33 37 46.5 14 46Z", INK)
    pen = line(21, 39, 40, 20, HOLE, 3.4) + poly([(40, 20), (44.5, 16.5), (43.5, 21.5)], HOLE, 1.5)
    return leaf + pen


@reg("0ad", BROWN)
def zero_ad():
    return (circle(CX, CY, 16.5, INK) + line(CX, 12, CX, 48, HOLE, 3.6, "butt")
            + line(14, CY, 50, CY, HOLE, 3.6, "butt"))


@reg("0cc-famitracker", DEEP_PURPLE_DARK)
def famitracker():
    return (word("OCC", base=26, h=13, sw=3.6, gap=6.5)
            + word("FT", base=47, h=13, sw=3.6, gap=6.5))


@reg("140-game", GREY_DARK)
def game140():
    one = rrect(13, 22, 5, 6, 1, INK) + rrect(19.5, 19, 5, 22, 1, INK)
    four = poly([(26, 35.5), (35.5, 19), (35.5, 35.5)], INK, 1.5) + rrect(31, 19, 5, 22, 1, INK)
    return one + four + circle(44, 30, 6.5, INK)


@reg("1cedt", BLUE_DARK)
def onecedt():
    return (stroke(_hexagon(27.5, 36, 9.5), BLUE_SOFT, 3.4)
            + stroke(_hexagon(36.5, 24, 9.5), INK, 3.4))


@reg("1cestart", RED)
def onecestart():
    one = stroke("M15.5 25L21.5 20.5V40", INK, 4.6)
    c = stroke("M41.4 23.8A9.5 9.5 0 1 0 34.8 40H49", INK, 4.6)
    return one + c


@reg("1password", BLUE_DEEP)
def onepassword():
    ring = cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 12.3), INK)
    return ring + rrect(28.5, 19.5, 7, 21, 3.5, INK)


@reg("2048-qt", INDIGO_SOFT)
def game2048():
    return (word("20", base=26.5, h=14, sw=3.8, gap=6)
            + word("48", base=47, h=14, sw=3.8, gap=6))


@reg("2064-read-only-memories", LIGHT_BLUE)
def rom2064():
    face = circle(CX, 31, 16.5, INK)
    feats = (line(CX, 14.5, CX, 18.5, HOLE, 2.6) + line(26, 22.5, 26, 29, HOLE, 2.6)
             + line(38, 22.5, 38, 29, HOLE, 2.6)
             + stroke("M25 36.5H37.5C39.5 36.5 40 34 38.3 33.2", HOLE, 2.6))
    cheeks = rrect(18.5, 32, 5.5, 2.8, 1.4, RED_SOFT) + rrect(40, 32, 5.5, 2.8, 1.4, RED_SOFT)
    return face + feats + cheeks


@reg("2gis", LIGHT_BLUE)
def twogis():
    head = path("M32 11.5C38.5 11.5 43.5 15.5 43.5 21C43.5 26.5 38 30 32 30C26 30 20.5 26.5 20.5 21"
                "C20.5 15.5 25.5 11.5 32 11.5Z", INK)
    trunk = stroke("M32 28V36C32 40 27.5 43.5 21 44.5M32 36C32 40 36.5 43.5 43 44.5", INK, 4.4)
    return head + trunk


@reg("3D-Coat", CYAN_DEEP)
def coat3d():
    ring = cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 13.8), INK)
    fill = circle(CX, CY, 12, INK)
    cap = path("M21 24A12 12 0 0 1 43 24Z", HOLE)
    drips = (rrect(21.5, 21, 5.2, 13, 2.6, HOLE) + rrect(29.4, 21, 5.2, 18, 2.6, HOLE)
             + rrect(37.3, 21, 5.2, 10.5, 2.6, HOLE))
    return ring + fill + cap + drips


@reg("3depict", BLUE_GREY)
def threedepict():
    ol = f' stroke="{HOLE}" stroke-width="2.2"'
    return (circle(23.5, 29, 9.5, INK, ol) + circle(40, 23, 9, INK, ol)
            + circle(36.5, 39, 9, INK, ol))


@reg("4Pane", BLUE_DEEP)
def fourpane():
    return word("4P", h=24, base=42)


@reg("4diac-ide", INDIGO_DEEP)
def fourdiac():
    bars = (rrect(13, 13.5, 6.5, 6.5, 1.2, INDIGO_SOFT) + rrect(13, 23, 11, 3.6, 1.8, INDIGO_SOFT)
            + rrect(13, 29, 7, 3.6, 1.8, INDIGO_SOFT) + rrect(13, 40.5, 21, 3.6, 1.8, INDIGO_SOFT))
    four = stroke("M42 46V14L23.5 34.5H49.5", INK, 6.4)
    return bars + four


@reg("4digits", RED)
def fourdigits():
    return stroke("M38.5 45V15L17.5 36H47", INK, 5.6)


@reg("4kslideshowmaker", RED_DEEP)
def slideshow4k():
    body = rrect(14, 23, 36, 23, 7, INK) + circle(23.5, 21.5, 9, INK)
    sun = circle(23.5, 21.5, 3.4, HOLE)
    hills = poly([(18, 42), (26, 32.5), (30, 36.5), (36.5, 28.5), (46, 42)], HOLE, 1.8)
    return body + sun + hills


@reg("4kstogram", DEEP_ORANGE)
def stogram4k():
    return circle(30.5, 31.5, 13.5, INK) + circle(30.5, 31.5, 8, DEEP_ORANGE_SOFT) + circle(45.5, 16, 3.3, INK)


@reg("4kvideodownloader", PURPLE_SOFT)
def videodl4k():
    frame = rrect(25, 27, 14, 16, 2, HOLE)
    slots = rrect(28, 30.2, 8, 3.8, 1, INK) + rrect(28, 36, 8, 3.8, 1, INK)
    return _cloud() + frame + slots


@reg("4kvideotomp3", PURPLE_LIGHT)
def videomp34k():
    band = stroke("M17.5 36V30A14.5 14.5 0 0 1 46.5 30V33", INK, 4)
    cup = rrect(13.5, 30, 8, 14, 3.5, INK)
    reel = circle(41, 39.5, 11, HOLE) + circle(41, 39.5, 8.8, INK)
    holes = "".join(circle(*pt(41, 39.5, 4.4, a), 1.9, HOLE) for a in (-90, 0, 90, 180))
    return band + cup + reel + holes


@reg("4kyoutubetomp3", BLUE_LIGHT)
def ytmp34k():
    note = (stroke("M30.5 38.5V25.5L39.5 23.5V36.5", HOLE, 2.8)
            + circle(27.6, 38.5, 3.4, HOLE) + circle(36.6, 36.5, 3.4, HOLE))
    return _cloud() + note


@reg("6180-the-moon", GREY_DEEP)
def moon6180():
    return circle(CX, CY, 16.5, INK) + word("6180", HOLE, base=35, h=10, sw=2.6, gap=6)


@reg("7-days-to-die", RED_DARK)
def days7():
    bar = poly([(17, 13.5), (47.5, 13.5), (45.5, 19.5), (18.5, 19.5)], INK, 2)
    leg = poly([(39, 17), (47.5, 15), (34, 39.5), (31.5, 47), (29, 40), (25, 42.5), (28.5, 36)], INK, 2)
    return bar + leg


@reg("7kaa", BROWN_DARK)
def kaa7():
    tri = poly([(25.5, 11.5), (38.5, 11.5), (32, 20)], RED_LIGHT, 2)
    return tri + word("7K", base=46, h=21, sw=5, gap=6)


@reg("8bitmmo", BLUE_GREY_DEEP)
def mmo8bit():
    head = rrect(17, 13, 30, 21, 2.5, INK)
    eyes = rrect(23, 20.5, 6, 3.4, 0.6, HOLE) + rrect(35, 20.5, 6, 3.4, 0.6, HOLE)
    neck = rrect(24, 36.5, 16, 4, 1, INK)
    base = rrect(17, 42.5, 30, 5, 1.5, INK)
    return head + eyes + neck + base


@reg("8tracks", BLUE_DARK)
def tracks8():
    pts = []
    for k in range(73):
        t = 2 * math.pi * k / 72
        d = 1 + math.sin(t) ** 2
        x, y = 16.5 * math.cos(t) / d, 16.5 * math.sin(t) * math.cos(t) / d
        a = math.radians(-45)
        pts.append((CX + x * math.cos(a) - y * math.sin(a), CY + x * math.sin(a) + y * math.cos(a)))
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
    return stroke(d, INK, 4.6)


@reg("9gag", BLUE_GREY_DARK)
def ninegag():
    body = poly([(32, 12), (47, 20.5), (47, 38.5), (32, 47), (17, 38.5), (17, 33),
                 (32, 41.5), (32, 29), (17, 20.5)], INK, 2)
    hole = poly([(32, 16.5), (39, 20.6), (32, 24.7), (25, 20.6)], HOLE, 1)
    return body + hole


@reg("ADLplug", CYAN_DARK)
def adlplug():
    return word("ADL", h=16, base=38, sw=4.2, gap=6.5, maxw=34)


ADOBE = {
    "AdobeAfterEffect": ("Ae", DEEP_PURPLE),
    "AdobeAnimate": ("An", RED_DARK),
    "AdobeAudition": ("Au", TEAL),
    "AdobeBridge": ("Br", DEEP_ORANGE_DARK),
    "AdobeCharacterAnimator": ("Ch", PURPLE),
    "AdobeDimension": ("Dn", TEAL_DEEP),
    "AdobeDreamweaver": ("Dw", PURPLE_LIGHT),
    "AdobeEdgeAnimate": ("An", DEEP_PURPLE_LIGHT),
    "AdobeEncore": ("En", INDIGO),
    "AdobeFirework": ("Fw", AMBER_DARK),
    "AdobeFlashBuilder": ("Fb", DEEP_ORANGE_DEEP),
    "AdobeFresco": ("Fr", PURPLE_SOFT),
    "AdobeFuse": ("Fs", BROWN_DEEP),
    "AdobeIllustrator": ("Ai", ORANGE_DARK),
    "AdobeIncopy": ("Ic", PURPLE_DEEP),
    "AdobeIndesign": ("Id", PINK_DEEP),
    "AdobeLightroom": ("Lr", CYAN_DARK),
    "AdobeLightroomClassic": ("Lr", BLUE_GREY),
    "AdobeMuse": ("Mu", YELLOW_DARK),
    "AdobePhotoshop": ("Ps", BLUE_DARK),
    "AdobePrelude": ("Pl", BLUE_DEEP),
    "AdobePremierePro": ("Pr", DEEP_PURPLE_SOFT),
}

for _name, (_letters, _tile) in ADOBE.items():
    reg(_name, _tile)(lambda _l=_letters: word(_l))


@reg("AdobeMediaEncoder", INDIGO_DARK)
def adobe_me():
    out = poly([(15, 14), (15, 46), (47, 46)], INK, 2)
    for k in range(4):
        x, y = 19 + 7 * k, 14 + 7 * k
        out += rrect(x, y, 4.5, 4.5, 0.8, INK)
    return out


for _name, (_letters, _tile) in ADOBE.items():
    small(_name)(lambda _l=_letters: word(_l, sw=3.5, gap=8.5))


@small("0cc-famitracker")
def famitracker_s():
    return word("FT", h=22, sw=3.6, gap=7)


@small("2048-qt")
def game2048_s():
    return (word("20", base=27, h=16, sw=2.6, gap=8, maxw=34)
            + word("48", base=48, h=16, sw=2.6, gap=8, maxw=34))


@small("6180-the-moon")
def moon6180_s():
    return circle(CX, CY, 16.5, INK) + word("6180", HOLE, base=35.5, h=11, sw=2, gap=6.5, maxw=26)


@small("ADLplug")
def adlplug_s():
    return word("ADL", h=16, base=38, sw=3.2, gap=7, maxw=34)


@small("7kaa")
def kaa7_s():
    return (poly([(24.5, 11), (39.5, 11), (32, 20.5)], RED_LIGHT, 2)
            + word("7K", base=46, h=21, sw=3.8, gap=7))


@small("3D-Coat")
def coat3d_s():
    ring = cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 13.2), INK)
    fill = circle(CX, CY, 10.8, INK)
    cap = path("M22 25A10.8 10.8 0 0 1 42 25Z", HOLE)
    drips = rrect(23.5, 22, 6, 13, 3, HOLE) + rrect(34.5, 22, 6, 9, 3, HOLE)
    return ring + fill + cap + drips


@small("4kvideotomp3")
def videomp34k_s():
    band = stroke("M17.5 36V30A14.5 14.5 0 0 1 46.5 30V33", INK, 4)
    cup = rrect(13, 30, 9, 15, 4, INK)
    reel = circle(41, 39.5, 11.5, HOLE) + circle(41, 39.5, 9, INK) + circle(41, 39.5, 3.4, HOLE)
    return band + cup + reel


@small("4kyoutubetomp3")
def ytmp34k_s():
    note = (stroke("M31 38V25L40 23V36", HOLE, 3) + circle(27.5, 38, 4, HOLE)
            + circle(36.5, 36, 4, HOLE))
    return _cloud() + note


@small("4kslideshowmaker")
def slideshow4k_s():
    body = rrect(14, 23, 36, 23, 7, INK) + circle(23.5, 21.5, 9, INK)
    return (body + circle(23.5, 21.5, 4, HOLE)
            + poly([(19, 42), (33, 28), (45, 42)], HOLE, 2))


@small("8bitmmo")
def mmo8bit_s():
    head = rrect(16, 12, 32, 24, 3, INK)
    eyes = rrect(22, 20.5, 7, 5, 1, HOLE) + rrect(35, 20.5, 7, 5, 1, HOLE)
    return head + eyes + rrect(17, 40, 30, 7, 2, INK)
