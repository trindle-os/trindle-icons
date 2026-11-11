# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 101: icon to BadgeMagic."""
import math
from lm import (
    AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DEEP, BLUE_LIGHT, BROWN,
    BROWN_DARK, BROWN_DEEP, BROWN_LIGHT, CYAN, CYAN_DARK, CYAN_DEEP, DEEP_ORANGE,
    DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DARK,
    DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, f, GREY, GREY_DARK, GREY_DEEP, HOLE, INDIGO,
    INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP,
    ORANGE_DARK, ORANGE_DEEP, path, PINK, PINK_DARK, PINK_DEEP, PINK_LIGHT, PINK_SOFT, poly, pt,
    PURPLE, PURPLE_DEEP, RED, RED_DARK, RED_DEEP, RED_LIGHT, TEAL, TEAL_DARK, TEAL_DEEP,
    TEAL_LIGHT, TEAL_SOFT,
)
from glyphs.kit import (
    arc_arrow, bubble, crescent, ell, ellring, fit, hs, hx, ink_circle, ink_stroke, mirror, petal, pie, registry, ring_c, ink_rrect, rot, star4, star5)

ICONS, SMALL, reg, _ = registry()


def bz(p0, p1, p2, t):
    return tuple((1 - t) ** 2 * a + 2 * t * (1 - t) * b + t * t * c for a, b, c in zip(p0, p1, p2))


def bzt(p0, p1, p2, t):
    return tuple(2 * (1 - t) * (b - a) + 2 * t * (c - b) for a, b, c in zip(p0, p1, p2))


@reg("nl.emphisia.icon", RED)
def icon():
    out = ink_rrect(7, 7, 22, 22, 6) + ink_circle(46, 18, 11) + poly([(18, 35), (30, 56), (6, 56)], INK, 3) + rot(ink_rrect(38, 38, 18, 18, 4), 45, 47, 47)
    return fit(out, 0.551, 31.2, 32.6)


@reg("nl.jknaapen.fladder", INDIGO)
def fladder():
    out = ink_rrect(14, 6, 8, 52, 3) + ink_rrect(42, 6, 8, 52, 3) + ink_rrect(22, 14, 20, 6, 2) + ink_rrect(22, 44, 20, 6, 2) + poly([(27, 25), (27, 39), (39, 32)], INK, 2)
    return fit(out, 0.65, 32.0, 32.0)


@reg("nl.lostboys.rollemup", DEEP_ORANGE)
def rollemup():
    out = ink_circle(42, 32, 14) + ink_stroke("M6 22H22", 4) + ink_stroke("M6 32H18", 4) + ink_stroke("M6 42H22", 4) + ink_stroke("M36 27Q40 23 46 25", 3, HOLE)
    return fit(out, 0.702, 30.0, 32.0)


@reg("nl.v0yd.Capsule", TEAL)
def capsule():
    out = rot(ink_rrect(6, 20, 52, 24, 12) + ink_rrect(30.5, 20, 3, 24, 0, HOLE), -40, 32, 32)
    return fit(out, 0.761, 32.0, 32.0)


@reg("one.alynx.FlipClock", PURPLE)
def flipclock():
    out = ink_rrect(8, 10, 48, 44, 8) + ink_stroke("M25 20L21 36H41", 4.2, HOLE) + ink_stroke("M35 22V44", 4.2, HOLE) + ink_rrect(8, 31, 48, 2.6, 0, HOLE) + ink_rrect(4, 26, 5, 12, 2.5) + ink_rrect(55, 26, 5, 12, 2.5)
    return fit(out, 0.652, 32.0, 32.0)


@reg("one.flipperzero.qFlipper", ORANGE_DEEP)
def qflipper():
    out = ink_rrect(6, 14, 52, 36, 10) + ink_rrect(13, 20, 25, 14, 3, HOLE) + ink_circle(47, 29, 6.5, HOLE) + ink_rrect(13, 39, 12, 4, 2, HOLE) + ink_circle(47, 29, 2.2)
    return fit(out, 0.702, 32.0, 32.0)


@reg("one.jwr.interstellar", DEEP_PURPLE)
def interstellar():
    out = rot(ellring(32, 32, 27, 9, 4.4), -25) + ink_circle(32, 32, 14, INK, hs(3.2)) + star4(52, 10, 6)
    return fit(out, 0.614, 32.8, 25.9)


@reg("one.k8ie.Identities", BLUE)
def identities():
    out = ink_rrect(5, 12, 54, 40, 8) + ink_circle(21, 28, 6, HOLE) + path("M11 44Q11 36 21 36Q31 36 31 44Z", HOLE) + ink_rrect(36, 22, 16, 4.4, 2.2, HOLE) + ink_rrect(36, 31, 12, 4.4, 2.2, HOLE) + ink_rrect(36, 40, 16, 4.4, 2.2, HOLE)
    return fit(out, 0.649, 32.0, 32.0)


@reg("one.mixin.messenger", AMBER_DEEP)
def messenger():
    out = ink_circle(32, 28, 22) + poly([(17, 44), (11, 58), (29, 50)], INK, 2) + ink_stroke("M23 19L41 37M41 19L23 37", 4.4, HOLE)
    return fit(out, 0.582, 32.0, 32.5)


