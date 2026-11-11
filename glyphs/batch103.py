# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 103: vipsdisp to MakeThemFall."""
from lm import (
    AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_LIGHT, BROWN, BROWN_DEEP, BROWN_SOFT, circle, CYAN,
    CYAN_DARK, CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_PURPLE, DEEP_PURPLE_DARK,
    DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, f, GREY, GREY_DARK, GREY_DEEP, HOLE, INDIGO,
    INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_LIGHT, ORANGE_DEEP, path, PINK, PINK_DARK, PINK_DEEP, poly, pt, PURPLE,
    PURPLE_DARK, PURPLE_DEEP, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, TEAL, TEAL_DARK, TEAL_DEEP,
    TEAL_LIGHT, YELLOW_DARK,
)
from glyphs.kit import (
    arc_arrow, arrowhead, asterisk, bubble, cells, ell, ellring, fit, hashmark, hs, hx, ink_circle, ink_stroke, pet, pie, registry, ring_c, ink_rrect, rot, spiral, star5)

ICONS, SMALL, reg, _ = registry()


@reg("org.libvips.vipsdisp", BLUE)
def vipsdisp():
    out = ink_rrect(6, 10, 52, 44, 7) + ink_circle(21, 25, 5, HOLE) + poly([(10, 46), (26, 30), (35, 40), (42, 33), (54, 46)], HOLE, 2.5)
    return fit(out, 0.657, 32.0, 32.0)


@reg("org.lightning_matrix.Lightning", YELLOW_DARK)
def lightning():
    out = poly([(38, 4), (14, 36), (29, 36), (24, 60), (50, 26), (35, 26)], INK, 3)
    return fit(out, 0.61, 32.0, 32.0)


@reg("org.linuxshowplayer.LinuxShowPlayer", RED)
def linuxshowplayer():
    out = ink_rrect(22, 5, 20, 11, 3) + poly([(25, 20), (39, 20), (56, 58), (8, 58)], INK, 2) + ell(32, 52, 12, 3, HOLE)
    return fit(out, 0.565, 32.0, 32.0)


@reg("org.love2d.love2d", CYAN_DEEP)
def love2d():
    out = path("M32 56C10 40 6 28 6 20C6 11 13 6 20 6C25 6 29 9 32 14C35 9 39 6 44 6C51 6 58 11 58 20C58 28 54 40 32 56Z", INK)
    return fit(out, 0.675, 32.0, 31.0)


@reg("org.lvnauth.LVNAuth", ORANGE_DEEP)
def lvnauth():
    out = ink_rrect(14, 28, 36, 28, 7) + ink_stroke("M21 28V21Q21 9 32 9T43 21V28", 5.4) + path("M32 49C24 43 22 39 22 36C22 33 24 31 27 31C29 31 31 32 32 34C33 32 35 31 37 31C40 31 42 33 42 36C42 39 40 43 32 49Z", HOLE)
    return fit(out, 0.724, 32.0, 31.1)


@reg("org.lyx.LyX", PURPLE)
def lyx():
    out = ink_stroke("M10 10V50H30", 7.5) + ink_stroke("M36 18L56 50", 7) + ink_stroke("M56 18L36 50", 7)
    return fit(out, 0.601, 32.9, 30.0)


@reg("org.manasource.Mana", AMBER_DARK)
def mana():
    out = poly([(32, 5), (53, 26), (32, 59), (11, 26)], INK, 3) + ink_stroke("M11 26H53", 2.6, HOLE) + ink_stroke("M24 26L32 59L40 26", 2.6, HOLE) + ink_stroke("M32 5L24 26M32 5L40 26", 2.6, HOLE)
    return fit(out, 0.632, 32.0, 32.0)


@reg("org.mattdm.icebreaker", BROWN_DEEP)
def icebreaker():
    out = poly([(6, 36), (58, 36), (50, 50), (14, 50)], INK, 2) + ink_rrect(20, 22, 24, 14, 2) + ink_rrect(28, 11, 8, 12, 1.5) + ink_stroke("M4 58L12 54L20 58L28 54L36 58L44 54L52 58L60 54", 2.8) + ink_stroke("M24 29H40", 3, HOLE)
    return fit(out, 0.549, 32.0, 35.2)


@reg("org.mavlink.qgroundcontrol", INDIGO)
def qgroundcontrol():
    out = ""
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        out += ink_stroke(f"M32 32L{32 + dx * 17} {32 + dy * 17}", 4.4) + ring_c(32 + dx * 20, 32 + dy * 20, 8, 3.6)
    out += ink_rrect(23, 25, 18, 14, 5)
    return fit(out, 0.539, 32.0, 32.0)


@reg("org.mediaharbor.MediaHarbor", YELLOW_DARK)
def mediaharbor():
    out = ring_c(32, 12, 6, 4.2) + ink_stroke("M32 18V56", 5) + ink_stroke("M21 28H43", 5) + ink_stroke("M8 38C9 52 20 57 32 57C44 57 55 52 56 38", 5) + arrowhead(8, 40, 0, -1, 6) + arrowhead(56, 40, 0, -1, 6)
    return fit(out, 0.6, 32.0, 31.8)


