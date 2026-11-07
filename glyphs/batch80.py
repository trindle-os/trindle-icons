# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 80: apps missing from Papirus (Flathub refs and a few found online)."""
from lm import *
from glyphs.kit import arc, ellipse, registry, ring_b, rot_b

ICONS, SMALL, reg, small = registry()

@reg("com.thincast.client", GREY_DEEP)
def thincast():
    return stroke("M13.5 31.5H20L24.5 21L30.5 43L36 15.5L41 36L44 30.5H50.5", INK, 3.6)

@reg("io.github.IshuSinghSE.aurynk", RED_LIGHT)
def aurynk():
    screen = stroke("M20 19.5H44Q50 19.5 50 25.5V35Q50 41 44 41H20Q14 41 14 35V25.5Q14 19.5 20 19.5Z", INK, 3.4)
    wifi = (stroke(arc(32, 38, 8, 225, 315), INK, 2.6) + stroke(arc(32, 38, 4, 225, 315), INK, 2.6)
            + circle(32, 38, 1.6, INK))
    return screen + wifi

@reg("docker", BLUE)
def docker():
    whale = path("M13 30.5H45.5C46.5 28.5 49 27.5 51.5 28.5C50.5 30.5 48.5 31.5 46.5 31.5"
                 "C44 40.5 36 46 26.5 46C18.5 46 13.5 40.5 13 30.5Z", INK)
    boxes = "".join(rrect(x, y, 5, 4.6, 1, INK) for x, y in
                    [(16, 24.5), (21.8, 24.5), (27.6, 24.5), (33.4, 24.5), (39.2, 24.5),
                     (21.8, 19), (27.6, 19), (33.4, 19), (33.4, 13.5)])
    eye = circle(21.5, 36.5, 1.5, HOLE)
    return g(whale + boxes + eye, "translate(0 1)")

@reg("chat.simplex.simplex", LIGHT_BLUE_DEEP)
def simplex():
    small_x = line(17, 30, 30, 43, INDIGO_DARK, 5) + line(30, 30, 17, 43, INDIGO_DARK, 5)
    big_x = line(28, 16, 47, 35, INK, 5) + line(47, 16, 28, 35, INK, 5)
    return small_x + big_x

@reg("io.github.zarestia_dev.rclone-manager", BLUE_DEEP)
def rclone():
    r, w = 7, 5
    top = stroke(arc(32, 22.5, r, 180, 450), BLUE_SOFT, w)
    left = stroke(arc(25, 35, r, 45, 315), INK, w)
    right = stroke(arc(39, 35, r, 270, 540), BLUE_SOFT, w)
    return top + left + right

@reg("io.github.unknownskl.greenlight", ORANGE_DARK)
def greenlight():
    return path("M20.5 41C16 41 13.5 38 13.5 34.5C13.5 31 16 28.3 19.5 28C19.5 22.5 23.5 18.5 29 18.5"
                "C33.5 18.5 37 21.3 38.3 25C39.3 24.5 40.3 24.3 41.5 24.3C46.5 24.3 50.5 28.5 50.5 33"
                "C50.5 37.5 47 41 42.5 41Z", INK)

@reg("io.github.astralvixen.geforce-infinity", BLUE_DEEP)
def geforce_infinity():
    a = path("M16 30C24 21 35 15.5 49 15.5C38 17 29 23 23.5 32Z", INK)
    b = path("M21 35C27 28 36 23.5 47.5 23C38.5 25 32 30 28 37.5Z", INK)
    c = path("M14.5 36C19 35.5 24.5 37.5 29 44C25.5 41.5 20 40 14.5 41Z", INK)
    return g(a + b + c, "translate(0 1)")

@reg("io.github.revisto.drum-machine", DEEP_PURPLE_LIGHT)
def drum_machine():
    pads = "".join(rrect(15 + c * 9, 13.5 + r * 8, 7, 6, 1.8, INK) for r in range(3) for c in range(4))
    rail = rrect(15, 41, 34, 3, 1.5, DEEP_PURPLE_SOFT)
    knob = rrect(26, 38, 6, 9, 2, INK) + rrect(40, 38.5, 4, 8, 2, INK)
    return pads + rail + knob

