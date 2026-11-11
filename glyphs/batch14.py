# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 14: com.belmoussaoui.Obfuscate to com.github.bartzaalberg.lottery."""
import math
from lm import (
    AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, BLUE_LIGHT, BLUE_SOFT, BROWN, BROWN_LIGHT, circle, CX, CY, CYAN_DARK,
    CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE_DEEP, f, g,
    GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO_LIGHT, INK, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_SOFT, line, ORANGE_DEEP, path, PINK, PINK_DEEP, poly, pt, PURPLE, PURPLE_DEEP,
    PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DEEP, rrect, stroke, TEAL_LIGHT,
)
from glyphs.kit import ellipse_c, registry, ring_b, sector, star_b

ICONS, SMALL, reg, small = registry()


@reg("com.belmoussaoui.Obfuscate", BLUE)
def obfuscate():
    card = path("M18 17H32V43H18A4 4 0 0 1 14 39V21A4 4 0 0 1 18 17Z", INK)
    chip = rrect(17.5, 33, 10, 3, 1.5, HOLE)
    pix = "".join(rrect(33.5 + c * 5.5, 17 + r * 6.5, 5.5, 6.5, 0, INK)
                  for r in range(4) for c in range(3) if (r + c) % 2 == 0)
    edge = rrect(33.5, 17, 16.5, 26, 3, "none").replace(
        'fill="none"', f'fill="none" stroke="{INK}" stroke-width="2.2"')
    bar = rrect(30, 11, 4.5, 38, 2.25, INK, f' stroke="{HOLE}" stroke-width="1.6"')
    return card + chip + edge + pix + bar


@reg("com.belmoussaoui.ReadItLater", BROWN)
def readitlater():
    frame = rrect(15, 12, 34, 36, 4, "none").replace(
        'fill="none"', f'fill="none" stroke="{INK}" stroke-width="3"')
    shelf = line(15, 30, 49, 30, INK, 3, "butt")
    books = ""
    for y0, row in [(28.5, [(19, 4, 11), (24, 4, 9), (29, 3.5, 11), (34, 4, 8), (39, 4, 11)]),
                    (46.5, [(19, 4, 9), (24, 4, 11), (29, 4, 10), (35.5, 3.5, 11), (40.5, 4, 8)])]:
        for x, w, h in row:
            books += rrect(x, y0 - h, w, h, 1, INK)
    return frame + shelf + books


@reg("com.bitstower.Markets", GREY_DARK)
def markets():
    screen = rrect(14, 14, 36, 31, 5, INK)
    zig = stroke("M17.5 33H21L24 26.5L27.5 36L30.5 24L34 31L37 22.5L40 28L43 25H46.5", HOLE, 2.8)
    cursor = line(34, 17.5, 34, 41.5, HOLE, 2)
    return screen + zig + cursor


@reg("com.bixense.PasswordCalculator", AMBER_DEEP)
def passwordcalculator():
    k = (circle(20, 30, 8.5, INK) + circle(17, 30, 3, HOLE) +
         rrect(25, 27, 25, 6, 2, INK) + rrect(38, 31, 4.5, 6.5, 1, INK) +
         rrect(44.5, 31, 4.5, 8, 1, INK))
    return g(k, "rotate(40 32 30)")


@reg("com.bladecoder.adventure-editor", GREY_DARK)
def adventure_editor():
    head = circle(35, 15.5, 3.8, INK)
    body = stroke("M34.5 21L31.5 31", INK, 4.2)
    arms = stroke("M26.5 28L33.5 22.5L39.5 27.5", INK, 3)
    legs = stroke("M31.5 31L26 39.5L19 42.5M31.5 31L38 38L39.5 46H43.5", INK, 3.4)
    return head + body + arms + legs


@reg("com.chatterino.chatterino", BLUE_DEEP)
def chatterino():
    c = stroke("M43.5 21A12.5 12.5 0 1 0 43.5 39", INK, 8.5)
    tail = poly([(19.5, 37), (15, 47), (27, 42)], INK, 2)
    return c + tail


