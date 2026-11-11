# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 92: Zed-Preview to dolm."""
from lm import (
    AMBER, AMBER_DEEP, AMBER_LIGHT, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DEEP, BLUE_GREY_LIGHT,
    BLUE_LIGHT, BLUE_SOFT, BROWN, BROWN_DEEP, BROWN_LIGHT, circle, CYAN, CYAN_DEEP, CYAN_LIGHT,
    DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE,
    DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY, GREY_DARK, GREY_DEEP,
    GREY_LIGHT, HOLE, INDIGO, INDIGO_DARK, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK,
    LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, line, ORANGE, ORANGE_DEEP, ORANGE_LIGHT, path, PINK,
    PINK_DEEP, PINK_LIGHT, poly, pt, PURPLE, PURPLE_DARK, PURPLE_DEEP, PURPLE_LIGHT,
    PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, rrect, TEAL, TEAL_DARK, TEAL_DEEP,
    TEAL_LIGHT, YELLOW, YELLOW_DARK, YELLOW_LIGHT,
)
from glyphs.kit import (
    arrowhead, dim, ell, fit, ink_circle, ink_stroke, registry, ring_c, rot, star4, star5)

ICONS, SMALL, reg, _ = registry()


@reg("dev.zed.Zed-Preview", RED)
def zedpreview():
    z = ink_stroke("M14 14H48L16 46H50", 7.4)
    return fit(g(dim(z, .4), "translate(5 5)") + z, 0.58, 34.7, 31.6)


@reg("dev.zelikos.rollit", CYAN_DEEP)
def rollit():
    out = rrect(12, 12, 40, 40, 10, INK)
    for x, y in ((22, 22), (42, 42), (32, 32)):
        out += ink_circle(x, y, 4.2, HOLE)
    return fit(rot(out, -14), 0.76, 32.6, 31.0)


@reg("dk.gqrx.gqrx", DEEP_ORANGE_LIGHT)
def gqrx():
    out = ink_stroke("M32 22L22 54M32 22L42 54M26 40H38M24.5 47H39.5", 4)
    return fit(out + ink_circle(32, 15, 4.6) + ink_stroke("M21 9Q15 15 21 21M43 9Q49 15 43 21", 3.8) + ink_stroke("M13 5Q4 15 13 25M51 5Q60 15 51 25", 3.4), 0.60, 32.0, 26.3)


@reg("dk.pracedru.Symbolical", DEEP_PURPLE)
def symbolical():
    return fit(ink_stroke("M46 12H18L32 30L18 48H48", 7) + ink_stroke("M50 12V20M50 48V40", 4.6), 0.68, 33.1, 29.3)


@reg("ee.ria.qdigidoc4", BROWN_LIGHT)
def qdigidoc4():
    doc = path("M14 8H34L46 20V52H14Z", INK)
    out = doc + poly([(34, 8), (34, 20), (46, 20)], HOLE, 1.2) + line(20, 28, 38, 28, HOLE, 3) + ink_stroke("M20 42Q24 33 28 41T36 41", 3, HOLE)
    seal = ink_circle(46, 46, 11, INK, f' stroke="{HOLE}" stroke-width="3"') + circle(46, 46, 3.8, HOLE)
    return fit(out + seal, 0.60, 33.5, 30.6)


@reg("engineer.atlas.Nyxt", BLUE_GREY_DEEP)
def nyxt():
    out = ink_stroke("M14 52V12L46 52V12", 8.4) + star4(52, 12, 7.5)
    return fit(out, 0.56, 33.1, 30.2)


@reg("es.danirod.Cartero", LIGHT_BLUE)
def cartero():
    out = rrect(8, 16, 48, 34, 5, INK) + ink_stroke("M12 22L32 37L52 22", 4.2, HOLE)
    return fit(rot(out, -6) + rrect(40, 4, 14, 14, 3, HOLE, f' stroke="{INK}" stroke-width="3.4"'), 0.58, 32.9, 26.4)


@reg("es.estoes.wallpaperDownloader", ORANGE_LIGHT)
def wallpaperdl():
    out = rrect(8, 10, 48, 34, 5, "none", f' stroke="{INK}" stroke-width="4.4"') + poly([(14, 38), (25, 22), (34, 34), (40, 28), (50, 38)], INK, 1.6)
    out += ink_circle(42, 20, 3.6)
    return fit(out + ink_stroke("M32 48V60", 4.6) + poly([(24, 56), (40, 56), (32, 64)], INK, 1.6), 0.56, 31.9, 31.3)


@reg("es.gob.afirma", PURPLE_DEEP)
def afirma():
    nib = path("M38 6L56 24L38 44L26 38L20 26Z", INK)
    out = nib + ink_stroke("M26 38L8 56", 4.6, INK) + ink_circle(22, 30, 3, HOLE) + line(38, 14, 28, 26, HOLE, 2.8)
    return fit(out + ink_stroke("M30 56Q38 46 44 56T58 54", 3.6), 0.56, 32.0, 37.3)


@reg("eu.acall.smart-sip-phone-hybrid", ORANGE_DEEP)
def smartsip():
    out = rrect(10, 6, 26, 46, 6, INK) + rrect(15, 12, 16, 29, 2, HOLE) + ink_circle(23, 46.5, 2.2, HOLE)
    return fit(out + ink_stroke("M42 18A11 11 0 0 1 42 38", 4) + ink_stroke("M50 10A22 22 0 0 1 50 46", 4), 0.62, 32.1, 28.2)