@reg("one.naiara.Kuychi", PINK)
def kuychi():
    out = ink_stroke("M6 46A26 26 0 0 1 58 46", 5) + ink_stroke("M15 46A17 17 0 0 1 49 46", 5) + ink_stroke("M24 46A8 8 0 0 1 40 46", 5)
    return fit(out, 0.626, 32.0, 33.0)


@reg("online.hatsune_miku.tachidesk-vaadinui", BLUE_GREY)
def tachidesk_vaadinui():
    out = path("M5 14Q19 10 30 16V52Q19 46 5 50Z", INK) + path("M59 14Q45 10 34 16V52Q45 46 59 50Z", INK)
    out += ink_stroke("M11 24Q17 22 24 25", 2.8, HOLE) + ink_stroke("M11 33Q17 31 24 34", 2.8, HOLE) + ink_stroke("M40 25Q47 22 53 24", 2.8, HOLE) + ink_stroke("M40 34Q47 31 53 33", 2.8, HOLE)
    return fit(out, 0.611, 32.0, 32.2)


@reg("org._2006Scape.Launcher", RED_DEEP)
def launcher():
    out = rot(ink_rrect(29, 4, 6, 36, 3) + ink_rrect(19, 36, 26, 6, 3) + ink_rrect(29, 42, 6, 12, 3) + ink_circle(32, 57, 4), 35, 32, 32)
    return fit(out, 0.689, 31.5, 32.5)


@reg("org._2009scape.Launcher", INDIGO_DEEP)
def launcher_icon():
    out = ink_stroke("M14 52L44 20", 6) + ink_stroke("M12 28Q28 4 56 18", 6.4) + rot(ink_rrect(40, 15, 8, 8, 2), 45, 44, 19)
    return fit(out, 0.638, 34.0, 32.3)


@reg("org._3fz.mtoc", LIGHT_BLUE_DEEP)
def mtoc():
    out = ""
    for k, (x, w) in enumerate([(4, 34), (18, 24), (18, 28), (4, 30)]):
        y = 10 + k * 13
        out += ink_rrect(x, y, 8, 7, 2) + ink_rrect(x + 12, y, w, 7, 3)
    return fit(out, 0.571, 31.0, 33.0)


@reg("org._99managers.futsal-edition", DEEP_PURPLE_LIGHT)
def futsal_edition():
    out = ink_rrect(6, 12, 52, 40, 6, "none", ' stroke="INK" stroke-width="4"') + ink_rrect(30.2, 12, 3.6, 40, 0) + ring_c(32, 32, 9, 3.6) + ink_rrect(6, 25, 9, 14, 0) + ink_rrect(49, 25, 9, 14, 0)
    return fit(out, 0.61, 32.0, 32.0)


@reg("org.adishatz.Screenshot", PURPLE_DEEP)
def screenshot():
    out = ink_stroke("M6 20V8H18", 4.6) + ink_stroke("M46 8H58V20", 4.6) + ink_stroke("M58 44V56H46", 4.6) + ink_stroke("M18 56H6V44", 4.6) + ink_rrect(22, 22, 20, 20, 4)
    return fit(out, 0.526, 32.0, 32.0)


@reg("org.ajsmith.RegistrySpy", BLUE_GREY_DEEP)
def registryspy():
    out = path("M4 32Q32 6 60 32Q32 58 4 32Z", INK) + ink_circle(32, 32, 11, HOLE) + ink_circle(32, 32, 5.5)
    return fit(out, 0.652, 32.0, 32.0)


@reg("org.altaqwaa.Altaqwaa", TEAL_DEEP)
def altaqwaa():
    out = crescent(28, 32, 22) + star5(47, 22, 9)
    return fit(out, 0.704, 31.1, 32.0)


@reg("org.altlinux.Tailor", PINK_DEEP)
def tailor():
    out = ink_stroke("M22 6L42 40", 5) + ink_stroke("M42 6L22 40", 5) + ring_c(20, 48, 7, 4.4) + ring_c(44, 48, 7, 4.4)
    return fit(out, 0.647, 32.0, 30.3)


@reg("org.altlinux.Tuner", BLUE_DEEP)
def tuner():
    out = ink_stroke("M21 6V30Q21 42 32 42Q43 42 43 30V6", 5.4) + ink_stroke("M32 42V58", 5.4) + ink_stroke("M13 14V22M51 14V22", 3.6)
    return fit(out, 0.634, 32.0, 32.0)


@reg("org.americanmonk.TipitakaPaliReader", DEEP_ORANGE_DEEP)
def tipitakapalireader():
    out = ring_c(32, 32, 21, 4.4) + ink_circle(32, 32, 6.5)
    for a in (0, 45, 90, 135):
        out += rot(ink_stroke("M32 11V26", 3.6) + ink_stroke("M32 38V53", 3.6), a, 32, 32)
    return fit(out, 0.787, 32.0, 32.0)


@reg("org.andypiper.Fedinspect", DEEP_PURPLE_DEEP)
def fedinspect():
    ps = [pt(32, 33, 21, -90 + 72 * k) for k in range(5)]
    out = ink_stroke("M" + "L".join(f"{f(ps[(2 * k) % 5][0])} {f(ps[(2 * k) % 5][1])}" for k in range(5)) + "Z", 3.4)
    for x, y in ps:
        out += ink_circle(x, y, 6)
    return fit(out, 0.691, 32.0, 31.0)


