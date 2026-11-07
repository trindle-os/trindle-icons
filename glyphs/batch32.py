# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 32: gpodder to guitarix."""
from lm import *
from glyphs.kit import arc, gear_b, registry, ring_b, rot_b, _slabs

ICONS, SMALL, reg, small = registry()

@reg("gpodder", PURPLE)
def gpodder():
    body = path("M32 16C37.5 16 40.5 20 40.5 25.5V35.5C40.5 37.5 42.5 38.8 45.5 39.8"
                "C49.5 41 49 46 45 46H19C15 46 14.5 41 18.5 39.8C21.5 38.8 23.5 37.5 23.5 35.5"
                "V25.5C23.5 20 26.5 16 32 16Z", INK)
    band = stroke("M20 27V23A12 12 0 0 1 44 23V27", INK, 2.6)
    cups = rrect(16, 22, 5.5, 10, 2.75, INK) + rrect(42.5, 22, 5.5, 10, 2.75, INK)
    eyes = (path("M28.2 21.5a3.4 4.6 0 1 0 0.01 0Z", HOLE) + path("M35.8 21.5a3.4 4.6 0 1 0 0.01 0Z", HOLE)
            + circle(28.6, 27.2, 1.7, INK) + circle(36.2, 27.2, 1.7, INK))
    return body + band + cups + eyes

@reg("gqrx", BROWN_DEEP)
def gqrx():
    pulse = stroke("M13.5 36H21L24.5 28L28 43L31.5 21L35 39L37.5 36H50.5", INK, 3.2)
    bars = "".join(rrect(41, y, 9, 3, 1.5, INK) for y in (14, 19.5, 25))
    return pulse + bars

@reg("groove", BLUE_DEEP)
def groove():
    disc = circle(CX, CY, 16.5, INK)
    loop = stroke(arc(CX, CY, 9.5, -45, 245), HOLE, 4.2)
    tick = line(35.5, 21.2, 41, 15.5, HOLE, 3.4)
    return disc + loop + tick + circle(CX, CY, 3.2, HOLE)

@reg("gridplayer", GREY_DEEP)
def gridplayer():
    out = ""
    for x in (14.5, 32.5):
        for y in (12.5, 30.5):
            out += rrect(x, y, 17, 17, 3.5, GREY_DARK)
            cx, cy = x + 8.5, y + 8.5
            out += poly([(cx - 3.3, cy - 5), (cx + 5, cy), (cx - 3.3, cy + 5)], INK, 2)
    return out

@reg("gthumb", ORANGE_DEEP)
def gthumb():
    petal = "M32 30C26 24.5 26.5 18 32 12.5C37.5 18 38 24.5 32 30Z"
    flower = "".join(rot_b(path(petal, INK), 60 * k) for k in range(6))
    return flower + circle(CX, CY, 4, HOLE) + circle(CX, CY, 1.8, INK)

@reg("gtkpod", GREY_DEEP)
def gtkpod():
    return (rrect(19.5, 11.5, 25, 37, 5, INK) + rrect(23, 15, 18, 13, 2, HOLE)
            + ring_b(32, 38.5, 5.3, HOLE, 3.4))

@reg("gtranscribe", TEAL)
def gtranscribe():
    pad = rrect(15, 14, 26, 32, 3.5, INK)
    rings = "".join(rrect(x, 11, 3, 6, 1.5, INK) for x in (19, 24.5, 30, 35.5))
    lines = (rrect(19, 21, 18, 2.6, 1.3, HOLE) + rrect(19, 27, 18, 2.6, 1.3, HOLE)
             + rrect(19, 33, 11, 2.6, 1.3, HOLE))
    badge = circle(41.5, 40, 10.5, HOLE) + circle(41.5, 40, 8.5, TEAL_DEEP)
    mic = (rrect(39, 33.5, 5, 8.5, 2.5, INK) + stroke("M36.8 39.5A4.7 4.7 0 0 0 46.2 39.5", INK, 2)
           + line(41.5, 44.5, 41.5, 46.5, INK, 2))
    return pad + rings + lines + badge + mic

