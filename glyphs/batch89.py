# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 89: the fourth hundred apps from the gap list (flags/app-gap-list-full.md),
rows 301 to 400, JioSphere to BigPEmu. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import dim, ell, fit_b, H, I, ink_stroke, registry, ring_d, star4

ICONS, SMALL, reg, _ = registry()

def leaf(cx, cy, rot, rx=7, ry=3.4):
    return g(ell(cx, cy, rx, ry), f"rotate({rot} {f(cx)} {f(cy)})")

@reg("com.jiosphere.JioSphere", DEEP_PURPLE)
def jiosphere():
    return fit_b(ring_d(32, 30, 17, 4) + ink_stroke("M32 13C22 20 22 40 32 47C42 40 42 20 32 13Z", 3.4) + line(15, 30, 49, 30, I, 3.4), 0.91)

@reg("com.jovial.jrpn15", ORANGE_LIGHT)
def jrpn15():
    out = rrect(17, 9, 30, 42, 5, I) + rrect(21, 13, 22, 8, 2, H)
    for r in range(3):
        for c in range(3):
            out += rrect(21 + c * 8, 25 + r * 7, 6, 4.5, 1.2, H)
    return fit_b(out + rrect(21, 46, 22, 2.5, 1, H), 0.74)

@reg("com.jovial.jrpn16", GREY_DEEP)
def jrpn16():
    out = rrect(8, 16, 48, 32, 5, I) + rrect(12, 20, 26, 8, 2, H) + star4(46, 24, 5, H)
    for r in range(2):
        for c in range(6):
            out += rrect(12 + c * 7.2, 33 + r * 7, 5, 4.5, 1.2, H)
    return fit_b(out, 0.71)

@reg("com.js8call.JS8Call", BLUE)
def js8call():
    return fit_b(poly([(32, 26), (37, 50), (27, 50)], I, 2) + circle(32, 22, 4, I) + line(29.5, 41, 34.5, 41, H, 2)
               + ink_stroke("M24 15A11 11 0 0 0 24 29", 3.4) + ink_stroke("M40 15A11 11 0 0 1 40 29", 3.4)
               + ink_stroke("M19 10A18 18 0 0 0 19 34", 3.4) + ink_stroke("M45 10A18 18 0 0 1 45 34", 3.4), 0.69)

@reg("com.jwestall.Forecast", YELLOW_DARK)
def forecast():
    cloud = "M20 46H42A7.5 7.5 0 0 0 43 31A11 11 0 0 0 22 29A8.5 8.5 0 0 0 20 46Z"
    sun = circle(41, 22, 11, I)
    return fit_b(sun + g(path(cloud, I, f' stroke="{H}" stroke-width="4"'), "translate(-6 2)"), 0.78)

@reg("com.k0vcz.Artemis", RED_LIGHT)
def artemis():
    return fit_b(ink_stroke("M22 10Q46 30 22 50", 4.5) + line(22, 10, 22, 50, I, 2) + line(12, 30, 52, 30, I, 3.5)
               + poly([(54, 30), (45, 24), (45, 36)], I, 1.5) + ink_stroke("M17 30L12 25M17 30L12 35", 3), 0.71)

@reg("com.kalbareader.Kalba", CYAN_DEEP)
def kalba():
    return fit_b(ink_stroke("M10 46L22 12L34 46M14.5 35H29.5", 5) + ring_d(44, 38, 6.5, 4.4) + line(50.5, 29, 50.5, 45, I, 4.4), 0.72)

@reg("com.kavilgroup.gelectrical", ORANGE)
def gelectrical():
    return fit_b(ink_stroke("M12 30H20L24 20L30 40L36 20L40 40L44 30H52", 4.2) + circle(10, 30, 4, I) + circle(54, 30, 4, I)
               + line(32, 44, 32, 52, I, 3.6) + line(25, 52, 39, 52, I, 3.6), 0.76)

@reg("com.kavilgroup.gestimator", PURPLE_LIGHT)
def gestimator():
    out = rrect(8, 22, 48, 18, 3.5, I)
    for k, h in enumerate((7, 4, 7, 4, 7, 4, 7)):
        out += line(14 + k * 6, 22, 14 + k * 6, 22 + h + 1, H, 2.2, "butt")
    return fit_b(g(out, "rotate(-28 32 30)"), 0.74)

@reg("com.kgurgul.cpuinfo", INDIGO_LIGHT)
def cpuinfo():
    out = rrect(19, 19, 26, 26, 4, I) + rrect(25, 25, 14, 14, 2, H)
    for x in (26, 32, 38):
        out += line(x, 11, x, 19, I, 3) + line(x, 45, x, 53, I, 3) + line(11, x - 0, 19, x, I, 3) + line(45, x, 53, x, I, 3)
    return fit_b(out, 0.81)

@reg("com.kjxbyz.PicGuard", BROWN)
def picguard():
    shield = "M32 9L49 15V30C49 41 41 47 32 51C23 47 15 41 15 30V15Z"
    return fit_b(path(shield, I) + poly([(21, 38), (28, 28), (33, 34), (37, 29), (43, 38)], H, 1.6) + circle(39, 22, 3, H), 0.8)

