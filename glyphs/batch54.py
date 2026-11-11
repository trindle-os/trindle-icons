# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 54: papirus-folders-gui to photogimp.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT, BROWN_LIGHT, circle,
    cpath, cut, CX, CY, CYAN_DARK, CYAN_DEEP, CYAN_SOFT, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT,
    DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY_DARK,
    GREY_DEEP, GREY_LIGHT, HOLE, INDIGO_DEEP, INDIGO_LIGHT, INK, LIGHT_BLUE_DARK,
    LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE, ORANGE_DEEP, ORANGE_LIGHT, path, PINK_DEEP,
    poly, pt, PURPLE_DARK, PURPLE_LIGHT, RED, RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke,
    TEAL, TEAL_DEEP, YELLOW, YELLOW_LIGHT,
)
from glyphs.kit import (
    GIMP_HEAD, registry,
)
from glyphs.kit import shared_gimp_s

ICONS, SMALL, reg, small = registry()


@reg("papirus-folders-gui", BLUE_GREY_DEEP)
def papirus_folders_gui():
    back = path("M15 17A3 3 0 0 1 18 14H27L31 18H46A3 3 0 0 1 49 21V30H15Z", BLUE_GREY_SOFT)
    front = rrect(15, 22, 34, 24, 3, INK)
    stripes = "".join(poly([(x, 46), (x + 6, 46), (x + 16, 22), (x + 10, 22)], c)
                      for x, c in [(18, RED), (26, AMBER), (34, TEAL)])
    return back + front + stripes


@reg("paraview", INDIGO_DEEP)
def paraview():
    return "".join(poly([(x, 45), (x + 6, 45), (x + 14, 15), (x + 8, 15)], INK, 3)
                   for x in (14.5, 24.5, 34.5))


@reg("parlatype", GREY_DEEP)
def parlatype():
    box = rrect(15, 13, 34, 34, 8, INK)
    band = stroke("M22 36V30A10 10 0 0 1 42 30V36", HOLE, 3.4)
    cups = rrect(20, 31, 6.5, 10, 3, HOLE) + rrect(37.5, 31, 6.5, 10, 3, HOLE)
    return box + band + cups


@reg("parley", BLUE_DEEP)
def parley():
    back = g(rrect(15, 15, 30, 26, 3, BLUE_SOFT), "rotate(-10 30 28)")
    front = rrect(19, 19, 30, 26, 3, INK)
    route = stroke("M24 38C27 29 34 36 37 30C39 26 36 23 34 25C32 27 38 31 44 26", HOLE, 2.4)
    return back + front + route + circle(24, 38, 2.2, HOLE)


@reg("parole", BLUE_GREY_DARK)
def parole():
    ring = f'<circle cx="32" cy="24" r="12.5" fill="none" stroke="{INK}" stroke-width="3.4"/>'
    play = poly([(28.5, 17.5), (38.5, 24), (28.5, 30.5)], INK, 2.4)
    bar = rrect(14, 42, 36, 5.5, 2.75, INK) + rrect(14, 42, 14, 5.5, 2.75, DEEP_ORANGE_LIGHT)
    return ring + play + bar


@reg("parsec", PINK_DEEP)
def parsec():
    back = cut("M24 15H44L38 45H18Z" + "M29 23H36L33 37H26Z", BLUE_LIGHT)
    front = cut("M21 13H41L35 43H15Z" + "M26 21H33L30 35H23Z", INK)
    return g(back + front, "translate(4 1)")


@reg("partitionmanager", BLUE_GREY)
def partitionmanager():
    body = rrect(17, 12, 30, 36, 5, INK)
    pie = circle(32, 30, 10.5, HOLE)
    wedge = path("M32 30V19.5A10.5 10.5 0 0 1 42.5 30Z", INK)
    wedge2 = path("M32 30H21.5A10.5 10.5 0 0 1 32 19.5Z", BLUE_GREY_SOFT)
    return body + pie + wedge + wedge2 + circle(32, 30, 2.2, INK)


@reg("password-manager", AMBER_DEEP)
def password_manager():
    ring = cut(cpath(22, 30, 8.5) + cpath(22, 30, 3), INK)
    shaft = rrect(28, 26.5, 21, 7, 2, INK)
    teeth = rrect(36, 30, 4.5, 9, 1.5, INK) + rrect(43, 30, 4.5, 7, 1.5, INK)
    return ring + shaft + teeth


@reg("patchage", BLUE_GREY_LIGHT)
def patchage():
    return stroke("M34 46V22A8.5 8.5 0 1 1 42.5 30.5H16", INK, 5.5)