@reg("guitar", BLUE)
def guitar():
    body = path("M22 28C25 27 27 29.5 29.5 27.5C31.5 26 31 23 33.5 22.5C36.5 22 38 25 37.5 28"
                "C37 31 39 32.5 39 35.5C39 43 33 48.5 25.5 48C18.5 47.5 14 42 15 36.5"
                "C15.6 32.5 18.5 29 22 28Z", INK)
    neck = line(29, 36, 45.5, 18, INK, 3.6)
    head = rot_b(rrect(43.5, 11.5, 6.5, 9, 2.5, INK), 42, 46.75, 16)
    detail = (line(24.5, 39.5, 35, 28, HOLE, 2.4) + circle(25.5, 42.5, 2, HOLE)
              + line(21.5, 34, 26, 38.5, HOLE, 2.4))
    return body + neck + head + detail

@reg("guitarix", GREY_DARK)
def guitarix():
    top = rrect(14, 12.5, 36, 11.5, 3, INK)
    knobs = "".join(circle(x, 18.25, 2.1, HOLE) for x in (20, 26, 32)) + rrect(41.5, 16, 4.5, 4.5, 1, HOLE)
    cab = rrect(14, 27, 36, 21, 4, INK)
    cones = ring_b(23.5, 37.5, 5.3, HOLE, 3.4) + ring_b(40.5, 37.5, 5.3, HOLE, 3.4)
    return top + knobs + cab + cones

@reg("gtklick", GREY_DARK)
def gtklick():
    body = poly([(27, 13), (37, 13), (46.5, 46), (17.5, 46)], INK, 3.5)
    notch = poly([(30, 11.5), (34, 11.5), (32, 16)], HOLE, 1)
    arm = line(32, 38, 26, 21, HOLE, 3.2) + circle(32, 38.5, 4.2, HOLE)
    return body + notch + arm

@reg("green-recorder", CYAN_DEEP)
def green_recorder():
    screen = rrect(14, 14, 36, 25, 4, INK) + rrect(24, 42, 16, 4.5, 2.25, INK)
    cam = rrect(21.5, 20.5, 13.5, 12, 2.5, HOLE) + poly([(36.5, 26.5), (43, 21.5), (43, 31.5)], HOLE, 1.5)
    return screen + cam

@reg("gpredict-icon", TEAL)
def gpredict():
    panels = (rot_b(rrect(15, 13, 11, 11, 2, INK), 45, 20.5, 18.5)
              + rot_b(rrect(38, 36, 11, 11, 2, INK), 45, 43.5, 41.5))
    arrow = rot_b(poly([(32, 21.5), (38.5, 37), (32, 33), (25.5, 37)], INK, 2.5), 45)
    return panels + arrow