@reg("com.kjxbyz.PicGuardPro", INDIGO_LIGHT)
def picguardpro():
    return fit_b(rrect(8, 12, 40, 32, 5, I) + poly([(13, 38), (22, 26), (29, 35), (34, 30), (43, 38)], H, 1.6)
               + circle(36, 21, 3.4, H) + circle(46, 43, 10, I, f' stroke="{H}" stroke-width="3.2"')
               + circle(46, 43, 3.6, H), 0.66)

@reg("com.konstantintutsch.Lock", YELLOW_DARK)
def lock():
    return fit_b(rrect(15, 27, 34, 25, 5, I) + ink_stroke("M22 27V21A10 10 0 0 1 42 21V27", 5.2) + circle(32, 38, 4, H) + rrect(30.2, 40, 3.6, 8, 1.4, H), 0.8)

@reg("com.krioltech.fnmap", BLUE_GREY)
def fnmap():
    lines = "M32 18V24M32 24H18V27M32 24H46V27M18 37V42M18 42H12V46M18 42H24V46M46 37V42M46 42H40V46M46 42H52V46"
    return fit_b(ink_stroke(lines, 3.2) + circle(32, 13, 5, I) + circle(18, 32, 5, I) + circle(46, 32, 5, I)
               + "".join(circle(x, 50, 4, I) for x in (12, 24, 40, 52)), 0.67)

@reg("com.kristianduske.TrenchBroom", LIGHT_BLUE_DARK)
def trenchbroom():
    return fit_b(poly([(32, 8), (51, 19), (32, 30), (13, 19)], I, 2) + dim(poly([(13, 24), (30, 34), (30, 54), (13, 44)], I, 2), .65)
               + dim(poly([(34, 34), (51, 24), (51, 44), (34, 54)], I, 2), .4), 0.76)

@reg("com.ktechpit.colorsmith", AMBER_LIGHT)
def colorsmith():
    out = ""
    for ang, o in ((-34, .45), (0, .72), (34, 1)):
        out += g(rrect(25, 8, 14, 40, 3.5, I, f' opacity="{o}"') + circle(32, 16, 2.6, H), f"rotate({ang} 32 50)")
    return fit_b(out, 0.63)

@reg("com.ktechpit.colorwall", PINK_DEEP)
def colorwall():
    rows = [((10, 18), (31, 23)), ((10, 26), (39, 15)), ((10, 14), (27, 27)), ]
    out = ""
    for r, row in enumerate(((10, 18, 31, 23), (10, 26, 39, 15), (10, 14, 27, 27))):
        a, wa, b, wb = row
        y = 12 + r * 13
        out += rrect(a, y, wa, 10, 2.5, I, f' opacity="{(1, .6, .8)[r]}"') + rrect(b, y, wb, 10, 2.5, I, f' opacity="{(.55, 1, .65)[r]}"')
    return fit_b(out + rrect(10, 51, 44, 3.5, 1.5, I, ' opacity=".4"'), 0.67)

@reg("com.ktechpit.formatfactory", TEAL)
def formatfactory():
    body = "M10 50V29L22 36V29L34 36V29L44 36V12H53V50Z"
    return fit_b(path(body, I) + "".join(rrect(x, 42, 5, 5, 1, H) for x in (15, 26, 37)), 0.66)

@reg("com.ktechpit.glate", DEEP_ORANGE_LIGHT)
def glate():
    return fit_b(rrect(8, 10, 28, 28, 6, I) + ink_stroke("M14 31L22 15L30 31M17 26H27", 3.2, H)
               + rrect(26, 26, 28, 28, 6, I, f' stroke="{H}" stroke-width="3.4"')
               + ink_stroke("M32 36H48M40 33V36M35 46C41 44 45 40 45 36M37 40C39 44 43 46 47 46", 2.4, H), 0.63)

@reg("com.ktechpit.omnidict", DEEP_PURPLE_DEEP)
def omnidict():
    return fit_b(rrect(14, 8, 32, 44, 4, I) + line(20, 8, 20, 52, H, 2.4) + rrect(25, 14, 16, 9, 1.8, H)
               + line(25, 31, 40, 31, H, 2.6) + line(25, 38, 36, 38, H, 2.6) + poly([(37, 52), (37, 58), (41, 55)], I, 1), 0.66)

@reg("com.ktechpit.orion", GREY_LIGHT)
def orion():
    out = ink_stroke("M20 14L27 31L22 50M44 12L37 27L42 48M27 31L37 27", 3)
    return fit_b(out + star4(20, 14, 6.5) + star4(44, 12, 5.5) + star4(22, 50, 5.5) + star4(42, 48, 5.5) + circle(27, 31, 3.4, I) + circle(37, 27, 3.4, I), 0.66)

@reg("com.ktechpit.pixelbatch", GREY_LIGHT)
def pixelbatch():
    out = ""
    for r in range(3):
        for c in range(3):
            o = 1 if (r + c) % 2 == 0 else .5
            out += rrect(11 + c * 14, 11 + r * 14, 11, 11, 2.4, I, f' opacity="{o}"')
    return fit_b(out, 0.66)

@reg("com.ktechpit.red", BLUE_DEEP)
def red():
    return fit_b(path("M8 30Q32 6 56 30Q32 54 8 30Z", I) + circle(32, 30, 10, H) + circle(32, 30, 5, I) + circle(35, 27, 1.8, H), 0.83)