@reg("app.devsuite.Ptyxis", BLUE_GREY)
def ptyxis():

    hedge = rrect(15, 14, 34, 32, 6, BLUE_GREY_SOFT)
    for k in range(5):
        t = 15 + k * 8.5
        hedge += "".join(circle(x, y, 3.6, BLUE_GREY_SOFT) for x, y in
                         [(t, 14), (t, 46), (15, 14 + k * 8), (49, 14 + k * 8)])
    chev = stroke("M25 21L36 30L25 39", INK, 5.2)
    return hedge + chev

@reg("tabby", CYAN_DEEP)
def tabby():
    side = poly([(20, 14.5), (24, 17.5), (46, 30), (46, 36), (24, 49), (20, 46)], LIGHT_BLUE_DARK, 1.5)
    face = poly([(18, 13), (44, 27.5), (44, 33.5), (18, 48), (18, 40.5), (34.5, 30.5), (18, 20.5)], INK, 1.5)
    return g(side + face, "translate(1 -1)")

@reg("io.github.qwersyk.Newelle", BLUE_DEEP)
def newelle():
    back = path("M20 13.5H34Q38.5 13.5 38.5 18V27.5Q38.5 32 34 32H22L16 36.5V18Q16 13.5 20 13.5Z", INK)
    front = path("M29 25H44Q48.5 25 48.5 29.5V41.5Q48.5 46 44 46H29Q24.5 46 24.5 41.5V29.5Q24.5 25 29 25Z",
                 INDIGO_SOFT, f' stroke="{HOLE}" stroke-width="2.4"')
    prompt = stroke("M29.5 31L34 34.5L29.5 38", INK, 2.6) + line(36, 40, 43, 40, INK, 2.6)
    return back + front + prompt

@reg("best.ellie.StartupConfiguration", CYAN_DEEP)
def startup_config():
    body = path("M32 11.5C37.5 16 39.5 22.5 39 30L37.5 40H26.5L25 30C24.5 22.5 26.5 16 32 11.5Z", INK)
    fins = (path("M26 31L19.5 38.5V44L27 40Z", INK) + path("M38 31L44.5 38.5V44L37 40Z", INK))
    window = circle(32, 25, 3, HOLE)
    flame = path("M29 42.5H35L32 48.5Z", INK)
    return rot_b(body + fins + window + flame, 45, 32, 30)

@reg("io.github.maniacx.BudsLink", DEEP_ORANGE_LIGHT)
def budslink():
    disc_ = circle(CX, CY, 17, BLUE_SOFT) + circle(CX, CY, 13, BLUE_DARK)
    band = stroke(arc(32, 31.5, 8, 180, 360), INK, 2.6)
    cups = rrect(21.5, 30, 4.6, 8, 2, INK) + rrect(37.9, 30, 4.6, 8, 2, INK)
    return disc_ + band + cups

@reg("org.rncbc.qpwgraph", BLUE_GREY_DARK)
def qpwgraph():
    wires = (stroke("M18 17C30 17 34 43 46 43", INK, 3) + stroke("M18 43C30 43 34 17 46 17", INK, 3)
             + line(18, 30, 46, 30, INK, 3))
    nodes = "".join(circle(x, y, 3.8, INK) + circle(x, y, 1.6, HOLE)
                    for x in (16, 48) for y in (17, 30, 43))
    return wires + nodes

@reg("io.github.bhack.mini-eq", BLUE_GREY_DARK)
def mini_eq():
    posts = "".join(line(x, 14, x, 42, INK, 2.8) for x in (20, 32, 44))
    curve = stroke("M20 31L32 21L44 31", ORANGE_LIGHT, 2.8)
    nodes = "".join(circle(x, y, 3.8, ORANGE_LIGHT) + circle(x, y, 1.6, HOLE)
                    for x, y in [(20, 31), (32, 21), (44, 31)])
    bars = "".join(line(x, 47 - h, x, 47, CYAN_SOFT, 2.2) for x, h in [(27, 2), (30, 4), (33, 3), (36, 5), (39, 2)])
    return posts + curve + nodes + bars