@reg("patroneo", GREY_DARK)
def patroneo():
    corners = "".join(rrect(x, y, 14, 14, 3, GREY_LIGHT)
                      for x in (14, 36) for y in (12, 34))
    centre = rrect(19, 17, 26, 26, 5, INK, f' stroke="{HOLE}" stroke-width="2"')
    hole = rrect(26, 24, 12, 12, 3, HOLE)
    return corners + centre + hole + rrect(28.5, 26.5, 7, 7, 1.5, INK)


@reg("payday2", BLUE_DEEP)
def payday2():
    two = poly([(20, 14), (42, 14), (47, 18.5), (47, 24), (33, 37), (46, 37),
                (46, 45), (17, 45), (17, 38.5), (33, 24.5), (33, 21), (18, 21)], INK, 3)
    return g(two, "translate(32 30) skewX(-10) translate(-32 -30)")


@reg("pcbcalculator", PURPLE_LIGHT)
def pcbcalculator():
    box = rrect(14, 12, 34, 34, 6, INK)
    plus = line(23, 17.5, 23, 26.5, HOLE, 3) + line(18.5, 22, 27.5, 22, HOLE, 3)
    minus = line(34.5, 22, 43.5, 22, HOLE, 3)
    times = line(19.5, 33, 26.5, 40, HOLE, 3) + line(26.5, 33, 19.5, 40, HOLE, 3)
    eq = (circle(42, 40, 9, HOLE) + circle(42, 40, 7, INK) +
          line(38.5, 38, 45.5, 38, HOLE, 2.4) + line(38.5, 42.5, 45.5, 42.5, HOLE, 2.4))
    return box + plus + minus + times + eq


@reg("pcbnew", GREY_DARK)
def pcbnew():
    wires = stroke("M32 16V43H19M32 30H45", INK, 3)
    nodes = "".join(circle(x, y, 4, INK) for x, y in
                    [(32, 16), (32, 30), (45, 30), (32, 43), (19, 43)])
    return wires + nodes


@reg("pcloud", CYAN_DEEP)
def pcloud():
    cloud = path("M20 44A7 7 0 0 1 17 30.5A10 10 0 0 1 27 20A11 11 0 0 1 46 25A9.5 9.5 0 0 1 45 44Z", INK)
    ring = circle(33, 31, 10, HOLE) + circle(33, 31, 7.5, INK)
    p = stroke("M30.5 37V26H34A2.8 2.8 0 0 1 34 31.5H30.5", HOLE, 2.4)
    return cloud + ring + p


@reg("pd", BLUE_GREY_DARK)
def pd():
    box = rrect(14, 15, 36, 29, 3, INK)
    tabs = rrect(20, 13, 8, 4, 1, HOLE) + rrect(20, 42, 8, 4, 1, HOLE) + rrect(40, 13, 6, 4, 1, HOLE)
    p = (f'<circle cx="26.5" cy="29" r="4.3" fill="none" stroke="{HOLE}" stroke-width="3"/>'
         + line(22.2, 25, 22.2, 39.5, HOLE, 3))
    d = (f'<circle cx="37.5" cy="31" r="4.3" fill="none" stroke="{HOLE}" stroke-width="3"/>'
         + line(41.8, 20, 41.8, 35.3, HOLE, 3))
    return box + tabs + p + d


@reg("pdfarranger", LIGHT_BLUE_DEEP)
def pdfarranger():
    back = g(rrect(16, 14, 22, 30, 3, LIGHT_BLUE_SOFT), "rotate(-14 27 29)")
    front = g(rrect(24, 14, 24, 32, 3, INK), "rotate(10 36 30)")
    lines = g(rrect(28, 20, 16, 5, 1.5, HOLE) + rrect(28, 28, 7, 12, 1.5, HOLE) +
              rrect(37, 28, 7, 12, 1.5, HOLE), "rotate(10 36 30)")
    return back + front + lines


@reg("pdfchain", BLUE_DEEP)
def pdfchain():
    back = rrect(15, 13, 24, 24, 5, BLUE_SOFT)
    front = rrect(25, 23, 24, 24, 5, INK, f' stroke="{HOLE}" stroke-width="2"')
    link = g(f'<rect x="28" y="31.5" width="16" height="8" rx="4" fill="none" stroke="{HOLE}" stroke-width="3"/>',
             "rotate(35 36 35.5)")
    return back + front + link


