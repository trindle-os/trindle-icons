# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 93: Kontainer to Scriptorium."""
import math
from lm import (
    AMBER_DEEP, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_LIGHT, BROWN,
    BROWN_LIGHT, BROWN_SOFT, CYAN, CYAN_DARK, CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, GREY, GREY_DARK,
    GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK,
    LIGHT_BLUE, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, line, ORANGE_DARK, ORANGE_DEEP, path, PINK,
    PINK_LIGHT, PINK_SOFT, poly, pt, PURPLE, PURPLE_DEEP, PURPLE_LIGHT, RED_DARK, RED_DEEP,
    RED_LIGHT, RED_SOFT, TEAL, TEAL_DEEP, TEAL_LIGHT,
)
from glyphs.kit import (
    arrowhead, dim, ell, fit, ink_circle, ink_rrect, ink_stroke, petal, registry, ring_c, rot, star4)

ICONS, SMALL, reg, _ = registry()


@reg("io.github.DenysMb.Kontainer", RED_SOFT)
def kontainer():
    out = ink_rrect(6, 14, 52, 34, 4, INK) + ink_rrect(10, 50, 12, 5, 2, INK) + ink_rrect(42, 50, 12, 5, 2, INK)
    for x in (14, 24, 34, 44):
        out += ink_rrect(x, 20, 5, 22, 2.5, HOLE)
    return fit(out, 0.63, 32.0, 34.5)


@reg("io.github.DraqueT.PolyGlot", DEEP_ORANGE)
def polyglot():
    a = path("M8 8H38Q42 8 42 12V30Q42 34 38 34H24L14 44V34H12Q8 34 8 30V12Q8 8 12 8Z", INK)
    a += ink_stroke("M16 28L25 12L34 28M19.5 22H30.5", 3.6, HOLE)
    b = path("M32 26H52Q56 26 56 30V44Q56 48 52 48H50V56L42 48H32Q28 48 28 44V30Q28 26 32 26Z", INK, f' stroke="{HOLE}" stroke-width="3.2" stroke-linejoin="round"')
    b += ink_stroke("M36 33H48M36 40H44", 3.2, HOLE)
    return fit(a + b, 0.59, 32.9, 32.9)


@reg("io.github.Dretch.MonomerFlatpakExample", BLUE_GREY_DEEP)
def monomer():
    hexa = poly([pt(28, 32, 20, -90 + 60 * k) for k in range(6)], INK, 3)
    hole = poly([pt(28, 32, 10, -90 + 60 * k) for k in range(6)], HOLE, 2)
    x, y = pt(28, 32, 20, -30)
    return fit(hexa + hole + ink_stroke(f"M{f(x)} {f(y)}L50 8", 5) + ink_circle(52, 8, 6), 0.60, 33.5, 27.8)


@reg("io.github.Duecki1.CalibRaw", TEAL_LIGHT)
def calibraw():
    body = ink_rrect(6, 16, 52, 36, 7, INK) + ink_rrect(18, 9, 14, 9, 3, INK)
    lens = ink_circle(32, 34, 13, HOLE) + ink_circle(32, 34, 8, INK) + ink_stroke("M32 29V39M27 34H37", 2.6, HOLE)
    return fit(body + lens + ink_circle(50, 24, 2.6, HOLE), 0.65, 32.0, 30.5)


@reg("io.github.FailurePoint.RandomNumberFive", CYAN_DARK)
def random5():
    out = ink_rrect(8, 8, 48, 48, 12, INK)
    five = ink_stroke("M42 18H26L24 32Q30 28 36 31Q42 34 41 41Q40 48 33 48Q27 48 24 44", 5.4, HOLE)
    return fit(rot(out + five, -10), 0.69, 32.2, 32.0)


@reg("io.github.FedericoCalzoni.EventRecorder", RED_DEEP)
def eventrecorder():
    cal = ink_rrect(8, 12, 48, 44, 8, INK) + ink_rrect(8, 12, 48, 14, 6, INK) + ink_rrect(18, 6, 5, 12, 2.5, INK) + ink_rrect(41, 6, 5, 12, 2.5, INK)
    return fit(cal + ink_circle(32, 40, 10, HOLE) + ink_circle(32, 40, 5.2, INK), 0.64, 32.0, 31.0)


@reg("io.github.Foldex.AdwSteamGtk", PURPLE_LIGHT)
def adwsteam():
    win = ink_rrect(6, 10, 52, 40, 7, INK) + ink_rrect(11, 22, 42, 23, 3, HOLE)
    brush = rot(ink_rrect(40, 4, 10, 22, 4, HOLE, f' stroke="{INK}" stroke-width="3.6"') + ink_rrect(42, 26, 6, 14, 3, INK), 28, 45, 30)
    return fit(win + brush + ink_circle(14, 16, 2.4, HOLE) + ink_circle(21, 16, 2.4, HOLE), 0.60, 34.0, 27.1)


@reg("io.github.ForWard_Technologies_LLC.Pylux", DEEP_PURPLE_LIGHT)
def pylux():
    out = ""
    for x, k in ((14, 36), (32, 22), (50, 40)):
        out += ink_rrect(x - 3, 8, 6, 46, 3, INK) + ink_rrect(x - 9, k - 4, 18, 11, 4, INK) + line(x - 5, k + 1.5, x + 5, k + 1.5, HOLE, 2.6)
    return fit(out, 0.66, 32.0, 31.0)


@reg("io.github.GGalya1.RiscvAdventure", TEAL_DEEP)
def riscv():
    out = ink_rrect(14, 14, 36, 36, 6, INK)
    for p in (22, 32, 42):
        out += line(p, 6, p, 14, INK, 4) + line(p, 50, p, 58, INK, 4) + line(6, p, 14, p, INK, 4) + line(50, p, 58, p, INK, 4)
    return fit(out + ink_stroke("M24 24L33 32L24 40M36 40H42", 4.6, HOLE), 0.65, 32.0, 32.0)


@reg("io.github.Geocld.PeaSyo4Desk", AMBER_DEEP)
def peasyo():
    body = path("M18 14H46Q58 14 60 30L62 46Q63 54 55 54Q49 54 45 46L43 42H21L19 46Q15 54 9 54Q1 54 2 46L4 30Q6 14 18 14Z", INK)
    pad = ink_stroke("M16 24V34M11 29H21", 3.6, HOLE) + ink_circle(47, 24, 2.8, HOLE) + ink_circle(47, 34, 2.8, HOLE) + ink_circle(41, 29, 2.8, HOLE) + ink_circle(53, 29, 2.8, HOLE)
    return fit(body + pad, 0.59, 32.0, 34.0)


