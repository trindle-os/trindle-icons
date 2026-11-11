# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 3: fifty more brand glyphs, drawn to match batch 1.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DEEP, AMBER_SOFT, BLUE_DEEP, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_LIGHT,
    BLUE_GREY_SOFT, BLUE_SOFT, BROWN, circle, cpath, cut, CYAN_DARK, CYAN_DEEP,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DARK,
    DEEP_PURPLE_DEEP, g, GREY_DARK, GREY_DEEP, GREY_LIGHT, HOLE, INDIGO, INDIGO_LIGHT,
    INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line,
    ORANGE_DARK, ORANGE_DEEP, ORANGE_SOFT, path, PINK_DARK, PINK_DEEP, PINK_LIGHT, PINK_SOFT,
    poly, pt, RED, RED_DARK, RED_DEEP, rrect, stroke, TEAL_LIGHT, WHITE, YELLOW,
)
from glyphs.kit import registry

ICONS, SMALL, reg, small = registry()


def _sc(content, k, ox=32, oy=32):
    """Scale content drawn round (ox, oy) by k and centre it on (32, 30)."""
    return g(content, f"translate(32 30) scale({k}) translate({-ox} {-oy})")


@reg("AdobePremiereRush", DEEP_PURPLE_DEEP)
def adobe_rush():
    r = stroke("M17.5 42V18H24.5A6 6 0 0 1 24.5 30H17.5M24.5 30L30.5 42", INK, 4.4)
    u = stroke("M35 26V35.5A4.6 4.6 0 0 0 44.2 35.5M44.2 26V42", INK, 4.4)
    return r + u


@reg("AdobeSpeedgrade", CYAN_DARK)
def adobe_speedgrade():
    s = stroke("M28 20.5C26.5 18.8 24.8 18 22.8 18C19.8 18 17.8 20 17.8 23"
               "C17.8 29.5 28.5 27 28.5 35C28.5 39 26 42 22.5 42C20.2 42 18.3 41 16.8 39.3", INK, 4.4)
    gg = (f'<circle cx="39.8" cy="31.5" r="5.3" fill="none" stroke="{INK}" stroke-width="4.4"/>'
          + stroke("M45.3 25.5V42.5C45.3 46 43 48 39.8 48C37.8 48 36.2 47.3 35 46", INK, 4.4))
    return s + gg


@reg("AdobeUpdate", RED_DEEP)
def adobe_update():
    return poly([(27, 12.6), (37, 12.6), (47.5, 47.4), (40.7, 47.4), (32, 25),
                 (26.4, 40.5), (32.6, 40.5), (35.1, 47.4), (16.5, 47.4)], INK, 1.5)


@reg("AdobeXD", PINK_DARK)
def adobe_xd():
    x = line(17, 19, 29, 41, INK, 4.4) + line(29, 19, 17, 41, INK, 4.4)
    d = (f'<circle cx="39.5" cy="34.5" r="5.5" fill="none" stroke="{INK}" stroke-width="4.4"/>'
         + line(45, 18, 45, 41, INK, 4.4))
    return x + d


@reg("Alacritty", ORANGE_DEEP)
def alacritty():
    legs = stroke("M17.5 46L32 13.5L46.5 46", INK, 5.5)
    gem = poly([(32, 26.5), (35.5, 35.5), (32, 45), (28.5, 35.5)], INK, 1.5)
    return legs + gem


@reg("Alva", DEEP_PURPLE)
def alva():
    frame = path("M34.3 12C34.7 12 35 12.3 35 12.7V35.3C35 35.7 34.7 36 34.3 36H18.7"
                 "C18.1 36 17.8 35.3 18.1 34.8L33.7 12.3C33.9 12.1 34.1 12 34.3 12Z"
                 "M32 20.1V33H23.1Z", INK, ' fill-rule="evenodd"')
    bolt = path("M28 29.7C28 29.3 28.3 29 28.7 29H44.3C44.9 29 45.2 29.7 44.9 30.2"
                "L29.3 52.7C28.9 53.3 28 53 28 52.3Z", PINK_SOFT)
    return _sc(frame + bolt, .9, 31.5, 32.5)