@reg("org.apache.jmeter", CYAN_DEEP)
def jmeter():
    out = ink_stroke("M9 46A24 24 0 1 1 55 46", 5.4) + ink_stroke("M32 42L45 23", 5.4) + ink_circle(32, 42, 6) + ink_stroke("M10 52H54", 4.4)
    return fit(out, 0.638, 32.0, 33.3)


@reg("org.archivekeep.ArchiveKeep", BROWN)
def archivekeep():
    out = ink_rrect(5, 10, 54, 16, 5) + ink_rrect(9, 29, 46, 27, 5) + ink_rrect(24, 37, 16, 5.4, 2.7, HOLE)
    return fit(out, 0.592, 32.0, 33.0)


@reg("org.arrl.trustedqsl", INDIGO_LIGHT)
def trustedqsl():
    out = ink_circle(32, 14, 5) + ink_stroke("M32 22L19 56M32 22L45 56M24.5 42H39.5", 4.4) + ink_stroke("M19 7Q12 14 19 21", 3.6) + ink_stroke("M45 7Q52 14 45 21", 3.6) + ink_stroke("M13 3Q3 14 13 25", 3.4) + ink_stroke("M51 3Q61 14 51 25", 3.4)
    return fit(out, 0.571, 32.0, 30.1)


@reg("org.artisan_scope.artisan", BROWN_DEEP)
def artisan():
    out = rot(ell(32, 32, 17, 24) + ink_stroke("M32 11Q22 32 32 53", 3.6, HOLE), 30, 32, 32)
    return fit(out, 0.808, 32.0, 32.0)


@reg("org.asamk.SignalCli", TEAL_LIGHT)
def signalcli():
    out = bubble(6, 8, 52, 36)
    for k, hh in enumerate([8, 16, 22, 14, 8]):
        out += ink_rrect(16 + k * 8, 26 - hh / 2, 4.4, hh, 2.2, HOLE)
    return fit(out, 0.631, 32.0, 30.9)


@reg("org.asc_hq.ASC", RED_DARK)
def asc():
    out = hx(20, 20, 11, -90, INK, 3) + hx(42, 20, 11, -90, INK, 3) + hx(31, 39, 11, -90, INK, 3) + hx(53, 39, 11, -90, INK, 3)
    return fit(out, 0.627, 36.5, 29.5)


@reg("org.audiveris.audiveris", DEEP_PURPLE_DARK)
def audiveris():
    out = "".join(ink_rrect(5, 14 + k * 8, 54, 2.8, 1.4) for k in range(5))
    out += ink_circle(24, 38, 7.5, INK, hs(2.6)) + ink_rrect(29.5, 8, 4.4, 30, 2, INK, hs(2)) + path("M33 8Q42 10 44 20Q38 15 33 15Z", INK)
    return fit(out, 0.589, 32.0, 27.9)


@reg("org.b3log.siyuan", BLUE_DARK)
def siyuan():
    out = ink_stroke("M22 8Q8 32 22 56", 5) + ink_stroke("M31 14Q21 32 31 50", 4.4) + ink_stroke("M42 8Q56 32 42 56", 5) + ink_stroke("M33 14Q43 32 33 50", 4.4)
    return fit(out, 0.686, 32.0, 32.0)


@reg("org.babelserver.spekter", PINK_LIGHT)
def spekter():
    out = ink_stroke("M5 44H16L22 18L29 44H36L42 8L49 44H59", 4.4) + ink_rrect(5, 51, 54, 4, 2)
    return fit(out, 0.555, 32.0, 30.4)


@reg("org.beagleboard.imagingutility", GREY_DARK)
def imagingutility():
    out = path("M14 6H40L51 17V58H14Z", INK) + ink_rrect(20, 10, 3.4, 9, 1, HOLE) + ink_rrect(27, 10, 3.4, 9, 1, HOLE) + ink_rrect(34, 10, 3.4, 9, 1, HOLE) + ink_rrect(30.5, 24, 5, 12, 0, HOLE) + poly([(23, 35), (43, 35), (33, 47)], HOLE, 2)
    return fit(out, 0.623, 32.5, 32.0)


@reg("org.beeref.BeeRef", GREY)
def beeref():
    out = rot(ink_rrect(6, 12, 30, 24, 3), -10, 21, 24) + rot(ink_rrect(26, 26, 32, 26, 3, INK, hs(3)), 8, 42, 39) + ink_circle(18, 22, 4, HOLE)
    return fit(out, 0.61, 32.7, 32.6)


@reg("org.biblemulti.thelife", DEEP_PURPLE_LIGHT)
def thelife():
    out = ink_rrect(27.5, 5, 9, 54, 3) + ink_rrect(12, 17, 40, 9, 3)
    return fit(out, 0.676, 32.0, 32.0)


@reg("org.bino3d.bino", CYAN_DARK)
def bino():
    out = ink_rrect(7, 12, 34, 34, 7, "none", ' stroke="INK" stroke-width="4.4"') + ink_rrect(24, 22, 34, 32, 7, INK, hs(3.2))
    return fit(out, 0.614, 32.2, 32.7)


@reg("org.bionus.Grabber", RED_LIGHT)
def grabber():
    out = ink_rrect(27.5, 6, 9, 24, 2) + poly([(15, 28), (49, 28), (32, 46)], INK, 3) + ink_stroke("M9 42V54H55V42", 5)
    return fit(out, 0.568, 32.0, 31.3)


