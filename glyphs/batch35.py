# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 35: ignuit to io.github.lainsce.DotMatrix.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_LIGHT, BROWN_DEEP, BROWN_LIGHT, BROWN_SOFT, circle, CX,
    CY, DEEP_ORANGE, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_LIGHT, f, g, GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK,
    INDIGO_LIGHT, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE_DARK,
    ORANGE_DEEP, ORANGE_SOFT, path, PINK, PINK_DEEP, PINK_LIGHT, PINK_SOFT, poly, pt,
    PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke,
    TEAL_DEEP,
)
from glyphs.kit import arc, registry, _ring

ICONS, SMALL, reg, small = registry()


@reg("ignuit", INDIGO_LIGHT)
def ignuit():
    back = rrect(27, 12, 21, 26, 3.5, INDIGO_DARK)
    front = rrect(16, 20, 22, 28, 3.5, INK)
    lines = "".join(rrect(20, y, w, 2.6, 1.3, HOLE) for y, w in
                    [(26, 14), (31.5, 14), (37, 14), (42.5, 9)])
    return back + front + lines


@reg("im.bernard.Nostalgia", BLUE_GREY_DEEP)
def nostalgia():
    body = rrect(14, 13, 36, 28, 4, INK)
    screen = rrect(18, 16.5, 28, 20, 2, HOLE)
    stripes = "".join(rrect(x, 16.5, 3.5, 20, 0, INK) for x in (22.5, 29.5, 36.5))
    stand = rrect(24, 42.5, 16, 5, 2, INK)
    return body + screen + stripes + stand


@reg("im.fluffychat.Fluffychat", DEEP_PURPLE_DEEP)
def fluffychat():
    fur = "".join(circle(*pt(32, 32, 12.5, a), 4.2, INK) for a in range(0, 360, 30))
    head = circle(32, 32, 13, INK)
    ears = (poly([(17.5, 23), (18.5, 11.5), (27, 19)], INK, 2.5) +
            poly([(46.5, 23), (45.5, 11.5), (37, 19)], INK, 2.5))
    face = circle(26.5, 30, 2.3, HOLE) + circle(37.5, 30, 2.3, HOLE) + circle(32, 35, 1.8, HOLE)
    return g(fur + head + ears + face, "translate(32 30) scale(.92) translate(-32 -31)")


@reg("im.srain.Srain", LIGHT_BLUE_DEEP)
def srain():
    drop = path("M32 13H45A2 2 0 0 1 47 15V30A15 15 0 1 1 32 15Z", INK)
    drop = path("M47 13V30A15 15 0 1 1 32 15C38 15 42 13 47 13Z", INK)
    hashm = (line(29.5, 23, 27.5, 39, HOLE, 3) + line(36.5, 23, 34.5, 39, HOLE, 3) +
             line(23.5, 28, 40.5, 28, HOLE, 3) + line(23, 34, 40, 34, HOLE, 3))
    return drop + hashm


@reg("imhex", INDIGO)
def imhex():
    zero = (rrect(14, 13, 20, 5, 1.5, INK) + rrect(14, 42, 20, 5, 1.5, INK) +
            rrect(15.5, 15, 5.5, 30, 0, INK) + rrect(27, 15, 5.5, 30, 0, INK))
    one = rrect(37, 13, 13, 5, 1.5, INK) + rrect(43.5, 15, 5.5, 32, 1.5, INK)
    return zero + one


@reg("imperator-rome", AMBER_DARK)
def imperator():
    wreath = ""
    for side in (-1, 1):
        for k in range(6):
            a = 100 + side * 0 + (k * 22 if side == 1 else -k * 22)
            a = 90 - side * (18 + k * 22)
            x, y = pt(32, 30, 16, a)
            wreath += g(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="3.2" ry="1.4" fill="{AMBER_SOFT}"/>',
                        f"rotate({f(a + 90 + side * 35)} {f(x)} {f(y)})")
    wings = (poly([(29, 26), (14, 20), (16, 25), (13, 26), (17, 29), (15, 31), (22, 32), (29, 33)], INK, 2) +
             poly([(35, 26), (50, 20), (48, 25), (51, 26), (47, 29), (49, 31), (42, 32), (35, 33)], INK, 2))
    body = path("M32 22C35 22 36.5 25 36 29L34.5 37L37 42H27L29.5 37L28 29C27.5 25 29 22 32 22Z", INK)
    head = circle(33, 20, 3.2, INK) + poly([(35, 18.5), (38.5, 20.5), (35, 21.5)], INK, 1)
    return wreath + wings + body + head


@reg("in.bharatkalluri.shortcircuit", GREY_DARK)
def shortcircuit():
    bolt = poly([(30, 13), (21, 32), (28, 32), (24, 47), (37, 26), (30, 26), (36, 13)], INK, 2)
    under = rrect(36, 42, 11, 4, 2, INK)
    return bolt + under


