# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 104: the nineteenth hundred apps from the gap list (flags/app-gap-list-full.md),
rows 1801 to 1900, MathHurdler to AntiBillard. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import (
    arrowhead, asterisk, bubble, dim, ell, ellring, fit, H, hexring, hx, I, ink_circle,
    ink_path, ink_stroke, petal_b, registry, ring_c, rl, rot, star4, star5,
)

ICONS, SMALL, reg, _ = registry()

def tee(x, y, w=20, t=5):
    return rl(x, y, w, t, 1.5, H) + rl(x + (w - t) / 2, y, t, w + 2, 1.5, H)

def burst(cx, cy, r0, r1, n):
    return poly([pt(cx, cy, r1 if k % 2 == 0 else r0, -90 + 180 / n * k) for k in range(2 * n)], I, 2)

@reg("org.sugarlabs.MathHurdler", DEEP_PURPLE)
def i1801():
    out = rl(6, 36, 52, 6, 3) + rl(10, 36, 6, 22, 2) + rl(48, 36, 6, 22, 2) + ink_stroke("M32 6V24M23 15H41", 5)
    return fit(out, 0.599, 32.0, 30.8)

@reg("org.sugarlabs.Maze", LIGHT_BLUE_DEEP)
def i1802():
    out = ink_stroke("M8 56V8H56V56H24V24H40V40", 5)
    return fit(out, 0.563, 32.0, 32.0)

@reg("org.sugarlabs.Measure", GREY)
def i1803():
    out = rot(rl(2, 20, 60, 24, 5) + "".join(rl(10 + 11 * k, 20, 4.4, 10 if k % 2 else 15, 0, H) for k in range(5)), -20, 32, 32)
    return fit(out, 0.581, 32.0, 32.0)

@reg("org.sugarlabs.Memorize", BLUE_DEEP)
def i1804():
    out = rl(4, 14, 25, 36, 5) + rl(35, 14, 25, 36, 5) + ink_circle(16.5, 32, 6, H) + poly([(47.5, 24), (54, 32), (47.5, 40), (41, 32)], H, 1.5)
    return fit(out, 0.643, 32.0, 32.0)

@reg("org.sugarlabs.MusicBlocks", YELLOW_DARK)
def i1805():
    out = rl(6, 36, 24, 20, 3) + rl(34, 36, 24, 20, 3) + rl(20, 12, 24, 20, 3) + ink_circle(29, 26, 3.6, H) + ink_stroke("M32 26V16", 2.6, H)
    return fit(out, 0.624, 32.0, 34.0)

@reg("org.sugarlabs.MusicKeyboard", RED)
def i1806():
    out = rl(4, 12, 56, 40, 5) + "".join(rl(x, 12, 2.6, 40, 0, H) for x in (18.7, 31.3, 44)) + rl(13, 12, 11, 24, 2, H) + rl(40, 12, 11, 24, 2, H)
    return fit(out, 0.631, 32.0, 32.0)

@reg("org.sugarlabs.Paint", CYAN_DARK)
def i1807():
    out = rot(rl(28, 4, 8, 26, 3) + rl(26, 30, 12, 8, 1) + ink_path("M26 40H38Q40 52 32 58Q24 52 26 40Z"), 30, 32, 32)
    return fit(out, 0.742, 33.0, 30.6)

@reg("org.sugarlabs.Physics", ORANGE_DEEP)
def i1808():
    out = "".join(rot(ellring(32, 32, 27, 11, 4.6), a, 32, 32) for a in (0, 60, 120)) + ink_circle(32, 32, 7)
    return fit(out, 0.61, 32.0, 32.0)

@reg("org.sugarlabs.Pippy", PURPLE)
def i1809():
    out = ink_stroke("M44 12H24Q12 12 12 22T24 32H40Q52 32 52 42T40 52H16", 7) + ink_circle(46, 12, 3, H)
    return fit(out, 0.702, 32.0, 32.0)

@reg("org.sugarlabs.Pukllanapac", BLUE_GREY)
def i1810():
    out = rl(8, 20, 48, 8, 4) + poly([(14, 28), (50, 28), (32, 58)], I, 5) + rl(29.5, 6, 5, 14, 2)
    return fit(out, 0.661, 32.0, 33.2)

@reg("org.sugarlabs.ReadETexts", BROWN)
def i1811():
    out = ink_path("M32 18Q20 10 4 14V50Q20 46 32 54Z") + ink_path("M32 18Q44 10 60 14V50Q44 46 32 54Z") + ink_stroke("M12 24Q20 24 26 27M12 33Q20 33 26 36", 2.4, H) + ink_stroke("M52 24Q44 24 38 27M52 33Q44 33 38 36", 2.4, H)
    return fit(out, 0.604, 32.0, 33.2)

