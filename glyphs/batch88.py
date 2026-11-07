# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 88: the third hundred apps from the gap list (flags/app-gap-list-full.md),
rows 201 to 300, file_manager to Gitnuro. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import bars, dim, fit_b, H, I, ink_stroke, registry, ring_d

ICONS, SMALL, reg, _ = registry()

@reg("com.expidusos.file_manager", INDIGO)
def file_manager():
    return fit_b(path("M11 20Q11 15 16 15H26L31 21H48Q53 21 53 26V42Q53 47 48 47H16Q11 47 11 42Z", I) + line(11, 28, 53, 28, H, 2.6), 0.75)

@reg("com.fafarunner.FaFaRunner", RED)
def fafarunner():
    return fit_b(circle(37, 14, 5, I) + ink_stroke("M33 24L28 34L18 36M33 24L42 30L48 26M28 34L34 44L30 52M34 44L44 46", 4.2), 0.78)

@reg("com.fanuriotimetracking.fanurio", TEAL_DEEP)
def fanurio():
    return fit_b(ring_d(32, 33, 15, 4.5) + ink_stroke("M32 33V23M32 33L39 38", 4) + rrect(28, 8, 8, 5, 2, I) + line(32, 13, 32, 18, I, 3.5), 0.86)

@reg("com.fastmail.Fastmail", PINK)
def fastmail():
    return fit_b(rrect(12, 17, 40, 28, 5, I) + ink_stroke("M16 23L32 35L48 23", 3.6, H), 0.82)

@reg("com.felipekinoshita.Kana", PURPLE)
def kana():
    return fit_b(ink_stroke("M17 22H44M31 12C31 26 29 38 25 46M42 28C48 33 46 44 38 47C32 49 26 44 31 38", 4.4), 0.93)

@reg("com.flow_browser.flow", BLUE)
def flow():
    return fit_b(ink_stroke("M12 24C20 14 28 34 36 24C42 17 48 22 52 24", 4.5) + ink_stroke("M12 38C20 28 28 48 36 38C42 31 48 36 52 38", 4.5), 0.79)

@reg("com.fogpanther.FogPanther", BLUE_GREY)
def fogpanther():
    head = poly([(14, 12), (26, 20), (38, 20), (50, 12), (50, 32), (32, 44), (14, 32)], I, 3)
    return fit_b(head + poly([(20, 28), (27, 27), (25, 32)], H, 1) + poly([(44, 28), (37, 27), (39, 32)], H, 1) + line(22, 51, 42, 51, I, 3.5), 0.7)

@reg("com.francescogaglione.chronos", DEEP_ORANGE_DEEP)
def chronos():
    return fit_b(poly([(18, 12), (46, 12), (34, 30), (46, 48), (18, 48), (30, 30)], I, 3) + line(14, 12, 50, 12, I, 4) + line(14, 48, 50, 48, I, 4) + poly([(26, 43), (38, 43), (32, 37)], H, 1), 0.69)

@reg("com.gamestarmechanic.gamestarmechanic", DEEP_PURPLE_SOFT)
def gamestarmechanic():
    out = ring_d(32, 30, 14, 7)
    for k in range(8):
        x, y = pt(32, 30, 18, k * 45)
        out += circle(x, y, 3.4, I)
    return fit_b(out + poly([(28, 24), (28, 36), (38, 30)], I, 1.5), 0.88)

@reg("com.geekbench.Geekbench6", DEEP_PURPLE)
def geekbench6():
    return fit_b(ink_stroke("M12 42A21 21 0 1 1 52 42", 5) + ink_stroke("M32 38L42 22", 4.5) + circle(32, 38, 4.5, I) + line(18, 49, 46, 49, I, 3.5), 0.73)

@reg("com.gesturedevelop.AirSQLiteManager", CYAN)
def airsqlitemanager():
    out = ""
    for y in (18, 30, 42):
        out += path(f"M16 {y}C16 {y-6} 48 {y-6} 48 {y}V{y+8}C48 {y+14} 16 {y+14} 16 {y+8}Z", I)
    return fit_b(out + ink_stroke("M16 25C20 31 44 31 48 25", 2.4, H) + ink_stroke("M16 37C20 43 44 43 48 37", 2.4, H), 0.71)

@reg("com.giadamusic.Giada", RED_DEEP)
def giada():
    return fit_b(ink_stroke("M44 22A15 15 0 0 0 18 24M20 38A15 15 0 0 0 46 36", 4.5) + poly([(48, 12), (49, 25), (37, 22)], I, 1.5) + poly([(16, 50), (15, 37), (27, 40)], I, 1.5) + circle(32, 30, 5, I), 0.72)

