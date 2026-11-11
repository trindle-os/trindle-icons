# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 86: Alacritty to lx-music-desktop."""
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP, BROWN_LIGHT,
    BROWN_SOFT, circle, CYAN, CYAN_DARK, CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, GREY_DARK, GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP,
    INDIGO_LIGHT, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, line, ORANGE, ORANGE_DARK,
    ORANGE_DEEP, path, PINK, PINK_DEEP, PINK_LIGHT, poly, pt, PURPLE, PURPLE_DARK, PURPLE_DEEP,
    PURPLE_LIGHT, RED, RED_DARK, RED_DEEP, RED_LIGHT, rrect, TEAL_DEEP, TEAL_LIGHT, TEAL_SOFT,
    YELLOW_DARK,
)
from glyphs.kit import bars, bubble_b, dim, ink_stroke, registry, ring_d

ICONS, SMALL, reg, _ = registry()


@reg("org.alacritty.Alacritty", DEEP_ORANGE_DEEP)
def alacritty():
    return ink_stroke("M17 20L29 30L17 40", 4.5) + line(33, 42, 47, 42, INK, 4.5)


@reg("rs.graphite.Graphite", BLUE_GREY)
def graphite():
    pencil = poly([(40, 13), (48, 21), (24, 45), (14, 47), (16, 37)], INK, 2)
    return pencil + line(35, 18, 43, 26, HOLE, 2.5)


@reg("dev.dynamic.normcap", BLUE)
def normcap():
    br = ink_stroke("M14 24V15H23M41 15H50V24M50 38V47H41M23 47H14V38", 3.5)
    return br + line(23, 26, 41, 26, INK, 3.5) + line(23, 32, 41, 32, INK, 3.5) + line(23, 38, 34, 38, INK, 3.5)


@reg("dev.geopjr.Tuba", DEEP_PURPLE)
def tuba():
    return (ink_stroke("M14 24H26C31 24 33 28 33 33", 4.5) + circle(38, 36, 11, INK) + circle(38, 36, 5, HOLE)
            + line(14, 24, 14, 20, INK, 4.5))


@reg("io.github.mrvladus.List", DEEP_PURPLE_SOFT)
def errands():
    out = ""
    for k, y in enumerate((20, 31, 42)):
        out += circle(19, y, 3, INK) if k < 2 else ring_d(19, y, 3.2, 2.6)
        out += line(29, y, 49, y, INK, 4)
    return out


@reg("org.dissent.Dissent", INDIGO)
def dissent():
    return bubble_b(32, 27, 34, 24) + circle(25, 27, 3, HOLE) + circle(32, 27, 3, HOLE) + circle(39, 27, 3, HOLE)


@reg("de.haeckerfelix.Packet", CYAN)
def packet():
    box = poly([(14, 26), (50, 26), (46, 46), (18, 46)], INK, 3)
    arrow = ink_stroke("M32 36V10M23 19L32 10L41 19", 4.5)
    return arrow + box


@reg("re.sonny.Iotas", ORANGE)
def iotas():
    return (rrect(17, 13, 30, 34, 5, INK) + line(23, 23, 41, 23, HOLE, 3.5) + line(23, 30, 41, 30, HOLE, 3.5)
            + line(23, 37, 33, 37, HOLE, 3.5))


@reg("com.github.finefindus.Hieroglyphic", BROWN)
def hieroglyphic():
    eye = path("M12 30C20 17 44 17 52 30C44 43 20 43 12 30Z", INK)
    return eye + circle(32, 30, 8, HOLE) + circle(32, 30, 3.5, INK) + line(32, 12, 32, 17, INK, 3.5)


@reg("ai.loomfy.Loomfy", PINK)
def loomfy():
    out = ""
    for r in range(3):
        for c in range(3):
            x, y = 15 + c * 12, 14 + r * 12
            if (r + c) % 2 == 0:
                out += rrect(x, y, 10, 10, 3, INK)
            else:
                out += rrect(x, y, 10, 10, 3, INK, ' opacity=".45"')
    return out


