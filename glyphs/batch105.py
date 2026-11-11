# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 105: Pfeilspiel to worklog."""
from lm import (
    AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_LIGHT, BLUE_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP, circle, CYAN, CYAN_DARK,
    CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_PURPLE, DEEP_PURPLE_DARK,
    DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, f, GREY, GREY_DARK, GREY_DEEP, HOLE, INDIGO_DARK,
    INDIGO_DEEP, INDIGO_LIGHT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_LIGHT, line, ORANGE_DEEP, PINK, PINK_DARK, PINK_DEEP, PINK_LIGHT, poly, pt,
    PURPLE, PURPLE_DARK, PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, TEAL,
    TEAL_DEEP, TEAL_LIGHT, YELLOW_DARK,
)
from glyphs.kit import (
    arc_arrow, arrowhead, bubble, crescent_b, ell, ellring, fit, hs, hx, ink_circle, ink_path, ink_stroke, registry, ring_c, ink_rrect, rot, star4, star5)

ICONS, SMALL, reg, _ = registry()


@reg("page.codeberg.maerchenfeeimgarten.Pfeilspiel", DEEP_PURPLE)
def pfeilspiel():
    out = ring_c(28, 36, 20, 5) + ink_circle(28, 36, 6) + ink_stroke("M33 31L53 11", 4.5) + ink_stroke("M54 20V10H44", 4.5)
    return fit(out, 0.589, 30.9, 33.1)


@reg("page.codeberg.maerchenfeeimgarten.doors_app", PURPLE_SOFT)
def doors_app():
    out = ink_rrect(14, 6, 36, 52, 4) + ink_rrect(21, 13, 22, 38, 2, HOLE) + ink_circle(37, 33, 3.4)
    return fit(out, 0.682, 32.0, 32.0)


@reg("page.codeberg.ostfriese4.Untis", GREY)
def untis():
    out = ink_rrect(6, 8, 52, 48, 6) + ink_rrect(12, 14, 40, 6, 2, HOLE) + "".join(ink_rrect(12 + 15 * i, 26, 10, 8, 2, HOLE) for i in range(3)) + "".join(ink_rrect(12 + 15 * i, 40, 10, 8, 2, HOLE) for i in range(2))
    return fit(out, 0.625, 32.0, 32.0)


@reg("page.codeberg.outfly.outfly", BLUE_DEEP)
def outfly():
    out = poly([(6, 28), (58, 8), (42, 56), (30, 38)], INK, 2) + ink_stroke("M30 38L58 8", 2.6, HOLE)
    return fit(out, 0.565, 32.0, 32.0)


@reg("page.codeberg.papojari.Find_Billy", YELLOW_DARK)
def find_billy():
    out = ring_c(26, 26, 18, 6) + ink_stroke("M40 40L56 56", 7) + ink_circle(26, 21, 5) + ink_path("M16 36Q16 28 26 28T36 36Z")
    return fit(out, 0.555, 32.2, 32.2)


@reg("page.codeberg.petsoi.coronet", RED)
def coronet():
    out = poly([(8, 46), (8, 18), (20, 32), (32, 12), (44, 32), (56, 18), (56, 46)], INK, 3) + ink_rrect(8, 49, 48, 8, 3)
    return fit(out, 0.64, 32.0, 33.8)


@reg("page.codeberg.petsoi.pully", CYAN_DARK)
def pully():
    out = ink_circle(32, 30, 15) + ink_circle(32, 30, 5, HOLE) + ink_stroke("M17 30V6", 4.5) + ink_stroke("M47 30V42", 4.5) + ink_rrect(39, 42, 16, 14, 3)
    return fit(out, 0.641, 34.9, 29.9)


@reg("page.codeberg.petsoi.words", ORANGE_DEEP)
def words():
    out = ink_stroke("M8 52L22 12L36 52M13 38H31", 5.5) + ring_c(48, 44, 7, 4.5) + ink_stroke("M55 37V52", 4.5)
    return fit(out, 0.614, 31.2, 32.0)


@reg("page.codeberg.sesivany.Meshy", PURPLE)
def meshy():
    out = ink_stroke("M8 52H56L32 10Z", 4) + ink_stroke("M20 31H44M32 52L20 31M32 52L44 31M32 10V31", 3) + "".join(ink_circle(x, y, 4.5) for x, y in [(8, 52), (56, 52), (32, 10)])
    return fit(out, 0.564, 32.0, 31.0)


@reg("page.codeberg.snensmens.Chapterize", INDIGO_LIGHT)
def chapterize():
    out = "".join(ink_rrect(6, y, 10, 10, 2) + ink_rrect(22, y + 2, 36 if k < 2 else 26, 6, 3) for k, y in enumerate((10, 27, 44)))
    return fit(out, 0.617, 32.0, 32.0)


@reg("page.codeberg.tahoso.azul-box", BROWN)
def azul_box():
    out = ink_rrect(8, 26, 48, 32, 4) + ink_rrect(4, 12, 56, 13, 3) + ink_rrect(24, 34, 16, 5, 2.5, HOLE)
    return fit(out, 0.587, 32.0, 35.0)