@reg("incredipede", AMBER_DARK)
def incredipede():
    eye = path("M14 31C19 21 27 17.5 34 18C41 18.5 46.5 23 50 30C45 38 38 42.5 31 42.5"
               "C23.5 42.5 18 38 14 31Z", INK)
    iris = circle(33, 29.5, 9, HOLE) + circle(33, 29.5, 4.5, INK) + circle(35, 27.5, 1.5, HOLE)
    return eye + iris


@reg("indicator-cpufreq", GREY_DARK)
def cpufreq():
    pins = ("".join(rrect(x, 11, 4, 6, 1.5, INK) for x in (23, 30, 37)) +
            "".join(rrect(12, y, 6, 4, 1.5, INK) for y in (23, 30, 37)))
    chip = rrect(19, 18, 31, 30, 4, INK)
    c = stroke("M28.5 29.5C28.5 28 27.5 27.5 26 27.5C24.5 27.5 23.5 28.5 23.5 30.5V35"
               "C23.5 37 24.5 38 26 38C27.5 38 28.5 37.5 28.5 36", HOLE, 2.2)
    p = stroke("M32 38V27.5H34.5C36.5 27.5 37.2 28.5 37.2 30.2C37.2 32 36.5 33 34.5 33H32", HOLE, 2.2)
    u = stroke("M40.5 27.5V35C40.5 37 41.5 38 43 38C44.5 38 45.5 37 45.5 35V27.5", HOLE, 2.2)
    return pins + chip + c + p + u


@reg("infector", GREY_DARK)
def infector():
    out = ""
    corners = {(0, 0): BROWN_SOFT, (4, 4): BROWN_SOFT, (4, 0): RED, (0, 4): RED}
    for r in range(5):
        for c in range(5):
            x, y = 15 + c * 6.8, 13 + r * 6.8
            if (r, c) in corners:
                out += rrect(x, y, 6.8, 6.8, 1.5, corners[(r, c)])
            elif (r + c) % 2 == 0:
                out += rrect(x, y, 6.8, 6.8, 0.8, INK)
    return out


@reg("infinifactory", ORANGE_DEEP)
def infinifactory():
    top = poly([(32, 13), (48, 21), (32, 29), (16, 21)], INK, 2.5)
    left = poly([(16, 21), (32, 29), (32, 47), (16, 39)], ORANGE_SOFT, 2.5)
    right = poly([(48, 21), (32, 29), (32, 47), (48, 39)], ORANGE_DARK, 2.5)
    arrow = poly([(18.5, 29), (24, 32), (24, 29.5), (29, 32), (29, 37), (24, 34.5), (24, 37.5), (18.5, 34.5)],
                 ORANGE_DARK, 1)
    return top + left + right + arrow


@reg("info.febvre.Komikku", RED_DEEP)
def komikku():
    page = rrect(16, 12, 30, 36, 3.5, INK)
    spine = rrect(43, 14, 6, 34, 2.5, RED_SOFT)
    cuts = (line(16, 24, 46, 21, HOLE, 2.4, "butt") + line(29, 12, 27.5, 22.8, HOLE, 2.4, "butt") +
            line(16, 35, 46, 32, HOLE, 2.4, "butt") + line(35, 22, 36.5, 33, HOLE, 2.4, "butt"))
    return spine + page + cuts


@reg("inky", BLUE_GREY_DARK)
def inky():
    moon = circle(CX, CY, 16.5, INK)
    blots = (circle(27, 32, 5.5, HOLE) + circle(33, 29, 4, HOLE) + circle(36, 35, 4.5, HOLE) +
             circle(23, 26, 2.3, HOLE) + circle(41, 24, 2, HOLE) + circle(38, 20, 1.4, HOLE) +
             circle(21, 38, 1.8, HOLE) + circle(31, 20.5, 1.5, HOLE) + circle(44, 33, 1.4, HOLE))
    return moon + blots


@reg("input-tablet", BLUE_GREY_DEEP)
def input_tablet():
    pad = rrect(13, 15, 36, 28, 4, INK)
    strip = rrect(19, 15, 2.6, 28, 0, HOLE)
    pen = (stroke("M45.5 20.5L33 33", HOLE, 7) + stroke("M45.5 20.5L33 33", AMBER_DEEP, 3.4) +
           poly([(31.5, 34.5), (30, 36.5), (32, 35)], AMBER_DEEP, 2))
    return pad + strip + pen


@reg("insomnia", DEEP_PURPLE)
def insomnia():
    return _ring(CX, CY, 14.5, INK, 4) + circle(25.5, 23.5, 5.5, INK)