@reg("moe.kopuz.kopuz", RED_DARK)
def kopuz():
    neck = line(35, 25, 47, 13, INK, 4.2)
    peg = rrect(44, 10, 7, 5.5, 2, INK, ' transform="rotate(-45 47.5 12.75)"')
    body = path("M37.5 22.5C42 27 40.5 36 33.5 42.5C27 48.5 17 49.5 14.5 43.5"
                "C12 37.5 16.5 29.5 23 25.5C29 21.5 34.5 19.5 37.5 22.5Z", INK)
    hole = circle(22, 36.5, 4.3, HOLE)
    return neck + peg + body + hole

@reg("io.github.dzheremi2.lrcmake-gtk", ORANGE_DARK)
def chronograph():
    book = (path("M14 24C19 22 26 22 31 25V47C26 44 19 44 14 46Z", INK) +
            path("M50 24C45 22 38 22 33 25V47C38 44 45 44 50 46Z", INK))
    note = (line(42.5, 30, 42.5, 39, HOLE, 2.2) + circle(40.3, 39.5, 2.4, HOLE)
            + stroke("M42.5 30L46 31.5", HOLE, 2.2))
    clock = circle(22, 20, 9, INK) + circle(22, 20, 6.8, HOLE) + stroke("M22 15.5V20L25.5 22", INK, 2.2)
    return book + note + clock

@reg("org.learningequality.Kolibri", AMBER)
def kolibri():
    bird = stroke("M32 16C28 19.5 27 26 28.5 32C29.5 36 31 39 31.5 42C32 45.5 29.5 47 28.5 45"
                  "C27.5 43 30 41 32.5 42.5M32 16C35.5 18.5 36.5 24 35.5 30C35 33.5 33.5 37 32.5 40"
                  "M32 16L37.5 12.5", INK, 2.4)
    waves = (stroke(arc(32, 30, 9.5, 150, 210), INK, 2.4) + stroke(arc(32, 30, 14, 145, 215), INK, 2.4)
             + stroke(arc(32, 30, 9.5, -30, 30), INK, 2.4) + stroke(arc(32, 30, 14, -35, 35), INK, 2.4))
    return bird + waves

@reg("net.opentabletdriver.OpenTabletDriver", BLUE_GREY_DARK)
def opentabletdriver():
    tablet = rrect(13.5, 15, 37, 30, 4, INK)
    strip = line(18.5, 20, 18.5, 40, HOLE, 2.4)
    pen = line(26.5, 36.5, 44, 19, HOLE, 3.6) + poly([(24, 39), (25, 35), (28, 38)], HOLE, 1)
    return tablet + strip + pen

@reg("io.gitlab.adhami3310.Converter", PINK_LIGHT)
def switcheroo():
    back = rrect(18, 12.5, 32, 32, 5, PINK_SOFT)
    card = rrect(14, 16, 32, 32, 5, INK)
    arrows = (stroke(arc(30, 32, 8.5, 190, 330), HOLE, 3.2) + poly([(35.5, 22), (39.5, 30.5), (31, 29)], HOLE, 1.2)
              + stroke(arc(30, 32, 8.5, 10, 150), HOLE, 3.2) + poly([(24.5, 42), (20.5, 33.5), (29, 35)], HOLE, 1.2))
    return back + card + arrows

@reg("io.github.giantpinkrobots.varia", BLUE)
def varia():
    arrow = line(28, 13, 28, 27, INK, 3.8) + stroke("M21.5 21.5L28 28L34.5 21.5", INK, 3.8)
    tray = line(19, 32.5, 37, 32.5, INK, 3.4)
    bar = rrect(14, 39, 30, 5.5, 2.75, BLUE_DARK) + rrect(14, 39, 21, 5.5, 2.75, INK)
    dots = "".join(circle(x, y, r, INK) for x, y, r in
                   [(47, 41.5, 2), (45.5, 35.5, 1.6), (49.5, 31, 1.4), (48.5, 25.5, 1.2), (44, 29.5, 1.2)])
    return arrow + tray + bar + dots