@reg("com.gitbutler.gitbutler", INDIGO_LIGHT)
def gitbutler():
    return fit_b(ink_stroke("M22 12V48M22 24C22 34 42 28 42 38", 4.2) + circle(22, 14, 5, I) + circle(22, 46, 5, I) + circle(42, 40, 5, I), 0.79)

@reg("com.gitfiend.GitFiend", TEAL)
def gitfiend():
    return fit_b(ink_stroke("M20 14V24C20 32 32 30 32 38V46M44 14V24C44 32 32 30 32 38", 4.2) + circle(20, 14, 5, I) + circle(44, 14, 5, I) + circle(32, 46, 5.5, I) + circle(32, 46, 2, H), 0.75)

@reg("com.github.Alcaro.Flips", PINK_DEEP)
def flips():
    return fit_b(g(rrect(12, 23, 40, 16, 8, I) + rrect(26, 23, 12, 16, 0, H, ' opacity=".35"') + circle(21, 28, 1.8, H) + circle(21, 34, 1.8, H) + circle(43, 28, 1.8, H) + circle(43, 34, 1.8, H), "rotate(-35 32 31)"), 0.92)

@reg("com.github.AlizaMedicalImaging.AlizaMS", LIGHT_BLUE_DEEP)
def alizams():
    return fit_b(ring_d(32, 30, 18, 4) + ring_d(32, 30, 8, 3.4) + line(32, 8, 32, 17, I, 3.4) + line(32, 43, 32, 52, I, 3.4) + line(10, 30, 19, 30, I, 3.4) + line(45, 30, 54, 30, I, 3.4), 0.8)

@reg("com.github.LongSoft.UEFITool", ORANGE)
def uefitool():
    return fit_b(rrect(13, 11, 38, 38, 8, I) + poly([(35, 15), (23, 32), (31, 32), (28, 45), (41, 27), (33, 27)], H, 1.5), 0.8)

@reg("com.github.Xenoveritas.abuse", PURPLE_DEEP)
def abuse():
    return fit_b(rrect(14, 15, 36, 30, 8, I) + poly([(19, 24), (29, 28), (19, 31)], H, 1.5) + poly([(45, 24), (35, 28), (45, 31)], H, 1.5) + line(23, 38, 41, 38, H, 3) + line(32, 8, 32, 15, I, 3.5) + circle(32, 8, 2.5, I), 0.77)

@reg("com.github._0negal.Viper", BLUE_GREY)
def viper():
    return fit_b(ink_stroke("M16 46C8 36 22 32 32 36C42 40 54 30 44 20C38 15 28 18 32 25", 5.5) + poly([(38, 10), (50, 14), (44, 24), (36, 20)], I, 2) + circle(42, 16, 1.8, H), 0.75)

@reg("com.github.arminstraub.krop", PURPLE_LIGHT)
def krop():
    return fit_b(ink_stroke("M20 10V44H54", 4.8) + ink_stroke("M10 20H44V54", 4.8) + rrect(24, 24, 16, 14, 2, I, ' opacity=".5"'), 0.64)

@reg("com.github.arshubham.gitignore", BROWN)
def gitignore():
    return fit_b(rrect(15, 11, 34, 40, 5, I) + line(22, 22, 42, 22, H, 3.2) + line(22, 31, 36, 31, H, 3.2) + line(12, 52, 52, 10, H, 6) + line(12, 52, 52, 10, I, 2.4), 0.58)

@reg("com.github.avojak.paint-spill", TEAL_LIGHT)
def paintspill():
    return fit_b(path("M32 8C25 18 20 24 20 30C20 37 25 41 32 41C39 41 44 37 44 30C44 24 39 18 32 8Z", I) + path("M10 50C14 44 26 46 34 45C44 44 52 44 54 49C54 53 44 53 32 53C20 54 10 54 10 50Z", I, ' opacity=".6"'), 0.62)

@reg("com.github.avojak.warble", DEEP_PURPLE_LIGHT)
def warble():
    return fit_b(rrect(9, 22, 14, 18, 3.5, I) + rrect(25, 22, 14, 18, 3.5, I, ' opacity=".45"') + rrect(41, 22, 14, 18, 3.5, "none", ' stroke="INK" stroke-width="3"') + line(14, 48, 50, 48, I, 3.5), 0.69)

@reg("com.github.bvschaik.julius", PINK_SOFT)
def julius():
    return fit_b(rrect(14, 11, 36, 6, 2, I) + rrect(18, 17, 28, 4, 1, I) + rrect(21, 21, 6, 24, 2, I) + rrect(29, 21, 6, 24, 2, I) + rrect(37, 21, 6, 24, 2, I) + rrect(14, 45, 36, 4, 1, I) + rrect(11, 49, 42, 5, 2, I), 0.61)