@reg("io.github.Geocld.XStreamingDesktop", BLUE)
def xstreaming():
    mon = ink_rrect(6, 8, 52, 36, 6, INK) + ink_rrect(22, 48, 20, 5, 2.5, INK) + line(32, 44, 32, 48, INK, 4)
    sig = ink_stroke("M24 34Q32 24 40 34", 3.6, HOLE) + ink_stroke("M18 30Q32 14 46 30", 3.6, HOLE) + ink_circle(32, 37, 2.6, HOLE)
    return fit(mon + sig, 0.62, 32.0, 30.5)


@reg("io.github.GoldenGnu.jEveAssets", INDIGO_DARK)
def jeve():
    ship = poly([(32, 4), (38, 22), (58, 44), (58, 52), (40, 46), (36, 56), (28, 56), (24, 46), (6, 52), (6, 44), (26, 22)], INK, 2)
    return fit(ship + ink_stroke("M32 20V40", 4.4, HOLE) + ink_rrect(27, 40, 10, 6, 2, HOLE), 0.57, 32.0, 30.0)


@reg("io.github.Icalingua.Icalingua", PINK_SOFT)
def icalingua():
    b = path("M10 6H54Q60 6 60 12V38Q60 44 54 44H30L16 58V44H10Q4 44 4 38V12Q4 6 10 6Z", INK)
    gl = ring_c(32, 25, 13, 3.4, HOLE) + ink_stroke("M19 25H45", 3, HOLE) + ink_stroke("M32 12Q22 25 32 38M32 12Q42 25 32 38", 3, HOLE)
    return fit(b + gl, 0.55, 32.0, 32.0)


@reg("io.github.KangLin.RabbitRemoteControl", GREY)
def rabbit():
    ears = rot(ell(32, 16, 6, 16), -14, 32, 36) + rot(ell(32, 16, 6, 16), 14, 32, 36)
    head = ell(32, 42, 17, 15) + ink_circle(26, 40, 2.8, HOLE) + ink_circle(38, 40, 2.8, HOLE) + poly([(29, 46), (35, 46), (32, 50)], HOLE, 1.4)
    return fit(ears + head, 0.65, 32.0, 29.0)


@reg("io.github.KangLin.SerialPortAssistant", ORANGE_DEEP)
def serialport():
    plug = poly([(4, 16), (60, 16), (52, 48), (12, 48)], INK, 5)
    out = plug + ink_stroke("M18 26H46M22 38H42", 4.6, HOLE)
    return fit(out + line(14, 52, 14, 58, INK, 4) + line(50, 52, 50, 58, INK, 4), 0.53, 32.0, 36.8)


@reg("io.github.Lluciocc.Shapebound", BROWN_SOFT)
def shapebound():
    out = ""
    for x, y, dx, dy in ((6, 6, 1, 1), (58, 6, -1, 1), (6, 58, 1, -1), (58, 58, -1, -1)):
        out += ink_stroke(f"M{x} {y + 12 * dy}V{y}H{x + 12 * dx}", 4.6)
    return fit(out + ink_circle(25, 27, 10) + ink_rrect(30, 28, 18, 18, 3) + poly([(14, 46), (28, 46), (21, 34)], INK, 2), 0.51, 32.0, 32.0)


@reg("io.github.Loganavter.Improve-ImgSLI", INDIGO_DEEP)
def imgsli():
    pic = ink_rrect(6, 10, 52, 42, 7, "none", f' stroke="{INK}" stroke-width="4.2"') + path("M6 17Q6 10 13 10H32V52H13Q6 52 6 45Z", INK)
    pic += poly([(12, 44), (20, 32), (26, 40)], HOLE, 1.6) + ink_circle(46, 22, 4.2) + poly([(38, 44), (46, 34), (52, 44)], INK, 1.6)
    return fit(pic + ink_rrect(28, 6, 8, 50, 4, HOLE) + ink_rrect(30, 8, 4, 46, 2, INK) + ink_circle(32, 31, 7, INK, f' stroke="{HOLE}" stroke-width="3"'), 0.61, 32.0, 31.0)


@reg("io.github.MakovWait.Godots", LIGHT_BLUE_DEEP)
def godots():
    out = dim(ink_rrect(14, 6, 38, 16, 5), .4) + dim(ink_rrect(10, 16, 46, 16, 5), .65) + ink_rrect(6, 26, 52, 30, 7)
    return fit(out + poly([(26, 33), (26, 50), (41, 41.5)], HOLE, 2), 0.60, 32.0, 31.0)


@reg("io.github.MrPiggy92.ScriptedJourneys", CYAN_DEEP)
def scriptedjourneys():
    out = ink_rrect(10, 6, 44, 46, 7, INK) + ell(32, 56, 24, 4.5) + ink_rrect(6, 6, 6, 46, 3, INK) + ink_rrect(52, 6, 6, 46, 3, INK)
    path_ = ink_stroke("M18 44C18 34 28 38 30 30S40 24 46 16", 3.6, HOLE)
    return fit(out + path_ + ink_circle(18, 44, 3.4, HOLE) + poly([(44, 12), (44, 24), (52, 18)], HOLE, 1.2), 0.55, 32.0, 33.2)


@reg("io.github.N3kosempai.hetairos-ai", RED_SOFT)
def hetairos():
    out = ink_circle(26, 20, 11) + path("M6 56C6 40 14 34 26 34S46 40 46 56Z", INK)
    return fit(out + star4(48, 18, 11), 0.55, 32.6, 31.2)


@reg("io.github.N3kosempai.klia-kompress", DEEP_ORANGE_DEEP)
def kompress():
    box = ink_rrect(23, 12, 18, 34, 5, INK) + line(26, 21, 38, 21, HOLE, 3)
    return fit(box + ink_stroke("M4 29H17", 5) + arrowhead(21, 29, 1, 0, 7) + ink_stroke("M60 29H47", 5) + arrowhead(43, 29, -1, 0, 7) + ink_stroke("M32 56V50", 4.6), 0.60, 32.0, 35.2)


@reg("io.github.N3kosempai.klia-store", BLUE_GREY_LIGHT)
def kliastore():
    bag = path("M10 20H54L50 56H14Z", INK)
    return fit(bag + ink_stroke("M22 28V16Q22 6 32 6Q42 6 42 16V28", 5) + star4(32, 38, 9, HOLE), 0.63, 32.0, 29.8)