@reg("org.megamek.MegaMek", BLUE_GREY)
def megamek():
    out = ink_rrect(17, 6, 30, 26, 6) + ink_rrect(21, 15, 22, 7, 2, HOLE) + ink_rrect(6, 14, 8, 24, 3) + ink_rrect(50, 14, 8, 24, 3) + ink_rrect(18, 34, 11, 22, 3) + ink_rrect(35, 34, 11, 22, 3)
    return fit(out, 0.686, 32.0, 31.0)


@reg("org.mersenne.mprime", LIGHT_BLUE_DEEP)
def mprime():
    out = ink_stroke("M10 50V14L32 36L54 14V50", 7.5)
    return fit(out, 0.638, 32.0, 32.0)


@reg("org.meshtastic.MeshtasticDesktop", AMBER_DEEP)
def meshtasticdesktop():
    pts = [pt(32, 33, 22, -90 + 72 * k) for k in range(5)]
    out = ""
    for k in range(5):
        a, b = pts[k], pts[(k + 2) % 5]
        out += ink_stroke(f"M{f(a[0])} {f(a[1])}L{f(b[0])} {f(b[1])}", 3.4)
    for x, y in pts:
        out += ink_circle(x, y, 6)
    return fit(out, 0.667, 32.0, 30.9)


@reg("org.meshtastic.meshtasticd", PINK)
def meshtasticd():
    out = ink_circle(32, 22, 5.5) + ink_stroke("M32 27V58", 5.4) + ink_stroke("M19 12Q13 22 19 32", 4) + ink_stroke("M45 12Q51 22 45 32", 4) + ink_stroke("M11 6Q1 22 11 38", 3.6) + ink_stroke("M53 6Q63 22 53 38", 3.6) + ink_stroke("M22 58H42", 5)
    return fit(out, 0.576, 32.0, 32.5)


@reg("org.metamuffin.hurrycurry.client", TEAL_DARK)
def client():
    out = ink_circle(21, 24, 10) + ink_circle(32, 18, 12) + ink_circle(43, 24, 10) + ink_rrect(16, 28, 32, 20, 4) + ink_rrect(16, 50, 32, 8, 3)
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.mfek.MFEKglif", DEEP_ORANGE_DEEP)
def mfekglif():
    out = ink_stroke("M8 52C14 12 50 12 56 52", 5) + ink_rrect(3, 47, 10, 10, 1.5) + ink_rrect(51, 47, 10, 10, 1.5) + ink_stroke("M13 38L24 14M51 38L40 14", 2.8) + ink_circle(24, 14, 4.6) + ink_circle(40, 14, 4.6)
    return fit(out, 0.557, 32.0, 33.2)


@reg("org.mintguide.WebAppReader", DEEP_PURPLE)
def webappreader():
    out = ink_rrect(6, 8, 52, 48, 7) + ink_stroke("M6 20H58", 3, HOLE) + ink_stroke("M14 30H50", 3.4, HOLE) + ink_stroke("M14 38H50", 3.4, HOLE) + ink_stroke("M14 46H36", 3.4, HOLE) + ink_circle(13, 14, 2.2, HOLE)
    return fit(out, 0.632, 32.0, 32.0)


@reg("org.mitmproxy.mitmproxy", LIGHT_BLUE_DEEP)
def mitmproxy():
    out = ink_stroke("M12 32H52", 4) + ink_circle(10, 32, 7) + ink_circle(54, 32, 7) + poly([(32, 16), (46, 32), (32, 48), (18, 32)], INK, 3) + ring_c(32, 32, 5, 3, HOLE)
    return fit(out, 0.621, 32.0, 32.0)


@reg("org.mosh.mosh", GREY)
def mosh():
    out = ink_stroke("M12 18L28 32L12 46", 6.4) + ink_stroke("M30 50Q35 43 40 50T50 50", 4.6)
    return fit(out, 0.72, 30.5, 35.2)


@reg("org.mpz_player.mpz", BLUE_DEEP)
def mpz():
    out = ring_c(32, 32, 24, 5.4) + poly([(26, 21), (26, 43), (45, 32)], INK, 3)
    return fit(out, 0.673, 32.0, 32.0)


@reg("org.msweet.htmldoc", YELLOW_DARK)
def htmldoc():
    out = path("M12 6H38L52 20V58H12Z", INK) + path("M38 6V20H52Z", HOLE) + ink_stroke("M26 29L19 38L26 47", 4, HOLE) + ink_stroke("M38 29L45 38L38 47", 4, HOLE)
    return fit(out, 0.628, 32.0, 32.0)


@reg("org.mume.MMapper", RED)
def mmapper():
    out = ink_rrect(6, 6, 18, 18, 4) + ink_rrect(40, 6, 18, 18, 4) + ink_rrect(23, 40, 18, 18, 4) + ink_stroke("M24 15H40", 4) + ink_stroke("M15 24V32H32V40", 4) + ink_stroke("M49 24V32H32", 4)
    return fit(out, 0.585, 32.0, 32.0)


@reg("org.munadi.Munadi", CYAN_DARK)
def munadi():
    out = poly([(8, 26), (22, 26), (48, 10), (48, 54), (22, 40), (8, 40)], INK, 3) + ink_rrect(12, 40, 9, 16, 2.5) + ink_stroke("M55 24Q60 32 55 40", 3.6)
    return fit(out, 0.673, 32.9, 32.2)


@reg("org.musacad.MusaCAD", ORANGE_DEEP)
def musacad():
    out = poly([(10, 56), (10, 8), (56, 56)], INK, 3) + poly([(20, 44), (20, 28), (36, 44)], HOLE, 2) + ink_stroke("M10 22H16M10 32H16M10 42H16", 2.6, HOLE)
    return fit(out, 0.591, 33.0, 32.0)