@reg("com.github.calo001.luna", ORANGE_DEEP)
def luna():
    return fit_b(circle(29, 31, 18, I) + circle(39, 24, 14.5, H), 0.79)

@reg("com.github.christianrauch.Jahresarbeit-2003", DEEP_PURPLE_DEEP)
def jahresarbeit():
    return fit_b(poly([(32, 11), (52, 22), (32, 33), (12, 22)], I, 2) + poly([(12, 30), (32, 41), (52, 30), (52, 35), (32, 46), (12, 35)], I, 2) + poly([(12, 42), (32, 53), (52, 42), (52, 47), (32, 58), (12, 47)], I, 2), 0.65)

@reg("com.github.cubitect.cubiomes-viewer", BLUE_DEEP)
def cubiomes():
    return fit_b(poly([(32, 10), (52, 21), (32, 32), (12, 21)], I, 1.5) + dim(poly([(12, 25), (30, 35), (30, 55), (12, 45)], I, 1.5), .7) + dim(poly([(34, 35), (52, 25), (52, 45), (34, 55)], I, 1.5), .5), 0.73)

@reg("com.github.devalien.workspaces", BROWN_SOFT)
def workspaces():
    return fit_b(rrect(11, 12, 20, 38, 5, I) + rrect(35, 12, 18, 17, 5, I, ' opacity=".6"') + rrect(35, 33, 18, 17, 5, I), 0.7)

@reg("com.github.dimkr.gplaces", RED_DARK)
def gplaces():
    return fit_b(path("M32 8C21 8 15 16 15 24C15 35 32 53 32 53C32 53 49 35 49 24C49 16 43 8 32 8Z", I) + circle(32, 24, 7, H), 0.83)

@reg("com.github.edenalencar.identifications", BLUE_GREY_DEEP)
def identifications():
    return fit_b(rrect(9, 15, 46, 32, 6, I) + circle(23, 28, 5, H) + path("M14 42C14 35 32 35 32 42Z", H) + line(37, 26, 48, 26, H, 3) + line(37, 33, 48, 33, H, 3), 0.72)

@reg("com.github.emmanueltouzery.cigale", DEEP_ORANGE)
def cigale():
    out = rrect(17, 11, 34, 40, 5, I)
    for y in (20, 30, 40):
        out += line(24, y, 44, y, H, 3) + line(13, y, 19, y, I, 3.6)
    return fit_b(out, 0.72)

@reg("com.github.emmanueltouzery.projectpad", INDIGO)
def projectpad():
    return fit_b(rrect(14, 15, 36, 38, 5, I) + rrect(23, 9, 18, 10, 3, I) + rrect(27, 11, 10, 3, 1.5, H) + ink_stroke("M24 33H40M24 41H34", 3.6, H), 0.69)

@reg("com.github.gpuvis.Gpuvis", AMBER_DARK)
def gpuvis():
    return fit_b(rrect(11, 14, 22, 7, 3, I) + rrect(23, 25, 24, 7, 3, I) + rrect(17, 36, 16, 7, 3, I) + rrect(39, 47, 14, 6, 3, I, ' opacity=".6"') + line(11, 10, 11, 52, I, 2.4), 0.6)

@reg("com.github.gyunaev.spivak", PINK)
def spivak():
    return fit_b(rrect(23, 8, 18, 28, 9, I) + ink_stroke("M16 28C16 44 48 44 48 28M32 42V52M24 52H40", 4) + line(23, 19, 41, 19, H, 2.4) + line(23, 26, 41, 26, H, 2.4), 0.74)

@reg("com.github.hopsan.Hopsan", CYAN_DARK)
def hopsan():
    return fit_b(rrect(10, 18, 15, 24, 4, I) + rrect(39, 18, 15, 24, 4, I) + ink_stroke("M25 25H32V35H39", 4) + circle(32, 30, 3, I), 0.8)

@reg("com.github.horaciodrs.tradesim", PURPLE_SOFT)
def tradesim():
    out = ""
    for x, top, bot, y1, y2 in ((17, 18, 44, 24, 38), (32, 10, 38, 16, 30), (47, 22, 50, 28, 44)):
        out += line(x, top, x, bot, I, 3) + rrect(x - 5, y1, 10, y2 - y1, 2, I)
    return fit_b(out, 0.71)

@reg("com.github.ilai_deutel.kibi", CYAN_DEEP)
def kibi():
    return fit_b(ink_stroke("M20 11V49M44 11L24 31L44 49", 6) + line(31, 49, 48, 49, I, 3.6), 0.71)

@reg("com.github.jkotra.unlockr", RED)
def unlockr():
    return fit_b(rrect(14, 28, 36, 24, 6, I) + ink_stroke("M22 28V20C22 8 40 8 42 18", 5) + circle(32, 38, 4, H) + line(32, 40, 32, 46, H, 3.4), 0.73)