@reg("app.cantara.Cantara", PURPLE)
def cantara():
    return (path("M26 14L48 10V36", "none", ' stroke="INK" stroke-width="4.5" stroke-linejoin="round"')
            + circle(21, 40, 7, INK) + circle(43, 36, 7, INK) + line(26, 14, 26, 40, INK, 4.5))


@reg("app.crankboy.crankboy-manager", AMBER)
def crankboy():
    body = rrect(14, 16, 28, 32, 6, INK) + rrect(18, 20, 20, 13, 2.5, HOLE)
    pad = line(21, 41, 29, 41, HOLE, 3.2) + line(25, 37, 25, 45, HOLE, 3.2) + circle(35, 41, 2.4, HOLE)
    crank = line(42, 28, 52, 28, INK, 4) + circle(52, 28, 3.5, INK) + line(52, 28, 52, 20, INK, 4)
    return body + pad + crank


@reg("app.curocalc.calculator", TEAL_DEEP)
def calculator():
    out = rrect(16, 11, 32, 38, 6, INK) + rrect(21, 16, 22, 8, 2, HOLE)
    for r in range(2):
        for c in range(3):
            out += rrect(21 + c * 8, 28 + r * 8, 6, 5, 1.5, HOLE)
    return out


@reg("app.devsuite.Schemes", RED_DEEP)
def schemes():
    return (rrect(13, 17, 12, 26, 5, INK, ' opacity=".5"') + rrect(26, 13, 12, 34, 5, INK)
            + rrect(39, 17, 12, 26, 5, INK, ' opacity=".75"'))


@reg("app.drey.Biblioteca", LIGHT_BLUE_DEEP)
def biblioteca():
    return (path("M32 18C26 13 18 13 12 15V45C18 43 26 43 32 48C38 43 46 43 52 45V15C46 13 38 13 32 18Z", INK)
            + line(32, 20, 32, 46, HOLE, 2.6))


@reg("app.drey.Blurble", TEAL_SOFT)
def blurble():
    return (rrect(13, 13, 17, 17, 4, INK) + rrect(34, 13, 17, 17, 4, INK, ' opacity=".5"')
            + rrect(13, 34, 17, 17, 4, INK, ' opacity=".5"') + rrect(34, 34, 17, 17, 4, INK)
            + line(38, 42.5, 47, 42.5, HOLE, 3) + line(21.5, 18, 21.5, 26, HOLE, 3))


@reg("app.drey.Damask", PURPLE_DEEP)
def damask():
    d = lambda cx, cy, r, c, o=1: dim(poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], c, 1.5), o)
    return d(32, 30, 17, INK) + d(32, 30, 8, HOLE) + d(15, 13, 6, INK) + d(49, 13, 6, INK) + d(15, 47, 6, INK) + d(49, 47, 6, INK)


@reg("app.drey.Elastic", BROWN_SOFT)
def elastic():
    return ink_stroke("M32 11V17L18 22L46 29L18 36L46 43V49", 4.2)


@reg("app.drey.Haystack", YELLOW_DARK)
def haystack():
    return ring_d(28, 26, 12, 5) + line(37, 35, 48, 46, INK, 6)


@reg("app.drey.KeyRack", AMBER_DEEP)
def keyrack():
    return ring_d(22, 30, 9, 5) + line(31, 30, 49, 30, INK, 5) + line(42, 30, 42, 39, INK, 5) + line(49, 30, 49, 37, INK, 5)


@reg("app.drey.MultiplicationPuzzle", BLUE_DEEP)
def multiplication():
    return ink_stroke("M18 16L46 44M46 16L18 44", 7) + circle(32, 30, 5, HOLE)


@reg("app.eduroam.geteduroam", INDIGO_DEEP)
def geteduroam():
    return (ink_stroke("M13 26C24 15 40 15 51 26M20 33C27 27 37 27 44 33", 4.6) + circle(32, 41, 4.5, INK))


@reg("app.feeddeck.feeddeck", DEEP_ORANGE_LIGHT)
def feeddeck():
    return circle(19, 41, 4.5, INK) + ink_stroke("M15 27C26 27 33 34 33 45M15 14C34 14 46 26 46 45", 5)