@reg("pdfeditor", RED_DEEP)
def pdfeditor():
    sheet = path("M19 12H36L44 20V44A3 3 0 0 1 41 47H19A3 3 0 0 1 16 44V15A3 3 0 0 1 19 12Z", INK)
    fold = path("M36 12V17A3 3 0 0 0 39 20H44Z", RED_SOFT)
    swirl = stroke("M24 40C28 34 30 26 29.5 21C29 18 27 18.5 27 21C27 26 33 33 39 34"
                   "C41 34.3 41 32 38.5 32C33 32 26 36 24 40Z", HOLE, 2.2)
    badge = circle(42, 41, 8.5, CYAN_DEEP)
    pen = line(38.5, 44.5, 45, 38, INK, 3) + poly([(37, 46), (37.5, 43.4), (39.6, 45.5)], INK)
    return sheet + fold + swirl + badge + pen


@reg("pdfsam", LIGHT_BLUE_DARK)
def pdfsam():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    disc_ = circle(32, 30, 11, INK)
    swoop = (path("M22 33C25 25 33 21 42 24C35 24 29 28 26 35Z", HOLE) +
             path("M42 27C39 35 31 39 22 36C29 36 35 32 38 25Z", HOLE))
    eye = circle(33, 30, 3, DEEP_ORANGE_LIGHT)
    return ring + disc_ + swoop + eye


@reg("pdfstudio", BLUE_DARK)
def pdfstudio():
    q = (f'<circle cx="31" cy="31" r="10.5" fill="none" stroke="{INK}" stroke-width="5"/>'
         + line(35.5, 36, 44, 45, INK, 5.5))
    tag = rrect(14, 11, 16, 9, 2.5, DEEP_ORANGE_LIGHT)
    return q + tag


@reg("peazip", DEEP_PURPLE_SOFT)
def peazip():
    pod = g(f'<ellipse cx="32" cy="30" rx="19" ry="11" fill="{INK}"/>', "rotate(-40 32 30)")
    peas = (circle(32, 30, 5.2, HOLE) + circle(22.5, 38.5, 3.2, HOLE) + circle(41.5, 21.5, 3.2, HOLE))
    return pod + peas + circle(32, 30, 2.6, INK)


@reg("peek", DEEP_ORANGE_DEEP)
def peek():
    bar = rrect(14, 12, 36, 7, 3, INK)
    btn = circle(44.5, 15.5, 1.8, HOLE) + rrect(23, 14.5, 10, 2, 1, HOLE)
    corners = stroke("M16 29V24H22M42 24H48V29M48 40V45H42M22 45H16V40", INK, 3.4)
    return bar + btn + corners


@reg("peerunity", ORANGE_DEEP)
def peerunity():
    leaf = path("M19 44C17 30 23 17 45 14C47 32 38 44 22 45Z", INK)
    vein = stroke("M21 43C26 34 32 27 40 20", HOLE, 2.4)
    return leaf + vein


@reg("peg-e", INDIGO_DEEP)
def peg_e():
    return circle(CX, CY, 16.5, INK)


@reg("pegasus-fe", RED_DEEP)
def pegasus_fe():
    top = path("M16 26L30 23.5A3 3 0 0 1 36 22.3L46 20.5L45 25L35.5 26.7A3 3 0 0 1 30 27.8L17 30Z", INK)
    mid = poly([(16, 34), (38, 30), (37, 34.5), (17, 38.5)], INK, 1.5)
    hook = stroke("M46 23C49 29 45 36 38 38.5L18 43", INK, 4.4)
    return top + mid + hook


@reg("pekka-kana-2", PURPLE_DARK)
def pekka_kana_2():
    comb = path("M24 22C21 18 22 13 26 13C27 10 32 10 33 13C36 11 40 13 39 17"
                "C42 17 43 21 40 23Z", RED_LIGHT)
    head = path("M26 21C31 19 39 20 41 26C42.5 32 41 40 39 47H28C29 42 28 37 25 34Z", INK)
    beak = poly([(26, 25), (19, 29), (26, 31)], AMBER, 1.5)
    wattle = path("M22 32C19 36 21 42 25 42C28.5 42 29 37 27 33Z", RED_LIGHT)
    eye = circle(32, 26.5, 2, HOLE)
    return g(comb + head + beak + wattle + eye, "translate(32 30) scale(1.12) translate(-31 -29.5)")


@reg("pencil", ORANGE_DEEP)
def pencil():
    body = poly([(21, 47), (21, 25), (32, 14), (43, 25), (43, 47)], INK, 3)
    return body + stroke("M27.5 26.5Q32 29 36.5 26.5", HOLE, 2.4)


