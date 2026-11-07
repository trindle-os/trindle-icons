# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 90: the fifth hundred apps from the gap list (flags/app-gap-list-full.md),
rows 401 to 500, Rio to constellation. Each is a simple original mark on its own tile."""
import math
from lm import *
from glyphs.kit import arrowhead, dim, ell, fit_b, H, I, ink_stroke, registry, ring_d, star4

ICONS, SMALL, reg, _ = registry()

def hexa(cx, cy, r, c=I):
    return poly([pt(cx, cy, r, 30 + 60 * k) for k in range(6)], c, 1.2)

def iso(cx, cy, s):
    w = .87 * s
    top = poly([(cx, cy - s), (cx + w, cy - s / 2), (cx, cy), (cx - w, cy - s / 2)], I, .8)
    left = poly([(cx - w, cy - s / 2), (cx, cy), (cx, cy + s), (cx - w, cy + s / 2)], I, .8)
    right = poly([(cx + w, cy - s / 2), (cx, cy), (cx, cy + s), (cx + w, cy + s / 2)], I, .8)
    return top + dim(left, .62) + dim(right, .38)

@reg("com.rioterm.Rio", RED)
def rio():
    return fit_b(rrect(9, 12, 46, 38, 7, I) + ink_stroke("M18 23L27 31L18 39", 4.4, H) + line(32, 41, 44, 41, H, 4.4), 0.71)

@reg("com.rocksandpaper.syndic", CYAN)
def syndic():
    return fit_b(circle(21, 43, 5, I) + ink_stroke("M21 29A14 14 0 0 1 35 43", 5.2) + ink_stroke("M21 15A28 28 0 0 1 49 43", 5.2), 0.81)

@reg("com.rq3.Reaction", BROWN_DARK)
def reaction():
    return fit_b(ring_d(32, 34, 16, 4.6) + rrect(27, 8, 10, 5, 2, I) + line(32, 13, 32, 16, I, 3)
               + poly([(35, 25), (26, 36), (31.5, 36), (29, 44), (38, 32), (32.5, 32)], I, 1.4), 0.88)

@reg("com.scanoss.sbom-workbench", INDIGO_DARK)
def sbom():
    return fit_b(rrect(11, 22, 42, 30, 4, I) + rrect(8, 13, 48, 11, 3, I, f' stroke="{H}" stroke-width="2.4"')
               + rrect(25, 30, 14, 5, 2.5, H) + line(32, 13, 32, 24, H, 2.4), 0.68)

@reg("com.sciactive.QuickDAV", AMBER_LIGHT)
def quickdav():
    folder = "M9 18Q9 14 13 14H25L30 19H51Q55 19 55 23V45Q55 49 51 49H13Q9 49 9 45Z"
    return fit_b(path(folder, I) + ink_stroke("M24 41V28M19 33L24 28L29 33", 3.4, H) + ink_stroke("M40 28V41M35 36L40 41L45 36", 3.4, H), 0.69)

@reg("com.seal_one.SealOne", PINK_LIGHT)
def sealone():
    out = "".join(circle(*pt(32, 30, 16, a * 36)[:2], 7.5, I) for a in range(10))
    return fit_b(out + circle(32, 30, 17, I) + ring_d(32, 30, 11, 2.6, H) + star4(32, 30, 6, H), 0.83)

@reg("com.sejda.Sejda", TEAL)
def sejda():
    page = "M14 9H33L46 22V49Q46 51 44 51H16Q14 51 14 49Z"
    penc = path("M-3.5 -14H3.5V6L0 13L-3.5 6Z", I, f' stroke="{H}" stroke-width="2.6" stroke-linejoin="round"')
    return fit_b(path(page, I) + poly([(33, 9), (33, 22), (46, 22)], H, 0.6) + line(20, 34, 36, 34, H, 3) + line(20, 41, 30, 41, H, 3)
               + g(penc, "translate(46 40) rotate(38)"), 0.71)

@reg("com.serial_studio.Serial-Studio", GREY)
def serialstudio():
    out = path("M10 14H54L49 38H15Z", I, f' stroke="{I}" stroke-width="3" stroke-linejoin="round"')
    for k in range(5):
        out += circle(18 + k * 7, 22, 2.3, H)
    for k in range(4):
        out += circle(21.5 + k * 7, 30.5, 2.3, H)
    return fit_b(out + rrect(24, 41, 16, 11, 2, I), 0.68)

@reg("com.sevenkfans.sevenkaa", BLUE)
def sevenkaa():
    return fit_b(ink_stroke("M17 15H47L28 50", 7) + line(23, 33, 40, 33, I, 5), 0.79)

@reg("com.seventhstring.Transcribe", ORANGE_DEEP)
def transcribe():
    out = ""
    for i, h in enumerate((8, 18, 28, 40, 24, 32, 16, 22, 8)):
        out += rrect(10 + i * 5.6, 30 - h / 2, 4, h, 2, I)
    return fit_b(out, 0.73)

@reg("com.sidevesh.Luminance", PURPLE_DARK)
def luminance():
    out = circle(32, 30, 11, I) + path("M32 19A11 11 0 0 0 32 41Z", H)
    for a in range(8):
        x1, y1 = pt(32, 30, 17, a * 45)
        x2, y2 = pt(32, 30, 22, a * 45)
        out += line(x1, y1, x2, y2, I, 3.6)
    return fit_b(out, 0.82)

@reg("com.sigmyne.crush", BLUE_GREY_SOFT)
def crush():
    return fit_b(ink_stroke("M19 10L32 23L45 10", 5) + ink_stroke("M19 50L32 37L45 50", 5) + line(10, 30, 54, 30, I, 5), 0.74)

@reg("com.simulide.simulide", BLUE_GREY)
def simulide():
    return fit_b(ink_stroke("M52 46V16H44L40 6L32 26L24 6L20 16H12V46H28M36 46H52", 4.6)
               + line(28, 38, 28, 54, I, 5) + line(36, 42, 36, 50, I, 5), 0.7)

@reg("com.simutrans.Simutrans", LIGHT_BLUE)
def simutrans():
    out = rrect(9, 16, 46, 26, 6, I) + ink_stroke("M32 16V8M24 8H40", 3.2)
    for x in (14, 27, 40):
        out += rrect(x, 21, 10, 9, 1.8, H)
    out += line(14, 36, 50, 36, H, 2.4)
    for x in (20, 44):
        out += circle(x, 46, 4.6, I, f' stroke="{H}" stroke-width="2.4"')
    return fit_b(out, 0.78)

@reg("com.sireliah.Dragit", DEEP_ORANGE)
def dragit():
    box = f'<rect x="9" y="9" width="30" height="30" rx="4" fill="none" stroke="{I}" stroke-width="3.6" stroke-dasharray="6 5"/>'
    arrow = path("M28 28V54L35 47L40 57L46 54L41 45L50 44Z", I, f' stroke="{H}" stroke-width="2.6" stroke-linejoin="round"')
    return fit_b(box + arrow, 0.63)

@reg("com.sleepfiles.OSCAR", DEEP_PURPLE_DEEP)
def oscar():
    return fit_b(path("M32 10A20 20 0 1 0 52 38A16 16 0 0 1 32 10Z", I) + star4(47, 17, 7) + circle(54, 30, 2.4, I), 0.76)

@reg("com.slugchess.SlugChess", BROWN_SOFT)
def slugchess():
    return fit_b(circle(32, 15, 8, I) + rrect(23, 24, 18, 6, 3, I) + poly([(27, 30), (37, 30), (42, 44), (22, 44)], I, 1.2) + rrect(16, 44, 32, 8, 3.5, I), 0.76)

@reg("com.smasisoftware.smasi", RED_DARK)
def smasi():
    return fit_b(ink_stroke("M45 18C41 10 21 10 21 21C21 32 43 28 43 40C43 51 22 50 18 42", 7) + circle(48, 48, 3.4, I), 0.71)

@reg("com.snekstudio.Snekstudio", CYAN_DARK)
def snekstudio():
    head = g(ell(0, 0, 8.5, 6) + circle(2.5, -1.8, 1.9, H), "translate(44 17) rotate(12)")
    return fit_b(ink_stroke("M12 46C22 54 34 42 26 33C18 25 30 14 38 18", 7.4) + head + ink_stroke("M52 18L57 19M57 19L60 16M57 19L60 22", 2.4), 0.6)

@reg("com.solvespace.SolveSpace", BROWN)
def solvespace():
    return fit_b(ink_stroke("M14 46V14L50 46Z", 4.2) + ink_stroke("M14 36H24V46", 2.8) + circle(14, 14, 5, I) + circle(14, 46, 5, I) + circle(50, 46, 5, I), 0.67)

@reg("com.somaxa8.earx", INDIGO)
def earx():
    return fit_b(ink_stroke("M20 36C16 18 26 8 37 10C48 12 52 26 43 35C39 39 40 44 36 47C32 51 24 50 23 43", 5.4)
               + ink_stroke("M31 22C37 20 41 25 37 30C35 33 32 33 32 37", 3.8), 0.84)

@reg("com.soulfiremc.soulfire", AMBER_DEEP)
def soulfire():
    return fit_b(path("M32 7C34 18 47 22 47 36C47 46 41 53 32 53C23 53 17 46 17 36C17 29 21 25 24 20C26 27 28 28 30 26C32 22 28 14 32 7Z", I)
               + path("M32 30C34 35 39 37 39 43C39 47 36 50 32 50C28 50 25 47 25 43C25 37 30 35 32 30Z", H), 0.85)

@reg("com.spacestation14.Launcher", PINK_DEEP)
def launcher():
    out = circle(32, 31, 8, I) + rrect(6, 24, 18, 14, 2.4, I) + rrect(40, 24, 18, 14, 2.4, I) + line(24, 31, 40, 31, I, 4)
    out += line(15, 24, 15, 38, H, 2) + line(49, 24, 49, 38, H, 2) + line(32, 23, 32, 14, I, 3.2) + circle(32, 11, 3.4, I) + line(32, 39, 32, 49, I, 3.2)
    return fit_b(out + circle(32, 31, 3, H), 0.74)

@reg("com.st.STM32CubeMX", TEAL_DEEP)
def stm32cubemx():
    out = path("M32 11L48 20V40L32 49L16 40V20Z", I, f' stroke="{I}" stroke-width="2.4" stroke-linejoin="round"')
    out += ink_stroke("M16 20L32 29L48 20M32 29V49", 2.8, H)
    for y in (24, 36):
        out += line(6, y, 16, y, I, 3.2) + line(48, y, 58, y, I, 3.2)
    return fit_b(out, 0.69)

@reg("com.strlen.TreeSheets", GREY)
def treesheets():
    return fit_b(rrect(9, 9, 46, 46, 5, I) + line(32, 9, 32, 55, H, 2.6) + line(9, 32, 55, 32, H, 2.6)
               + line(20.5, 9, 20.5, 32, H, 2) + line(9, 20.5, 32, 20.5, H, 2), 0.61)

@reg("com.swarmtunes.Swarmtunes", BLUE_DARK)
def swarmtunes():
    return fit_b(hexa(20, 44, 7.5) + hexa(42, 40, 7.5) + line(25.5, 42, 25.5, 16, I, 4.2) + line(47.5, 38, 47.5, 11, I, 4.2)
               + poly([(25.5, 13), (47.5, 7.5), (47.5, 16), (25.5, 22)], I, 1), 0.7)

@reg("com.synology.synology-note-station", ORANGE)
def synologynotestation():
    return fit_b(path("M11 9H53V36L37 52H11Z", I) + poly([(53, 36), (37, 36), (37, 52)], H, .8)
               + line(18, 19, 46, 19, H, 3.4) + line(18, 27, 46, 27, H, 3.4) + line(18, 35, 29, 35, H, 3.4), 0.65)

@reg("com.syntevo.SmartGit", PURPLE_DEEP)
def smartgit():
    return fit_b(ink_stroke("M22 12V48", 4.6) + ink_stroke("M22 38C22 26 42 30 42 18", 4.6)
               + "".join(circle(x, y, 6.4, I) + circle(x, y, 2.4, H) for x, y in ((22, 12), (22, 48), (42, 16))), 0.73)

@reg("com.syntevo.SmartSynchronize", DEEP_PURPLE_LIGHT)
def smartsynchronize():
    return fit_b(rrect(8, 8, 18, 26, 3, I) + rrect(38, 26, 18, 26, 3, I) + line(12, 16, 22, 16, H, 2.2) + line(12, 22, 22, 22, H, 2.2)
               + line(42, 34, 52, 34, H, 2.2) + line(42, 40, 52, 40, H, 2.2)
               + ink_stroke("M30 16H48M43 11L48 16L43 21", 3.6) + ink_stroke("M34 44H16M21 39L16 44L21 49", 3.6), 0.63)

@reg("com.tenetcode.LiberDrop", BLUE_GREY_DEEP)
def liberdrop():
    return fit_b(ink_stroke("M10 38V50H54V38", 5.4) + ink_stroke("M32 8V36M20 26L32 38L44 26", 5.6), 0.6)

@reg("com.tercad.fingrom", LIGHT_BLUE_LIGHT)
def fingrom():
    out = rrect(8, 36, 10, 14, 2.4, I) + rrect(21, 28, 10, 22, 2.4, I) + rrect(34, 20, 10, 30, 2.4, I)
    return fit_b(out + circle(48, 17, 8.5, I) + ring_d(48, 17, 4, 2.2, H), 0.65)

@reg("com.theappgineer.community_remote", DEEP_ORANGE)
def communityremote():
    return fit_b(rrect(19, 8, 26, 46, 8, I) + circle(32, 22, 7, H) + circle(32, 22, 2.6, I)
               + circle(25.5, 38, 3, H) + circle(38.5, 38, 3, H) + rrect(25, 45, 14, 3.4, 1.7, H), 0.79)

@reg("com.thewavewarden.Odin2", DEEP_PURPLE_DARK)
def odin2():
    out = circle(32, 31, 13, I) + line(32, 31, 32, 21, H, 3.8)
    for a in range(135, 406, 45):
        x1, y1 = pt(32, 31, 18.5, a)
        x2, y2 = pt(32, 31, 23, a)
        out += line(x1, y1, x2, y2, I, 3.2)
    return fit_b(out, 0.77)

@reg("com.tominlab.wonderpen", CYAN_DARK)
def wonderpen():
    return fit_b(path("M32 55C19 44 16 33 22 22L32 9L42 22C48 33 45 44 32 55Z", I) + line(32, 35, 32, 53, H, 2.8) + circle(32, 30, 4, H), 0.79)

@reg("com.toolstack.Folio", RED_DEEP)
def folio():
    return fit_b(path("M29 14C23 10 15 10 8 13V48C15 45 23 45 29 49Z", I) + path("M35 14C41 10 49 10 56 13V48C49 45 41 45 35 49Z", I), 0.66)

@reg("com.tradingview.tradingview", CYAN_DEEP)
def tradingview():
    out = line(15, 10, 15, 50, I, 3) + rrect(9.5, 20, 11, 18, 2, I)
    out += line(32, 14, 32, 52, I, 3) + rrect(26.5, 24, 11, 20, 2, I) + rrect(29.5, 27, 5, 14, 1, H)
    out += line(49, 8, 49, 42, I, 3) + rrect(43.5, 14, 11, 18, 2, I)
    return fit_b(out, 0.67)

@reg("com.trougnouf.Cfait", BROWN_LIGHT)
def cfait():
    out = ""
    for k, y in enumerate((14, 30, 46)):
        out += (rrect(8, y - 7, 14, 14, 3.4, I) + circle(15, y, 2.4, H) if k < 2
                else rrect(8, y - 7, 14, 14, 3.4, "none", f' stroke="{I}" stroke-width="3"'))
        out += line(29, y, 55, y, I, 4.8)
    return fit_b(out, 0.59)

@reg("com.trustytodo.trustytodo", INDIGO_LIGHT)
def trustytodo():
    return fit_b(rrect(13, 11, 38, 43, 5, I) + rrect(23, 6, 18, 10, 3.4, I, f' stroke="{H}" stroke-width="2.4"') + ink_stroke("M22 34H42M22 43H33", 5, H), 0.68)

@reg("com.tuxpusher.TuxPusher", AMBER)
def tuxpusher():
    out = rrect(6, 41, 52, 6, 2.5, I)
    for k in range(3):
        out += rrect(8, 33 - k * 9, 26, 6, 3, I)
    return fit_b(out + circle(47, 20, 8.5, I) + ring_d(47, 20, 4, 2.4, H), 0.65)

@reg("com.tuxpusher.TuxPusherAF", PINK)
def tuxpusheraf():
    return fit_b(circle(32, 25, 17, I) + ring_d(32, 25, 11.5, 2.6, H) + star4(32, 25, 7.5, H) + rrect(12, 47, 40, 6, 3, I), 0.67)

@reg("com.ulaa.Ulaa", TEAL_DARK)
def ulaa():
    needle = g(poly([(32, 14), (38, 30), (32, 46), (26, 30)], I, 1.2) + circle(32, 30, 2.8, H), "rotate(45 32 30)")
    return fit_b(ring_d(32, 30, 22, 4.4) + needle, 0.81)

@reg("com.unfolding_machines.pum_lite", GREY_DEEP)
def pumlite():
    return fit_b(ink_stroke("M20 52V10H35A12 12 0 0 1 35 34H20", 7) + circle(46, 50, 3.6, I), 0.69)

@reg("com.unicornsonlsd.finamp", BLUE_LIGHT)
def finamp():
    return fit_b(ink_stroke("M13 40V32A19 19 0 0 1 51 32V40", 5.4) + rrect(9, 35, 11, 19, 5, I) + rrect(44, 35, 11, 19, 5, I), 0.63)

@reg("com.vargary.focal", ORANGE_LIGHT)
def focal():
    out = ""
    for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        x, y = 32 - sx * 22, 30 - sy * 22
        out += ink_stroke(f"M{x} {y + sy * 10}V{y}H{x + sx * 10}", 4.6)
    return fit_b(out + circle(32, 30, 9, I) + circle(32, 30, 3.6, H), 0.59)

@reg("com.vba_m.visualboyadvance-m", PURPLE_LIGHT)
def visualboyadvancem():
    return fit_b(rrect(5, 14, 54, 32, 12, I) + rrect(21, 19, 22, 17, 2.4, H) + line(9, 30, 17, 30, H, 3.4) + line(13, 26, 13, 34, H, 3.4)
               + circle(48, 32, 2.8, H) + circle(53, 27, 2.8, H), 0.71)

@reg("com.vesc_project.VescTool", INDIGO_SOFT)
def vesctool():
    return fit_b(ring_d(32, 30, 21, 4.6) + poly([(36, 14), (24, 32), (31, 32), (28, 46), (40, 27), (33, 27)], I, 1.4), 0.84)

@reg("com.vicr123.thebeat", BLUE_GREY)
def thebeat():
    return fit_b(poly([(23, 8), (41, 8), (49, 52), (15, 52)], I, 3) + line(32, 45, 39, 16, H, 3) + rrect(34.5, 22, 9, 5.5, 1.6, H)
               + line(21, 46, 43, 46, H, 2.4), 0.67)

@reg("com.voxdsp.AstroImpact", LIGHT_BLUE_DARK)
def astroimpact():
    rock = poly([(16, 26), (26, 20), (36, 24), (40, 34), (38, 44), (28, 50), (18, 46), (12, 36)], I, 2.4)
    return fit_b(rock + circle(23, 32, 3, H) + circle(32, 38, 4, H) + circle(24, 42, 2, H)
               + line(41, 22, 56, 7, I, 3.4) + line(46, 31, 58, 19, I, 3), 0.56)

@reg("com.voxdsp.Borg", DEEP_ORANGE_DARK)
def borg():
    out = rrect(9, 9, 46, 46, 4, I) + circle(32, 32, 12, H) + circle(32, 32, 5.5, I)
    for x, y in ((14, 14), (44, 14), (14, 44), (44, 44)):
        out += rrect(x, y, 6, 6, 1.4, H)
    return fit_b(out, 0.61)

@reg("com.voxdsp.Borg0", DEEP_PURPLE_LIGHT)
def borg0():
    return fit_b(path("M32 9L52 20V42L32 53L12 42V20Z", I, f' stroke="{I}" stroke-width="2.4" stroke-linejoin="round"')
               + ell(32, 31, 8, 13, H) + ell(32, 31, 3.4, 8, I), 0.8)

@reg("com.voxdsp.CubeShooter", BLUE_SOFT)
def cubeshooter():
    return fit_b(ring_d(32, 30, 16, 4) + line(32, 7, 32, 19, I, 4) + line(32, 41, 32, 53, I, 4) + line(9, 30, 21, 30, I, 4) + line(43, 30, 55, 30, I, 4)
               + rrect(27.5, 25.5, 9, 9, 1.8, I), 0.79)

@reg("com.voxdsp.PacGal", RED)
def pacgal():
    return fit_b(path("M28 31L45 19A21 21 0 1 0 45 43Z", I) + circle(26, 20, 3, H)
               + poly([(24, 11), (14, 5), (14, 17)], I, 1.2) + poly([(24, 11), (34, 5), (34, 17)], I, 1.2)
               + circle(54, 31, 3.4, I), 0.62)

@reg("com.voxdsp.PoryDrive", CYAN)
def porydrive():
    return fit_b(rrect(8, 14, 48, 36, 7, I) + ring_d(27, 28, 9, 3, H) + circle(27, 28, 2.4, H) + line(40, 19, 36, 27, H, 3)
               + line(15, 43, 34, 43, H, 3.2) + circle(47, 43, 2.8, H), 0.69)

@reg("com.voxdsp.SeriousShooter", BROWN)
def seriousshooter():
    return fit_b(rrect(8, 14, 48, 14, 3.4, I) + rrect(14, 26, 28, 7, 2, I) + path("M32 28H45L50 54H37Z", I)
               + ink_stroke("M20 32V39H31", 3.2) + circle(11, 21, 2, H) + line(48, 17, 48, 24, H, 2.6), 0.66)

@reg("com.voxdsp.Snowboarder", INDIGO_DEEP)
def snowboarder():
    board = g(rrect(-27, -6.5, 54, 13, 6.5, I) + rrect(-13, -6.5, 7, 13, 1.2, H) + rrect(6, -6.5, 7, 13, 1.2, H), "translate(33 33) rotate(-35)")
    return fit_b(board + star4(15, 13, 7) + star4(50, 50, 4.4), 0.64)

@reg("com.voxdsp.Snowling", AMBER_DARK)
def snowling():
    return fit_b(circle(32, 41, 14.5, I) + circle(32, 20, 10, I, f' stroke="{H}" stroke-width="2.6"') + circle(28.6, 18.6, 2, H) + circle(35.4, 18.6, 2, H)
               + poly([(32, 21), (32, 25), (38.5, 23.4)], H, .8) + circle(32, 38, 2, H) + circle(32, 45, 2, H)
               + ink_stroke("M18 36L8 29M46 36L56 29", 3.2), 0.76)

@reg("com.voxdsp.Spaceminer", PINK_LIGHT)
def spaceminer():
    return fit_b(ink_stroke("M12 29C20 12 42 10 54 22", 7) + line(33, 16, 23, 53, I, 5.6) + star4(50, 44, 7) + star4(12, 46, 4.4), 0.67)

@reg("com.voxdsp.TempleDriver", TEAL)
def templedriver():
    out = poly([(6, 22), (32, 7), (58, 22)], I, 2) + rrect(9, 24, 46, 5, 1.4, I) + rrect(8, 48, 48, 6, 1.8, I)
    for x in (13, 29, 45):
        out += rrect(x, 31, 6, 15, 1.2, I)
    return fit_b(out, 0.59)

@reg("com.voxdsp.TheCatrooms", GREY)
def thecatrooms():
    return fit_b(circle(32, 35, 17, I) + poly([(15, 27), (16, 8), (30, 21)], I, 2.4) + poly([(49, 27), (48, 8), (34, 21)], I, 2.4)
               + circle(25.5, 33, 2.8, H) + circle(38.5, 33, 2.8, H) + poly([(29.5, 39), (34.5, 39), (32, 42)], H, 1.2)
               + ink_stroke("M27 45Q32 49 37 45", 2.2, H), 0.69)

@reg("com.voxdsp.TuxFishing", BLUE)
def tuxfishing():
    return (fit_b(ink_stroke("M46 6V22A6.5 6.5 0 0 1 33 22", 3.4) + ell(31, 43, 17, 8.5) + poly([(15, 43), (5, 34), (5, 52)], I, 1.6)
                + circle(40, 41, 2, H) + ink_stroke("M26 40Q30 43 26 47", 2, H), 0.55))

@reg("com.voxdsp.TuxScape", ORANGE_DEEP)
def tuxscape():
    return fit_b(poly([(5, 50), (23, 20), (34, 36), (42, 25), (59, 50)], I, 2.4) + poly([(23, 20), (17.5, 29), (23, 26), (28.5, 28.5)], H, .8)
               + circle(48, 11, 6.5, I), 0.56)

@reg("com.voxdsp.TuxScape2", PURPLE_DEEP)
def tuxscape2():
    out = ""
    for cx, y0, s in ((19, 8, 1), (43, 14, 1.15)):
        out += poly([(cx, y0), (cx + 9 * s, y0 + 14 * s), (cx - 9 * s, y0 + 14 * s)], I, 2)
        out += poly([(cx, y0 + 8 * s), (cx + 11 * s, y0 + 26 * s), (cx - 11 * s, y0 + 26 * s)], I, 2)
        out += rrect(cx - 2, y0 + 25 * s, 4, 8 * s, 1, I)
    return fit_b(out + line(6, 52, 58, 52, I, 3.6), 0.55)

@reg("com.voxdsp.TuxVsDragon", PURPLE)
def tuxvsdragon():
    sword = (poly([(21, 5), (27, 11), (27, 36), (15, 36), (15, 11)], I, 1.6) + rrect(8, 37, 26, 5, 2.5, I)
             + line(21, 42, 21, 51, I, 5) + circle(21, 54, 3, I))
    flame = g(path("M32 7C34 18 47 22 47 36C47 46 41 53 32 53C23 53 17 46 17 36C17 29 21 25 24 20C26 27 28 28 30 26C32 22 28 14 32 7Z", I), "translate(33 20) scale(.62)")
    return fit_b(sword + flame, 0.57)

@reg("com.voxdsp.Tuxocide", BLUE_GREY_DARK)
def tuxocide():
    return fit_b(circle(28, 37, 17, I) + circle(21, 30, 3.6, H) + g(rrect(-5, -4, 10, 8, 1.8, I), "translate(40 22) rotate(42)")
               + ink_stroke("M44 19Q50 12 55 15", 3.4) + star4(56, 9, 6.4), 0.53)

@reg("com.voxdsp.VoxelPaint", LIGHT_BLUE)
def voxelpaint():
    return fit_b(iso(42, 40, 11) + iso(21, 40, 11) + iso(21, 29, 11), 0.75)

@reg("com.voxdsp.VoxelPaintPro", DEEP_ORANGE)
def voxelpaintpro():
    return fit_b(iso(27, 33, 17) + star4(49, 13, 8) + circle(52, 36, 2.6, I), 0.64)

@reg("com.voxdsp.aigeneratedgame", DEEP_PURPLE_DEEP)
def aigeneratedgame():
    return fit_b(rrect(7, 24, 50, 27, 13.5, I) + line(15, 38, 27, 38, H, 3.8) + line(21, 32, 21, 44, H, 3.8)
               + circle(43, 35, 3, H) + circle(50, 40, 3, H) + star4(47, 12, 8), 0.65)

@reg("com.w1hkj.fldigi", INDIGO_SOFT)
def fldigi():
    return fit_b(ink_stroke("M8 28H18L22 12L27 36L31 28H40L44 20L48 28H56", 3.8)
               + dim(rrect(9, 40, 12, 4.4, 2.2, I), .85) + dim(rrect(25, 40, 8, 4.4, 2.2, I), .85) + dim(rrect(37, 40, 18, 4.4, 2.2, I), .85)
               + dim(rrect(11, 48, 20, 4.4, 2.2, I), .5) + dim(rrect(36, 48, 14, 4.4, 2.2, I), .5), 0.66)

@reg("com.w1hkj.flrig", RED_DEEP)
def flrig():
    return fit_b(rrect(7, 22, 50, 29, 5, I) + ink_stroke("M46 22L51 8", 3.2) + rrect(12, 27, 20, 10, 2, H)
               + circle(45, 36, 7, H) + circle(45, 36, 2.6, I) + line(13, 44, 31, 44, H, 2.4), 0.64)

@reg("com.warlordsoftwares.formatlab", CYAN)
def formatlab():
    out = ""
    for a0, a1 in ((200, 335), (20, 155)):
        x0, y0 = pt(32, 30, 17, a0)
        x1, y1 = pt(32, 30, 17, a1)
        out += ink_stroke(f"M{f(x0)} {f(y0)}A17 17 0 0 1 {f(x1)} {f(y1)}", 5)
        r = math.radians(a1)
        out += arrowhead(x1, y1, -math.sin(r), math.cos(r), 7.5)
    return fit_b(out, 0.8)

@reg("com.warlordsoftwares.jpeg2pdf", BROWN_DARK)
def jpeg2pdf():
    return fit_b(rrect(4, 17, 24, 20, 3.4, I) + poly([(7, 34), (13, 25), (17, 30), (20, 27), (25, 34)], H, 1) + circle(22, 22, 2, H)
               + ink_stroke("M31 27H39M35.5 22.5L40 27L35.5 31.5", 3.2) + path("M43 12H53L59 18V43H43Z", I)
               + line(47, 26, 55, 26, H, 2.2) + line(47, 32, 55, 32, H, 2.2), 0.66)

@reg("com.wireframesketcher.WireframeSketcher", INDIGO)
def wireframesketcher():
    return fit_b(rrect(9, 11, 46, 38, 5, "none", f' stroke="{I}" stroke-width="3.6"') + line(9, 21, 55, 21, I, 3.4)
               + ink_stroke("M16 27L32 43M32 27L16 43", 2.8) + line(38, 30, 49, 30, I, 3.2) + line(38, 38, 46, 38, I, 3.2), 0.66)

@reg("com.wonderlandengine.editor", AMBER_DEEP)
def wonderlandeditor():
    return fit_b(rrect(7, 16, 50, 28, 10, I) + circle(21.5, 30, 7.4, H) + circle(42.5, 30, 7.4, H) + circle(21.5, 30, 3, I) + circle(42.5, 30, 3, I)
               + path("M27 44Q32 35 37 44Z", H) + ink_stroke("M18 16Q32 6 46 16", 3.2), 0.77)

@reg("com.writerduet.writersolo", PINK_DEEP)
def writersolo():
    return fit_b(path("M47 7C31 10 22 22 18 39L13 51L23 45C36 41 46 29 48 14Z", I) + ink_stroke("M18 46L41 17", 2.4, H)
               + line(25, 54, 53, 54, I, 3.4), 0.58)

@reg("com.xiaoyaocz.simple_live", TEAL_DEEP)
def simplelive():
    return fit_b(rrect(7, 10, 50, 34, 6, I) + poly([(26, 19), (26, 35), (40, 27)], H, 1.6) + circle(48, 18, 3, H)
               + line(32, 44, 32, 50, I, 3.6) + line(20, 52, 44, 52, I, 4), 0.66)

@reg("com.xunlei.Thunder", GREY_LIGHT)
def thunder():
    return fit_b(poly([(39, 6), (16, 35), (29, 35), (23, 55), (48, 24), (34, 24)], I, 2.4), 0.71)

@reg("com.yutovo.yutovo", BLUE)
def yutovo():
    bar = g(rrect(-25, -5.5, 50, 11, 2.6, I, f' stroke="{H}" stroke-width="2.2"')
            + "".join(line(x, -5.5, x + 5, 5.5, H, 3.2, "butt") for x in (-17, -5, 7, 19)), "translate(32 17) rotate(-11)")
    return fit_b(rrect(9, 25, 46, 28, 4, I) + bar + poly([(27, 32), (27, 47), (40, 39.5)], H, 1.6), 0.61)

@reg("com.zerobrane.studio", ORANGE_DARK)
def zerobranestudio():
    return fit_b(ink_stroke("M21 15L7 30L21 45", 5.8) + ink_stroke("M43 15L57 30L43 45", 5.8) + line(37, 13, 27, 47, I, 5), 0.7)

@reg("com.zoho.Notebook", PURPLE_DARK)
def zohonotebook():
    return fit_b(rrect(13, 7, 38, 46, 4.4, I) + line(20.5, 7, 20.5, 53, H, 2.6) + poly([(38, 7), (38, 24), (43.5, 19), (49, 24), (49, 7)], H, 0)
               + line(27, 33, 43, 33, H, 3) + line(27, 40, 39, 40, H, 3), 0.7)

@reg("com.zquestclassic.ZQuest", ORANGE_DARK)
def zquest():
    return fit_b(ring_d(21, 21, 10, 5.2) + line(28, 28, 52, 52, I, 5.4) + line(41, 41, 47, 35, I, 4.4) + line(48, 48, 54, 42, I, 4.4), 0.6)

@reg("community.pathofbuilding.PathOfBuilding", BLUE_GREY_DEEP)
def pathofbuilding():
    out = ring_d(32, 30, 18, 2.8)
    for a in range(-90, 270, 72):
        x, y = pt(32, 30, 18, a)
        out += line(32, 30, x, y, I, 3.2) + circle(x, y, 4.6, I)
    return fit_b(out + circle(32, 30, 7, I) + circle(32, 30, 2.6, H), 0.87)

@reg("cool.ldr.lfy", LIGHT_BLUE_LIGHT)
def lfy():
    return fit_b(rrect(6, 8, 30, 23, 6.4, I) + poly([(12, 30), (12, 40), (23, 30)], I, 1) + ink_stroke("M14 25L21 13L28 25M16.6 21H25.4", 2.8, H)
               + rrect(28, 24, 30, 23, 6.4, I, f' stroke="{H}" stroke-width="2.8"') + poly([(52, 46), (52, 55), (42, 46)], I, 1)
               + line(34, 32, 52, 32, H, 2.8) + line(34, 39, 46, 39, H, 2.8), 0.6)

@reg("cx.modal.TestCenter", DEEP_ORANGE_LIGHT)
def testcenter():
    return fit_b(path("M25 11H39V24L51 47Q53 53 47 53H17Q11 53 13 47L25 24Z", I) + rrect(22, 7, 20, 5, 2.5, I)
               + path("M19 39H45L48 46Q49 48 47 48H17Q15 48 16 46Z", H) + circle(28, 43, 2, I) + circle(36, 45, 1.7, I)
               + circle(33, 33, 2.2, H), 0.68)

@reg("cz.bugsy.roster", DEEP_PURPLE)
def roster():
    out = ""
    for k, y in enumerate((14, 30, 46)):
        out += circle(16, y, 6, I) + rrect(27, y - 5, 28, 10, 3, I, f' opacity="{(1, .7, .45)[k]}"')
    return fit_b(out, 0.66)

@reg("cz.cvut.edu.comparch.qtrvsim", ORANGE)
def qtrvsim():
    out = ""
    for k in range(4):
        out += rrect(8 + k * 8, 8 + k * 12, 24, 9, 2.6, I, f' opacity="{(1, .85, .7, .55)[k]}"')
    return fit_b(out + ink_stroke("M38 14H50V22", 2.6) + ink_stroke("M46 18L50 22L54 18", 2.6), 0.61)

@reg("cz.krupkat.Xpano", RED_DARK)
def xpano():
    return fit_b(rrect(5, 8, 54, 28, 5, I) + poly([(8, 33), (19, 20), (26, 28), (36, 16), (46, 29), (51, 24), (56, 33)], H, 1)
               + ink_stroke("M13 47H51M19 42L13 47L19 52M45 42L51 47L45 52", 3.2), 0.6)

@reg("cz.nic.mobile-datovka", CYAN_DEEP)
def mobiledatovka():
    return fit_b(rrect(16, 5, 32, 50, 6, I) + rrect(20, 12, 24, 31, 2.4, H) + rrect(23, 22, 18, 13, 2.2, I) + ink_stroke("M24 23.5L32 30L40 23.5", 2, H) + circle(32, 49, 2.4, H), 0.71)

@reg("cz.ondrejkolin.Barcoder", BROWN_LIGHT)
def barcoder():
    out = ""
    for x, w in ((8, 3), (14, 6), (24, 2.5), (30, 5), (39, 2.5), (45, 6), (54, 2.5)):
        out += rrect(x, 14, w, 32, .8, I)
    return fit_b(out + line(4, 30, 60, 30, H, 2.6, "butt"), 0.68)

@reg("cz.zeropage.Formiko", INDIGO_LIGHT)
def formiko():
    legs = ink_stroke("M26 30L16 16M30 29L30 12M34 30L44 16M26 34L16 48M30 35L30 52M34 34L44 48", 3.2)
    return fit_b(legs + g(ell(0, 0, 11, 8), "translate(49 31) rotate(8)") + ell(30, 32, 6.5, 5.5) + circle(17, 31, 6, I)
               + ink_stroke("M14 27L7 20M19 26L20 18", 2.6), 0.69)

@reg("de._0x539.gobby", AMBER_LIGHT)
def gobby():
    return fit_b(rrect(7, 8, 38, 48, 4.4, I) + line(14, 18, 36, 18, H, 3.2) + line(14, 27, 38, 27, H, 3.2) + line(14, 36, 30, 36, H, 3.2) + line(14, 45, 34, 45, H, 3.2)
               + ink_stroke("M53 15V43M48 15H58M48 43H58", 3.4), 0.57)

@reg("de.akaflieg_freiburg.cavok.add_hours_and_minutes", PINK)
def addhoursandminutes():
    return fit_b(ring_d(27, 34, 18, 4.6) + ink_stroke("M27 22V34L35 39", 3.8) + circle(46, 15, 10, I, f' stroke="{H}" stroke-width="2.6"')
               + line(46, 9.5, 46, 20.5, H, 3.2) + line(40.5, 15, 51.5, 15, H, 3.2), 0.64)

@reg("de.akaflieg_freiburg.enroute", TEAL)
def enroute():
    plane = (rrect(29, 6, 6, 46, 3, I) + poly([(32, 20), (57, 38), (57, 43), (32, 35), (7, 43), (7, 38)], I, 1.6)
             + poly([(32, 44), (43, 53), (43, 56), (32, 52), (21, 56), (21, 53)], I, 1.2))
    return fit_b(g(plane, "rotate(38 32 30)"), 0.68)

@reg("de.berny23.virtual_surround_manager", GREY_DARK)
def virtualsurroundmanager():
    orbit = '<ellipse cx="32" cy="30" rx="25" ry="10" fill="none" stroke="INK" stroke-width="3"/>'
    st = f' stroke="{H}" stroke-width="2.6" stroke-linejoin="round"'
    return fit_b(orbit + circle(7, 30, 4.6, I) + circle(57, 30, 4.6, I) + circle(32, 23, 7.4, I, st) + path("M19 47Q19 35 32 35Q45 35 45 47Z", I, st), 0.66)

@reg("de.bforartists.Bforartists", BLUE_DARK)
def bforartists():
    out = circle(30, 33, 5.4, I)
    for x, y in ((30, 8), (52, 46), (8, 46)):
        out += line(30, 33, x, y, I, 3.6) + circle(x, y, 5, I)
    return fit_b(out + circle(30, 33, 2, H), 0.58)

@reg("de.billance.billance", ORANGE_LIGHT)
def billance():
    return fit_b(line(32, 12, 32, 48, I, 4) + line(12, 18, 52, 18, I, 4) + circle(32, 11, 4, I) + rrect(21, 48, 22, 5.5, 2.6, I)
               + ink_stroke("M12 20L6 36M12 20L18 36M52 20L46 36M52 20L58 36", 2.2) + path("M3 36H21A9 9 0 0 1 3 36Z", I) + path("M43 36H61A9 9 0 0 1 43 36Z", I), 0.65)

@reg("de.breitbandmessung.Breitbandmessung", PURPLE_LIGHT)
def breitbandmessung():
    return fit_b(ink_stroke("M13 47A22 22 0 1 1 51 47", 5.4) + line(32, 36, 44, 19, I, 4.4) + circle(32, 36, 5, I) + line(13, 52, 51, 52, I, 3.6), 0.63)

@reg("de.bund.ausweisapp.ausweisapp2", BLUE_LIGHT)
def ausweisapp2():
    return fit_b(rrect(6, 12, 52, 38, 5.4, I) + circle(20, 28, 5.4, H) + path("M11 42Q11 34 20 34Q29 34 29 42Z", H)
               + line(36, 24, 51, 24, H, 3.2) + line(36, 31, 51, 31, H, 3.2) + line(36, 38, 46, 38, H, 3.2), 0.64)

@reg("de.capypara.FieldMonitor", BLUE_GREY)
def fieldmonitor():
    return fit_b(rrect(7, 7, 50, 35, 5.4, I) + rrect(12, 12, 40, 25, 2.4, H)
               + poly([(25, 17), (25, 33), (30, 29), (34, 36), (38, 34), (34, 27), (40, 26)], I, 1.2)
               + rrect(28, 42, 8, 6, 1, I) + rrect(19, 48, 26, 5, 2.5, I), 0.62)

@reg("de.danielnoethen.butt", LIGHT_BLUE)
def butt():
    return fit_b(rrect(23, 6, 18, 28, 9, I) + line(23, 15, 41, 15, H, 2.2) + line(23, 22, 41, 22, H, 2.2)
               + ink_stroke("M15 26C15 46 49 46 49 26", 4.4) + line(32, 41, 32, 51, I, 4.2) + line(21, 53, 43, 53, I, 4.4), 0.71)

@reg("de.desy.constellation", DEEP_ORANGE_DEEP)
def constellation():
    pts = [(12, 42), (24, 22), (40, 34), (52, 12), (36, 52)]
    out = ink_stroke("M12 42L24 22L40 34L52 12M40 34L36 52", 2.8)
    return fit_b(out + star4(24, 22, 9) + star4(52, 12, 8) + circle(12, 42, 3.8, I) + circle(40, 34, 4.2, I) + circle(36, 52, 3.8, I), 0.59)