@reg("app.fotema.Fotema", TEAL_LIGHT)
def fotema():
    return (rrect(12, 14, 40, 32, 6, INK) + circle(25, 24, 4, HOLE)
            + poly([(14, 44), (28, 29), (36, 38), (42, 32), (50, 44)], HOLE, 1.5))


@reg("app.freelens.Freelens", DEEP_PURPLE_LIGHT)
def freelens():
    return ring_d(32, 30, 16, 5) + poly([pt(32, 30, 7.5, 60 * k - 90) for k in range(6)], INK, 2)


@reg("app.getclipboard.Clipboard", BLUE_GREY_DEEP)
def clipboard():
    return (rrect(16, 15, 32, 34, 5, INK) + rrect(24, 10, 16, 9, 3, INK) + rrect(26, 12.5, 12, 4, 1.5, HOLE)
            + line(23, 28, 41, 28, HOLE, 3.4) + line(23, 36, 37, 36, HOLE, 3.4))


@reg("app.getspace.Space", DEEP_PURPLE_DARK)
def space():
    return circle(32, 30, 12, INK) + ink_stroke("M9 39C12 28 42 12 55 21", 5.5, HOLE) + ink_stroke("M9 39C12 28 42 12 55 21", 2.6, INK)


@reg("app.gmtp.gMTP", CYAN_DEEP)
def gmtp():
    return (rrect(21, 11, 22, 38, 5, INK) + rrect(25, 16, 14, 24, 1.5, HOLE) + circle(32, 44.5, 1.8, HOLE)
            + ink_stroke("M10 26H17M13.5 22.5L10 26L13.5 29.5", 2.8) + ink_stroke("M54 34H47M50.5 30.5L54 34L50.5 37.5", 2.8))


@reg("app.go2tv.go2tv", PINK_DEEP)
def go2tv():
    return (rrect(12, 16, 40, 27, 5, INK) + line(24, 48, 40, 48, INK, 4.5)
            + ink_stroke("M19 36C19 33 22 30 25 30M19 41C19 34 26 27 33 27", 3, HOLE) + circle(20, 40, 1.8, HOLE))


@reg("app.inkdrop.Inkdrop", INDIGO_LIGHT)
def inkdrop():
    return path("M32 11C32 11 16 28 16 36A16 16 0 0 0 48 36C48 28 32 11 32 11Z", INK) + ink_stroke("M24 37A8 8 0 0 0 31 44", 3.2, HOLE)


@reg("app.katvan.Katvan", BROWN_LIGHT)
def katvan():
    face = circle(32, 34, 15, INK) + poly([(17, 24), (17, 11), (28, 19)], INK, 3) + poly([(47, 24), (47, 11), (36, 19)], INK, 3)
    return face + circle(26, 33, 2.6, HOLE) + circle(38, 33, 2.6, HOLE) + poly([(29.5, 38), (34.5, 38), (32, 41)], HOLE, 1)


@reg("app.kreya.Kreya", PINK_LIGHT)
def kreya():
    return ink_stroke("M14 22H46M38 14L47 22L38 30", 4.2) + ink_stroke("M50 40H18M26 32L17 40L26 48", 4.2)


@reg("app.legcord.Legcord", BLUE_LIGHT)
def legcord():
    return (path("M14 22C14 16 18 13 24 13H40C46 13 50 16 50 22V38C50 44 46 47 40 47H24C18 47 14 44 14 38Z", INK)
            + circle(25, 29, 4.2, HOLE) + circle(39, 29, 4.2, HOLE) + ink_stroke("M26 38C29 41 35 41 38 38", 3, HOLE))


@reg("app.lepse.Lepse", AMBER_DARK)
def lepse():
    return ink_stroke("M20 13V45H46", 6) + circle(40, 22, 4.5, INK)


@reg("app.lith.Lith", LIGHT_BLUE_LIGHT)
def lith():
    top = poly([(32, 11), (48, 25), (16, 25)], INK, 2)
    return top + poly([(16, 29), (48, 29), (32, 49)], INK, 2)