@reg("pencil2d", BLUE_DEEP)
def pencil2d():
    ring = f'<circle cx="37" cy="26" r="11.5" fill="none" stroke="{BLUE_SOFT}" stroke-width="3"/>'
    body = g(rrect(20, 25.5, 30, 9, 3, INK), "rotate(-45 35 30)")
    tip = g(poly([(20.5, 25.5), (20.5, 34.5), (12, 30)], INK, 1.5) +
            poly([(15.5, 28.2), (15.5, 31.8), (12.5, 30)], HOLE), "rotate(-45 35 30)")
    band = g(rrect(44, 25.5, 2.4, 9, 0, HOLE), "rotate(-45 35 30)")
    return ring + g(body + tip + band, "translate(-3 3)")


def _penumbra():
    pts = [pt(CX, CY, 17 if k % 2 == 0 else 13.2, -90 + 18 * k) for k in range(20)]
    star = poly(pts, INK, 3)
    figure = path("M32 15.5L29 19.5C28 21.5 28 23.5 29 25.5L26.5 28C25.5 32.5 25.8 37.5 27.2 42.5"
                  "H36.8C38.2 37.5 38.5 32.5 37.5 28L35 25.5C36 23.5 36 21.5 35 19.5Z", HOLE)
    return star + figure


@reg("penumbra-necrologue", DEEP_ORANGE_DEEP)
@reg("penumbra-overture", BLUE_GREY_LIGHT)
@reg("penumbra-requiem", BROWN_LIGHT)
@reg("penumbra-black-plague", RED_DEEP)
def penumbra_black_plague():
    return _penumbra()


@reg("performous", INDIGO_LIGHT)
def performous():
    head = circle(29, 17, 4.2, INK)
    body = stroke("M28 22C30 29 30 34 28 40L26 47M29.5 34L34 41L36 47", INK, 4.4)
    arm = stroke("M28.5 23.5L35 25L33 19.5", INK, 3.2)
    other = stroke("M29 26L40 32L47 36", INK, 3.2)
    mic = line(33, 19.5, 31.5, 15.5, INK, 3.4)
    return head + body + arm + other + mic


@reg("persepolis", RED)
def persepolis():
    spikes = "".join(path(f"M21 {y}C29 {y - 1.5} 38 {y - 1} 46 {y + 2.5}C38 {y + 3.5} 29 {y + 4.5} 21 {y + 5}Z", INK)
                     for y in (13, 20.5, 28))
    fangs = (path("M22 35H29C28.5 40 27 44 25 47.5C24 44 22.5 40 22 35Z", INK) +
             path("M32 35H39C38.5 40 37 44 35 47.5C34 44 32.5 40 32 35Z", INK))
    return spikes + fangs


@reg("persona-4-golden", AMBER)
def persona_4_golden():
    p = stroke("M17 44V17H24.5A7 7 0 0 1 24.5 31H17", INK, 5)
    four = stroke("M44 44V17L31 36H48", INK, 5)
    return p + four


@reg("peruse", TEAL_DEEP)
def peruse():
    page = rrect(14, 13, 36, 34, 5, INK)
    gutters = stroke("M35 11L27 49M33.5 26L52 30", HOLE, 2.6)
    eye = (f'<ellipse cx="42.5" cy="20" rx="5" ry="3.6" fill="{HOLE}"/>' + circle(43.5, 20, 1.8, INK))
    return page + gutters + eye


@reg("pgadmin", BLUE_DARK)
def pgadmin():
    ears = (f'<ellipse cx="19.5" cy="25" rx="6.5" ry="9.5" fill="{INK}" stroke="{HOLE}" stroke-width="2"/>'
            f'<ellipse cx="44.5" cy="25" rx="6.5" ry="9.5" fill="{INK}" stroke="{HOLE}" stroke-width="2"/>')
    head = circle(32, 25, 10.5, INK)
    trunk = stroke("M32 30V41C32 45 37 46 38 42", INK, 6)
    tusks = stroke("M26.5 33.5L24 38M37.5 33.5L40 38", INK, 2.6)
    eyes = circle(27.5, 24, 1.8, HOLE) + circle(36.5, 24, 1.8, HOLE)
    return ears + head + trunk + tusks + eyes