@reg("com.ktechpit.torrhunt", YELLOW)
def torrhunt():
    return fit_b(path("M14 10H27V30A5 5 0 0 0 37 30V10H50V30A18 18 0 0 1 14 30Z", I) + line(14, 18, 27, 18, H, 2.6, "butt") + line(37, 18, 50, 18, H, 2.6, "butt"), 0.67)

@reg("com.ktechpit.typingtutor", RED_DARK)
def typingtutor():
    out = rrect(8, 16, 48, 32, 5, I)
    for x in (13, 21, 29, 37, 45):
        out += rrect(x, 22, 5, 5, 1.2, H)
    for x in (17, 25, 33, 41):
        out += rrect(x, 30, 5, 5, 1.2, H)
    return fit_b(out + rrect(20, 38, 24, 4.5, 1.8, H), 0.72)

@reg("com.ktechpit.wonderwall", CYAN_LIGHT)
def wonderwall():
    out = path("M15 38A17 17 0 0 1 49 38Z", I) + ink_stroke("M12 43Q18 39 24 43T36 43T48 43", 3.2) + ink_stroke("M18 50Q24 46 30 50T42 50", 3.2)
    for a in (-150, -120, -90, -60, -30):
        out += line(*pt(32, 38, 22, a), *pt(32, 38, 27, a), I, 3.2)
    return fit_b(out, 0.75)

@reg("com.kymorphia.Daphne", ORANGE_DEEP)
def daphne():
    out = ink_stroke("M20 52Q22 26 44 10", 3.6)
    for x, y in ((22.5, 38.5), (27, 28), (34, 18.5)):
        out += leaf(x - 6, y - 2, -55) + leaf(x + 6, y + 1, 15)
    return fit_b(out + leaf(45, 11, -20, 9, 4), 0.58)

@reg("com.lablicate.OpenChrom", PURPLE)
def openchrom():
    return fit_b(ink_stroke("M10 46H54", 3.6) + ink_stroke("M12 46C18 46 18 28 22 28C26 28 26 46 30 46C34 46 35 14 40 14C45 14 45 46 50 46", 4), 0.74)

@reg("com.leinardi.gx52", CYAN)
def gx52():
    return fit_b(rrect(12, 42, 40, 10, 4, I) + line(32, 42, 32, 24, I, 6) + circle(32, 17, 10, I) + circle(32, 17, 4, H) + rrect(40, 36, 8, 4, 2, H), 0.76)

@reg("com.lixgame.Lix", BROWN_DEEP)
def lix():
    return fit_b(path("M12 28A20 17 0 0 1 52 28Q47 34 42 28Q37 34 32 28Q27 34 22 28Q17 34 12 28Z", I) + ink_stroke("M32 29V46Q32 52 26 52", 4.2), 0.9)

@reg("com.longbridgeapp.LongbridgePro", INDIGO)
def longbridgepro():
    out = line(8, 36, 56, 36, I, 4.5) + ink_stroke("M12 36Q32 4 52 36", 4.2)
    for x, y in ((20, 25), (26, 21), (32, 19.5), (38, 21), (44, 25)):
        out += line(x, y, x, 36, I, 2.6)
    return fit_b(out + line(18, 36, 18, 50, I, 3.4) + line(46, 36, 46, 50, I, 3.4), 0.76)

@reg("com.luigi311.fitness-tracker", YELLOW_LIGHT)
def fitness_tracker():
    out = line(20, 30, 44, 30, I, 5) + rrect(17, 14, 7, 32, 2.5, I) + rrect(40, 14, 7, 32, 2.5, I) + rrect(10, 21, 6, 18, 2, I) + rrect(48, 21, 6, 18, 2, I)
    return fit_b(g(out, "rotate(-30 32 30)"), 0.77)

@reg("com.lumarcgames.miniball", BLUE_GREY_DEEP)
def miniball():
    return fit_b(circle(32, 30, 18, I) + ink_stroke("M16 24C25 34 39 34 48 24", 2.8, H) + ink_stroke("M16 37C25 27 39 27 48 37", 2.8, H) + line(32, 12.5, 32, 47.5, H, 2.6), 0.96)

@reg("com.lynnmichaelmartin.TimeTracker", LIGHT_BLUE)
def timetracker():
    return fit_b(rrect(10, 10, 44, 42, 5, I) + rrect(15, 16, 16, 5.5, 2.2, H) + rrect(22, 26, 22, 5.5, 2.2, H) + rrect(17, 36, 27, 5.5, 2.2, H) + line(15, 46, 49, 46, H, 2, "butt"), 0.66)

@reg("com.maplerain.telsis_translator_flutter", AMBER_DARK)
def telsis():
    return fit_b(ink_stroke("M10 22H44M36 13L45 22L36 31", 5) + ink_stroke("M54 40H20M28 31L19 40L28 49", 5), 0.73)

@reg("com.mardojai.DiccionarioLengua", PINK_LIGHT)
def diccionariolengua():
    return fit_b(ink_stroke("M20 52V28M20 35C20 24 44 24 44 36V52", 5.4) + ink_stroke("M14 15Q21 8 29 14T43 13", 4.2), 0.71)

@reg("com.mardojai.ForgeSparks", TEAL_DEEP)
def forgesparks():
    hammer = rrect(15, 11, 28, 12, 3, I) + rrect(26, 22, 6, 30, 2.5, I)
    return fit_b(g(hammer, "rotate(38 29 30)") + star4(48, 40, 6) + star4(54, 28, 4) + star4(40, 52, 4), 0.74)