@reg("com.github.jmlich.geotagging", DEEP_PURPLE)
def geotagging():
    return fit_b(rrect(9, 14, 36, 30, 5, I) + poly([(13, 40), (23, 26), (29, 34), (34, 29), (41, 40)], H, 1.5) + circle(36, 22, 3, H) + path("M47 29C42 29 40 33 40 36C40 42 47 50 47 50C47 50 54 42 54 36C54 33 52 29 47 29Z", I, ' stroke="HOLE" stroke-width="2.4"') + circle(47, 36, 2, H), 0.71)

@reg("com.github.juzzlin.DustRacing2D", BLUE)
def dustracing2d():
    return fit_b(rrect(23, 8, 18, 44, 8, I) + rrect(26, 17, 12, 9, 2.5, H) + rrect(26, 36, 12, 6, 2, H) + rrect(15, 14, 6, 11, 2, I) + rrect(43, 14, 6, 11, 2, I) + rrect(15, 36, 6, 11, 2, I) + rrect(43, 36, 6, 11, 2, I), 0.82)

@reg("com.github.kalibari.audok", AMBER)
def audok():
    return fit_b(bars([13, 20, 27, 34, 41, 48], 41, 5, [10, 24, 34, 20, 28, 8]) + line(11, 48, 53, 48, I, 3), 0.65)

@reg("com.github.keriew.augustus", PURPLE)
def augustus():
    return fit_b(ink_stroke("M17 48L32 12L47 48M23 36H41", 5.5) + line(13, 48, 21, 48, I, 4.5) + line(43, 48, 51, 48, I, 4.5) + line(26, 12, 38, 12, I, 4.5), 0.66)

@reg("com.github.makhber.Makhber", TEAL)
def makhber():
    return fit_b(ink_stroke("M13 12V48H52", 4) + ink_stroke("M18 40C26 40 28 16 36 20C42 24 42 38 50 24", 4) + circle(36, 20, 3.5, I) + circle(18, 40, 3.5, I), 0.65)

@reg("com.github.mgropp.PdfJumbler", RED_DEEP)
def pdfjumbler():
    return fit_b(g(rrect(14, 13, 24, 32, 3, I), "rotate(-12 26 29)") + g(rrect(26, 17, 24, 32, 3, I, ' stroke="HOLE" stroke-width="2.6"') + line(31, 28, 45, 28, H, 2.6) + line(31, 35, 42, 35, H, 2.6), "rotate(10 38 33)"), 0.73)

@reg("com.github.mikacousin.olc", INDIGO_SOFT)
def olc():
    out = ""
    for x, kn in ((17, 38), (32, 22), (47, 30)):
        out += line(x, 10, x, 50, I, 3.2, extra=' opacity=".5"') + rrect(x - 7, kn - 5, 14, 10, 3, I)
    return fit_b(out, 0.71)

@reg("com.github.muriloventuroso.pdftricks", DEEP_PURPLE_SOFT)
def pdftricks():
    return fit_b(rrect(13, 11, 30, 40, 4, I) + line(19, 21, 37, 21, H, 3) + line(19, 29, 31, 29, H, 3) + poly([(46, 20), (49, 29), (58, 32), (49, 35), (46, 44), (43, 35), (34, 32), (43, 29)], I, 1), 0.71)

@reg("com.github.nihui.waifu2x-ncnn-vulkan", PINK)
def waifu2x():
    return fit_b(rrect(10, 28, 22, 22, 4, I, ' opacity=".55"') + rrect(26, 10, 28, 28, 5, I) + ink_stroke("M33 31L47 17M38 17H47V26", 3.6, H), 0.67)

@reg("com.github.nrittsti.NTag", DEEP_PURPLE_DARK)
def ntag():
    return fit_b(poly([(10, 31), (30, 11), (52, 11), (52, 33), (32, 53)], I, 4) + circle(41, 22, 4, H), 0.64)

@reg("com.github.polymeilex.neothesia", ORANGE)
def neothesia():
    out = rrect(17, 10, 8, 14, 2.5, I) + rrect(30, 18, 8, 12, 2.5, I, ' opacity=".6"') + rrect(43, 8, 8, 18, 2.5, I)
    out += rrect(11, 36, 42, 16, 3, I)
    for x in (19.5, 28, 36.5, 45):
        out += line(x, 36, x, 52, H, 1.8)
    return fit_b(out, 0.65)

@reg("com.github.powertab.powertabeditor", CYAN_DEEP)
def powertabeditor():
    out = ""
    for y in (14, 24, 34, 44):
        out += line(10, y, 54, y, I, 2.6)
    return fit_b(out + circle(22, 24, 5.5, I) + circle(22, 24, 3, H) + circle(38, 34, 5.5, I) + circle(38, 34, 3, H) + circle(46, 14, 5.5, I) + circle(46, 14, 3, H), 0.66)