@reg("eu.ad5001.LogarithmPlotter", GREY)
def logplotter():
    out = ink_stroke("M12 8V52H58", 3.8) + ink_stroke("M16 50C18 30 24 22 34 18C42 15 50 13 56 13", 5.6)
    return fit(out + ink_stroke("M24 52V47M36 52V47M48 52V47", 3), 0.54, 35.0, 29.3)


@reg("eu.alyshmahell.ServeMedia", BLUE_DEEP)
def servemedia():
    out = rrect(8, 8, 48, 16, 4, INK) + rrect(8, 28, 48, 16, 4, INK) + ink_circle(17, 16, 2.4, HOLE) + ink_circle(17, 36, 2.4, HOLE)
    return fit(out + poly([(37, 12), (37, 20), (46, 16)], HOLE, 1.2) + poly([(37, 32), (37, 40), (46, 36)], HOLE, 1.2) + ink_stroke("M32 46V56M22 56H42", 4), 0.60, 32.0, 28.7)


@reg("eu.binjr.binjr", AMBER_LIGHT)
def binjr():
    area = poly([(8, 40), (18, 24), (28, 34), (40, 14), (56, 30), (56, 52), (8, 52)], INK)
    return fit(dim(area, .4) + ink_stroke("M8 40L18 24L28 34L40 14L56 30", 4.8) + ink_stroke("M8 54H56", 3.6), 0.62, 32.0, 39.3)


@reg("eu.cichy1173.tabela", PINK)
def tabela():
    out = rrect(8, 10, 48, 44, 6, INK) + rrect(8, 10, 48, 12, 6, INK) + line(8, 22, 56, 22, HOLE, 3)
    return fit(out + line(24, 22, 24, 54, HOLE, 3) + line(40, 22, 40, 54, HOLE, 3) + line(8, 38, 56, 38, HOLE, 3), 0.61, 31.8, 31.4)


@reg("eu.codepoems.xl-converter", TEAL_DARK)
def xlconv():
    out = rrect(4, 34, 16, 16, 3.4, INK) + rrect(34, 8, 26, 26, 4.4, INK) + ink_stroke("M22 42H30", 4) + arrowhead(32, 42, 1, 0, 5.5)
    return fit(out + poly([(39, 28), (45, 19), (50, 25), (53, 21), (56, 28)], HOLE, 1.2) + ink_circle(43, 15, 2.6, HOLE), 0.55, 31.7, 28.3)


@reg("eu.fortysixandtwo.chessclock", BROWN_DEEP)
def chessclock():
    out = rrect(6, 14, 24, 34, 6, INK) + rrect(34, 14, 24, 34, 6, INK)
    out += ring_c(18, 28, 7, 3, HOLE) + ink_stroke("M18 28V24M18 28L21.5 30", 2.6, HOLE) + ring_c(46, 28, 7, 3, HOLE) + ink_stroke("M46 28V24M46 28L49 30", 2.6, HOLE)
    return fit(out + rrect(26, 6, 12, 6, 2.6, INK) + line(12, 40, 24, 40, HOLE, 3) + line(40, 40, 52, 40, HOLE, 3), 0.63, 32.0, 30.3)


@reg("eu.grimripper.grimripper", INDIGO)
def grimripper():
    out = ink_circle(32, 30, 23) + ink_circle(32, 30, 8, HOLE) + ink_circle(32, 30, 3.4)
    return fit(out + ink_stroke("M20 17L27 25L21 33L33 43L31 49", 3.6, HOLE), 0.79, 32.0, 29.3)


@reg("eu.ithz.umftpd", YELLOW_LIGHT)
def umftpd():
    out = rrect(20, 6, 24, 20, 3, INK) + rrect(25, 11, 5, 8, 1.2, HOLE) + rrect(34, 11, 5, 8, 1.2, HOLE) + rrect(15, 26, 34, 18, 5, INK)
    return fit(out + ink_stroke("M32 44V58", 4.6), 0.65, 32.0, 31.6)


@reg("eu.jumplink.Learn6502", RED_DEEP)
def learn6502():
    out = rrect(14, 8, 36, 46, 5, INK) + path("M28 8A4 4 0 0 0 36 8Z", HOLE) + line(24, 24, 40, 24, HOLE, 3) + line(24, 32, 40, 32, HOLE, 3) + line(24, 40, 34, 40, HOLE, 3)
    for y in (14, 26, 38, 50):
        out += line(8, y, 14, y, INK, 4) + line(50, y, 56, y, INK, 4)
    return fit(out, 0.57, 32.0, 31.3)


@reg("eu.ngdevelopment.tsukitag", CYAN)
def tsukitag():
    tag = path("M10 8H34L56 30L34 52L10 30Z", INK)
    moon = path("M36 24A11 11 0 1 0 42 40A9 9 0 0 1 36 24Z", HOLE)
    return fit(tag + ink_circle(19, 18, 3.4, HOLE) + moon, 0.69, 29.8, 25.1)


@reg("eu.nimmerfort.blackbody", DEEP_ORANGE)
def blackbody():
    area = path("M8 52C14 52 18 16 26 16C36 16 38 46 56 52Z", INK)
    return fit(area + ink_stroke("M8 56H58", 3.6) + line(26, 28, 26, 44, HOLE, 3.4), 0.62, 33.0, 43.7)


@reg("eu.nokun.MirrorHall", DEEP_PURPLE_DEEP)
def mirrorhall():
    out = ""
    for k, (w, y) in enumerate(((22, 8), (15, 15), (8.5, 22))):
        out += ink_stroke(f"M{f(32 - w)} 54V{f(y + w)}A{f(w)} {f(w)} 0 0 1 {f(32 + w)} {f(y + w)}V54", 4.4 - k * .4)
    return fit(out, 0.60, 32.0, 35.5)