@reg("AmneziaVPN", DEEP_ORANGE_DEEP)
def amnezia():
    ring = f'<circle cx="32" cy="31" r="13" fill="none" stroke="{INK}" stroke-width="3.4"/>'
    a = stroke("M20 46L32 13L44 46", INK, 4.4) + line(14.5, 35, 49.5, 27.5, INK, 4)
    return ring + a


@reg("AppImageLauncher", LIGHT_BLUE_DARK)
def appimagelauncher():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    arrow = poly([(32, 18), (42.5, 38.5), (32, 33.5), (21.5, 38.5)], INK, 2.2)
    return ring + arrow


@reg("BadlionClient", BLUE_DEEP)
def badlion():
    hexa = poly([pt(32, 30, 17.5, -90 + 60 * k) for k in range(6)], INK, 3)
    mane = poly([pt(32, 31, 12 if k % 2 == 0 else 9.5, -90 + 22.5 * k) for k in range(16)], HOLE, 1.5)
    face = path("M25 28C25 24 39 24 39 28L38 36C37 40 34.5 42 32 42C29.5 42 27 40 26 36Z", INK)
    shades = rrect(24.5, 28, 15, 4.2, 2, HOLE)
    nose = poly([(29.5, 35), (34.5, 35), (32, 38)], HOLE, 1)
    return hexa + mane + face + shades + nose


@reg("BambooTracker", LIGHT_BLUE_DEEP)
def bambootracker():
    out = ""
    for c, n in enumerate([4, 2, 2, 5, 6]):
        for r in range(n):
            out += rrect(15 + c * 7, 41.8 - r * 5.7, 6, 4.6, 1.3, INK)
    leaf = path("M24 30C24 24 29 21.5 35 22C34.5 27.5 30 31 24 30Z", LIGHT_BLUE_SOFT)
    return out + leaf


@reg("CMakeSetup", INDIGO)
def cmake():
    tri = poly([(32, 12.5), (49.5, 46.5), (14.5, 46.5)], INK, 2.5)
    right = poly([(32, 12.5), (49.5, 46.5), (33.5, 39.5)], INDIGO_SOFT, 2.5)
    hole = poly([(33.5, 27), (33.5, 39.5), (23, 39.5)], HOLE, 1.5)
    return tri + right + hole


@reg("CraftStudio", DEEP_ORANGE_DEEP)
def craftstudio():
    top = poly([(32, 12.5), (46, 19.5), (32, 26.5), (18, 19.5)], INK, 2.5)
    left = poly([(18, 19.5), (32, 26.5), (32, 44), (18, 37)], DEEP_ORANGE_SOFT, 2.5)
    right = poly([(46, 19.5), (32, 26.5), (32, 44), (46, 37)], DEEP_ORANGE_LIGHT, 2.5)
    star = ""
    for cx, cy, r in [(20.5, 38, 7), (43.5, 38, 7)]:
        pts = [pt(cx, cy, r if k % 2 == 0 else r * .45, -90 + 36 * k) for k in range(10)]
        star += poly(pts, HOLE, 3.5) + poly(pts, AMBER_SOFT, 1.2)
    return top + left + right + star


@reg("CubicSDR", BLUE_GREY_DEEP)
def cubicsdr():
    top = poly([(32, 20), (47, 27.5), (32, 35), (17, 27.5)], INK, 2.5)
    left = poly([(17, 27.5), (32, 35), (32, 48), (17, 40.5)], BLUE_GREY_SOFT, 2.5)
    right = poly([(47, 27.5), (32, 35), (32, 48), (47, 40.5)], BLUE_GREY_LIGHT, 2.5)
    wave = stroke("M35 41L37 36.5L39 42L41 35L43 40", INK, 2.2)
    stick = line(32, 27.5, 32, 19, BLUE_GREY_DARK, 2.6) + circle(32, 16.5, 4.5, RED)
    return top + left + right + wave + stick


@reg("CycligentGitTool", TEAL_LIGHT)
def cycligent():
    return stroke("M30.5 33C29.5 29.5 32.5 27 36.5 28.5C41.5 30.5 43 37 39 41C35 45 27.5 43.5 22.5 38"
                  "C17 32.5 15.5 24 20.5 19.5C26 14.5 37 16.5 44 23.5", INK, 4.2)


@reg("Dicomizer", GREY_DARK)
def dicomizer():
    v = stroke("M18.5 15.5L32 44.5L45.5 15.5", INK, 4)
    return v + poly([(23.2, 25.8), (40.8, 25.8), (32, 43.5)], INK, 1)