@reg("app.moosync.moosync", PURPLE_LIGHT)
def moosync():
    return (ink_stroke("M15 36V30C15 20 22 14 32 14C42 14 49 20 49 30V36", 4.5)
            + rrect(12, 32, 9, 15, 4, INK) + rrect(43, 32, 9, 15, 4, INK))


@reg("app.nestful.Nestful", BROWN_DEEP)
def nestful():
    eggs = circle(24, 29, 6.5, INK) + circle(36, 29, 6.5, INK) + circle(30, 22, 6.5, INK)
    nest = path("M11 34C11 46 21 50 32 50C43 50 53 46 53 34Z", INK)
    return eggs + nest + ink_stroke("M17 41C26 44 38 44 47 41", 2.8, HOLE)


@reg("app.openbubbles.OpenBubbles", ORANGE_DARK)
def openbubbles():
    return circle(24, 33, 12, INK) + circle(40, 23, 10, INK, ' opacity=".6"') + circle(40, 23, 4, HOLE) + circle(24, 33, 5, HOLE)


@reg("app.opencomic.OpenComic", RED_LIGHT)
def opencomic():
    return rrect(13, 13, 20, 15, 3, INK) + rrect(36, 13, 15, 15, 3, INK) + rrect(13, 32, 15, 15, 3, INK) + rrect(31, 32, 20, 15, 3, INK)


@reg("app.prelora.Prelora", DEEP_PURPLE_DEEP)
def prelora():
    return ink_stroke("M21 46V14H34C42 14 45 18 45 24C45 30 42 34 34 34H21", 6)


@reg("app.shaz.pianocheetah", INDIGO_DARK)
def pianocheetah():
    out = rrect(12, 14, 40, 32, 4, INK)
    for x in (22, 32, 42):
        out += line(x, 30, x, 46, HOLE, 2.4)
    for x in (22, 32, 42):
        out += rrect(x - 3, 14, 6, 18, 1.5, HOLE, ' opacity="1"')
    return out


@reg("app.shizumu.Shizumu", CYAN_DARK)
def shizumu():
    return ink_stroke("M12 22C18 16 24 28 32 22C40 16 46 28 52 22", 4.2) + ink_stroke("M12 33C18 27 24 39 32 33C40 27 46 39 52 33", 4.2) + ink_stroke("M12 44C18 38 24 50 32 44C40 38 46 50 52 44", 4.2)


@reg("app.tintero.Tintero", BLUE_DARK)
def tintero():
    pot = rrect(14, 32, 26, 16, 5, INK) + rrect(20, 26, 14, 8, 2, INK)
    quill = ink_stroke("M30 26L48 10", 4) + path("M48 10C54 12 54 20 46 28C42 32 38 32 36 30C38 24 42 16 48 10Z", INK)
    return pot + quill


@reg("app.towdow.TowDow", ORANGE_DEEP)
def towdow():
    return rrect(14, 14, 36, 36, 9, INK) + ink_stroke("M23 27H41M23 37H34", 4.6, HOLE)


@reg("app.tuneline.Tuneline", PINK)
def tuneline():
    return bars((14, 22, 30, 38, 46), 40, 4, (10, 22, 32, 18, 8)) + ink_stroke("M14 14H50", 3.5)


@reg("app.vger.voyager", GREY_DEEP)
def voyager():
    body = path("M32 9C40 15 42 28 40 40H24C22 28 24 15 32 9Z", INK) + circle(32, 26, 4.5, HOLE)
    fins = poly([(24, 32), (15, 44), (24, 42)], INK, 2) + poly([(40, 32), (49, 44), (40, 42)], INK, 2)
    return body + fins + poly([(28, 45), (36, 45), (32, 53)], INK, 1.5)


@reg("app.ywallet.Ywallet", CYAN_DEEP)
def ywallet():
    return rrect(12, 17, 40, 30, 7, INK) + rrect(34, 27, 18, 10, 5, HOLE) + circle(40, 32, 2.6, INK)


@reg("ar.com.pilas_engine.App", PURPLE_DARK)
def pilas():
    return (rrect(11, 22, 42, 22, 11, INK) + line(21, 28, 21, 38, HOLE, 3.4) + line(16, 33, 26, 33, HOLE, 3.4)
            + circle(40, 29.5, 2.6, HOLE) + circle(46, 35, 2.6, HOLE))