@reg("io.github.NickKarpowicz.LightwaveExplorer", TEAL)
def lightwave():
    pts = []
    for i in range(0, 61):
        x = 4 + i
        env = math.exp(-((x - 34) / 14) ** 2)
        pts.append((x, 30 - 24 * env * math.cos((x - 34) * .75)))
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts)
    return fit(ink_stroke(d, 4.6) + ink_stroke("M4 54H60", 3.4) + dim(ink_stroke("M8 30H56", 2.6), .6), 0.49, 34.0, 29.6)


@reg("io.github.NikolausB.WorkoutTimer", CYAN)
def workouttimer():
    out = ring_c(32, 36, 22, 5.4) + ink_rrect(26, 4, 12, 6, 2) + line(32, 10, 32, 14, INK, 4.4) + line(47, 15, 52, 10, INK, 5)
    bell = ink_rrect(15, 33, 5, 11, 2) + ink_rrect(44, 33, 5, 11, 2) + ink_rrect(20, 30, 5, 17, 2) + ink_rrect(39, 30, 5, 17, 2) + line(25, 38.5, 39, 38.5, INK, 4)
    return fit(out + bell, 0.61, 32.0, 32.4)


@reg("io.github.OkuBrowser.oku", RED_DEEP)
def oku():
    win = ink_rrect(6, 14, 52, 42, 8, INK) + path("M6 22Q6 12 16 12H26Q30 12 32 15H16Q12 15 12 22Z", INK)
    return fit(win + ring_c(32, 36, 10, 5.4, HOLE) + line(6, 26, 58, 26, HOLE, 2.6), 0.65, 32.0, 34.0)


@reg("io.github.Omniaevo.mqtt5-explorer", PURPLE)
def mqtt():
    out = ink_rrect(4, 22, 16, 16, 4, INK) + ink_stroke("M20 30H28M28 12V48M28 12H36M28 30H36M28 48H36", 4.4)
    return fit(out + ink_rrect(36, 6, 22, 12, 4) + ink_rrect(36, 24, 22, 12, 4) + ink_rrect(36, 42, 22, 12, 4), 0.58, 31.0, 30.0)


@reg("io.github.Predidit.Kazumi", DEEP_PURPLE)
def kazumi():
    out = ""
    for k in range(5):
        a = -90 + 72 * k
        x, y = pt(32, 30, 14, a)
        out += ell(x, y, 10, 8.5)
    return fit(out + ink_circle(32, 30, 10.5, HOLE) + poly([(28, 24), (28, 36), (38, 30)], INK, 1.6), 0.78, 32.0, 28.8)


@reg("io.github.Q1CHENL.fig", TEAL_DEEP)
def fig():
    body = path("M32 14C44 14 54 26 54 40C54 50 44 58 32 58C20 58 10 50 10 40C10 26 20 14 32 14Z", INK)
    return fit(body + ink_stroke("M32 14C32 8 34 6 40 4", 5) + path("M32 10C26 4 18 6 16 12C22 16 30 15 32 10Z", INK) + ink_stroke("M32 28C26 34 25 42 30 50", 3.4, HOLE), 0.65, 32.0, 29.8)


@reg("io.github.Querz.mcaselector", AMBER_DEEP)
def mcaselector():
    out = ink_rrect(12, 18, 40, 10, 3, INK) + dim(ink_rrect(12, 31, 40, 10, 3, INK), .6) + dim(ink_rrect(12, 44, 40, 10, 3, INK), .35)
    for x, y, dx, dy in ((4, 6, 1, 1), (60, 6, -1, 1), (4, 52, 1, -1), (60, 52, -1, -1)):
        out += ink_stroke(f"M{x} {y + 10 * dy}V{y}H{x + 10 * dx}", 4.4)
    return fit(out, 0.52, 32.0, 29.0)


@reg("io.github.Rangi42.polished-map", BLUE_DEEP)
def polishedmap():
    m = poly([(6, 14), (22, 8), (42, 14), (58, 8), (58, 50), (42, 56), (22, 50), (6, 56)], INK, 3)
    return fit(m + ink_stroke("M22 8V50M42 14V56", 3.2, HOLE) + star4(32, 32, 7.5, HOLE), 0.54, 32.0, 32.0)


@reg("io.github.Rangi42.polished-map-plusplus", INDIGO_SOFT)
def polishedplus():
    pin = path("M32 4C20 4 12 12 12 23C12 38 32 58 32 58C32 58 52 38 52 23C52 12 44 4 32 4Z", INK)
    return fit(pin + ink_stroke("M32 14V32M23 23H41", 5.6, HOLE), 0.68, 32.0, 31.0)


@reg("io.github.Rangi42.tilemap-studio", PINK_LIGHT)
def tilemapstudio():
    out = ink_rrect(6, 6, 52, 52, 7, "none", f' stroke="{INK}" stroke-width="4.6"')
    out += ink_stroke("M32 8V56M8 32H56", 3.6)
    return fit(out + ink_rrect(11, 11, 16, 16, 2) + ink_rrect(37, 37, 16, 16, 2) + dim(ink_rrect(37, 11, 16, 16, 2), .45), 0.55, 32.0, 32.0)


@reg("io.github.Rescator7.Hearts", GREY_DEEP)
def hearts():
    card = ink_rrect(12, 6, 40, 52, 7, INK)
    heart = path("M32 46C16 36 16 22 24 20C28 19 31 22 32 25C33 22 36 19 40 20C48 22 48 36 32 46Z", HOLE)
    return fit(rot(card + heart, -9), 0.65, 32.4, 31.9)


@reg("io.github.RobertBeckebans.RBDOOM-3-BFG", ORANGE_DEEP)
def bfg():
    out = ink_rrect(4, 18, 42, 22, 6, INK) + path("M42 14H58V44H42Z", INK) + poly([(14, 40), (30, 40), (26, 58), (14, 58)], INK, 2)
    return fit(out + ink_rrect(8, 24, 14, 10, 3, HOLE) + ink_stroke("M28 22V36M34 22V36", 3.4, HOLE) + ink_circle(50, 29, 5, HOLE), 0.57, 31.0, 36.5)