@reg("io.github.edewin.corex", TEAL_DARK)
def corex():
    chip = rrect(20, 18, 24, 24, 3.5, INK)
    pins = ""
    for k in (25, 32, 39):
        pins += line(k, 12.5, k, 17, INK, 2.4) + line(k, 43, k, 47.5, INK, 2.4)
        pins += line(14.5, k - 2, 19, k - 2, INK, 2.4) + line(45, k - 2, 49.5, k - 2, INK, 2.4)
    pulse = stroke("M23.5 30.5H27L29.5 25L33 35.5L35.5 28.5L37 30.5H40.5", HOLE, 2.2)
    return chip + pins + pulse

@reg("com.github.tenderowl.frog", CYAN_DEEP)
def frog():
    head = (circle(22.5, 21, 7, INK) + circle(41.5, 21, 7, INK)
            + path("M14 34C14 26 22 22.5 32 22.5C42 22.5 50 26 50 34C50 41.5 42 45.5 32 45.5"
                   "C22 45.5 14 41.5 14 34Z", INK))
    eyes = "".join(circle(x, 20.5, 3.6, HOLE) + circle(x, 20.5, 1.6, INK) for x in (22.5, 41.5))
    mouth = stroke("M20.5 34.5C27 39 37 39 43.5 34.5", HOLE, 2.6)
    return head + eyes + mouth

@reg("io.github.JakubMelka.Pdf4qt", RED_DEEP)
def pdf4qt():
    doc = path("M18.5 12H37L45.5 20.5V45Q45.5 48 42.5 48H21.5Q18.5 48 18.5 45V15Q18.5 12 21.5 12Z", INK)
    fold = poly([(37, 12), (45.5, 20.5), (37, 20.5)], LIGHT_BLUE_SOFT, 1)
    jet = poly([(32, 21), (33.5, 26), (33.5, 30), (41, 35), (41, 37.5), (33.5, 35.5), (33.3, 39.5),
                (36, 42), (36, 43.5), (32, 42.5), (28, 43.5), (28, 42), (30.7, 39.5), (30.5, 35.5),
                (23, 37.5), (23, 35), (30.5, 30), (30.5, 26)], HOLE, 1)
    return doc + fold + jet

@reg("ca.parallel_launcher.ParallelLauncher", INDIGO)
def parallel_launcher():
    out = ""
    for x, y0 in [(15, 17), (27.5, 22), (40, 13)]:
        h = 46 - y0 if x != 27.5 else 26
        y1 = y0 + h
        out += poly([(x, y0 + 3), (x + 4.5, y0 + 5), (x + 4.5, y1), (x, y1 - 2)], GREY_DEEP, 0.8)
        out += poly([(x + 4.5, y0 + 5), (x + 9, y0 + 3), (x + 9, y1 - 2), (x + 4.5, y1)], INK, 0.8)
        out += poly([(x, y0 + 3), (x + 4.5, y0 + 1), (x + 9, y0 + 3), (x + 4.5, y0 + 5)], AMBER_LIGHT, 0.8)
    return out

@reg("io.github.focustimerhq.FocusTimer", RED_LIGHT)
def focus_timer():
    egg = path("M32 12C40.5 12 46.5 23 46.5 33C46.5 42 40 47.5 32 47.5C24 47.5 17.5 42 17.5 33"
               "C17.5 23 23.5 12 32 12Z", INK)
    ticks = "".join(line(x, 35, x, 37.5 if i % 2 else 39, HOLE, 1.8)
                    for i, x in enumerate(range(21, 45, 3)))
    pointer = poly([(32, 41), (34.3, 44.5), (29.7, 44.5)], HOLE, 1)
    band = line(18, 33, 46, 33, HOLE, 1.6)
    return egg + band + ticks + pointer

@reg("com.github.Darazaki.Spedread", DEEP_PURPLE_DEEP)
def spedread():
    paper = rrect(16, 12, 32, 36, 3.5, INK)
    s = stroke("M31 24.5C30 22.5 22 22 22 25.5C22 29 31 28.5 31 32.5C31 36 23 36 21.5 33.5", HOLE, 3)
    r = stroke("M35.5 36V26M35.5 29C36.5 26.5 39 25.5 42 26", HOLE, 3)
    lines = line(21.5, 17, 42.5, 17, DEEP_PURPLE_SOFT, 2.2) + line(21.5, 42, 42.5, 42, DEEP_PURPLE_SOFT, 2.2)
    return paper + s + r + lines