@reg("org.bitcoin_safe.BitcoinSafe", ORANGE_DARK)
def bitcoinsafe():
    out = ink_rrect(7, 8, 50, 44, 8) + ink_circle(32, 30, 14, HOLE) + ink_circle(32, 30, 4.4) + ink_stroke("M32 30V20M32 30L40 35M32 30L24 35", 3) + ink_rrect(14, 52, 9, 5, 2) + ink_rrect(41, 52, 9, 5, 2)
    return fit(out, 0.626, 32.0, 32.5)


@reg("org.bitfighter.Bitfighter", INDIGO_DARK)
def bitfighter():
    out = poly([(32, 6), (50, 52), (32, 42), (14, 52)], INK, 4) + ink_stroke("M32 20V32", 3.4, HOLE)
    return fit(out, 0.634, 32.0, 29.0)


@reg("org.blackfennec.app", DEEP_ORANGE_LIGHT)
def app():
    out = poly([(6, 5), (25, 22), (39, 22), (58, 5), (53, 38), (32, 58), (11, 38)], INK, 3)
    out += ink_circle(24, 36, 3.4, HOLE) + ink_circle(40, 36, 3.4, HOLE) + poly([(28, 47), (36, 47), (32, 53)], HOLE, 1.5)
    return fit(out, 0.512, 32.0, 31.5)


@reg("org.blue_nebula.BlueNebula", BLUE_LIGHT)
def bluenebula():
    out = star4(30, 34, 24) + star4(51, 13, 8) + ink_circle(10, 12, 3.6)
    return fit(out, 0.593, 32.5, 31.5)


@reg("org.briarproject.Briar", PINK_DARK)
def briar():
    p0, p1, p2 = (10, 54), (14, 20), (54, 12)
    out = ink_stroke("M10 54Q14 20 54 12", 6)
    for t, s in ((.25, 1), (.45, -1), (.65, 1), (.82, -1)):
        x, y = bz(p0, p1, p2, t)
        tx, ty = bzt(p0, p1, p2, t)
        n = math.hypot(tx, ty)
        tx, ty = tx / n, ty / n
        nx, ny = -ty * s, tx * s
        out += poly([(x - tx * 5, y - ty * 5), (x + tx * 5, y + ty * 5), (x + nx * 13 + tx * 3, y + ny * 13 + ty * 3)], INK, 2.4)
    return fit(out, 0.551, 32.0, 29.5)


@reg("org.caione.GScope", TEAL_DARK)
def gscope():
    out = ink_rrect(5, 8, 54, 42, 8) + ink_stroke("M11 30Q17 14 23 30T35 30T47 30T53 26", 3.4, HOLE) + ink_rrect(22, 52, 20, 5, 2.5)
    return fit(out, 0.597, 32.0, 32.5)


@reg("org.cataclysmbn.CataclysmBN", GREY_DEEP)
def cataclysmbn():
    out = ink_circle(32, 27, 21) + ink_rrect(21, 42, 22, 15, 4) + ink_circle(23.5, 27, 5.5, HOLE) + ink_circle(40.5, 27, 5.5, HOLE) + poly([(29, 37), (35, 37), (32, 32)], HOLE, 1.4) + ink_rrect(27, 48, 2.6, 9, 0, HOLE) + ink_rrect(35, 48, 2.6, 9, 0, HOLE)
    return fit(out, 0.716, 32.0, 31.5)


@reg("org.cataclysmdda.CataclysmDDA", DEEP_ORANGE_DARK)
def cataclysmdda():
    out = ink_rrect(4, 30, 13, 28, 2) + ink_rrect(19, 14, 17, 44, 2) + ink_rrect(38, 22, 13, 36, 2) + ink_rrect(53, 36, 8, 22, 2)
    out += ink_rrect(23, 20, 3.4, 5, 0.8, HOLE) + ink_rrect(29, 20, 3.4, 5, .8, HOLE) + ink_rrect(23, 30, 3.4, 5, .8, HOLE) + ink_rrect(29, 30, 3.4, 5, .8, HOLE) + ink_rrect(42, 28, 3.4, 5, .8, HOLE) + ink_rrect(42, 38, 3.4, 5, .8, HOLE) + ink_circle(50, 10, 6)
    return fit(out, 0.515, 32.5, 31.0)


@reg("org.chessmd.chessmd", TEAL_SOFT)
def chessmd():
    out = ink_circle(32, 16, 9.5) + ink_rrect(25, 25, 14, 6, 3) + poly([(26, 30), (38, 30), (44, 48), (20, 48)], INK, 3) + ink_rrect(14, 48, 36, 9, 3.5)
    return fit(out, 0.667, 32.0, 31.7)


@reg("org.chrisoft.qmidiplayer", PINK_SOFT)
def qmidiplayer():
    out = ink_rrect(5, 10, 54, 44, 6)
    for x in (19, 32, 45):
        out += ink_rrect(x - 5, 10, 10, 26, 2, HOLE) + ink_rrect(x - 1.7, 36, 3.4, 18, 0, HOLE)
    return fit(out, 0.611, 32.0, 32.0)


@reg("org.cloudcompare.CloudCompare", LIGHT_BLUE)
def cloudcompare():
    out = ink_circle(20, 38, 13) + ink_circle(35, 28, 16) + ink_circle(48, 38, 11) + ink_rrect(8, 38, 51, 14, 7)
    out += ink_stroke("M29 46V32M29 46H42M29 46L22 52", 2.8, HOLE)
    return fit(out, 0.668, 33.0, 32.7)


