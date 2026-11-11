# SPDX-License-Identifier: GPL-3.0-or-later
"""Shared drawing kit for the Trindle icon theme.

Every icon is a 64x64 canvas: a round
disc and a brand glyph centred on (CX, CY) inside a ~34px box.
"""
import math
import re

from symbolic.kit import n as f

CX, CY = 32, 30

INK = "INK"
HOLE = "HOLE"
WHITE, BLACK = "#FAFAFA", "#09090B"
RED_SOFT = "#F7847C"
RED_LIGHT = "#F5645A"
RED = "#F34236"
RED_DEEP = "#C2352B"
RED_DARK = "#972921"

PINK_SOFT = "#F06EAB"
PINK_LIGHT = "#EC4895"
PINK = "#E8207E"
PINK_DEEP = "#BA1A65"
PINK_DARK = "#90144E"

PURPLE_SOFT = "#BE72CA"
PURPLE_LIGHT = "#AD4DBD"
PURPLE = "#9B26AE"
PURPLE_DEEP = "#7C1E8B"
PURPLE_DARK = "#60186C"

DEEP_PURPLE_SOFT = "#9C7EC8"
DEEP_PURPLE_LIGHT = "#825DBA"
DEEP_PURPLE = "#6639AB"
DEEP_PURPLE_DEEP = "#522E89"
DEEP_PURPLE_DARK = "#3F236A"

INDIGO_SOFT = "#818ECE"
INDIGO_LIGHT = "#6070C2"
INDIGO = "#3D51B4"
INDIGO_DEEP = "#314190"
INDIGO_DARK = "#263270"

BLUE_SOFT = "#6FBAF6"
BLUE_LIGHT = "#4AA8F4"
BLUE = "#2295F1"
BLUE_DEEP = "#1B77C1"
BLUE_DARK = "#155C95"

LIGHT_BLUE_SOFT = "#5BC6F7"
LIGHT_BLUE_LIGHT = "#30B8F5"
LIGHT_BLUE = "#03A8F3"
LIGHT_BLUE_DEEP = "#0286C2"
LIGHT_BLUE_DARK = "#026897"

CYAN_SOFT = "#59D3E2"
CYAN_LIGHT = "#2EC8DB"
CYAN = "#00BCD3"
CYAN_DEEP = "#0096A9"
CYAN_DARK = "#007583"

TEAL_SOFT = "#5ABAB1"
TEAL_LIGHT = "#2FA89D"
TEAL = "#019587"
TEAL_DEEP = "#01776C"
TEAL_DARK = "#015C54"

YELLOW_SOFT = "#FFF17F"
YELLOW_LIGHT = "#FFEE5D"
YELLOW = "#FFEA3A"
YELLOW_DEEP = "#CCBB2E"
YELLOW_DARK = "#9E9124"

AMBER_SOFT = "#FFD65D"
AMBER_LIGHT = "#FFCB33"
AMBER = "#FFC006"
AMBER_DEEP = "#CC9A05"
AMBER_DARK = "#9E7704"

ORANGE_SOFT = "#FEBB59"
ORANGE_LIGHT = "#FEAA2E"
ORANGE = "#FE9700"
ORANGE_DEEP = "#CB7900"
ORANGE_DARK = "#9D5E00"

DEEP_ORANGE_SOFT = "#FF926F"
DEEP_ORANGE_LIGHT = "#FF7549"
DEEP_ORANGE = "#FF5721"
DEEP_ORANGE_DEEP = "#CC461A"
DEEP_ORANGE_DARK = "#9E3614"

BROWN_SOFT = "#A89189"
BROWN_LIGHT = "#91746A"
BROWN = "#795649"
BROWN_DEEP = "#61453A"
BROWN_DARK = "#4B352D"

GREY_SOFT = "#C0BFC0"
GREY_LIGHT = "#AFAFAF"
GREY = "#9E9D9E"
GREY_DEEP = "#7E7E7E"
GREY_DARK = "#626162"

BLUE_GREY_SOFT = "#98AAB4"
BLUE_GREY_LIGHT = "#7D94A0"
BLUE_GREY = "#607C8B"
BLUE_GREY_DEEP = "#4D636F"
BLUE_GREY_DARK = "#3C4D56"