@reg("org.sugarlabs.Sliderule", INDIGO_DEEP)
def i1812():
    out = rl(4, 16, 56, 32, 5) + rl(8, 27, 48, 10, 2, H) + rl(20, 24, 22, 16, 2) + rl(34, 16, 2.6, 32, 0, H)
    return fit(out, 0.643, 32.0, 32.0)

@reg("org.sugarlabs.SolarSystem", YELLOW_DARK)
def i1813():
    out = ink_circle(32, 32, 9) + ring_c(32, 32, 21, 3.6) + ink_circle(53, 32, 5.5) + ink_circle(17, 17, 4.4)
    return fit(out, 0.727, 33.8, 32.0)

@reg("org.sugarlabs.Speak", BLUE_GREY)
def i1814():
    out = bubble(4, 8, 56, 36) + ink_circle(22, 24, 3.4, H) + ink_circle(42, 24, 3.4, H) + ink_stroke("M22 33Q32 40 42 33", 3, H)
    return fit(out, 0.621, 32.0, 30.9)

@reg("org.sugarlabs.StoryActivity", LIGHT_BLUE_DARK)
def i1815():
    out = ink_path("M12 6H38L54 22V58H12Z") + ink_path("M38 6V22H54Z", H) + ink_stroke("M20 34H46M20 43H46M20 52H34", 3, H)
    return fit(out, 0.617, 33.0, 32.0)

@reg("org.sugarlabs.SwiftFeet", AMBER_DEEP)
def i1816():
    out = ink_path("M8 42Q8 32 16 30L24 12L34 16L30 26Q44 28 52 38Q60 40 60 48V50H8Z") + ink_stroke("M4 58H60", 4)
    return fit(out, 0.545, 32.0, 36.0)

@reg("org.sugarlabs.TurtlePondActivity", PINK)
def i1817():
    out = ell(32, 36, 16, 18) + ink_circle(32, 10, 6.5) + ell(13, 24, 5, 8) + ell(51, 24, 5, 8) + ell(14, 50, 5, 7) + ell(50, 50, 5, 7) + poly([(28, 56), (36, 56), (32, 63)], I, 1) + hx(32, 36, 7, -90, H, 1)
    return fit(out, 0.6, 32.0, 33.5)

@reg("org.sugarlabs.TypingTurtle", TEAL_DEEP)
def i1818():
    out = rl(6, 8, 52, 48, 11) + tee(21, 20, 22, 6)
    return fit(out, 0.663, 32.0, 32.0)

@reg("org.sugarlabs.Words", DEEP_ORANGE)
def i1819():
    out = ink_stroke("M6 12L18 52L32 24L46 52L58 12", 7)
    return fit(out, 0.564, 32.0, 32.0)

@reg("org.surge_synth_team.surge-xt", DEEP_PURPLE_DEEP)
def i1820():
    out = ink_stroke("M4 46L20 16V46L36 16V46L52 16V46", 5.5) + ink_stroke("M54 46H60", 5.5)
    return fit(out, 0.585, 32.0, 31.0)

@reg("org.svxlink.Qtel", DEEP_PURPLE_SOFT)
def i1821():
    out = rl(6, 24, 52, 34, 7) + ink_stroke("M44 24L54 4", 4.4) + ink_circle(21, 41, 9, H) + ink_stroke("M38 33H50M38 41H50M38 49H50", 3, H)
    return fit(out, 0.568, 32.0, 29.9)

@reg("org.swi_prolog.swipl", GREY)
def i1822():
    out = ink_circle(14, 22, 5) + ink_circle(14, 42, 5) + rl(28, 29, 32, 7, 3.5)
    return fit(out, 0.706, 34.5, 32.0)

