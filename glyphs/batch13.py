# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 13: chromium-dev to com.belmoussaoui.Decoder."""
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_LIGHT, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP,
    BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT, BROWN_SOFT, circle,
    CX, CY, CYAN_DEEP, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_ORANGE_SOFT, DEEP_PURPLE,
    DEEP_PURPLE_LIGHT, f, g, GREY, GREY_DARK, GREY_DEEP, GREY_LIGHT, GREY_SOFT, HOLE, INDIGO,
    INDIGO_DARK, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, line,
    ORANGE, ORANGE_DEEP, ORANGE_LIGHT, ORANGE_SOFT, path, PINK, PINK_LIGHT, poly, pt,
    PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke,
    TEAL_DEEP, TEAL_LIGHT,
)
from glyphs.kit import arc, _chrome, registry, ring_b

ICONS, SMALL, reg, small = registry()


@reg("chromium-dev", BLUE_DARK)
def chromium_dev():
    logo = g(_chrome(), "translate(32 23.5) scale(.68) translate(-32 -30)")
    band = rrect(16.5, 37.5, 31, 11.5, 4, INK)
    dev = stroke("M21.5 40.5V46H23.3Q26.3 46 26.3 43.25Q26.3 40.5 23.3 40.5Z"
                 "M34.5 40.5H30V46H34.5M30 43.25H33.5M37.5 40.5L40 46L42.5 40.5", HOLE, 2)
    return logo + band + dev


@reg("com.beakerbrowser.Beaker", INDIGO)
def beaker():
    return ring_b(31, 31, 12.5, INK, 6.5) + rrect(40, 14.5, 7.5, 7.5, 2.5, INK)


@reg("cinny", GREY_DARK)
def cinny():
    bird = path("M15.5 40C20 35.5 22.5 31 23 26C23.5 19.5 27.5 15.5 33 15.5C36.5 15.5 39 17 40.5 19.5"
                "C44 19.5 47.5 20.5 49.5 22.5C46 22 42.5 22.3 41 23.5C41 30 39 35 36.5 39"
                "C35 41.5 34 44 33.5 47C26.5 46 20 43.5 15.5 40Z", INK)
    return bird + circle(35.5, 20.5, 1.8, HOLE)


@reg("ciano", CYAN_DEEP)
def ciano():
    out = ""
    for rot in (0, 180):
        head = poly([pt(CX, CY, 7.5, 316), pt(CX, CY, 16.5, 316), pt(CX, CY, 12, 346)], INK, 2)
        out += g(stroke(arc(CX, CY, 12, 200, 318), INK, 4.2) + head, f"rotate({rot} 32 30)")
    return out


@reg("cider", PINK)
def cider():
    return ring_b(CX, CY, 15, INK, 3.8) + poly([(28, 22.5), (39.5, 30), (28, 37.5)], INK, 3)


@reg("cine-encoder", BLUE_GREY_DEEP)
def cine_encoder():
    diamond = g(rrect(17.5, 15.5, 29, 29, 7, INK), "rotate(45 32 30)")
    ce = (stroke("M30.3 26A5 5 0 1 0 30.3 34", HOLE, 3.2) +
          stroke("M40.5 25.2H35.2V34.8H40.5M35.2 30H39.5", HOLE, 3.2))
    return diamond + ce


@reg("cinelerra", AMBER_DEEP)
def cinelerra():
    strip = rrect(13, 14, 38, 32, 4, INK)
    holes = "".join(rrect(16.2 + 6.4 * k, y, 3.2, 2.6, 1, HOLE)
                    for k in range(6) for y in (16, 41.4))
    frames = rrect(17, 21, 13.5, 18, 2, HOLE) + rrect(33.5, 21, 13.5, 18, 2, HOLE)
    return strip + holes + frames