@reg("com.dhsdevelopments.Climaxima", BLUE_DEEP)
def climaxima():
    corner = path("M14 14H26C26 21 21 26 14 26Z", BLUE_LIGHT,
                  f' stroke="{BLUE_LIGHT}" stroke-width="2" stroke-linejoin="round"')
    sigma = stroke("M46 17H26L36 30L26 43H46", INK, 4.8)
    return corner + sigma


@reg("com.eduke32.EDuke32", BLUE_DEEP)
def eduke32():
    base = ring_b(CX, CY, 15, INK, 3)
    blades = "".join(path(sector(CX, CY, 5, 12, a - 30, a + 30), INK,
                          f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
                     for a in (-150, -30, 90))
    return base + blades + circle(CX, CY, 3, INK)


@reg("com.endlessm.HatchPreviewer", BLUE_GREY_DARK)
def hatchpreviewer():
    cx, cy, r = 29, 30, 13.5
    a, b = pt(cx, cy, r, -35), pt(cx, cy, r, 35)
    pac = path(f"M{cx} {cy}L{f(a[0])} {f(a[1])}A{r} {r} 0 1 0 {f(b[0])} {f(b[1])}Z", INK)
    return pac + circle(46, 30, 3.2, DEEP_ORANGE_LIGHT)


@reg("com.endlessm.photos", ORANGE_DEEP)
def endless_photos():
    screen = rrect(14, 12, 36, 25, 4, INK)
    hills = poly([(17.5, 34), (17.5, 29), (23.5, 24.5), (28.5, 28), (35.5, 20),
                  (40.5, 25), (46.5, 21.5), (46.5, 34)], HOLE, 1.5)
    slider = line(17, 44, 47, 44, INK, 2.6) + circle(37, 44, 4, INK)
    return screen + hills + slider


@reg("com.endlessnetwork.aqueducts", LIGHT_BLUE_DEEP)
def aqueducts():
    pipe = rrect(26, 20, 24, 11, 2.5, INK)
    collar = rrect(26, 16, 7, 19, 2, INK, f' stroke="{HOLE}" stroke-width="1.6"')
    water = "".join(rrect(x, y, 5.5, 5.5, 0.8, LIGHT_BLUE_SOFT)
                    for x, y in [(20, 26), (20, 31.5), (14.5, 31.5), (14.5, 37), (14.5, 42.5)])
    return water + pipe + collar


@reg("com.endlessnetwork.dragonsapprentice", PURPLE_DEEP)
def dragonsapprentice():
    pts = []
    turns = 2.6
    for k in range(0, 121):
        t = k / 120 * turns * 2 * math.pi
        r = 1.5 + 13.5 * t / (turns * 2 * math.pi)
        pts.append((CX + r * math.cos(t + 1.2), CY + r * math.sin(t + 1.2)))
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts)
    return stroke(d, INK, 3.6)


@reg("com.endlessnetwork.fablemaker", DEEP_ORANGE_DEEP)
def fablemaker():
    book = rrect(17, 12, 30, 36, 3.5, INK)
    spine = line(22.5, 12, 22.5, 48, HOLE, 1.8, "butt")
    ribbon = poly([(36, 12), (43, 12), (43, 26), (39.5, 22.5), (36, 26)], HOLE, 1)
    return book + spine + ribbon


@reg("com.endlessnetwork.frogsquash", LIGHT_BLUE_DEEP)
def frogsquash():
    body = path("M14.5 45C14.5 35 20 28.5 29 26.5L38 23.5C43.5 21.5 49 23 49 27.5"
                "C49 31 45.5 32.5 41 33L35.5 35C32.5 37 31.5 41 31.5 45Z", INK)
    eye = circle(41, 20.5, 5, INK) + circle(41.5, 19.8, 2, HOLE)
    haunch = stroke("M20.5 45C20.5 39.5 24 36 29 36.5", HOLE, 2)
    arm = stroke("M38 32L44.5 42.5H49", INK, 4.5)
    return body + eye + haunch + arm