@reg("ar.com.softwareperonista.Rockarrolla", RED)
def rockarrolla():
    body = circle(24, 38, 10, INK) + circle(30, 29, 6.5, INK)
    neck = line(32, 26, 48, 10, INK, 4.5) + rrect(44, 8, 8, 7, 2, INK)
    return body + neck + circle(24, 38, 3.5, HOLE)


@reg("ar.net.covacha.spelloff", BLUE_GREY_LIGHT)
def spelloff():
    return ink_stroke("M16 44L28 14L40 44M20 35H36", 5) + line(14, 48, 50, 14, HOLE, 6) + line(14, 48, 50, 14, INK, 3)


@reg("art.darkly.Darkly", BLUE_GREY_DARK)
def darkly():
    return ring_d(32, 30, 16, 4) + path("M32 14A16 16 0 0 1 32 46Z", INK)


@reg("art.fatdawlf.Piccolo", DEEP_ORANGE)
def piccolo():
    out = ""
    for r, row in enumerate(("0110", "1111", "0110", "1001")):
        for c, v in enumerate(row):
            if v == "1":
                out += rrect(15 + c * 9, 15 + r * 9, 8, 8, 1.5, INK)
    return out


@reg("art.taunoerik.tauno-monitor", CYAN)
def taunomonitor():
    return rrect(11, 14, 42, 30, 5, INK) + ink_stroke("M16 30H23L27 21L33 37L37 28H48", 3.2, HOLE) + line(24, 50, 40, 50, INK, 4)


@reg("art.taunoerik.tauno-serial-plotter", ORANGE)
def taunoplotter():
    return ink_stroke("M14 12V48H52", 3.6) + ink_stroke("M20 38L28 26L35 34L48 17", 4)


@reg("as.may.moat", DEEP_PURPLE_SOFT)
def moat():
    castle = poly([(17, 40), (17, 17), (23, 17), (23, 22), (28, 22), (28, 17), (36, 17), (36, 22), (41, 22), (41, 17), (47, 17), (47, 40)], INK, 1.5)
    return castle + rrect(28, 28, 8, 12, 4, HOLE) + ink_stroke("M12 47C18 43 22 51 28 47C34 43 38 51 44 47C48 45 50 46 52 47", 3.4)


@reg("at.ssh_mitm.server", GREY_DARK)
def sshserver():
    out = ""
    for y in (13, 26, 39):
        out += rrect(14, y, 36, 10, 3, INK) + circle(21, y + 5, 1.9, HOLE) + line(28, y + 5, 43, y + 5, HOLE, 2.6)
    return out


@reg("au.stevetech.yafi", LIGHT_BLUE_DEEP)
def yafi():
    return rrect(16, 14, 32, 22, 3.5, INK) + rrect(20, 18, 24, 14, 1.5, HOLE) + path("M9 41H55L52 46H12Z", INK)


@reg("br.app.pw3270.terminal", PURPLE)
def pw3270():
    return rrect(12, 14, 40, 30, 5, INK) + rrect(18, 31, 8, 6, 1, HOLE) + line(18, 23, 40, 23, HOLE, 3.2) + line(24, 50, 40, 50, INK, 4.5)


@reg("br.com.eduk.school", PINK)
def school():
    return (poly([(32, 14), (54, 25), (32, 36), (10, 25)], INK, 2.5) + path("M20 32V41C26 47 38 47 44 41V32L32 38Z", INK)
            + line(52, 27, 52, 40, INK, 3))


@reg("br.eng.silas.qpdftools", RED)
def qpdftools():
    return (rrect(18, 11, 28, 38, 4, INK) + line(24, 21, 40, 21, HOLE, 3.4) + line(24, 28, 40, 28, HOLE, 3.4)
            + ink_stroke("M24 38L29 33L35 41L40 35", 3, HOLE))