@reg("cinema4d", INDIGO_DARK)
def cinema4d():
    ball = circle(CX, CY, 16.5, INK)
    inner = circle(35, 27, 11, INDIGO)
    swoosh = path("M22 17.5C28 14 38 13.5 44 16C47.5 17.5 48.5 21 48 25"
                  "C46.5 21 44 18.5 40 17.5C35 16.3 28 16.5 22 17.5Z", INK)
    return ball + inner + swoosh


@reg("clementine", ORANGE_DEEP)
def clementine():
    outer = path("M18 15C13.5 23 14.5 35.5 22 42C28 47.5 38.5 47.5 49 42.5"
                 "C41 38.5 33.5 33 28.5 27C24.5 22.5 21 18 18 15Z", INK)
    inner = path("M20.2 20.5C18.3 27.5 19.5 35 24.5 39.5C29 43.5 36 44.5 42.5 42.2"
                 "C36 38.5 30.5 34 26.5 29.5C23.8 26.5 21.8 23.5 20.2 20.5Z", ORANGE_SOFT)
    return outer + inner


@reg("cockos-reaper", DEEP_ORANGE_DEEP)
def reaper():
    pick = path("M15 22C15 15 22 12.5 32 12.5C42 12.5 49 15 49 22"
                "C49 32 40 42.5 32 48C24 42.5 15 32 15 22Z", INK)
    return pick + stroke("M17.5 22.5C23 17 30.5 16.5 34 21C37.5 26.5 34.5 37 32.5 46", HOLE, 2.8)


@reg("claudia", RED_DARK)
def claudia():
    base = f'<ellipse cx="32" cy="39" rx="14" ry="5.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    note = line(35, 14, 35, 36, INK, 3) + f'<ellipse cx="31.2" cy="36.5" rx="5" ry="3.8" fill="{INK}"/>'
    return base + note + stroke("M35 14.5C38 16 41 17 42 21", INK, 3)


@reg("claudia-launcher", RED_DARK)
def claudia_launcher():
    base = f'<ellipse cx="32" cy="39" rx="14" ry="5.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    return base + line(32, 39, 32, 20, INK, 3.4) + poly([(25.5, 22), (32, 13), (38.5, 22)], INK, 2.5)


@reg("colortone", LIGHT_BLUE_DARK)
def colortone():
    return (circle(CX, CY, 16.5, TEAL_LIGHT) + circle(CX, CY, 12.5, BLUE_GREY_SOFT) +
            circle(CX, CY, 8.5, AMBER_LIGHT) + circle(CX, CY, 4.8, RED_LIGHT))


@reg("clipgrab", BLUE)
def clipgrab():
    return (circle(CX, CY, 16.5, INK) + line(32, 19, 32, 34, HOLE, 5.5) +
            poly([(23.5, 31), (40.5, 31), (32, 41.5)], HOLE, 3))


@reg("clion", TEAL_DEEP)
def clion():
    sq = rrect(15, 13, 34, 34, 3, INK)
    cl = (stroke("M29 21.2A5 5 0 1 0 29 28.8", HOLE, 3.2) +
          stroke("M33.5 20V30H40", HOLE, 3.2))
    return sq + cl + rrect(20.5, 38.5, 12, 3.2, 1.6, HOLE)


@reg("code-oss", BLUE_DARK)
def code_oss():
    pills = "".join(rrect(27, y, w, 4.4, 2.2, INK) for y, w in
                    [(14.5, 10), (21.2, 18), (27.9, 15), (34.6, 18), (41.3, 11)])
    return line(21.5, 14, 21.5, 46, INK, 4.4) + pills


@reg("codeblocks", BLUE_GREY_DARK)
def codeblocks():
    return "".join(rrect(x, y, 14, 14, 3, c) for (x, y), c in
                   [((17.5, 15.5), RED), ((32.5, 15.5), BROWN_SOFT),
                    ((17.5, 30.5), AMBER), ((32.5, 30.5), BLUE)])