@reg("com.github.qarmin.szyszka", ORANGE_DARK)
def szyszka():
    out = path("M32 8C44 8 50 20 48 32C46 46 38 54 32 54C26 54 18 46 16 32C14 20 20 8 32 8Z", I)
    for y, n in ((20, 3), (30, 4), (40, 3)):
        for k in range(n):
            x = 32 + (k - (n - 1) / 2) * 9
            out += ink_stroke(f"M{x-4} {y+2}L{x} {y-3}L{x+4} {y+2}", 2.6, H)
    return fit_b(out, 0.79)

@reg("com.github.raibtoffoletto.litteris", PURPLE_DEEP)
def litteris():
    return fit_b(path("M16 18C16 12 28 12 28 20C28 30 22 36 15 40C22 40 30 36 30 24V18Z", I) + path("M36 18C36 12 48 12 48 20C48 30 42 36 35 40C42 40 50 36 50 24V18Z", I), 0.88)

@reg("com.github.rajsolai.textsnatcher", DEEP_ORANGE_LIGHT)
def textsnatcher():
    out = ring_d(32, 30, 20, 3.2, I).replace('stroke-width="3.2"', 'stroke-width="3.2" stroke-dasharray="7 5"')
    return fit_b(out + line(22, 22, 42, 22, I, 4.4) + line(32, 22, 32, 40, I, 4.4), 0.87)

@reg("com.github.ransome1.sleek", BLUE_GREY_SOFT)
def sleek():
    return fit_b(ring_d(32, 30, 20, 4.4) + circle(32, 30, 6, I), 0.85)

@reg("com.github.reduz.ChibiTracker", INDIGO_DEEP)
def chibitracker():
    out = ""
    for c, x in enumerate((12, 28, 44)):
        out += rrect(x, 11, 10, 40, 3, I, ' opacity=".35"')
        for r in range(5):
            if (r * 2 + c) % 3 != 1:
                out += rrect(x + 2, 15 + r * 7.5, 6, 3.4, 1.2, I)
    return fit_b(out, 0.65)

@reg("com.github.rogercrocker.badabib", PINK_LIGHT)
def badabib():
    return fit_b(path("M20 10H44V20C44 24 46 28 49 32C54 40 46 54 32 54C18 54 10 40 15 32C18 28 20 24 20 10Z", I) + path("M24 10C24 24 40 24 40 10Z", H) + circle(32, 40, 5, H), 0.79)

@reg("com.github.ryonakano.pinit", BLUE_GREY)
def pinit():
    return fit_b(poly([(22, 10), (44, 10), (40, 26), (48, 32), (16, 32), (24, 26)], I, 3) + line(32, 32, 32, 52, I, 3.8), 0.76)

@reg("com.github.sakya.corechess", DEEP_ORANGE_DEEP)
def corechess():
    return fit_b(circle(32, 17, 8, I) + path("M25 29H39L36 33C40 38 43 43 43 47H21C21 43 24 38 28 33Z", I) + rrect(16, 47, 32, 7, 3, I) + rrect(24, 28, 16, 4, 2, H), 0.68)

@reg("com.github.scrivanolabs.scrivano", INDIGO_LIGHT)
def scrivano():
    return fit_b(path("M48 9C34 10 22 20 20 38L17 50L24 46C40 42 50 28 48 9Z", I) + ink_stroke("M18 49L36 28", 3, H) + ink_stroke("M30 24L40 26M26 31L36 33", 2.6, H), 0.72)

@reg("com.github.shonumi.gbe-plus", ORANGE_DARK)
def gbeplus():
    return fit_b(rrect(8, 16, 48, 30, 10, I) + rrect(22, 21, 20, 14, 2.5, H) + line(15, 28, 15, 38, H, 3) + line(10, 33, 20, 33, H, 3) + circle(48, 30, 2.6, H) + circle(52, 38, 2.6, H), 0.75)

@reg("com.github.tenderowl.norka", DEEP_ORANGE_LIGHT)
def norka():
    return fit_b(ink_stroke("M18 49V13L46 49V13", 6.5), 0.7)

@reg("com.github.tmewett.BrogueCE", INDIGO)
def broguece():
    return fit_b(ink_stroke("M44 40C36 49 22 47 18 36C14 25 21 14 33 14C44 14 49 22 47 31C46 38 38 38 38 31V24", 4.5) + ring_d(32, 30, 6.5, 4.5), 0.99)