@reg("page.codeberg.terratactician_expandoria.game", INDIGO_DEEP)
def game():
    out = hx(20, 22, 11) + hx(44, 22, 11) + hx(32, 43, 11)
    return fit(out, 0.725, 32.0, 32.5)


@reg("page.codeberg.tpikonen.geobug", YELLOW_DARK)
def geobug():
    out = ink_circle(32, 28, 18) + poly([(18, 38), (46, 38), (32, 58)], INK, 2) + ink_circle(32, 28, 7, HOLE) + ink_stroke("M26 12L21 5M38 12L43 5", 3.6)
    return fit(out, 0.646, 32.0, 31.1)


@reg("page.codeberg.tpikonen.satellite", BLUE_GREY)
def satellite():
    out = rot(ink_rrect(24, 22, 16, 20, 3) + ink_rrect(4, 26, 15, 12, 2) + ink_rrect(45, 26, 15, 12, 2) + ink_stroke("M19 32H24M40 32H45", 3), -40, 32, 32) + ink_stroke("M42 50Q52 50 52 40", 4) + ink_stroke("M42 58Q60 58 60 40", 4)
    return fit(out, 0.661, 34.8, 35.1)


@reg("page.codeberg.vendillah.GamepadMirror", LIGHT_BLUE_DARK)
def gamepadmirror():
    out = ink_rrect(6, 20, 52, 28, 12) + ink_stroke("M20 28V40M14 34H26", 3.8, HOLE) + ink_circle(43, 30, 3.2, HOLE) + ink_circle(50, 37, 3.2, HOLE)
    return fit(out, 0.692, 32.0, 34.0)


@reg("page.codeberg.yeldham.Librerama", AMBER_DEEP)
def librerama():
    out = ink_path("M30 14Q20 8 6 12V50Q20 46 30 52Z") + ink_path("M34 14Q44 8 58 12V50Q44 46 34 52Z")
    return fit(out, 0.637, 32.0, 31.2)


@reg("page.kramo.Sly", PINK)
def sly():
    out = ink_stroke("M46 18Q40 8 30 8Q16 8 16 20Q16 30 32 32Q48 34 48 44Q48 56 34 56Q22 56 16 46", 6.5)
    return fit(out, 0.661, 32.0, 32.0)


@reg("page.wisha.platen", TEAL_DEEP)
def platen():
    out = ink_rrect(6, 10, 52, 16, 8) + ink_circle(14, 18, 3.4, HOLE) + ink_rrect(16, 30, 32, 26, 2) + ink_stroke("M22 40H42M22 47H36", 3, HOLE)
    return fit(out, 0.653, 32.0, 33.0)


@reg("pl.fuzjajadrowa.pulsar", DEEP_ORANGE)
def pulsar():
    out = ink_circle(32, 32, 9) + ink_stroke("M32 6V18M32 46V58", 5.5) + ellring(32, 32, 25, 10, 3.6)
    return fit(out, 0.626, 32.0, 32.0)


@reg("pl.ksefinvoice.KsefInvoice", DEEP_PURPLE_DEEP)
def ksefinvoice():
    out = ink_path("M14 6H50V58L44 53L38 58L32 53L26 58L20 53L14 58Z") + ink_stroke("M22 18H42M22 28H42M22 38H34", 3.6, HOLE)
    return fit(out, 0.652, 32.0, 32.0)


@reg("pl.nieto.fityk", PURPLE_SOFT)
def fityk():
    out = ink_stroke("M8 8V56H58", 4) + ink_stroke("M12 50Q24 50 28 34Q32 10 36 34Q40 50 56 50", 5) + ink_circle(18, 44, 2.8) + ink_circle(46, 44, 2.8)
    return fit(out, 0.56, 33.0, 32.0)