@reg("gpsd-logo", BLUE_DEEP)
def gpsd():
    panel = rot_b(rrect(12.5, 26, 39, 9, 2.5, INK), 45, 32, 30.5)
    cells = "".join(rot_b(line(x, 26.5, x, 34.5, HOLE, 2), 45, 32, 30.5) for x in (21, 26.5, 37.5, 43))
    body = line(24.5, 38, 38.5, 24, HOLE, 9.5) + line(24.5, 38, 38.5, 24, INK, 6)
    dish = path("M37 13A8 8 0 0 0 48.5 24.5Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return panel + cells + body + dish

@reg("gpxviewer", BLUE_DEEP)
def gpxviewer():
    globe = circle(CX, CY, 16.5, INK)
    land = (path("M18 22C20 18 25 16 29 17C30.5 19 28.5 21 27.5 23C26.5 25 23.5 25 22.5 27"
                 "C21.5 28.5 19 27.5 18 25Z", HOLE)
            + path("M26 31C29 30 31 32 30.5 35C30 38 28 42 26.5 44C25.5 42 25.5 38 24.5 36"
                   "C24 34 24 31.5 26 31Z", HOLE)
            + path("M37 16.5C40 15.5 44 17.5 45.5 20C43.5 21 41.5 21 40.5 23C42.5 24 45.5 26 46 30"
                   "C45.5 34 42.5 36 41.5 39C40.5 41 39 40.5 39 38.5C39 36 37.5 34 36.5 32"
                   "C35.5 30 36.5 28 36 26C35.5 24 35 22 36 20C36.5 18.5 36.5 17.5 37 16.5Z", HOLE))
    return globe + land

@reg("gretl", ORANGE_DEEP)
def gretl():
    pts = [(18, 40), (26.5, 29), (36, 35), (46, 20)]
    trend = stroke("M" + "L".join(f"{x} {y}" for x, y in pts), INK, 3.2)
    return trend + "".join(circle(x, y, 4, INK) + circle(x, y, 1.8, HOLE) for x, y in pts)

@reg("gramps", BROWN_LIGHT)
def gramps():
    box = lambda x, y, s=7.5: rrect(x - s / 2, y - s / 2, s, s, 1.6, INK)
    out = box(32, 16) + box(21, 29) + box(43, 29)
    out += "".join(box(x, 43, 6.5) for x in (16.5, 25.5, 38.5, 47.5))
    wires = (stroke("M32 19.5V23H21V25.5M32 23H43V25.5", INK, 2.2)
             + stroke("M21 32.5V36H16.5V39.5M21 36H25.5V39.5M43 32.5V36H38.5V39.5M43 36H47.5V39.5", INK, 2.2))
    return out + wires

@reg("grass", ORANGE_DARK)
def grass():
    diamond = rot_b(rrect(18.5, 16.5, 27, 27, 5, INK), 45)
    blades = (stroke("M32 44C31 36 30.5 27 33.5 16", HOLE, 2.6)
              + stroke("M30.5 44C28 38 24 34 20 32", HOLE, 2.4)
              + stroke("M33.5 44C36 38 40 34.5 44 32.5", HOLE, 2.4)
              + stroke("M31 44C29.5 37 27 31 25 25.5", HOLE, 2.4)
              + stroke("M33 44C34.5 37 37 31.5 39.5 26", HOLE, 2.4))
    return diamond + blades

@reg("gtkwave", CYAN_DARK)
def gtkwave():
    grid = ("".join(line(x, 13, x, 47, CYAN_DEEP, 2.2) for x in (19, 32, 45))
            + "".join(line(14, y, 50, y, CYAN_DEEP, 2.2) for y in (18, 30, 42)))
    wave = stroke("M13.5 44H21.5L26.5 16H37.5L42.5 44H50.5", INK, 3.6)
    return grid + wave

@reg("graebert-gmbh.ares-commander", RED_DEEP)
def ares():
    edge = f' stroke="{HOLE}" stroke-width="1.6" stroke-linejoin="round"'
    return (path("M17 46Q19 22 44 12.5Q27 25 21.5 45Z", INK, edge)
            + path("M19 46Q25 27 48 19Q32 30 24.5 45.5Z", INK, edge)
            + path("M21 46.5Q31 32 50 27Q36 35 27.5 46Z", INK, edge))

@reg("grafx2", BLUE_DEEP)
def grafx2():
    x1 = line(19, 15, 45, 45, BLUE_SOFT, 8.5)
    x2 = line(19, 45, 45, 15, INK, 8.5)
    two = stroke("M42.5 26.5C43 24 48 24 48 27C48 29.5 44.5 31 42.5 34H48.5", INK, 2.6)
    return x1 + x2 + two

@reg("gtk-theme-config", BLUE_GREY_DARK)
def gtk_theme_config():
    petals = "".join(rot_b(rrect(28.5, 11.5, 7, 12, 3.5, INK), 45 * k) for k in range(8))
    return (petals + circle(CX, CY, 9, HOLE) + gear_b(CX, CY, 7, 5.3, INK)
            + circle(CX, CY, 2.4, HOLE))

@reg("gtk3-demo", BLUE)
def gtk3_demo():
    top = poly([(32, 12.5), (47, 20.5), (32, 28.5), (17, 20.5)], INK, 2.5)
    left = poly([(17, 20.5), (32, 28.5), (32, 47), (17, 39)], BLUE_DARK, 2.5)
    right = poly([(47, 20.5), (32, 28.5), (32, 47), (47, 39)], BLUE_SOFT, 2.5)
    return top + left + right

@reg("gtkhash", BLUE_GREY)
def gtkhash():
    return (line(29.5, 14, 25.5, 46, INK, 4.6) + line(40.5, 14, 36.5, 46, INK, 4.6)
            + line(17, 24, 47.5, 24, INK, 4.6) + line(16.5, 36, 47, 36, INK, 4.6))

@reg("gpu-screen-recorder", PURPLE_LIGHT)
def gpu_screen_recorder():
    screen = rrect(15, 14, 34, 31, 4, INK)
    glasses = (rrect(18, 25, 28, 3, 0, HOLE) + rrect(20, 25, 10, 6.5, 1, HOLE)
               + rrect(34, 25, 10, 6.5, 1, HOLE) + rrect(22, 27, 2.5, 2.5, 0, INK)
               + rrect(36, 27, 2.5, 2.5, 0, INK))
    return screen + glasses

@reg("grub-customizer", GREY_DEEP)
def grub_customizer():
    return (gear_b(CX, CY, 17, 13, INK, 8) + circle(CX, CY, 9.5, HOLE)
            + circle(CX, CY, 6.5, INK) + stroke(arc(CX, CY, 9.5, 120, 330), YELLOW_SOFT, 2.4))

@reg("gshutdown", RED_DEEP)
def gshutdown():
    return (circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.5, HOLE)
            + stroke(arc(CX, 31, 6.5, -50, 230), INK, 3) + line(32, 21.5, 32, 29, INK, 3))