@reg("codelite", BLUE_GREY_DARK)
def codelite():
    return "".join(rrect(x, y, 18, 18, 3.5, c, f' stroke="{HOLE}" stroke-width="2"')
                   for (x, y), c in [((15, 13), AMBER_SOFT), ((22.5, 20.5), GREY),
                                     ((30, 28), BLUE_LIGHT)])


@reg("cointop", BLUE_GREY_DARK)
def cointop():
    bracket = stroke("M22 15H18V45H22", INK, 3.4)
    bars = "".join(rrect(25, y, w, 3.6, 1, INK) for y, w in
                   [(15.5, 22), (21.3, 7), (27.1, 7), (32.9, 12), (38.7, 22)])
    return bracket + bars


@reg("colorpicker", DEEP_PURPLE)
def colorpicker():
    out = ""
    for y, c, kx in [(20, RED_LIGHT, 40), (30, GREY, 27), (40, BLUE_LIGHT, 35)]:
        out += rrect(15, y - 2, 34, 4, 2, c) + circle(kx, y, 4.6, INK)
    return out


@reg("colon", ORANGE_DEEP)
def colon():
    frame = rrect(15.5, 13.5, 33, 33, 3, "none", f' stroke="{INK}" stroke-width="3.6"')
    return frame + stroke("M37 24.7A7.5 7.5 0 1 0 37 35.3", INK, 4.6)


@reg("cinnamon-virtual-keyboard", GREY_DEEP)
def cinnamon_keyboard():
    kb = rrect(13, 18, 38, 24, 5, INK)
    keys = "".join(rrect(17 + 5.2 * c, 22 + 5.4 * r, 3.6, 3.4, 1, HOLE)
                   for r in range(2) for c in range(6))
    return kb + keys + rrect(22, 33.5, 20, 3.4, 1.2, HOLE)


@reg("cisco-anyconnect", LIGHT_BLUE_DEEP)
def anyconnect():
    return ring_b(30, 31, 15, INK, 3.8) + ring_b(37.5, 26.5, 9, ORANGE_LIGHT, 4.4)


@reg("citrix-receiver", BLUE_DEEP)
def citrix():
    return (stroke(arc(CX, CY, 15, 70, 380), INK, 3.8) +
            stroke(arc(CX, CY, 9.5, 70, 380), INK, 3.8) + circle(CX, CY, 3.3, INK))


@reg("clight", BLUE_GREY_DEEP)
def clight():
    cam = circle(32, 27, 14.5, INK) + circle(32, 27, 9.5, HOLE) + circle(32, 27, 5.8, INK)
    stand = line(32, 41, 32, 45, INK, 3.4) + rrect(24, 44, 16, 4, 2, INK)
    return cam + stand