@reg("io.github.RobertBeckebans.RBDoom3BFG-GL", BROWN_LIGHT)
def doomskull():
    out = path("M10 6Q14 18 22 20H42Q50 18 54 6Q60 24 52 38Q50 42 48 44V54H16V44Q14 42 12 38Q4 24 10 6Z", INK)
    return fit(out + poly([(16, 32), (28, 34), (22, 40)], HOLE, 1.4) + poly([(48, 32), (36, 34), (42, 40)], HOLE, 1.4) + ink_stroke("M24 54V46M32 54V46M40 54V46", 3.4, HOLE), 0.60, 32.0, 30.9)


@reg("io.github.Samuel_Schlemper_Schlemuel.SignWriter", INDIGO)
def signwriter():
    out = ink_rrect(18, 28, 30, 28, 10, INK)
    for i, (x, top) in enumerate(((18, 14), (26, 8), (34, 8), (42, 14))):
        out += ink_rrect(x, top, 7, 30, 3.5, INK)
    out += rot(ink_rrect(8, 28, 8, 22, 4, INK), -34, 12, 40)
    return fit(out + ink_stroke("M24 46Q32 52 42 46", 3.2, HOLE), 0.71, 26.2, 32.0)


@reg("io.github.Snaggly.PS2_Pnacher", LIGHT_BLUE_LIGHT)
def ps2patcher():
    d = ring_c(30, 30, 22, 5) + ink_circle(30, 30, 7, INK) + ink_circle(30, 30, 3, HOLE)
    p = rot(ink_rrect(34, 34, 26, 20, 4, INK, f' stroke="{HOLE}" stroke-width="3.2"') + ink_stroke("M40 44H54M40 48H54", 2.6, HOLE), -20, 47, 44)
    return fit(d + p, 0.61, 34.4, 32.0)


@reg("io.github.Sunderland93.sway-input-config", PURPLE_LIGHT)
def swayinput():
    m = path("M32 4C20 4 12 10 12 22V40C12 52 20 60 32 60S52 52 52 40V22C52 10 44 4 32 4Z", INK)
    return fit(m + ink_stroke("M12 26H52M32 4V26", 3.2, HOLE) + ink_rrect(29, 12, 6, 10, 3, HOLE) + ink_stroke("M24 42H40", 3.4, HOLE), 0.63, 32.0, 31.1)


@reg("io.github.TTimo.GtkRadiant", RED_SOFT)
def radiant():
    out = ink_stroke("M32 4L56 17V43L32 56L8 43V17Z", 4.8) + ink_stroke("M8 17L32 30L56 17M32 30V56", 4.2)
    return fit(out + ink_circle(32, 30, 4), 0.64, 32.0, 30.0)


@reg("io.github.TanmayPatil105.verse", DEEP_ORANGE_LIGHT)
def verse():
    book = path("M4 12Q18 8 32 14Q46 8 60 12V52Q46 48 32 54Q18 48 4 52Z", INK)
    return fit(book + ink_stroke("M32 14V54", 3, HOLE) + ink_stroke("M18 20V36M12 27H24", 4.6, HOLE) + ink_stroke("M42 24H54M42 32H54M42 40H52", 3, HOLE), 0.57, 32.0, 32.9)


@reg("io.github.TheThirdOne.rars", BLUE_GREY)
def rars():
    out = ink_rrect(6, 24, 52, 12, 4) + ink_rrect(6, 42, 52, 12, 4) + ink_rrect(6, 6, 52, 12, 4)
    return fit(out + ink_stroke("M12 12H22", 3, HOLE) + ink_stroke("M12 30H42", 3, HOLE) + ink_stroke("M12 48H34", 3, HOLE), 0.59, 32.0, 30.0)


@reg("io.github.TheWisker.Cavasik", TEAL_DEEP)
def cavasik():
    out = ""
    ln = (7, 11, 6, 13, 9, 12, 6, 10, 13, 8, 12, 7)
    for k in range(12):
        a = -90 + 30 * k
        x1, y1 = pt(32, 30, 11, a)
        x2, y2 = pt(32, 30, 11 + ln[k], a)
        out += line(x1, y1, x2, y2, INK, 5.6)
    return fit(out, 0.71, 33.6, 30.4)


@reg("io.github._0_don.clippy", CYAN_DARK)
def clippy():
    board = ink_rrect(8, 10, 48, 50, 8, INK)
    clip = ink_rrect(20, 4, 24, 14, 5, INK, f' stroke="{HOLE}" stroke-width="3.4"')
    return fit(board + clip + ink_stroke("M18 30H46M18 40H46M18 50H34", 3.8, HOLE), 0.58, 32.0, 31.1)


@reg("io.github._0xzer0x.qurancompanion", RED_DARK)
def quran():
    a = ink_rrect(12, 12, 40, 40, 3, INK)
    return fit(rot(a, 0) + rot(a, 45) + ink_circle(32, 32, 11, HOLE) + ink_circle(32, 32, 5, INK), 0.67, 30.6, 31.4)


@reg("io.github._66HEX.Frame", PURPLE_DEEP)
def frame():
    strip = ink_rrect(6, 6, 52, 52, 6, INK) + ink_rrect(18, 16, 28, 32, 3, HOLE)
    for y in (12, 24, 36, 48):
        strip += ink_rrect(9.5, y, 5, 6, 1.5, HOLE) + ink_rrect(49.5, y, 5, 6, 1.5, HOLE)
    return fit(strip + poly([(27, 25), (27, 39), (38, 32)], INK, 1.6), 0.58, 32.0, 32.0)


@reg("io.github.accessory.minus_games_gui", DEEP_PURPLE_SOFT)
def minusgames():
    jc = ink_rrect(14, 4, 36, 56, 16, INK)
    return fit(jc + ink_circle(32, 20, 8, HOLE) + ink_circle(32, 20, 3.4, INK) + line(25, 40, 39, 40, HOLE, 5) + ink_circle(32, 51, 3, HOLE), 0.65, 32.0, 32.0)


@reg("io.github.adenlall.salatok-gtk", TEAL)
def salatok():
    dome = path("M12 34C12 20 22 14 32 8C42 14 52 20 52 34Z", INK)
    out = dome + ink_rrect(8, 34, 48, 22, 3, INK) + ink_stroke("M32 8V2", 3.6) + path("M32 44Q40 44 40 52V56H24V52Q24 44 32 44Z", HOLE)
    return fit(out + ink_rrect(2, 26, 7, 30, 3, INK) + ink_rrect(55, 26, 7, 30, 3, INK), 0.50, 32.0, 28.0)