@reg("com.feaneron.Boatswain", BLUE_GREY_DEEP)
def boatswain():
    dev = rrect(13, 13, 38, 33, 5, INK)
    keys = "".join(rrect(16.25 + c * 11.5, 20 + r * 11.5, 8.5, 8.5, 2, HOLE)
                   for r in range(2) for c in range(3))
    cam = rrect(28, 15.8, 8, 2.2, 1.1, HOLE)
    return dev + keys + cam


@reg("com.frac_tion.teleport", CYAN_DEEP)
def teleport():
    base = ellipse_c(32, 44.5, 13, 3.8, CYAN_DARK)
    rings = (ellipse_c(32, 15.5, 15, 3.8, INK, 3) + ellipse_c(32, 23, 11.5, 3.2, INK, 3) +
             ellipse_c(32, 30, 8, 2.7, INK, 3))
    tip = poly([(27.5, 35), (36.5, 35), (34, 42.5), (30, 42.5)], INK, 2)
    return base + rings + tip


@reg("com.github.ADBeveridge.Raider", GREY_DARK)
def raider():
    paper = path("M22 11H35L41 17V30H22Z", INK)
    fold = path("M35 11V17H41Z", HOLE)
    text = rrect(25, 18, 8, 2.2, 1.1, HOLE) + rrect(25, 22.5, 12, 2.2, 1.1, HOLE)
    body = rrect(14, 27, 36, 12, 3, INK, f' stroke="{HOLE}" stroke-width="1.8"')
    slot = line(18, 31, 46, 31, HOLE, 2)
    strips = "".join(line(x, 40, x, y, INK, 2.6, "butt")
                     for x, y in [(20, 46), (25.5, 48), (31, 45), (36.5, 48), (42, 46.5)])
    return paper + fold + text + body + slot + strips


@reg("com.github.Bleuzen.FFaudioConverter", INDIGO_LIGHT)
def ffaudioconverter():
    z = "M22.5 21.5H30L22.5 29V38.5L41.5 21.5V31L34 38.5H41.5"
    return circle(CX, CY, 16.5, INK) + stroke(z, HOLE, 6.4) + stroke(z, INK, 2.2)


@reg("com.github.GradienceTeam.Gradience", INDIGO_LIGHT)
def gradience():
    roller = rrect(14, 13, 30, 13, 3, INK)
    bands = "".join(rrect(x, 16, 3, 7, 1, HOLE) for x in (18, 23, 28))
    handle = stroke("M44 19.5H48.5V31.5H32V37", INK, 2.8)
    grip = rrect(29, 36, 6, 12.5, 3, INK)
    return roller + bands + handle + grip


@reg("com.github.HypatiaProject.hypatia", BROWN_LIGHT)
def hypatia():
    out = ""
    for r in range(3):
        for c in range(3):
            x, y = 14 + c * 12.5, 12.5 + r * 12.5
            out += rrect(x, y, 11, 11, 2.2, INK)
            out += stroke(f"M{f(x + 3)} {f(y + 6.5)}V{f(y + 4.5)}H{f(x + 8)}V{f(y + 6.5)}", HOLE, 2)
    return out


@reg("com.github.aggalex.wineglass", RED_DEEP)
def wineglass():
    ball = circle(CX, CY, 16.5, INK)
    a, b = pt(CX, CY, 16.3, -68), pt(CX, CY, 16.3, 112)
    cross = line(a[0], a[1], b[0], b[1], HOLE, 3.6, "butt")
    wave = stroke("M15.8 31.5C21 26 26.5 37 32.5 32.5C38 28.5 43 34.5 48.2 29", HOLE, 3.2).replace(
        'stroke-linecap="round"', 'stroke-linecap="butt"')
    return ball + cross + wave