@reg("pgmodeler", CYAN_DEEP)
def pgmodeler():
    tiles = (rrect(15, 12, 9, 9, 1, CYAN_DARK) + rrect(41, 16, 9, 9, 1, CYAN_SOFT) +
             rrect(14, 34, 8, 8, 1, RED_LIGHT) + rrect(42, 38, 8, 8, 1, AMBER_SOFT))
    head = path("M27 15C33 12 42 15 43 23C43.5 28 42 33 38 36C36.5 38 36 41 37 44"
                "C34 47 30 45 30 40C30 36 29 33 26 31C21 28 20 18 27 15Z", INK)
    return tiles + head + circle(36.5, 23, 1.8, HOLE) + path("M38 33L44 34.5L39.5 37Z", HOLE)


@reg("phantompeer", BLUE)
def phantompeer():
    brim = f'<ellipse cx="32" cy="29" rx="18" ry="5.5" fill="{INK}"/>'
    crown = path("M22 28C22 20 24 13 28 13C30 13 31 15 32 15C33 15 34 13 36 13C40 13 42 20 42 28Z", INK)
    band = rrect(22.5, 22, 19, 3.2, 1, HOLE)
    mask = path("M22 33H42C42 42 38 47 32 47C26 47 22 42 22 33Z", BLUE_DARK)
    eyes = path("M25 37C27 36 29.5 37 30.5 39C28 40.5 26 39.5 25 37Z", INK) + \
        path("M39 37C37 36 34.5 37 33.5 39C36 40.5 38 39.5 39 37Z", INK)
    return crown + brim + band + mask + eyes


@reg("phasmophobia", BLUE_GREY_DARK)
def phasmophobia():
    stem = stroke("M31.5 17C31 26 32 36 28.5 45", INK, 3.6)
    bowl = stroke("M24 19C28 14 38 13.5 41 17.5C43.5 21 40 27 33 28.5", INK, 3.6)
    flick = stroke("M24 19C24.5 22 26 23 27.5 22.5", INK, 2.6)
    return stem + bowl + flick


def _eye():
    return path("M13 30C18 20 25 15.5 32 15.5C39 15.5 46 20 51 30C46 40 39 44.5 32 44.5"
                "C25 44.5 18 40 13 30Z", INK)


@reg("phatch", BLUE_DEEP)
def phatch():
    teeth = "".join(g(rrect(29.5, 17, 5, 26, 1.5, HOLE), f"rotate({45 * k} 32 30)") for k in range(4))
    return _eye() + teeth + circle(32, 30, 10, HOLE) + circle(32, 30, 4, INK)


@reg("phatch-inspector", BLUE_GREY)
def phatch_inspector():
    lens = f'<circle cx="34.5" cy="27" r="6.5" fill="none" stroke="{HOLE}" stroke-width="3.6"/>'
    return _eye() + lens + line(29.5, 32, 24, 37.5, HOLE, 4.2)


@reg("phd2", DEEP_PURPLE_LIGHT)
def phd2():
    ring = "".join(stroke("M{:.2f} {:.2f}A15 15 0 0 1 {:.2f} {:.2f}".format(
        *pt(32, 30, 15, a + 6), *pt(32, 30, 15, a + 84)), INK, 4.4) for a in (0, 90, 180, 270))
    letters = (stroke("M20.5 36V24H23.5A3 3 0 0 1 23.5 30H20.5", INK, 2.4) +
               stroke("M28.5 24V36M35 24V36M28.5 30H35", INK, 2.4) +
               stroke("M39.5 24V36H40.5A5 6 0 0 0 40.5 24Z", INK, 2.4))
    return ring + letters


@reg("phoenix-emu-project-logo", BLUE_GREY_DARK)
def phoenix_emu():
    left = path("M24 13C16 18 14 34 22 43C26 47 30 48 31 47C24 42 21 35 22 27C22.5 21 24 16 24 13Z", ORANGE)
    right = path("M40 13C48 18 50 34 42 43C38 47 34 48 33 47C40 42 43 35 42 27C41.5 21 40 16 40 13Z", INK)
    gem = g(rrect(28.5, 14.5, 7, 7, 1, RED), "rotate(45 32 18)")
    drum = rrect(26.5, 25.5, 11, 6.5, 2.5, BLUE_LIGHT)
    dot = circle(32, 39.5, 5, YELLOW)
    return left + right + gem + drum + dot


@reg("phoenix-wright-ace-attorney-trilogy", INDIGO_DEEP)
def phoenix_wright():
    hair = path("M22 17L27 13L28.5 15L38 11L37 14.5L50 14L41 18L51 20L41 22L49 26L39 27L44 32"
                "L36 31L33 36L28 35L25 30L22 29L21 25L18 25L20 21Z", INK)
    face = path("M22 27L19 30L21 32L20 35L24 36L30 35L33 36C32 40 34 44 38 47H16"
                "C18 43 20 40 21 37Z", INK)
    mouth = path("M20 32.5L25 31.5L24 34Z", HOLE)
    return hair + face + mouth