@reg("io.github.aerocyber.sitemarker", BLUE_GREY)
def sitemarker():
    rb = path("M12 4H52V60L32 46L12 60Z", INK)
    return fit(rb + ring_c(32, 24, 10, 3.4, HOLE) + ink_stroke("M22 24H42M32 14Q26 24 32 34M32 14Q38 24 32 34", 2.8, HOLE), 0.58, 32.0, 32.0)


@reg("io.github.aganzha.Stage", BLUE_LIGHT)
def stagegit():
    out = ink_stroke("M18 8V56", 5) + ink_stroke("M18 40C18 28 46 34 46 20", 5)
    return fit(out + ink_circle(18, 12, 7) + ink_circle(18, 52, 7) + ink_circle(46, 16, 7) + ink_circle(18, 12, 3, HOLE) + ink_circle(18, 52, 3, HOLE) + ink_circle(46, 16, 3, HOLE), 0.63, 32.0, 32.0)


@reg("io.github.aginies.watermark", INDIGO_SOFT)
def watermark():
    page = path("M12 4H38L52 18V60H12Z", INK) + poly([(38, 4), (38, 18), (52, 18)], HOLE, 1.2)
    drop = path("M32 26C40 36 44 40 44 46A12 12 0 0 1 20 46C20 40 24 36 32 26Z", HOLE)
    return fit(page + drop, 0.58, 32.4, 31.6)


@reg("io.github.alamahant.Asteria", PINK)
def asteria():
    orb = rot(f'<ellipse cx="32" cy="30" rx="27" ry="9" fill="none" stroke="{INK}" stroke-width="3.8"/>', -24)
    return fit(star4(32, 30, 24) + orb + ink_circle(32, 30, 5, HOLE), 0.68, 32.0, 30.0)


@reg("io.github.alamahant.BinauralPlayer", GREY)
def binaural():
    out = ink_stroke("M10 40V32A22 22 0 0 1 54 32V40", 5.4)
    return fit(out + ink_rrect(6, 36, 14, 22, 6) + ink_rrect(44, 36, 14, 22, 6) + ink_stroke("M32 26V42M26 30V38M38 30V38", 3.6), 0.59, 32.0, 32.6)


@reg("io.github.alamahant.Ermis", ORANGE_DARK)
def ermis():
    wing = ""
    for a, r in ((-80, 40), (-55, 46), (-30, 48), (-8, 44)):
        wing += petal(10, 52, r, 8, a)
    return fit(wing + ink_circle(10, 52, 6), 0.64, 28.8, 35.2)


@reg("io.github.alamahant.IChingDiviner", BROWN)
def iching():
    out = ""
    for i, y in enumerate((8, 18, 28, 38, 48)):
        out += ink_rrect(6, y, 52, 7, 3.5, INK) if i in (0, 3) else ink_rrect(6, y, 21, 7, 3.5, INK) + ink_rrect(37, y, 21, 7, 3.5, INK)
    out += ink_rrect(6, 58, 52, 7, 3.5, INK)
    return fit(out, 0.54, 32.0, 36.5)


@reg("io.github.alamahant.Jasmine", INDIGO)
def jasmine():
    out = ""
    for k in range(6):
        out += petal(32, 30, 25, 9, -90 + 60 * k)
    return fit(out + ink_circle(32, 30, 8, HOLE) + ink_circle(32, 30, 3.6, INK), 0.73, 32.0, 30.0)


@reg("io.github.alamahant.Kerveros", LIGHT_BLUE)
def kerveros():
    def dog(cx, top, s):
        h = path(f"M{cx - 10 * s} {top + 4 * s}L{cx - 8 * s} {top - 8 * s}L{cx - 2 * s} {top}H{cx + 2 * s}L{cx + 8 * s} {top - 8 * s}L{cx + 10 * s} {top + 4 * s}V{top + 14 * s}Q{cx + 10 * s} {top + 24 * s} {cx} {top + 24 * s}Q{cx - 10 * s} {top + 24 * s} {cx - 10 * s} {top + 14 * s}Z", INK)
        return h + ink_circle(cx - 4 * s, top + 10 * s, 1.9 * s, HOLE) + ink_circle(cx + 4 * s, top + 10 * s, 1.9 * s, HOLE) + poly([(cx - 3 * s, top + 17 * s), (cx + 3 * s, top + 17 * s), (cx, top + 21 * s)], HOLE, 1)
    return fit(rot(dog(13, 26, .95), -14, 13, 38) + rot(dog(51, 26, .95), 14, 51, 38) + dog(32, 12, 1.25), 0.58, 32.0, 25.5)


@reg("io.github.alamahant.Pawns", ORANGE_DEEP)
def pawns():
    out = ink_circle(32, 14, 9) + ink_rrect(22, 22, 20, 6, 3) + path("M25 28H39L43 48H21Z", INK) + ink_rrect(14, 48, 36, 8, 4)
    return fit(out, 0.68, 32.0, 30.5)


@reg("io.github.alamahant.Sadhana", RED_LIGHT)
def sadhana():
    out = ink_circle(32, 12, 8) + path("M32 22C42 22 46 34 46 44H18C18 34 22 22 32 22Z", INK)
    legs = path("M6 52C6 44 18 42 32 46C46 42 58 44 58 52C58 58 50 58 32 54C14 58 6 58 6 52Z", INK)
    return fit(out + legs + ink_stroke("M18 38L10 30M46 38L54 30", 4.6), 0.57, 32.0, 30.5)


@reg("io.github.alamahant.Selene", DEEP_ORANGE)
def selene():
    m = path("M40 6A26 26 0 1 0 58 44A21 21 0 0 1 40 6Z", INK)
    return fit(m + star4(48, 18, 8) + ink_circle(55, 31, 2.4), 0.70, 33.5, 31.6)


@reg("io.github.alamahant.TarotCaster", BLUE_GREY_DEEP)
def tarotcaster():
    back = dim(rot(ink_rrect(14, 8, 30, 46, 5), 14, 29, 31), .45)
    card = rot(ink_rrect(18, 6, 30, 46, 5, INK), -8, 33, 29)
    eye = path("M22 29Q33 16 44 29Q33 42 22 29Z", HOLE) + ink_circle(33, 29, 5, INK)
    return fit(back + card + rot(eye, -8, 33, 29) + rot(ink_stroke("M33 10V14M33 44V48", 3, HOLE), -8, 33, 29), 0.71, 30.2, 30.4)