@reg("com.markdeepwell.GitY", DEEP_ORANGE)
def gity():
    return fit_b(ink_stroke("M32 52V35M32 35L18 16M32 35L46 16", 5) + circle(18, 14, 5.5, I) + circle(46, 14, 5.5, I) + circle(32, 52, 5, I)
               + circle(18, 14, 2.2, H) + circle(46, 14, 2.2, H) + circle(32, 52, 2, H), 0.67)

@reg("com.markwyner.ratio", DEEP_PURPLE_LIGHT)
def ratio():
    return fit_b(rrect(8, 14, 48, 30, 3, I) + line(38, 14, 38, 44, H, 2.4, "butt") + line(38, 26, 56, 26, H, 2.4, "butt")
               + stroke("M38 14A30 30 0 0 0 8 44", H, 2.6) + stroke("M56 26A18 18 0 0 1 38 44", H, 2.6), 0.66)

@reg("com.mastropaolo.www.tabela", GREY_DEEP)
def tabela():
    return fit_b(ink_stroke("M46 12H19L34 30L19 48H46", 6), 0.69)

@reg("com.matthiasn.lotti", GREY)
def lotti():
    out = rrect(16, 10, 34, 42, 4, I)
    for y in (16, 26, 36, 46):
        out += rrect(9, y - 2, 12, 4, 2, I)
    return fit_b(out + line(28, 19, 43, 19, H, 3) + line(28, 29, 43, 29, H, 3) + line(28, 39, 37, 39, H, 3), 0.67)

@reg("com.maxint.maxint", BLUE_LIGHT)
def maxint():
    return fit_b(line(14, 12, 50, 12, I, 4.8) + ink_stroke("M32 52V24M20 35L32 23L44 35", 5.4), 0.65)

@reg("com.mediahuman.LyricsFinder", YELLOW_DEEP)
def lyricsfinder():
    return fit_b(circle(32, 28, 19, I) + poly([(19, 40), (15, 54), (30, 46)], I, 1.5) + circle(28, 35, 4.2, H)
               + ink_stroke("M32 35V20L41 23", 3.4, H), 0.73)

@reg("com.microsoft.AzureStorageExplorer", RED)
def azurestorageexplorer():
    cloud = "M8 48H50A9 9 0 0 0 51 30A13 13 0 0 0 26 27A10 10 0 0 0 8 48Z"
    return fit_b(path(cloud, I) + stroke("M30 28L38 32.5V41.5L30 46L22 41.5V32.5Z", H, 2.6) + stroke("M22 32.5L30 37L38 32.5M30 37V46", H, 2), 0.68)

@reg("com.mind_elixir.MindElixir", CYAN_DARK)
def mindelixir():
    return fit_b(rrect(21, 24, 22, 13, 4.5, I) + rrect(6, 10, 16, 9, 3, I) + rrect(6, 41, 16, 9, 3, I) + rrect(42, 10, 16, 9, 3, I) + rrect(42, 41, 16, 9, 3, I)
               + ink_stroke("M25 26L17 19M25 35L17 41M39 26L47 19M39 35L47 41", 3), 0.58)

@reg("com.moddb.TotalChaosRetro", ORANGE_LIGHT)
def totalchaosretro():
    return fit_b(path("M32 9C20 9 13 17 13 27C13 33 16 37 20 39V47H44V39C48 37 51 33 51 27C51 17 44 9 32 9Z", I)
               + circle(24, 28, 5.4, H) + circle(40, 28, 5.4, H) + poly([(32, 32), (29, 38), (35, 38)], H, 1)
               + line(28, 42, 28, 47, H, 2.2, "butt") + line(32, 42, 32, 47, H, 2.2, "butt") + line(36, 42, 36, 47, H, 2.2, "butt"), 0.82)

@reg("com.moulberry.PandoraLauncher", PURPLE_DEEP)
def pandoralauncher():
    return fit_b(path("M10 28C10 12 54 12 54 28Z", I) + rrect(10, 31, 44, 20, 3.5, I) + circle(32, 38, 3.6, H) + rrect(30.2, 40, 3.6, 7, 1.4, H)
               + star4(32, 10, 6) , 0.67)

@reg("com.mtkennerly.madamiru", ORANGE_DEEP)
def madamiru():
    out = rrect(8, 11, 22, 18, 3.5, I) + poly([(16, 16), (16, 24), (23, 20)], H, 1)
    for x, y in ((34, 11), (8, 33), (34, 33)):
        out += rrect(x, y, 22, 18, 3.5, I, ' opacity=".5"')
    return fit_b(out, 0.63)

@reg("com.nedrichards.octopusagile", BROWN_LIGHT)
def octopusagile():
    return fit_b(path("M15 28C15 15 22 9 32 9C42 9 49 15 49 28Z", I) + circle(25, 21, 3, H) + circle(39, 21, 3, H)
               + ink_stroke("M19 27C19 39 11 38 11 48M27 27C27 40 23 43 23 51M37 27C37 40 41 43 41 51M45 27C45 39 53 38 53 48", 4.6), 0.72)

@reg("com.neosubhamoy.neodlp", INDIGO_DEEP)
def neodlp():
    return fit_b(path("M24 9H40V26H50L32 46L14 26H24Z", I) + poly([(29, 14), (29, 22), (36, 18)], H, 1.2) + line(14, 53, 50, 53, I, 4.4), 0.7)