@reg("grsync", RED)
def grsync():
    top = stroke(arc(CX, CY, 11, 170, 330), INK, 3.6)
    bot = stroke(arc(CX, CY, 11, -10, 150), INK, 3.6)
    h1 = poly([(37.5, 22.5), (47, 21), (44.5, 30)], INK, 2)
    h2 = poly([(26.5, 37.5), (17, 39), (19.5, 30)], INK, 2)
    return top + bot + h1 + h2

@reg("gst", RED_DEEP)
def gst():
    pins = ""
    for v in (25, 32, 39):
        pins += line(v, 13.5, v, 20, INK, 2.6) + line(v, 40, v, 46.5, INK, 2.6)
        pins += line(15, v - 2, 21.5, v - 2, INK, 2.6) + line(42.5, v - 2, 49, v - 2, INK, 2.6)
    return pins + rrect(20.5, 18.5, 23, 23, 3, INK) + rrect(26, 24, 12, 12, 1.5, HOLE)

@reg("gst-debug-viewer", DEEP_PURPLE_DEEP)
def gst_debug_viewer():
    return (stroke("M17 23C21 18.5 25 18.5 29 21C33 23.5 37 23.5 41 20.5", INK, 3.6)
            + stroke("M23 31C27 26.5 31 26.5 35 29C39 31.5 43 31.5 47 28.5", DEEP_PURPLE_SOFT, 3.6)
            + stroke("M17 39C21 34.5 25 34.5 29 37C33 39.5 37 39.5 41 36.5", INK, 3.6))

@reg("gtimelog", ORANGE_DEEP)
def gtimelog():
    note = rrect(20.5, 33, 23, 14, 3, ORANGE_SOFT)
    lines = rrect(25, 40, 14, 2.6, 1.3, HOLE) + rrect(25, 43.8, 9, 2.4, 1.2, HOLE)
    clock = circle(32, 24, 14.5, HOLE) + circle(32, 24, 12.5, INK)
    hands = stroke("M32 17V24.5H37.5", HOLE, 2.8)
    return note + lines + clock + hands