@reg("org.cockpit_project.CockpitClient", BROWN_DARK)
def cockpitclient():
    out = ring_c(32, 32, 22, 5) + ink_circle(32, 32, 6) + ink_stroke("M11 36L26 33M53 36L38 33M32 38V54", 5)
    return fit(out, 0.742, 32.0, 32.0)


@reg("org.contourterminal.Contour", BLUE_DARK)
def contour():
    out = ink_rrect(5, 9, 54, 46, 10) + ink_rrect(5, 9, 54, 11, 6) + ink_stroke("M16 33L25 40L16 47", 4.2, HOLE) + ink_rrect(30, 44, 18, 4.4, 2.2, HOLE)
    return fit(out, 0.597, 32.0, 32.0)


@reg("org.cubocore.CoreAction", PINK)
def coreaction():
    out = ink_circle(32, 32, 24) + poly([(37, 12), (21, 35), (31, 35), (27, 52), (44, 27), (33, 27)], HOLE, 2)
    return fit(out, 0.76, 32.0, 32.0)


@reg("org.cubocore.CoreArchiver", DEEP_PURPLE_DEEP)
def corearchiver():
    out = ink_rrect(10, 6, 44, 52, 8) + ink_rrect(30, 6, 4, 30, 0, HOLE)
    out += ink_rrect(26, 36, 12, 14, 4, HOLE) + ink_rrect(30.7, 41, 2.6, 5, 1.3)
    return fit(out, 0.642, 32.0, 32.0)


@reg("org.cubocore.CoreFM", BLUE_DEEP)
def corefm():
    out = ink_rrect(5, 17, 54, 38, 8) + ink_rrect(5, 9, 26, 16, 5)
    return fit(out, 0.592, 32.0, 32.0)


@reg("org.cubocore.CoreHunt", DEEP_ORANGE_DEEP)
def corehunt():
    out = ring_c(26, 26, 17, 6) + ink_stroke("M39 39L56 56", 7.4) + ink_stroke("M19 22Q22 17 28 17", 3, INK)
    return fit(out, 0.545, 32.9, 32.9)


@reg("org.cubocore.CoreImage", ORANGE_DARK)
def coreimage():
    out = ink_rrect(5, 9, 54, 46, 8) + ink_circle(21, 24, 6, HOLE) + poly([(9, 50), (24, 33), (33, 43), (41, 34), (55, 50)], HOLE, 3)
    return fit(out, 0.614, 32.0, 32.0)


@reg("org.cubocore.CoreInfo", CYAN_DEEP)
def coreinfo():
    out = ink_circle(32, 32, 24) + ink_circle(32, 19, 4, HOLE) + ink_rrect(28.6, 27, 6.8, 20, 3.4, HOLE)
    return fit(out, 0.76, 32.0, 32.0)


@reg("org.cubocore.CorePDF", RED_DARK)
def corepdf():
    out = path("M12 5H38L53 20V59H12Z", INK) + poly([(38, 5), (38, 20), (53, 20)], HOLE, 1.5)
    out += ink_rrect(19, 31, 27, 4, 2, HOLE) + ink_rrect(19, 40, 27, 4, 2, HOLE) + ink_rrect(19, 49, 17, 4, 2, HOLE)
    return fit(out, 0.577, 32.9, 31.6)


@reg("org.cubocore.CorePad", AMBER_DEEP)
def corepad():
    out = ink_rrect(9, 11, 46, 47, 7) + ink_rrect(18, 5, 5, 13, 2.5) + ink_rrect(30, 5, 5, 13, 2.5) + ink_rrect(42, 5, 5, 13, 2.5)
    out += ink_rrect(16, 28, 32, 3.8, 1.9, HOLE) + ink_rrect(16, 37, 32, 3.8, 1.9, HOLE) + ink_rrect(16, 46, 20, 3.8, 1.9, HOLE)
    return fit(out, 0.614, 32.0, 31.5)


@reg("org.cubocore.CorePaint", PURPLE)
def corepaint():
    out = ink_circle(32, 32, 25) + ink_circle(21, 26, 4.6, HOLE) + ink_circle(34, 17, 4.6, HOLE) + ink_circle(46, 27, 4.6, HOLE) + ink_circle(35, 45, 7, HOLE)
    return fit(out, 0.73, 32.0, 32.0)


@reg("org.cubocore.CoreShot", INDIGO)
def coreshot():
    out = ink_rrect(5, 18, 54, 38, 9) + ink_rrect(21, 10, 22, 12, 4) + ink_circle(32, 37, 12, HOLE) + ink_circle(32, 37, 6.5) + ink_circle(51, 27, 2.6, HOLE)
    return fit(out, 0.622, 32.0, 33.0)


@reg("org.cubocore.CoreStats", TEAL_DEEP)
def corestats():
    out = pie(30, 34, 22, 0, 270) + pie(35, 29, 22, 270, 360)
    return fit(out, 0.745, 32.5, 31.5)


@reg("org.cubocore.CoreTime", BLUE_GREY)
def coretime():
    out = ring_c(32, 32, 22, 5) + ink_stroke("M32 17V32L42 39", 5)
    return fit(out, 0.742, 32.0, 32.0)