@reg("org.muttum.muttum", PURPLE)
def muttum():
    out = ink_stroke("M12 52V24", 6.4) + ink_stroke("M12 36Q12 22 24 22T36 36V52", 6.4) + ink_stroke("M36 36Q36 22 48 22T60 36V52", 6.4)
    return fit(out, 0.651, 36.0, 37.0)


@reg("org.nongnu.Xlog", BLUE_GREY)
def xlog():
    out = ink_rrect(6, 24, 42, 32, 6) + ink_stroke("M40 24L52 6", 4.4) + ink_circle(52, 6, 3) + ink_circle(19, 40, 6.5, HOLE) + ink_stroke("M32 33H42M32 40H42M32 47H42", 3, HOLE) + ink_stroke("M12 30H26", 2.6, HOLE)
    return fit(out, 0.59, 30.5, 29.5)


@reg("org.nongnu.enigma", BROWN)
def enigma():
    out = ""
    for x, y in ((6, 14), (24, 8), (42, 18)):
        out += ink_rrect(x, y, 16, 38, 4.5) + ink_rrect(x + 4, y + 8 + (x % 7), 8, 5, 2, HOLE)
    return fit(out, 0.612, 32.0, 32.0)


@reg("org.nongnu.gsequencer.gsequencer", INDIGO_DEEP)
def gsequencer():
    out = ""
    for y, x, w in ((10, 24, 18), (21, 34, 20), (32, 18, 16), (43, 40, 14)):
        out += ink_rrect(x, y, w, 7, 3)
    out += ink_rrect(6, 8, 12, 44, 3) + ink_stroke("M6 20H14M6 31H14M6 42H14", 2, HOLE)
    return fit(out, 0.657, 30.0, 30.0)


@reg("org.notepadng.Notepadng", YELLOW_DARK)
def notepadng():
    out = ink_rrect(12, 12, 40, 46, 6) + ink_rrect(18, 5, 5, 12, 2.5) + ink_rrect(29.5, 5, 5, 12, 2.5) + ink_rrect(41, 5, 5, 12, 2.5) + ink_stroke("M20 28H44M20 37H44M20 46H34", 3.4, HOLE)
    return fit(out, 0.667, 32.0, 31.5)


@reg("org.nsnam.NetAnim", BLUE_GREY)
def netanim():
    out = ink_circle(12, 46, 7) + ink_circle(52, 14, 7) + ink_stroke("M16 42Q28 38 34 28", 4) + ink_rrect(26, 38, 20, 18, 4) + poly([(32, 42), (32, 52), (41, 47)], HOLE)
    return fit(out, 0.611, 32.0, 31.5)


@reg("org.nuicpp.nui_sftp", LIGHT_BLUE_DARK)
def nui_sftp():
    out = path("M6 14H26L32 21H58V54H6Z", INK) + poly([(22, 29), (16, 36), (21, 36), (21, 47), (23, 47), (23, 36), (28, 36)], HOLE) + poly([(43, 47), (49, 40), (44, 40), (44, 29), (42, 29), (42, 40), (37, 40)], HOLE)
    return fit(out, 0.628, 32.0, 34.0)


@reg("org.nuspell.Nuspell", AMBER_DEEP)
def nuspell():
    out = ink_stroke("M8 52L22 12L36 52", 6) + ink_stroke("M13 38H31", 5) + ink_stroke("M44 38H60M44 50H60", 6)
    return fit(out, 0.574, 34.0, 32.0)


@reg("org.okstar.ok-msg", PINK)
def ok_msg():
    out = bubble(6, 8, 52, 38) + ink_stroke("M18 21H46M18 31H46M18 41H32", 5, HOLE)
    return fit(out, 0.641, 32.0, 31.9)


@reg("org.omegat.OmegaT", TEAL_DEEP)
def omegat():
    out = ink_stroke("M8 52H22C12 46 9 38 9 30C9 17 19 8 32 8C45 8 55 17 55 30C55 38 52 46 42 52H56", 6.4)
    return fit(out, 0.574, 32.0, 30.0)


@reg("org.openandroidinstaller.OpenAndroidInstaller", DEEP_ORANGE)
def openandroidinstaller():
    out = ink_rrect(16, 4, 32, 56, 7) + ink_rrect(21, 10, 22, 34, 2, HOLE) + ink_stroke("M32 16V30", 4.4) + poly([(24, 27), (40, 27), (32, 37)], INK, 1.5) + ink_circle(32, 51, 3, HOLE)
    return fit(out, 0.643, 32.0, 32.0)


@reg("org.opencpn.OpenCPN", DEEP_PURPLE_DEEP)
def opencpn():
    out = ring_c(32, 32, 23, 3.6) + poly([(32, 6), (39, 32), (32, 58), (25, 32)], INK, 1.5) + poly([(6, 32), (32, 25), (58, 32), (32, 39)], INK, 1.5) + ink_circle(32, 32, 4, HOLE)
    return fit(out, 0.673, 32.0, 32.0)


@reg("org.openfodder.OpenFodder", BROWN_SOFT)
def openfodder():
    out = path("M10 40Q10 12 32 12Q54 12 54 40Z", INK) + ink_rrect(5, 40, 54, 8, 4) + star5(32, 27, 8, HOLE)
    return fit(out, 0.663, 32.0, 30.0)