@reg("com.github.utsushi.Utsushi", PINK_DEEP)
def utsushi():
    return fit_b(rrect(9, 29, 46, 18, 5, I) + path("M14 25L50 25L47 14L17 14Z", I, ' opacity=".6"') + line(14, 38, 50, 38, H, 3.2) + circle(46, 42, 1.8, H), 0.71)

@reg("com.github.varnholt.dynablaster_revenge", CYAN)
def dynablaster():
    return fit_b(circle(30, 36, 16, I) + ink_stroke("M40 22L46 15", 3.6) + poly([(52, 10), (53, 16), (58, 17), (53, 20), (52, 26), (50, 20), (44, 17), (50, 16)], I, 0.8) + ink_stroke("M20 32A10 10 0 0 1 28 26", 3.4, H), 0.64)

@reg("com.github.vikdevelop.timer", RED)
def timer():
    return fit_b(circle(32, 33, 18, I) + path("M32 33V17A16 16 0 0 1 46 41Z", H) + rrect(28, 8, 8, 5, 2, I) + line(32, 13, 32, 16, I, 3.2), 0.86)

@reg("com.github.yucefsourani.albasheer-electronic-quran-browser", BLUE_GREY_DEEP)
def albasheer():
    return fit_b(path("M32 18C26 13 18 13 11 15V47C18 45 26 45 32 50C38 45 46 45 53 47V15C46 13 38 13 32 18Z", I) + path("M32 22C34 22 36 24 36 26C36 30 32 31 32 33C32 31 28 30 28 26C28 24 30 22 32 22Z", H) + line(32, 20, 32, 48, H, 2.2), 0.7)

@reg("com.gitlab.adnan338.Nixwriter", PURPLE)
def nixwriter():
    return fit_b(rrect(21, 22, 22, 30, 5, I) + rrect(24, 10, 16, 13, 2, I, ' opacity=".6"') + rrect(27, 13, 3.5, 5, 1, H) + rrect(34, 13, 3.5, 5, 1, H) + ink_stroke("M32 47V33M26 39L32 33L38 39", 3.6, H), 0.82)

@reg("com.gitlab.azymohliad.Qwertone", TEAL_LIGHT)
def qwertone():
    return fit_b(rrect(11, 11, 42, 40, 9, I) + ring_d(30, 29, 9, 4.4, H) + line(35, 34, 43, 42, H, 4.4), 0.73)

@reg("com.gitlab.coringao.JAG", INDIGO_LIGHT)
def jag():
    return fit_b(path("M13 38C13 22 21 14 32 14C43 14 51 22 51 38Z", I) + rrect(9, 38, 46, 8, 4, I) + poly([(32, 19), (34, 24), (39, 25), (35, 28), (36, 33), (32, 30), (28, 33), (29, 28), (25, 25), (30, 24)], H, .5), 0.71)

@reg("com.gitlab.guillermop.MasterKey", AMBER_DEEP)
def masterkey():
    return fit_b(ring_d(22, 30, 11, 5.4) + ink_stroke("M33 30H54M46 30V38M53 30V36", 5), 0.77)

@reg("com.gitlab.j0chn.nextcloud_password_client", DEEP_PURPLE_LIGHT)
def nextcloudpw():
    return fit_b(circle(21, 36, 11, I) + circle(33, 27, 14, I) + circle(45, 37, 10, I) + rrect(15, 36, 36, 11, 5, I) + circle(32, 32, 4.4, H) + path("M30 34L34 34L35.6 43L28.4 43Z", H), 0.76)

@reg("com.glitchedpolygons.Argon2GUI", RED_DEEP)
def argon2gui():
    return fit_b(ink_stroke("M25 12L21 50M43 12L39 50M13 25H53M11 38H51", 4.8), 0.75)

@reg("com.glitchedpolygons.l8w8jwtgui", LIGHT_BLUE_DEEP)
def l8w8jwt():
    return fit_b(path("M10 18H54V26A5 5 0 0 0 54 38V46H10V38A5 5 0 0 0 10 26Z", I) + ink_stroke("M19 36C23 28 26 40 30 32C32 29 34 32 36 30", 2.8, H) + line(19, 26, 45, 26, H, 3), 0.7)

@reg("com.gooseberrydevelopment.pinepods", ORANGE_DEEP)
def pinepods():
    return fit_b(poly([(32, 8), (42, 22), (36, 22), (46, 36), (38, 36), (49, 48), (15, 48), (26, 36), (18, 36), (28, 22), (22, 22)], I, 2.5) + rrect(29, 48, 6, 7, 1.5, I), 0.73)

@reg("com.gopeed.Gopeed", PINK)
def gopeed():
    return fit_b(ink_stroke("M32 10V34M21 24L32 35L43 24", 5) + path("M10 40H54V50Q54 54 50 54H14Q10 54 10 50Z", I) + line(18, 47, 30, 47, H, 3), 0.6)