@reg("eu.ototu.Quteqoin", BLUE_SOFT)
def quteqoin():
    out = ring_c(32, 30, 22, 4) + ring_c(30, 28, 10, 5.4) + ink_stroke("M34 34L42 42", 5.6)
    return fit(out, 0.76, 32.0, 29.3)


@reg("eu.planete_kraus.Tarot", BLUE_GREY)
def tarot():
    back = dim(rrect(8, 10, 30, 46, 5, INK), .45)
    front = rot(rrect(24, 6, 30, 46, 5, INK) + star4(39, 26, 9, HOLE) + ink_circle(39, 26, 3, INK) + line(31, 42, 47, 42, HOLE, 3), 8, 39, 29)
    return fit(back + front, 0.57, 32.3, 31.0)


@reg("eu.quelltext.open_chakra_toning", LIGHT_BLUE_DARK)
def chakra():
    petal = path("M32 8Q44 26 32 46Q20 26 32 8Z", INK)
    out = rot(petal, -56, 32, 46) + rot(petal, 56, 32, 46) + rot(petal, -28, 32, 46) + rot(petal, 28, 32, 46) + petal
    return fit(out + ink_stroke("M14 54Q32 62 50 54", 4.4), 0.57, 32.0, 29.7)


@reg("eu.skribisto.skribisto", ORANGE_DEEP)
def skribisto():
    feather = path("M50 6C32 6 16 20 16 38L18 44L26 38C42 36 52 22 50 6Z", INK)
    return fit(feather + ink_stroke("M14 56L40 20", 3.6, HOLE) + ink_stroke("M10 58L22 44", 4.4) + ink_stroke("M30 56H56", 4), 0.54, 31.9, 34.3)


@reg("eu.stethewwolf.gresistor", PURPLE)
def gresistor():
    out = rrect(16, 20, 32, 20, 9, INK)
    for x in (22, 30, 38):
        out += line(x, 20, x, 40, HOLE, 3.8)
    return fit(out + ink_stroke("M4 30H16M48 30H60", 4.6), 0.61, 32.1, 29.3)


@reg("eu.vcmi.VCMI", CYAN)
def vcmi():
    out = path("M10 54V18H18V12H24V18H28V12H36V18H40V12H46V18H54V54Z", INK)
    return fit(out + path("M25 54V38A7 7 0 0 1 39 38V54Z", HOLE) + rrect(14, 26, 5, 8, 2, HOLE) + rrect(45, 26, 5, 8, 2, HOLE), 0.65, 32.0, 35.3)