@reg("gtkorphan", BROWN_LIGHT)
def gtkorphan():
    box = rrect(13, 12, 30, 30, 4, INK)
    tape = rrect(25, 12, 6, 30, 0, BROWN_SOFT) + rrect(13, 24, 30, 6, 0, BROWN_SOFT)
    badge = circle(41.5, 39.5, 11, HOLE) + circle(41.5, 39.5, 9, BROWN_DEEP)
    x = line(38.3, 36.3, 44.7, 42.7, INK, 2.8) + line(44.7, 36.3, 38.3, 42.7, INK, 2.8)
    return box + tape + badge + x

@reg("gtkterm", TEAL_DEEP)
def gtkterm():
    flange = rrect(12.5, 22.5, 39, 15, 4, INK) + circle(17, 30, 2.1, HOLE) + circle(47, 30, 2.1, HOLE)
    shell = poly([(21.5, 19.5), (42.5, 19.5), (39, 40.5), (25, 40.5)], HOLE, 7) + poly(
        [(21.5, 19.5), (42.5, 19.5), (39, 40.5), (25, 40.5)], INK, 3)
    pins = ("".join(circle(x, 26.5, 1.8, HOLE) for x in (25.5, 28.75, 32, 35.25, 38.5))
            + "".join(circle(x, 33.5, 1.8, HOLE) for x in (27.2, 30.4, 33.6, 36.8)))
    return flange + shell + pins

@reg("guake", INDIGO_SOFT)
def guake():
    dollar = (stroke("M27.5 21C25.5 18.5 17.5 18.5 17.5 23.5C17.5 28.5 27.5 27.5 27.5 33"
                     "C27.5 38.5 19 38.5 16.5 35.5", INK, 3.6) + line(22.2, 15, 22.2, 42, INK, 3))
    return dollar + rrect(32.5, 36, 15, 4.4, 2.2, INK)

@reg("guake-prefs", INDIGO_SOFT)
def guake_prefs():
    dollar = (stroke("M24.5 17C22.5 14.5 14.5 14.5 14.5 19.5C14.5 24.5 24.5 23.5 24.5 29"
                     "C24.5 34.5 16 34.5 13.5 31.5", INK, 3.6) + line(19.2, 11, 19.2, 38, INK, 3))
    under = rrect(29.5, 30, 13, 4.4, 2.2, INK)
    badge = circle(41, 39.5, 12, HOLE) + circle(41, 39.5, 10, INK)
    cog = gear_b(41, 39.5, 6.6, 4.9, HOLE, 8) + circle(41, 39.5, 2.2, INK)
    return dollar + under + badge + cog