@reg("com.hannes_campidell.MelodicMix", DEEP_ORANGE_DARK)
def melodicmix():
    return fit_b(ink_stroke("M10 30C18 14 26 14 32 30C38 46 46 46 54 30", 5) + dim(ink_stroke("M10 30C18 46 26 46 32 30C38 14 46 14 54 30", 5), .55), 0.77)

@reg("com.her01n.BatteryInfo", INDIGO_DARK)
def batteryinfo():
    return fit_b(rrect(9, 19, 42, 24, 5, I) + rrect(52, 26, 4, 10, 1.5, I) + rrect(14, 24, 9, 14, 2, H) + rrect(25, 24, 9, 14, 2, H) + rrect(36, 24, 9, 14, 2, H, ' opacity=".35"'), 0.77)

@reg("com.holypangolin.Animatch", ORANGE_LIGHT)
def animatch():
    return fit_b(poly([(20, 15), (44, 15), (54, 28), (32, 52), (10, 28)], I, 2) + path("M10 28H54M24 15L32 28L40 15M32 28V52M32 28L20 15", "none", ' stroke="HOLE" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"'), 0.81)

@reg("com.hoptodesk.HopToDesk", DEEP_PURPLE)
def hoptodesk():
    return fit_b(rrect(9, 22, 36, 26, 4, I) + line(21, 52, 33, 52, I, 4) + ink_stroke("M20 17C28 5 44 8 49 20", 3.6) + poly([(52, 24), (44, 21), (50, 15)], I, 1.5) + poly([(25, 28), (25, 42), (29, 38), (33, 44), (36, 42), (32, 36), (37, 35)], H, 1), 0.69)

@reg("com.hostbuf.FinalShell", BLUE_GREY_DARK)
def finalshell():
    return fit_b(rrect(9, 12, 46, 38, 6, I) + line(9, 22, 55, 22, H, 2.6) + ink_stroke("M17 30L25 36L17 42", 3.6, H) + rrect(30, 40, 12, 4, 1, H), 0.67)

@reg("com.howlingmoonsoftware.CrayonBall", RED_LIGHT)
def crayonball():
    return fit_b(g(rrect(26, 20, 12, 36, 2, I) + poly([(26, 20), (32, 8), (38, 20)], I, 1.5) + rrect(26, 32, 12, 8, 0, H, ' opacity=".5"'), "rotate(35 32 32)") + circle(16, 44, 8, I), 0.64)

@reg("com.hperrin.StreamOverlay", TEAL_DEEP)
def streamoverlay():
    return fit_b(rrect(9, 13, 46, 32, 5, "none", ' stroke="INK" stroke-width="4"') + rrect(32, 28, 17, 11, 3, I) + circle(18, 22, 3.4, I) + line(24, 51, 40, 51, I, 4), 0.66)

@reg("com.hylianmodding.modloader64", PURPLE_DEEP)
def modloader64():
    return fit_b(path("M12 24H22C19 17 25 13 29 13C33 13 37 17 34 24H42V32C48 29 53 33 53 37C53 41 48 45 42 42V52H12Z", I), 0.64)

@reg("com.icanblink.blink", BLUE)
def blink():
    return fit_b(ink_stroke("M17 21C15 33 27 47 41 46L46 39L38 32L33 36C28 33 25 29 24 24L28 20L22 13Z", 4.4) + ink_stroke("M40 12A12 12 0 0 1 52 24M40 19A5 5 0 0 1 45 24", 3.6), 0.79)

@reg("com.iche2.fileshows", PINK_DEEP)
def fileshows():
    out = rrect(11, 12, 42, 36, 5, I)
    for y in (17, 28, 39):
        out += rrect(13.5, y, 3, 5, 1, H) + rrect(47.5, y, 3, 5, 1, H)
    return fit_b(out + poly([(27, 21), (27, 39), (40, 30)], H, 1.5), 0.74)

@reg("com.iche2.gai", INDIGO_LIGHT)
def gai():
    return fit_b(poly([(26, 8), (31, 24), (47, 29), (31, 34), (26, 50), (21, 34), (5, 29), (21, 24)], I, 1.5) + poly([(47, 8), (49, 14), (55, 16), (49, 18), (47, 24), (45, 18), (39, 16), (45, 14)], I, 1), 0.68)

@reg("com.identicalsoftware.anagramarama", BROWN_LIGHT)
def anagramarama():
    return fit_b(g(rrect(9, 22, 22, 22, 5, I) + ink_stroke("M14 38L20 26L26 38M16 34H24", 3, H), "rotate(-10 20 33)") + g(rrect(33, 20, 22, 22, 5, I) + ink_stroke("M40 38V26H46C51 26 51 32 46 32H40M46 32L50 38", 3, H), "rotate(9 44 31)"), 0.77)

