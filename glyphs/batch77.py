# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 77: Flathub apps missing from Papirus (Sober to Trayscale)."""
from lm import (
    AMBER, AMBER_DEEP, AMBER_LIGHT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_LIGHT, circle, CYAN, CYAN_LIGHT, DEEP_ORANGE, DEEP_ORANGE_DARK,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DARK,
    DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY_LIGHT, HOLE, INDIGO, INDIGO_DARK,
    INDIGO_LIGHT, INK, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, line, ORANGE_DEEP, ORANGE_LIGHT, path,
    PINK_DEEP, poly, pt, RED, RED_DEEP, RED_LIGHT, rrect, stroke, TEAL_LIGHT,
)
from glyphs.kit import arc_c, ellipse, ering, gear_n, registry, _ring

ICONS, SMALL, reg, small = registry()


def _roblox(tile_band, rot):
    sq = rrect(16, 14, 32, 32, 4, INK)
    return g(sq + tile_band + rrect(27, 25, 10, 10, 1.5, HOLE), f"rotate({rot} 32 30)")


@reg("org.vinegarhq.Sober", ORANGE_DEEP)
def sober():
    return _roblox(rrect(16, 26.5, 32, 7, 0, ORANGE_LIGHT), 15)


@reg("space.bigrat.mocktail", DEEP_ORANGE)
def mocktail():
    facet = poly([(16, 31), (31, 46), (20, 46), (16, 42)], DEEP_ORANGE_SOFT)
    return _roblox(facet, -15)


@reg("io.github.shiiion.primehack", INDIGO_DARK)
def primehack():
    rim = _ring(32, 30, 15.5, INK, 3)
    blade = line(47.5, 12.5, 16.5, 47.5, INK, 2.6)
    s = "M39 22H27V30H37V38H25"
    ess = g(stroke(s, HOLE, 9) + stroke(s, INK, 4.6), "translate(32 30) skewX(-12) translate(-32 -30)")
    return rim + blade + ess


@reg("com.supermodel3.Supermodel", BLUE_DARK)
def supermodel():
    band = stroke("M16 16Q33 9 48.5 17.5", AMBER_LIGHT, 4)
    three = stroke("M17.5 25C19 22 28 21.5 28 27C28 30.5 24.5 31.5 22 31.5C25.5 31.5 29 33 29 37"
                   "C29 43 19 43.5 17 40", INK, 4.4)
    d = stroke("M34.5 23.5V42.5H38.5A9.5 9.5 0 0 0 38.5 23.5Z", INK, 4.4)
    return band + three + d


@reg("dev.lizardbyte.app.Sunshine", ORANGE_DEEP)
def sunshine():
    return ellipse(32, 30, 17.5, 13, INK, -25) + ellipse(34.5, 27.8, 13, 8.8, HOLE, -25)


@reg("com.modrinth.ModrinthApp", INDIGO_LIGHT)
def modrinth():
    outer = arc_c(32, 30, 15.5, -40, 280, INK, 3.2)
    inner = arc_c(32, 30, 9.5, 100, 400, INK, 3.2)
    wrench = _ring(32, 30, 3, INK, 3) + line(34.2, 32.2, 45, 43, INK, 3.2)
    return outer + inner + wrench