@reg("org.openhantek.OpenHantek6022", GREY)
def openhantek6022():
    out = ink_rrect(5, 8, 54, 38, 7) + ink_rrect(10, 13, 44, 28, 3, HOLE) + ink_stroke("M12 27Q18 15 24 27T36 27T48 27", 3.6) + ink_circle(16, 54, 3.6) + ink_circle(48, 54, 3.6) + ink_rrect(26, 51, 12, 6, 3)
    return fit(out, 0.608, 32.0, 32.8)


@reg("org.openjkdf2.OpenJKDF2", BLUE_DARK)
def openjkdf2():
    out = rot(ink_rrect(29, 3, 6, 36, 3) + ink_rrect(25, 40, 14, 16, 3) + ink_stroke("M25 46H39M25 51H39", 2.4, HOLE), 35)
    return fit(out, 0.726, 30.6, 30.6)


@reg("org.openmsx.openMSX", YELLOW_DARK)
def openmsx():
    out = ink_rrect(12, 4, 40, 54, 4) + ink_rrect(19, 10, 26, 20, 3, HOLE) + ink_rrect(19, 36, 26, 4, 1, HOLE) + ink_rrect(19, 44, 26, 4, 1, HOLE) + ink_rrect(26, 4, 12, 5, 1, HOLE)
    return fit(out, 0.641, 32.0, 31.0)


@reg("org.openomf.OpenOMF", RED)
def openomf():
    out = ink_rrect(12, 8, 34, 34, 14) + ink_rrect(18, 42, 22, 14, 3) + ell(44, 22, 7, 5) + ink_stroke("M18 24H32M18 31H32", 3, HOLE) + ink_stroke("M21 49H37", 3, HOLE)
    return fit(out, 0.75, 31.5, 32.0)


@reg("org.openscopeproject.TrguiNG", CYAN_DEEP)
def trguing():
    out = ink_stroke("M16 8V32Q16 50 32 50Q48 50 48 32V8", 11) + ink_stroke("M10.5 18H21.5M42.5 18H53.5", 3, HOLE)
    return fit(out, 0.643, 32.0, 29.0)


@reg("org.opensurge2d.OpenSurge", ORANGE_DEEP)
def opensurge():
    out = ring_c(38, 32, 17, 7) + ink_stroke("M4 22H14", 4.4) + ink_stroke("M2 32H11", 4.4) + ink_stroke("M4 42H14", 4.4)
    return fit(out, 0.613, 29.1, 32.0)


@reg("org.otfried.Ipe", PURPLE_DEEP)
def ipe():
    out = poly([(22, 5), (42, 5), (46, 28), (32, 60), (18, 28)], INK, 3) + ink_stroke("M32 33V58", 3, HOLE) + ink_circle(32, 28, 4.4, HOLE)
    return fit(out, 0.621, 32.0, 32.5)


@reg("org.pairinteraction.Pairinteraction", INDIGO_SOFT)
def pairinteraction():
    out = ring_c(21, 32, 14, 4.4) + ring_c(43, 32, 14, 4.4) + ink_circle(21, 32, 4.4) + ink_circle(43, 32, 4.4)
    return fit(out, 0.661, 32.0, 32.0)


@reg("org.pdfstitcher.pdfstitcher", BROWN)
def pdfstitcher():
    out = ink_rrect(6, 8, 22, 48, 4) + ink_rrect(36, 8, 22, 48, 4) + ink_stroke("M22 18H42M22 28H42M22 38H42M22 48H42", 3.6) + ink_stroke("M12 18H20M12 28H20M12 38H20M44 48H52", 2.4, HOLE)
    return fit(out, 0.609, 32.0, 32.0)


@reg("org.plomgrading.PlomClient", INDIGO_DARK)
def plomclient():
    out = ink_rrect(8, 6, 36, 50, 5) + ink_stroke("M15 18H37M15 27H37M15 36H28", 3, HOLE) + ink_circle(46, 44, 14, HOLE) + ink_circle(46, 44, 11) + circle(46, 44, 4, HOLE)
    return fit(out, 0.623, 32.5, 31.0)


@reg("org.praat.Praat", YELLOW_DARK)
def praat():
    out = ""
    for k, h in enumerate((10, 26, 40, 16, 32, 46, 22, 12, 28, 8)):
        out += ink_rrect(5 + 5.6 * k, 32 - h / 2, 3.6, h, 1.8)
    return fit(out, 0.667, 32.0, 32.0)


@reg("org.previewqt.PreviewQt", BLUE_GREY)
def previewqt():
    out = path("M4 32Q32 6 60 32Q32 58 4 32Z", INK) + ink_circle(32, 32, 13, HOLE) + ink_circle(32, 32, 7) + ink_circle(36, 28, 2.4, HOLE)
    return fit(out, 0.649, 32.0, 32.0)


@reg("org.profex_xrd.Profex", LIGHT_BLUE_DEEP)
def profex():
    out = ink_stroke("M6 54H58", 3.4) + ink_stroke("M10 54H16L19 38L22 54H28L32 18L36 54H42L46 30L50 54H56", 4)
    return fit(out, 0.617, 32.0, 36.0)