@reg("com.indomitusgroup.indiaccounting", ORANGE_DEEP)
def indiaccounting():
    return fit_b(ink_stroke("M20 14H46M20 24H46M30 14C42 14 42 33 28 33H22L40 51", 5), 0.75)

@reg("com.indomitusgroup.indidatabase", BLUE_DARK)
def indidatabase():
    return fit_b(rrect(10, 13, 44, 38, 6, I) + line(10, 24, 54, 24, H, 2.4) + line(10, 36, 54, 36, H, 2.4) + line(28, 24, 28, 51, H, 2.4), 0.67)

@reg("com.infinipaint.infinipaint", RED_DEEP)
def infinipaint():
    return fit_b(ink_stroke("M32 30C26 18 12 18 12 30C12 42 26 42 32 30C38 18 52 18 52 30C52 42 38 42 32 30Z", 5.5) + poly([(44, 46), (50, 40), (55, 45), (49, 51)], I, 1), 0.67)

@reg("com.infochunk.OpenMadoola", PURPLE)
def openmadoola():
    out = ""
    for k in range(8):
        out += g('<ellipse cx="32" cy="19" rx="5" ry="10.5" fill="INK" opacity=".75"/>', f"rotate({k * 45} 32 30)")
    return fit_b(out + circle(32, 30, 4, H), 0.88)

@reg("com.inform7.IDE", ORANGE)
def inform7ide():
    return fit_b(path("M14 16Q14 12 18 12H46Q50 12 50 16V40Q50 44 46 44H30L20 54V44H18Q14 44 14 40Z", I) + circle(32, 20, 2.8, H) + rrect(30, 26, 4, 12, 1.5, H) + line(28.5, 26, 34, 26, H, 3), 0.71)

@reg("com.inochi2d.inochi-creator", BROWN_DARK)
def inochicreator():
    return fit_b(ring_d(32, 30, 19, 4.4) + circle(24, 26, 3.2, I) + circle(40, 26, 3.2, I) + ink_stroke("M23 36C27 44 37 44 41 36", 3.6), 0.89)

@reg("com.inochi2d.inochi-session", CYAN)
def inochisession():
    return fit_b(circle(32, 24, 16, I) + circle(32, 24, 8, H) + circle(32, 24, 3.4, I) + path("M23 44H41L44 52H20Z", I), 0.76)

@reg("com.invoiceninja.InvoiceNinja", PINK_LIGHT)
def invoiceninja():
    return fit_b(rrect(14, 9, 36, 46, 5, I) + line(21, 19, 43, 19, H, 3) + line(21, 27, 43, 27, H, 3) + rrect(21, 36, 22, 12, 3, H) + line(26, 42, 38, 42, I, 3), 0.65)

@reg("com.irealpro.irealpro", LIGHT_BLUE_DARK)
def irealpro():
    return fit_b(line(12, 12, 12, 48, I, 3) + line(33, 12, 33, 48, I, 3) + line(52, 12, 52, 48, I, 5) + ink_stroke("M17 40L23 20M24 40L30 20M38 40L44 20", 3.4), 0.64)

@reg("com.itextpdf.RUPS", BLUE_GREY_DEEP)
def rups():
    return fit_b(ring_d(27, 26, 15, 5) + line(38, 37, 52, 51, I, 6.5) + line(19, 21, 35, 21, I, 3) + line(19, 27, 31, 27, I, 3) + line(19, 33, 33, 33, I, 3), 0.58)

@reg("com.jeffser.Nocturne", INDIGO)
def nocturne():
    return fit_b(circle(24, 42, 8, I) + ink_stroke("M31 41V14C36 20 45 20 45 30", 4.6) + poly([(48, 9), (50, 15), (56, 17), (50, 19), (48, 25), (46, 19), (40, 17), (46, 15)], I, .6), 0.69)

@reg("com.jeffser.Pigment", RED)
def pigment():
    return fit_b(cut("M32 9C47 9 56 18 54 30C53 38 46 38 44 41C42 46 46 52 38 54C24 56 9 46 9 32C9 19 19 9 32 9Z" + cpath(22, 22, 4) + cpath(34, 18, 4) + cpath(43, 26, 4) + cpath(19, 35, 4), I), 0.76)

@reg("com.jetpackduba.Gitnuro", CYAN_DEEP)
def gitnuro():
    return fit_b(line(11, 36, 53, 36, I, 4) + ink_stroke("M24 36C28 24 34 20 46 20", 4) + circle(14, 36, 5, I) + circle(32, 36, 5, I) + circle(50, 36, 5, I) + circle(48, 20, 5.5, I) + circle(48, 20, 2, H), 0.77)