@reg("com.neoutils.NeoRegex", YELLOW)
def neoregex():
    out = ink_stroke("M25 12H17V48H25", 4.6) + ink_stroke("M39 12H47V48H39", 4.6)
    for a in (90, 30, 150):
        out += line(*pt(32, 30, 8.5, a), *pt(32, 30, 8.5, a + 180), I, 4)
    return fit_b(out, 0.69)

@reg("com.netxms.NetXMSClient", BLUE_GREY_LIGHT)
def netxmsclient():
    return fit_b(rrect(9, 11, 46, 31, 5, I) + ink_stroke("M14 29H23L27 20L33 36L37 26H50", 3.2, H) + rrect(26, 44, 12, 4, 1.5, I) + line(19, 51, 45, 51, I, 3.4), 0.65)

@reg("com.netxms.NetXMSClient50", LIGHT_BLUE_DEEP)
def netxmsclient50():
    out = ""
    for y in (10, 26, 42):
        out += rrect(13, y, 38, 12, 3.4, I) + circle(19.5, y + 6, 1.9, H) + line(27, y + 6, 44, y + 6, H, 2.4)
    return fit_b(out, 0.69)

@reg("com.netxms.NetXMSClient51", AMBER)
def netxmsclient51():
    return fit_b(ring_d(32, 30, 19, 4) + path("M32 30L32 12A18 18 0 0 1 50 30Z", I, ' opacity=".5"')
               + line(32, 30, 32, 12, I, 3.6) + circle(22, 38, 3, I), 0.82)

@reg("com.netxms.NetXMSClient52", PINK_DARK)
def netxmsclient52():
    out = circle(32, 30, 7, I)
    for k in range(5):
        x, y = pt(32, 30, 18, -90 + k * 72)
        out += line(32, 30, x, y, I, 3) + rrect(x - 4.5, y - 4.5, 9, 9, 2.4, I)
    return fit_b(out, 0.77)

@reg("com.netxms.NetXMSClient60", TEAL_LIGHT)
def netxmsclient60():
    return fit_b(rrect(9, 32, 46, 18, 4.5, I) + circle(18, 41, 2.3, H) + circle(26, 41, 2.3, H) + line(36, 41, 48, 41, H, 2.6)
               + line(18, 32, 13, 14, I, 3.6) + line(46, 32, 51, 14, I, 3.6) + line(32, 32, 32, 10, I, 3.6)
               + circle(13, 13, 3.4, I) + circle(51, 13, 3.4, I) + circle(32, 9, 3.4, I), 0.63)

@reg("com.netxms.NetXMSClient61", DEEP_ORANGE_DEEP)
def netxmsclient61():
    return fit_b(path("M32 9C23 9 19 16 19 25V33L14 40H50L45 33V25C45 16 41 9 32 9Z", I) + path("M26 44A6 6 0 0 0 38 44Z", I), 0.82)

@reg("com.netxms.NetXMSClient62", DEEP_PURPLE)
def netxmsclient62():
    out = rrect(15, 22, 34, 28, 4, I) + rrect(23, 11, 18, 12, 2.5, I)
    for x in (22, 27, 32, 37, 42):
        out += line(x, 36, x, 46, H, 2.4, "butt")
    return fit_b(out, 0.86)

@reg("com.nickgirga.webready", GREY_SOFT)
def webready():
    return fit_b(rrect(8, 11, 48, 38, 5.5, I) + line(8, 22, 56, 22, H, 2.6, "butt") + ink_stroke("M22 35H42M22 43H34", 5, H), 0.64)

@reg("com.nitrokey.nitrokey-app", GREY_DEEP)
def nitrokey_app():
    return fit_b(rrect(8, 22, 32, 20, 5, I) + rrect(40, 25, 15, 14, 2, I) + circle(18, 32, 4.4, H) + rrect(45, 28, 7, 2.6, 1, H) + rrect(45, 33.4, 7, 2.6, 1, H), 0.8)

@reg("com.nitrokey.nitrokey-app2", BLUE)
def nitrokey_app2():
    return fit_b(ink_stroke("M20 44C17 28 23 19 32 19C41 19 47 28 44 44", 3.8) + ink_stroke("M26 48C24 36 27 27 32 27C37 27 40 36 38 48", 3.8)
               + ink_stroke("M32 34V50", 3.8) + ink_stroke("M13 38C12 22 21 11 32 11C43 11 52 22 51 38", 3.8), 0.83)

@reg("com.nomachine.nxplayer", YELLOW_LIGHT)
def nxplayer():
    return fit_b(rrect(8, 11, 34, 25, 4.5, I) + rrect(26, 26, 30, 24, 4.5, I, f' stroke="{H}" stroke-width="3.6"')
               + poly([(37, 32), (37, 44), (47, 38)], H, 1.4), 0.63)

@reg("com.nonpolynomial.intiface_central", RED_DEEP)
def intiface_central():
    return fit_b(g(rrect(24, 8, 16, 44, 8, I) + line(24, 29, 40, 29, H, 2.4, "butt"), "rotate(30 32 30)")
               + ink_stroke("M12 20Q7 30 12 40", 3.4) + ink_stroke("M52 20Q57 30 52 40", 3.4) + ink_stroke("M5 24Q2 30 5 36", 3) + ink_stroke("M59 24Q62 30 59 36", 3), 0.65)