@reg("org.projecttick.MeshMC", AMBER_DEEP)
def meshmc():
    out = hx(32, 32, 26, -90, INK, 3) + ink_stroke("M32 32L9.5 19M32 32L54.5 19M32 32V58", 3, HOLE)
    return fit(out, 0.655, 32.0, 32.0)


@reg("org.pydpainter.PyDPainter", PINK_DEEP)
def pydpainter():
    out = ell(32, 33, 27, 23) + ink_circle(20, 28, 4.6, HOLE) + ink_circle(33, 20, 4.6, HOLE) + ink_circle(46, 27, 4.6, HOLE) + ink_circle(46, 41, 4.6, HOLE) + ell(25, 45, 7, 5, HOLE)
    return fit(out, 0.667, 32.0, 33.0)


@reg("org.quelea.Quelea", TEAL_LIGHT)
def quelea():
    out = ink_rrect(5, 6, 54, 36, 5) + ink_rrect(28.5, 12, 7, 24, 1.5, HOLE) + ink_rrect(21, 19, 22, 7, 1.5, HOLE) + ink_stroke("M32 42V54", 4) + ink_stroke("M18 57H46", 4.6)
    return fit(out, 0.573, 32.0, 32.6)


@reg("org.quetoo.Quetoo", DEEP_ORANGE)
def quetoo():
    out = ring_c(32, 32, 19, 4.6) + ink_stroke("M32 5V19M32 45V59M5 32H19M45 32H59", 4.6) + ink_circle(32, 32, 3.2)
    return fit(out, 0.615, 32.0, 32.0)


@reg("org.qxmledit.QXmlEdit", DEEP_PURPLE_DARK)
def qxmledit():
    out = ink_rrect(23, 4, 18, 12, 3) + ink_rrect(6, 40, 18, 14, 3) + ink_rrect(40, 40, 18, 14, 3) + ink_stroke("M32 16V30M15 30H49M15 30V40M49 30V40", 3.6) + ink_stroke("M12 47H18M46 47H52", 2.4, HOLE)
    return fit(out, 0.591, 32.0, 29.0)


@reg("org.raceintospace.Raceintospace", BLUE_GREY_LIGHT)
def raceintospace():
    out = path("M32 3C42 13 44 28 42 46H22C20 28 22 14 32 3Z", INK) + poly([(22, 34), (11, 52), (22, 48)], INK, 2) + poly([(42, 34), (53, 52), (42, 48)], INK, 2) + ink_circle(32, 22, 5, HOLE) + path("M26 50H38L32 62Z", INK)
    return fit(out, 0.615, 32.0, 32.5)


@reg("org.rayforge.rayforge", GREY)
def rayforge():
    out = ink_rrect(18, 4, 28, 16, 4) + poly([(24, 20), (40, 20), (32, 32)], INK, 2) + ink_stroke("M32 33V41", 3.4) + asterisk(32, 46, 7, 3.4) + ink_rrect(5, 57, 54, 5, 2.5)
    return fit(out, 0.531, 32.0, 33.0)


@reg("org.recoll.recoll", BLUE_DEEP)
def recoll():
    out = ring_c(26, 26, 18, 5.4) + ink_stroke("M39 39L57 57", 7) + ink_stroke("M16 20H36M16 27H36M16 34H28", 3, INK)
    return fit(out, 0.547, 32.9, 32.9)


@reg("org.regular_dev.biplanes_revival", YELLOW_DARK)
def biplanes_revival():
    out = ell(30, 32, 22, 7) + ink_rrect(14, 14, 32, 5, 2.5) + ink_rrect(14, 41, 32, 5, 2.5) + ink_stroke("M20 19V41M40 19V41", 2.4) + poly([(46, 30), (60, 20), (60, 44), (46, 34)], INK, 1.5) + ink_stroke("M7 20V44", 3.4) + ell(30, 30, 8, 3, HOLE)
    return fit(out, 0.649, 33.0, 30.0)


@reg("org.robocode.Robocode", RED_DEEP)
def robocode():
    out = ink_rrect(6, 34, 52, 17, 7) + ink_rrect(18, 20, 28, 16, 5) + ink_rrect(44, 24, 17, 5.5, 2.7) + ink_circle(15, 43, 4, HOLE) + ink_circle(32, 43, 4, HOLE) + ink_circle(49, 43, 4, HOLE)
    return fit(out, 0.655, 33.5, 35.5)


@reg("org.rolisteam.rolisteam", CYAN)
def rolisteam():
    out = rot(ink_rrect(10, 10, 44, 44, 10) + ink_circle(24, 24, 4.6, HOLE) + ink_circle(40, 24, 4.6, HOLE) + ink_circle(32, 32, 4.6, HOLE) + ink_circle(24, 40, 4.6, HOLE) + ink_circle(40, 40, 4.6, HOLE), 14, 32, 32)
    return fit(out, 0.735, 32.0, 32.0)


@reg("org.roojs.roobuilder", ORANGE_DEEP)
def roobuilder():
    out = ink_rrect(6, 8, 24, 14, 2) + ink_rrect(34, 8, 24, 14, 2) + ink_rrect(6, 25, 14, 14, 2) + ink_rrect(24, 25, 24, 14, 2) + ink_rrect(52, 25, 6, 14, 2) + ink_rrect(6, 42, 24, 14, 2) + ink_rrect(34, 42, 24, 14, 2)
    return fit(out, 0.594, 32.0, 32.0)