@reg("clawsker", ORANGE_DEEP)
def clawsker():
    card = rrect(20, 12, 24, 21, 3, INK)
    keys = "".join(rrect(23 + 5 * c, 15.5 + 5 * r, 3, 3, 0.8, HOLE) for r in range(2) for c in range(4))
    env = path("M14 29L32 40L50 29V43A3 3 0 0 1 47 46H17A3 3 0 0 1 14 43Z", INK,
               f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"')
    badge = circle(45, 42, 8, LIGHT_BLUE_DEEP, f' stroke="{HOLE}" stroke-width="2"')
    pencil = line(41.5, 45.5, 48, 39, INK, 3)
    return card + keys + env + badge + pencil


@reg("clockify", LIGHT_BLUE)
def clockify():
    c = stroke(arc(30, 30, 12.5, 45, 315), INK, 5)
    arms = line(40, 25.5, 45, 20.5, INK, 4.6) + line(40, 34.5, 45, 39.5, INK, 4.6)
    return c + arms + circle(35, 30, 3, INK)


@reg("cmyktool", GREY_DEEP)
def cmyktool():
    return "".join(g(rrect(cx - 5.8, cy - 5.8, 11.6, 11.6, 2.5, c), f"rotate(45 {cx} {cy})")
                   for (cx, cy), c in [((32, 17.5), LIGHT_BLUE_LIGHT), ((19.5, 30), PINK_LIGHT),
                                       ((44.5, 30), AMBER_LIGHT), ((32, 42.5), BLUE_GREY_DARK)])


@reg("com.adrienplazas.Metronome", RED_DEEP)
def metronome():
    body = poly([(27.5, 13), (36.5, 13), (46, 46), (18, 46)], INK, 3)
    inner = poly([(29.5, 18), (34.5, 18), (41, 41), (23, 41)], HOLE, 1)
    return body + inner + line(32, 38, 41, 16, INK, 3) + circle(32, 38, 3.2, INK)


@reg("com.amazon.Workspaces", DEEP_ORANGE_DEEP)
def workspaces():
    def cube(cx, cy, s):
        h = s / 2
        top = poly([(cx, cy - s), (cx + s, cy - h), (cx, cy), (cx - s, cy - h)], INK, 1.5)
        left = poly([(cx - s, cy - h), (cx, cy), (cx, cy + s * 1.1), (cx - s, cy + s * 1.1 - h)], DEEP_ORANGE_SOFT, 1.5)
        right = poly([(cx + s, cy - h), (cx, cy), (cx, cy + s * 1.1), (cx + s, cy + s * 1.1 - h)], DEEP_ORANGE_DARK, 1.5)
        return top + left + right
    return cube(34, 31, 13.5) + cube(18.5, 17, 4.2)


@reg("com.belmoussaoui.Decoder", BLUE_GREY_DARK)
def decoder():
    out = ""
    for x, y in [(15, 13), (37, 13), (15, 35)]:
        out += rrect(x, y, 12, 12, 2.5, INK) + rrect(x + 2.3, y + 2.3, 7.4, 7.4, 1.5, HOLE) + rrect(x + 4, y + 4, 4, 4, 1, INK)
    for x, y in [(30, 13), (30, 19.5), (37, 36), (43, 36), (40, 42), (45, 44), (30, 40), (22, 26)]:
        out += rrect(x, y, 4, 4, 0.8, INK)
    return out + rrect(12, 28.5, 40, 3, 1.5, RED_LIGHT)


@reg("cities-skylines", LIGHT_BLUE_DEEP)
def cities():
    cs = stroke("M29 17H20.5V33H29M43.5 17H35V25H43V33H34.5", INK, 5)
    town = path("M14 46V41H17V37.5H20.5V41.5H23V36H26.5V40H29.5V38.5H33V35H36V40.5"
                "H39V37.5H43V40H46V36.5H50V46Z", INK)
    return cs + town


@reg("cities-skylines-2", BLUE)
def cities2():
    v = [pt(CX, CY, 16, a) for a in (-30, -90, 210, 150, 90, 30)]
    outer = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in v), INK, 5.5)
    inner = [pt(CX, CY, 6.5, a) for a in range(-90, 270, 60)]
    return outer + stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in inner) + "Z", INK, 3.6)


@reg("citra", ORANGE_DEEP)
def citra():
    out = circle(CX, CY, 16.5, INK) + circle(CX, CY, 13.2, HOLE) + circle(CX, CY, 11.5, INK)
    out += "".join(line(CX, CY, *pt(CX, CY, 12, 22.5 + 45 * k), HOLE, 2.2) for k in range(8))
    return out + circle(CX, CY, 2.6, HOLE)


@reg("civilization-beyond-earth", BLUE_GREY_DEEP)
def civ_be():
    hexa = poly([pt(CX, CY, 16, a) for a in range(-90, 270, 60)], INK, 3)
    spokes = "".join(line(*pt(CX, CY, 5, a), *pt(CX, CY, 13, a), HOLE, 2.4)
                     for a in range(-90, 270, 60))
    return hexa + spokes + ring_b(CX, CY, 4.8, HOLE, 2.4)


@reg("civilization5", AMBER_DARK)
def civ5():
    return line(21.5, 15, 32, 44, INK, 6.5) + line(42.5, 15, 32, 44, INK, 5)


