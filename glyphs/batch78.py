# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 78: Flathub apps Papirus lacks (gradia to rufin)."""
from lm import *
from glyphs.kit import arc_b, ellipse, ering, registry, ring_e, spiral_b

ICONS, SMALL, reg, small = registry()

@reg("be.alexandervanhee.gradia", BLUE_DEEP)
def gradia():
    w = 3
    corners = (stroke("M14.5 19.5V13.5H20.5", INK, w) + stroke("M43.5 13.5H49.5V19.5", INK, w) +
               stroke("M14.5 40.5V46.5H20.5", INK, w) + stroke("M43.5 46.5H49.5V40.5", INK, w))
    card = rrect(20, 18.5, 24, 23, 4, INK)
    bar = rrect(23.5, 22, 9, 3, 1.5, HOLE) + circle(39, 23.5, 2.3, HOLE)
    row = line(24.5, 30.5, 39.5, 30.5, HOLE, 2.2)
    toggle = rrect(31, 34, 10, 5, 2.5, HOLE) + circle(38.5, 36.5, 1.5, INK) + line(24.5, 36.5, 27.5, 36.5, HOLE, 2.2)
    return corners + card + bar + row + toggle

@reg("org.deskflow.deskflow", LIGHT_BLUE_DEEP)
def deskflow():
    out = ""
    for y in (19, 30, 41):
        out += stroke(f"M15 {y + 2}C20.5 {y - 4.5} 26 {y - 4.5} 32 {y}S43.5 {y + 4.5} 49 {y - 2}", INK, 5)
    return out

@reg("org.mozilla.vpn", DEEP_PURPLE_DEEP)
def mozilla_vpn():
    j = (30, 30)
    nodes = [(21.5, 17.5), (44, 30), (22.5, 42.5)]
    out = ""
    for x, y in nodes:
        out += line(j[0], j[1], x, y, INK, 3.6)
    for x, y in nodes:
        out += circle(x, y, 5, HOLE, f' stroke="{INK}" stroke-width="3.6"')
    return out

@reg("com.vixalien.sticky", AMBER_DARK)
def sticky():
    note = rrect(15.5, 15, 33, 33, 3.5, YELLOW_LIGHT, ' transform="rotate(-6 32 31.5)"')
    ink = (stroke("M21 29C23 25 25.5 25 25.5 28.5C25.5 32 28 32 30 28.5S34.5 26 36 29H42", AMBER_DARK, 2.4) +
           stroke("M21 38.5H27C29 35.5 31 35.5 32 38.5S35.5 41 38 37.5", AMBER_DARK, 2.4))
    pin = line(34, 14, 34, 20, RED_DARK, 2.2) + circle(34, 13.5, 4.5, RED)
    return note + ink + pin

@reg("ai.opencode.opencode", BLUE_GREY_DARK)
def opencode():
    frame = cut("M17 12H47V48H17Z M23 18V42H41V18Z", INK)
    lower = path("M23 30H41V42H23Z", BLUE_GREY_SOFT)
    return frame + lower

@reg("io.github.tobagin.karere", ORANGE_DARK)
def karere():
    bubble = circle(33, 28.5, 15.5, INK) + poly([(20, 35), (16, 47.5), (29, 42)], INK, 2)
    swirl = stroke(spiral_b(33, 28.5, .8, 9.5, 2.3, 180), HOLE, 2.8)
    return bubble + swirl

@reg("org.dupot.easyflatpak", INDIGO_DEEP)
def easyflatpak():
    out = arc_b(32, 30, 16, 60, 300, INK, 3.6)
    for a in (-40, -10, 20, 45):
        out += arc_b(32, 30, 16, a - 7, a + 7, INK, 3.6)
    top = poly([(32, 20.5), (41, 25.5), (32, 30.5), (23, 25.5)], INK, 1)
    left = poly([(23, 27.5), (31, 32), (31, 41.5), (23, 37)], INK, 1)
    right = poly([(33, 32), (41, 27.5), (41, 37), (33, 41.5)], INK, 1)
    return out + top + left + right