@reg("com.ntrack.n-track", CYAN)
def ntrack():
    return fit_b(rrect(8, 14, 20, 8, 2.5, I) + rrect(34, 14, 20, 8, 2.5, I) + rrect(8, 28, 10, 8, 2.5, I) + rrect(22, 28, 32, 8, 2.5, I)
               + rrect(8, 42, 26, 8, 2.5, I) + rrect(38, 42, 16, 8, 2.5, I) + line(31, 10, 31, 54, H, 3, "butt"), 0.66)

@reg("com.odnoyko.valot", ORANGE_DARK)
def valot():
    return fit_b(circle(32, 24, 15, I) + path("M24 34Q25 38 26 40H38Q39 38 40 34Z", I) + rrect(25, 42, 14, 4.5, 2, I) + rrect(28, 48, 8, 4, 2, I)
               + ink_stroke("M26 25L30 30L34 22L38 27", 2.6, H), 0.83)

@reg("com.okta.developer.CLI", PURPLE_LIGHT)
def okta_cli():
    return fit_b(ring_d(32, 30, 17, 6.5) + ink_stroke("M27 22L37 30L27 38", 4.6), 0.85)

@reg("com.one_ware.OneWare", INDIGO_LIGHT)
def oneware():
    return fit_b(path("M16 12H32A18 18 0 0 1 32 48H16Z", I) + line(6, 22, 16, 22, I, 3.6) + line(6, 38, 16, 38, I, 3.6) + line(50, 30, 58, 30, I, 3.6), 0.65)

@reg("com.onekeepass.OneKeePass", BROWN)
def onekeepass():
    out = rrect(11, 12, 42, 38, 5, I) + ring_d(32, 31, 10, 3, H) + circle(32, 31, 3.2, H)
    for a in (0, 90, 180, 270):
        out += line(*pt(32, 31, 10, a), *pt(32, 31, 14.5, a), H, 2.6, "butt")
    return fit_b(out + rrect(15, 50, 7, 4, 1.5, I) + rrect(42, 50, 7, 4, 1.5, I), 0.71)

@reg("com.openterface.openterfaceQT", INDIGO_LIGHT)
def openterfaceqt():
    return fit_b(line(14, 30, 48, 30, I, 3.6) + circle(10, 30, 5.4, I) + poly([(58, 30), (48, 24), (48, 36)], I, 1.2)
               + ink_stroke("M24 30L30 18H38", 3.2) + rrect(37, 14, 8, 8, 1.2, I) + ink_stroke("M32 30L38 43H44", 3.2) + circle(48, 43, 4.2, I), 0.72)

@reg("com.openwebui.open-webui", YELLOW_DARK)
def open_webui():
    return fit_b(rrect(8, 10, 34, 24, 6.5, I) + poly([(14, 33), (12, 43), (24, 34)], I, 1.5) + line(15, 18, 35, 18, H, 2.8) + line(15, 26, 29, 26, H, 2.8)
               + rrect(24, 28, 32, 22, 6.5, I, f' stroke="{H}" stroke-width="3.6"') + poly([(50, 49), (52, 57), (43, 50)], I, 1.5)
               + line(31, 36, 49, 36, H, 2.8) + line(31, 43, 42, 43, H, 2.8), 0.64)

@reg("com.oppzippy.OpenSCQ30", BLUE_GREY)
def openscq30():
    return fit_b(ink_stroke("M14 38V30A18 18 0 0 1 50 30V38", 4.8) + rrect(9, 34, 11, 18, 4.5, I) + rrect(44, 34, 11, 18, 4.5, I), 0.72)

@reg("com.outerwildsmods.owmods_gui", LIGHT_BLUE_LIGHT)
def owmods_gui():
    ring_ = g('<ellipse cx="32" cy="30" rx="24" ry="8" fill="none" stroke="INK" stroke-width="3.6"/>', "rotate(-24 32 30)")
    return fit_b(ring_ + circle(32, 30, 12, I, f' stroke="{H}" stroke-width="3.4"') + circle(52, 14, 3.6, I), 0.62)

@reg("com.overwolf.curseforge", AMBER_DEEP)
def curseforge():
    return fit_b(path("M8 22H52V26Q52 30 42 31H40V38H46V47H20V38H26V31H24Q12 31 8 22Z", I) + star4(47, 11, 6) + star4(55, 21, 3.4), 0.6)

@reg("com.oyajun.ColorCode", PINK)
def colorcode():
    out = ""
    for k, o in enumerate((1, .85, .7, .55, .9, .75)):
        x0, y0 = pt(32, 30, 20, -90 + k * 60)
        x1, y1 = pt(32, 30, 20, -30 + k * 60)
        out += path(f"M32 30L{f(x0)} {f(y0)}A20 20 0 0 1 {f(x1)} {f(y1)}Z", I, f' opacity="{o}" stroke="{H}" stroke-width="2.6" stroke-linejoin="round"')
    return fit_b(out, 0.92)

@reg("com.p1security.diagng", TEAL_DARK)
def diagng():
    return fit_b(rrect(15, 26, 32, 20, 3.5, I) + rrect(23, 19, 16, 8, 2, I) + rrect(8, 31, 7, 10, 2, I) + rrect(47, 31, 8, 10, 2, I) + rrect(20, 46, 22, 5, 2, I)
               + ink_stroke("M20 36H26L29 31L33 41L36 36H43", 2.6, H), 0.81)