@reg("civilization6", DEEP_ORANGE_DARK)
def civ6():
    return (line(17.5, 16, 25.5, 43, INK, 6) + line(34, 16, 25.5, 43, INK, 6) +
            line(44, 16, 44, 43, INK, 6))


@reg("ckb-next", BLUE_GREY_DARK)
def ckb_next():
    sails = ""
    for k, (x, top) in enumerate([(19, 30), (24.5, 25.5), (30, 21), (35.5, 16.5)]):
        sails += stroke(f"M{f(x)} 40C{f(x + 1.5)} {f(top + 6)} {f(x + 3)} {f(top + 2)} {f(x + 5)} {f(top)}", INK, 3.4)
    sails += path("M41 14.5C47 18 49.5 25 47.5 31L41.5 29C43.5 24 43 19 41 14.5Z", INK)
    hull = path("M14 44C24 43 36 39 47.5 30C46 38 40 45 29 46.5C23 47.3 18 46.5 14 44Z", INK)
    return sails + hull


@reg("clamav", RED_DEEP)
def clamav():
    horns = (path("M21 29C17 25 16 19 18.5 13C20 18 23 21 27 22Z", INK) +
             path("M43 29C47 25 48 19 45.5 13C44 18 41 21 37 22Z", INK))
    head = circle(32, 33, 14, INK)
    eyes = (poly([(22.5, 30), (29.5, 33.5), (28, 37), (23.5, 35.5)], HOLE, 1.5) +
            poly([(41.5, 30), (34.5, 33.5), (36, 37), (40.5, 35.5)], HOLE, 1.5))
    return horns + head + eyes


@reg("classic-racers", BLUE_GREY_DARK)
def classic_racers():
    return "".join(poly([(16 + 7.5 * i, 41), (23 + 7.5 * i, 19), (27.5 + 7.5 * i, 19), (20.5 + 7.5 * i, 41)],
                        ORANGE if i == 3 else INK, 1.5) for i in range(4))


@reg("clustertruck", BLUE_GREY_DEEP)
def clustertruck():
    box = rrect(16, 13, 32, 29, 5, INK) + rrect(20.5, 19, 23, 14, 3.5, HOLE)
    return box + rrect(19, 40, 7, 7, 2, INK) + rrect(38, 40, 7, 7, 2, INK)


@reg("cockatrice", BLUE_DEEP)
def cockatrice():
    bird = path("M16 46C16 38 20 33 25 31C24 27 24 23 25.5 20.5C23.5 19.5 21.5 19.8 19.5 21"
                "L23 16.5C24.5 15 26.5 14 28.5 14.5L29.5 11.5L31.5 14L33.5 11.5L34.5 15"
                "L37 14L36 17.5C37.5 19.5 37 22 35.5 24.5C34 27 33.5 29 34 31"
                "C39 29 44.5 25.5 49 21C47.5 30 42.5 36 36.5 39C38 41.5 38 44 37 46Z", INK)
    return bird + circle(30, 18.5, 1.6, HOLE)


@reg("colobot", ORANGE_DEEP)
def colobot():
    c = stroke(arc(34, 31, 10.5, 50, 310), INK, 7)
    arm = rrect(13, 16.5, 16, 7, 3.5, INK) + circle(17, 20, 1.8, HOLE)
    bolts = circle(*pt(34, 31, 10.5, 215), 2.4, HOLE) + circle(*pt(34, 31, 10.5, 140), 1.8, HOLE)
    return c + arm + bolts


@reg("codes.nora.gDiceRoller", RED_DEEP)
def dice():
    die = rrect(15, 13, 34, 34, 7, INK)
    return die + "".join(circle(x, y, 3.2, HOLE) for x, y in
                         [(22.5, 20.5), (41.5, 20.5), (32, 30), (22.5, 39.5), (41.5, 39.5)])