@reg("com.github.aharotias2.parapara", GREY_DEEP)
def parapara():
    return rrect(18, 11, 28, 38, 3, INK) + rrect(21.5, 14.5, 21, 22, 1.5, HOLE)


@reg("com.github.aimproxy.dotfonts", DEEP_PURPLE_DEEP)
def dotfonts():
    return path("M25 16H45L43.3 22.5H33.3L32.3 27H41L39.4 33.5H30.8L28.3 44H19.5Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')


@reg("com.github.alainm23.byte", PINK)
def byte():
    head = g(ellipse_c(27, 0, 6.5, 5, INK), "translate(0 40) rotate(-22 27 0)")
    stem = line(32.5, 39, 32.5, 14, INK, 3.6)
    flag = stroke("M32.5 14C33 21 42.5 22 41 31.5", INK, 3.6)
    return head + stem + flag


@reg("com.github.alainm23.planner", BLUE)
def planner():
    back = g(rrect(19, 14, 26, 32, 4, BLUE_SOFT), "rotate(-8 32 30)")
    front = g(rrect(19, 13, 26, 32, 4, INK), "rotate(6 32 30)")
    tick = stroke("M26 29H38M26 36H34", HOLE, 3.6)
    return back + front + tick


@reg("com.github.alcadica.develop", GREY_SOFT)
def develop():
    teeth = []
    for k in range(8):
        a = k * 45
        teeth += [pt(CX, CY, 12, a - 18), pt(CX, CY, 16, a - 10),
                  pt(CX, CY, 16, a + 10), pt(CX, CY, 12, a + 18)]
    return poly(teeth, INK, 2) + circle(CX, CY, 5.5, HOLE)


@reg("com.github.alcinnz.odysseus", TEAL_LIGHT)
def odysseus():
    eye = path("M13.5 31C19 22 27 18.5 35 18.5C41 18.5 46 21 50.5 26"
               "C45.5 36 37 41 28.5 40.5C22 40 17 36.5 13.5 31Z", INK)
    wing = poly([(15, 14), (27, 19.5), (20.5, 23.5)], INK, 2)
    iris = circle(33, 29.5, 6.8, HOLE) + circle(33, 29.5, 3.2, INK)
    return wing + eye + iris


@reg("com.github.alecaddd.sequeler", BLUE_GREY)
def sequeler():
    out = ""
    for r, y in enumerate((13, 24.5, 36)):
        out += rrect(14, y, 36, 10, 3, INK)
        for k in range(r + 1):
            out += circle(18.5 + k * 4.5, y + 5, 1.6, HOLE)
        for k in range(4):
            x = 35 + k * 3.8
            out += line(x + 1.6, y + 3, x, y + 7, HOLE, 2)
    return out


@reg("com.github.aleksandar-stefanovic.urmsimulator", PURPLE_LIGHT)
def urmsimulator():
    u = stroke("M14.5 21V32.5A4.5 4.5 0 0 0 23.5 32.5V21", INK, 3.6)
    r = stroke("M27.5 39V21H31.5A4.5 4.5 0 0 1 31.5 30H27.5M31.5 30L36 39", INK, 3.6)
    m = stroke("M39.5 39V21L44.5 31L49.5 21V39", INK, 3.6)
    return u + r + m


@reg("com.github.alexhuntley.Plots", BLUE_DEEP)
def plots():
    paper = rrect(14, 14, 36, 31, 3, INK)
    axes = stroke("M19 17V41.5H47", HOLE, 2)
    curve = stroke("M20.5 19C22.5 31 24 39 27 39C30 39 31 27.5 34 27.5C37 27.5 38 34 41 34"
                   "C43.5 34 44.5 31 47 31", HOLE, 2.8)
    return paper + axes + curve


@reg("com.github.allen-b1.news", PINK_DEEP)
def news():
    arcs = (stroke("M19 29A13 13 0 0 1 32 42", INK, 4.6) +
            stroke("M19 18A24 24 0 0 1 43 42", INK, 4.6))
    return arcs + circle(23, 38, 3.8, INK)


@reg("com.github.alonsoenrique.quotes", GREY_DEEP)
def quotes():
    bubble = rrect(15, 13, 34, 28, 6, INK) + poly([(27.5, 39), (36.5, 39), (32, 46)], INK, 2)
    q = ring_b(32, 26.5, 6.8, HOLE, 3.6) + line(35, 30, 39.5, 35, HOLE, 3.6)
    return bubble + q


@reg("com.github.amikha1lov.RecApp", RED)
def recapp():
    corners = stroke("M15 20V16A3 3 0 0 1 18 13H22M42 13H46A3 3 0 0 1 49 16V20"
                     "M49 40V44A3 3 0 0 1 46 47H42M22 47H18A3 3 0 0 1 15 44V40", INK, 3.2)
    dashes = stroke("M28.5 13H35.5M28.5 47H35.5M15 26.5V33.5M49 26.5V33.5", INK, 3.2)
    rec = ring_b(CX, CY, 9.5, INK, 2.6) + circle(CX, CY, 6, INK)
    return corners + dashes + rec


@reg("com.github.appadeia.Taigo", PURPLE_SOFT)
def taigo():
    egg = path("M32 12C41 12 47 22.5 47 32.5C47 42 40.5 48 32 48C23.5 48 17 42 17 32.5"
               "C17 22.5 23 12 32 12Z", INK)
    screen = rrect(24, 21, 16, 15, 4, HOLE)
    btns = circle(26, 41.5, 2.3, HOLE) + circle(32, 43, 2.3, HOLE) + circle(38, 41.5, 2.3, HOLE)
    return egg + screen + btns


@reg("com.github.arshubham.cipher", CYAN_DEEP)
def cipher():
    shackle = stroke("M24.5 28V22.5A7.5 7.5 0 0 1 39.5 22.5V28", INK, 4.2)
    return shackle + rrect(18.5, 27, 27, 20, 4, INK)


@reg("com.github.artemanufrij.findfileconflicts", DEEP_ORANGE)
def findfileconflicts():
    bolt = poly([(36, 11.5), (25, 31), (31.5, 31), (28, 48.5), (40, 27), (33.5, 27)], INK, 1.8)
    left = poly([(13, 26.5), (17.5, 26.5), (17.5, 22.5), (24, 30), (17.5, 37.5),
                 (17.5, 33.5), (13, 33.5)], INK, 1.6)
    right = poly([(51, 26.5), (46.5, 26.5), (46.5, 22.5), (40, 30), (46.5, 37.5),
                  (46.5, 33.5), (51, 33.5)], INK, 1.6)
    return left + right + bolt


@reg("com.github.artemanufrij.graphui", BROWN)
def graphui():
    links = stroke("M28.5 20C21 24.5 21 32 21 39M35.5 20C43 24.5 43 32 43 39"
                   "M32 22V25M29 33L24 39M35 33L40 39", INK, 2.2)
    nodes = (circle(32, 17, 5.2, INK) + rrect(24.5, 25, 15, 8, 2, INK) +
             rrect(13.5, 39, 15, 8, 2, INK) + rrect(35.5, 39, 15, 8, 2, INK))
    return links + nodes


@reg("com.github.artemanufrij.hashit", GREY_DEEP)
def hashit():
    return stroke("M28 15L23.5 45M41 15L36.5 45M17.5 24H47M16.5 36H46", INK, 4.6)


@reg("com.github.artemanufrij.metronome", BLUE_GREY_LIGHT)
def metronome():
    body = poly([(26.5, 13), (37.5, 13), (47, 46), (17, 46)], INK, 3)
    notch = poly([(29, 13), (35, 13), (32, 17.5)], HOLE, 1)
    arm = line(29.5, 38.5, 40.5, 19.5, HOLE, 3)
    bob = circle(29.5, 38.5, 4.5, HOLE) + circle(29.5, 38.5, 2.2, INK)
    return body + notch + arm + bob


@reg("com.github.artemanufrij.playmymusic", LIGHT_BLUE_DEEP)
def playmymusic():
    band = stroke("M18 38V30.5A14 14 0 0 1 46 30.5V38", INK, 4.6)
    cups = rrect(13, 29, 9.5, 17, 4, INK) + rrect(41.5, 29, 9.5, 17, 4, INK)
    return band + cups


@reg("com.github.artemanufrij.playmyvideos", GREY_DARK)
def playmyvideos():
    film = rrect(13, 14, 38, 32, 4, INK)
    holes = "".join(rrect(x, y, 3.4, 3.4, 0.8, HOLE)
                    for x in (15.8, 44.8) for y in (18, 24.5, 31, 37.5))
    play = poly([(28, 22.5), (38.5, 30), (28, 37.5)], HOLE, 2.2)
    return film + holes + play


@reg("com.github.artemanufrij.regextester", GREY_DEEP)
def regextester():
    s = stroke("M13.5 39L17.5 20M19.5 20L23.5 39M30 39L34 20", INK, 3)
    dot = circle(26.8, 37.8, 2, INK)
    gg = ring_b(42.5, 31.5, 4.6, INK, 3) + stroke("M47.1 26.5V40A4.6 4.6 0 0 1 42.5 44.6H39.5", INK, 3)
    return s + dot + gg


@reg("com.github.artemanufrij.showmypictures", CYAN_DEEP)
def showmypictures():
    frame = rrect(14, 12, 36, 36, 3, INK)
    sky = rrect(18, 16, 28, 28, 1.5, HOLE)
    sun = circle(32, 26, 5.5, INK)
    sea = rrect(18, 31, 28, 13, 1.5, CYAN_DARK) + rrect(18, 31, 28, 3, 0, CYAN_DARK)
    glint = stroke("M32 32.5L29.5 35.5L33.5 38.5L30.5 41.5", INK, 2.4)
    cloud = circle(22.5, 20.5, 2.6, INK) + circle(26, 19.8, 3, INK) + rrect(20, 20.5, 9, 3, 1.5, INK)
    return frame + sky + sun + sea + glint + cloud


@reg("com.github.artemanufrij.translit", GREY_DARK)
def translit():
    d = stroke("M15.5 21V39H19.5C24.5 39 27.5 35.5 27.5 30C27.5 24.5 24.5 21 19.5 21Z", INK, 3.6)
    de = stroke("M36.5 21H45.5V38.5M33.5 38.5H48.5M33.5 38.5V43.5M48.5 38.5V43.5"
                "M36.5 21C36.5 29 35.5 34.5 33.5 38.5", INK, 3.4)
    return d + de


@reg("com.github.artemanufrij.webpin", LIGHT_BLUE_DEEP)
def webpin():
    cloud = (circle(24, 31, 7.5, INK) + circle(34.5, 25.5, 10, INK) +
             circle(43, 32, 7, INK) + rrect(15, 30, 35, 13, 6.5, INK))
    w = stroke("M23.5 26L27.5 37L32 29L36.5 37L40.5 26", HOLE, 3.6)
    return cloud + w


@reg("com.github.avojak.iridium", BLUE)
def iridium():
    back = rrect(13, 13, 27, 19, 7, BLUE_DARK) + poly([(16, 29), (15, 36), (22, 31)], BLUE_DARK, 2)
    front = (rrect(21, 24, 30, 19, 7, INK, f' stroke="{HOLE}" stroke-width="1.6"') +
             poly([(43, 41), (50, 47.5), (40, 44)], INK, 2))
    dots = "".join(circle(x, 33.5, 2.1, HOLE) for x in (29.5, 36, 42.5))
    return back + front + dots


@reg("com.github.babluboy.nutty", PURPLE_SOFT)
def nutty():
    nodes = [pt(CX, CY, 14, -90 + 60 * k) for k in range(6)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in nodes) + "Z"
    links = stroke(d, PURPLE, 2.6) + line(32, 16, 32, 44, PURPLE, 2.6)
    return links + "".join(circle(x, y, 4.3, INK) for x, y in nodes + [(CX, CY)])


@reg("com.github.bartzaalberg.alias", LIGHT_BLUE_DEEP)
def alias():
    return (circle(CX, CY, 16.5, INK) +
            stroke("M24.5 40.5L32 19.5L39.5 40.5M27.5 33.5H36.5", HOLE, 4.2))


@reg("com.github.bartzaalberg.bookmark-manager", BLUE_GREY_DEEP)
def bookmark_manager():
    term = rrect(13, 13, 35, 29, 4, INK)
    dollar = stroke("M23.5 19.5C22.5 18.6 21.5 18.2 20.2 18.2C18.5 18.2 17.3 19.2 17.3 20.6"
                    "C17.3 23.8 23.8 22.6 23.8 25.9C23.8 27.4 22.4 28.4 20.4 28.4"
                    "C18.9 28.4 17.8 27.9 16.8 27M20.5 16V30.5", HOLE, 2.2)
    under = rrect(27, 27, 9, 2.8, 1.4, HOLE)
    badge = circle(42, 40, 9, BLUE, f' stroke="{HOLE}" stroke-width="2.2"')
    return term + dollar + under + badge + star_b(42, 40.3, 5.6, 2.5, INK, 1)


@reg("com.github.bartzaalberg.lottery", RED_DEEP)
def lottery():
    crown = poly([(16, 22), (24.5, 30), (32, 18), (39.5, 30), (48, 22), (45, 39), (19, 39)], INK, 2.5)
    balls = circle(16, 20.5, 3, INK) + circle(32, 15.5, 3, INK) + circle(48, 20.5, 3, INK)
    base = rrect(19, 41.5, 26, 5, 2.2, INK)
    return crown + balls + base


@small("com.belmoussaoui.Obfuscate")
def obfuscate_s():
    card = path("M18 17H32V43H18A4 4 0 0 1 14 39V21A4 4 0 0 1 18 17Z", INK)
    pix = rrect(34, 17, 8, 13, 0, INK) + rrect(42, 30, 8, 13, 0, INK)
    bar = rrect(29.5, 11, 5, 38, 2.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    return card + pix + bar


@small("com.belmoussaoui.ReadItLater")
def readitlater_s():
    frame = rrect(15, 12, 34, 36, 4, "none").replace(
        'fill="none"', f'fill="none" stroke="{INK}" stroke-width="3.2"')
    shelf = line(15, 30, 49, 30, INK, 3.2, "butt")
    books = "".join(rrect(x, 30 - h - 1.5 + dy, 5.5, h, 1, INK)
                    for dy in (0, 17.5) for x, h in [(19.5, 11), (28.5, 9), (37.5, 11)])
    return frame + shelf + books


@small("com.bitstower.Markets")
def markets_s():
    return rrect(13, 14, 38, 32, 5, INK) + stroke("M17.5 34L24 26L30 34L36 23L46.5 29", HOLE, 3.4)


@small("com.github.ADBeveridge.Raider")
def raider_s():
    paper = path("M22 11H42V28H22Z", INK)
    body = rrect(13, 26, 38, 13, 3, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    strips = "".join(line(x, 40, x, 47, INK, 3.4, "butt") for x in (21, 28, 35, 42))
    return paper + body + strips


@small("com.github.HypatiaProject.hypatia")
def hypatia_s():
    out = ""
    for r in range(2):
        for c in range(2):
            x, y = 14 + c * 19, 12 + r * 19
            out += rrect(x, y, 17, 17, 3, INK) + rrect(x + 5, y + 6, 7, 3, 1.5, HOLE)
    return out


@small("com.github.alecaddd.sequeler")
def sequeler_s():
    out = ""
    for y in (12.5, 25, 37.5):
        out += rrect(13, y, 38, 10.5, 3, INK) + circle(19, y + 5.25, 2.2, HOLE)
        out += rrect(31, y + 3.8, 15, 3, 1.5, HOLE)
    return out


@small("com.github.artemanufrij.showmypictures")
def showmypictures_s():
    return (rrect(13, 12, 38, 36, 3, INK) + rrect(18, 17, 28, 26, 1.5, HOLE) +
            circle(32, 27, 6, INK) + rrect(18, 32, 28, 11, 1.5, CYAN_DARK))


@small("com.github.artemanufrij.regextester")
def regextester_s():
    return stroke("M15 40L21 20M23 20L29 40M35 40L41 20", INK, 3.6) + circle(47, 38, 3, INK)


@small("com.github.bartzaalberg.bookmark-manager")
def bookmark_manager_s():
    term = rrect(12, 12, 36, 30, 4, INK)
    prompt = stroke("M17 18L22 22.5L17 27", HOLE, 3.2) + rrect(25, 25, 9, 3.2, 1.6, HOLE)
    badge = circle(42, 40, 10, BLUE, f' stroke="{HOLE}" stroke-width="2.4"')
    return term + prompt + badge + star_b(42, 40.3, 6.5, 3, INK, 1)


@small("com.github.babluboy.nutty")
def nutty_s():
    nodes = [pt(CX, CY, 13.5, -90 + 60 * k) for k in range(6)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in nodes) + "Z"
    return stroke(d, LIGHT_BLUE_DARK, 3) + "".join(circle(x, y, 5, INK) for x, y in nodes + [(CX, CY)])


@small("com.endlessnetwork.dragonsapprentice")
def dragonsapprentice_s():
    pts = []
    turns = 1.8
    for k in range(0, 91):
        t = k / 90 * turns * 2 * math.pi
        r = 2 + 13 * t / (turns * 2 * math.pi)
        pts.append((CX + r * math.cos(t + 1.2), CY + r * math.sin(t + 1.2)))
    return stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts), INK, 3.6)


@small("com.eduke32.EDuke32")
def eduke32_s():
    blades = "".join(path(sector(CX, CY, 4.5, 15, a - 30, a + 30), INK) for a in (-150, -30, 90))
    return blades + circle(CX, CY, 2.8, INK)


@small("com.github.Bleuzen.FFaudioConverter")
def ffaudioconverter_s():
    return circle(CX, CY, 16.5, INK) + stroke("M22 21H30L22 29V39L42 21V31L34 39H42", HOLE, 3)


@small("com.github.avojak.iridium")
def iridium_s():
    back = rrect(12, 12, 28, 20, 7, BLUE_DARK)
    front = (rrect(20, 23, 32, 21, 8, INK, f' stroke="{HOLE}" stroke-width="2.2"') +
             poly([(43, 42), (50, 48), (39, 45)], INK, 2))
    return back + front + "".join(circle(x, 33.5, 2.8, HOLE) for x in (28.5, 36, 43.5))


@small("com.github.amikha1lov.RecApp")
def recapp_s():
    corners = stroke("M14 21V15H20M44 15H50V21M50 39V45H44M20 45H14V39", INK, 3.6)
    return corners + circle(CX, CY, 9, INK)


@small("com.github.artemanufrij.graphui")
def graphui_s():
    links = stroke("M32 18V26M26 32L21 40M38 32L43 40", INK, 3)
    return (links + circle(32, 16, 5.5, INK) + rrect(23, 24, 18, 9, 2, INK) +
            rrect(13, 38, 16, 9, 2, INK) + rrect(35, 38, 16, 9, 2, INK))