def _tax(name, tile, year, gain):
    def drawing():
        out = rrect(16, 11, 32, 33, 5, INK)
        if gain:
            out += ink_stroke("M22 36L29 28L34 33L42 22M36 22H42V28", 3.4, HOLE)
        else:
            out += circle(25, 21, 3.2, HOLE) + circle(39, 31, 3.2, HOLE) + line(40, 19, 24, 33, HOLE, 3.4)
        n = year - 2020
        for k in range(n):
            out += circle(32 + (k - (n - 1) / 2) * 7, 50, 2.6, INK)
        return out
    ICONS[name] = (drawing, tile)


for _n, _t, _y, _g in (("gcap2024", TEAL_LIGHT, 2024, True), ("gcap2025", TEAL_DEEP, 2025, True),
                       ("gcap2026", TEAL_SOFT, 2026, True), ("irpf2022", DEEP_PURPLE, 2022, False),
                       ("irpf2023", DEEP_ORANGE_DEEP, 2023, False), ("irpf2024", INDIGO, 2024, False),
                       ("irpf2025", PINK_DEEP, 2025, False), ("irpf2026", BLUE_DEEP, 2026, False)):
    _tax(f"br.gov.fazenda.receita.{_n}", _t, _y, _g)


@reg("ca.uwaterloo.Raven", BROWN_DARK)
def raven():
    body = path("M10 36C10 28 18 24 26 24C32 24 34 18 40 15C46 12 50 14 53 18L46 21C46 28 42 33 36 36L24 38L12 47L14 38Z", INK)
    return body + poly([(26, 38), (22, 52), (31, 40)], INK, 2.5) + circle(43, 19, 1.8, HOLE)


@reg("ca.vlacroix.Tally", BLUE)
def tally():
    return ink_stroke("M16 15V45M26 15V45M36 15V45M46 15V45", 4.5) + line(11, 40, 51, 20, INK, 4.5)


@reg("ca.vtrlx.Parchment", BROWN_SOFT)
def parchment():
    sheet = path("M20 14H46V42C46 46 43 48 40 48H18C22 46 22 42 22 38V16C22 15 21 14 20 14Z", INK)
    curl = path("M20 14C14 14 14 22 20 22H22", "none", ' stroke="INK" stroke-width="3.5" stroke-linecap="round"')
    return sheet + curl + line(28, 24, 40, 24, HOLE, 3) + line(28, 31, 40, 31, HOLE, 3)


@reg("ca.vtrlx.Telepipe", LIGHT_BLUE)
def telepipe():
    return poly([(12, 30), (52, 12), (42, 50), (31, 38), (24, 44), (24, 33)], INK, 2) + line(24, 33, 52, 12, HOLE, 2.4)


@reg("ca.wiilink.Patcher", DEEP_PURPLE_LIGHT)
def patcher():
    band = rrect(10, 24, 44, 16, 8, INK)
    return f'<g transform="rotate(-40 32 32)">{band + rrect(24, 24, 16, 16, 2, HOLE, " opacity=\".4\"") + circle(29, 30, 1.6, INK) + circle(35, 30, 1.6, INK) + circle(29, 35, 1.6, INK) + circle(35, 35, 1.6, INK)}</g>'


@reg("cafe.avery.Delfin", CYAN_DEEP)
def delfin():
    return path("M12 40C12 26 20 15 30 11C28 20 34 25 46 28C46 38 40 46 30 46C22 46 15 44 12 40Z", INK) + ink_stroke("M10 52C16 48 22 54 28 50C34 46 40 54 46 50", 3, INK)


@reg("camp.nook.nookdesktop", BROWN_LIGHT)
def nook():
    return path("M16 48V28C16 18 23 12 32 12C41 12 48 18 48 28V48Z", INK) + path("M25 48V33C25 29 28 27 32 27C36 27 39 29 39 33V48Z", HOLE)


@reg("cc.craftos_pc.CraftOS-PC", ORANGE_DARK)
def craftos():
    return rrect(11, 13, 42, 31, 5, INK) + ink_stroke("M18 22L25 28L18 34", 3.6, HOLE) + line(30, 35, 41, 35, HOLE, 3.6) + rrect(23, 47, 18, 4, 2, INK)


@reg("cc.craftos_pc.CraftOS-PC-Accelerated", BLUE_GREY)
def craftosacc():
    bolt = poly([(36, 10), (22, 32), (31, 32), (27, 50), (43, 26), (33, 26)], INK, 2)
    return bolt