@reg("org.ecosia.Browser", LIGHT_BLUE_DARK)
def ecosia():
    crown = path("M26 42C18.5 42 14.5 37 15.5 31.5C16 28.5 18 26.5 20.5 26C18.5 20 23 14 29 14.5"
                 "C31.5 12.5 36 12.5 38.5 15C44 15 47.5 20 45.5 25.5C49 27.5 50 32 48 36"
                 "C46.5 39.5 43 42 38 42Z", LIGHT_BLUE_SOFT)
    trunk = rrect(28.5, 38, 7, 11, 2, LIGHT_BLUE_SOFT)
    e = stroke("M36.5 21.5H28V35.5H36.5M28 28.5H35", HOLE, 3.2)
    return crown + trunk + e

@reg("io.github.cboxdoerfer.FSearch", GREY_DARK)
def fsearch():
    return ring_b(28, 26, 10.5, INK, 4.4) + line(35.5, 33.5, 47, 45, INK, 5.2)

@reg("com.ktechpit.typingmaster", AMBER)
def typingmaster():
    board = rrect(12.5, 19, 39, 23, 4, INK)
    keys = "".join(rrect(17 + c * 7.8, 23.5, 5.2, 4.4, 1.2, HOLE) for c in range(4))
    keys += "".join(rrect(17 + c * 7.8, 30.5, 5.2, 4.4, 1.2, WHITE) for c in range(1, 3))
    keys += rrect(17, 30.5, 5.2, 4.4, 1.2, HOLE) + rrect(40.4, 30.5, 5.2, 4.4, 1.2, HOLE)
    return board + keys

@reg("io.github.gopher64.gopher64", BLUE_DEEP)
def gopher64():
    ears = circle(19, 16.5, 4.5, INK) + circle(45, 16.5, 4.5, INK)
    head = path("M32 13C42.5 13 48.5 20 48.5 30C48.5 41 41 47.5 32 47.5C23 47.5 15.5 41 15.5 30"
                "C15.5 20 21.5 13 32 13Z", INK)
    eyes = "".join(circle(x, 25, 5.2, HOLE) + circle(x + 1, 25.5, 2.3, INK) for x in (24.5, 39.5))
    snout = ellipse(32, 35.5, 7.5, 5.5, AMBER_LIGHT)
    nose = ellipse(32, 32, 3.2, 2.2, BROWN_DARK)
    teeth = rrect(28.8, 38, 3, 4.6, 0.8, INK) + rrect(32.2, 38, 3, 4.6, 0.8, INK)
    return ears + head + eyes + snout + nose + teeth

@reg("org.pvermeer.WebAppHub", RED_DEEP)
def webapphub():
    win = rrect(13, 14, 38, 30, 4, INK)
    bar = "".join(circle(18 + i * 4, 19, 1.3, HOLE) for i in range(3))
    top = line(13, 23, 51, 23, HOLE, 1.6)
    blocks = rrect(18, 28, 13, 11, 2, HOLE) + rrect(34.5, 28, 12, 4, 2, RED_SOFT) + rrect(34.5, 35, 9, 4, 2, RED_SOFT)
    hand = path("M13 44C15.5 40 19.5 39 22 41.5L26 45.5C27 46.5 26 48 24.5 47.5L18 47.5Q14 47.5 13 44Z", RED_SOFT)
    return win + bar + top + blocks + hand

@reg("windsurf", TEAL)
def windsurf():
    return stroke("M13.5 20L20.5 34.5C22 37.5 25.5 36.5 25.5 33.5V26C25.5 22.5 29.5 21.5 31.5 24.5"
                  "L38.5 36C40 38.5 44 37.5 44 34.5V26.5C44 23.5 46.5 22 50.5 22", INK, 5)