@reg("insomnia-designer", DEEP_PURPLE_LIGHT)
def insomnia_designer():
    i = rrect(16, 14, 13, 4.5, 1.5, INK) + rrect(20.25, 14, 4.5, 32, 0, INK) + rrect(16, 41.5, 13, 4.5, 1.5, INK)
    e = (rrect(33, 14, 12, 4.5, 1.5, INK) + rrect(37, 27.75, 12, 4.5, 1.5, INK) +
         rrect(33, 41.5, 12, 4.5, 1.5, INK))
    return i + e


@reg("instagram", PINK)
def instagram():
    frame = (f'<rect x="16" y="14" width="32" height="32" rx="9" fill="none" '
             f'stroke="{INK}" stroke-width="3.8"/>')
    return frame + _ring(CX, CY, 7.2, INK, 3.8) + circle(41.2, 20.8, 2.2, INK)


@reg("insurgency", TEAL_DEEP)
def insurgency():
    shield = path("M15 12H49V36L32 48L15 36Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    arm = stroke("M22 43L31 28", HOLE, 7)
    fist = rrect(26, 15, 16, 14, 3.5, HOLE)
    fingers = "".join(line(x, 15, x, 21, INK, 1.8, "butt") for x in (30, 34, 38))
    thumb = line(26.5, 24.5, 35, 24.5, INK, 1.8)
    return shield + arm + fist + fingers + thumb


@reg("insync", LIGHT_BLUE)
def insync():
    stem = rrect(31, 29, 6, 17, 3, INK)
    dot = circle(34, 23, 3.2, INK)
    arcs = (stroke(arc(34, 23, 8, 180, 270), INK, 3.4) +
            stroke(arc(34, 23, 14, 180, 270), INK, 3.4))
    return g(stem + dot + arcs, "translate(-2 1)")


@reg("intel", BLUE_DEEP)
def intel():
    swoosh = stroke("M44 16.5C52 20 51 31 41 36C31 41 17 41 14.5 35C12.5 30 17 23.5 25 20.5", INK, 2.4)
    word = (line(18, 28, 18, 35, INK, 2.3) + circle(18, 24.8, 1.4, INK) +
            stroke("M21.5 35V28M21.5 30.5C21.5 28 26 28 26 30.5V35", INK, 2.3) +
            stroke("M29 24.5V33C29 34.5 30 35 31.5 35M27.3 28H31.3", INK, 2.3) +
            stroke("M34 31.5H39C39 29 37.8 27.7 36.5 27.7C35 27.7 34 29 34 31.5C34 34 35.2 35 36.8 35"
                   "C37.8 35 38.5 34.6 39 34", INK, 2.3) +
            line(42, 23, 42, 35, INK, 2.3))
    return swoosh + word


def _ij():
    box = rrect(16, 14, 32, 32, 2.5, INK)
    i = stroke("M21 20.5H27M24 20.5V32M21 32H27", HOLE, 3)
    j = stroke("M37 20.5V29C37 31.5 35.8 32.5 33.5 32.5", HOLE, 3)
    bar = rrect(21, 38, 12, 3.2, 0.6, HOLE)
    return box + i + j + bar


@reg("intellij-idea-ce", BLUE_DEEP)
@reg("intellij", PINK_LIGHT)
def intellij():
    return _ij()


@reg("internet-chat", LIGHT_BLUE_DEEP)
def internet_chat():
    back = path("M27 12H46A3 3 0 0 1 49 15V36H30A3 3 0 0 1 27 33Z", LIGHT_BLUE_SOFT)
    front = path("M17 22H38A3 3 0 0 1 41 25V45A3 3 0 0 1 38 48H21A3 3 0 0 1 18 45V26L14 22Z", INK,
                 f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    lines = "".join(rrect(22, y, w, 2.4, 1.2, HOLE) for y, w in [(28.5, 15), (33.5, 15), (38.5, 10)])
    return back + front + lines


@reg("internet-mail", ORANGE_DEEP)
def internet_mail():
    back = path("M15 28L32 14L49 28Z", ORANGE_SOFT,
                f' stroke="{ORANGE_SOFT}" stroke-width="3" stroke-linejoin="round"')
    letter = rrect(20, 15, 24, 24, 2.5, INK)
    at = (_ring(32, 26, 4.5, HOLE, 2.2) +
          stroke("M36.5 26V27.5C36.5 29.5 39.5 29.5 39.5 26.5A7.5 7.5 0 1 0 35.5 32.8", HOLE, 2.2))
    body = path("M15 30L32 40L49 30V45A3 3 0 0 1 46 48H18A3 3 0 0 1 15 45Z", INK,
                f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    return back + letter + at + body


@reg("internet-web-browser", INDIGO)
def web_browser():
    planet = circle(CX, CY, 12.5, INK)
    ellipse = '<ellipse cx="32" cy="30" rx="19" ry="5.5" fill="none" stroke="{c}" stroke-width="{w}" transform="rotate(-25 32 30)"/>'
    front_gap = g(stroke("M13 30A19 5.5 0 0 0 51 30", HOLE, 6.5), "rotate(-25 32 30)")
    front = g(stroke("M13 30A19 5.5 0 0 0 51 30", INK, 3), "rotate(-25 32 30)")
    back = ellipse.format(c=INK, w=3)
    return back + planet + front_gap + front


@reg("internxt-drive", INDIGO_DARK)
def internxt():
    return line(20, 16, 44, 44, INK, 7.5, "square") + line(44, 16, 20, 44, INK, 7.5, "square")


INVESALIUS_HEAD = path('M31 12C40 12 46 18.5 46 26.5L49.5 32.5L46 33.5V38C46 40 44.5 41 42.5 41H38.5V48H22V40C17.5 37 15 32 15 27C15 18.5 22 12 31 12Z', INK)


@reg("invesalius", BLUE_DEEP)
def invesalius():
    head = INVESALIUS_HEAD
    cuts = "".join(line(12, y, 52, y, HOLE, 2.2, "butt") for y in (19, 25, 31, 37, 43))
    return head + cuts


@reg("io.ark.Desktop", RED)
def ark():
    chev = stroke("M16 43L32 16L48 43", INK, 5)
    tri = poly([(32, 31), (38.5, 42), (25.5, 42)], INK, 2)
    cut_ = line(24, 37.2, 40, 37.2, HOLE, 2.2, "butt")
    return chev + tri + cut_


@reg("io.bassi.Amberol", LIGHT_BLUE)
def amberol():
    return circle(CX, CY, 16.5, INK) + poly([(28, 22.5), (40.5, 30), (28, 37.5)], HOLE, 3.5)


@reg("io.botfather.Botfather", PINK)
def botfather():
    bloom = path("M20 18L26 22L32 13L38 22L44 18C45.5 26 45 33 40.5 37.5C37 41 27 41 23.5 37.5"
                 "C19 33 18.5 26 20 18Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    fold = stroke("M26 23.5C26.5 30 29 34 32 36C35 34 37.5 30 38 23.5", HOLE, 2.2)
    leaves = (path("M32 46C27 45.5 21 43 18.5 39C23.5 39 28.5 41 32 46Z", INK) +
              path("M32 46C37 45.5 43 43 45.5 39C40.5 39 35.5 41 32 46Z", INK) +
              line(32, 40, 32, 46, INK, 2.4))
    return bloom + fold + leaves


@reg("io.conduktor.Conduktor", BLUE)
def conduktor():
    hexa = poly([(32, 12.5), (47.5, 21.5), (47.5, 38.5), (32, 47.5), (16.5, 38.5), (16.5, 21.5)], INK, 2)
    cuts = (stroke("M15 23.5L37.5 30.5", HOLE, 3) + stroke("M26.5 29.5L49 36.5", HOLE, 3) +
            stroke("M37.5 30.5L31 37", HOLE, 3) + stroke("M26.5 29.5L33 23", HOLE, 3))
    return hexa + cuts


@reg("io.elementary.appcenter", PURPLE_DEEP)
def appcenter():
    awning = "".join(path(f"M{x} 15A3 3 0 0 1 {x + 3} 12H{x + 6}A3 3 0 0 1 {x + 9} 15V20.5"
                          f"A4.5 4.5 0 0 1 {x} 20.5Z" if False else
                          f"M{x} 12H{x + 9}V20.5A4.5 4.5 0 0 1 {x} 20.5Z",
                          INK if k % 2 == 0 else PURPLE_SOFT)
                     for k, x in enumerate((14, 23, 32, 41)))
    shop = rrect(16, 28, 32, 20, 2.5, INK)
    window = rrect(20, 32, 11, 8, 1.5, HOLE)
    door = path("M35 48V36A4.5 4.5 0 0 1 44 36V48Z", HOLE)
    return awning + shop + window + door


@reg("io.elementary.code", BLUE_GREY_DEEP)
def elementary_code():
    page = rrect(17, 12, 30, 36, 4, INK)
    braces = (stroke("M28 22C25 22 25 23.5 25 26V27.5C25 29 24 30 22.5 30C24 30 25 31 25 32.5V34"
                     "C25 36.5 25 38 28 38", HOLE, 2.6) +
              stroke("M36 22C39 22 39 23.5 39 26V27.5C39 29 40 30 41.5 30C40 30 39 31 39 32.5V34"
                     "C39 36.5 39 38 36 38", HOLE, 2.6))
    return page + braces


@reg("io.elementary.monitor", BLUE_DEEP)
def elementary_monitor():
    gauge = stroke(arc(CX, CY, 15.5, 135, 405), INK, 4)
    pulse = stroke("M20 31H25.5L28 25L31.5 37L35 22L38 31H44", INK, 2.8)
    return gauge + pulse


@reg("io.elementary.tasks", PINK_DEEP)
def elementary_tasks():
    page = rrect(18, 12, 30, 36, 3.5, INK)
    spine = rrect(18, 12, 6, 36, 0, PINK_SOFT)
    rings = "".join(rrect(14, y, 8, 3.4, 1.7, INK) + rrect(14, y, 8, 3.4, 1.7, INK,
                    f' stroke="{HOLE}" stroke-width="1.2"') for y in (16, 23, 30, 37, 44))
    check = stroke("M29 28H43M29 36H38", HOLE, 3.6)
    return page + spine + rings + check


@reg("io.github.ImEditor", RED)
def imeditor():
    i = line(16, 22, 16, 38, INK, 3.4)
    m = stroke("M21 38V29M21 31.5C21 28 26.5 28 26.5 31.5V38M26.5 31.5C26.5 28 32 28 32 31.5V38", INK, 3.2)
    e = stroke("M46.5 23.5C45 22 43.5 21.5 41.5 21.5C38.5 21.5 36.5 23.5 36.5 25.8C36.5 28 38.5 29.8 41.5 29.8"
               "C38 29.8 35.8 31.8 35.8 34.3C35.8 36.8 38 38.5 41.5 38.5C43.5 38.5 45.3 37.8 47 36", INK, 3.2)
    return i + m + e


@reg("io.github.OpenToonz", GREY_DEEP)
def opentoonz():
    board = path("M17 13H47A3 3 0 0 1 50 16V37L38 48H17A3 3 0 0 1 14 45V16A3 3 0 0 1 17 13Z", INK)
    fold = path("M50 37H41A3 3 0 0 0 38 40V48Z", GREY_SOFT)
    o = _ring(25, 27, 6.5, HOLE, 3.6)
    t = line(31.5, 27, 44.5, 27, HOLE, 3.6, "butt") + line(40, 27, 40, 34, HOLE, 3.6)
    return board + fold + o + t


@reg("io.github.Youda008.DoomRunner", GREY_DARK)
def doomrunner():
    d = path("M17 13H30L37 18V41L30 47H23L24.5 43.5V18.5L21 16.5Z", INK)
    cut_ = path("M29 20.5L32 22.5V37.5L29 40Z", HOLE)
    bars = "".join(rrect(42, 13 + k * 8.9, 6, 7.4, 1.2, c) for k, c in
                   enumerate([DEEP_PURPLE_LIGHT, PURPLE_LIGHT, RED_DEEP, DEEP_ORANGE]))
    return d + cut_ + bars


@reg("io.github.achetagames.epic_asset_manager", BLUE_GREY_DARK)
def epic_asset_manager():
    body = path("M19 13H45L47 38H17Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    notch = poly([(27.5, 13), (36.5, 13), (32, 20)], HOLE, 1.5)
    hands = (path("M13 36C15 33 21 32 25 34.5C28.5 36.5 29 41 25.5 42.5L17 45C13.5 46 11.5 43 12.5 40Z",
                  AMBER, f' stroke="{HOLE}" stroke-width="1.8"') +
             path("M51 36C49 33 43 32 39 34.5C35.5 36.5 35 41 38.5 42.5L47 45C50.5 46 52.5 43 51.5 40Z",
                  AMBER, f' stroke="{HOLE}" stroke-width="1.8"'))
    return body + notch + hands


@reg("io.github.cges30901.hmtimer", INDIGO)
def hmtimer():
    return stroke(arc(CX, 31.5, 14, -55, 235), INK, 4.4) + line(32, 13.5, 32, 28, INK, 4.4)


@reg("io.github.diegoivanme.flowtime", GREY_DARK)
def flowtime():
    face = _ring(CX, CY, 14.5, INK, 3.8)
    hands = line(32, 30, 38.5, 19.5, RED_SOFT, 3.2) + line(32, 30, 21.5, 36, LIGHT_BLUE_SOFT, 3.2)
    return face + hands + circle(CX, CY, 3.2, INK) + circle(CX, CY, 1.3, HOLE)


@reg("io.github.dvlv.boxbuddyrs", BROWN_LIGHT)
def boxbuddy():
    box = path("M17 20H47L45.5 47H18.5Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    flap = poly([(34, 12), (45, 14), (47, 20), (35, 20)], GREY_SOFT, 1.5)
    flap_l = poly([(18.5, 14), (32, 14), (31.5, 20), (17, 20)], GREY_SOFT, 1.5)
    face = (circle(26, 30, 2.6, HOLE) + circle(38, 30, 2.6, HOLE) +
            stroke("M28 36C30 38.5 34 38.5 36 36", HOLE, 2.4))
    return flap + flap_l + box + face


@reg("io.github.ezQuake", BLUE_GREY_DARK)
def ezquake():
    c = stroke(arc(35, 30, 13.5, 105, 255), INK, 3.4)
    swoosh = stroke("M36 17C41 15 47 17.5 48 21L34 40C39 43 45 41 48.5 37", INK, 3.4)
    shaft = line(15, 30, 38, 30, INK, 3.2)
    head = poly([(13, 30), (19, 27), (19, 33)], INK, 1.5) + rrect(36.5, 25.5, 3.2, 9, 1.6, INK)
    return c + swoosh + shaft + head


@reg("io.github.flattool.Warehouse", BLUE)
def warehouse():
    frame = rrect(14, 12, 36, 36, 4, INK)
    bays = rrect(17, 15, 30, 13.5, 1.5, HOLE) + rrect(17, 31.5, 30, 13.5, 1.5, HOLE)
    boxes = (rrect(19, 19, 12, 9.5, 1, INK) + rrect(33, 22.5, 11, 6, 1, INK) +
             rrect(24, 35.5, 12, 9.5, 1, INK) + rrect(38, 38.5, 7, 6.5, 1, INK))
    return frame + bays + boxes


@reg("io.github.htkhiem.Euphonica", DEEP_PURPLE_DARK)
def euphonica():
    body = path("M19 24C19 17 24 13 29 13C34 13 37.5 17 38 22C43 25 47 32 50 44"
                "C45 41 41 39 37 39C33 41.5 28 42 24.5 40C20 37.5 18.5 32 19 24Z", AMBER_SOFT)
    wing = path("M28 27C35 26 42 31 46 40C40 38 33 37.5 28 34Z", INK)
    beak = poly([(19.5, 20), (14, 22.5), (19.5, 24)], DEEP_ORANGE_SOFT, 1.5)
    eye = circle(25, 20, 1.8, DEEP_PURPLE_DARK)
    feet = line(26, 41, 25, 46, AMBER_SOFT, 2.2) + line(30.5, 41.5, 30.5, 46.5, AMBER_SOFT, 2.2)
    return body + wing + beak + eye + feet


@reg("io.github.jeffshee.Hidamari", BLUE_GREY)
def hidamari():
    petals = "".join(g(f'<ellipse cx="32" cy="17" rx="3.6" ry="6" fill="{INK}"/>',
                       f"rotate({a} 32 30)") for a in range(0, 360, 30))
    centre = circle(CX, CY, 8.5, HOLE) + circle(CX, CY, 6.8, BROWN_DEEP)
    return petals + centre


@reg("io.github.lainsce.Colorway", GREY_DARK)
def colorway():
    return (_ring(32, 23, 8.5, RED_LIGHT, 3.4) + _ring(25, 35, 8.5, BLUE_GREY_SOFT, 3.4) +
            _ring(39, 35, 8.5, BLUE_LIGHT, 3.4))


@reg("io.github.lainsce.Countdown", ORANGE_DEEP)
def countdown():
    panels = rrect(13, 14, 18, 32, 3.5, INK) + rrect(33, 14, 18, 32, 3.5, INK)
    zero = f'<rect x="17.5" y="21" width="9" height="18" rx="4.5" fill="none" stroke="{HOLE}" stroke-width="3"/>'
    one = line(42, 20.5, 42, 39.5, HOLE, 3)
    return panels + zero + one


@reg("io.github.lainsce.DotMatrix", LIGHT_BLUE_DEEP)
def dotmatrix():
    dots = "".join(circle(x, y, 1.2, LIGHT_BLUE_SOFT) for x in (14, 50) for y in (14, 26, 38, 48))
    wings = (stroke("M32 22C28 13 18 11 17 17C16 23 23 28 32 29", INK, 2.8) +
             stroke("M32 22C36 13 46 11 47 17C48 23 41 28 32 29", INK, 2.8) +
             stroke("M32 29C26 30 19 35 21 41C23 46 30 42 32 34", INK, 2.8) +
             stroke("M32 29C38 30 45 35 43 41C41 46 34 42 32 34", INK, 2.8) +
             line(32, 20, 32, 44, INK, 2.8))
    return dots + wings


@small("ignuit")
def ignuit_s():
    return (rrect(27, 11, 22, 26, 4, INDIGO_DARK) + rrect(15, 20, 24, 29, 4, INK) +
            "".join(rrect(19.5, y, 15, 4, 2, HOLE) for y in (27, 35)))


@small("indicator-cpufreq")
def cpufreq_s():
    pins = ("".join(rrect(x, 10, 5, 7, 2, INK) for x in (22, 34)) +
            "".join(rrect(11, y, 7, 5, 2, INK) for y in (24, 36)))
    return pins + rrect(19, 17, 32, 32, 5, INK) + rrect(28, 26, 14, 14, 2.5, HOLE)


@small("infector")
def infector_s():
    out = ""
    corners = {(0, 0): AMBER_DEEP, (2, 2): AMBER_DEEP, (2, 0): RED, (0, 2): RED}
    for r in range(3):
        for c in range(3):
            x, y = 15 + c * 11.3, 13 + r * 11.3
            if (r, c) in corners:
                out += rrect(x, y, 11.3, 11.3, 2, corners[(r, c)])
            elif (r + c) % 2 == 0:
                out += rrect(x, y, 11.3, 11.3, 1, INK)
    return out


@small("inky")
def inky_s():
    return (circle(CX, CY, 16.5, INK) + circle(28, 32, 6.5, HOLE) + circle(36, 28, 5, HOLE) +
            circle(40, 21, 2.5, HOLE))


@small("intel")
def intel_s():
    swoosh = stroke("M44 16.5C52 20 51 31 41 36C31 41 17 41 14.5 35C12.5 30 17 23.5 25 20.5", INK, 3)
    word = (line(22, 28, 22, 36, INK, 3.4) + circle(22, 23.5, 2, INK) +
            stroke("M28 36V28M28 31C28 27.5 36 27.5 36 31V36", INK, 3.4))
    return swoosh + word


def _ij_s():
    box = rrect(15, 13, 34, 34, 3, INK)
    i = line(24, 20, 24, 33, HOLE, 4.2)
    j = stroke("M36 20V29.5C36 32 34.5 33.5 31.5 33.5", HOLE, 4.2)
    return box + i + j + rrect(20, 38.5, 13, 4, 1, HOLE)


SMALL["intellij"] = _ij_s
SMALL["intellij-idea-ce"] = _ij_s


@small("internet-mail")
def internet_mail_s():
    letter = rrect(19, 13, 26, 24, 3, INK)
    body = path("M14 29L32 40L50 29V45A3 3 0 0 1 47 48H17A3 3 0 0 1 14 45Z", INK,
                f' stroke="{HOLE}" stroke-width="2.5" stroke-linejoin="round"')
    return letter + _ring(32, 24, 4.5, HOLE, 3) + body


@small("invesalius")
def invesalius_s():
    head = INVESALIUS_HEAD
    return head + "".join(line(12, y, 52, y, HOLE, 3, "butt") for y in (22, 31, 40))


@small("io.elementary.appcenter")
def appcenter_s():
    awning = rrect(13, 11, 38, 11, 3, INK)
    shop = rrect(16, 26, 32, 22, 3, INK)
    return awning + shop + path("M34 48V36A5 5 0 0 1 44 36V48Z", HOLE)


@small("io.elementary.tasks")
def elementary_tasks_s():
    return rrect(16, 12, 32, 36, 4, INK) + stroke("M24 28H40M24 37H35", HOLE, 5)


@small("io.github.ImEditor")
def imeditor_s():
    return line(19, 20, 19, 40, INK, 4.4) + stroke(
        "M26 40V30M26 33C26 28.5 33 28.5 33 33V40M33 33C33 28.5 40 28.5 40 33V40", INK, 4)


@small("imperator-rome")
def imperator_s():
    wings = (poly([(29, 24), (12, 18), (15, 31), (29, 34)], INK, 2.5) +
             poly([(35, 24), (52, 18), (49, 31), (35, 34)], INK, 2.5))
    body = path("M32 18C36 18 37 22 36.5 28L35 38L38 44H26L29 38L27.5 28C27 22 28 18 32 18Z", INK)
    return wings + body + circle(33, 17, 4, INK)


@small("infinifactory")
def infinifactory_s():
    top = poly([(32, 12), (49, 21), (32, 30), (15, 21)], INK, 2.5)
    left = poly([(15, 21), (32, 30), (32, 48), (15, 39)], ORANGE_SOFT, 2.5)
    right = poly([(49, 21), (32, 30), (32, 48), (49, 39)], ORANGE_DARK, 2.5)
    return top + left + right


@small("io.github.Youda008.DoomRunner")
def doomrunner_s():
    d = path("M15 13H30L38 18V41L30 47H21L23 43.5V18.5L19 16.5Z", INK)
    return d + path("M29 21L32.5 23V37L29 39.5Z", HOLE) + rrect(42, 13, 7, 34, 2, DEEP_ORANGE)


@small("io.github.lainsce.DotMatrix")
def dotmatrix_s():
    return (stroke("M32 22C28 13 18 11 17 17C16 23 23 28 32 29", INK, 3.4) +
            stroke("M32 22C36 13 46 11 47 17C48 23 41 28 32 29", INK, 3.4) +
            stroke("M32 29C26 30 19 35 21 41C23 46 30 42 32 34", INK, 3.4) +
            stroke("M32 29C38 30 45 35 43 41C41 46 34 42 32 34", INK, 3.4))


@small("io.github.ezQuake")
def ezquake_s():
    c = stroke(arc(35, 30, 13.5, 105, 255), INK, 4)
    z = stroke("M36 18H47L34 41H48", INK, 4)
    return c + z + line(14, 30, 36, 30, INK, 4)


@small("io.github.htkhiem.Euphonica")
def euphonica_s():
    body = path("M18 24C18 16 23 12 29 12C35 12 38.5 16.5 39 22C44 25 48 32 51 45"
                "C45 42 41 40 37 40C33 42.5 27 43 23.5 40.5C19 37.5 17.5 32 18 24Z", AMBER_SOFT)
    return body + poly([(18.5, 19.5), (12.5, 22.5), (18.5, 25)], DEEP_ORANGE_SOFT, 2)


@small("im.srain.Srain")
def srain_s():
    drop = path("M47 13V30A15 15 0 1 1 32 15C38 15 42 13 47 13Z", INK)
    return drop + (line(29, 22, 27, 40, HOLE, 3.6) + line(37, 22, 35, 40, HOLE, 3.6) +
                   line(22.5, 27.5, 41.5, 27.5, HOLE, 3.6) + line(22, 35, 41, 35, HOLE, 3.6))


@small("insync")
def insync_s():
    return (rrect(30, 28, 7, 18, 3.5, INK) + circle(33.5, 21.5, 3.8, INK) +
            stroke(arc(33.5, 21.5, 10.5, 180, 270), INK, 4.2))


@small("insurgency")
def insurgency_s():
    shield = path("M15 12H49V36L32 48L15 36Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return shield + stroke("M22 43L31 28", HOLE, 8) + rrect(24.5, 14.5, 18, 15, 4, HOLE)


@small("incredipede")
def incredipede_s():
    eye = path("M13 31C18 20 26 16.5 33 17C41 17.5 47 22 51 30C46 38.5 38 43.5 31 43.5"
               "C23 43.5 17 38.5 13 31Z", INK)
    return eye + circle(33, 29.5, 9.5, HOLE) + circle(33, 29.5, 5, INK)


@small("io.elementary.monitor")
def elementary_monitor_s():
    return stroke(arc(CX, CY, 15.5, 135, 405), INK, 4) + stroke("M20 31H25L29 22L35 38L39 31H44", INK, 3.4)


@small("io.elementary.code")
def elementary_code_s():
    page = rrect(16, 12, 32, 36, 4, INK)
    return page + (stroke("M28 21C24.5 21 24.5 24 24.5 26V28L21.5 30L24.5 32V34C24.5 36 24.5 39 28 39", HOLE, 3.4) +
                   stroke("M36 21C39.5 21 39.5 24 39.5 26V28L42.5 30L39.5 32V34C39.5 36 39.5 39 36 39", HOLE, 3.4))


@small("io.github.lainsce.Colorway")
def colorway_s():
    return (circle(32, 22.5, 9, RED_LIGHT) + circle(24, 36, 9, AMBER_DEEP) + circle(40, 36, 9, BLUE_LIGHT))


@small("io.github.jeffshee.Hidamari")
def hidamari_s():
    petals = "".join(g(f'<ellipse cx="32" cy="16" rx="5" ry="6.5" fill="{INK}"/>',
                       f"rotate({a} 32 30)") for a in range(0, 360, 45))
    return petals + circle(CX, CY, 9.5, HOLE) + circle(CX, CY, 7.5, BROWN_DEEP)


@small("info.febvre.Komikku")
def komikku_s():
    page = rrect(15, 12, 32, 36, 4, INK)
    return page + line(15, 29, 47, 27, HOLE, 3.2, "butt") + line(31, 12, 30, 28, HOLE, 3.2, "butt")


@small("io.github.diegoivanme.flowtime")
def flowtime_s():
    return (_ring(CX, CY, 14.5, INK, 4.2) + line(32, 30, 38.5, 19.5, RED_SOFT, 4) +
            line(32, 30, 21.5, 36, AMBER, 4))


@small("io.github.OpenToonz")
def opentoonz_s():
    board = path("M17 13H47A3 3 0 0 1 50 16V37L38 48H17A3 3 0 0 1 14 45V16A3 3 0 0 1 17 13Z", INK)
    return board + _ring(25, 28, 6, HOLE, 4.4) + line(31, 28, 45, 28, HOLE, 4.4, "butt") + line(40, 28, 40, 36, HOLE, 4.4)


@small("im.fluffychat.Fluffychat")
def fluffychat_s():
    head = circle(32, 32, 15.5, INK)
    ears = (poly([(17, 25), (18, 11), (28, 19)], INK, 3) + poly([(47, 25), (46, 11), (36, 19)], INK, 3))
    return head + ears + circle(26, 31, 3, HOLE) + circle(38, 31, 3, HOLE)


@small("io.conduktor.Conduktor")
def conduktor_s():
    hexa = poly([(32, 12), (48, 21), (48, 39), (32, 48), (16, 39), (16, 21)], INK, 2)
    return hexa + stroke("M14 23L37.5 30.5L31 37", HOLE, 3.8) + stroke("M50 37L26.5 29.5L33 23", HOLE, 3.8)