@reg("cc.cubocore.CoreGarage", LIGHT_BLUE_DEEP)
def coregarage():
    out = poly([(10, 26), (32, 11), (54, 26), (54, 49), (10, 49)], INK, 2)
    for y in (31, 37, 43):
        out += line(17, y, 47, y, HOLE, 2.8)
    return out


@reg("cc.nift.nsm", DEEP_ORANGE_LIGHT)
def nsm():
    return ink_stroke("M10 32H20L25 18L33 44L39 26L43 32H54", 4.4)


@reg("cc.spek.Spek", PURPLE_DEEP)
def spek():
    return bars((13, 20, 27, 34, 41, 48), 46, 5, (12, 26, 34, 20, 30, 10))


@reg("cern.root.ROOT", INDIGO_DEEP)
def root():
    return bars((14, 23, 32, 41), 46, 8, (12, 24, 32, 16)) + ink_stroke("M12 28C22 12 34 12 52 24", 3.2, HOLE) + line(12, 49, 52, 49, INK, 3)


@reg("ch.bailu.aat", AMBER_DEEP)
def aat():
    return path("M32 11C24 11 19 17 19 24C19 33 32 47 32 47C32 47 45 33 45 24C45 17 40 11 32 11Z", INK) + circle(32, 24, 5, HOLE) + ink_stroke("M12 52C20 46 26 54 36 49", 3)


@reg("ch.bailu.gtk_meteo", LIGHT_BLUE_LIGHT)
def meteo():
    return circle(41, 22, 8, INK) + circle(24, 36, 8, INK) + circle(35, 33, 10, INK) + circle(44, 38, 7, INK) + rrect(24, 36, 20, 9, 4, INK) + line(41, 10, 41, 11, INK, 3)


@reg("ch.dragondreams.deigde", RED_DARK)
def deigde():
    return poly([pt(32, 30, 19, 60 * k - 90) for k in range(6)], INK, 2.5) + poly([(32, 20), (42, 30), (32, 40), (22, 30)], HOLE, 1)


@reg("ch.dragondreams.delauncher", INDIGO_DARK)
def delauncher():
    return rrect(13, 13, 14, 14, 4, INK) + rrect(13, 33, 14, 14, 4, INK) + rrect(33, 13, 14, 14, 4, INK) + poly([(34, 34), (50, 40), (34, 48)], INK, 3)


@reg("ch.imatt.ClipQR", BLUE_GREY_DEEP)
def clipqr():
    out = ""
    for x, y in ((13, 13), (37, 13), (13, 37)):
        out += rrect(x, y, 14, 14, 3, INK) + rrect(x + 4, y + 4, 6, 6, 1, HOLE)
    return out + rrect(35, 35, 6, 6, 1.5, INK) + rrect(44, 44, 6, 6, 1.5, INK) + rrect(44, 35, 6, 6, 1.5, INK) + rrect(35, 44, 6, 6, 1.5, INK)


@reg("ch.threema.threema-web-desktop", GREY_DARK)
def threema():
    return bubble_b(32, 27, 38, 26) + rrect(26, 26, 12, 9, 2, HOLE) + ink_stroke("M28.5 26V22C28.5 18 35.5 18 35.5 22V26", 2.6, HOLE)


@reg("ch.tigerjython.TigerJython2", DEEP_ORANGE)
def tiger():
    face = circle(32, 31, 18, INK) + circle(18, 17, 5, INK) + circle(46, 17, 5, INK)
    stripes = line(32, 14, 32, 21, HOLE, 3) + line(22, 17, 24, 23, HOLE, 3) + line(42, 17, 40, 23, HOLE, 3)
    return face + stripes + circle(25, 31, 2.8, HOLE) + circle(39, 31, 2.8, HOLE) + poly([(29, 38), (35, 38), (32, 42)], HOLE, 1) + ink_stroke("M26 44C30 47 34 47 38 44", 2.4, HOLE)


@reg("chat.iamb.iamb", GREY_DARK)
def iamb():
    return ink_stroke("M22 13H14V47H22M42 13H50V47H42", 4.5) + circle(32, 30, 5, INK)