@reg("phoronix-test-suite", DEEP_PURPLE_SOFT)
def phoronix():
    p = path("M17 18A5 5 0 0 1 22 13H42A5 5 0 0 1 47 18V35A5 5 0 0 1 42 40H28V45A3 3 0 0 1 25 48"
             "H20A3 3 0 0 1 17 45Z", INK)
    arrows = (stroke("M24 21H38", HOLE, 2.8) + poly([(37, 17.5), (42, 21), (37, 24.5)], HOLE, 1) +
              stroke("M40 32H26", HOLE, 2.8) + poly([(27, 28.5), (22, 32), (27, 35.5)], HOLE, 1))
    return p + arrows + circle(32, 26.5, 2, HOLE)


@reg("photocollage", RED)
def photocollage():
    frame = rrect(14, 12, 36, 36, 4, INK)
    gutters = stroke("M36 12V24M14 24H50M26 24V48", HOLE, 2.8)
    return frame + gutters


@reg("photofilmstrip", BLUE_GREY_DARK)
def photofilmstrip():
    film = rrect(13, 13, 38, 34, 4, INK)
    holes = "".join(rrect(x, y, 4, 3.2, 0.8, HOLE) for x in (17, 25, 33, 41) for y in (15.5, 41.3))
    screen = rrect(15, 20.5, 34, 19, 1.5, HOLE)
    eyes = (path("M18 26L29 29C28 33 23 34 20 31C18.5 29.5 18 28 18 26Z", YELLOW_LIGHT) +
            path("M46 26L35 29C36 33 41 34 44 31C45.5 29.5 46 28 46 26Z", YELLOW_LIGHT))
    slits = line(24, 29.5, 24, 32, HOLE, 1.6) + line(40, 29.5, 40, 32, HOLE, 1.6)
    return film + holes + screen + eyes + slits


def _sparkle(cx, cy, r):
    return path(f"M{f(cx)} {f(cy - r)}Q{f(cx + r * .2)} {f(cy - r * .2)} {f(cx + r)} {f(cy)}"
                f"Q{f(cx + r * .2)} {f(cy + r * .2)} {f(cx)} {f(cy + r)}"
                f"Q{f(cx - r * .2)} {f(cy + r * .2)} {f(cx - r)} {f(cy)}"
                f"Q{f(cx - r * .2)} {f(cy - r * .2)} {f(cx)} {f(cy - r)}Z", INK)


@reg("photoflare", LIGHT_BLUE_DEEP)
def photoflare():
    ring = stroke("M40 19A14.5 14.5 0 1 0 45.5 28", INK, 3)
    disc_ = circle(30, 32, 10, INK)
    cuts = stroke("M30 22V42M20 32H40", HOLE, 2)
    knobs = circle(30, 27, 2, HOLE) + circle(35, 32, 2, HOLE)
    return ring + disc_ + cuts + knobs + _sparkle(44, 17, 5.5) + circle(49.5, 25, 1.6, INK)


@reg("photogimp", DEEP_PURPLE)
def photogimp():
    head = GIMP_HEAD
    eyes = (circle(26.5, 25, 5, HOLE) + circle(37.5, 25, 5, HOLE) +
            circle(28, 26, 2.2, INK) + circle(39, 26, 2.2, INK))
    brush = line(34, 38, 48, 29, DEEP_PURPLE_DARK, 3) + path(
        "M46.5 30L50.5 27.5L52 30.5L48.5 32Z", DEEP_PURPLE_DARK,
        f' stroke="{DEEP_PURPLE_DARK}" stroke-width="1.5" stroke-linejoin="round"')
    return head + eyes + brush


@small("paraview")
def paraview_s():
    return "".join(poly([(x, 45), (x + 7, 45), (x + 15, 15), (x + 8, 15)], INK, 3)
                   for x in (13, 25, 37))


@small("parlatype")
def parlatype_s():
    return (rrect(14, 12, 36, 36, 8, INK) + stroke("M21.5 36V30A10.5 10.5 0 0 1 42.5 30V36", HOLE, 4.4) +
            rrect(19, 30, 8, 12, 3, HOLE) + rrect(37, 30, 8, 12, 3, HOLE))


@small("parole")
def parole_s():
    ring = circle(32, 24, 14, INK)
    play = poly([(28, 17), (39, 24), (28, 31)], HOLE, 2)
    return ring + play + rrect(14, 42, 36, 6, 3, INK)