@reg("org.cutwire.Prism", INDIGO_LIGHT)
def prism():
    out = ink_stroke("M32 10L52 50H12Z", 6) + ink_stroke("M3 38L24 35", 5) + ink_stroke("M40 30L59 21", 5) + ink_stroke("M44 38H60", 5) + ink_stroke("M42 46L59 53", 5)
    return fit(out, 0.527, 31.5, 31.3)


@reg("org.cvfosammmm.Lemma", RED_DEEP)
def lemma():
    out = ink_stroke("M17 6L47 58", 6) + ink_stroke("M33 33L15 58", 6)
    return fit(out, 0.59, 31.0, 32.0)


@reg("org.d3cod3.Mosaic", TEAL)
def mosaic():
    out = ink_rrect(5, 5, 30, 30, 5) + ink_rrect(39, 5, 20, 13, 4) + ink_rrect(39, 22, 20, 13, 4) + ink_rrect(5, 39, 13, 20, 4) + ink_rrect(22, 39, 37, 20, 4)
    return fit(out, 0.543, 32.0, 32.0)


@reg("org.damask_multiphysics.DAMASK_grid", INDIGO_DEEP)
def damask_grid():
    out = ink_rrect(6, 6, 52, 52, 8, "none", ' stroke="INK" stroke-width="4"') + ink_rrect(22, 6, 3.6, 52, 0) + ink_rrect(38.4, 6, 3.6, 52, 0) + ink_rrect(6, 22, 52, 3.6, 0) + ink_rrect(6, 38.4, 52, 3.6, 0)
    return fit(out, 0.558, 32.0, 32.0)


@reg("org.damask_multiphysics.DAMASK_mesh", ORANGE_DEEP)
def damask_mesh():
    out = ink_stroke("M8 52L32 8L56 52Z", 4.6) + ink_stroke("M20 30H44L32 52Z", 3.6)
    return fit(out, 0.568, 32.0, 30.0)


@reg("org.dash.dash-core", BLUE)
def dash_core():
    out = ink_stroke("M17 10V54H31Q51 54 51 32Q51 10 31 10Z", 6) + ink_rrect(6, 29.5, 26, 6, 3)
    return fit(out, 0.693, 30.0, 32.0)


@reg("org.dbgate.DbGate", BROWN)
def dbgate():
    out = path("M10 14V48Q10 58 32 58Q54 58 54 48V14Z", INK) + ell(32, 14, 22, 8) + ink_stroke("M10 28Q32 40 54 28", 3, HOLE) + ink_stroke("M10 41Q32 53 54 41", 3, HOLE)
    return fit(out, 0.676, 32.0, 32.0)


@reg("org.deidentifier.arx", BLUE_GREY_DEEP)
def arx():
    out = ink_circle(32, 19, 11) + path("M10 56Q10 35 32 35Q54 35 54 56Z", INK) + ink_stroke("M12 8L52 58", 4, HOLE)
    return fit(out, 0.582, 32.0, 33.0)


@reg("org.desktop_plus.desktop-plus", INDIGO_SOFT)
def desktop_plus():
    out = ink_rrect(5, 8, 54, 36, 7) + ink_rrect(26, 44, 12, 7, 0) + ink_rrect(16, 50, 32, 6, 3) + ink_rrect(29.2, 17, 5.6, 18, 2, HOLE) + ink_rrect(23, 23.2, 18, 5.6, 2, HOLE)
    return fit(out, 0.595, 32.0, 32.0)


@reg("org.dpsoftware.FireflyLuciferin", DEEP_ORANGE)
def fireflyluciferin():
    out = ink_circle(32, 32, 10)
    for k in range(8):
        a = 45 * k
        x0, y0 = pt(32, 32, 17, a)
        x1, y1 = pt(32, 32, 25 if k % 2 == 0 else 22, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 4.2)
    return fit(out, 0.671, 32.0, 32.0)


@reg("org.duckdns.bugfreeblog.mldonkeynext", DEEP_PURPLE)
def mldonkeynext():
    out = rot(ell(20, 17, 6, 15), -15, 20, 17) + rot(ell(44, 17, 6, 15), 15, 44, 17) + ink_rrect(14, 22, 36, 34, 14)
    out += ink_circle(24, 34, 3.2, HOLE) + ink_circle(40, 34, 3.2, HOLE) + ell(32, 47, 11, 7, HOLE) + ink_circle(28.5, 47, 1.8) + ink_circle(35.5, 47, 1.8)
    return fit(out, 0.634, 32.0, 29.2)


@reg("org.dune3d.dune3d", CYAN)
def dune3d():
    out = poly([(32, 6), (56, 19), (32, 32), (8, 19)], INK, 2) + poly([(8, 25), (29, 37), (29, 59), (8, 47)], INK, 2) + poly([(56, 25), (35, 37), (35, 59), (56, 47)], INK, 2)
    return fit(out, 0.664, 32.0, 32.5)


@reg("org.dupot.beatmatchtopass", DEEP_PURPLE_DARK)
def beatmatchtopass():
    out = ink_circle(32, 32, 25) + ring_c(32, 32, 17, 2.4, HOLE) + ring_c(32, 32, 12, 2.4, HOLE) + ink_circle(32, 32, 6, HOLE) + ink_circle(32, 32, 2)
    return fit(out, 0.73, 32.0, 32.0)