@reg("clickup-desktop", DEEP_PURPLE_LIGHT)
def clickup():
    return stroke("M21.5 28L32 19.5L42.5 28", INK, 5.2) + stroke("M19.5 35.5C26.5 44 37.5 44 44.5 35.5", INK, 5.2)


HUG = [(-90, GREY, GREY_SOFT), (150, RED_LIGHT, RED_SOFT), (30, BLUE_LIGHT, BLUE_SOFT)]


def _hug(cx=CX, cy=CY, k=1.0, cols=None, dots=True):
    out = ""
    for a, c, d in (cols or HUG):
        x, y = pt(cx, cy, 7.8 * k, a)
        out += circle(x, y, 8.8 * k, c, f' stroke="{HOLE}" stroke-width="2"')
    if dots:
        for a, c, d in (cols or HUG):
            x, y = pt(cx, cy, 10 * k, a)
            out += circle(x, y, 2.4 * k, d)
    return out + poly([pt(cx, cy, 3.6 * k, a) for a in range(-90, 270, 60)], HOLE, 1)


def _badge(sym, colour):
    return circle(43.5, 41, 8.5, colour, f' stroke="{HOLE}" stroke-width="2.2"') + sym


@reg("colorhug", BLUE_GREY_DARK)
def colorhug():
    return _hug()


@reg("colorhug-ccmx", BLUE_GREY_DARK)
def colorhug_ccmx():
    return _hug(cols=[(-90, GREY_LIGHT, BLUE_LIGHT), (150, GREY, RED_LIGHT), (30, GREY_SOFT, BLUE_LIGHT)])


@reg("colorhug-backlight", BLUE_GREY_DARK)
def colorhug_backlight():
    bulb = circle(43.5, 39.5, 3.8, INK) + rrect(41.5, 42, 4, 3.5, 1, INK)
    return _hug(28.5, 26.5, .9) + _badge(bulb, BLUE_LIGHT)


@reg("colorhug-flash", BLUE_GREY_DARK)
def colorhug_flash():
    sym = stroke(arc(43.5, 41, 4.3, 300, 210), INK, 2.4) + poly([(46, 35.5), (49.5, 37.5), (46, 39.5)], INK, 1)
    return _hug(28.5, 26.5, .9) + _badge(sym, RED_LIGHT)


@reg("colorhug-refresh", BLUE_GREY_DARK)
def colorhug_refresh():
    return _hug(28.5, 26.5, .9) + _badge(circle(43.5, 41.5, 2.8, INK), PURPLE_SOFT)


@small("chromium-dev")
def chromium_dev_s():
    logo = g(_chrome(), "translate(32 24) scale(.7) translate(-32 -30)")
    return logo + rrect(18, 39.5, 28, 6, 3, INK)


@small("cinnamon-virtual-keyboard")
def cinnamon_keyboard_s():
    kb = rrect(12, 17, 40, 26, 5, INK)
    keys = "".join(rrect(17 + 8 * c, 22, 6, 5, 1.2, HOLE) for c in range(4))
    return kb + keys + rrect(21, 32, 22, 5, 1.5, HOLE)


@small("cinelerra")
def cinelerra_s():
    return rrect(13, 14, 38, 32, 4, INK) + rrect(17, 19, 13.5, 22, 2, HOLE) + rrect(33.5, 19, 13.5, 22, 2, HOLE)