@reg("com.keepsolid.VpnUnlimited", LIGHT_BLUE_DEEP)
def vpn_unlimited():
    shield = path("M32 12L47.5 17.5V29C47.5 38.5 41 45 32 48.5C23 45 16.5 38.5 16.5 29V17.5Z", INK,
                  f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    loops = ering(26.5, 29.5, 4.8, 7, HOLE, 3.2) + ering(37.5, 29.5, 4.8, 7, HOLE, 3.2)
    return shield + loops

@reg("io.github.radiolamp.mangojuice", ORANGE_DEEP)
def mangojuice():
    saucer = ellipse(32, 41, 17.5, 7, TEAL)
    glass = path("M19.5 19H44.5V32C44.5 40 39 44.5 32 44.5C25 44.5 19.5 40 19.5 32Z", INK)
    juice = ellipse(32, 19, 12.5, 3.6, ORANGE_SOFT)
    straw = line(36, 21, 43.5, 11.5, INK, 2.8)
    return saucer + glass + juice + straw

@reg("hu.irl.cameractrls", BLUE_GREY_DARK)
def cameractrls():
    outer = cut(cpath(32, 30, 17) + cpath(32, 30, 13.5), INK)
    lens = circle(32, 30, 11.5, INK)
    blades = ""
    for k in range(6):
        a = 60 * k - 90
        x0, y0 = pt(32, 30, 4.8, a)
        x1, y1 = pt(32, 30, 12, a + 62)
        blades += line(x0, y0, x1, y1, HOLE, 1.8, "butt")
    hexa = poly([pt(32, 30, 4.8, 60 * k - 90) for k in range(6)], RED_DEEP)
    return outer + lens + blades + hexa

@reg("io.gitlab.theevilskeleton.Upscaler", TEAL_DARK)
def upscaler():
    frame = cut("M19 12H45A5 5 0 0 1 50 17V43A5 5 0 0 1 45 48H19A5 5 0 0 1 14 43V17A5 5 0 0 1 19 12Z"
                "M18 16V44H46V16Z", INK)
    pink = PINK_SOFT
    petals = (ellipse(25.5, 24, 5.5, 2.8, pink, 35) + ellipse(24, 30, 5.5, 2.8, pink) +
              ellipse(25.5, 36, 5.5, 2.8, pink, -35))
    px = ""
    for x, y in [(33, 19.5), (36.5, 23), (40, 23), (33, 28.5), (36.5, 28.5), (40, 28.5),
                 (36.5, 34), (40, 34), (33, 37.5), (33, 23), (33, 33)]:
        px += f'<rect x="{f(x)}" y="{f(y)}" width="3.5" height="3.5" fill="{pink}"/>'
    divider = line(32, 16, 32, 44, INK, 2.2, "butt")
    return frame + petals + px + divider

@reg("com.github.mtkennerly.ludusavi", PINK_LIGHT)
def ludusavi():
    w = 3.6
    left = circle(16, 14, 2.4, INK) + circle(16, 21.5, 2.4, INK) + stroke("M16 29V46.5H48.5", INK, w)
    box = rrect(24.5, 12.5, 23.5, 23.5, 3, "none", f' stroke="{INK}" stroke-width="{w}"')
    dots = "".join(circle(x, y, 2.4, INK) for x in (31.5, 41) for y in (19.5, 29))
    return left + box + dots

@reg("io.github.giantpinkrobots.flatsweep", RED_DEEP)
def flatsweep():
    hexa = poly([pt(32, 30, 17, -90 + 60 * k) for k in range(6)], INK, 3)
    edges = ""
    for a in (-150, -30, 90):
        x, y = pt(32, 30, 17, a)
        edges += line(32, 30, x, y, HOLE, 2.2)
    can = (path("M36.5 34H44L43.2 43H37.3Z", HOLE) + line(35.5, 32, 45, 32, HOLE, 2) +
           line(38.8, 36, 39, 41, INK, 1.2) + line(41.7, 36, 41.5, 41, INK, 1.2))
    return hexa + edges + can

@reg("io.github.diegopvlk.Cine", CYAN_DEEP)
def cine():
    body = rrect(14, 12, 36, 36, 6, INK)
    holes = "".join(circle(x, 17, 1.8, HOLE) for x in (20, 26, 32, 38, 44))
    screen = rrect(18.5, 21.5, 27, 22, 3, HOLE)
    play = poly([(28.5, 26.5), (28.5, 38.5), (38.5, 32.5)], INK, 2.5)
    return body + holes + screen + play

@reg("dev.fredol.open-tv", BLUE_GREY_DARK)
def open_tv():
    body = rrect(13.5, 12.5, 37, 33, 5, INK)
    cols = [YELLOW, CYAN, AMBER_DEEP, PINK, RED, INDIGO]
    bars = ""
    bw = 29 / 6
    for i, c in enumerate(cols):
        bars += f'<rect x="{f(17.5 + i * bw)}" y="16.5" width="{f(bw + .05)}" height="19" fill="{c}"/>'
    knobs = circle(40, 40.5, 1.8, HOLE) + circle(45, 40.5, 1.8, HOLE) + rrect(18, 39.3, 14, 2.4, 1.2, HOLE)
    legs = line(21, 46, 19, 49, INK, 2.6) + line(43, 46, 45, 49, INK, 2.6)
    return body + bars + knobs + legs

@reg("nl.andreasknoben.Laser", BLUE_GREY_DARK)
def laser():
    tab = rrect(27.5, 11, 9, 7, 2, INK)
    disc = cut(cpath(32, 31, 15.5) + cpath(32, 31, 3), INK)
    groove = ring_e(32, 31, 7, BLUE_GREY_SOFT, 2.2)
    led = circle(45, 44, 3.2, RED)
    return tab + disc + groove + led

@reg("io.gitlab.news_flash.NewsFlash", DEEP_ORANGE_DEEP)
def newsflash():
    paper = rrect(16, 12, 32, 36, 3.5, INK)
    head = rrect(20, 16, 24, 4.5, 1.5, HOLE)
    lines = "".join(line(20.5, y, 43.5, y, HOLE, 2.2) for y in (25, 40, 44))
    band = f'<rect x="16" y="30" width="32" height="5" fill="{HOLE}"/>'
    return paper + head + lines + band

@reg("com.github.KRTirtho.Spotube", INDIGO_DARK)
def spotube():
    band = stroke("M17.5 35V30A14.5 14.5 0 0 1 46.5 30V35", INK, 3.6)
    cups = rrect(14, 31.5, 9, 15, 4, INK) + rrect(41, 31.5, 9, 15, 4, INK)
    return band + cups

@reg("org.kde.koko", PINK_DEEP)
def koko():
    frame = cut("M19 13H45A5 5 0 0 1 50 18V42A5 5 0 0 1 45 47H19A5 5 0 0 1 14 42V18A5 5 0 0 1 19 13Z"
                "M18 17V43H46V17Z", INK)
    sun = circle(30, 31, 6.5, AMBER)
    hills = poly([(18, 43), (18, 36), (25, 31.5), (31, 36), (39, 26.5), (46, 33), (46, 43)], INK)
    return frame + sun + hills

@reg("io.github.screwys.Rufin", DEEP_ORANGE_DEEP)
def rufin():
    base = rrect(14, 12, 36, 36, 6, INK)
    vinyl = circle(29.5, 28, 12, BLUE_GREY_DARK) + ring_e(29.5, 28, 8, GREY_DARK, 1.2)
    label = circle(29.5, 28, 3.6, DEEP_ORANGE_LIGHT)
    arm = stroke("M44 17V32L38 38", BLUE_GREY_DARK, 2.4) + circle(44, 17, 2.6, BLUE_GREY_DARK)
    grille = rrect(19, 43, 26, 2.4, 1.2, HOLE)
    return base + vinyl + label + arm + grille

@reg("com.bilingify.readest", ORANGE_DARK)
def readest():
    left = path("M31 17C26 14 20.5 13.5 14.5 15.5V43C20.5 41 26 41.5 31 44.5Z", INK)
    right = path("M33 17C38 14 43.5 13.5 49.5 15.5V43C43.5 41 38 41.5 33 44.5Z", INK)
    lines = (stroke("M18.5 21C21.5 20.3 24.5 20.5 27 21.5", HOLE, 2) + stroke("M18.5 27C21.5 26.3 24.5 26.5 27 27.5", HOLE, 2) +
             stroke("M37 21.5C39.5 20.5 42.5 20.3 45.5 21", HOLE, 2))
    mark = poly([(38, 36), (38, 48), (40.5, 45.5), (43, 48), (43, 36)], DEEP_ORANGE_LIGHT, 1)
    return left + right + lines + mark

@reg("com.github.k4zmu2a.spacecadetpinball", INDIGO_DARK)
def spacecadet():
    shade = circle(32, 30, 16.5, BLUE_GREY_SOFT)
    ball = circle(30, 28, 14, INK)
    shine = ellipse(25.5, 22.5, 4, 2.6, BLUE_GREY_SOFT, -40)
    return shade + ball + shine

@reg("no.bragefuglseth.Keypunch", AMBER_DARK)
def keypunch():
    keys = (rrect(14.5, 12.5, 16, 16, 4, INK) + rrect(33.5, 12.5, 16, 16, 4, INK) +
            rrect(14.5, 31.5, 16, 16, 4, INK) + rrect(33.5, 31.5, 16, 16, 4, PURPLE_LIGHT))
    k = line(19.5, 16.5, 19.5, 24.5, HOLE, 2.4) + stroke("M25.5 16.5L20 21L25.5 24.5", HOLE, 2.4)
    e = stroke("M45 16.5H38.5V24.5H45M38.5 20.5H43", HOLE, 2.4)
    y = stroke("M19 35.5L22.5 39.5L26 35.5M22.5 39.5V43.5", HOLE, 2.4)
    bolt = poly([(43.5, 34), (37.5, 40.5), (41.3, 40.5), (40, 45.5), (46, 38.5), (42, 38.5)], INK, 1)
    return keys + k + e + y + bolt

@reg("io.github.wivrn.wivrn", TEAL)
def wivrn():
    spikes = (poly([(24, 18), (26, 10.5), (30, 16)], ORANGE, 1.5) +
              poly([(30.5, 15.5), (34, 9), (36.5, 16)], ORANGE, 1.5) +
              poly([(37, 17), (42, 12), (42, 20)], ORANGE, 1.5))
    head = circle(32, 29, 13.5, INK) + ellipse(32, 38, 11, 7.5, INK)
    headset = rrect(15.5, 21.5, 33, 11, 4, BLUE_GREY_DARK) + rrect(19, 24, 26, 2.4, 1.2, BLUE_GREY_LIGHT)
    nostrils = circle(29, 38, 1.3, HOLE) + circle(35, 38, 1.3, HOLE)
    mouth = stroke("M26.5 42C30 44.5 34 44.5 37.5 42", HOLE, 2)
    return spikes + head + headset + nostrils + mouth

@reg("io.github.fastrizwaan.WineZGUI", RED_DARK)
def winezgui():
    swirl = arc_b(32, 30, 16.5, 215, 145, INK, 3.4)
    bowl = path("M25 15.5H39C39 24.5 36.5 29 32 29.5C27.5 29 25 24.5 25 15.5Z", INK)
    wine = path("M25.7 21.5H38.3C37.6 26 35.5 28.2 32 28.5C28.5 28.2 26.4 26 25.7 21.5Z", RED)
    stem = line(32, 29, 32, 40, INK, 2.6) + line(26.5, 41.5, 37.5, 41.5, INK, 2.8)
    return swirl + bowl + wine + stem

@reg("org.luanti.luanti", BLUE_GREY)
def luanti():
    top = poly([(32, 16), (48, 24.5), (32, 33), (16, 24.5)], INK, 1.5)
    pool = poly([(33, 22), (40, 25.5), (35, 28.5), (28, 25)], LIGHT_BLUE_LIGHT, 1)
    left = poly([(16, 24.5), (32, 33), (32, 46), (16, 37.5)], BROWN_SOFT, 1.5)
    right = poly([(32, 33), (48, 24.5), (48, 37.5), (32, 46)], BROWN, 1.5)
    tree = (line(22.5, 22, 22.5, 18, BROWN, 2.4) + poly([(22.5, 10.5), (27.5, 13), (22.5, 15.5), (17.5, 13)], BLUE_GREY_LIGHT, 1) +
            poly([(17.5, 13), (22.5, 15.5), (22.5, 20), (17.5, 17.5)], BLUE_GREY, 1) +
            poly([(22.5, 15.5), (27.5, 13), (27.5, 17.5), (22.5, 20)], BLUE_GREY_DEEP, 1))
    return left + right + top + pool + tree

@reg("app.xmcl.voxelum", BLUE_GREY_DEEP)
def voxelum():
    hexa = poly([pt(32, 30, 17.5, -90 + 60 * k) for k in range(6)], INK, 3)
    x = line(25, 20.5, 39, 39.5, HOLE, 5.5) + line(39, 20.5, 25, 39.5, HOLE, 3.6)
    return hexa + x

@reg("org.fkoehler.KTailctl", BLUE_GREY_DARK)
def ktailctl():
    lit = {(1, 0), (1, 1), (1, 2), (2, 1)}
    out = ""
    for r in range(3):
        for c in range(3):
            fill = INK if (r, c) in lit else BLUE_GREY_LIGHT
            out += rrect(16 + 11.5 * c, 14 + 11.5 * r, 9, 9, 2.5, fill)
    return out

@reg("dev.goats.xivlauncher", BLUE_DARK)
def xivlauncher():
    main = path("M13 47C24 42 36 31 46 12C40 29 30 41 13 47Z", INK)
    loop1 = stroke("M22 30C25 23 30 18 34 17C31 22 29 28 29 34", INK, 2.6)
    loop2 = stroke("M33 28C37 22 42 17 46 15.5C43 21 40 27 40 32", INK, 2.6)
    tail = stroke("M15 34C19 32 23 31.5 27 32", INK, 2.4)
    return main + loop1 + loop2 + tail

@reg("io.github.fastrizwaan.WineCharm", BLUE_GREY_DARK)
def winecharm():
    cols = {-90: LIGHT_BLUE_LIGHT, 0: DEEP_ORANGE_LIGHT, 90: BLUE_SOFT, 180: AMBER}
    out = ""
    for a, c in cols.items():
        tip = pt(32, 30, 1, a)
        cx, cy = pt(32, 30, 11.5, a)
        l = pt(cx, cy, 6.5, a - 90)
        r = pt(cx, cy, 6.5, a + 90)
        out += circle(cx, cy, 6.5, c) + poly([tip, l, r], c)
    out += circle(32, 30, 7, HOLE)
    bowl = path("M28.3 25H35.7C35.7 29.5 34.2 31.5 32 31.8C29.8 31.5 28.3 29.5 28.3 25Z", INK)
    stem = line(32, 31.5, 32, 35, INK, 1.8) + line(29.5, 35.5, 34.5, 35.5, INK, 1.8)
    return out + bowl + stem

@reg("io.github.TeamWheelWizard.WheelWizard", BLUE_GREY_DEEP)
def wheelwizard():
    tyre = cut(cpath(32, 30, 17) + cpath(32, 30, 12.5), INK)
    rim = circle(32, 30, 10.5, INK)
    holes = ""
    for k in range(5):
        a = -90 + 72 * k + 36
        x, y = pt(32, 30, 6.5, a)
        holes += ellipse(x, y, 2.6, 1.9, HOLE, a + 90)
    return tyre + rim + holes + circle(32, 30, 2.2, HOLE)

@reg("com.usebruno.Bruno", BROWN_DARK)
def bruno():
    ears = ellipse(18.5, 27, 5.5, 10.5, ORANGE_DEEP, 18) + ellipse(45.5, 27, 5.5, 10.5, ORANGE_DEEP, -18)
    head = path("M32 14C40 14 45 20 45 28C45 38 40 45 32 45C24 45 19 38 19 28C19 20 24 14 32 14Z", ORANGE_LIGHT)
    eyes = circle(26.5, 28, 2, HOLE) + circle(37.5, 28, 2, HOLE)
    nose = ellipse(32, 34, 3.6, 2.5, HOLE)
    tongue = ellipse(32, 42, 3.2, 4.2, RED)
    mouth = stroke("M27 38.5C29 40.5 31 40.5 32 38.5C33 40.5 35 40.5 37 38.5", HOLE, 2)
    return ears + head + tongue + eyes + nose + mouth

@reg("app.twintaillauncher.ttl", DEEP_PURPLE_DEEP)
def ttl():
    ring_ = arc_b(34, 31, 13, -50, 150, INK, 4.2)
    slash = path("M50 11L22 48L27.5 48L48.5 18Z", INK)
    hair = path("M32 16C23 14 16 19 15.5 27C15 33 12 38 9.5 40.5C17 41 22 36 22.5 30"
                "C24 34 22.5 38 20 41C26 39 28 32 26.5 25C28 21 30 18 32 16Z", INK)
    return ring_ + slash + hair

@reg("org.equicord.equibop", BLUE_GREY_DEEP)
def equibop():
    outer = cut(cpath(32, 30, 17) + cpath(32, 30, 11), INK)
    x0, y0 = pt(32, 30, 12, 160)
    x1, y1 = pt(32, 30, 12, -20)
    bar = line(x0, y0, x1, y1, INK, 5, "butt")
    hub = circle(32, 30, 5.5, INK) + circle(32, 30, 2.4, HOLE)
    return outer + bar + hub

@reg("org.cutwire.Drift", BLUE_GREY_DARK)
def drift():
    y = AMBER_LIGHT
    chev = "".join(stroke(f"M{x} 21L{x + 7.5} 30L{x} 39", y, 5.5) for x in (27, 35, 43))
    dots = "".join(circle(x, yy, r, y) for x, yy, r in
                   [(20, 23.5, 2.2), (14.5, 26.5, 1.8), (21, 30, 2.2), (15.5, 33.5, 1.8), (20, 36.5, 2.2)])
    return g(chev + dots, "rotate(-30 32 30) translate(-2.5 0)")

@small("be.alexandervanhee.gradia")
def gradia_s():
    w = 3.4
    corners = (stroke("M13.5 20V13H20.5", INK, w) + stroke("M43.5 13H50.5V20", INK, w) +
               stroke("M13.5 40V47H20.5", INK, w) + stroke("M43.5 47H50.5V40", INK, w))
    card = rrect(20, 19, 24, 22, 4, INK)
    return corners + card + rrect(24, 23.5, 16, 4, 2, HOLE) + rrect(30, 32.5, 10, 5, 2.5, HOLE)

@small("com.github.mtkennerly.ludusavi")
def ludusavi_s():
    w = 4
    left = circle(15.5, 15, 3, INK) + stroke("M15.5 25V46H48.5", INK, w)
    box = rrect(25, 12.5, 23, 23, 3, "none", f' stroke="{INK}" stroke-width="{w}"')
    dots = "".join(circle(x, y, 2.8, INK) for x in (32, 41) for y in (19.5, 28.5))
    return left + box + dots

@small("com.keepsolid.VpnUnlimited")
def vpn_unlimited_s():
    shield = path("M32 12L47.5 17.5V29C47.5 38.5 41 45 32 48.5C23 45 16.5 38.5 16.5 29V17.5Z", INK)
    return shield + ering(26, 29.5, 4.5, 6.5, HOLE, 3.6) + ering(38, 29.5, 4.5, 6.5, HOLE, 3.6)

@small("com.usebruno.Bruno")
def bruno_s():
    ears = ellipse(18.5, 27, 6, 11, ORANGE_DEEP, 18) + ellipse(45.5, 27, 6, 11, ORANGE_DEEP, -18)
    head = circle(32, 30, 14, ORANGE_LIGHT)
    return ears + head + circle(26.5, 27, 2.5, HOLE) + circle(37.5, 27, 2.5, HOLE) + ellipse(32, 35, 4.5, 3.2, HOLE)

@small("hu.irl.cameractrls")
def cameractrls_s():
    outer = cut(cpath(32, 30, 17) + cpath(32, 30, 13), INK)
    return outer + circle(32, 30, 10.5, INK) + poly([pt(32, 30, 5.5, 60 * k - 90) for k in range(6)], RED_DEEP)

@small("io.github.TeamWheelWizard.WheelWizard")
def wheelwizard_s():
    tyre = cut(cpath(32, 30, 17) + cpath(32, 30, 12), INK)
    rim = cut(cpath(32, 30, 10) + cpath(32, 30, 4.5), INK)
    return tyre + rim + circle(32, 30, 2.2, INK)

@small("io.github.giantpinkrobots.flatsweep")
def flatsweep_s():
    hexa = poly([pt(32, 30, 17, -90 + 60 * k) for k in range(6)], INK, 3)
    edges = ""
    for a in (-150, -30, 90):
        x, y = pt(32, 30, 17, a)
        edges += line(32, 30, x, y, HOLE, 3)
    return hexa + edges

@small("io.github.tobagin.karere")
def karere_s():
    bubble = circle(33, 28.5, 15.5, INK) + poly([(20, 35), (16, 47.5), (29, 42)], INK, 2)
    return bubble + stroke(spiral_b(33, 28.5, 1, 9, 1.6, 180), HOLE, 3.2)

@small("io.gitlab.theevilskeleton.Upscaler")
def upscaler_s():
    frame = cut("M19 12H45A5 5 0 0 1 50 17V43A5 5 0 0 1 45 48H19A5 5 0 0 1 14 43V17A5 5 0 0 1 19 12Z"
                "M18.5 16.5V43.5H45.5V16.5Z", INK)
    pink = PINK_SOFT
    left = ellipse(25, 30, 6, 7.5, pink)
    right = f'<rect x="33" y="22" width="7" height="16" fill="{pink}"/>'
    return frame + left + right + line(32, 16, 32, 44, INK, 2.5, "butt")

@small("no.bragefuglseth.Keypunch")
def keypunch_s():
    keys = (rrect(14, 12, 17, 17, 4, INK) + rrect(33, 12, 17, 17, 4, INK) +
            rrect(14, 31, 17, 17, 4, INK) + rrect(33, 31, 17, 17, 4, PURPLE_LIGHT))
    bolt = poly([(44, 33.5), (37.5, 41), (41.5, 41), (40, 46), (46.5, 38.5), (42.5, 38.5)], INK, 1)
    return keys + bolt

@small("org.cutwire.Drift")
def drift_s():
    y = AMBER_LIGHT
    chev = "".join(stroke(f"M{x} 20L{x + 8} 30L{x} 40", y, 6) for x in (22, 32, 42))
    return g(chev + circle(15, 30, 2.6, y), "rotate(-30 32 30) translate(-2 0)")

@small("org.deskflow.deskflow")
def deskflow_s():
    out = ""
    for y in (18.5, 30, 41.5):
        out += stroke(f"M15 {y + 2}C20.5 {y - 4.5} 26 {y - 4.5} 32 {y}S43.5 {y + 4.5} 49 {y - 2}", INK, 4)
    return out

@small("org.dupot.easyflatpak")
def easyflatpak_s():
    out = arc_b(32, 30, 16.5, 60, 300, INK, 4)
    top = poly([(32, 19.5), (42, 25), (32, 30.5), (22, 25)], INK, 1)
    left = poly([(22, 27.5), (30.8, 32.3), (30.8, 42.5), (22, 37.5)], INK, 1)
    right = poly([(33.2, 32.3), (42, 27.5), (42, 37.5), (33.2, 42.5)], INK, 1)
    return out + top + left + right

@small("app.twintaillauncher.ttl")
def ttl_s():
    ring_ = arc_b(34, 31, 13, -50, 150, INK, 4.5)
    slash = path("M50 11L21 48L28 48L48.5 18Z", INK)
    hair = path("M32 16C23 14 16 19 15.5 27C15 33 12 38 9.5 40.5C17 41 22 36 22.5 30"
                "C24 34 22.5 38 20 41C26 39 28 32 26.5 25C28 21 30 18 32 16Z", INK)
    return ring_ + slash + hair