@reg("pl.suve.colorful", GREY)
def colorful():
    out = ell(32, 32, 26, 22) + ink_circle(18, 30, 4, HOLE) + ink_circle(28, 18, 4, HOLE) + ink_circle(42, 20, 4, HOLE) + ink_circle(48, 34, 4, HOLE) + ell(36, 44, 8, 6, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("place.derpy.ketchup", BLUE_DARK)
def ketchup():
    out = ink_rrect(20, 26, 24, 32, 8) + poly([(27, 27), (37, 27), (36, 13), (28, 13)], INK, 1) + poly([(28, 12), (36, 12), (32, 4)], INK, 1.5) + ink_rrect(24, 36, 16, 11, 2, HOLE)
    return fit(out, 0.658, 32.0, 30.6)


@reg("pro.saladin.Eeman", YELLOW_DARK)
def eeman():
    out = crescent_b(26, 32, 22) + star5(46, 24, 9)
    return fit(out, 0.706, 29.5, 32.0)


@reg("pw.mmk.OpenFreebuds", RED)
def openfreebuds():
    out = ell(26, 24, 15, 17) + ink_rrect(30, 30, 12, 28, 6) + ink_circle(24, 24, 5.5, HOLE)
    return fit(out, 0.706, 26.5, 32.5)


@reg("radio.k0swe.Kel_Agent", CYAN_DEEP)
def kel_agent():
    out = ink_stroke("M32 24V58M20 58H44", 5) + ink_circle(32, 20, 5.5) + ink_stroke("M22 10Q15 20 22 30M42 10Q49 20 42 30", 4) + ink_stroke("M13 4Q2 20 13 36M51 4Q62 20 51 36", 3.6)
    return fit(out, 0.584, 32.0, 31.4)


@reg("re.fossplant.pbtk", ORANGE_DEEP)
def pbtk():
    out = ink_stroke("M24 8Q16 8 16 16V26Q16 32 8 32Q16 32 16 38V48Q16 56 24 56M40 8Q48 8 48 16V26Q48 32 56 32Q48 32 48 38V48Q48 56 40 56", 4.5) + ink_circle(32, 32, 5.5)
    return fit(out, 0.686, 32.0, 32.0)


@reg("re.fossplant.vmlinux-to-elf", PURPLE_DEEP)
def vmlinux_to_elf():
    out = ink_rrect(6, 6, 24, 20, 4) + ink_rrect(36, 38, 22, 20, 4) + ink_stroke("M30 16H47V26", 4.5) + arrowhead(47, 27, 0, 1, 7)
    return fit(out, 0.585, 32.0, 32.0)


@reg("re.sonny.Playhouse", PURPLE_SOFT)
def playhouse():
    out = poly([(8, 30), (32, 8), (56, 30)], INK, 3) + ink_rrect(14, 28, 36, 28, 3) + poly([(27, 34), (27, 50), (41, 42)], HOLE, 1.5)
    return fit(out, 0.698, 32.0, 31.2)


@reg("re.sonny.Retro", BROWN)
def retro():
    out = ink_rrect(6, 16, 52, 40, 8) + ink_rrect(12, 22, 30, 28, 4, HOLE) + ink_circle(50, 29, 3, HOLE) + ink_circle(50, 42, 3, HOLE) + ink_stroke("M22 8L32 15L42 8", 3.6)
    return fit(out, 0.628, 32.0, 31.1)


@reg("re.sonny.Workbench", INDIGO_DARK)
def workbench():
    out = ink_rrect(6, 28, 52, 8, 2) + ink_rrect(10, 36, 7, 22, 2) + ink_rrect(47, 36, 7, 22, 2) + ink_stroke("M17 48H47", 4) + ink_rrect(22, 8, 20, 16, 3)
    return fit(out, 0.632, 32.0, 33.0)


@reg("ro.fxdata.taskmonitor.viewer", YELLOW_DARK)
def viewer():
    out = ink_rrect(6, 8, 52, 36, 5) + ink_stroke("M12 36L22 26L30 32L42 18L52 24", 3.6, HOLE) + ink_rrect(27, 46, 10, 6, 1) + ink_rrect(20, 52, 24, 5, 2)
    return fit(out, 0.61, 32.0, 32.5)


@reg("ro.go.hmlendea.SokoGrump", BLUE_GREY)
def sokogrump():
    out = ink_rrect(8, 8, 48, 48, 6) + ink_rrect(15, 15, 34, 34, 2, HOLE) + ink_stroke("M15 15L49 49M49 15L15 49", 4.6)
    return fit(out, 0.655, 32.0, 32.0)


@reg("ro.hume.cosmin.ShoppingList", LIGHT_BLUE_DEEP)
def shoppinglist():
    out = ink_stroke("M6 10H14L20 40H48L54 18H16", 4.5) + ink_circle(24, 51, 4.6) + ink_circle(44, 51, 4.6)
    return fit(out, 0.595, 30.0, 31.6)


@reg("rocks.koreader.KOReader", AMBER_DEEP)
def koreader():
    out = ink_rrect(14, 4, 36, 56, 6) + ink_rrect(19, 10, 26, 36, 2, HOLE) + ink_rrect(23, 16, 18, 3, 1.5) + ink_rrect(23, 23, 18, 3, 1.5) + ink_rrect(23, 30, 12, 3, 1.5) + ink_circle(32, 53, 2.6, HOLE)
    return fit(out, 0.643, 32.0, 32.0)


@reg("rocks.noise.qspeakers", PINK_DEEP)
def qspeakers():
    out = ink_rrect(14, 4, 36, 56, 6) + ink_circle(32, 19, 6, HOLE) + ink_circle(32, 43, 11, HOLE) + ink_circle(32, 43, 4.2)
    return fit(out, 0.643, 32.0, 32.0)


@reg("rocks.poopjournal.librelinkupdesktop", TEAL_LIGHT)
def librelinkupdesktop():
    out = ink_path("M32 6C32 6 12 28 12 40A20 20 0 0 0 52 40C52 28 32 6 32 6Z") + ink_stroke("M18 40H26L30 32L36 48L40 40H46", 3.4, HOLE)
    return fit(out, 0.67, 32.0, 33.1)


@reg("rocks.syng.Syng", DEEP_ORANGE)
def syng():
    out = ink_rrect(22, 6, 20, 30, 10) + ink_stroke("M14 28Q14 46 32 46Q50 46 50 28M32 46V56M22 56H42", 4.5) + ink_stroke("M22 20H42", 2.8, HOLE)
    return fit(out, 0.689, 32.0, 32.1)


@reg("rs.ilijaruzic.loopa", DEEP_PURPLE_DARK)
def loopa():
    out = arc_arrow(32, 32, 20, 200, 340, 4.8, 6.5) + arc_arrow(32, 32, 20, 20, 160, 4.8, 6.5)
    return fit(out, 0.72, 32.0, 32.0)


@reg("ru.max.MAX", GREY_DEEP)
def max_icon():
    out = bubble(8, 8, 48, 36) + ink_stroke("M20 36V18L32 28L44 18V36", 4.4, HOLE)
    return fit(out, 0.687, 32.0, 30.9)


@reg("ru.proninyaroslav.libretrack", GREY)
def libretrack():
    out = ink_circle(12, 50, 5) + ink_stroke("M12 50Q30 50 30 38T40 28", 4.5) + ink_circle(46, 18, 10) + ink_circle(46, 18, 4, HOLE) + poly([(38, 24), (54, 24), (46, 38)], INK, 1.5)
    return fit(out, 0.644, 31.5, 31.5)


@reg("ru.sview.sView", BLUE_DEEP)
def sview():
    out = ink_rrect(6, 20, 22, 26, 8) + ink_rrect(36, 20, 22, 26, 8) + ink_rrect(11, 26, 12, 14, 4, HOLE) + ink_rrect(41, 26, 12, 14, 4, HOLE) + ink_stroke("M28 28H36", 4.4)
    return fit(out, 0.692, 32.0, 33.0)


@reg("ru.toxblh.KeeneticManager", YELLOW_DARK)
def keeneticmanager():
    out = ink_rrect(6, 36, 52, 18, 5) + ink_stroke("M16 36L10 14M48 36L54 14M32 36V8", 5) + ink_circle(16, 45, 2.8, HOLE) + ink_circle(26, 45, 2.8, HOLE) + ink_rrect(38, 43, 14, 4, 2, HOLE)
    return fit(out, 0.613, 32.0, 29.8)


@reg("run.chameleon.chameleonultragui", RED_DEEP)
def chameleonultragui():
    out = ink_rrect(6, 14, 52, 36, 6) + ink_rrect(14, 24, 14, 12, 2, HOLE) + ink_stroke("M38 26Q44 32 38 38M45 22Q55 32 45 42", 3, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("sa.sy.bluerecorder", CYAN)
def bluerecorder():
    out = ink_stroke("M18 22L46 42L32 54V10L46 22L18 42", 5.2)
    return fit(out, 0.735, 32.0, 32.0)


@reg("se.cendio.tlclient", ORANGE_DEEP)
def tlclient():
    out = ink_rrect(6, 8, 36, 28, 4) + ink_rrect(22, 26, 36, 28, 4, INK, hs(3)) + ink_stroke("M29 36H51M29 44H42", 3, HOLE)
    return fit(out, 0.621, 32.0, 31.0)


@reg("se.sjoerd.GIScan", PURPLE_DARK)
def giscan():
    out = ring_c(32, 32, 22, 4.5) + ellring(32, 32, 10, 22, 3.4) + ink_stroke("M10 32H54M14 20H50M14 44H50", 3.2)
    return fit(out, 0.742, 32.0, 32.0)


@reg("se.sjoerd.Graphs", BLUE_DEEP)
def graphs():
    out = ink_stroke("M10 8V54H58", 4.2) + ink_stroke("M16 46Q26 12 34 34T54 16", 5)
    return fit(out, 0.582, 34.0, 31.0)


@reg("se.sjoerd.lockpicker", BROWN)
def lockpicker():
    out = ink_rrect(12, 28, 40, 28, 6) + ink_stroke("M20 28V20A12 12 0 0 1 44 20V28", 5.5) + ink_circle(32, 39, 4.4, HOLE) + ink_rrect(30.5, 41, 3, 9, 1, HOLE)
    return fit(out, 0.687, 32.0, 30.6)


@reg("se.trixon.Mapollage", INDIGO_DEEP)
def mapollage():
    out = poly([(6, 14), (22, 8), (22, 50), (6, 56)], INK, 1.5) + poly([(26, 8), (38, 14), (38, 56), (26, 50)], INK, 1.5) + poly([(42, 14), (58, 8), (58, 50), (42, 56)], INK, 1.5)
    return fit(out, 0.568, 32.0, 32.0)


@reg("sh.fhs.ksre", YELLOW_DARK)
def ksre():
    out = ink_stroke("M16 8V56M16 32L46 8M24 28L48 56", 6.5)
    return fit(out, 0.639, 32.0, 32.0)


@reg("sh.tat.bpmdetect", BLUE_GREY_DEEP)
def bpmdetect():
    out = poly([(20, 56), (44, 56), (37, 8), (27, 8)], INK, 3) + ink_stroke("M32 48L42 18", 3.6, HOLE) + ink_circle(40, 24, 4.5, HOLE)
    return fit(out, 0.706, 32.0, 32.0)


@reg("site.someones.Lonewolf", LIGHT_BLUE_LIGHT)
def lonewolf():
    out = poly([(10, 8), (24, 22), (40, 22), (54, 8), (52, 36), (32, 58), (12, 36)], INK, 3) + ink_stroke("M18 33L27 37M46 33L37 37", 3.6, HOLE) + poly([(28, 48), (36, 48), (32, 54)], HOLE, 1.5)
    return fit(out, 0.59, 32.0, 33.0)


@reg("so.libdb.dissent", AMBER_DEEP)
def dissent():
    out = ink_circle(32, 28, 24) + poly([(14, 42), (10, 58), (28, 50)], INK, 2) + ink_stroke("M32 16V30", 5, HOLE) + ink_circle(32, 39, 3, HOLE)
    return fit(out, 0.58, 32.0, 31.5)


@reg("so.onekey.Wallet", PINK_DARK)
def wallet():
    out = ink_rrect(6, 12, 52, 42, 8) + ink_rrect(34, 26, 24, 14, 6, HOLE) + ink_circle(43, 33, 3)
    return fit(out, 0.679, 32.0, 33.0)


@reg("software.haven.HavenDesktop", TEAL_DEEP)
def havendesktop():
    out = ring_c(32, 13, 6, 4.5) + ink_stroke("M32 19V54M20 28H44M10 38Q12 54 32 54Q52 54 54 38", 4.8)
    return fit(out, 0.696, 32.0, 30.6)


@reg("space.f1nn.chorus", DEEP_ORANGE)
def chorus():
    out = ink_stroke("M22 46V16L48 10V40", 4.5) + ell(15, 46, 8, 6) + ell(41, 40, 8, 6)
    return fit(out, 0.686, 28.6, 29.9)


@reg("space.gaiasky.GaiaSky", DEEP_PURPLE_DEEP)
def gaiasky():
    out = ink_circle(32, 32, 13) + rot(ellring(32, 32, 26, 9, 9, HOLE) + ellring(32, 32, 26, 9, 4.4), -25, 32, 32)
    return fit(out, 0.692, 32.0, 32.0)


@reg("space.nouspiro.tenmon", ORANGE_DEEP)
def tenmon():
    out = star4(28, 36, 22) + star4(50, 14, 8)
    return fit(out, 0.645, 32.0, 32.0)


@reg("space.oolite.Oolite", GREY_DEEP)
def oolite():
    out = poly([(6, 32), (26, 20), (58, 28), (58, 36), (26, 44)], INK, 3) + poly([(30, 20), (40, 8), (44, 22)], INK, 2) + poly([(30, 44), (40, 56), (44, 42)], INK, 2) + ink_circle(38, 32, 4, HOLE)
    return fit(out, 0.655, 32.0, 32.0)


@reg("space.rirusha.Cassette", BLUE_LIGHT)
def cassette():
    out = ink_rrect(6, 12, 52, 40, 6) + ink_circle(22, 28, 7.5, HOLE) + ink_circle(42, 28, 7.5, HOLE) + ink_circle(22, 28, 2.8) + ink_circle(42, 28, 2.8) + ink_rrect(18, 41, 28, 6, 2, HOLE)
    return fit(out, 0.676, 32.0, 32.0)


@reg("space.x1z53.iris", YELLOW_DARK)
def iris():
    out = ink_path("M4 32Q32 6 60 32Q32 58 4 32Z") + ink_circle(32, 32, 11, HOLE) + ink_circle(32, 32, 5)
    return fit(out, 0.649, 32.0, 32.0)


@reg("studio.assetmanager.ams", RED_DARK)
def ams():
    out = poly([(32, 6), (58, 18), (32, 30), (6, 18)], INK, 2) + ink_stroke("M6 30L32 42L58 30", 5) + ink_stroke("M6 42L32 54L58 42", 5)
    return fit(out, 0.632, 32.0, 30.8)


@reg("studio.eufonia.EufoniaClient", CYAN_DEEP)
def eufoniaclient():
    out = "".join(ink_rrect(x, 32 - h / 2, 9, h, 4.5) for x, h in ((7, 22), (21, 48), (35, 34), (49, 16)))
    return fit(out, 0.706, 32.5, 32.0)


@reg("studio.okcode.open_alert_viewer", ORANGE_DEEP)
def open_alert_viewer():
    out = ink_path("M32 6C20 6 16 16 16 26V38L10 46H54L48 38V26C48 16 44 6 32 6Z") + ink_circle(32, 53, 5) + ink_stroke("M32 17V30", 4.4, HOLE) + ink_circle(32, 37, 2.6, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("studio.planetpeanut.Bobby", PURPLE_DEEP)
def bobby():
    out = ink_path("M10 40C10 20 20 8 32 8S54 20 54 40Z") + ink_rrect(6, 40, 52, 9, 3) + star5(32, 26, 8, HOLE)
    return fit(out, 0.644, 32.0, 28.5)


@reg("surf.deckr.deckr", PURPLE_SOFT)
def deckr():
    out = rot(ink_rrect(18, 12, 26, 38, 4, INK, hs(2.6)), -22, 32, 54) + rot(ink_rrect(18, 12, 26, 38, 4, INK, hs(2.6)), 22, 32, 54) + ink_rrect(19, 12, 26, 38, 4, INK, hs(2.6)) + ink_circle(32, 31, 6, HOLE)
    return fit(out, 0.679, 31.0, 32.6)


@reg("systems.fracture.launcher", BROWN_DEEP)
def launcher():
    out = ink_path("M32 4C44 12 46 28 44 42H20C18 28 20 12 32 4Z") + poly([(20, 34), (10, 48), (20, 46)], INK, 1.5) + poly([(44, 34), (54, 48), (44, 46)], INK, 1.5) + ink_circle(32, 24, 6, HOLE) + poly([(26, 47), (38, 47), (32, 60)], INK, 1.5)
    return fit(out, 0.634, 32.0, 32.4)


@reg("systems.tranquil.Map", INDIGO_LIGHT)
def map_icon():
    out = rot(ellring(32, 32, 25, 18, 4.4) + ellring(32, 32, 13, 9, 4.4) + ink_circle(32, 32, 2.5), -20, 32, 32)
    return fit(out, 0.679, 32.0, 32.0)


@reg("tech.digiroad.Convertidor", YELLOW_DARK)
def convertidor():
    out = ink_stroke("M8 20H46", 5) + arrowhead(48, 20, 1, 0, 8) + ink_stroke("M56 44H18", 5) + arrowhead(16, 44, -1, 0, 8)
    return fit(out, 0.679, 32.0, 32.0)


@reg("tech.digiroad.ImageFlow", BLUE_GREY_DARK)
def imageflow():
    out = ink_rrect(6, 8, 38, 30, 5) + poly([(12, 32), (22, 19), (30, 28), (34, 23), (40, 32)], HOLE, 1.5) + ink_stroke("M12 50H48", 5) + arrowhead(48, 50, 1, 0, 8)
    return fit(out, 0.612, 31.4, 33.0)


@reg("tech.dongdongbh.mindwtr", LIGHT_BLUE_DEEP)
def mindwtr():
    out = ink_circle(22, 30, 12) + ink_circle(36, 24, 14) + ink_circle(46, 34, 11) + ink_rrect(14, 32, 40, 14, 7) + ink_circle(16, 52, 4) + ink_circle(8, 58, 2.5) + circle(23, 39, 2.6, HOLE) + circle(33, 39, 2.6, HOLE) + circle(43, 39, 2.6, HOLE)
    return fit(out, 0.586, 31.2, 35.2)


@reg("tech.emendir.QR-ScanGen", AMBER_DEEP)
def qr_scangen():
    out = "".join(ink_rrect(x, y, 18, 18, 3) + ink_rrect(x + 4, y + 4, 10, 10, 1, HOLE) + ink_rrect(x + 7, y + 7, 4, 4, 1) for x, y in ((6, 6), (40, 6), (6, 40))) + ink_rrect(40, 40, 7, 7, 1.5) + ink_rrect(51, 51, 7, 7, 1.5) + ink_rrect(40, 51, 7, 7, 1.5)
    return fit(out, 0.568, 32.0, 32.0)


@reg("tech.keyforge.keyforge_master", PINK_DEEP)
def keyforge_master():
    out = rot(ring_c(14, 32, 10, 6) + ink_stroke("M24 32H56M46 32V42M54 32V40", 5), -45, 32, 32)
    return fit(out, 0.699, 31.0, 35.1)


@reg("tf.harmony.UnCSO2", TEAL)
def uncso2():
    out = ink_rrect(8, 34, 48, 22, 4) + ink_stroke("M32 32V18", 5) + arrowhead(32, 18, 0, -1, 10) + ink_rrect(24, 40, 16, 4, 2, HOLE)
    return fit(out, 0.632, 32.0, 31.6)


@reg("tk.deat.Jazz2Resurrection", DEEP_ORANGE_DEEP)
def jazz2resurrection():
    out = rot(ell(22, 18, 6, 14), -10, 22, 18) + rot(ell(42, 18, 6, 14), 10, 42, 18) + ink_circle(32, 40, 18) + ink_circle(25, 38, 3, HOLE) + ink_circle(39, 38, 3, HOLE) + poly([(29, 46), (35, 46), (32, 50)], HOLE, 1.2)
    return fit(out, 0.67, 32.0, 31.1)


@reg("to.bnt.sendworm", DEEP_PURPLE_LIGHT)
def sendworm():
    out = ink_stroke("M10 48Q14 24 30 38T50 22", 9) + ink_circle(52, 18, 8) + ink_circle(54, 16, 2.4, HOLE)
    return fit(out, 0.626, 32.8, 31.2)


@reg("tr.com.ikooskar.ikoOSKAR", BLUE)
def ikooskar():
    out = ink_path("M18 8H46V26A14 14 0 0 1 18 26Z") + ink_stroke("M18 12H8V18Q8 26 18 26M46 12H56V18Q56 26 46 26", 4) + ink_rrect(29, 38, 6, 10, 1) + ink_rrect(20, 48, 24, 8, 2)
    return fit(out, 0.617, 32.0, 32.0)


@reg("tr.gov.uyap.Editor", GREY_DARK)
def editor():
    out = ink_rrect(8, 6, 36, 50, 5) + ink_stroke("M15 18H37M15 27H37M15 36H28", 3.4, HOLE) + ink_path("M48 30L56 38L40 54L30 58L34 48Z", INK, hs(3))
    return fit(out, 0.616, 32.0, 32.0)


@reg("tr.org.pardus.pen", BLUE_DEEP)
def pen():
    out = rot(ink_rrect(26, 4, 12, 34, 4) + poly([(26, 40), (38, 40), (32, 56)], INK, 1.5) + ink_rrect(26, 28, 12, 3, 0, HOLE), 35, 32, 32) + ink_stroke("M6 56Q14 48 20 56", 4)
    return fit(out, 0.606, 27.6, 32.6)


@reg("uk.co._69_studios.kublit", YELLOW_DARK)
def kublit():
    out = poly([(32, 6), (56, 18), (32, 30), (8, 18)], INK, 1.5) + poly([(8, 23), (30, 35), (30, 58), (8, 46)], INK, 1.5) + poly([(34, 35), (56, 23), (56, 46), (34, 58)], INK, 1.5)
    return fit(out, 0.673, 32.0, 32.0)


@reg("uk.co.cappsy.Tesseract", RED_DEEP)
def tesseract():
    out = ink_stroke("M8 24H40V56H8Z", 4.4) + ink_stroke("M24 8H56V40H24Z", 4.4) + ink_stroke("M8 24L24 8M40 24L56 8M8 56L24 40M40 56L56 40", 3.6)
    return fit(out, 0.568, 32.0, 32.0)


@reg("uk.co.easysmartapps.WeatherWidget", CYAN)
def weatherwidget():
    out = ink_circle(24, 24, 10) + "".join(line(*pt(24, 24, 15, a), *pt(24, 24, 20, a), INK, 4) for a in (-180, -135, -90, -45)) + ink_path("M18 54A9 9 0 0 1 18 38A12 12 0 0 1 40 32A10 10 0 0 1 48 54Z", INK, hs(3.2)) + ink_rrect(18, 46, 36, 10, 5)
    return fit(out, 0.589, 28.9, 29.0)


@reg("uk.co.electronstudio.ComicReaderUltimate", ORANGE_DEEP)
def comicreaderultimate():
    out = ink_rrect(6, 6, 28, 24, 3) + ink_rrect(38, 6, 20, 24, 3) + ink_rrect(6, 34, 18, 24, 3) + ink_rrect(28, 34, 30, 24, 3)
    return fit(out, 0.58, 32.0, 32.0)


@reg("uk.co.parallelrealities.games.edgar", PURPLE_LIGHT)
def edgar():
    out = rot(poly([(32, 4), (37, 10), (37, 38), (27, 38), (27, 10)], INK, 1.5) + ink_rrect(18, 38, 28, 6, 3) + ink_rrect(29, 44, 6, 12, 2) + ink_circle(32, 59, 3.4), 40, 32, 32)
    return fit(out, 0.685, 31.0, 32.9)


@reg("uk.co.piggz.amazfish", BLUE_GREY_LIGHT)
def amazfish():
    out = ink_rrect(18, 16, 28, 32, 9) + ink_rrect(22, 4, 20, 14, 3) + ink_rrect(22, 46, 20, 14, 3) + ink_stroke("M32 25V33L38 37", 3.4, HOLE)
    return fit(out, 0.643, 32.0, 32.0)


@reg("uk.co.powdertoy.tpt", BROWN_DARK)
def tpt():
    out = poly([(6, 56), (20, 38), (32, 30), (44, 38), (58, 56)], INK, 3) + ink_circle(32, 8, 3.2) + ink_circle(27, 16, 3.2) + ink_circle(37, 18, 3.2) + ink_circle(32, 22, 2.6)
    return fit(out, 0.548, 32.0, 31.1)


@reg("uk.co.studiopond.spiderbro", INDIGO_DEEP)
def spiderbro():
    out = ink_circle(32, 36, 10) + ink_circle(32, 22, 7) + ink_stroke("M24 33L10 25L8 13M24 38L8 40L6 54M40 33L54 25L56 13M40 38L56 40L58 54", 3.6) + ink_circle(29.5, 20, 1.8, HOLE) + ink_circle(34.5, 20, 1.8, HOLE)
    return fit(out, 0.588, 32.0, 33.5)


@reg("uk.co.studiopond.spiderbro2", YELLOW_DARK)
def spiderbro2():
    octa = lambda r: "M" + "L".join("%s %s" % (f(a), f(b)) for a, b in [pt(32, 32, r, 22.5 + 45 * k) for k in range(8)]) + "Z"
    out = ink_stroke("M32 6V58M6 32H58M14 14L50 50M50 14L14 50", 3) + ink_stroke(octa(11), 3.4) + ink_stroke(octa(21), 3.4)
    return fit(out, 0.655, 32.0, 32.0)


@reg("uk.org.greenend.chiark.sgtatham.puzzles", BLUE_GREY_DEEP)
def puzzles():
    out = ink_path("M8 18H24C24 8 40 8 40 18H56V30C48 30 48 44 56 44V56H8Z")
    return fit(out, 0.623, 32.0, 33.2)


@reg("uno.platform.uno-calculator", LIGHT_BLUE)
def uno_calculator():
    out = ink_rrect(12, 4, 40, 56, 6) + ink_rrect(18, 10, 28, 12, 2, HOLE) + "".join(ink_rrect(18 + 11 * i, 28 + 10 * j, 7, 6, 2, HOLE) for i in range(3) for j in range(2)) + ink_rrect(18, 49, 28, 6, 2, HOLE)
    return fit(out, 0.64, 32.0, 32.0)


@reg("us.acei.AbsoluteInfinity", AMBER_DEEP)
def absoluteinfinity():
    out = ink_stroke("M32 32C24 18 8 20 8 32C8 44 24 46 32 32C40 18 56 20 56 32C56 44 40 46 32 32Z", 6)
    return fit(out, 0.667, 32.0, 32.0)


@reg("us.ihmc.cmap.CmapTools", PINK_LIGHT)
def cmaptools():
    out = ink_rrect(20, 6, 24, 14, 5) + ink_rrect(4, 44, 22, 14, 5) + ink_rrect(38, 44, 22, 14, 5) + ink_stroke("M32 20V32M32 32L15 44M32 32L49 44", 3.6)
    return fit(out, 0.568, 32.0, 32.0)


@reg("us.materialio.Materialious", TEAL)
def materialious():
    out = ink_rrect(6, 8, 52, 36, 10) + poly([(26, 18), (26, 34), (40, 26)], HOLE, 1.5) + ink_rrect(6, 50, 52, 5, 2.5) + ink_circle(24, 52.5, 5, INK, hs(2.4))
    return fit(out, 0.618, 32.0, 32.8)


@reg("us.pixls.art.ART", DEEP_ORANGE_DARK)
def art():
    out = ring_c(32, 32, 24, 5) + "".join(ink_stroke("M%s %sL%s %s" % tuple(f(v) for v in (*pt(32, 32, 24, a), *pt(32, 32, 9, a + 100))), 4.2) for a in range(0, 360, 60))
    return fit(out, 0.679, 32.0, 32.0)


@reg("vc.dion.Dion", DEEP_PURPLE_DEEP)
def dion():
    out = ink_stroke("M18 8H30Q50 8 50 32T30 56H18Z", 6.5) + ink_circle(32, 32, 5)
    return fit(out, 0.639, 34.0, 32.0)


@reg("vet.rsc.OpenRSC.Launcher", GREY_DEEP)
def launcher_icon():
    out = ink_path("M32 4L54 12V30C54 44 44 54 32 60C20 54 10 44 10 30V12Z") + ink_rrect(30, 16, 4, 28, 1, HOLE) + ink_rrect(23, 24, 18, 4, 2, HOLE)
    return fit(out, 0.643, 32.0, 32.0)


@reg("vn.hoabinh.quan.CoBang", GREY_DEEP)
def cobang():
    out = ink_stroke("M8 22V8H22M42 8H56V22M56 42V56H42M22 56H8V42", 5) + ink_stroke("M13 32H51", 4.5)
    return fit(out, 0.563, 32.0, 32.0)


@reg("vn.suika3.engine", BLUE)
def engine():
    out = ink_rrect(6, 32, 52, 24, 6) + ink_stroke("M14 42H50M14 49H38", 3.4, HOLE) + ink_rrect(6, 22, 20, 8, 3) + star4(44, 16, 9)
    return fit(out, 0.617, 32.0, 31.4)


@reg("work.worklog.worklog", YELLOW_DARK)
def worklog():
    out = ink_rrect(10, 10, 44, 48, 6) + ink_rrect(22, 5, 20, 11, 4, INK, hs(2.6)) + "".join(ink_circle(20, y, 3, HOLE) + ink_rrect(28, y - 2, 18, 4, 2, HOLE) for y in (28, 38, 48))
    return fit(out, 0.642, 32.0, 31.5)