@reg("io.github.alescdb.mailviewer", TEAL_LIGHT)
def mailviewer():
    env = ink_rrect(4, 12, 44, 32, 5, INK) + ink_stroke("M8 18L26 31L44 18", 3.6, HOLE)
    return fit(env + ink_circle(44, 40, 11, HOLE) + ring_c(44, 40, 9, 5) + ink_stroke("M51 47L58 56", 6), 0.56, 32.5, 35.5)


@reg("io.github.alsofelix.crabdrop", CYAN)
def crabdrop():
    body = ell(32, 38, 18, 13)
    out = body + ink_stroke("M18 42L8 52M22 48L14 58M46 42L56 52M42 48L50 58", 4)
    out += ink_stroke("M18 30L10 18", 4.4) + ink_stroke("M46 30L54 18", 4.4)
    claws = path("M4 14Q2 4 12 4Q14 10 10 16Z", INK) + path("M60 14Q62 4 52 4Q50 10 54 16Z", INK)
    return fit(out + claws + ink_circle(26, 34, 3, HOLE) + ink_circle(38, 34, 3, HOLE), 0.54, 32.0, 32.0)


@reg("io.github.alyraffauf.Switchyard", RED_DEEP)
def switchyard():
    out = ink_stroke("M32 58V36C32 28 20 28 14 8", 5) + ink_stroke("M32 36C32 28 44 28 50 8", 5)
    ties = ""
    for y in (50, 42):
        ties += line(24, y, 40, y, INK, 3.6)
    return fit(out + ties + line(22, 16, 27, 18, INK, 3.6) + line(37, 18, 42, 16, INK, 3.6) + ink_circle(14, 8, 4) + ink_circle(50, 8, 4), 0.58, 32.0, 32.2)


@reg("io.github.am2r_community_developers.Atomic", PURPLE_LIGHT)
def atomic():
    out = ""
    for a in (0, 60, 120):
        out += rot(f'<ellipse cx="32" cy="30" rx="26" ry="10" fill="none" stroke="{INK}" stroke-width="4.2"/>', a)
    return fit(out + ink_circle(32, 30, 6.5), 0.65, 32.0, 30.0)


@reg("io.github.amarz45.Comicpress", DEEP_PURPLE_LIGHT)
def comicpress():
    out = ink_rrect(4, 6, 26, 52, 4, INK) + ink_rrect(34, 6, 26, 24, 4, INK) + ink_rrect(34, 34, 26, 24, 4, INK)
    burst = poly([pt(47, 46, 9 if k % 2 == 0 else 5, -90 + 36 * k) for k in range(10)], HOLE, 1)
    return fit(out + burst + ink_stroke("M10 40L18 24L24 34", 3.4, HOLE) + ink_circle(14, 16, 3.4, HOLE), 0.54, 32.0, 32.0)


@reg("io.github.andreibachim.shortcut", TEAL_DEEP)
def shortcut():
    out = ink_stroke("M12 54V38Q12 22 28 22H48", 7) + arrowhead(50, 22, 1, 0, 11)
    return fit(out + ink_rrect(34, 36, 24, 20, 4), 0.59, 35.1, 34.4)


@reg("io.github.anil_e.Codd", CYAN)
def codd():
    t = ink_rrect(6, 8, 36, 40, 5, INK) + ink_rrect(6, 8, 36, 11, 5, INK)
    t += ink_stroke("M6 32H42M24 19V48", 3, HOLE)
    t2 = ink_rrect(34, 32, 24, 24, 5, INK, f' stroke="{HOLE}" stroke-width="3.2"') + ink_stroke("M34 44H58M46 32V56", 3, HOLE)
    return fit(t + t2, 0.59, 32.1, 32.9)


@reg("io.github.ans_ibrahim.Memento", BLUE)
def memento():
    scr = ink_rrect(4, 8, 56, 40, 7, INK) + poly([(26, 17), (26, 33), (40, 25)], HOLE, 2)
    return fit(scr + ink_stroke("M14 41H50", 3.4, HOLE) + ink_stroke("M22 56H42", 5), 0.57, 32.0, 33.2)


@reg("io.github.appoutlet.GameOutlet", INDIGO_SOFT)
def gameoutlet():
    awn = path("M4 20L10 6H54L60 20Q60 26 54 26Q48 26 48 20Q48 26 42 26Q36 26 36 20Q36 26 30 26Q24 26 24 20Q24 26 18 26Q12 26 12 20Q12 26 6 26Q4 26 4 20Z", INK)
    return fit(awn + ink_rrect(8, 30, 48, 28, 3) + ink_rrect(14, 36, 18, 22, 2, HOLE) + ink_rrect(38, 36, 12, 12, 2, HOLE), 0.58, 32.0, 32.0)


@reg("io.github.archisman_panigrahi.QuickBib", PINK_SOFT)
def quickbib():
    q = path("M8 36Q8 12 28 8V16Q18 20 18 28H26V48H8Z", INK) + path("M36 36Q36 12 56 8V16Q46 20 46 28H54V48H36Z", INK)
    return fit(q, 0.64, 32.0, 28.0)


@reg("io.github.archisman_panigrahi.typhoon", GREY_DEEP)
def typhoon():
    out = ""
    for a in (0, 120, 240):
        out += rot(ink_stroke("M32 30C32 16 44 10 56 16", 6), a)
    return fit(out + ink_circle(32, 30, 6, INK, f' stroke="{INK}" stroke-width="0"') + ink_circle(32, 30, 3, HOLE), 0.58, 31.9, 35.8)


@reg("io.github.archisman_panigrahi.wombat", ORANGE_DEEP)
def wombat():
    body = ell(34, 38, 24, 16) + ink_circle(14, 30, 11) + ink_circle(8, 22, 4.4) + ink_circle(20, 21, 4.4)
    legs = ink_rrect(18, 44, 8, 14, 4) + ink_rrect(42, 44, 8, 14, 4)
    return fit(body + legs + ink_circle(11, 29, 2.6, HOLE) + ell(5, 33, 3, 2.4, HOLE), 0.64, 30.0, 37.2)


@reg("io.github.arijanj.Mimic", BROWN_SOFT)
def mimic():
    base = path("M6 30H58V54Q58 58 54 58H10Q6 58 6 54Z", INK)
    lid = path("M6 30Q6 8 32 8Q58 8 58 30Z", INK)
    teeth = poly([(10, 30), (16, 38), (22, 30), (28, 38), (34, 30), (40, 38), (46, 30), (52, 38), (54, 30)], HOLE, 1)
    return fit(base + lid + teeth + ink_rrect(28, 44, 8, 8, 2, HOLE), 0.58, 32.0, 33.0)