def _ente_e():
    return cut("M33.5 18.5C42.5 18.5 49 24.5 49 33V35.5H27.5C28.5 38.5 31 40.5 35 40.5C38 40.5 40.5 39.5 42 38"
            "L47 43C44 46 39.5 48 34.5 48C25 48 18 41.5 18 33C18 24.5 24.5 18.5 33.5 18.5Z"
            "M27.8 30H39.5C38.5 27 36.2 25.5 33.6 25.5C31 25.5 28.8 27 27.8 30Z", INK)

@reg("ente-auth", DEEP_PURPLE_LIGHT)
def ente_auth():
    e = _ente_e()
    shield = path("M19.5 11L26 13.5V18.5C26 22.5 23.5 25 19.5 26.5C15.5 25 13 22.5 13 18.5V13.5Z",
                  YELLOW_LIGHT, f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    return e + shield

def _plug(fill):
    head = path("M26 30.5L33.5 38C35 39.5 35 42 33.5 43.5L31 46C29 48 26 48 24 46L18 40"
                "C16 38 16 35 18 33L20.5 30.5C22 29 24.5 29 26 30.5Z", fill)
    prongs = line(19.5, 43.5, 15.5, 47.5, fill, 2.6) + line(24, 48, 21.5, 50.5, fill, 2.6)
    return head + prongs

@reg("armcord", INDIGO_LIGHT)
def armcord():
    cord = stroke("M31.5 34.5C37 29 34 24.5 29 23C23 21 18 17 17.5 13.5M31.5 34.5"
                  "C38 28 44 26 47 30C49.5 34 47.5 39 44.5 45", INK, 2.6)
    return cord + _plug(INK)

@reg("legcord", DEEP_PURPLE)
def legcord():
    cord = stroke("M30.5 33.5C35 29 37 25 37 21C37 16 40.5 13 44.5 13C48.5 13 50 16.5 48.5 19.5"
                  "C47 22 43.5 22 42.5 19.5C41.5 17.5 43 16 44.5 16.5", INK, 2.8)
    return cord + _plug(INK)

@reg("chatgpt", TEAL)
def chatgpt():

    link = "M27.75 31.3V22.2A6 6 0 0 1 39.75 22.2"
    out = "".join(rot_b(stroke(link, INK, 3), 60 * k) for k in range(6))
    return g(out, "translate(32 30) scale(1.12) translate(-32 -30)")

@reg("claude", DEEP_ORANGE_DEEP)
def claude():
    rays = ""
    for i, (a, r) in enumerate([(0, 17), (28, 14.5), (58, 16.5), (88, 13.5), (118, 17), (148, 14.5),
                                (180, 16.5), (210, 14), (240, 17), (268, 13.5), (298, 16.5), (330, 14.5)]):
        x, y = pt(CX, CY, r, a - 90)
        xa, ya = pt(CX, CY, 1.5, a - 90 + 90)
        xb, yb = pt(CX, CY, 1.5, a - 90 - 90)
        rays += poly([(xa, ya), (x, y), (xb, yb)], INK, 2.6)
    return rays + circle(CX, CY, 3.2, INK)

@small("org.learningequality.Kolibri")
def kolibri_s():
    bird = stroke("M32 15C27.5 19 27 28 30 36C31 39 32 42 32 45M32 15C36.5 19 37 28 34 36"
                  "C33 39 32 42 32 45", INK, 3)
    waves = stroke(arc(32, 30, 12, 145, 215), INK, 3) + stroke(arc(32, 30, 12, -35, 35), INK, 3)
    return bird + waves

@small("io.github.edewin.corex")
def corex_s():
    chip = rrect(18, 16, 28, 28, 4, INK)
    pins = ""
    for k in (26, 38):
        pins += line(k, 11, k, 15, INK, 3) + line(k, 45, k, 49, INK, 3)
        pins += line(13, k - 2, 17, k - 2, INK, 3) + line(47, k - 2, 51, k - 2, INK, 3)
    return chip + pins + stroke("M22 30.5H26L29.5 23.5L34 37L37.5 30.5H42", HOLE, 3)

@small("io.github.dzheremi2.lrcmake-gtk")
def chronograph_s():
    book = (path("M13 26C18.5 24 25.5 24 31 27V48C25.5 45 18.5 45 13 47Z", INK) +
            path("M51 26C45.5 24 38.5 24 33 27V48C38.5 45 45.5 45 51 47Z", INK))
    clock = circle(24, 19, 9.5, INK) + circle(24, 19, 6.5, HOLE) + stroke("M24 15V19.5L27 21", INK, 2.6)
    return book + clock

@small("io.github.revisto.drum-machine")
def drum_machine_s():
    return "".join(rrect(14 + c * 13, 15 + r * 12, 10, 9, 2.5, INK) for r in range(3) for c in range(3))

@small("io.github.bhack.mini-eq")
def mini_eq_s():
    posts = "".join(line(x, 14, x, 46, INK, 3) for x in (19, 32, 45))
    curve = stroke("M19 33L32 22L45 33", ORANGE_LIGHT, 3)
    nodes = "".join(circle(x, y, 4.5, ORANGE_LIGHT) for x, y in [(19, 33), (32, 22), (45, 33)])
    return posts + curve + nodes

@small("org.rncbc.qpwgraph")
def qpwgraph_s():
    wires = stroke("M18 17C30 17 34 43 46 43", INK, 3.4) + stroke("M18 43C30 43 34 17 46 17", INK, 3.4)
    nodes = "".join(circle(x, y, 4.6, INK) for x in (16, 48) for y in (17, 43))
    return wires + nodes

@small("chatgpt")
def chatgpt_s():
    link = "M27.75 31.3V22.2A6 6 0 0 1 39.75 22.2"
    out = "".join(rot_b(stroke(link, INK, 2.4), 60 * k) for k in range(6))
    return g(out, "translate(32 30) scale(1.2) translate(-32 -30)")

@small("com.ktechpit.typingmaster")
def typingmaster_s():
    board = rrect(11, 17, 42, 27, 5, INK)
    keys = "".join(rrect(16 + c * 11.5, 22.5 + r * 9, 8, 6, 1.8, HOLE) for r in range(2) for c in range(3))
    return board + keys

@small("org.pvermeer.WebAppHub")
def webapphub_s():
    win = rrect(12, 13, 40, 33, 5, INK)
    return win + line(12, 22, 52, 22, HOLE, 2.6) + rrect(18, 28, 14, 12, 2.5, HOLE)

@small("io.github.focustimerhq.FocusTimer")
def focus_timer_s():
    egg = path("M32 11C41 11 47.5 22.5 47.5 33C47.5 42.5 40.5 48 32 48C23.5 48 16.5 42.5 16.5 33"
               "C16.5 22.5 23 11 32 11Z", INK)
    return egg + line(17, 33, 47, 33, HOLE, 3) + poly([(32, 37.5), (35.5, 43), (28.5, 43)], HOLE, 1)

@small("com.github.Darazaki.Spedread")
def spedread_s():
    paper = rrect(15, 11, 34, 38, 4, INK)
    s_ = stroke("M38 22C36.5 19 26 18.5 26 23.5C26 28.5 38 27.5 38 33.5C38 39 27 39.5 25.5 36", HOLE, 4)
    return paper + s_

@small("io.github.JakubMelka.Pdf4qt")
def pdf4qt_s():
    doc = path("M17 11H37L47 21V46Q47 49 44 49H20Q17 49 17 46V14Q17 11 20 11Z", INK)
    fold = poly([(37, 11), (47, 21), (37, 21)], LIGHT_BLUE_SOFT, 1)
    jet = (line(32, 22, 32, 42, HOLE, 4) + poly([(22, 36), (42, 36), (32, 28)], HOLE, 2)
           + line(28, 42, 36, 42, HOLE, 3))
    return doc + fold + jet

def _plug_s():
    head = path("M26.5 29L35 37.5C36.5 39 36.5 41.5 35 43L31.5 46.5C30 48 27.5 48 26 46.5L17.5 38"
                "C16 36.5 16 34 17.5 32.5L21 29C22.5 27.5 25 27.5 26.5 29Z", INK)
    return head + line(19, 44.5, 14.5, 49, INK, 3.4) + line(24, 49, 21.5, 51.5, INK, 3.4)

@small("armcord")
def armcord_s():
    return stroke("M32 33C39 26 45 26 47 31C48.5 35 47 40 44 45", INK, 3) + _plug_s()

@small("legcord")
def legcord_s():
    return stroke("M31 32C35.5 27.5 37.5 23 37.5 19.5C37.5 15 41 12.5 44.5 12.5C48 12.5 50 15.5 49 18.5", INK, 3.2) + _plug_s()

@small("io.github.giantpinkrobots.varia")
def varia_s():
    arrow = line(32, 11, 32, 26, INK, 4.4) + stroke("M24.5 19.5L32 27L39.5 19.5", INK, 4.4)
    tray = line(20, 32.5, 44, 32.5, INK, 4)
    bar = rrect(14, 39.5, 36, 7, 3.5, BLUE_DARK) + rrect(14, 39.5, 24, 7, 3.5, INK)
    return arrow + tray + bar

@small("io.gitlab.adhami3310.Converter")
def switcheroo_s():
    card = rrect(12, 12, 40, 36, 6, INK)
    arrows = (stroke(arc(32, 30, 9, 200, 330), HOLE, 3.6) + poly([(37.5, 19.5), (42, 28.5), (32.5, 27)], HOLE, 1.2)
              + stroke(arc(32, 30, 9, 20, 150), HOLE, 3.6) + poly([(26.5, 40.5), (22, 31.5), (31.5, 33)], HOLE, 1.2))
    return card + arrows

@small("io.github.gopher64.gopher64")
def gopher64_s():
    ears = circle(18, 16, 5, INK) + circle(46, 16, 5, INK)
    head = ellipse(32, 30.5, 17.5, 17, INK)
    eyes = "".join(circle(x, 25, 5.5, HOLE) + circle(x, 25.5, 2.6, INK) for x in (24, 40))
    teeth = rrect(27.5, 36, 4, 7, 1, HOLE) + rrect(32.5, 36, 4, 7, 1, HOLE)
    return ears + head + eyes + teeth

@small("io.github.maniacx.BudsLink")
def budslink_s():
    disc_ = circle(CX, CY, 18, LIGHT_BLUE_SOFT) + circle(CX, CY, 13, LIGHT_BLUE_DARK)
    band = stroke(arc(32, 31.5, 8, 180, 360), INK, 3)
    cups = rrect(20.5, 29.5, 6, 9, 2.5, INK) + rrect(37.5, 29.5, 6, 9, 2.5, INK)
    return disc_ + band + cups

@small("io.github.astralvixen.geforce-infinity")
def geforce_infinity_s():
    a = path("M14 32C22.5 21 34.5 14.5 50 14.5C38 17 29 24 23.5 34Z", INK)
    b = path("M21 38C28 29 37 24 49 23.5C39.5 26 32.5 32 28.5 41Z", INK)
    return a + b

@small("ca.parallel_launcher.ParallelLauncher")
def parallel_launcher_s():
    out = ""
    for x, y0, y1 in [(13, 16, 44), (27, 22, 48), (41, 12, 42)]:
        out += rrect(x, y0, 10, y1 - y0, 1.5, INK) + rrect(x, y0 - 1, 10, 5, 1.5, AMBER_LIGHT)
    return out

@small("docker")
def docker_s():
    whale = path("M12 30H46C47 28 49.5 27 52 28C51 30 49 31 47 31C44.5 40.5 36 46.5 26 46.5"
                 "C17.5 46.5 12.5 40.5 12 30Z", INK)
    boxes = "".join(rrect(x, y, 7, 6.5, 1.3, INK) for x, y in
                    [(16, 21.5), (24.5, 21.5), (33, 21.5), (24.5, 13), (33, 13)])
    return whale + boxes

@small("claude")
def claude_s():
    rays = ""
    for a in range(0, 360, 45):
        r = 17 if a % 90 == 0 else 14.5
        x, y = pt(CX, CY, r, a - 90)
        xa, ya = pt(CX, CY, 2.2, a)
        xb, yb = pt(CX, CY, 2.2, a - 180)
        rays += poly([(xa, ya), (x, y), (xb, yb)], INK, 3)
    return rays + circle(CX, CY, 4, INK)

@small("ente-auth")
def ente_auth_s():
    return _ente_e()