@reg("com.pikatorrent.PikaTorrent", DEEP_ORANGE_LIGHT)
def pikatorrent():
    ears = g('<ellipse cx="22" cy="15" rx="4.8" ry="11" fill="INK"/>', "rotate(-14 22 15)") + g('<ellipse cx="42" cy="15" rx="4.8" ry="11" fill="INK"/>', "rotate(14 42 15)")
    return fit_b(ears + circle(32, 36, 16, I) + circle(25.5, 34, 2.8, H) + circle(38.5, 34, 2.8, H) + circle(21, 42, 3.2, H) + circle(43, 42, 3.2, H)
               + poly([(30, 40), (34, 40), (32, 43)], H, 1), 0.61)

@reg("com.pinegrow.Pinegrow", DEEP_PURPLE_DEEP)
def pinegrow():
    out = line(32, 9, 32, 52, I, 3.6)
    for y in (22, 32, 42):
        out += line(32, y + 7, 17, y - 2, I, 3.6) + line(32, y + 7, 47, y - 2, I, 3.6)
    return fit_b(out + line(32, 52, 32, 58, I, 3.6), 0.74)

@reg("com.pojtinger.felicitas.Multiplex", BLUE_SOFT)
def multiplex():
    out = poly([(24, 10), (42, 21), (42, 39), (24, 50)], I, 3)
    for y in (19, 30, 41):
        out += line(7, y, 24, y, I, 3.6)
    return fit_b(out + line(42, 30, 57, 30, I, 3.6), 0.64)

@reg("com.pojtinger.felicitas.Sessions", GREY_LIGHT)
def sessions():
    return fit_b(rrect(18, 9, 36, 28, 4.5, I, ' opacity=".5"') + rrect(8, 22, 36, 28, 4.5, I) + line(8, 31, 44, 31, H, 2.6, "butt")
               + line(14, 38, 30, 38, H, 2.6) + line(14, 44, 25, 44, H, 2.6), 0.73)

@reg("com.pokemmo.PokeMMO", BLUE_DEEP)
def pokemmo():
    return fit_b(circle(32, 35, 16, I) + poly([(17, 28), (13, 9), (28, 20)], I, 2.4) + poly([(47, 28), (51, 9), (36, 20)], I, 2.4)
               + circle(26, 34, 3.6, H) + circle(38, 34, 3.6, H) + ink_stroke("M24 43L28 46L32 43L36 46L40 43", 2.4, H), 0.61)

@reg("com.polydez.KeyVault", YELLOW)
def keyvault():
    out = ring_d(16, 30, 9, 5) + line(25, 30, 53, 30, I, 5) + line(43, 30, 43, 40, I, 4.6) + line(51, 30, 51, 38, I, 4.6)
    return fit_b(g(out, "rotate(-40 32 30)"), 0.77)

@reg("com.popcornfx.PopcornFXEditor", RED_LIGHT)
def popcornfx():
    out = poly([(16, 29), (48, 29), (43, 52), (21, 52)], I, 2.4)
    for x in (25, 32, 39):
        out += line(x - 0.5, 33, x - 1, 48, H, 3)
    return fit_b(out + circle(21, 22, 7, I) + circle(32, 16, 8.5, I) + circle(43, 22, 7, I) + circle(27, 24, 6, I) + circle(38, 24, 6, I), 0.77)

@reg("com.poppingmoon.aria", CYAN_DEEP)
def aria():
    return fit_b(ink_stroke("M13 50L32 11L51 50", 5.4) + ink_stroke("M32 28V45M25 38L32 45L39 38", 4.4), 0.72)

@reg("com.pot_app.pot", ORANGE)
def pot():
    return fit_b(rrect(13, 27, 38, 22, 9, I) + line(11, 26, 53, 26, I, 4.4) + line(7, 33, 13, 33, I, 4) + line(51, 33, 57, 33, I, 4)
               + ink_stroke("M25 19Q21 15 25 11M39 19Q35 15 39 11", 3.2), 0.74)

@reg("com.pragmar.interrobot", PURPLE_DARK)
def interrobot():
    return fit_b(ink_stroke("M21 22C21 6 44 6 44 22C44 31 32 30 32 40", 5.6) + circle(32, 51, 4, I), 0.76)

@reg("com.prof18.feedflow", DEEP_PURPLE_SOFT)
def feedflow():
    return fit_b(circle(16, 46, 4.6, I) + ink_stroke("M12 28A24 24 0 0 1 38 52", 5) + ink_stroke("M12 12A40 40 0 0 1 54 52", 5), 0.61)

@reg("com.projecthawkthorne.Hawkthorne", BROWN_DEEP)
def hawkthorne():
    return fit_b(path("M6 26Q20 12 32 30Q44 12 58 26Q46 25 41 35L32 47L23 35Q18 25 6 26Z", I) + circle(32, 33, 2.2, H), 0.74)

@reg("com.q3rally.Q3Rally", INDIGO)
def q3rally():
    out = line(14, 8, 14, 54, I, 4.4)
    for r in range(3):
        for c in range(4):
            if (r + c) % 2 == 0:
                out += rrect(20 + c * 9, 11 + r * 9, 9, 9, 0.8, I)
    return fit_b(out, 0.58)