@reg("io.github.athanor_dev.athanor-launcher", INDIGO_DEEP)
def athanor():
    fl = path("M24 4H40V22L54 40Q58 50 50 52H14Q6 50 10 40L24 22Z", INK)
    return fit(ink_rrect(20, 2, 24, 6, 3) + fl + ink_stroke("M14 40H50", 3, HOLE) + path("M32 58C24 52 24 46 32 40C40 46 40 52 32 58Z", HOLE), 0.65, 32.0, 30.0)


@reg("io.github.avomar.dev-toolbox", LIGHT_BLUE_DEEP)
def devtoolbox():
    box = ink_rrect(4, 24, 56, 34, 6, INK) + ink_stroke("M20 24V16Q20 10 26 10H38Q44 10 44 16V24", 5)
    return fit(box + line(4, 38, 60, 38, HOLE, 3) + ink_rrect(26, 33, 12, 10, 3, HOLE), 0.57, 32.0, 32.8)


@reg("io.github.b1ngggg.CloudMusicPlayer", GREY_DEEP)
def cloudmusic():
    cl = path("M18 50A14 14 0 0 1 16 22A18 18 0 0 1 50 26A12 12 0 0 1 48 50Z", INK)
    return fit(cl + ell(27, 41, 5, 4, HOLE) + line(32, 41, 32, 22, HOLE, 4) + ink_stroke("M32 22Q40 22 40 30", 4, HOLE), 0.62, 32.0, 30.9)


@reg("io.github.b43NnUNF4vidFYFhpqaLWy2ANawtRbMtUXZY9Pf.jumpdf", RED_LIGHT)
def jumpdf():
    page = path("M10 4H34L48 18V58H10Z", INK) + poly([(34, 4), (34, 18), (48, 18)], HOLE, 1.2)
    return fit(page + ink_stroke("M16 46H34", 3.4, HOLE) + ink_stroke("M17 36Q29 22 41 34", 4.2, HOLE) + arrowhead(43, 36, .7, .7, 7, HOLE), 0.60, 29.4, 30.6)


@reg("io.github.babaissarkar.ssplot", DEEP_ORANGE_DEEP)
def ssplot():
    out = ink_stroke("M8 6V54H58", 4.4)
    for i, h in enumerate((8, 16, 26, 36, 26, 14, 6)):
        out += ink_rrect(13 + i * 6.8, 51 - h, 5, h, 1.5)
    return fit(out, 0.54, 33.0, 30.0)


@reg("io.github.basshift.Recall", BLUE_GREY_LIGHT)
def recall():
    out = ink_stroke("M12 32A20 20 0 1 0 18 18", 5.4) + arrowhead(14, 12, 0, 1, 9)
    return fit(out + ink_stroke("M32 18V32L42 38", 5), 0.62, 29.9, 32.2)


@reg("io.github.bcpierce00.unison", TEAL)
def unison():
    return fit(ink_stroke("M6 20H48", 6) + arrowhead(54, 20, 1, 0, 10) + ink_stroke("M58 44H16", 6) + arrowhead(10, 44, -1, 0, 10), 0.56, 32.0, 32.0)


@reg("io.github.bendik.Zodia", CYAN_DEEP)
def zodia():
    out = ring_c(32, 30, 26, 4.4)
    for k in range(12):
        a = 30 * k + 15
        x1, y1 = pt(32, 30, 17, a)
        x2, y2 = pt(32, 30, 26, a)
        out += line(x1, y1, x2, y2, INK, 3.4)
    return fit(out + ink_stroke("M32 44V26M32 26C32 14 22 14 20 22M32 26C32 14 42 14 44 22", 4.4), 0.65, 32.0, 30.0)


@reg("io.github.berarma.Oversteer", RED_DEEP)
def oversteer():
    out = ring_c(32, 30, 24, 6) + ink_circle(32, 30, 7)
    return fit(out + ink_stroke("M9 30H25M39 30H55M32 37V54", 6), 0.68, 32.0, 30.0)


@reg("io.github.bgrabitmap.LazPaint", PURPLE)
def lazpaint():
    pal = path("M32 6C14 6 4 18 4 32C4 48 18 56 28 54C36 52 30 44 36 42C44 40 60 44 60 30C60 16 48 6 32 6Z", INK)
    return fit(pal + ink_circle(18, 30, 4.6, HOLE) + ink_circle(26, 18, 4.6, HOLE) + ink_circle(40, 16, 4.6, HOLE) + ink_circle(50, 28, 4.6, HOLE) + ink_circle(30, 44, 3.6, HOLE), 0.65, 32.0, 30.2)


@reg("io.github.bkbilly.lnxlink", DEEP_PURPLE)
def lnxlink():
    l1 = ink_rrect(4, 22, 36, 20, 10, "none", f' stroke="{INK}" stroke-width="6"')
    l2 = ink_rrect(24, 22, 36, 20, 10, "none", f' stroke="{INK}" stroke-width="6"')
    return fit(l1 + l2 + line(26, 32, 38, 32, INK, 6), 0.59, 32.0, 32.0)


@reg("io.github.bkueng.qMasterPassword", TEAL_DEEP)
def qmaster():
    out = ring_c(18, 18, 11, 6.4) + ink_stroke("M26 26L56 56M44 44L52 36M50 50L56 44", 6)
    return fit(out, 0.53, 31.4, 31.4)


@reg("io.github.bommbomm34.latindefense", LIGHT_BLUE)
def latindefense():
    t = path("M8 4H20V10H26V4H38V10H44V4H56V24H48L46 58H18L16 24H8Z", INK)
    return fit(t + path("M26 58V46Q26 38 32 38Q38 38 38 46V58Z", HOLE) + ink_rrect(29, 20, 6, 10, 3, HOLE), 0.55, 32.0, 31.0)


@reg("io.github.bothlab.omerewriter", BLUE_DEEP)
def microscope():
    out = rot(ink_rrect(24, 4, 12, 30, 4), -20, 30, 20) + ink_stroke("M46 20C58 30 54 50 36 50", 5.4)
    return fit(out + ink_rrect(8, 52, 48, 6, 3) + ink_rrect(16, 36, 22, 4, 2) + ink_stroke("M22 50V44", 4.6), 0.57, 32.0, 31.0)