@reg("org.sasview.sasview", PURPLE_DARK)
def sasview():
    out = ink_stroke("M10 6V54H58", 4) + ink_stroke("M14 12C18 36 24 48 31 45C36 43 37 37 41 39C45 41 46 46 56 46", 5)
    return fit(out, 0.571, 34.0, 30.0)


@reg("org.scratchmark.Scratchmark", GREY_DEEP)
def scratchmark():
    out = ink_rrect(4, 12, 56, 40, 7) + ink_stroke("M12 42V22L20 32L28 22V42", 4.4, HOLE) + ink_stroke("M44 22V40M37 33L44 41L51 33", 4.4, HOLE)
    return fit(out, 0.643, 32.0, 32.0)


@reg("org.seekfast.SeekFast", BROWN)
def seekfast():
    out = ring_c(32, 32, 24, 4.6) + pie(32, 32, 24, -90, -5) + ink_circle(32, 32, 3.4, HOLE)
    return fit(out, 0.686, 32.0, 32.0)


@reg("org.selfprivacy.selfprivacy", INDIGO_DEEP)
def selfprivacy():
    out = ink_circle(20, 36, 13) + ink_circle(35, 28, 15) + ink_circle(48, 40, 10) + ink_rrect(10, 38, 46, 15, 7.5) + ink_rrect(25, 38, 14, 12, 2.5, HOLE) + ink_stroke("M28 38V35Q28 30 32 30T36 35V38", 2.8, HOLE)
    return fit(out, 0.706, 32.5, 33.0)


@reg("org.seul.crimson", YELLOW_DARK)
def crimson():
    out = poly([(32, 3), (38, 12), (38, 40), (26, 40), (26, 12)], INK, 2) + ink_rrect(15, 40, 34, 6, 3) + ink_rrect(28.5, 46, 7, 10, 2) + ink_circle(32, 59, 3.6)
    return fit(out, 0.595, 32.0, 32.2)


@reg("org.shadered.SHADERed", BLUE_GREY_DEEP)
def shadered():
    out = ink_stroke("M20 6Q10 6 10 15V25Q10 30 5 32Q10 34 10 39V49Q10 58 20 58", 4) + ink_stroke("M44 6Q54 6 54 15V25Q54 30 59 32Q54 34 54 39V49Q54 58 44 58", 4) + poly([(32, 17), (45, 41), (19, 41)], INK, 3)
    return fit(out, 0.621, 32.0, 32.0)


@reg("org.sigxcpu.Livi", LIGHT_BLUE_LIGHT)
def livi():
    out = ink_rrect(8, 24, 48, 30, 4) + rot(ink_rrect(8, 11, 48, 11, 2), -9, 8, 22) + rot(ink_stroke("M18 11L24 22M30 11L36 22M42 11L48 22", 3, HOLE), -9, 8, 22) + poly([(26, 31), (26, 47), (40, 39)], HOLE, 1.5)
    return fit(out, 0.613, 31.2, 29.0)


@reg("org.sil.dictionary-app-builder", AMBER_DEEP)
def dictionary_app_builder():
    out = ink_rrect(12, 6, 40, 50, 5) + ink_rrect(12, 6, 9, 50, 3) + ink_stroke("M26 42L34 16L42 42M29 33H39", 4, HOLE) + ink_stroke("M12 56H52", 1)
    return fit(out, 0.637, 32.0, 31.2)


@reg("org.sil.keyboard-app-builder", PINK_DARK)
def keyboard_app_builder():
    out = ink_rrect(5, 14, 54, 36, 7) + ink_rrect(11, 20, 12, 12, 2.5, HOLE) + ink_rrect(26, 20, 12, 12, 2.5, HOLE) + ink_rrect(41, 20, 12, 12, 2.5, HOLE) + ink_rrect(14, 37, 36, 6, 3, HOLE)
    return fit(out, 0.667, 32.0, 32.0)


@reg("org.sil.reading-app-builder", TEAL_DEEP)
def reading_app_builder():
    out = ring_c(18, 36, 11, 4.6) + ring_c(46, 36, 11, 4.6) + ink_stroke("M29 34Q32 29 35 34", 4) + ink_stroke("M7 34L10 16", 4) + ink_stroke("M57 34L54 16", 4)
    return fit(out, 0.661, 32.0, 31.6)


@reg("org.sil.scripture-app-builder", DEEP_ORANGE)
def scripture_app_builder():
    out = ink_rrect(14, 12, 36, 40, 3) + ink_rrect(8, 6, 48, 10, 5) + ink_rrect(8, 48, 48, 10, 5) + ink_stroke("M22 24H42M22 32H42M22 40H36", 3, HOLE)
    return fit(out, 0.616, 32.0, 32.0)


@reg("org.simondalvai.ball2box", DEEP_PURPLE_DEEP)
def ball2box():
    out = ink_rrect(8, 34, 48, 22, 3) + ink_stroke("M8 34L14 24H50L56 34", 5) + ink_circle(32, 15, 9) + ink_stroke("M26 45H38", 3, HOLE)
    return fit(out, 0.616, 32.0, 31.0)


@reg("org.simondalvai.pocket-broomball", GREY_DEEP)
def pocket_broomball():
    out = rot(ink_rrect(30, 4, 4.4, 36, 2.2) + poly([(21, 56), (43, 56), (46, 36), (18, 36)], INK, 2) + ink_stroke("M26 42V54M32 42V54M38 42V54", 2.2, HOLE), 28, 32, 30) + ink_circle(15, 53, 6)
    return fit(out, 0.662, 27.2, 33.0)