NAVY = "#111827"
BRAND_YELLOW = "#FBC711"
INK_SLATE = "#3A3F44"

PALE = {BLUE_SOFT, LIGHT_BLUE_SOFT, CYAN_SOFT, CYAN_LIGHT, YELLOW_SOFT,
        YELLOW_LIGHT, YELLOW, YELLOW_DEEP, AMBER_SOFT, AMBER_LIGHT,
        AMBER, ORANGE_SOFT, ORANGE_LIGHT, ORANGE, DEEP_ORANGE_SOFT,
        GREY_SOFT, GREY_LIGHT, BRAND_YELLOW}


GLYPH_SCALE = .94


def disc(fill):
    return f'<circle cx="32" cy="32" r="25.5" fill="{fill}"/>'


def _fit(glyph, extra=1):
    k = GLYPH_SCALE * extra
    return glyph if k == 1 else f'<g transform="translate(32 30) scale({k}) translate(-32 -30)">{glyph}</g>'


def lift(glyph):
    """The mark's own silhouette dropped below it in three crisp steps,
    so the logo stands up off its tile. No blur filters."""
    flat = re.sub(r'(fill|stroke)="#[0-9A-Fa-f]{6}"', rf'\1="{BLACK}"', glyph)
    copies = [re.sub(r'(id="|url\(#)([\w-]+)', rf'\g<1>\g<2>-s{k}', flat) for k in range(3)]
    return "".join(f'<g opacity="{o}" transform="translate(0 {dy})">{c}</g>'
                   for c, (dy, o) in zip(copies, [(4.5, .07), (3, .11), (1.5, .16)]))


def _inked(glyph, tile):
    ink = BLACK if tile in PALE else WHITE
    return glyph.replace('"INK"', f'"{ink}"').replace('"HOLE"', f'"{tile}"')


def icon(glyph, tile, fit=1):
    """Full-size icon (32px and up): tile plus a logo lifted off it."""
    glyph = _fit(_inked(glyph, tile), fit)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">'
        + disc(tile)
        + f'<g transform="translate(0 1)">{lift(glyph)}</g>'
        + f'<g transform="translate(0 -.5)">{glyph}</g>'
        + "</svg>\n"
    )


def _thicken(glyph, k=1.3):
    return re.sub(r'stroke-width="([\d.]+)"', lambda m: f'stroke-width="{f(float(m[1]) * k)}"', glyph)


def small_icon(glyph, tile, px, fit=1):
    """16/22/24px icon: no lift, tile fills the canvas, logo enlarged and
    strokes thickened so the mark survives a handful of pixels."""
    glyph = _fit(_thicken(_inked(glyph, tile)), fit)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" viewBox="0 0 64 64">'
        + f'<circle cx="32" cy="32" r="30.5" fill="{tile}"/>'
        + f'<g transform="translate(32 32) scale(1.22) translate(-32 -30)">{glyph}</g>'
        + "</svg>\n"
    )


def circle(cx, cy, r, fill, extra=""):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}"{extra}/>'


def cpath(cx, cy, r):
    """Circle as a path fragment, for evenodd cut-outs."""
    return (f"M{f(cx - r)} {f(cy)}a{f(r)} {f(r)} 0 1 0 {f(2 * r)} 0"
            f"a{f(r)} {f(r)} 0 1 0 {f(-2 * r)} 0Z")


def path(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}"{extra}/>'


def cut(d, fill):
    return f'<path d="{d}" fill="{fill}" fill-rule="evenodd"/>'


def line(x1, y1, x2, y2, stroke, w, cap="round", extra=""):
    return (f'<path d="M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}" stroke="{stroke}" '
            f'stroke-width="{f(w)}" stroke-linecap="{cap}" fill="none"{extra}/>')


def stroke(d, colour, w, extra=""):
    return (f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{f(w)}" '
            f'stroke-linecap="round" stroke-linejoin="round"{extra}/>')


def rrect(x, y, w, h, r, fill, extra=""):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="{f(r)}" fill="{fill}"{extra}/>')


def poly(pts, fill, rounding=0):
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
    extra = ""
    if rounding:
        extra = f' stroke="{fill}" stroke-width="{f(rounding)}" stroke-linejoin="round"'
    return path(d, fill, extra)


def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def g(content, transform):
    return f'<g transform="{transform}">{content}</g>'