@small("clawsker")
def clawsker_s():
    card = rrect(20, 12, 24, 21, 3, INK)
    env = path("M14 29L32 40L50 29V43A3 3 0 0 1 47 46H17A3 3 0 0 1 14 43Z", INK,
               f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"')
    return card + env + circle(45, 42, 8.5, PURPLE_LIGHT, f' stroke="{HOLE}" stroke-width="2.4"')


@small("cointop")
def cointop_s():
    bars = "".join(rrect(25, y, w, 5, 1.5, INK) for y, w in [(16, 22), (27.5, 12), (39, 22)])
    return stroke("M22 15H18V45H22", INK, 3.6) + bars


@small("colorhug")
def colorhug_s():
    return _hug(dots=False)


@small("colorhug-ccmx")
def colorhug_ccmx_s():
    return _hug(cols=[(-90, GREY_LIGHT, ""), (150, GREY, ""), (30, GREY_SOFT, "")], dots=False)


@small("colorhug-backlight")
def colorhug_backlight_s():
    return _hug(28.5, 26.5, .9, dots=False) + _badge(circle(43.5, 40, 4, INK), BLUE_LIGHT)


@small("colorhug-flash")
def colorhug_flash_s():
    return _hug(28.5, 26.5, .9, dots=False) + _badge(stroke(arc(43.5, 41, 4, 300, 210), INK, 2.6), RED_LIGHT)


@small("colorhug-refresh")
def colorhug_refresh_s():
    return _hug(28.5, 26.5, .9, dots=False) + _badge(circle(43.5, 41.5, 3, INK), PURPLE_SOFT)


@small("com.amazon.Workspaces")
def workspaces_s():
    s, cx, cy = 15, 32, 30
    h = s / 2
    return (poly([(cx, cy - s), (cx + s, cy - h), (cx, cy), (cx - s, cy - h)], INK, 1.5) +
            poly([(cx - s, cy - h), (cx, cy), (cx, cy + s * 1.1), (cx - s, cy + s * 1.1 - h)], DEEP_ORANGE_SOFT, 1.5) +
            poly([(cx + s, cy - h), (cx, cy), (cx, cy + s * 1.1), (cx + s, cy + s * 1.1 - h)], DEEP_ORANGE_DARK, 1.5))


@small("com.belmoussaoui.Decoder")
def decoder_s():
    out = ""
    for x, y in [(14, 12), (37, 12), (14, 35)]:
        out += rrect(x, y, 13, 13, 3, INK) + rrect(x + 3.5, y + 3.5, 6, 6, 1.5, HOLE)
    out += rrect(38, 37, 5, 5, 1, INK) + rrect(44, 43, 5, 5, 1, INK)
    return out + rrect(12, 28, 40, 4, 2, RED_LIGHT)


@small("ckb-next")
def ckb_next_s():
    sails = "".join(stroke(f"M{f(x)} 40C{f(x + 1.5)} {f(top + 6)} {f(x + 3)} {f(top + 2)} {f(x + 5)} {f(top)}", INK, 4)
                    for x, top in [(21, 28), (29, 21)])
    sails += path("M38 15C45 18 49 25 47 31L40 29C42.5 24 41.5 19 38 15Z", INK)
    hull = path("M14 44C24 43 36 39 47.5 30C46 38 40 45 29 46.5C23 47.3 18 46.5 14 44Z", INK)
    return sails + hull


@small("citrix-receiver")
def citrix_s():
    return stroke(arc(CX, CY, 14, 70, 380), INK, 4.4) + circle(CX, CY, 5, INK)


@small("cine-encoder")
def cine_encoder_s():
    diamond = g(rrect(16.5, 14.5, 31, 31, 7, INK), "rotate(45 32 30)")
    return diamond + stroke("M29.5 24.5A6 6 0 1 0 29.5 35.5", HOLE, 2.6) + stroke("M40 24H35V36H40M35 30H39", HOLE, 2.6)


@small("citra")
def citra_s():
    out = circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.8, HOLE) + circle(CX, CY, 10.5, INK)
    return out + "".join(line(CX, CY, *pt(CX, CY, 11, 30 + 60 * k), HOLE, 2.2) for k in range(6))


@small("clion")
def clion_s():
    sq = rrect(14, 12, 36, 36, 3, INK)
    cl = stroke("M29.5 20.5A6 6 0 1 0 29.5 31.5", HOLE, 2.8) + stroke("M34.5 19.5V32H41", HOLE, 2.8)
    return sq + cl + rrect(20, 39, 14, 3.4, 1.7, HOLE)