@reg("org.sinzala.silori", GREY_DEEP)
def silori():
    out = ""
    for k in range(5):
        out += pet(32, 32, 26, 9, -90 + 72 * k, 2.8)
    out += ink_circle(32, 32, 4, HOLE)
    return fit(out, 0.735, 32.0, 29.6)


@reg("org.siril.Siril", BLUE_LIGHT)
def siril():
    out = ink_circle(32, 32, 14) + rot(ellring(32, 32, 28, 9, 6.4, HOLE), -22) + rot(ellring(32, 32, 28, 9, 3.6), -22)
    return fit(out, 0.643, 32.8, 31.9)


@reg("org.skaven.ratic", YELLOW_DARK)
def ratic():
    out = ell(26, 38, 20, 12) + ink_circle(42, 29, 8) + poly([(46, 24), (60, 36), (46, 44)], INK, 3) + ink_circle(38, 20, 5.4) + ink_circle(38, 20, 2.6, HOLE) + ink_circle(50, 33, 1.8, HOLE) + ink_stroke("M7 38Q-1 50 12 54", 3.4)
    return fit(out, 0.608, 31.9, 35.1)


@reg("org.sonic3air.Sonic3AIR", RED_DARK)
def sonic3air():
    out = ink_circle(32, 32, 24) + spiral(32, 32, 3, 17, 2, 0, 4, HOLE)
    return fit(out, 0.75, 32.0, 32.0)


@reg("org.speedynote.SpeedyNote", CYAN_DEEP)
def speedynote():
    out = ink_stroke("M8 40C16 14 26 14 24 30C22 46 36 22 56 18", 5.4) + ink_stroke("M8 54H44", 4) + poly([(52, 8), (59, 14), (42, 34), (36, 30)], INK, 2)
    return fit(out, 0.58, 32.6, 31.5)


@reg("org.squey.Squey", ORANGE_DEEP)
def squey():
    out = ""
    ys = [(10, 40), (28, 14), (46, 44), (62, 26)]
    for x in (10, 25, 40, 55):
        out += ink_stroke(f"M{x} 8V56", 3)
    out += ink_stroke("M10 18L25 42L40 14L55 38", 3.6) + ink_stroke("M10 44L25 20L40 46L55 22", 3.6) + ink_circle(10, 18, 4) + ink_circle(55, 38, 4) + ink_circle(25, 20, 4) + ink_circle(40, 46, 4)
    return fit(out, 0.597, 32.5, 32.0)


@reg("org.squidowl.halloy", PURPLE_DEEP)
def halloy():
    out = bubble(6, 8, 52, 36) + hashmark(32, 26, 11, 4.4, HOLE)
    return fit(out, 0.654, 32.0, 30.9)


@reg("org.srb2.SRB2Kart-Saturn", PURPLE_SOFT)
def srb2kart_saturn():
    out = ink_rrect(14, 22, 34, 22, 8) + ink_rrect(6, 15, 11, 12, 3) + ink_rrect(6, 39, 11, 12, 3) + ink_rrect(45, 15, 11, 12, 3) + ink_rrect(45, 39, 11, 12, 3) + ink_rrect(40, 28, 20, 10, 5) + ink_circle(28, 33, 5, HOLE)
    return fit(out, 0.656, 33.0, 33.0)


@reg("org.srb2.SRB2Kart-galaxy_azerty", BROWN_DEEP)
def srb2kart_galaxy_azerty():
    out = ink_rrect(10, 6, 5, 52, 2) + ink_rrect(15, 8, 38, 28, 2)
    for r in range(3):
        for c in range(4):
            if (r + c) % 2 == 0:
                out += ink_rrect(15 + c * 9.5, 8 + r * 9.33, 9.5, 9.33, 0, HOLE)
    return fit(out, 0.623, 31.5, 32.0)


@reg("org.srb2.SRB2Persona", INDIGO_LIGHT)
def srb2persona():
    out = path("M8 14Q32 2 56 14C58 40 46 54 32 60C18 54 6 40 8 14Z", INK) + poly([(14, 24), (28, 28), (26, 34), (15, 32)], HOLE, 1.5) + poly([(50, 24), (36, 28), (38, 34), (49, 32)], HOLE, 1.5) + ink_stroke("M32 30V42", 3, HOLE) + ink_stroke("M24 48Q32 52 40 48", 3, HOLE)
    return fit(out, 0.66, 32.0, 34.0)


@reg("org.stochas.Stochas", YELLOW_DARK)
def stochas():
    out = path("M4 54C14 54 20 50 24 32C27 18 29 10 32 10C35 10 37 18 40 32C44 50 50 54 60 54Z", INK) + ink_stroke("M32 14V54", 2.6, HOLE) + ink_stroke("M18 54V48M46 54V48", 2.6, HOLE)
    return fit(out, 0.615, 32.0, 32.0)


@reg("org.sugarlabs.AbacusActivity", BLUE_GREY_DARK)
def abacusactivity():
    out = ink_rrect(6, 8, 52, 48, 6) + ink_rrect(11, 13, 42, 38, 2, HOLE)
    for x, ys in ((22, (22, 34, 43)), (32, (24, 36, 44)), (42, (20, 30, 41))):
        out += ink_stroke(f"M{x} 13V51", 2.6)
        for y in ys:
            out += ell(x, y, 4.6, 3.6)
    return fit(out, 0.625, 32.0, 32.0)