@reg("io.github.Faugus.faugus-launcher", BLUE_DARK)
def faugus():
    head = path("M20 31C20 20 25 13.5 32 13.5C39 13.5 44 20 44 31Z", INK)
    eyes = (poly([(24, 21.5), (30.5, 24), (30, 27.5), (24.5, 26.5)], HOLE, 1.5) +
            poly([(40, 21.5), (33.5, 24), (34, 27.5), (39.5, 26.5)], HOLE, 1.5))
    pad_d = ("M18.5 36C18.5 32.5 21 30.5 24.5 30.5H39.5C43 30.5 45.5 32.5 45.5 36L47.5 43.5"
             "C48 46.5 45 48 42.5 46L38.5 42.5H25.5L21.5 46C19 48 16 46.5 16.5 43.5Z")
    pad = path(pad_d, INK, f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"')
    dpad = line(21, 36.5, 28, 36.5, HOLE, 2.4) + line(24.5, 33, 24.5, 40, HOLE, 2.4)
    btns = circle(38.5, 35, 1.9, HOLE) + circle(42, 38.5, 1.9, HOLE)
    beak = poly([(29.5, 27), (34.5, 27), (32, 30)], AMBER, 1.2)
    return head + eyes + beak + pad + dpad + btns


@reg("org.azahar_emu.Azahar", ORANGE_DEEP)
def azahar():
    petal = path("M32 30C27.5 24 27.5 17 32 11.5C36.5 17 36.5 24 32 30Z", INK)
    out = "".join(g(petal, f"rotate({60 * k} 32 30)") for k in range(6))
    return out + circle(32, 30, 4.5, HOLE) + circle(32, 30, 3, GREY_LIGHT)


@reg("dev.eden_emu.eden", DEEP_PURPLE)
def eden():
    sun = circle(32, 30, 15, INK)
    stripes = "".join(rrect(15, y, 34, h, 0, HOLE) for y, h in [(32.5, 2.2), (37, 2.4), (41.5, 2.8)])
    trunk = stroke("M27 47C26 39 28 29 33.5 20", DEEP_PURPLE_DARK, 3.6)
    fronds = "".join(stroke(d, DEEP_PURPLE_DARK, 3) for d in [
        "M33.5 20C29 15.5 22.5 15.5 18.5 19", "M33.5 20C29 20.5 25.5 23.5 24 28.5",
        "M33.5 20C38.5 15 43.5 15 47 18.5", "M33.5 20C38 20.5 41.5 23.5 42.5 28.5",
        "M33.5 20C33 16 31 13.5 27.5 12.5"])
    return sun + stripes + trunk + fronds


@reg("com.fightcade.Fightcade", INDIGO_DARK)
def fightcade():
    out = ""
    for k in range(8):
        a = 45 * k
        x0, y0 = pt(32, 30, 6.5, a)
        x1, y1 = pt(32, 30, 13, a)
        out += line(x0, y0, x1, y1, INK, 2.4)
        cx, cy = pt(32, 30, 14.5, a)
        rot = 45 if k % 2 == 0 else 0
        out += g(rrect(cx - 3.2, cy - 3.2, 6.4, 6.4, 1.2, INK), f"rotate({rot} {f(cx)} {f(cy)})")
    return out + _ring(32, 30, 5, CYAN_LIGHT, 3.8)


@reg("io.github.streetpea.Chiaki4deck", ORANGE_DEEP)
def chiaki():
    waves = arc_c(32, 30, 17, -145, -35, INK, 3.2) + arc_c(32, 30, 11, -140, -40, INK, 3.2)
    tri = poly([(32, 25), (45.5, 46.5), (18.5, 46.5)], INK, 3)
    face = circle(32, 39, 8, HOLE) + circle(32, 39, 6.2, INK)
    bars = rrect(28.6, 35.5, 2.6, 7, 1.3, HOLE) + rrect(32.8, 35.5, 2.6, 7, 1.3, HOLE)
    return waves + tri + face + bars


@reg("io.github.kolunmi.Bazaar", RED)
def bazaar():
    awn = ""
    for i in range(5):
        x = 16 + i * 6.4
        awn += rrect(x + .5, 13, 5.4, 10, 1.2, INK) + circle(x + 3.2, 23, 2.7, INK)
    posts = line(19, 24, 19, 31, INK, 2.4) + line(45, 24, 45, 31, INK, 2.4)
    stall = rrect(17, 30, 30, 17, 3.5, INK)
    goods = poly([(22.5, 43), (27.5, 34.5), (32.5, 43)], HOLE, 1.5) + circle(38.5, 39, 4.3, HOLE)
    return awn + posts + stall + goods


@reg("io.gitlab.adhami3310.Impression", BLUE_GREY)
def impression():
    disc_ = circle(36, 30, 14, INK) + circle(36, 30, 4.5, HOLE) + circle(36, 30, 2, INK)
    stick = rrect(15, 12.5, 13, 25, 3, DEEP_ORANGE_LIGHT, f' stroke="{HOLE}" stroke-width="2"')
    usb = line(21.5, 18, 21.5, 31, INK, 2.2) + stroke("M18.5 23.5L21.5 26.5L24.5 23.5", INK, 2.2)
    plug = rrect(17.2, 38.5, 8.6, 9, 1.8, INK)
    return disc_ + stick + usb + plug


@reg("io.github.ilya_zlobintsev.LACT", RED_DEEP)
def lact():
    bracket = line(13.5, 15.5, 13.5, 44.5, INK, 2.6)
    card = rrect(16, 18.5, 34, 22, 4, INK)
    fans = ""
    for cx in (25, 41):
        fans += circle(cx, 29.5, 7, HOLE) + circle(cx, 29.5, 2.4, INK)
        for k in range(3):
            x1, y1 = pt(cx, 29.5, 5.6, 120 * k + 20)
            fans += line(cx, 29.5, x1, y1, INK, 2.2)
    fingers = rrect(22, 40, 18, 4.5, 1, INK)
    return bracket + card + fans + fingers


@reg("net.nokyan.Resources", BLUE_DEEP)
def resources():
    dial = path("M17.5 40A16 16 0 1 1 46.5 40Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    ticks = ""
    for a in (-165, -135, -105, -75, -45, -15):
        x0, y0 = pt(32, 34, 10.5, a)
        x1, y1 = pt(32, 34, 13, a)
        ticks += line(x0, y0, x1, y1, HOLE, 2.2)
    x, y = pt(32, 34, 11, -45)
    needle = line(32, 34, x, y, HOLE, 3) + circle(32, 34, 3, HOLE)
    base = rrect(16, 42.5, 32, 5, 2.5, INK)
    return dial + ticks + needle + base


@reg("io.github.linx_systems.ClamUI", BLUE_DARK)
def clamui():
    shield = path("M17 14H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    ball = circle(32, 27.5, 10.5, BLUE_LIGHT)
    seams = (stroke("M24.5 20C29 24 29 31 24.5 35.5", BLUE_DARK, 2.2) +
             stroke("M39.5 20C35 24 35 31 39.5 35.5", BLUE_DARK, 2.2) +
             line(21.5, 27.5, 42.5, 27.5, BLUE_DARK, 2.2))
    return shield + ball + seams


@reg("io.github.giantpinkrobots.bootqt", BLUE)
def bootqt():
    head = rrect(21, 12, 22, 17, 2, INK)
    holes = rrect(25, 16, 4.5, 4.5, .8, HOLE) + rrect(34.5, 16, 4.5, 4.5, .8, HOLE)
    body = rrect(17, 28, 30, 20, 3.5, BLUE_DARK)
    return head + holes + body


@reg("com.ranfdev.DistroShelf", BLUE_GREY_DEEP)
def distroshelf():
    frame = (line(15, 12.5, 15, 47.5, INK, 3) + line(49, 12.5, 49, 47.5, INK, 3) +
             line(15, 30.5, 49, 30.5, INK, 3) + line(15, 47.5, 49, 47.5, INK, 3))
    boxes = (rrect(19.5, 17, 11, 11, 1.5, ORANGE_LIGHT) + rrect(33.5, 17, 11, 11, 1.5, RED_LIGHT) +
             rrect(19.5, 34, 11, 11, 1.5, BLUE_LIGHT) + rrect(33.5, 34, 11, 11, 1.5, CYAN))
    return frame + boxes


@reg("com.freerdp.FreeRDP", LIGHT_BLUE_DARK)
def freerdp():
    big = path("M31 47.5C30.5 40.5 32.5 35.5 36 33.5C36 27 37.5 19.5 41.5 12.5"
               "C43.5 19 44.5 26 44 32.5C47.5 34.5 49.5 40 49 47.5Z", INK)
    eye = circle(40, 40, 3.8, HOLE) + circle(40.6, 40.4, 1.8, INK)
    small_ = path("M16.5 47.5C16 42 17.5 38 20 36.5C19.5 30 20.5 24 22.5 19.5"
                  "C25 23.5 26 29.5 25.5 35.5C27.5 38 28.5 42.5 28 47.5Z", INK)
    return big + eye + small_ + circle(23.5, 33, 1.6, HOLE)


@reg("io.github.wiiznokes.fan-control", BLUE_GREY_DEEP)
def fan_control():
    out = ""
    for k in range(4):
        a0 = -90 + 90 * k
        a1 = a0 + 72
        x0, y0 = pt(32, 30, 17.5, a0)
        x1, y1 = pt(32, 30, 17.5, a1)
        out += path(f"M32 30L{f(x0)} {f(y0)}A17.5 17.5 0 0 1 {f(x1)} {f(y1)}Z", INK,
                    f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return out + circle(32, 30, 3.2, HOLE) + circle(32, 30, 1.6, INK)


@reg("com.geeks3d.furmark", DEEP_ORANGE_DEEP)
def furmark():
    flame = path("M32 12C33 19 39 21 40 27C42 25 42 22 41.5 20C46 24 48.5 30 48 36"
                 "C47.5 43 41 48 32 48C23 48 16.5 43 16 36C15.5 30 18 25 22 21"
                 "C22 25 23 27 25 28C24 22 27 16 32 12Z", INK)
    core = path("M32 27C33 32 38 34 38 39C38 43 35.5 45 32 45C28.5 45 26 43 26 39"
                "C26 35 30 32 32 27Z", AMBER)
    return flame + core


@reg("dev.deedles.Trayscale", BLUE_GREY_DARK)
def trayscale():
    on = [(21, 30), (32, 30), (43, 30), (32, 41)]
    off = [(21, 19), (32, 19), (43, 19), (21, 41), (43, 41)]
    return ("".join(circle(x, y, 4.4, BLUE_GREY) for x, y in off) +
            "".join(circle(x, y, 4.4, INK) for x, y in on))


@reg("com.opera.opera-gx", PINK_DEEP)
def opera_gx():
    return _ring(32, 30, 16, INK, 2.6) + ering(32, 30, 7.2, 11, INK, 3.4)


@reg("one.ablaze.floorp", INDIGO)
def floorp():
    hexa = poly([pt(32, 30, 16.5, 60 * k) for k in range(6)], INK, 4)
    fl = (rrect(24.5, 19, 6.2, 22, 3.1, HOLE) + rrect(24.5, 19, 16, 6, 3, HOLE) +
          rrect(24.5, 28.2, 12, 5.6, 2.8, HOLE))
    return hexa + fl


@reg("rocks.shy.VacuumTube", RED_DEEP)
def vacuumtube():
    body = rrect(18, 12, 28, 35, 12, INK)
    screen = rrect(22.5, 19, 19, 16, 5, HOLE)
    play = poly([(29, 23), (29, 31), (36, 27)], INK, 1.8)
    feet = line(24, 41.5, 24, 45, HOLE, 2.2) + line(40, 41.5, 40, 45, HOLE, 2.2)
    return body + screen + play + feet


@reg("io.github.aandrew_me.ytdn", BLUE)
def ytdn():
    frame = stroke("M35 44H22A5 5 0 0 1 17 39V21A5 5 0 0 1 22 16H40A5 5 0 0 1 45 21V31", INK, 3.4)
    play = stroke("M27 24.5V35.5L35.5 30Z", INK, 3)
    arrow = line(43, 35, 43, 46, INK, 3.4) + stroke("M38.5 41.5L43 46L47.5 41.5", INK, 3.4)
    return frame + play + arrow


@reg("com.ktechpit.ultimate-media-downloader", BLUE_DEEP)
def umd():
    globe = circle(32, 25.5, 14, INK)
    lines_ = ering(32, 25.5, 6, 14, HOLE, 2.2) + line(18, 25.5, 46, 25.5, HOLE, 2.2)
    pts = [(27, 27), (37, 27), (37, 36), (43, 36), (32, 47), (21, 36), (27, 36)]
    arrow = poly(pts, HOLE, 6) + poly(pts, INK, 2)
    return globe + lines_ + arrow


@reg("com.warlordsoftwares.youtube-downloader-4ktube", RED_DEEP)
def ktube():
    cloud = (circle(23.5, 34, 8, INK) + circle(34, 27.5, 11.5, INK) + circle(42.5, 35, 7, INK) +
             rrect(15.5, 34, 34, 8, 4, INK))
    arrow = line(32, 24.5, 32, 38, HOLE, 4) + stroke("M26.5 33L32 38.5L37.5 33", HOLE, 4)
    return cloud + arrow


@reg("org.waywallen.waywallen", DEEP_ORANGE_DARK)
def waywallen():
    panels = (rrect(14, 12, 16, 19, 3, INK) + rrect(33, 12, 17, 13, 3, INK) +
              rrect(14, 34, 16, 14, 3, INK) + rrect(33, 28, 17, 20, 3, INK))
    cog = (gear_n(32, 30.5, 8.6, 5, HOLE) + gear_n(32, 30.5, 6.4, 3.4, DEEP_ORANGE_SOFT) +
           circle(32, 30.5, 2.8, HOLE))
    return panels + cog


@reg("com.wps.Office", RED)
def wps():
    return stroke("M15.5 17L23.5 43L32 24L40.5 43L48.5 17", INK, 5.5)


@reg("com.collaboraoffice.Office", DEEP_PURPLE_LIGHT)
def collabora():
    diamond = poly([(36, 13), (50, 30), (36, 47), (22, 30)], DEEP_PURPLE_DARK, 3)
    tri = poly([(20, 18.5), (33.5, 30), (20, 41.5)], INK, 2.5)
    return diamond + tri


@reg("io.github.alainm23.planify", BLUE)
def planify():
    back = g(rrect(22, 13.5, 23, 32, 4, ORANGE_LIGHT), "rotate(12 34 30)")
    front = g(rrect(17, 14, 25, 33, 4, INK), "rotate(-4 30 30)")
    tick = stroke("M22.5 27H33M22.5 34H30", HOLE, 3.4)
    return back + front + tick


@reg("net.mkiol.SpeechNote", BLUE_DEEP)
def speechnote():
    page = rrect(15, 13, 34, 34, 4.5, INK)
    pills = (rrect(20.5, 23.5, 6.5, 13, 3.25, HOLE) + rrect(28.75, 18, 6.5, 24, 3.25, HOLE) +
             rrect(37, 23.5, 6.5, 13, 3.25, HOLE))
    return page + pills


@reg("ai.lmstudio.lm-studio", DEEP_PURPLE)
def lmstudio():
    rows = [(16, 19, 24, 26, 40), (20.7, 24, 30, 32, 45), (25.4, 17, 22, 24, 38),
            (30.1, 22, 28, 30, 43), (34.8, 18, 24, 26, 40), (39.5, 23, 29, 31, 46),
            (44.2, 27, 32, 34, 44)]
    out = ""
    for y, d0, d1, b0, b1 in rows:
        out += line(d0, y, d1, y, DEEP_PURPLE_SOFT, 3.2) + line(b0, y, b1, y, INK, 3.2)
    return out


@reg("com.jeffser.Alpaca", LIGHT_BLUE_DEEP)
def alpaca():
    body = rrect(14, 29.5, 29, 13, 6.5, INK) + circle(15.5, 32, 3.5, INK)
    neck = rrect(33, 17, 9, 22, 4, INK)
    head = rrect(33, 15, 15, 8, 4, INK)
    ear = poly([(34.5, 16), (35.5, 10), (38.5, 16)], INK, 1.5)
    legs = "".join(rrect(x, 39, 5, 9, 2.5, INK) for x in (17, 23.5, 31, 37.5))
    eye = circle(41, 18.8, 1.6, HOLE)
    return body + neck + head + ear + legs + eye


@reg("ai.jan.Jan", AMBER_DEEP)
def jan():
    thumb = g(rrect(12, 31.5, 15, 6.5, 3.25, INK), "rotate(-40 25 35)")
    fingers = "".join(rrect(x, top, 5.4, 34 - top, 2.7, INK, f' stroke="{HOLE}" stroke-width="1.3"')
                      for x, top in [(21.5, 15), (27.3, 12), (33.1, 13), (38.9, 17)])
    palm = rrect(21.5, 27, 22.8, 19.5, 9, INK)
    hand = g(thumb + fingers + palm, "rotate(-12 33 30)")
    waves = (stroke("M45 12.5C48 14 50 17 50 21", INK, 2.4) +
             stroke("M13.5 38.5C13.5 42 15 45 18 47", INK, 2.4))
    return hand + waves


@small("ai.lmstudio.lm-studio")
def lmstudio_s():
    rows = [(17, 18, 23, 27, 42), (25, 24, 29, 33, 46), (33, 17, 22, 26, 40), (41, 22, 27, 31, 45)]
    return "".join(line(d0, y, d1, y, DEEP_PURPLE_SOFT, 4.4) + line(b0, y, b1, y, INK, 4.4)
                   for y, d0, d1, b0, b1 in rows)


@small("com.fightcade.Fightcade")
def fightcade_s():
    out = ""
    for k in range(4):
        a = 90 * k
        x0, y0 = pt(32, 30, 7, a)
        x1, y1 = pt(32, 30, 13, a)
        out += line(x0, y0, x1, y1, INK, 3)
        cx, cy = pt(32, 30, 14, a)
        out += g(rrect(cx - 4, cy - 4, 8, 8, 1.5, INK), f"rotate(45 {f(cx)} {f(cy)})")
    return out + _ring(32, 30, 5.5, CYAN_LIGHT, 4.5)


@small("io.github.shiiion.primehack")
def primehack_s():
    s = "M40 21H26V30H38V39H24"
    return _ring(32, 30, 16, INK, 3.4) + g(stroke(s, INK, 5.5), "translate(32 30) skewX(-12) translate(-32 -30)")


@small("dev.eden_emu.eden")
def eden_s():
    sun = circle(32, 30, 16, INK) + rrect(15, 35, 34, 3, 0, HOLE) + rrect(15, 41, 34, 3.4, 0, HOLE)
    palm = (stroke("M27 47C26 39 28 29 33.5 20", DEEP_PURPLE_DARK, 4.4) +
            stroke("M20 20C24 15.5 30 16 33.5 20C37 16 43 15.5 46 20", DEEP_PURPLE_DARK, 4))
    return sun + palm


@small("org.azahar_emu.Azahar")
def azahar_s():
    petal = path("M32 30C26.5 24 26.5 16 32 10.5C37.5 16 37.5 24 32 30Z", INK)
    return "".join(g(petal, f"rotate({72 * k} 32 30)") for k in range(5)) + circle(32, 30, 4, CYAN_LIGHT)


@small("org.waywallen.waywallen")
def waywallen_s():
    panels = (rrect(13, 11, 17, 20, 3, INK) + rrect(33, 11, 18, 14, 3, INK) +
              rrect(13, 34, 17, 15, 3, INK) + rrect(33, 28, 18, 21, 3, INK))
    return panels + gear_n(32, 30.5, 8, 5, HOLE, 6) + circle(32, 30.5, 3.5, INK)


@small("io.github.streetpea.Chiaki4deck")
def chiaki_s():
    waves = arc_c(32, 30, 17, -145, -35, INK, 3.6)
    tri = poly([(32, 22), (47, 47), (17, 47)], INK, 3)
    return waves + tri + circle(32, 39, 7, HOLE)


@small("ai.jan.Jan")
def jan_s():
    thumb = g(rrect(11, 31, 15, 7, 3.5, INK), "rotate(-35 23 36)")
    fingers = "".join(rrect(x, top, 6.4, 34 - top, 3.2, INK, f' stroke="{HOLE}" stroke-width="1.6"')
                      for x, top in [(19.5, 15), (26, 12.5), (32.5, 15)])
    palm = rrect(19.5, 26, 20, 20, 8, INK)
    return g(thumb + fingers + palm, "rotate(-15 31 32)")


@small("io.github.kolunmi.Bazaar")
def bazaar_s():
    awn = ""
    for i in range(3):
        x = 15 + i * 11.3
        awn += rrect(x + .6, 12, 10, 11, 2, INK) + circle(x + 5.6, 23, 5, INK)
    stall = rrect(17, 31, 30, 16, 3.5, INK)
    return awn + stall + circle(32, 39, 4.5, HOLE)


@small("io.github.ilya_zlobintsev.LACT")
def lact_s():
    card = rrect(13, 18, 38, 24, 4, INK)
    fans = "".join(circle(cx, 30, 8, HOLE) + circle(cx, 30, 3.2, INK) for cx in (23.5, 40.5))
    return card + fans


@small("net.nokyan.Resources")
def resources_s():
    dial = path("M16.5 42A16.5 16.5 0 1 1 47.5 42Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    x, y = pt(32, 35, 12, -45)
    return dial + line(32, 35, x, y, HOLE, 4) + circle(32, 35, 3.8, HOLE)


@small("com.modrinth.ModrinthApp")
def modrinth_s():
    return (arc_c(32, 30, 15, -40, 280, INK, 4) + arc_c(32, 30, 7.5, 100, 400, INK, 4) +
            line(34, 32, 45, 43, INK, 4))


@small("io.github.aandrew_me.ytdn")
def ytdn_s():
    frame = stroke("M34 45H21A5 5 0 0 1 16 40V20A5 5 0 0 1 21 15H41A5 5 0 0 1 46 20V30", INK, 3.4)
    play = poly([(26.5, 23.5), (26.5, 36.5), (36.5, 30)], INK, 2)
    arrow = line(44, 35, 44, 46, INK, 3.6) + stroke("M39.5 41.5L44 46L48.5 41.5", INK, 3.6)
    return frame + play + arrow


@small("io.github.Faugus.faugus-launcher")
def faugus_s():
    head = path("M20 31C20 20 25 13.5 32 13.5C39 13.5 44 20 44 31Z", INK)
    eyes = circle(27.5, 24.5, 3, HOLE) + circle(36.5, 24.5, 3, HOLE)
    pad = rrect(15, 31, 34, 15, 7.5, INK, f' stroke="{HOLE}" stroke-width="2.5"')
    return head + eyes + pad + circle(24, 38.5, 2.8, HOLE) + circle(40, 38.5, 2.8, HOLE)


@reg("com.orcaslicer.OrcaSlicer", BLUE_GREY_DARK)
def orcaslicer():
    body = path("M31 12C24 14 19 21 19 31C19 40.5 25 47.5 32 47.5C39.5 47.5 45 41.5 45 33"
                "C45 28 43 24.5 40 21.5L47 17.5L38 17C36 14 33.5 12.2 31 12Z", INK)
    band = path("M19.6 38L44.6 27.8L45 33.2L21.8 43.2C20.8 41.6 20.1 39.9 19.6 38Z", TEAL_LIGHT)
    eye = circle(34, 19.5, 1.8, HOLE)
    return body + band + eye