@small("pcbcalculator")
def pcbcalculator_s():
    box = rrect(13, 11, 38, 38, 6, INK)
    plus = line(23, 16, 23, 28, HOLE, 4) + line(17, 22, 29, 22, HOLE, 4)
    eq = line(35, 36, 45, 36, HOLE, 4) + line(35, 43, 45, 43, HOLE, 4)
    return box + plus + line(35, 22, 45, 22, HOLE, 4) + eq


@small("pcbnew")
def pcbnew_s():
    return (stroke("M32 16V43H18M32 30H46", INK, 4) +
            "".join(circle(x, y, 5, INK) for x, y in [(32, 16), (46, 30), (32, 43), (18, 43)]))


@small("pcloud")
def pcloud_s():
    cloud = path("M20 45A7 7 0 0 1 16 30.5A10 10 0 0 1 27 19A11 11 0 0 1 47 24A10 10 0 0 1 46 45Z", INK)
    return cloud + stroke("M29 40V25H34.5A4 4 0 0 1 34.5 33H29", HOLE, 4)


@small("pd")
def pd_s():
    box = rrect(13, 14, 38, 32, 4, INK)
    p = (f'<circle cx="26" cy="29" r="4.5" fill="none" stroke="{HOLE}" stroke-width="4"/>'
         + line(21.5, 25, 21.5, 42, HOLE, 4))
    d = (f'<circle cx="38" cy="31" r="4.5" fill="none" stroke="{HOLE}" stroke-width="4"/>'
         + line(42.5, 18, 42.5, 35.5, HOLE, 4))
    return box + p + d


@small("pdfarranger")
def pdfarranger_s():
    back = g(rrect(15, 13, 24, 32, 3, ORANGE_LIGHT), "rotate(-14 27 29)")
    front = g(rrect(23, 13, 26, 34, 3, INK), "rotate(10 36 30)")
    return back + front + g(rrect(27, 19, 18, 6, 2, HOLE), "rotate(10 36 30)")


@small("pdfchain")
def pdfchain_s():
    back = rrect(13, 11, 26, 26, 5, BLUE_SOFT)
    front = rrect(24, 22, 26, 26, 5, INK, f' stroke="{HOLE}" stroke-width="2"')
    return back + front


@small("pdfeditor")
def pdfeditor_s():
    sheet = path("M19 11H36L45 20V45A3 3 0 0 1 42 48H19A3 3 0 0 1 16 45V14A3 3 0 0 1 19 11Z", INK)
    return sheet + line(24, 41, 38, 27, HOLE, 5) + poly([(21, 44), (22, 39), (26, 43)], HOLE)


@small("pdfsam")
def pdfsam_s():
    return (circle(32, 30, 16.5, INK) +
            path("M20 34C23 24 33 19 44 23C36 23 29 28 25 37Z", HOLE) +
            path("M44 26C41 36 31 41 20 37C28 37 35 32 39 23Z", HOLE))


@small("peazip")
def peazip_s():
    pod = g(f'<ellipse cx="32" cy="30" rx="20" ry="12" fill="{INK}"/>', "rotate(-40 32 30)")
    return pod + circle(32, 30, 6, HOLE) + circle(22, 39, 3.8, HOLE) + circle(42, 21, 3.8, HOLE)


@small("peek")
def peek_s():
    return rrect(13, 11, 38, 8, 3, INK) + stroke("M16 31V25H23M41 25H48V31M48 40V46H41M23 46H16V40", INK, 4.4)


def _penumbra_s():
    pts = [pt(CX, CY, 17.5 if k % 2 == 0 else 14, -90 + 18 * k) for k in range(20)]
    figure = path("M32 14.5L28.5 19.5C27.5 21.5 27.5 23.5 28.5 25.5L25.5 28.5C24.5 33 25 38 26.5 43"
                  "H37.5C39 38 39.5 33 38.5 28.5L35.5 25.5C36.5 23.5 36.5 21.5 35.5 19.5Z", HOLE)
    return poly(pts, INK, 3) + figure


for _n in ("penumbra-black-plague", "penumbra-necrologue", "penumbra-overture", "penumbra-requiem"):
    small(_n)(_penumbra_s)


@small("persepolis")
def persepolis_s():
    spikes = "".join(path(f"M19 {y}C28 {y - 1.5} 38 {y - 1} 47 {y + 3}C38 {y + 4.5} 28 {y + 5.5} 19 {y + 6.5}Z", INK)
                     for y in (12, 21))
    fangs = (path("M20 32H29C28.5 38 27 43 24.5 48C22.5 43 21 38 20 32Z", INK) +
             path("M33 32H42C41.5 38 40 43 37.5 48C35.5 43 34 38 33 32Z", INK))
    return spikes + fangs