@reg("org.dupot.littleadventure", GREY_DARK)
def littleadventure():
    out = poly([(4, 56), (24, 22), (36, 40), (44, 30), (60, 56)], INK, 3) + ink_stroke("M24 22V7", 3) + poly([(24, 6), (38, 10.5), (24, 15)], INK, 1.6)
    return fit(out, 0.51, 32.0, 31.4)


@reg("org.dupot.savethesheep", GREY_DARK)
def savethesheep():
    out = ink_circle(26, 29, 10) + ink_circle(36, 24, 11) + ink_circle(46, 30, 10) + ink_circle(31, 38, 11) + ink_circle(43, 38, 10)
    out += ink_rrect(26, 44, 5, 14, 2.5) + ink_rrect(44, 44, 5, 14, 2.5) + rot(ell(12, 38, 6, 8.5), 15, 12, 38) + ink_circle(11, 36, 1.8, HOLE)
    return fit(out, 0.71, 30.9, 35.5)


@reg("org.easycoding.TunedSwitcher", RED)
def tunedswitcher():
    out = ink_rrect(5, 17, 54, 30, 15) + ink_circle(44, 32, 10, HOLE) + ink_rrect(14, 29, 14, 6, 3, HOLE)
    return fit(out, 0.676, 32.0, 32.0)


@reg("org.easyrpg.player", INDIGO_DARK)
def player():
    out = path("M32 5L55 13V31Q55 49 32 59Q9 49 9 31V13Z", INK) + star5(32, 32, 12, HOLE)
    return fit(out, 0.664, 32.0, 32.0)


@reg("org.eclipse.sumo", DEEP_ORANGE_LIGHT)
def sumo():
    out = poly([(22, 5), (42, 5), (60, 59), (4, 59)], INK, 3) + ink_rrect(30.3, 10, 3.4, 9, 0, HOLE) + ink_rrect(29.8, 25, 4.4, 12, 0, HOLE) + ink_rrect(29.2, 43, 5.6, 14, 0, HOLE)
    return fit(out, 0.489, 32.0, 32.0)


@reg("org.emptyflow.ArdorQuery", DEEP_PURPLE_LIGHT)
def ardorquery():
    out = ink_stroke("M20 22Q20 8 32 8Q46 8 46 21Q46 30 32 35V40", 6) + ink_circle(32, 53, 4.6)
    return fit(out, 0.694, 33.0, 31.3)


@reg("org.endlessaccess.threadbare", BROWN_LIGHT)
def threadbare():
    out = ink_rrect(10, 6, 44, 9, 3) + ink_rrect(10, 49, 44, 9, 3) + ink_rrect(17, 15, 30, 34, 0) + ink_stroke("M17 23L47 30", 3.2, HOLE) + ink_stroke("M17 33L47 40", 3.2, HOLE) + ink_stroke("M17 43L47 48", 3.2, HOLE)
    return fit(out, 0.603, 32.0, 32.0)


@reg("org.endlessos.Key", AMBER_DEEP)
def key():
    out = ring_c(21, 23, 12, 6.4) + ink_stroke("M30 32L54 56", 6.4) + ink_stroke("M42 44L49 37", 5.4) + ink_stroke("M48 50L54 44", 5.4)
    return fit(out, 0.565, 31.5, 33.5)


@reg("org.enjoyingfoss.FOSStriangulator", BLUE_LIGHT)
def fosstriangulator():
    out = ink_stroke("M32 7L57 53H7Z", 4.4) + ink_stroke("M36 38L32 7M36 38L57 53M36 38L7 53", 3) + ink_circle(36, 38, 5.4)
    return fit(out, 0.548, 32.0, 30.0)


@reg("org.eu.getcatalyst.Catalyst", PINK_DEEP)
def catalyst():
    out = path("M25 8H39V24L55 52Q58 59 50 59H14Q6 59 9 52L25 24Z", INK) + ink_rrect(21, 5, 22, 5, 2.5) + ink_stroke("M17 44Q24 39 32 44T47 44", 3, HOLE) + ink_circle(30, 51, 2.2, HOLE)
    return fit(out, 0.575, 32.0, 32.0)


@reg("org.eu.wabarc.wayback", TEAL_DEEP)
def wayback():
    out = mirror(arc_arrow(32, 32, 22, -60, 235, 5, 7)) + ink_stroke("M32 19V32L40 38", 4.6)
    return fit(out, 0.677, 32.0, 32.3)


@reg("org.exbin.BinEd", INDIGO)
def bined():
    out = ellring(18, 32, 9, 16, 5.2) + ink_stroke("M38 22L47 14V50M37 50H57", 5.2)
    return fit(out, 0.607, 33.0, 32.0)


@reg("org.expresslrs.ExpressLRSConfigurator", RED_LIGHT)
def expresslrsconfigurator():
    out = ink_stroke("M17 17L47 47M47 17L17 47", 5) + ink_rrect(24, 24, 16, 16, 5) + ring_c(13, 13, 8, 3.8) + ring_c(51, 13, 8, 3.8) + ring_c(13, 51, 8, 3.8) + ring_c(51, 51, 8, 3.8)
    return fit(out, 0.538, 32.0, 32.0)


@reg("org.eyecreate.qiflora", ORANGE_DEEP)
def qiflora():
    out = petal(32, 42, 32, 10, -90) + petal(32, 42, 26, 9, -148) + petal(32, 42, 26, 9, -32) + poly([(18, 42), (46, 42), (41, 59), (23, 59)], INK, 3)
    return fit(out, 0.721, 32.0, 35.3)