@reg("Encryptr", PINK_DEEP)
def encryptr():
    x0, x1, x2 = 20.5, 32, 43.5
    y0, y1, y2, y3 = 12.7, 24.2, 35.8, 47.3
    col = rrect(x0, y0, x1 - x0, y2 - y0, .8, INK)
    tris = (poly([(x0, y2), (x1, y2), (x1, y3)], INK, 1) +
            poly([(x2, y2), (x1, y2), (x1, y3)], INK, 1) +
            poly([(x2, y1), (x1, y1), (x1, y2)], INK, 1) +
            poly([(x2, y0), (x1, y0), (x1, y1)], PINK_SOFT, 1))
    return col + tris


@reg("FAHControl", RED)
def fahcontrol():
    out = ""
    for cx, cy, r in [(25, 25.5, 8.5), (37.5, 34, 9.5), (41, 20, 6.5), (24.5, 40, 6), (46, 14.5, 4)]:
        out += circle(cx, cy, r, INK, f' stroke="{HOLE}" stroke-width="2"')
    return out


@reg("FamiStudio", BLUE_GREY_DARK)
def famistudio():
    s, x0, y0 = 11.2, 15.2, 13.2
    cells = "".join(rrect(x0 + c * s, y0 + r * s, s - 1, s - 1, 2.2, INK)
                    for c, r in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])
    sq = rrect(28.3, 16.8, 5.4, 5.4, .6, HOLE)
    tri = poly([(20.2, 32.5), (23.4, 26.8), (26.6, 32.5)], HOLE, .8)
    chk = "".join(rrect(41.5 + i * 2.6, 26.2 + j * 2.6, 2.6, 2.6, 0, HOLE)
                  for i in range(3) for j in range(3) if (i + j) % 2 == 0)
    bars = "".join(rrect(28.4 + i * 2.6, 39.2, 1.6, 6, .6, HOLE) for i in range(3))
    return cells + sq + tri + chk + bars


@reg("FlashCS6", RED_DARK)
def flash_cs6():
    frame = rrect(15.5, 13.5, 33, 33, 4, "none", f' stroke="{INK}" stroke-width="3"')
    fl = stroke("M24 40.5V21.5H33M24 30.5H31.5", INK, 4.2) + line(38.5, 20, 38.5, 40.5, INK, 4.2)
    return frame + fl


@reg("FreeTexturePacker", GREY_DARK)
def freetexturepacker():
    hexa = poly([pt(32, 30, 17.5, -90 + 60 * k) for k in range(6)], INK, 3)
    cube = (stroke("M32 18.5L42 24.3V35.7L32 41.5L22 35.7V24.3Z", HOLE, 2.6) +
            stroke("M22 24.3L32 30L42 24.3M32 30V41.5", HOLE, 2.6))
    return hexa + cube


@reg("Freeter", BLUE_GREY_DEEP)
def freeter():
    return (rrect(17.6, 13.2, 8, 33.6, 1.2, INK) + rrect(28.8, 13.2, 17.6, 8, 1.2, INK) +
            rrect(28.8, 24.4, 8, 8, 1.2, INK))


@reg("GP6-icon", RED_DEEP)
def guitar_pro():
    pick = path("M32 12C42.5 12 49.5 15 49.5 21.5C49.5 31 38.5 46 32 48.5"
                "C25.5 46 14.5 31 14.5 21.5C14.5 15 21.5 12 32 12Z", INK)
    gl = stroke("M30 20.5C29 19 27.5 18.5 26 18.5C22.8 18.5 20.5 21 20.5 24.5"
                "C20.5 28 22.8 30.5 26 30.5C28.5 30.5 30.3 29 30.3 26H26.5", HOLE, 2.6)
    pl = stroke("M34.5 30.5V18.5H38.5A3.3 3.3 0 0 1 38.5 25.2H34.5", HOLE, 2.6)
    return pick + gl + pl