@reg("org.syntalos.syntalos", BLUE_DARK)
def i1823():
    out = ink_path("M24 6H40V22L56 52Q58 60 50 60H14Q6 60 8 52L24 22Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"') + ink_stroke("M14 44H50", 3, H) + ink_circle(30, 52, 2.6, H) + ink_circle(40, 34, 2.4, H)
    return fit(out, 0.579, 32.0, 33.0)

@reg("org.tabos.bloodpressure", YELLOW_DARK)
def i1824():
    out = ink_path("M32 58C4 38 4 12 20 10C27 10 31 14 32 19C33 14 37 10 44 10C60 12 60 38 32 58Z") + ink_stroke("M12 32H24L28 22L35 42L39 32H52", 3.2, H)
    return fit(out, 0.727, 32.0, 34.0)

@reg("org.tabos.roger", RED)
def i1825():
    out = rl(16, 20, 30, 42, 7) + rl(35, 4, 6, 18, 2.5) + ink_stroke("M25 32H37M25 39H37M25 46H37", 2.8, H) + ink_stroke("M52 24Q58 32 52 40", 3.4) 
    return fit(out, 0.621, 36.4, 33.0)

@reg("org.tabos.saldo", CYAN_DEEP)
def i1826():
    out = rl(10, 8, 36, 12, 3) + rl(4, 16, 56, 40, 9) + rl(38, 29, 22, 14, 6, H) + ink_circle(47, 36, 3)
    return fit(out, 0.616, 32.0, 32.0)

@reg("org.temple.Bible", ORANGE_DEEP)
def i1827():
    out = rl(12, 4, 40, 56, 5) + rl(30, 14, 4, 28, 1.5, H) + rl(22, 21, 20, 4, 1.5, H) + rl(12, 50, 40, 3, 0, H)
    return fit(out, 0.631, 32.0, 32.0)

@reg("org.texmacs.TeXmacs", PURPLE_DEEP)
def i1828():
    out = rl(4, 12, 28, 7, 2) + rl(14.5, 12, 7, 36, 2) + rl(36, 24, 7, 36, 2) + rl(36, 24, 24, 7, 2) + rl(36, 38, 18, 7, 2) + rl(36, 53, 24, 7, 2)
    return fit(out, 0.569, 32.0, 36.0)

@reg("org.thentrythis.Samplebrain", GREY)
def i1829():
    hs2 = ' stroke="HOLE" stroke-width="2.4"'
    out = ink_circle(22, 24, 13, I, hs2) + ink_circle(42, 24, 13, I, hs2) + ink_circle(18, 40, 11, I, hs2) + ink_circle(46, 40, 11, I, hs2) + rl(24, 34, 16, 24, 6) + ink_stroke("M32 14V52", 2.6, H) + ink_stroke("M12 38H22L26 30L30 44", 2.6, H)
    return fit(out, 0.72, 32.0, 34.5)

@reg("org.tibirna.qgit", BROWN)
def i1830():
    out = ink_stroke("M16 18V46M46 28Q46 44 22 46", 4.4) + ink_circle(16, 12, 7) + ink_circle(16, 52, 7) + ink_circle(46, 22, 7)
    return fit(out, 0.64, 31.0, 32.0)

@reg("org.tildearrow.furnace", INDIGO_DARK)
def i1831():
    out = ink_path("M32 2Q38 18 48 28Q58 40 50 52Q44 60 32 60Q20 60 14 52Q6 40 20 26Q20 36 28 36Q22 18 32 2Z") + ink_path("M32 58Q24 58 24 50Q24 42 32 34Q40 42 40 50Q40 58 32 58Z", H)
    return fit(out, 0.621, 32.4, 31.0)

@reg("org.trelby.Trelby", YELLOW_DARK)
def i1832():
    out = rl(6, 26, 52, 32, 4) + rot(rl(6, 10, 52, 11, 2), -9, 6, 21) + "".join(rot(rl(x, 10, 6, 11, 0, H), -9, 6, 21) for x in (16, 30, 44)) + ink_stroke("M14 40H50M14 49H38", 3, H)
    return fit(out, 0.553, 31.2, 30.1)

@reg("org.triliumnotes.Trilium", BLUE_GREY)
def i1833():
    out = "".join(petal_b(32, 36, 26, 11, a) for a in (-90, 30, 150)) + ink_circle(32, 36, 5, H)
    return fit(out, 0.696, 32.0, 29.8)

@reg("org.tropy.Tropy", LIGHT_BLUE_DEEP)
def i1834():
    out = ink_path("M16 6H48V24Q48 38 32 40Q16 38 16 24Z") + ink_stroke("M16 12H8Q6 28 18 30M48 12H56Q58 28 46 30", 3.6) + rl(29, 40, 6, 10, 1) + rl(18, 50, 28, 8, 3)
    return fit(out, 0.62, 32.0, 32.0)

@reg("org.tryton.Tryton-70", AMBER_DEEP)
def i1835():
    out = hexring(32, 32, 26, 5) + tee(22, 22, 20, 5).replace(H, I)
    return fit(out, 0.632, 32.0, 32.0)

@reg("org.tryton.Tryton-78", PINK_DEEP)
def i1836():
    out = poly([(32, 6), (58, 18), (32, 30), (6, 18)], I, 2) + ink_stroke("M8 32L32 43L56 32M8 45L32 56L56 45", 4.4)
    return fit(out, 0.667, 32.0, 31.6)

@reg("org.tryton.Tryton-80", TEAL_LIGHT)
def i1837():
    out = poly([(32, 2), (62, 32), (32, 62), (2, 32)], I, 6) + tee(22, 22, 20, 5)
    return fit(out, 0.545, 32.0, 32.0)

@reg("org.tryton.Tryton-82", DEEP_ORANGE)
def i1838():
    out = rl(6, 6, 52, 52, 15) + tee(22, 20, 20, 5)
    return fit(out, 0.67, 32.0, 32.0)

@reg("org.tvbrowser.TVBrowser", DEEP_PURPLE_DARK)
def i1839():
    out = rl(4, 20, 56, 38, 8) + rl(10, 26, 33, 26, 3, H) + ink_circle(51, 33, 3.2, H) + ink_circle(51, 45, 3.2, H) + ink_stroke("M20 6L32 16L44 6", 3.6)
    return fit(out, 0.576, 32.0, 31.0)

@reg("org.twinery.Twine", AMBER_DARK)
def i1840():
    out = rl(4, 22, 18, 20, 5) + rl(42, 4, 18, 20, 5) + rl(42, 40, 18, 20, 5) + ink_stroke("M22 32Q32 32 42 14M22 32Q32 32 42 50", 3.4)
    return fit(out, 0.547, 32.0, 32.0)

@reg("org.ultimatepp.TheIDE", GREY)
def i1841():
    out = ink_stroke("M24 6Q16 6 16 14V24Q16 30 8 32Q16 34 16 40V50Q16 58 24 58M40 6Q48 6 48 14V24Q48 30 56 32Q48 34 48 40V50Q48 58 40 58", 4.4)
    return fit(out, 0.637, 32.0, 32.0)

@reg("org.unifiedpush.Troubleshooter", BLUE_DEEP)
def i1842():
    out = rot(rl(28, 24, 8, 38, 4) + ring_c(32, 17, 10, 7) + rl(28, 0, 8, 13, 0, H), 40, 32, 32)
    return fit(out, 0.657, 33.2, 31.5)

@reg("org.unofficialrevport.REVHubInterface", YELLOW_DARK)
def i1843():
    out = rl(4, 26, 56, 22, 6) + "".join(rl(10 + 12 * k, 33, 8, 8, 2, H) for k in range(4)) + ink_stroke("M32 26V10", 4.4) + ink_circle(32, 8, 4)
    return fit(out, 0.616, 32.0, 26.0)

@reg("org.upbge.UPBGE", RED_DEEP)
def i1844():
    out = rl(2, 20, 60, 32, 15) + rl(11, 32, 14, 4, 1.5, H) + rl(16, 27, 4, 14, 1.5, H) + ink_circle(44, 30, 3.2, H) + ink_circle(51, 37, 3.2, H)
    return fit(out, 0.6, 32.0, 36.0)

@reg("org.upnproutercontrol.UPnPRouterControl", CYAN)
def i1845():
    out = rl(4, 36, 56, 20, 6) + rl(12, 10, 5, 28, 2.5) + rl(47, 10, 5, 28, 2.5) + ink_circle(16, 46, 2.8, H) + ink_circle(26, 46, 2.8, H) + rl(38, 44, 16, 4, 2, H)
    return fit(out, 0.605, 32.0, 33.0)

@reg("org.v1993.NXDumpClient", ORANGE_DEEP)
def i1846():
    out = ink_stroke("M32 6V34", 5.5) + arrowhead(32, 28, 0, 1, 14) + ink_stroke("M8 40V56H56V40", 5)
    return fit(out, 0.551, 32.0, 30.9)

@reg("org.vanillaos.ApxGUI", PURPLE_DARK)
def i1847():
    out = rl(4, 10, 56, 12, 3) + rl(8, 26, 48, 32, 4) + rl(25, 32, 14, 5, 2.5, H)
    return fit(out, 0.575, 32.0, 34.0)

@reg("org.vassalengine.vassal", DEEP_PURPLE_LIGHT)
def i1848():
    out = hx(32, 32, 28, -90, I, 4) + rl(20, 20, 24, 24, 3, H) + star5(32, 32, 9)
    return fit(out, 0.6, 32.0, 32.0)

@reg("org.verapdf.veraPDF", BROWN)
def i1849():
    out = ink_path("M32 4L56 12V32Q56 50 32 60Q8 50 8 32V12Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"') + ink_stroke("M20 28H44M20 38H34", 5, H)
    return fit(out, 0.621, 32.0, 32.0)

@reg("org.vergecurrency.verge-qt", INDIGO_DEEP)
def i1850():
    out = ring_c(32, 32, 26, 5) + ink_stroke("M19 22L32 44L45 22", 5.5)
    return fit(out, 0.632, 32.0, 32.0)

@reg("org.vertcoin.vertcoin-qt", YELLOW_DARK)
def i1851():
    out = poly([(6, 10), (58, 10), (32, 58)], I, 6) + poly([(20, 22), (44, 22), (32, 42)], H, 2)
    return fit(out, 0.534, 32.0, 34.0)

@reg("org.virtualxt.VirtualXT", BLUE_GREY_DEEP)
def i1852():
    out = rl(10, 4, 44, 34, 5) + rl(16, 10, 32, 22, 2, H) + rl(4, 42, 56, 16, 4) + rl(34, 47, 18, 3.6, 1.5, H) + ink_circle(14, 50, 2.4, H)
    return fit(out, 0.55, 32.0, 31.0)

@reg("org.wfview.wfview", LIGHT_BLUE_LIGHT)
def i1853():
    out = "".join(rl(5 + 9.4 * k, 54 - h, 6.2, h, 2) for k, h in enumerate((14, 26, 18, 44, 30, 48)))
    return fit(out, 0.586, 31.6, 30.0)

@reg("org.xnec2c.Xnec2c", AMBER_DEEP)
def i1854():
    out = ink_stroke("M4 32H60", 3.6) + ink_stroke("M14 22V42", 4.4) + ink_stroke("M26 12V52", 4.4) + ink_stroke("M38 18V46", 4.4) + ink_stroke("M50 24V40", 4.4)
    return fit(out, 0.6, 32.0, 32.0)

@reg("org.yacas.yacas-gui", PINK_DARK)
def i1855():
    out = ink_stroke("M44 12Q38 6 34 14Q32 20 32 32Q32 44 30 50Q26 58 20 52", 5.5) + ink_circle(46, 12, 3.4) + ink_circle(18, 54, 3.4)
    return fit(out, 0.695, 32.0, 32.0)

@reg("org.yamagi.YamagiQ2", TEAL_DEEP)
def i1856():
    out = ring_c(28, 28, 20, 7) + ink_stroke("M38 40L56 58", 7.5)
    return fit(out, 0.537, 32.1, 33.1)

@reg("org.zdoom.Raze", DEEP_ORANGE)
def i1857():
    out = burst(32, 32, 14, 30, 8) + ink_circle(32, 32, 7, H)
    return fit(out, 0.581, 32.0, 32.0)

@reg("page.codeberg.DrRac27.Karoto", DEEP_PURPLE_DEEP)
def i1858():
    out = rot(poly([(22, 22), (42, 22), (32, 62)], I, 7), 28, 32, 40) + ell(32, 10, 4, 9) + rot(ell(32, 10, 4, 9), 38, 32, 18) + rot(ell(32, 10, 4, 9), -38, 32, 18)
    return fit(out, 0.581, 35.4, 32.0)

@reg("page.codeberg.Imaginer.Imaginer", LIGHT_BLUE_DEEP)
def i1859():
    out = star4(30, 34, 26) + star4(52, 12, 9) + star4(12, 54, 7)
    return fit(out, 0.574, 32.5, 32.0)

@reg("page.codeberg.JakobDev.CCLite", GREY_DEEP)
def i1860():
    out = ink_stroke("M26 18A15 15 0 1 0 26 46", 6.5) + ink_stroke("M54 18A15 15 0 1 0 54 46", 6.5)
    return fit(out, 0.655, 29.8, 32.0)

@reg("page.codeberg.JakobDev.jdAnimatedImageEditor", BLUE_LIGHT)
def i1861():
    out = rl(8, 4, 48, 56, 6) + "".join(rl(x, y, 5, 6, 1.4, H) for x in (12, 47) for y in (10, 22, 34, 46)) + rl(21, 14, 22, 36, 3, H)
    return fit(out, 0.594, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdAppStreamEdit", YELLOW_DARK)
def i1862():
    out = ink_stroke("M20 16L6 32L20 48M44 16L58 32L44 48M37 10L27 54", 5)
    return fit(out, 0.632, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdDBusDebugger", RED_DARK)
def i1863():
    out = rl(8, 6, 48, 44, 10) + rl(14, 13, 36, 16, 3, H) + ink_circle(18, 39, 3.4, H) + ink_circle(46, 39, 3.4, H) + rl(12, 50, 10, 10, 3) + rl(42, 50, 10, 10, 3)
    return fit(out, 0.632, 32.0, 33.0)

@reg("page.codeberg.JakobDev.jdDesktopEntryEdit", CYAN_DEEP)
def i1864():
    out = rl(4, 10, 56, 44, 7) + ink_stroke("M4 24H60", 2.8, H) + ink_circle(13, 17, 2.4, H) + ink_circle(21, 17, 2.4, H) + rl(12, 32, 18, 14, 2, H) + ink_stroke("M38 34H52M38 42H48", 3, H)
    return fit(out, 0.624, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdDiff", ORANGE_DEEP)
def i1865():
    out = rl(4, 8, 26, 48, 5) + rl(34, 8, 26, 48, 5) + rl(10, 30, 14, 4, 1, H) + rl(40, 30, 14, 4, 1, H) + rl(45, 25, 4, 14, 1, H)
    return fit(out, 0.588, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdEolConverter", PURPLE_DEEP)
def i1866():
    out = ink_stroke("M52 8V34H22", 5.5) + arrowhead(22, 34, -1, 0, 15) + ink_stroke("M10 52H54", 4)
    return fit(out, 0.604, 31.1, 29.6)

@reg("page.codeberg.JakobDev.jdFlatpakSnapshot", ORANGE_DEEP)
def i1867():
    out = rl(4, 18, 56, 40, 8) + rl(20, 8, 24, 12, 4) + ink_circle(32, 38, 12, H) + ink_circle(32, 38, 6.5)
    return fit(out, 0.598, 32.0, 33.0)

@reg("page.codeberg.JakobDev.jdMacroPlayer", BROWN_DEEP)
def i1868():
    out = ink_circle(14, 32, 9) + poly([(32, 10), (32, 54), (60, 32)], I, 5)
    return fit(out, 0.626, 33.8, 32.0)

@reg("page.codeberg.JakobDev.jdMinecraftLauncher", INDIGO_LIGHT)
def i1869():
    out = poly([(32, 4), (58, 18), (32, 32), (6, 18)], I, 2) + dim(poly([(6, 22), (30, 35), (30, 62), (6, 49)], I, 2), .72) + dim(poly([(58, 22), (34, 35), (34, 62), (58, 49)], I, 2), .5)
    return fit(out, 0.6, 32.0, 33.0)

@reg("page.codeberg.JakobDev.jdMrpackInstaller", YELLOW_DARK)
def i1870():
    out = ink_stroke("M32 4V24", 5.5) + arrowhead(32, 18, 0, 1, 12) + rl(6, 38, 52, 22, 5) + ink_stroke("M6 46H58", 2.6, H)
    return fit(out, 0.551, 32.0, 30.6)

@reg("page.codeberg.JakobDev.jdNBTExplorer", BLUE_GREY_DARK)
def i1871():
    out = rl(6, 6, 22, 10, 3) + rl(24, 27, 34, 10, 3) + rl(24, 48, 34, 10, 3) + ink_stroke("M12 18V53H20M12 32H20", 3.4)
    return fit(out, 0.577, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdPermissionStoreEdit", LIGHT_BLUE_DEEP)
def i1872():
    out = rl(8, 28, 48, 32, 7) + ink_stroke("M18 28V20Q18 6 32 6T46 20V28", 5.5) + ink_circle(32, 41, 5, H) + rl(30, 43, 4, 10, 1.5, H)
    return fit(out, 0.597, 32.0, 31.6)

@reg("page.codeberg.JakobDev.jdPixelUpscaler", AMBER_DEEP)
def i1873():
    out = rl(4, 48, 8, 8, 1.4) + rl(16, 36, 16, 20, 2) + rl(36, 20, 24, 36, 3)
    return fit(out, 0.627, 32.0, 38.0)

@reg("page.codeberg.JakobDev.jdProcessFileWatcher", PINK_DEEP)
def i1874():
    out = ellring(32, 32, 27, 17, 5.5) + ink_circle(32, 32, 9)
    return fit(out, 0.605, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdReplace", TEAL)
def i1875():
    out = ink_stroke("M6 20H42", 5.5) + arrowhead(42, 20, 1, 0, 15) + ink_stroke("M58 44H22", 5.5) + arrowhead(22, 44, -1, 0, 15)
    return fit(out, 0.626, 32.0, 32.0)

@reg("page.codeberg.JakobDev.jdSimpleAutostart", DEEP_ORANGE_DEEP)
def i1876():
    out = ink_stroke("M19 14A22 22 0 1 0 45 14", 6) + ink_stroke("M32 4V28", 6)
    return fit(out, 0.646, 32.0, 28.9)

@reg("page.codeberg.JakobDev.jdSystemMonitor", DEEP_PURPLE_LIGHT)
def i1877():
    out = ink_stroke("M6 48A26 26 0 0 1 58 48", 7) + ink_stroke("M32 48L44 26", 5) + ink_circle(32, 48, 6.5) + ink_stroke("M12 58H52", 3)
    return fit(out, 0.61, 32.0, 39.0)

@reg("page.codeberg.JakobDev.jdTextEdit", BROWN_SOFT)
def i1878():
    out = ink_stroke("M6 14H46M6 28H38M6 42H30", 5) + rl(48, 22, 5, 36, 2) + rl(43, 22, 15, 4, 1.5) + rl(43, 54, 15, 4, 1.5)
    return fit(out, 0.583, 30.8, 34.8)

@reg("page.codeberg.bjawebos.Filmbook", GREY_DARK)
def i1879():
    out = ink_circle(32, 32, 28) + ink_circle(32, 32, 6, H) + "".join(ink_circle(*pt(32, 32, 15, -90 + 72 * k), 5, H) for k in range(5))
    return fit(out, 0.643, 32.0, 32.0)

@reg("page.codeberg.censor.Censor", BLUE_DEEP)
def i1880():
    out = ink_stroke("M6 12H42", 5) + rl(6, 24, 52, 14, 3) + ink_stroke("M6 50H48", 5)
    return fit(out, 0.608, 30.8, 31.0)

@reg("page.codeberg.cozyowl.OpaqueFiles", YELLOW_DARK)
def i1881():
    out = ink_path("M4 14Q4 10 8 10H24L30 18H56Q60 18 60 22V52Q60 56 56 56H8Q4 56 4 52Z") + ink_stroke("M20 46L44 26", 7, H) + ink_stroke("M20 46L44 26", 3.4)
    return fit(out, 0.588, 32.0, 33.0)

@reg("page.codeberg.dnkl.foot", RED_DEEP)
def i1882():
    out = ink_stroke("M10 12L32 32L10 52", 7) + rl(36, 46, 22, 7, 3.5)
    return fit(out, 0.612, 32.2, 32.0)

@reg("page.codeberg.dudenix.escritoire", CYAN)
def i1883():
    out = rl(2, 14, 60, 9, 3) + rl(8, 23, 9, 36, 2) + rl(47, 23, 9, 36, 2) + rl(21, 23, 22, 16, 2) + rl(29, 29, 6, 4, 2, H)
    return fit(out, 0.564, 32.0, 36.5)

@reg("page.codeberg.elly_code.cherrypick", ORANGE_DEEP)
def i1884():
    out = ink_circle(17, 46, 12) + ink_circle(46, 46, 12) + ink_stroke("M17 34Q22 16 42 8M46 34Q44 20 42 8", 3.4) + rot(ell(52, 12, 11, 5), -25, 52, 12)
    return fit(out, 0.547, 33.6, 31.8)

@reg("page.codeberg.elly_code.inscriptions", PURPLE_LIGHT)
def i1885():
    out = poly([(32, 2), (50, 28), (40, 62), (24, 62), (14, 28)], I, 3) + ink_stroke("M32 26V50", 2.8, H) + ink_circle(32, 24, 4.4, H)
    return fit(out, 0.571, 32.0, 32.0)

@reg("page.codeberg.elly_code.jorts", ORANGE_DEEP)
def i1886():
    out = ink_path("M8 8H56L60 56H36L32 32L28 56H4Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"') + rl(8, 8, 48, 6, 0, H) + rl(40, 20, 10, 12, 2, H)
    return fit(out, 0.54, 32.0, 32.0)

@reg("page.codeberg.elly_code.reminduck", BROWN_DARK)
def i1887():
    out = ink_circle(42, 16, 11) + ell(28, 42, 23, 15) + poly([(51, 14), (62, 19), (51, 23)], I, 2) + poly([(8, 36), (2, 26), (14, 32)], I, 2) + ink_circle(45, 14, 2.4, H)
    return fit(out, 0.581, 32.0, 31.0)

@reg("page.codeberg.elth0r0.iqpuzzle", INDIGO_DEEP)
def i1888():
    out = rl(8, 20, 40, 40, 5) + ink_circle(28, 16, 8) + ink_circle(52, 40, 8) + ink_circle(8, 40, 7, H)
    return fit(out, 0.594, 34.0, 34.0)

@reg("page.codeberg.foolish.Flipbook", YELLOW_DARK)
def i1889():
    out = dim(rl(4, 12, 42, 48, 5), .45) + rl(14, 4, 42, 48, 5) + ink_stroke("M22 18H40M22 26H34", 3.6, H) + poly([(56, 38), (40, 52), (56, 52)], H, 1.5)
    return fit(out, 0.569, 30.0, 32.0)

@reg("page.codeberg.friedrich.DND-Dice-Roller", BLUE_GREY_DEEP)
def i1890():
    out = hx(32, 32, 28, -90, I, 4) + poly([pt(32, 33, 14, -90 + 120 * k) for k in range(3)], H, 2.4) 
    return fit(out, 0.6, 32.0, 32.0)

@reg("page.codeberg.grinka.Transition", LIGHT_BLUE)
def i1891():
    out = ink_circle(21, 32, 17) + ring_c(43, 32, 15, 4.4)
    return fit(out, 0.64, 32.1, 32.0)

@reg("page.codeberg.gwync.glerm", AMBER_DEEP)
def i1892():
    out = rl(4, 8, 56, 48, 8) + ink_stroke("M14 22L25 32L14 42", 4.4, H) + rl(30, 40, 18, 4.6, 2, H)
    return fit(out, 0.609, 32.0, 32.0)

@reg("page.codeberg.ilijaculap.snux", PINK_LIGHT)
def i1893():
    out = asterisk(32, 32, 27, 5.4)
    return fit(out, 0.605, 32.0, 32.0)

@reg("page.codeberg.jaerrib.RNGremlin", TEAL)
def i1894():
    out = ink_circle(32, 38, 20) + poly([(14, 30), (0, 6), (26, 22)], I, 3) + poly([(50, 30), (64, 6), (38, 22)], I, 3) + ink_circle(24, 34, 4, H) + ink_circle(40, 34, 4, H) + poly([(22, 46), (42, 46), (38, 55), (34, 49), (30, 49), (26, 55)], H, 1.4)
    return fit(out, 0.485, 32.0, 31.2)

@reg("page.codeberg.jaerrib.attack-vector-alpha", DEEP_ORANGE_DARK)
def i1895():
    out = poly([(32, 2), (56, 56), (32, 44), (8, 56)], I, 5) + ink_circle(32, 27, 5, H)
    return fit(out, 0.531, 32.0, 29.0)

@reg("page.codeberg.jaerrib.wightwatch_keep", DEEP_PURPLE_DEEP)
def i1896():
    out = "".join(rl(x, 4, 12, 18, 1.5) for x in (6, 26, 46)) + rl(6, 20, 52, 40, 2) + ink_path("M24 60V46Q24 36 32 36T40 46V60Z", H)
    return fit(out, 0.546, 32.0, 32.0)

@reg("page.codeberg.lazyt.ubpm", INDIGO_SOFT)
def i1897():
    out = ring_c(32, 26, 21, 5.5) + ink_stroke("M32 26L43 14", 4.4) + ink_circle(32, 26, 4.4) + ink_stroke("M32 47V52", 4.4) + ell(32, 58, 9, 5)
    return fit(out, 0.593, 32.0, 32.6)

@reg("page.codeberg.lk108.deltatouch", GREY_DEEP)
def i1898():
    out = ink_stroke("M32 8L58 54H6Z", 6.5) + ink_circle(32, 40, 4)
    return fit(out, 0.54, 32.0, 31.0)

@reg("page.codeberg.lo_vely.Nucleus", BLUE)
def i1899():
    hs2 = ' stroke="HOLE" stroke-width="2.4"'
    out = ink_circle(24, 24, 12, I, hs2) + ink_circle(42, 22, 12, I, hs2) + ink_circle(33, 38, 12, I, hs2) + ink_circle(16, 42, 10, I, hs2) + ink_circle(50, 42, 10, I, hs2)
    return fit(out, 0.667, 33.0, 31.0)

@reg("page.codeberg.maerchenfeeimgarten.AntiBillard", YELLOW_DARK)
def i1900():
    out = ink_circle(32, 32, 26) + ink_circle(32, 32, 10, H) + ink_stroke("M10 54L54 10", 10, H) + ink_stroke("M10 54L54 10", 5)
    return fit(out, 0.61, 32.0, 32.0)