@reg("com.qzandronum.Q-Zandronum", YELLOW_LIGHT)
def qzandronum():
    return fit_b(ring_d(30, 28, 16, 6.6) + line(39, 38, 52, 51, I, 7), 0.67)

@reg("com.rabbit_company.passky", BLUE_GREY_DEEP)
def passky():
    out = rrect(7, 17, 50, 28, 7.5, I)
    for x in (19, 32, 45):
        for a in (90, 30, 150):
            out += line(*pt(x, 31, 4.6, a), *pt(x, 31, 4.6, a + 180), H, 2.6)
    return fit_b(out, 0.73)

@reg("com.ranfdev.Lobjur", LIGHT_BLUE)
def lobjur():
    out = ell(32, 38, 7.5, 12) + poly([(27, 48), (37, 48), (42, 55), (22, 55)], I, 1.5) + ink_stroke("M26 30L18 21M38 30L46 21", 4)
    out += circle(15, 16, 8, I) + circle(49, 16, 8, I)
    out += line(15, 16, 11, 7, H, 3.2) + line(49, 16, 53, 7, H, 3.2)
    return fit_b(out + ink_stroke("M29 27Q27 16 31 8M35 27Q37 16 33 8", 2.2), 0.61)

@reg("com.ranfdev.Notify", AMBER_LIGHT)
def notify():
    return fit_b(rrect(8, 18, 46, 26, 6.5, I) + circle(20, 31, 5.4, H) + line(30, 26, 46, 26, H, 3) + line(30, 34, 41, 34, H, 3)
               + circle(52, 17, 6.6, I, f' stroke="{H}" stroke-width="3"'), 0.63)

@reg("com.rcloneui.RcloneUI", PINK_DEEP)
def rcloneui():
    return fit_b(rrect(24, 8, 28, 34, 4.5, I, ' opacity=".35"') + rrect(17, 16, 28, 34, 4.5, I, ' opacity=".65"') + rrect(10, 24, 28, 30, 4.5, I)
               + line(16, 34, 32, 34, H, 2.8) + line(16, 41, 32, 41, H, 2.8) + line(16, 48, 26, 48, H, 2.8), 0.72)

@reg("com.realm667.Wolfenstein_Blade_of_Agony", TEAL)
def wolfenstein_blade_of_agony():
    sword = poly([(32, 5), (37, 12), (36, 35), (28, 35), (27, 12)], I, 1.6) + line(32, 13, 32, 32, H, 1.8) + rrect(19, 36, 26, 5.4, 2.4, I) + rrect(29.4, 42, 5.2, 10, 1.6, I) + circle(32, 55, 3.4, I)
    return fit_b(g(sword, "rotate(40 32 30)"), 0.69)

@reg("com.recisio.karafun-premium", DEEP_ORANGE_DARK)
def karafun_premium():
    return fit_b(circle(33, 15, 5.6, I) + dim(ink_stroke("M11 32Q13 16 26 15", 2.6), .6) + line(11, 36, 32, 36, I, 5) + dim(line(32, 36, 53, 36, I, 5), .45) + dim(line(11, 48, 44, 48, I, 5), .45), 0.81)

@reg("com.remnantsoftheprecursors.ROTP", DEEP_PURPLE_LIGHT)
def rotp():
    return fit_b(path("M21 29A11 11 0 0 1 43 29Z", I) + ell(32, 32, 24, 7.5) + circle(20, 32, 1.8, H) + circle(32, 33.5, 1.8, H) + circle(44, 32, 1.8, H)
               + dim(poly([(24, 41), (40, 41), (47, 54), (17, 54)], I, 1), .45), 0.83)

@reg("com.remnote.RemNote", LIGHT_BLUE_DEEP)
def remnote():
    out = ""
    for cx, cy, x2, y in ((13, 14, 51, 14), (21, 28, 51, 28), (29, 42, 51, 42)):
        out += circle(cx, cy, 3.6, I) + line(cx + 8, cy, x2, y, I, 4.6)
    return fit_b(out + ink_stroke("M13 19V28H17M21 33V42H25", 2.6), 0.64)

@reg("com.reqable.Reqable", GREY)
def reqable():
    return fit_b(ink_stroke("M24 11Q17 11 17 18V25Q17 30 11 30Q17 30 17 35V42Q17 49 24 49", 3.8) + ink_stroke("M40 11Q47 11 47 18V25Q47 30 53 30Q47 30 47 35V42Q47 49 40 49", 3.8)
               + ink_stroke("M26 25H38M34 21L38 25L34 29", 3) + ink_stroke("M38 36H26M30 32L26 36L30 40", 3), 0.74)

@reg("com.revolutionarygamesstudio.ThriveLauncher", BLUE_LIGHT)
def thrivelauncher():
    return fit_b(circle(29, 27, 17, I) + circle(26, 25, 7, H) + circle(26, 25, 3, I) + circle(37, 36, 2.4, H) + circle(21, 37, 2, H)
               + ink_stroke("M41 40C49 40 46 48 54 48C57 48 58 51 57 53", 3.8), 0.61)

@reg("com.richwhitehouse.BigPEmu", YELLOW_DEEP)
def bigpemu():
    return fit_b(rrect(13, 9, 38, 35, 5, I) + rrect(20, 42, 24, 11, 2.4, I) + rrect(18, 14, 28, 17, 2.6, H) + star4(32, 22.5, 6)
               + line(18, 37, 46, 37, H, 2.4, "butt"), 0.68)