@reg("io.github.bothlab.pomidaq", INDIGO_LIGHT)
def pomidaq():
    t = ell(32, 36, 25, 21)
    crown = poly([(32, 18), (36, 12), (42, 16), (38, 22), (46, 24), (34, 26), (32, 32), (28, 26), (16, 24), (26, 22), (22, 16), (28, 12)], HOLE, 1)
    return fit(t + crown + ink_circle(32, 22, 2.6, INK) + ink_stroke("M32 14V6", 4.2), 0.69, 32.0, 30.4)


@reg("io.github.brainstormtrooper.facteur", PINK_LIGHT)
def facteur():
    st = ink_rrect(8, 8, 48, 48, 4, INK)
    for k in range(4):
        st += ink_circle(16 + 10.7 * k, 8, 2.6, HOLE) + ink_circle(16 + 10.7 * k, 56, 2.6, HOLE) + ink_circle(8, 16 + 10.7 * k, 2.6, HOLE) + ink_circle(56, 16 + 10.7 * k, 2.6, HOLE)
    st += ink_rrect(16, 16, 32, 32, 2, HOLE) + poly([(20, 44), (29, 30), (35, 38), (39, 33), (44, 44)], INK, 1.4) + ink_circle(40, 23, 3.2, INK)
    return fit(st, 0.61, 32.0, 32.0)


@reg("io.github.breadmakesyoufull.baseconvert", GREY_DARK)
def baseconvert():
    out = ink_stroke("M16 40V10L8 17", 6.4) + f'<ellipse cx="46" cy="25" rx="9" ry="14" fill="none" stroke="{INK}" stroke-width="6"/>'
    return fit(out + ink_stroke("M16 54H48", 5) + arrowhead(10, 54, -1, 0, 9) + arrowhead(54, 54, 1, 0, 9), 0.54, 32.0, 34.9)


@reg("io.github.breadmakesyoufull.bpm2fps", ORANGE_DEEP)
def metronome():
    body = path("M22 6H42L54 56H10Z", INK)
    return fit(body + ink_stroke("M32 50L42 14", 4.6, HOLE) + ink_circle(39, 24, 5, HOLE) + ink_rrect(8, 54, 48, 6, 3, INK), 0.57, 32.0, 33.0)


@reg("io.github.brunoanc.eternalmodmanager", BROWN_LIGHT)
def modmanager():
    out = ink_rrect(8, 18, 38, 38, 3) + ink_circle(27, 12, 7) + ink_circle(52, 37, 7)
    return fit(out + ink_circle(8, 37, 7, HOLE) + ink_circle(27, 56, 7, HOLE), 0.63, 30.0, 34.0)


@reg("io.github.brunofin.Cohesion", INDIGO)
def cohesion():
    out = ""
    for cx, cy in ((20, 22), (44, 22), (32, 43)):
        hx = [pt(cx, cy, 14, 30 + 60 * k) for k in range(6)]
        out += path("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hx) + "Z", INK, f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"')
    return fit(out, 0.64, 32.0, 32.5)


@reg("io.github.brunoherbelin.Vimix", LIGHT_BLUE_LIGHT)
def vimix():
    a = ink_rrect(4, 6, 36, 28, 5, INK)
    b = ink_rrect(24, 18, 36, 28, 5, INK, f' stroke="{HOLE}" stroke-width="3.4"')
    return fit(a + b + ink_rrect(6, 54, 52, 5, 2.5) + ink_rrect(24, 50, 12, 13, 4, INK, f' stroke="{HOLE}" stroke-width="2.6"'), 0.51, 32.9, 35.2)


@reg("io.github.bujjuisabee.shimelinux", ORANGE_DARK)
def shimeji():
    body = path("M10 14L16 4L26 12H38L48 4L54 14V40Q54 50 44 50H20Q10 50 10 40Z", INK)
    return fit(body + ink_circle(24, 28, 3.4, HOLE) + ink_circle(40, 28, 3.4, HOLE) + ink_stroke("M28 38Q32 42 36 38", 2.8, HOLE) + ink_rrect(4, 54, 56, 6, 3), 0.52, 32.0, 32.0)


@reg("io.github.buonhobo.Katharsis", RED_LIGHT)
def katharsis():
    mask = path("M10 8Q32 16 54 8V32Q54 54 32 60Q10 54 10 32Z", INK)
    return fit(mask + path("M16 24Q22 18 28 26Q22 28 16 24Z", HOLE) + path("M36 26Q42 18 48 24Q42 28 36 26Z", HOLE) + ink_stroke("M20 40Q32 54 44 40", 4, HOLE), 0.59, 32.0, 34.0)


@reg("io.github.bytezz.IPLookup", DEEP_ORANGE_LIGHT)
def iplookup():
    out = ring_c(26, 26, 20, 6)
    pin = path("M26 12C19 12 15 17 15 22C15 30 26 40 26 40C26 40 37 30 37 22C37 17 33 12 26 12Z", INK)
    return fit(out + ink_stroke("M42 42L58 58", 7) + pin + ink_circle(26, 22, 4, HOLE), 0.50, 32.2, 32.2)


@reg("io.github.carterbox.Electricity_Clock", BLUE_GREY)
def elecclock():
    out = ring_c(32, 30, 25, 5.4)
    return fit(out + poly([(36, 8), (20, 34), (30, 34), (26, 52), (44, 24), (34, 24)], INK, 2), 0.66, 32.0, 30.0)


@reg("io.github.cdrummond.melodeon", TEAL_DEEP)
def melodeon():
    out = ink_rrect(2, 8, 12, 46, 5) + ink_rrect(50, 8, 12, 46, 5)
    for k in range(6):
        out += line(18 + 5.6 * k, 12, 18 + 5.6 * k, 50, INK, 3.4)
    return fit(out + ink_rrect(5, 14, 6, 6, 2, HOLE) + ink_rrect(5, 24, 6, 6, 2, HOLE) + ink_rrect(53, 14, 6, 6, 2, HOLE) + ink_rrect(53, 24, 6, 6, 2, HOLE), 0.55, 32.0, 31.0)


@reg("io.github.cgueret.Scriptorium", CYAN)
def scriptorium():
    q = path("M56 4C36 6 20 20 14 40L22 46C40 40 54 24 56 4Z", INK)
    ink = ink_rrect(34, 44, 24, 16, 5) + ink_rrect(38, 38, 16, 8, 2)
    return fit(q + ink_stroke("M14 50L28 30", 3.4, HOLE) + ink_stroke("M10 58L16 46", 4.4) + ink, 0.54, 32.9, 32.1)