@small("phatch")
def phatch_s():
    teeth = "".join(g(rrect(28.5, 15, 7, 30, 2, HOLE), f"rotate({45 * k} 32 30)") for k in range(4))
    return _eye() + teeth + circle(32, 30, 11, HOLE) + circle(32, 30, 5, INK)


@small("phatch-inspector")
def phatch_inspector_s():
    lens = f'<circle cx="35" cy="26.5" r="6.5" fill="none" stroke="{HOLE}" stroke-width="4.4"/>'
    return _eye() + lens + line(29.5, 32, 23, 38.5, HOLE, 5)


@small("phd2")
def phd2_s():
    ring = "".join(stroke("M{:.2f} {:.2f}A15 15 0 0 1 {:.2f} {:.2f}".format(
        *pt(32, 30, 15, a + 8), *pt(32, 30, 15, a + 82)), INK, 4.4) for a in (0, 90, 180, 270))
    return ring + stroke("M27 38V22H32.5A4.5 4.5 0 0 1 32.5 31H27", INK, 4)


@small("phoenix-emu-project-logo")
def phoenix_emu_s():
    left = path("M23 12C14 18 12 35 21 44C25 48 30 49 31 48C23 42 20 35 21 27C21.5 21 23 16 23 12Z", ORANGE)
    right = path("M41 12C50 18 52 35 43 44C39 48 34 49 33 48C41 42 44 35 43 27C42.5 21 41 16 41 12Z", INK)
    gem = g(rrect(27.5, 13.5, 9, 9, 1, RED), "rotate(45 32 18)")
    return left + right + gem + rrect(26, 26, 12, 7, 2.5, BLUE_LIGHT) + circle(32, 40, 5.5, YELLOW)


@small("phoronix-test-suite")
def phoronix_s():
    p = path("M16 17A5 5 0 0 1 21 12H43A5 5 0 0 1 48 17V36A5 5 0 0 1 43 41H29V46A3 3 0 0 1 26 49"
             "H19A3 3 0 0 1 16 46Z", INK)
    return p + stroke("M22 21H40", HOLE, 3.6) + poly([(38, 16.5), (44, 21), (38, 25.5)], HOLE, 1) + \
        stroke("M42 32H24", HOLE, 3.6) + poly([(26, 27.5), (20, 32), (26, 36.5)], HOLE, 1)


@small("photofilmstrip")
def photofilmstrip_s():
    film = rrect(12, 13, 40, 34, 4, INK)
    screen = rrect(12, 20, 40, 20, 0, HOLE)
    eyes = (path("M15 25L29 29C28 34 22 35 18.5 32C16 30 15 28 15 25Z", YELLOW_LIGHT) +
            path("M49 25L35 29C36 34 42 35 45.5 32C48 30 49 28 49 25Z", YELLOW_LIGHT))
    return film + screen + eyes


@small("photoflare")
def photoflare_s():
    ring = stroke("M40 18A15 15 0 1 0 46 28", INK, 4)
    disc_ = circle(30, 32, 10.5, INK)
    return ring + disc_ + stroke("M30 22V42M20 32H40", HOLE, 3) + _sparkle(45, 16, 6.5)


@small("photogimp")
def photogimp_s():
    return shared_gimp_s()


@small("pekka-kana-2")
def pekka_s():
    comb = path("M23 22C20 17 21 11 26 11C27.5 8 33 8 34 11.5C37.5 10 42 12 40.5 17C43 18 43.5 22 40 23.5Z", RED_LIGHT)
    head = path("M25 21C31 18.5 40 19.5 42 26C43.5 32 42 40 40 48H27C28 42 27 37 24 34Z", INK)
    beak = poly([(25, 24), (16, 29), (25, 31.5)], AMBER, 1.5)
    return comb + head + beak + circle(32, 27, 2.6, HOLE)


@small("pgadmin")
def pgadmin_s():
    ears = (f'<ellipse cx="18.5" cy="25" rx="7" ry="10" fill="{INK}" stroke="{HOLE}" stroke-width="2"/>'
            f'<ellipse cx="45.5" cy="25" rx="7" ry="10" fill="{INK}" stroke="{HOLE}" stroke-width="2"/>')
    return ears + circle(32, 25, 11, INK) + stroke("M32 30V42C32 46 38 47 39 43", INK, 7)