@reg("GPG-Key4", ORANGE_DARK)
def gpg_key():
    key = (cut(cpath(21, 25, 7.5) + cpath(19.8, 25, 2.8), INK) +
           rrect(26, 22.7, 21, 4.6, 1.5, INK) + rrect(37, 17.5, 4, 6, 1, INK) +
           rrect(43, 17.5, 4, 6, 1, INK))
    badge = circle(41, 39, 9.5, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    tick = circle(41, 39, 3.2, HOLE)
    return key + badge + tick


@reg("GPU_Viewer", BLUE_GREY_DEEP)
def gpu_viewer():
    card = rrect(16, 17, 34, 22, 3, INK) + rrect(13, 15, 3.5, 30, 1.5, INK)
    pins = "".join(rrect(20 + i * 5.5, 38, 3.4, 6, 1, INK) for i in range(5))
    fans = ""
    for cx, r in [(26, 7), (40.5, 6)]:
        fans += circle(cx, 28, r, HOLE)
        for k in range(3):
            a = 30 + 60 * k
            x1, y1 = pt(cx, 28, r - 2, a)
            x2, y2 = pt(cx, 28, r - 2, a + 180)
            fans += line(x1, y1, x2, y2, INK, 2.2)
    return card + pins + fans


@reg("GameMakerStudio2", BLUE_GREY_DARK)
def gamemaker():
    return cut("M32 12.4L14.4 30L32 47.6L40 39.7V30H49.6Z" "M32 30V37.4L24.6 30L32 22.6L40 30Z", INK)


@reg("GammaRay", BLUE_DEEP)
def gammaray():
    return stroke("M18.5 23.5C20.5 20 24 19 26.5 22C29.5 26 31 33.5 32 38.5"
                  "C33 43.5 31.5 47 29.5 45.5C27.5 44 29 38.5 32.5 33L44.5 13.5", INK, 3.8)


@reg("ILSpy", BLUE_GREY_DEEP)
def ilspy():
    win = rrect(24, 12, 25, 19, 3, BLUE_GREY_SOFT)
    bar = path("M27 12H46A3 3 0 0 1 49 15V17H24V15A3 3 0 0 1 27 12Z", INK)
    lens = circle(29, 32.5, 9, INK) + circle(29, 32.5, 5.5, HOLE)
    handle = line(22.5, 39, 16, 45.5, INK, 4.6)
    return win + bar + lens + handle


@reg("Impactor", GREY_DARK)
def impactor():
    body = rrect(24, 16, 23, 13, 4, INK)
    grip = poly([(33, 27), (45, 27), (43.5, 45.5), (37, 45.5)], INK, 3)
    nozzle = rrect(17, 18.7, 8, 7.6, 1.5, INK)
    cable = line(12.5, 22.5, 17.5, 22.5, INK, 3)
    return body + grip + nozzle + cable + circle(41.5, 22.5, 2.2, HOLE)


@reg("JForex", RED_DARK)
def jforex():
    j = stroke("M28 14.5V36C28 42 24.5 45.5 18.5 44", INK, 5)
    ff = stroke("M35 45.5V22C35 17.5 37.5 15 41.5 15H46M35 29H44", INK, 5)
    return j + ff


@reg("JRomManager", BLUE_GREY_DEEP)
def jrommanager():
    pins = "".join(rrect(x, 12.5, 5.4, 10, 1.2, BLUE_GREY_SOFT) + rrect(x, 37.5, 5.4, 10, 1.2, BLUE_GREY_SOFT)
                   for x in (19.5, 29.3, 39.1))
    body = rrect(13, 19.5, 38, 21, 3.5, INK)
    r = stroke("M17.5 35.5V24.5H20.8A2.8 2.8 0 0 1 20.8 30H17.5M20.8 30L23.8 35.5", HOLE, 2.4)
    o = rrect(27, 24.5, 8, 11, 3.4, "none", f' stroke="{HOLE}" stroke-width="2.4"')
    m = stroke("M38.5 35.5V24.5L42.5 30.5L46.5 24.5V35.5", HOLE, 2.4)
    return pins + body + r + o + m


@reg("JabRef", INDIGO)
def jabref():
    left = path("M30.5 20.5C27 16.5 21 15.5 15.5 16.5V43.5C21 42.5 27 43.5 30.5 47Z", INK)
    right = path("M33.5 20.5C37 16.5 43 15.5 48.5 16.5V43.5C43 42.5 37 43.5 33.5 47Z", INK)
    arcs = (stroke("M19.5 22C23 22 26 23 27.5 25.5", HOLE, 2.2) +
            stroke("M19.5 29C23 29 26 30 27.5 32.5", HOLE, 2.2) +
            stroke("M44.5 22C41 22 38 23 36.5 25.5", HOLE, 2.2) +
            stroke("M44.5 29C41 29 38 30 36.5 32.5", HOLE, 2.2))
    tip = poly([(28, 12.5), (36, 12.5), (32, 17.5)], INK, 2)
    return left + right + arcs + tip


@reg("JavaFXSceneBuilder2.0", BLUE_GREY_DARK)
def scenebuilder():
    hand = (rrect(26, 9, 7, 22, 3.5, INK) + rrect(33.8, 17.5, 6.4, 13, 3.2, INK) +
            rrect(40.8, 19.5, 6.2, 12, 3.1, INK) +
            path("M26 27H47V36C47 43 42 47 36 47H33C28.5 47 25.5 45 23 41L17.5 32.5"
                 "C16.5 30.8 17 29 18.5 28.3C20 27.6 21.5 28.2 22.5 29.5L26 34Z", INK))
    gaps = line(33.4, 23, 33.4, 30, HOLE, 2) + line(40.5, 24.5, 40.5, 30, HOLE, 2)
    return g(hand + gaps, "rotate(-30 32 30)")


@reg("Jellyamp", DEEP_PURPLE)
def jellyamp():
    outer = poly([(19.5, 13), (47.5, 33), (17, 46)], INK, 5)
    inner = poly([(25.5, 25), (37.5, 33.5), (24.5, 39)], HOLE, 2.5)
    return outer + inner


@reg("KakaoTalk", YELLOW)
def kakaotalk():
    bubble = ('<ellipse cx="32" cy="28.5" rx="17.5" ry="13.5" fill="INK"/>' +
              poly([(21, 36), (18.5, 46.5), (28.5, 40)], INK, 2))
    w = 2.2
    t = line(18.2, 24.5, 23.2, 24.5, HOLE, w) + line(20.7, 24.5, 20.7, 33, HOLE, w)
    a = stroke("M25 33L27.6 24.5L30.2 33M26 30.2H29.2", HOLE, w)
    l_ = stroke("M33 24.5V33H37", HOLE, w)
    k = line(39.5, 24.5, 39.5, 33, HOLE, w) + stroke("M44.5 24.5L39.8 29L44.8 33", HOLE, w)
    return bubble + t + a + l_ + k


@reg("KittehPlayer", PINK_LIGHT)
def kittehplayer():
    ears = poly([(17.5, 23), (19.5, 11), (28, 18)], INK, 2.5) + poly([(46.5, 23), (44.5, 11), (36, 18)], INK, 2.5)
    body = rrect(14.5, 16.5, 35, 31, 9, INK)
    screen = rrect(19.5, 21.5, 25, 21, 5.5, HOLE)
    play = poly([(28.5, 26.5), (37.5, 32), (28.5, 37.5)], INK, 2.5)
    return ears + body + screen + play


@reg("KoboDeluxe", BLUE_DEEP)
def kobodeluxe():
    wings = (poly([(27, 25), (15, 41), (16.5, 44.5), (27, 42)], INK, 2) +
             poly([(37, 25), (49, 41), (47.5, 44.5), (37, 42)], INK, 2))
    body = path("M32 12C35.5 16 38.5 23 38.5 31V43.5C38.5 45.5 25.5 45.5 25.5 43.5V31"
                "C25.5 23 28.5 16 32 12Z", INK, f' stroke="{HOLE}" stroke-width="1.8"')
    return wings + body + '<ellipse cx="32" cy="33" rx="3.5" ry="4.5" fill="HOLE"/>'


@reg("LanguageTool", BLUE_DEEP)
def languagetool():
    l_ = stroke("M17.5 14.5H21.5V30H28", INK, 4)
    t = stroke("M31 14.5H46M38.5 14.5V30", INK, 4)
    wave = stroke("M16 38.5C18.5 35.5 21.5 35.5 24 38.5C26.5 41.5 29.5 41.5 32 38.5"
                  "C34.5 35.5 37.5 35.5 40 38.5C42.5 41.5 45.5 41.5 48 38.5", BLUE_SOFT, 3.6)
    return l_ + t + wave


@reg("LyricsFinder", LIGHT_BLUE_DEEP)
def lyricsfinder():
    bino = (rrect(15, 21, 13, 23, 4, INK) + rrect(34, 21, 13, 23, 4, INK) +
            rrect(26, 24, 10, 9, 1.5, INK) + rrect(17, 13, 9, 9, 2, INK) + rrect(36, 13, 9, 9, 2, INK))
    badge = circle(42.5, 40.5, 9.5, HOLE)
    note = (circle(39.5, 44, 2.3, INK) + circle(46, 42.5, 2.3, INK) +
            stroke("M41.2 44V35.5L47.7 34V42.5", INK, 1.9))
    return bino + badge + note


@reg("MAX", INDIGO_LIGHT)
def max_messenger():
    bubble = cut("M32.5 12.5C43 12.5 50 20.5 50 30C50 40 42.5 47.5 32.5 47.5"
                 "C29 47.5 26.5 46.5 24.5 45C22.5 47.5 17.5 48.5 17 46C17 43.5 15.5 40.5 15.5 34"
                 "C15.5 21 23 12.5 32.5 12.5Z"
                 "M31.5 21.5C26.5 21.5 23.5 25.5 23 30.5C22.6 34.5 23.5 38.5 24.5 38.8"
                 "C25 39 26.5 37.8 27.3 37C28.8 38 30.5 38.8 32.5 38.8C37.5 38.8 41 35 41 30"
                 "C41 25.3 37 21.5 31.5 21.5Z", INK)
    return bubble


@reg("MediaElch", BROWN)
def mediaelch():
    ant = (stroke("M24 22C19 21 15.5 17.5 15 13M20 20.5L20.5 13M16.5 18.5L12.5 19", INK, 3) +
           stroke("M40 22C45 21 48.5 17.5 49 13M44 20.5L43.5 13M47.5 18.5L51.5 19", INK, 3))
    head = path("M25.5 24C25.5 20.5 38.5 20.5 38.5 24L39.5 37C40 43 36.5 47.5 32 47.5"
                "C27.5 47.5 24 43 24.5 37Z", INK)
    ears = (path("M25 26L18 25.5C19 29 22 30.5 25.5 30Z", INK) +
            path("M39 26L46 25.5C45 29 42 30.5 38.5 30Z", INK))
    face = circle(28.5, 29, 1.6, HOLE) + circle(35.5, 29, 1.6, HOLE) + \
        circle(29.5, 42, 1.4, HOLE) + circle(34.5, 42, 1.4, HOLE)
    return ant + head + ears + face


@reg("MediaHuman", GREY_DEEP)
def mediahuman():
    mic = rrect(24.5, 11.5, 15, 22, 7.5, INK)
    slots = "".join(line(28.5, y, 35.5, y, HOLE, 2.2) for y in (18, 22.5, 27))
    neck = rrect(30, 33, 4, 5, 0, INK)
    base = (path("M17 41.5C17 38.5 19 37 22 37H42C45 37 47 38.5 47 41.5C47 44 45 45 43 44.5"
                 "L32 41L21 44.5C19 45 17 44 17 41.5Z", INK) +
            path("M26 43L32 41L38 43L36 48H28Z", INK))
    return mic + slots + neck + base


@reg("MesenSIcon", ORANGE_DEEP)
def mesen():
    brow = stroke("M15.5 27C25 17.5 39 17.5 48.5 27", INK, 4.2)
    lower = stroke("M17.5 38C26 44.5 38 44.5 46.5 38", ORANGE_SOFT, 3.4)
    iris = circle(32, 32, 8.5, INK) + line(33.5, 28.5, 36.5, 31.5, HOLE, 2.4)
    return brow + lower + iris


@reg("MotionBox", LIGHT_BLUE)
def motionbox():
    return poly([(14.5, 45.5), (20.5, 14.5), (27, 14.5), (32, 28), (37, 14.5), (43.5, 14.5),
                 (49.5, 45.5), (42.5, 45.5), (39.5, 28), (34.5, 40), (29.5, 40), (24.5, 28),
                 (21.5, 45.5)], INK, 2)


@reg("Nim", AMBER_DEEP)
def nim():
    crown = path("M13 23.5L19 25.5L22 18.5L27 22.5L32 16.5L37 22.5L42 18.5L45 25.5L51 23.5"
                 "L47 31.5C41.5 27 22.5 27 17 31.5Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    band = path("M15 37.5C21.5 33.5 42.5 33.5 49 37.5L45 43C38.5 48 25.5 48 19 43Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return crown + band


@reg("NoMachine-icon", RED_DEEP)
def nomachine():
    bang = rrect(15, 16, 6.5, 18.5, 1.5, INK) + rrect(15, 37.5, 6.5, 6.5, 1.5, INK)
    m = path("M26.5 16H47.5A1.5 1.5 0 0 1 49 17.5V44H43V22.5H40.5V44H35V22.5H32.5V44H25V17.5"
             "A1.5 1.5 0 0 1 26.5 16Z", INK)
    return bang + m


@reg("Notesnook", BLUE_GREY_DARK)
def notesnook():
    top = stroke("M20.5 12.5V26A11.75 11.75 0 0 1 44 26V38.5", INK, 5)
    bottom = stroke("M20.5 32V38.5C20.5 45.5 26 50.5 32.25 50.5C37 50.5 41 47.5 42.6 43.5", INK, 5)
    return _sc(top + bottom, .8, 32.25, 31.5)


@reg("Nvidiux", RED_DEEP)
def nvidiux():
    ticks = (f'<path d="M20 20.5A20 20 0 0 1 47 38.5" fill="none" stroke="{INK}" '
             'stroke-width="4" stroke-dasharray="3 2.2"/>')
    needle = poly([(24.5, 33.5), (47, 16.5), (29.5, 38.5)], INK, 1.5)
    hub = circle(26, 37.5, 6.8, INK)
    return _sc(ticks + needle + hub, 1, 33, 31)


@reg("Black_Chocobo", GREY_LIGHT)
def black_chocobo():
    crest = (path("M36 21L41 11L41.5 19.5L48 13.5L45.5 22.5L50.5 21.5L44 28Z", INK))
    head = path("M23 26C23 19.5 28 16.5 33.5 16.5C40.5 16.5 45 21.5 45 28.5V48H26"
                "C27 43 29 38.5 27.5 34.5C25 32.5 23 30 23 26Z", INK)
    beak = poly([(26, 23.5), (13, 30.5), (27.5, 32.5)], AMBER, 1.5)
    eye = circle(30, 24, 2, WHITE) + circle(30.4, 24, 1.1, INK)
    return head + crest + beak + eye


@reg("Diablo", RED_DARK)
def diablo():
    d = cut("M18 13H32.5C42 13 47.5 20 47.5 30C47.5 40 42 47 32.5 47H18Z"
            "M26 20.5H32C37 20.5 39.5 24.5 39.5 30C39.5 35.5 37 39.5 32 39.5H26Z", INK)
    foot = path("M18 38L26 38V47H20C17 47 14.5 48 12.5 50C13 45 15.5 41 18 38Z", INK)
    return d + foot


@reg("Dstroy2", DEEP_PURPLE)
def dstroy2():
    out = ""
    for cx, cy, r in [(23.5, 32, 7.5), (39.5, 29, 8.5)]:
        out += circle(cx, cy, r, INK) + circle(cx + r * .3, cy, r * .5, CYAN_DEEP) + \
            circle(cx + r * .3, cy, r * .22, DEEP_PURPLE_DARK)
    return out


@small("KakaoTalk")
def kakaotalk_s():
    return ('<ellipse cx="32" cy="28.5" rx="18" ry="14" fill="INK"/>' +
            poly([(21, 36), (18, 47), (29, 40)], INK, 2))


@small("JRomManager")
def jrommanager_s():
    pins = "".join(rrect(x, 12, 6, 10, 1.2, BLUE_GREY_SOFT) + rrect(x, 38, 6, 10, 1.2, BLUE_GREY_SOFT)
                   for x in (18.5, 29, 39.5))
    return pins + rrect(13, 19.5, 38, 21, 4, INK)


@small("FamiStudio")
def famistudio_s():
    s, x0, y0 = 11.2, 15.2, 13.2
    return "".join(rrect(x0 + c * s, y0 + r * s, s - 1, s - 1, 2.2, INK)
                   for c, r in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])


@small("GPU_Viewer")
def gpu_viewer_s():
    card = rrect(13, 16, 38, 24, 3.5, INK)
    pins = "".join(rrect(19 + i * 7.5, 38, 5, 7, 1.2, INK) for i in range(4))
    return card + pins + circle(24.5, 28, 7, HOLE) + circle(40, 28, 7, HOLE)


@small("LyricsFinder")
def lyricsfinder_s():
    bino = (rrect(14, 20, 14, 25, 4.5, INK) + rrect(36, 20, 14, 25, 4.5, INK) +
            rrect(26, 24, 12, 10, 1.5, INK))
    return bino + circle(43, 41, 9.5, HOLE) + circle(42, 43, 4.5, INK)


@small("BadlionClient")
def badlion_s():
    hexa = poly([pt(32, 30, 18, -90 + 60 * k) for k in range(6)], INK, 3)
    mane = poly([pt(32, 30.5, 13 if k % 2 == 0 else 10.5, -90 + 30 * k) for k in range(12)], HOLE, 2)
    return hexa + mane + circle(32, 31.5, 6.5, INK)


@small("CraftStudio")
def craftstudio_s():
    top = poly([(32, 11.5), (48, 19.5), (32, 27.5), (16, 19.5)], INK, 2.5)
    left = poly([(16, 19.5), (32, 27.5), (32, 47), (16, 39)], DEEP_ORANGE_SOFT, 2.5)
    right = poly([(48, 19.5), (32, 27.5), (32, 47), (48, 39)], DEEP_ORANGE_LIGHT, 2.5)
    pts = [pt(32, 38, 10 if k % 2 == 0 else 4.5, -90 + 36 * k) for k in range(10)]
    return top + left + right + poly(pts, HOLE, 3) + poly(pts, AMBER_SOFT, 1)


@small("CubicSDR")
def cubicsdr_s():
    top = poly([(32, 19), (49, 27.5), (32, 36), (15, 27.5)], INK, 2.5)
    left = poly([(15, 27.5), (32, 36), (32, 49), (15, 40.5)], BLUE_GREY_SOFT, 2.5)
    right = poly([(49, 27.5), (32, 36), (32, 49), (49, 40.5)], BLUE_GREY_LIGHT, 2.5)
    return top + left + right + line(32, 27.5, 32, 18, BLUE_GREY_DARK, 3) + circle(32, 15, 5.5, RED)


@small("FreeTexturePacker")
def freetexturepacker_s():
    hexa = poly([pt(32, 30, 18, -90 + 60 * k) for k in range(6)], INK, 3)
    return hexa + stroke("M22 24.3L32 30L42 24.3M32 30V42", HOLE, 3)


@small("Nvidiux")
def nvidiux_s():
    arc = (f'<path d="M20 20.5A20 20 0 0 1 47 38.5" fill="none" stroke="{INK}" '
           'stroke-width="4" stroke-dasharray="6 3.5"/>')
    return _sc(arc + poly([(23.5, 33), (47, 16.5), (30, 39.5)], INK, 2) + circle(26, 37.5, 7.5, INK), 1, 33, 31)


@small("AmneziaVPN")
def amnezia_s():
    ring = f'<circle cx="32" cy="31" r="14.5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
    return ring + stroke("M21.5 45L32 15L42.5 45", INK, 3.6) + line(15.5, 35, 48.5, 28, INK, 3.2)


@small("GPG-Key4")
def gpg_key_s():
    key = (cut(cpath(21, 24, 8) + cpath(21, 24, 3.2), INK) + rrect(27, 21.5, 21, 5.5, 1.5, INK) +
           rrect(41, 16, 5, 7, 1, INK))
    return key + circle(41, 40, 9.5, INK, f' stroke="{HOLE}" stroke-width="3"') + \
        circle(41, 40, 3.4, HOLE)


@small("GP6-icon")
def guitar_pro_s():
    pick = path("M32 11C43 11 50.5 14 50.5 21C50.5 31 39 46.5 32 49"
                "C25 46.5 13.5 31 13.5 21C13.5 14 21 11 32 11Z", INK)
    return pick + stroke("M37.5 20C36 18 34 17.5 32 17.5C27.5 17.5 24.5 21 24.5 25.5"
                         "C24.5 30 27.5 33 32 33C35.5 33 38 31 38 27H32.5", HOLE, 3)


@small("JabRef")
def jabref_s():
    left = path("M30.5 18.5C27 14.5 20.5 13.5 14.5 14.5V44.5C20.5 43.5 27 44.5 30.5 48Z", INK)
    right = path("M33.5 18.5C37 14.5 43.5 13.5 49.5 14.5V44.5C43.5 43.5 37 44.5 33.5 48Z", INK)
    return left + right