@reg("gufw", INDIGO)
def gufw():
    shield = path("M17 14H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    band = poly([(36.5, 14), (47, 14), (47, 21), (24.4, 43.3), (20, 38.6)], HOLE)
    return shield + band

@reg("guiscrcpy", INDIGO)
def guiscrcpy():
    phone = rrect(21.5, 11.5, 21, 37, 4.5, INK) + rrect(25, 16, 14, 25.5, 2, HOLE)
    droid = (path("M26.5 39A5.5 5 0 0 1 37.5 39Z", INK) + line(28, 33.3, 27, 31.8, INK, 1.4)
             + line(36, 33.3, 37, 31.8, INK, 1.4))
    return phone + droid + circle(32, 45, 1.6, HOLE)

@reg("gramwallet", LIGHT_BLUE_DEEP)
def gramwallet():
    tri = stroke("M21.5 21H42.5C44.5 21 45.5 23 44.5 24.7L33.3 43C32.7 44 31.3 44 30.7 43"
                 "L19.5 24.7C18.5 23 19.5 21 21.5 21Z", HOLE, 3.2)
    return circle(CX, CY, 16.5, INK) + tri + line(32, 21.5, 32, 42.5, HOLE, 3.2)

@reg("granatier", RED_DEEP)
def granatier():
    bomb = circle(29, 34, 13, INK)
    cap = rot_b(rrect(33.5, 17, 8, 7, 1.8, INK), 40, 37.5, 20.5)
    fuse = stroke("M40 17.5C40.5 13.5 44 12 47.5 14", INK, 2.4)
    spark = poly([pt(44, 41, 6.8 if k % 2 == 0 else 3.2, -90 + 30 * k) for k in range(12)], RED_SOFT)
    return bomb + cap + fuse + circle(44, 41, 7.8, HOLE) + spark

@reg("granule", AMBER_DARK)
def granule():
    card = rrect(20, 12.5, 24, 19, 2.5, AMBER_SOFT)
    lines = rrect(24, 17, 16, 2.6, 1.3, HOLE) + rrect(24, 22, 16, 2.6, 1.3, HOLE)
    tray = rrect(14.5, 28, 35, 18, 3.5, INK) + rrect(25.5, 34.5, 13, 4, 2, HOLE)
    return card + lines + tray

@reg("grapejuice", DEEP_PURPLE)
def grapejuice():
    return _slabs(DEEP_PURPLE_SOFT, INK)

@reg("grapejuice-roblox-studio", LIGHT_BLUE_DEEP)
def grapejuice_studio():
    return _slabs(INK, LIGHT_BLUE_SOFT)

@reg("grapejuice-roblox-player", GREY_DARK)
def roblox_player():
    return rot_b(rrect(16.5, 14.5, 31, 31, 3.5, INK) + rrect(28, 26, 8, 8, 1, HOLE), 15)

@reg("greenfoot", DEEP_PURPLE_SOFT)
def greenfoot():
    foot = path("M25 25C25 22 28 20.5 31 21.5C35.5 23 37.5 28 39 31C41 34.5 46.5 36 47.5 41"
                "C48.5 46 44 48.5 38.5 47.5C33.5 46.5 30.5 46.5 27.5 47.5C24 48.5 22 46 22 42"
                "C22 36 25 31 25 25Z", INK)
    toes = circle(19.5, 17.5, 5, INK) + circle(28.5, 13.5, 3.4, INK) + circle(35, 15.5, 2.8, INK)
    return foot + toes

@reg("grid-autosport", GREY_DARK)
def grid_autosport():
    wing = path("M30 25C25 25 19 21 13 14C13.5 20 15 24 17.5 26.5L13 26C15 30 18 32 21.5 33"
                "L17 35C20.5 37.5 24.5 37.5 27.5 36.5L25.5 41C28.5 40 30 38 30.5 36Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    wings = wing + g(wing, "translate(64 0) scale(-1 1)")
    body = poly([(32, 16), (35.5, 24), (32, 45), (28.5, 24)], HOLE, 5) + poly(
        [(32, 16), (35.5, 24), (32, 45), (28.5, 24)], INK, 2)
    return wings + body

@reg("grim-fandango-remastered", AMBER_DARK)
def grim_fandango():
    mask = path("M16 15.5L22 13L27 15.5L32 12L37 15.5L42 13L48 15.5L46 32C45 40.5 39.5 47 32 47"
                "C24.5 47 19 40.5 18 32Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    eyes = path("M26 20a3.6 4.4 0 1 0 0.01 0Z", HOLE) + path("M38 20a3.6 4.4 0 1 0 0.01 0Z", HOLE)
    nose = poly([(30, 30), (34, 30), (32, 33.5)], HOLE, 1.5)
    teeth = rrect(24, 36, 16, 7.5, 2, HOLE)
    gaps = ("".join(line(x, 36.5, x, 43, INK, 1.6) for x in (28, 32, 36))
            + line(24.5, 39.75, 39.5, 39.75, INK, 1.6))
    return mask + eyes + nose + teeth + gaps

@reg("groovy", DEEP_PURPLE_LIGHT)
def groovy():
    return ring_b(CX, CY, 15.5, INK, 3.4) + stroke("M38.5 23.5A9 9 0 1 0 41 30.5H33", INK, 4.2)

@reg("gta-3", BLUE_GREY_DARK)
def gta3():
    block = rrect(13.5, 16, 37, 28, 4, INK)
    gaps = rrect(24.5, 22, 4, 16, 1.2, HOLE) + rrect(35.5, 22, 4, 16, 1.2, HOLE)
    sides = circle(13.5, 30, 4, HOLE) + circle(50.5, 30, 4, HOLE)
    return block + gaps + sides

@reg("gta-5", GREY_DARK)
def gta5():
    v = ("M13 16H29V19.5H26L32 35L38 19.5H35V16H51V19.5H47.5L36 45H28L16.5 19.5H13Z")
    return (path(v, INK, f' stroke="{INK}" stroke-width="5" stroke-linejoin="round"')
            + path(v, GREY))

@reg("gta-vice-city", PINK)
def gta_vice_city():
    word = (stroke("M14.5 19L21 36L28 17", INK, 3.4)
            + stroke("M31 27L30 36", INK, 3) + circle(31.6, 22.3, 2, INK)
            + stroke("M40 28.5C37.5 26 34 28 34.2 32.5C34.4 36 37.5 37 40.5 35", INK, 3)
            + stroke("M42.5 32.5C46 32.5 49 30.5 48 28C47 26 42.5 26.5 42.5 31.5"
                     "C42.5 35.5 46 37 49.5 34.5", INK, 3))
    swoosh = stroke("M15 43C25 39.5 38 39.5 50 42", INK, 2.6)
    return word + swoosh

@reg("guilded", AMBER_DEEP)
def guilded():
    return stroke("M47.5 16.5H16.5V25C16.5 36 24 43 32 46.5C40 43 47.5 36 47.5 30H33", INK, 6)

@small("gta-vice-city")
def gta_vice_city_s():
    return stroke("M17 17L25 40L33 17", INK, 4.4) + stroke("M46 26C41 22 35 26 35.5 32.5C36 38 42 39.5 47 36", INK, 4.4)

@small("grim-fandango-remastered")
def grim_fandango_s():
    mask = path("M16 15.5L22 13L27 15.5L32 12L37 15.5L42 13L48 15.5L46 32C45 40.5 39.5 47 32 47"
                "C24.5 47 19 40.5 18 32Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    eyes = path("M25.5 19.5a4.2 5 0 1 0 0.01 0Z", HOLE) + path("M38.5 19.5a4.2 5 0 1 0 0.01 0Z", HOLE)
    return mask + eyes + rrect(24, 35, 16, 7, 2, HOLE)

@small("gtranscribe")
def gtranscribe_s():
    pad = rrect(14, 12, 28, 34, 4, INK)
    lines = rrect(18.5, 19, 19, 4, 2, HOLE) + rrect(18.5, 27, 12, 4, 2, HOLE)
    badge = circle(42, 40, 11.5, HOLE) + circle(42, 40, 9.5, TEAL_DEEP)
    mic = rrect(38.5, 33, 7, 11, 3.5, INK)
    return pad + lines + badge + mic

@small("gtkterm")
def gtkterm_s():
    flange = rrect(12, 22.5, 40, 15, 4, INK)
    q = [(21, 18.5), (43, 18.5), (39.5, 41.5), (24.5, 41.5)]
    shell = poly(q, HOLE, 7) + poly(q, INK, 3)
    pins = "".join(circle(x, 26.5, 2.6, HOLE) for x in (26, 32, 38)) + \
        "".join(circle(x, 34, 2.6, HOLE) for x in (29, 35))
    return flange + shell + pins

@small("gramps")
def gramps_s():
    out = rrect(26.5, 11, 11, 10, 2, INK)
    out += rrect(14, 37, 12, 11, 2, INK) + rrect(38, 37, 12, 11, 2, INK)
    return out + stroke("M32 21V29H20V37M32 29H44V37", INK, 3.2)

@small("guiscrcpy")
def guiscrcpy_s():
    return rrect(20.5, 11, 23, 38, 5, INK) + rrect(24.5, 16, 15, 26, 2, HOLE) + \
        path("M26.5 40A5.5 5.5 0 0 1 37.5 40Z", INK)

@small("gpsd-logo")
def gpsd_s():
    panel = rot_b(rrect(12, 25.5, 40, 10, 3, INK), 45, 32, 30.5)
    body = line(24.5, 38, 38.5, 24, HOLE, 11) + line(24.5, 38, 38.5, 24, INK, 7)
    dish = path("M36 12A9 9 0 0 0 49.5 25.5Z", INK)
    return panel + body + dish

@small("graebert-gmbh.ares-commander")
def ares_s():
    edge = f' stroke="{HOLE}" stroke-width="1.6" stroke-linejoin="round"'
    return (path("M15 47Q15 20 46 11Q30 28 24 46Z", INK, edge)
            + path("M21 48Q30 29 51 24Q40 36 31 48Z", INK, edge))

@small("gqrx")
def gqrx_s():
    return stroke("M13 34H20L25 22L31 44L37 26L40 34H51", INK, 4) + rrect(40, 13, 11, 4, 2, INK)

@small("gridplayer")
def gridplayer_s():
    out = ""
    for cx in (23, 41):
        for cy in (21, 39):
            out += poly([(cx - 4.5, cy - 6), (cx + 6, cy), (cx - 4.5, cy + 6)], INK, 2)
    return out

@small("gshutdown")
def gshutdown_s():
    return (circle(CX, CY, 17, INK) + stroke(arc(CX, 31.5, 8, -50, 230), HOLE, 4.2)
            + line(32, 19, 32, 29, HOLE, 4.2))

@small("gst")
def gst_s():
    pins = ""
    for v in (26, 38):
        pins += line(v, 12, v, 20, INK, 4) + line(v, 40, v, 48, INK, 4)
        pins += line(13, v - 2, 21, v - 2, INK, 4) + line(43, v - 2, 51, v - 2, INK, 4)
    return pins + rrect(20, 18, 24, 24, 3.5, INK) + rrect(27, 25, 10, 10, 1.5, HOLE)

@small("gtimelog")
def gtimelog_s():
    note = rrect(19.5, 35, 25, 13, 3, ORANGE_SOFT)
    clock = circle(32, 24, 15.5, HOLE) + circle(32, 24, 13.5, INK)
    return note + clock + stroke("M32 16.5V25H38.5", HOLE, 4)

@small("guitarix")
def guitarix_s():
    top = rrect(13, 11, 38, 11, 3, INK) + rrect(18, 14.5, 12, 4, 2, HOLE)
    cab = rrect(13, 26, 38, 23, 4, INK)
    return top + cab + circle(23, 37.5, 5.5, HOLE) + circle(41, 37.5, 5.5, HOLE)

@small("guake-prefs")
def guake_prefs_s():
    dollar = (stroke("M25 17C23 14.5 15 14.5 15 19.5C15 24.5 25 23.5 25 29"
                     "C25 34.5 16.5 34.5 14 31.5", INK, 4) + line(19.7, 11, 19.7, 38, INK, 3.2))
    badge = circle(41, 39.5, 12.5, HOLE) + circle(41, 39.5, 10.5, INK) + circle(41, 39.5, 4, HOLE)
    return dollar + badge

@small("grass")
def grass_s():
    diamond = rot_b(rrect(18.5, 16.5, 27, 27, 5, INK), 45)
    return diamond + stroke("M32 45C31 36 31 27 33.5 16", HOLE, 3.4) + \
        stroke("M31 45C28 38 24 34 20 32.5", HOLE, 3.4) + stroke("M33 45C36 38 40 34.5 44 33", HOLE, 3.4)