@reg("fi.csc.Elmer", GREY_DEEP)
def elmer():
    pts = [pt(32, 30, 22, -90 + 60 * k) for k in range(6)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
    out = ink_stroke(d, 4.4)
    out += ink_stroke(f"M{f(pts[0][0])} {f(pts[0][1])}L{f(pts[3][0])} {f(pts[3][1])}M{f(pts[1][0])} {f(pts[1][1])}L{f(pts[5][0])} {f(pts[5][1])}M{f(pts[2][0])} {f(pts[2][1])}L{f(pts[4][0])} {f(pts[4][1])}", 3.4)
    return fit(out + ink_circle(32, 30, 6), 0.75, 32.0, 29.3)


@reg("fi.mooc.tmc.tmc-cli-rust", BLUE)
def tmccli():
    out = rrect(6, 10, 52, 44, 7, INK) + ink_stroke("M16 24L25 31L16 38", 4.4, HOLE) + line(30, 40, 44, 40, HOLE, 4)
    return fit(out + ink_stroke("M36 24H47", 3.8, HOLE), 0.59, 32.0, 31.3)


@reg("fm.helio.Workstation", AMBER)
def workstation():
    out = ""
    for x, y in ((14, 36), (32, 18), (50, 30)):
        out += line(x, 8, x, 54, INK, 3.6) + rrect(x - 7, y - 5.5, 14, 11, 3, INK, f' stroke="{HOLE}" stroke-width="2.6"')
    return fit(out, 0.59, 32.0, 30.3)


@reg("fr.arnaudmichel.launcherstudio", PINK_DEEP)
def launcherstudio():
    body = path("M32 4C44 12 46 28 42 44H22C18 28 20 12 32 4Z", INK)
    out = body + ink_circle(32, 22, 5.4, HOLE) + poly([(22, 34), (10, 46), (22, 44)], INK, 1.6) + poly([(42, 34), (54, 46), (42, 44)], INK, 1.6)
    return fit(out + ink_stroke("M28 50V58M36 50V58", 4), 0.65, 32.0, 31.5)


@reg("fr.dwightstudio.JArmEmu", TEAL_LIGHT)
def jarmemu():
    out = rrect(16, 16, 32, 32, 5, INK) + rrect(25, 25, 14, 14, 2, HOLE)
    for t in (22, 32, 42):
        out += line(t, 6, t, 16, INK, 3.6) + line(t, 48, t, 58, INK, 3.6) + line(6, t, 16, t, INK, 3.6) + line(48, t, 58, t, INK, 3.6)
    return fit(out, 0.62, 32.0, 31.3)


@reg("fr.ethal.tessera", BROWN)
def tessera():
    out = ""
    for dx, dy, o in ((-12, 0, 1), (12, 0, .55), (0, -12, .8), (0, 12, 1)):
        out += dim(rot(rrect(32 + dx - 9, 30 + dy - 9, 18, 18, 3, INK), 45, 32 + dx, 30 + dy), o)
    return fit(out, 0.78, 32.0, 29.3)


@reg("fr.ffhandball.fdme", INDIGO_DARK)
def fdme():
    out = ink_circle(32, 30, 22) + ink_stroke("M15 22Q32 33 49 22", 3.4, HOLE) + ink_stroke("M15 38Q32 27 49 38", 3.4, HOLE) + ink_stroke("M32 12V48", 3.4, HOLE)
    return fit(out, 0.83, 32.0, 29.3)


@reg("fr.free.hxc2001.HxCFloppyEmulator", YELLOW_DARK)
def hxcfloppy():
    out = path("M10 8H46L56 18V54H10Z", INK) + rrect(20, 8, 24, 16, 2, HOLE) + rrect(35, 11, 5, 10, 1.4, INK) + rrect(18, 34, 28, 20, 3, HOLE)
    return fit(out + line(23, 41, 41, 41, INK, 3) + line(23, 47, 36, 47, INK, 3), 0.56, 33.0, 30.3)


@reg("fr.free.qccrypt.Qccrypt", RED)
def qccrypt():
    out = ink_stroke("M20 26V20A12 12 0 0 1 44 20V26", 6) + ink_circle(32, 40, 16)
    return fit(out + ink_circle(32, 38, 4, HOLE) + poly([(32, 38), (29, 49), (35, 49)], HOLE, 1.4), 0.72, 32.0, 29.8)


@reg("fr.inria.corese.CoreseCommand", CYAN_LIGHT)
def coresecmd():
    out = ink_stroke("M32 30L32 10M32 30L12 46M32 30L52 46", 4.4)
    return fit(out + ink_circle(32, 30, 8) + ink_circle(32, 10, 5.6) + ink_circle(12, 46, 5.6) + ink_circle(52, 46, 5.6), 0.63, 32.0, 32.8)


@reg("fr.inria.corese.CoreseGui", DEEP_ORANGE_DEEP)
def coresegui():
    out = rrect(6, 8, 52, 46, 7, "none", f' stroke="{INK}" stroke-width="4.4"') + ink_stroke("M20 40L32 20L44 40Z", 3.4)
    return fit(out + ink_circle(32, 20, 4.6) + ink_circle(20, 40, 4.6) + ink_circle(44, 40, 4.6), 0.54, 32.0, 30.3)


@reg("fr.masson_informatique.WhosWho", DEEP_PURPLE)
def whoswho():
    out = rrect(12, 8, 38, 48, 6, INK) + ink_circle(31, 26, 7, HOLE) + path("M19 46Q19 36 31 36Q43 36 43 46Z", HOLE)
    return fit(out + rrect(46, 14, 8, 8, 2.4, INK) + rrect(46, 26, 8, 8, 2.4, INK) + rrect(46, 38, 8, 8, 2.4, INK), 0.65, 31.0, 31.3)


@reg("fr.quentium.acters", CYAN_LIGHT)
def acters():
    out = path("M10 14Q32 6 54 14V30Q54 50 32 58Q10 50 10 30Z", INK)
    return fit(out + path("M16 25Q22 21 27 27Q22 29 16 25Z", HOLE) + path("M37 27Q42 21 48 25Q42 29 37 27Z", HOLE) + ink_stroke("M20 40Q32 52 44 40", 4, HOLE), 0.67, 32.0, 29.9)


@reg("fr.rubet.rpn", BLUE_GREY_DEEP)
def rpn():
    out = rrect(6, 8, 52, 46, 9, INK)
    return fit(out + ink_stroke("M46 20V34H22", 5, HOLE) + ink_stroke("M30 26L22 34L30 42", 5, HOLE), 0.59, 32.0, 30.3)


@reg("fr.sgued.bodev", LIGHT_BLUE_LIGHT)
def bodev():
    out = ink_stroke("M22 8Q12 8 12 18V24Q12 30 6 31Q12 32 12 38V44Q12 54 22 54", 5) + ink_stroke("M42 8Q52 8 52 18V24Q52 30 58 31Q52 32 52 38V44Q52 54 42 54", 5)
    return fit(out + line(26, 31, 38, 31, INK, 4.6), 0.62, 32.0, 30.3)


@reg("fr.sgued.ten_forward", ORANGE)
def tenforward():
    out = poly([(8, 10), (56, 10), (32, 38)], INK, 2) + line(32, 38, 32, 54, INK, 5) + line(20, 56, 44, 56, INK, 5)
    return fit(out + ink_stroke("M20 18H44", 3.4, HOLE) + ink_circle(42, 20, 4.4, HOLE), 0.58, 32.0, 28.6)


@reg("fun.dragonfly.switchfin", PURPLE_DARK)
def switchfin():
    fin = path("M12 46C14 30 24 16 38 6C38 18 42 30 52 46Z", INK)
    return fit(fin + ink_stroke("M6 54Q13 48 20 54T34 54T48 54T60 54", 4.2) + ink_stroke("M30 24C28 30 27 36 28 42", 3.4, HOLE), 0.55, 33.0, 38.2)


@reg("fyi.soltfrfr.NightmareEditor", BLUE_DEEP)
def nightmare():
    out = path("M4 28Q32 2 60 28Q32 54 4 28Z", INK) + ink_circle(32, 28, 11, HOLE) + ink_circle(32, 28, 5, INK)
    return fit(out + ink_stroke("M16 44L12 54M32 50V58M48 44L52 54", 3.8), 0.63, 32.0, 35.1)


@reg("fyi.zoey.TeX-Match", GREY)
def texmatch():
    return fit(ink_stroke("M8 12H40M24 12V50", 7.4) + ink_stroke("M54 28H40V54H54M40 41H51", 5.6), 0.53, 30.7, 32.1)


@reg("games.zetsubou.AnAdventurersGallantry", BLUE_LIGHT)
def gallantry():
    out = path("M10 10H54V32Q54 48 32 58Q10 48 10 32Z", INK)
    return fit(out + line(32, 16, 32, 46, HOLE, 5) + poly([(32, 12), (28, 18), (36, 18)], HOLE, 1) + line(23, 38, 41, 38, HOLE, 4.4), 0.63, 32.0, 28.3)


@reg("games.zetsubou.HumanityMustPerish", AMBER_DEEP)
def humanity():
    out = path("M10 30C10 14 20 6 32 6C44 6 54 14 54 30C54 36 51 40 46 42V50H18V42C13 40 10 36 10 30Z", INK)
    return fit(out + ell(22, 30, 6.4, 7.4, HOLE) + ell(42, 30, 6.4, 7.4, HOLE) + poly([(32, 36), (28, 44), (36, 44)], HOLE, 1) + line(26, 50, 26, 44, HOLE, 3) + line(38, 50, 38, 44, HOLE, 3), 0.76, 32.0, 29.4)


@reg("games.zetsubou.MaxMassacre", PINK)
def maxmassacre():
    head = path("M26 14Q44 4 58 22Q50 38 40 38Q38 28 26 14Z", INK)
    return fit(line(12, 58, 36, 22, INK, 6) + head + ink_stroke("M36 22L44 30", 4), 0.59, 32.9, 39.0)


@reg("games.zetsubou.SablesGrimoireDemo", TEAL)
def grimoire():
    out = rrect(10, 6, 44, 52, 6, INK) + line(19, 6, 19, 58, HOLE, 3)
    return fit(out + star5(37, 31, 12, HOLE) + ink_circle(37, 31, 4, INK), 0.58, 32.0, 31.3)


@reg("games.zetsubou.WanderNoMore", BROWN_DEEP)
def wandernomore():
    out = line(32, 10, 32, 58, INK, 5.4) + poly([(8, 14), (42, 14), (52, 22), (42, 30), (8, 30)], INK, 2.4) + poly([(56, 36), (22, 36), (12, 44), (22, 52), (56, 52)], INK, 2.4)
    return fit(out + line(15, 22, 33, 22, HOLE, 3.4) + line(30, 44, 48, 44, HOLE, 3.4), 0.57, 32.0, 32.3)


@reg("garden.turtle.Jellybean", PINK_LIGHT)
def jellybean():
    bean = path("M14 42C6 32 14 12 32 12C52 12 58 28 48 42C40 52 24 54 14 42Z", INK)
    return fit(rot(bean, -20) + ink_stroke("M20 22Q28 16 38 18", 3.8, HOLE), 0.85, 32.3, 30.2)


@reg("gay.brie.CheesePaper", ORANGE)
def cheesepaper():
    out = path("M6 44L52 12L58 40L58 54H6Z", INK)
    return fit(out + ink_circle(22, 46, 4.2, HOLE) + ink_circle(44, 40, 3.6, HOLE) + ink_circle(34, 29, 3, HOLE), 0.58, 32.0, 35.6)


@reg("gg.minion.Minion", RED_DARK)
def minion():
    head = ink_stroke("M10 28Q32 2 56 20", 7.4)
    return fit(line(14, 56, 40, 14, INK, 5.6) + head + ink_stroke("M54 18L58 30", 5.4), 0.59, 35.3, 37.1)


@reg("gg.norisk.NoRiskClientLauncherV3", CYAN_DEEP)
def noriskclient():
    out = path("M32 4L54 12V32Q54 48 32 58Q10 48 10 32V12Z", INK)
    return fit(out + poly([(25, 20), (25, 42), (43, 31)], HOLE, 2.4), 0.65, 32.0, 29.1)


@reg("gg.tesseract.Tesseract", DEEP_ORANGE)
def tesseract():
    out = rrect(8, 8, 30, 30, 3, "none", f' stroke="{INK}" stroke-width="4.2"') + rrect(26, 26, 30, 30, 3, "none", f' stroke="{INK}" stroke-width="4.2"')
    return fit(out + ink_stroke("M8 8L26 26M38 8L56 26M8 38L26 56M38 38L56 56", 3.4), 0.51, 32.0, 31.3)


@reg("hu.irl.sysex-controls", DEEP_PURPLE_LIGHT)
def sysexcontrols():
    out = ink_circle(32, 34, 20) + line(32, 34, 40, 20, HOLE, 4.6)
    return fit(out + ink_stroke("M13 52A26 26 0 0 1 8 32", 3.4) + ink_stroke("M51 52A26 26 0 0 0 56 32", 3.4) + ink_circle(32, 34, 3.8, HOLE), 0.70, 32.0, 35.9)


@reg("id.my.ttl.TruckersToolLinux", PURPLE_SOFT)
def truckers():
    out = rrect(4, 14, 34, 30, 3, INK) + path("M40 22H50L58 32V44H40Z", INK) + path("M44 26H49L53 32H44Z", HOLE)
    for x in (16, 48):
        out += ink_circle(x, 47, 8, INK, f' stroke="{HOLE}" stroke-width="3"') + ink_circle(x, 47, 2.6, HOLE)
    return fit(out, 0.59, 29.5, 32.8)


@reg("im.bernard.Funkcio", BLUE_GREY)
def funkcio():
    out = ink_stroke("M38 8Q26 6 26 18V52M16 24H38", 7) + ink_stroke("M42 30L56 52M56 30L42 52", 4.6)
    return fit(out, 0.64, 39.6, 31.0)


@reg("im.bernard.Memorado", LIGHT_BLUE)
def memorado():
    back = dim(rot(rrect(10, 8, 32, 42, 5, INK), -10, 26, 29), .5)
    front = rot(rrect(22, 14, 32, 42, 5, INK) + ink_stroke("M32 29Q32 23 38 23Q44 23 44 29Q44 33 38 36V39", 3.8, HOLE) + ink_circle(38, 46, 2.4, HOLE), 8, 38, 35)
    return fit(back + front, 0.60, 29.4, 33.2)


@reg("im.bernard.Parolu", ORANGE_DEEP)
def parolu():
    out = path("M10 8H54Q58 8 58 12V38Q58 42 54 42H30L16 54V42H10Q6 42 6 38V12Q6 8 10 8Z", INK)
    for x, h in ((16, 4), (24, 10), (32, 15), (40, 8), (48, 4)):
        out += line(x, 25 - h, x, 25 + h, HOLE, 4)
    return fit(out, 0.59, 32.0, 26.5)


@reg("in.bharatkalluri.splash", PURPLE_LIGHT)
def splash():
    drop = path("M32 4C32 4 18 20 18 30A14 14 0 0 0 46 30C46 20 32 4 32 4Z", INK)
    return fit(drop + ell(32, 52, 24, 5.6, "none").replace('fill="none"', f'fill="none" stroke="{INK}" stroke-width="3.8"') + ink_stroke("M32 36A6 6 0 0 1 26 30", 3, HOLE) + ink_stroke("M10 40L14 36M54 40L50 36", 3.6), 0.58, 32.0, 34.7)


@reg("in.co.nandakumar.amsam", DEEP_PURPLE_SOFT)
def amsam():
    return fit(ink_stroke("M10 54L28 8L46 54", 7.4) + line(18, 38, 38, 38, INK, 6), 0.60, 28.0, 33.8)


@reg("in.co.nandakumar.vara", GREY_DARK)
def vara():
    out = path("M8 52C14 28 28 10 54 8C50 30 34 48 8 52Z", INK)
    return fit(out + ink_stroke("M14 48C26 36 36 24 46 16", 3.4, HOLE), 0.58, 31.0, 29.3)


@reg("in.org.dawn.wikilynx", BLUE_DEEP)
def wikilynx():
    out = path("M10 8L24 20H40L54 8L56 36Q56 52 32 58Q8 52 8 36Z", INK)
    return fit(out + poly([(22, 28), (28, 32), (23, 36)], HOLE, 1.6) + poly([(42, 28), (36, 32), (41, 36)], HOLE, 1.6) + poly([(28, 44), (36, 44), (32, 49)], HOLE, 1.2), 0.62, 32.0, 27.5)


@reg("in.suyogtandel.picoforge", AMBER)
def picoforge():
    out = path("M6 22H46Q56 22 58 14Q50 10 46 12H18Q8 12 6 22Z", INK) + path("M18 22H44L40 34H22Z", INK) + rrect(22, 34, 20, 8, 2, INK) + rrect(14, 42, 36, 12, 3, INK)
    return fit(out + line(24, 18, 40, 18, HOLE, 2.8), 0.62, 33.7, 29.9)


@reg("in.varb.Ausweiskopie", PINK_LIGHT)
def ausweiskopie():
    back = dim(rrect(14, 6, 44, 30, 5, INK), .45)
    front = rrect(6, 20, 46, 32, 5, INK) + ink_circle(19, 32, 5, HOLE) + path("M11 46Q11 39 19 39Q27 39 27 46Z", HOLE) + line(32, 30, 45, 30, HOLE, 3.4) + line(32, 38, 45, 38, HOLE, 3.4)
    return fit(back + front, 0.56, 31.9, 28.1)


@reg("info.cinfinity.cdfp", TEAL_DEEP)
def cdfp():
    out = rrect(6, 10, 34, 44, 4, INK) + line(12, 18, 32, 18, HOLE, 3) + line(12, 25, 26, 25, HOLE, 3)
    disc = ink_circle(42, 38, 15, INK, f' stroke="{HOLE}" stroke-width="3.4"') + ink_circle(42, 38, 5, HOLE) + ink_circle(42, 38, 2, INK)
    return fit(out + disc, 0.61, 28.6, 31.3)


@reg("info.cinfinity.goldstein", AMBER)
def goldstein():
    out = poly([(20, 8), (44, 8), (50, 24), (14, 24)], INK, 2.4) + poly([(8, 28), (30, 28), (34, 48), (4, 48)], INK, 2.4) + poly([(34, 28), (56, 28), (60, 48), (30, 48)], INK, 2.4)
    return fit(out + star4(32, 16, 4.4, HOLE), 0.58, 32.0, 35.3)


@reg("info.exult.exult", INDIGO)
def exult():
    out = ink_stroke("M32 30V58M20 40H44", 7) + ink_stroke("M32 30C18 28 20 6 32 6C44 6 46 28 32 30Z", 6.4)
    return fit(out, 0.62, 32.0, 31.4)


@reg("info.rttr.Return-To-The-Roots", YELLOW_DARK)
def roots():
    out = path("M32 6C14 8 8 24 18 32C24 36 30 34 32 32C34 34 40 36 46 32C56 24 50 8 32 6Z", INK) + line(32, 32, 32, 42, INK, 6)
    out += ink_stroke("M32 42Q30 50 18 54M32 42Q34 50 46 54M32 42V58", 4.4)
    return fit(out + ink_stroke("M32 12V28", 3.4, HOLE), 0.67, 32.0, 32.6)


@reg("ink.scribl.Scribl", RED_LIGHT)
def scribl():
    return fit(ink_stroke("M8 36C12 14 24 12 24 28C24 44 36 48 38 32C40 18 30 16 34 28C38 40 52 36 56 22", 5.4) + ink_stroke("M10 54H54", 3.8), 0.60, 33.5, 37.3)


@reg("ink.whis.Whis", CYAN)
def whis():
    out = ring_c(26, 36, 17, 7.4) + path("M32 6H56V20H40Z", INK)
    return fit(out + ink_circle(26, 36, 4.4), 0.58, 33.6, 27.7)


@reg("io.anytype.anytype", DEEP_ORANGE_DARK)
def anytype():
    return fit(ink_circle(18, 18, 12) + rrect(34, 6, 24, 24, 5, INK) + poly([(6, 56), (30, 56), (18, 34)], INK, 3) + rot(rrect(38, 38, 18, 18, 3, INK), 45, 47, 47), 0.51, 30.8, 31.8)


@reg("io.blockloader.BlockLoader", DEEP_PURPLE_DEEP)
def blockloader():
    out = rrect(14, 8, 36, 28, 5, INK) + line(14, 18, 50, 18, HOLE, 3)
    return fit(out + ink_stroke("M32 40V52", 4.6) + poly([(24, 50), (40, 50), (32, 58)], INK, 1.6) + ink_stroke("M8 58H56", 4), 0.55, 32.0, 37.3)


@reg("io.defn.Franz", GREY_LIGHT)
def franz():
    out = path("M10 8H54Q58 8 58 12V38Q58 42 54 42H28L14 54V42H10Q6 42 6 38V12Q6 8 10 8Z", INK)
    return fit(out + ink_stroke("M42 16H22V36M22 26H37", 5.2, HOLE), 0.58, 32.0, 27.3)


@reg("io.edcd.EDMarketConnector", BLUE_GREY_LIGHT)
def edmc():
    ship = path("M32 4L40 22L58 46L42 42L32 52L22 42L6 46L24 22Z", INK)
    return fit(ship + path("M32 18L36 30L32 36L28 30Z", HOLE), 0.63, 32.0, 32.5)


@reg("io.emeric.toolblex", LIGHT_BLUE_DEEP)
def toolblex():
    out = rrect(6, 20, 52, 34, 5, INK) + ink_stroke("M22 20V12Q22 8 26 8H38Q42 8 42 12V20", 4.4) + line(6, 34, 58, 34, HOLE, 3)
    return fit(out + rrect(26, 30, 12, 10, 2.4, HOLE), 0.61, 32.1, 34.4)


@reg("io.emeric.watchflower", PINK)
def watchflower():
    out = ""
    for a in range(0, 360, 72):
        out += rot(ell(32, 14, 7, 11), a, 32, 28)
    return fit(out + ink_circle(32, 28, 7, HOLE) + ink_stroke("M32 40V58", 4.6) + path("M32 52Q42 52 46 44Q36 44 32 52Z", INK), 0.64, 32.0, 30.9)


@reg("io.frama.editide.editide", PURPLE)
def editide():
    return fit(ink_stroke("M22 14L6 31L22 48", 6.4) + ink_stroke("M42 14L58 31L42 48", 6.4) + ink_stroke("M36 10L28 52", 5), 0.63, 32.0, 30.3)


@reg("io.frama.tractor.carburetor", DEEP_PURPLE)
def carburetor():
    out = path("M32 14C52 22 58 38 50 50Q32 62 14 50C6 38 12 22 32 14Z", INK) + ink_stroke("M32 14C26 8 28 4 34 4", 4.4)
    return fit(out + ink_stroke("M32 20C22 28 22 44 32 52M32 20C42 28 42 44 32 52", 3, HOLE) + line(32, 20, 32, 52, HOLE, 3), 0.66, 32.0, 28.5)


@reg("io.github.ADG_Foundation.Java-Geometry-Expert", GREY_LIGHT)
def geoexpert():
    out = ring_c(32, 30, 22, 3.8) + ink_stroke("M32 12L50 42H14Z", 4.6) + line(32, 12, 32, 42, INK, 3.4)
    return fit(out + ink_circle(32, 12, 4) + ink_circle(50, 42, 4) + ink_circle(14, 42, 4), 0.73, 32.0, 30.4)


@reg("io.github.ADG_Foundation.gclc", BLUE)
def gclc():
    out = ink_stroke("M32 6V16", 5) + ink_stroke("M32 16L12 54M32 16L52 54", 5.4) + ink_circle(32, 12, 5.4)
    return fit(out + ink_stroke("M14 58Q32 46 50 58", 3.6) , 0.59, 32.0, 34.1)


@reg("io.github.Adda0.Stardrop", YELLOW_DARK)
def stardrop():
    out = star5(32, 24, 24) + path("M32 40C32 40 22 50 22 54A10 10 0 0 0 42 54C42 50 32 40 32 40Z", INK)
    return fit(out, 0.57, 32.0, 31.1)


@reg("io.github.AllanChain.sane-break", PINK_DEEP)
def sanebreak():
    out = path("M10 28H46V42Q46 54 34 54H22Q10 54 10 42Z", INK) + ink_stroke("M46 32H50Q56 32 56 38Q56 44 50 44H46", 4.4)
    return fit(out + ink_stroke("M20 20Q16 14 20 8M30 20Q26 14 30 8M40 20Q36 14 40 8", 3.6) + line(10, 60, 46, 60, INK, 3.6), 0.57, 28.0, 35.0)


@reg("io.github.Archeb.opentrace", TEAL)
def opentrace():
    out = ink_stroke("M10 50H28V34H46V16", 4.4) + ink_circle(10, 50, 5.4) + ink_circle(28, 34, 5.4) + ink_circle(46, 16, 5.4)
    return fit(out + ring_c(46, 16, 10, 3.2), 0.55, 30.3, 30.3)


@reg("io.github.Arisotura.CoinKiller", AMBER_LIGHT)
def coinkiller():
    out = ell(32, 30, 18, 24) + ell(32, 30, 8, 14, HOLE)
    return fit(out + ink_stroke("M29 10L36 22L28 30L36 42L31 51", 3, HOLE), 0.76, 32.0, 29.3)


@reg("io.github.AronCalvert.Workouts", GREY_DEEP)
def workouts():
    out = line(14, 30, 50, 30, INK, 5.6) + rrect(4, 20, 9, 20, 3, INK) + rrect(15, 14, 9, 32, 3.4, INK) + rrect(40, 14, 9, 32, 3.4, INK) + rrect(51, 20, 9, 20, 3, INK)
    return fit(out, 0.63, 32.0, 29.3)


@reg("io.github.AshBuk.FingerGo", YELLOW)
def fingergo():
    out = ink_stroke("M12 34V28A20 20 0 0 1 52 28V34", 4.4) + ink_stroke("M20 38V28A12 12 0 0 1 44 28V42", 4.4) + ink_stroke("M28 52V28A4 4 0 0 1 36 28V50", 4.4)
    return fit(out + ink_stroke("M52 44Q52 54 46 58M44 50Q44 54 40 58", 4), 0.64, 34.9, 33.0)


@reg("io.github.BlazingHotCode.CircuitSim", RED)
def circuitsim():
    out = path("M18 10H32A20 20 0 0 1 32 50H18Z", INK) + ink_stroke("M4 21H18M4 39H18M52 30H60", 4.4)
    return fit(out, 0.59, 31.2, 29.3)


@reg("io.github.Bollos00.LibreMines", BLUE_GREY)
def libremines():
    out = ink_circle(32, 30, 15)
    for a in range(0, 180, 45):
        out += rot(line(32, 6, 32, 54, INK, 5), a, 32, 30)
    return fit(out + ink_circle(26, 24, 4, HOLE), 0.69, 32.0, 29.3)


@reg("io.github.BrisklyDev.Brisk", DEEP_ORANGE_LIGHT)
def brisk():
    return fit(poly([(36, 4), (12, 34), (28, 34), (24, 58), (52, 24), (35, 24)], INK, 3), 0.63, 30.0, 30.3)


@reg("io.github.BuddySirJava.SSH-Studio", DEEP_PURPLE)
def sshstudio():
    out = ring_c(18, 20, 11, 6) + ink_stroke("M26 28L52 54M42 44L50 36M48 50L54 44", 5.4)
    return fit(out, 0.56, 31.0, 32.3)


@reg("io.github.C_Yassin.AmethystMiner", PURPLE)
def amethyst():
    def prism(x, y0, w):
        return poly([(x, y0), (x + w, y0 + 9), (x + w, 52), (x - w, 52), (x - w, y0 + 9)], INK, 2.4)
    out = rot(prism(13, 22, 7), -14, 13, 52) + rot(prism(51, 20, 7), 14, 51, 52) + prism(32, 6, 9.4)
    return fit(out + line(32, 18, 32, 46, HOLE, 3) + ink_stroke("M6 58H58", 4), 0.54, 32.0, 38.3)


@reg("io.github.C_Yassin.FlameGet", DEEP_ORANGE)
def flameget():
    out = path("M32 4C36 18 52 24 52 42A20 20 0 0 1 12 42C12 32 18 28 22 20C24 26 28 28 30 26C32 20 30 12 32 4Z", INK)
    return fit(out + ink_stroke("M32 32V46", 4.4, HOLE) + poly([(25, 43), (39, 43), (32, 51)], HOLE, 1.4), 0.63, 32.0, 32.5)


@reg("io.github.CardiJey.schulrechner", LIGHT_BLUE)
def schulrechner():
    out = rrect(10, 4, 44, 56, 7, INK) + rrect(16, 10, 32, 14, 3, HOLE)
    for x in (16, 28, 40):
        for y in (31, 41, 51):
            out += rrect(x, y, 8, 6, 2, HOLE)
    return fit(out, 0.56, 32.0, 31.3)


@reg("io.github.Cookiiieee.WSelector", ORANGE_LIGHT)
def wselector():
    out = ""
    for x, y, dx, dy in ((8, 8, 1, 1), (56, 8, -1, 1), (8, 44, 1, -1), (56, 44, -1, -1)):
        out += ink_stroke(f"M{x} {y + 10 * dy}V{y}H{x + 10 * dx}", 4.4)
    return fit(out + poly([(26, 18), (26, 46), (34, 38), (40, 50), (45, 48), (39, 36), (49, 35)], INK, 2.4), 0.57, 32.0, 25.3)


@reg("io.github.CsoundQt.CsoundQt", PURPLE_DEEP)
def csoundqt():
    out = ell(18, 44, 9, 7) + line(26, 42, 26, 8, INK, 5) + ink_stroke("M26 8Q40 8 40 22", 5)
    return fit(out + ink_stroke("M30 48C38 36 44 36 48 44S56 52 60 40", 4.4), 0.64, 34.6, 31.9)


@reg("io.github.DCCXXV.dolm", INDIGO_SOFT)
def dolm():
    out = path("M10 8H46Q50 8 50 12V38Q50 42 46 42H26L14 54V42H10Q6 42 6 38V12Q6 8 10 8Z", INK)
    return fit(out + line(16, 18, 38, 18, HOLE, 3.4) + line(16, 28, 30, 28, HOLE, 3.4) + star4(54, 46, 9), 0.54, 34.9, 27.1)