@reg("chat.moin.moin", RED_LIGHT)
def moin():
    return bubble_b(32, 27, 36, 26) + circle(25, 24, 2.6, HOLE) + circle(39, 24, 2.6, HOLE) + ink_stroke("M24 31C28 36 36 36 40 31", 3, HOLE)


@reg("chat.quadrix.Quadrix", DEEP_PURPLE_LIGHT)
def quadrix():
    return rrect(13, 13, 17, 17, 4, INK) + rrect(34, 13, 17, 17, 4, INK, ' opacity=".7"') + rrect(13, 34, 17, 17, 4, INK, ' opacity=".7"') + rrect(34, 34, 17, 17, 4, INK, ' opacity=".4"')


@reg("ci.not.Rune", DEEP_PURPLE_DARK)
def rune():
    return ink_stroke("M23 11V49M23 14H36L44 22L36 30H23M30 30L45 49", 5)


@reg("club.haroohie.SerialLoops", TEAL_DEEP)
def serialloops():
    return (ink_stroke("M45 22C41 15 34 12 27 14C19 17 15 25 17 33", 4.2) + poly([(11, 29), (22, 29), (17, 38)], INK, 2)
            + ink_stroke("M19 38C23 45 30 48 37 46C45 43 49 35 47 27", 4.2) + poly([(53, 31), (42, 31), (47, 22)], INK, 2))


@reg("club.zbridge.zbridge", BLUE_DARK)
def zbridge():
    return ink_stroke("M10 38H54M14 38C14 24 24 18 32 18C40 18 50 24 50 38M22 38V27M32 38V18M42 38V27", 3.6) + line(10, 46, 54, 46, INK, 4)


@reg("cn.apipost.apipost", ORANGE)
def apipost():
    return ink_stroke("M24 13C19 13 19 18 19 22C19 26 17 30 13 30C17 30 19 34 19 38C19 42 19 47 24 47M40 13C45 13 45 18 45 22C45 26 47 30 51 30C47 30 45 34 45 38C45 42 45 47 40 47", 4) + circle(32, 30, 4, INK)


@reg("cn.eeo.ClassIn", BLUE)
def classin():
    return rrect(11, 13, 42, 28, 4, INK) + line(18, 23, 34, 23, HOLE, 3.4) + line(18, 31, 28, 31, HOLE, 3.4) + ink_stroke("M32 41V50M24 50H40", 4)


@reg("cn.feishu.Feishu", INDIGO)
def feishu():
    return path("M12 24C24 22 34 28 42 38C36 40 28 38 22 33C17 29 14 27 12 24Z", INK) + path("M30 18C42 14 52 20 54 30C48 28 40 28 34 30C30 26 30 22 30 18Z", INK, ' opacity=".6"')


@reg("cn.lceda.LCEDAPro", ORANGE_DEEP)
def lceda():
    out = rrect(20, 20, 24, 24, 4, INK) + rrect(27, 27, 10, 10, 2, HOLE)
    for t in (25, 32, 39):
        out += line(t, 12, t, 20, INK, 3.2) + line(t, 44, t, 52, INK, 3.2) + line(12, t + 0, 20, t, INK, 3.2) + line(44, t, 52, t, INK, 3.2)
    return out


@reg("cn.ottercorp.xivlaunchercn", INDIGO_LIGHT)
def xivlauncher():
    return (poly([(32, 9), (42, 24), (32, 51), (22, 24)], INK, 2) + line(22, 24, 42, 24, HOLE, 2.6) + line(32, 9, 32, 24, HOLE, 2.2)
            + poly([(14, 28), (20, 31), (23, 38)], INK, 1.5) + poly([(50, 28), (44, 31), (41, 38)], INK, 1.5))


@reg("cn.toside.lxmusic.lx-music-desktop", DEEP_PURPLE_SOFT)
def lxmusic():
    return circle(32, 30, 18, INK) + ink_stroke("M28 38V22L40 19V35", 3.4, HOLE) + circle(25, 38, 4, HOLE) + circle(37, 35, 4, HOLE)