@reg("org.eyecreate.vehiclevoyage", BLUE_DARK)
def vehiclevoyage():
    out = ink_rrect(5, 32, 54, 15, 6) + poly([(17, 33), (24, 17), (42, 17), (50, 33)], INK, 3)
    out += poly([(23, 31), (27, 21), (31, 21), (31, 31)], HOLE, 1) + poly([(35, 31), (35, 21), (40, 21), (45, 31)], HOLE, 1)
    out += ink_circle(18, 48, 7, INK, hs(3)) + ink_circle(46, 48, 7, INK, hs(3)) + ink_circle(18, 48, 2.4, HOLE) + ink_circle(46, 48, 2.4, HOLE)
    return fit(out, 0.676, 32.0, 36.0)


@reg("org.fcast.Receiver", PURPLE_DEEP)
def receiver():
    out = ink_rrect(5, 8, 54, 38, 8) + ink_rrect(26, 46, 12, 6, 0) + ink_rrect(17, 51, 30, 5, 2.5) + poly([(26, 18), (26, 36), (42, 27)], HOLE, 2.4)
    return fit(out, 0.603, 32.0, 32.0)


@reg("org.fcast.Sender", CYAN_DEEP)
def sender():
    out = ink_rrect(5, 8, 23, 44, 6) + ink_rrect(10, 14, 13, 26, 2, HOLE) + ink_rrect(11, 44, 11, 3, 1.5, HOLE) + ink_stroke("M35 30H51", 5) + poly([(48, 19), (48, 41), (60, 30)], INK, 2.4)
    return fit(out, 0.594, 33.1, 30.0)


@reg("org.feichtmeier.Musicpod", PINK_LIGHT)
def musicpod():
    out = ell(18, 47, 9, 6.6) + ell(45, 41, 9, 6.6) + ink_rrect(23, 14, 4.6, 33, 2) + ink_rrect(50, 8, 4.6, 33, 2) + poly([(23, 12), (55, 5), (55, 15), (23, 22)], INK, 1.5)
    return fit(out, 0.589, 32.4, 28.9)


@reg("org.firestormviewer.FirestormViewer", DEEP_ORANGE)
def firestormviewer():
    out = path("M32 4Q37 19 48 29Q57 40 49 51Q42 59 32 59Q20 59 14 50Q8 40 17 29Q21 36 26 36Q22 20 32 4Z", INK)
    out += path("M32 35Q36 43 40 47Q42 53 32 54Q22 54 24 47Q28 44 32 35Z", HOLE)
    return fit(out, 0.664, 32.2, 31.5)


@reg("org.firo.firo-qt", DEEP_PURPLE_DEEP)
def firo_qt():
    out = ink_circle(32, 32, 25) + ink_stroke("M24 47V19H42M24 33H37", 5.4, HOLE)
    return fit(out, 0.73, 32.0, 32.0)


@reg("org.flathub.electron-sample-app", BLUE_GREY_DEEP)
def electron_sample_app():
    out = ink_rrect(5, 9, 54, 46, 8) + ink_rrect(5, 21, 54, 2.8, 0, HOLE) + star4(32, 39, 9, HOLE) + ink_circle(13, 15, 1.8, HOLE)
    return fit(out, 0.614, 32.0, 32.0)


@reg("org.flathub.flatpak-external-data-checker", PURPLE)
def flatpak_external_data_checker():
    out = ink_rrect(6, 8, 52, 48, 7) + ink_rrect(6, 22, 52, 2.8, 0, HOLE) + ink_stroke("M19 36H45M19 46H34", 5, HOLE)
    return fit(out, 0.61, 32.0, 32.0)


@reg("org.flatpak.Builder", ORANGE_DEEP)
def builder():
    out = rot(ink_rrect(28, 22, 7, 38, 3) + ink_rrect(12, 7, 40, 17, 5) + ink_rrect(12, 12, 8, 7, 1, HOLE), -35, 32, 32)
    return fit(out, 0.584, 26.3, 29.0)


@reg("org.flowkeeper.Flowkeeper", RED)
def flowkeeper():
    out = ink_circle(32, 37, 21) + poly([(32, 17), (21, 9), (29, 11), (32, 3), (35, 11), (43, 9)], INK, 2) + ink_stroke("M17 38Q17 30 24 26", 3.2, HOLE)
    return fit(out, 0.652, 32.0, 30.0)


@reg("org.flozz.calcleaner", BLUE_DEEP)
def calcleaner():
    out = rot(ink_rrect(29, 3, 6, 32, 3) + poly([(20, 33), (44, 33), (52, 59), (12, 59)], INK, 3) + ink_stroke("M24 41V55", 2.6, HOLE) + ink_stroke("M32 41V55", 2.6, HOLE) + ink_stroke("M40 41V55", 2.6, HOLE), 22, 32, 32)
    return fit(out, 0.548, 23.3, 35.4)


@reg("org.fossasia.BadgeMagic", PURPLE)
def badgemagic():
    out = ink_rrect(11, 5, 42, 54, 7) + ink_rrect(26, 10, 12, 4.4, 2.2, HOLE) + star4(32, 37, 12, HOLE)
    return fit(out, 0.63, 32.0, 32.0)