@reg("org.sugarlabs.Calculate", LIGHT_BLUE_DEEP)
def calculate():
    out = ink_rrect(14, 6, 36, 52, 6) + ink_rrect(19, 12, 26, 11, 2, HOLE)
    for r in range(3):
        for c in range(3):
            out += ink_rrect(19 + c * 9.5, 28 + r * 10, 7, 7, 1.8, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.sugarlabs.CellGame", AMBER_DEEP)
def cellgame():
    out = cells([(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)], 14, 17, 6, 6)
    return fit(out, 0.623, 30.0, 30.0)


@reg("org.sugarlabs.Chart", PINK_DEEP)
def chart():
    out = ink_stroke("M8 6V54H58", 4) + ink_rrect(16, 36, 10, 14, 1.5) + ink_rrect(30, 24, 10, 26, 1.5) + ink_rrect(44, 12, 10, 38, 1.5)
    return fit(out, 0.56, 33.0, 30.0)


@reg("org.sugarlabs.Chess", TEAL)
def chess():
    out = ink_circle(32, 15, 9.5) + ink_rrect(23, 26, 18, 5.5, 2.7) + path("M26 31H38Q39 42 45 50H19Q25 42 26 31Z", INK) + ink_rrect(13, 50, 38, 8, 4)
    return fit(out, 0.665, 32.0, 31.8)


@reg("org.sugarlabs.ColorDeducto", DEEP_ORANGE_DEEP)
def colordeducto():
    out = ink_circle(32, 26, 19) + ink_rrect(23, 42, 18, 5.5, 2.7) + ink_rrect(26, 49, 12, 6, 3) + ink_stroke("M25 29L28 22L32 29L36 22L39 29", 3, HOLE)
    return fit(out, 0.75, 32.0, 31.0)


@reg("org.sugarlabs.Dimensions", DEEP_PURPLE_LIGHT)
def dimensions():
    out = ink_stroke("M24 38V8", 4.4) + arrowhead(24, 14, 0, -1, 6.5) + ink_stroke("M24 38L6 52", 4.4) + arrowhead(10, 49, -.8, .6, 6.5) + ink_stroke("M24 38L56 38", 4.4) + arrowhead(50, 38, 1, 0, 6.5) + ink_circle(24, 38, 5)
    return fit(out, 0.578, 31.0, 30.0)


@reg("org.sugarlabs.Falabracman", PURPLE_SOFT)
def falabracman():
    out = pie(28, 32, 24, 38, 322) + ink_circle(33, 18, 3.4, HOLE) + ink_circle(54, 32, 4.4)
    return fit(out, 0.661, 31.2, 32.0)


@reg("org.sugarlabs.Finance", GREY_DARK)
def finance():
    out = ""
    for y in (46, 33, 20):
        out += ink_rrect(8, y, 48, 14, 7, INK, hs(2.6))
    out += ink_stroke("M26 27H38", 3, HOLE)
    return fit(out, 0.722, 32.0, 40.0)


@reg("org.sugarlabs.FlipSticks", BLUE_DEEP)
def flipsticks():
    out = rot(ink_rrect(6, 26, 52, 9.5, 4.7), 32, 32, 30) + rot(ink_rrect(6, 26, 52, 9.5, 4.7), -32, 32, 30) + arc_arrow(32, 30, 27, 205, 335, 3.4, 5)
    return fit(out, 0.649, 33.5, 24.0)


@reg("org.sugarlabs.FotoToon", YELLOW_DARK)
def fototoon():
    out = ink_rrect(5, 18, 54, 38, 8) + ink_rrect(21, 10, 22, 12, 4) + ink_circle(32, 37, 13, HOLE) + ink_circle(32, 37, 8) + ink_circle(50, 27, 2.4, HOLE)
    return fit(out, 0.637, 32.0, 33.0)


@reg("org.sugarlabs.FractionBounce", RED_DEEP)
def fractionbounce():
    out = ink_stroke("M14 32H50", 4.4) + ink_stroke("M31 8V22M27 12L31 8", 4) + ink_stroke("M24 40Q24 36 31 36T38 41L24 56H40", 4) + ink_circle(54, 12, 5)
    return fit(out, 0.635, 35.4, 32.0)


@reg("org.sugarlabs.ImplodeActivity", CYAN)
def implodeactivity():
    out = ""
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        out += ink_stroke(f"M{32 + dx * 24} {32 + dy * 24}L{32 + dx * 13} {32 + dy * 13}", 4.4) + arrowhead(32 + dx * 14, 32 + dy * 14, -dx * .707, -dy * .707, 7)
    out += ink_circle(32, 32, 5)
    return fit(out, 0.568, 32.0, 32.0)


@reg("org.sugarlabs.MakeThemFall", ORANGE_DEEP)
def makethemfall():
    out = ink_rrect(4, 52, 56, 8, 2) + ink_rrect(10, 38, 16, 14, 2) + ink_rrect(10, 24, 16, 14, 2) + rot(ink_rrect(30, 36, 16, 14, 2), 18, 38, 43) + rot(ink_rrect(38, 20, 16, 14, 2), 40, 46, 27)
    return fit(out, 0.596, 32.0, 38.6)
