# SPDX-License-Identifier: MIT
"""Trindle's small one-colour icons, drawn in the Trindle symbolic style."""
from .kit import *

SYM = {}

def reg(name, context):
    def deco(fn):
        SYM[name] = (context, fn)
        return fn
    return deco

def _speaker():
    return s("M2 6.2A1 1 0 0 1 3 5.2H5L8.2 2.6A.5.5 0 0 1 9 3V13A.5.5 0 0 1 8.2 13.4L5 10.8H3A1 1 0 0 1 2 9.8Z")

def _bell():
    return (p("M4 11V7A4 4 0 0 1 12 7V11L13.2 12.5H2.8Z") + ln(6.8, 14.2, 9.2, 14.2))

def _wifi(level, faint_dot=False):
    """level: how many of the three arcs are lit (0-3)."""
    out = dot(8, 12.6, 1.3, FAINT if faint_dot else "")
    for k, rad in enumerate([4, 7.5, 11]):
        out += arc(8, 14, rad * .95, 225, 315, "" if k < level else FAINT)
    return out

def _battery(fill_w, extra=""):
    body = r(1.75, 4.75, 11, 6.5, 2) + rs(13.3, 6.5, 1.4, 3, .6)
    return body + (rs(3.5, 6.5, fill_w, 3, .8) if fill_w else "") + extra

def _gauge(angle):
    x, y = 8 + 4.2 * math.cos(math.radians(angle)), 11 + 4.2 * math.sin(math.radians(angle))
    return arc(8, 11, 6.25, 180, 360) + ln(8, 11, x, y) + dot(8, 11, 1.3)

def _gear(cx=8, cy=8, ro=6.2, ri=2.1, teeth=8):
    pts = []
    for k in range(teeth * 2):
        a0 = math.radians(k * 180 / teeth - 90)
        rr = ro if k % 2 == 0 else ro - 1.6
        for da in (-.13, .13):
            pts.append((cx + rr * math.cos(a0 + da * (4 / teeth) * 2), cy + rr * math.sin(a0 + da * (4 / teeth) * 2)))
    d = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in pts) + "Z"
    return p(d) + c(cx, cy, ri)

def _person(cx=8, cy=8, sc=1.0):
    return (c(cx, cy - 3 * sc, 2.5 * sc) +
            p(f"M{n(cx - 5 * sc)} {n(cy + 6 * sc)}A{n(5 * sc)} {n(4.5 * sc)} 0 0 1 {n(cx + 5 * sc)} {n(cy + 6 * sc)}"))

def _folder(open_=False):
    if open_:
        return p("M1.75 12.5V4A1.25 1.25 0 0 1 3 2.75H6L7.5 4.25H12A1.25 1.25 0 0 1 13.25 5.5V6.5"
                 "M1.75 12.5L3.5 7.5A1.25 1.25 0 0 1 4.7 6.75H14.2L12.5 12.5A1 1 0 0 1 11.5 13.25H2.5A.75.75 0 0 1 1.75 12.5Z")
    return p("M1.75 4A1.25 1.25 0 0 1 3 2.75H6L7.5 4.25H13A1.25 1.25 0 0 1 14.25 5.5V12A1.25 1.25 0 0 1 13 13.25H3"
             "A1.25 1.25 0 0 1 1.75 12Z")

def _doc(lines=True):
    out = p("M4 1.75H9.5L12.25 4.5V13A1.25 1.25 0 0 1 11 14.25H4A1.25 1.25 0 0 1 2.75 13V3A1.25 1.25 0 0 1 4 1.75Z")
    if lines:
        out += ln(5.5, 7.5, 9.5, 7.5) + ln(5.5, 10.5, 9.5, 10.5)
    return out

def _printer():
    return (p("M4.5 5.25V2.5A.75.75 0 0 1 5.25 1.75H10.75A.75.75 0 0 1 11.5 2.5V5.25") +
            p("M4.5 11.5H3A1.25 1.25 0 0 1 1.75 10.25V6.5A1.25 1.25 0 0 1 3 5.25H13A1.25 1.25 0 0 1 14.25 6.5V10.25"
              "A1.25 1.25 0 0 1 13 11.5H11.5") + r(4.5, 9, 7, 5.25, .75))

def _monitor():
    return r(1.75, 2.25, 12.5, 8.5, 1.5) + ln(8, 10.75, 8, 13.25) + ln(5, 13.75, 11, 13.75)

def _globe():
    return (c(8, 8, 6.25) + p("M8 1.75C5.8 4 5.8 12 8 14.25M8 1.75C10.2 4 10.2 12 8 14.25") +
            ln(1.75, 8, 14.25, 8))

def _pad():
    return (p("M4.5 4.25H11.5A3.5 3.5 0 0 1 14.8 8.8L14 11.6A1.8 1.8 0 0 1 11 12.4L9.6 10.75H6.4L5 12.4"
              "A1.8 1.8 0 0 1 2 11.6L1.2 8.8A3.5 3.5 0 0 1 4.5 4.25Z") +
            ln(5, 6.5, 5, 8.5) + ln(4, 7.5, 6, 7.5) + dot(10.5, 7, .8) + dot(12, 8.3, .8))

def _padlock():
    return r(3.25, 7, 9.5, 7.25, 1.75) + p("M5.25 7V5A2.75 2.75 0 0 1 10.75 5V7") + dot(8, 10.6, 1.1)

def _mic():
    return r(5.75, 1.75, 4.5, 7.5, 2.25) + p("M3.25 7.5A4.75 4.75 0 0 0 12.75 7.5") + ln(8, 12.25, 8, 14.25)

def _headphones():
    return (p("M2.25 10V8A5.75 5.75 0 0 1 13.75 8V10") +
            rs(1.5, 8.75, 3.5, 5.5, 1.5) + rs(11, 8.75, 3.5, 5.5, 1.5))

@reg("input-keyboard", "devices")
def keyboard():
    keys = "".join(dot(x, y, .75) for y in (6.75, 9) for x in (4.5, 6.8, 9.2, 11.5))
    return r(1.75, 3.75, 12.5, 8.5, 2) + keys + ln(5.5, 11.2, 10.5, 11.2)

@reg("zoom-in", "actions")
def zoom_in():
    return c(6.75, 6.75, 4.75) + ln(10.2, 10.2, 14, 14) + ln(4.75, 6.75, 8.75, 6.75) + ln(6.75, 4.75, 6.75, 8.75)

@reg("trindle-keep-awake", "apps")
def keep_awake():
    cup = p("M2.75 7H11V10.5A3.25 3.25 0 0 1 7.75 13.75H6A3.25 3.25 0 0 1 2.75 10.5Z")
    handle = p("M11 8H12A1.75 1.75 0 0 1 12 11.5H11")
    steam = p("M5.25 1.75C4.5 2.75 6 3.5 5.25 4.75") + p("M8.25 1.75C7.5 2.75 9 3.5 8.25 4.75")
    return cup + handle + steam

@reg("trindle-ring", "apps")
def trindle_ring():

    spots = [(12, 8), (11, 11), (8, 12), (5, 11), (4, 8), (5, 5), (8, 4), (11, 5)]
    return c(8, 8, 7, ' stroke-width="2"') + "".join(dot(x, y, 1) for x, y in spots)

@reg("edit-paste", "actions")
def paste():
    return p("M5.25 3H4A1.25 1.25 0 0 0 2.75 4.25V13A1.25 1.25 0 0 0 4 14.25H12A1.25 1.25 0 0 0 13.25 13V4.25"
             "A1.25 1.25 0 0 0 12 3H10.75") + r(5.25, 1.75, 5.5, 2.75, 1.2) + ln(5.5, 8.5, 10.5, 8.5) + ln(5.5, 11, 9, 11)

@reg("preferences-system-notifications", "categories")
def bell():
    return _bell()

@reg("notifications-disabled", "status")
def bell_off():
    return _bell() + ln(2, 2, 14, 14)

@reg("audio-volume-high", "status")
def vol_high():
    return _speaker() + arc(9, 8, 2.6, -55, 55) + arc(9, 8, 5, -55, 55)

@reg("audio-volume-medium", "status")
def vol_med():
    return _speaker() + arc(9, 8, 2.6, -55, 55) + arc(9, 8, 5, -55, 55, FAINT)

@reg("audio-volume-low", "status")
def vol_low():
    return _speaker() + arc(9, 8, 2.6, -55, 55, FAINT) + arc(9, 8, 5, -55, 55, FAINT)

@reg("audio-volume-muted", "status")
def vol_muted():
    return _speaker() + ln(11, 6, 14, 10) + ln(14, 6, 11, 10)

@reg("audio-headphones", "devices")
def headphones():
    return _headphones()

@reg("audio-headset", "devices")
def headset():
    return _headphones() + p("M3.25 14.25C5 14.75 7 14.5 8.5 13.5")

@reg("audio-input-microphone", "devices")
def mic():
    return _mic()

@reg("microphone-sensitivity-muted", "status")
def mic_muted():
    return _mic() + ln(2, 2, 14, 14)

@reg("audio-speakers", "devices")
def speakers():
    return r(3.25, 1.75, 9.5, 12.5, 2) + c(8, 9.75, 2.5) + dot(8, 4.75, 1)

@reg("audio-x-generic", "mimetypes")
def music():
    return c(4.75, 12, 2) + c(11.25, 10.5, 2) + p("M6.75 12V3.75L13.25 2.25V10.5")

@reg("network-wireless", "status")
def wifi():
    return _wifi(3)

@reg("network-wireless-signal-excellent", "status")
def wifi4():
    return _wifi(3)

@reg("network-wireless-signal-good", "status")
def wifi3():
    return _wifi(2)

@reg("network-wireless-signal-ok", "status")
def wifi2():
    return _wifi(1)

@reg("network-wireless-signal-weak", "status")
def wifi1():
    return _wifi(0)

@reg("network-wireless-signal-none", "status")
def wifi0():
    return _wifi(0, faint_dot=True)

@reg("network-wireless-offline", "status")
def wifi_off():
    return _wifi(0, faint_dot=True) + ln(2.5, 2.5, 13.5, 13.5)

@reg("network-wireless-encrypted", "status")
def wifi_lock():
    lock = rs(10.25, 11, 5, 4, 1) + p("M11.25 11V10A1.5 1.5 0 0 1 14.25 10V11", ' stroke-width="1.2"')
    return dot(6.5, 12.6, 1.3) + arc(6.5, 14, 3.8, 225, 315) + arc(6.5, 14, 7.1, 225, 300) + arc(6.5, 14, 10.4, 225, 290) + lock

@reg("network-wired", "status")
def wired():
    return r(5.25, 1.75, 5.5, 4, 1.2) + ln(8, 5.75, 8, 8.25) + p("M3.5 10.25V8.25H12.5V10.25") + r(1.75, 10.25, 4, 4, 1.2) + r(10.25, 10.25, 4, 4, 1.2)

@reg("network-wired-disconnected", "status")
def wired_off():
    return (r(5.25, 1.75, 5.5, 4, 1.2) + ln(8, 5.75, 8, 6.75) + p("M3.5 10.25V9.25M12.5 10.25V9.25") +
            r(1.75, 10.25, 4, 4, 1.2) + r(10.25, 10.25, 4, 4, 1.2) + ln(6, 8.5, 10, 8.5, FAINT))

@reg("network-offline", "status")
def net_off():
    return _globe() + ln(2, 2, 14, 14)

@reg("network-transmit-receive", "status")
def txrx():
    return p("M5 13.75V2.75M2.25 5.5L5 2.75L7.75 5.5") + p("M11 2.25V13.25M8.25 10.5L11 13.25L13.75 10.5")

@reg("network-vpn", "status")
def vpn():
    return p("M8 1.75L13.25 3.75V7.5C13.25 10.75 11 13 8 14.25C5 13 2.75 10.75 2.75 7.5V3.75Z") + c(8, 7.25, 1.6) + ln(8, 8.85, 8, 10.75)

@reg("network-server", "devices")
def server():
    return r(2.25, 1.75, 11.5, 5.25, 1.5) + r(2.25, 9, 11.5, 5.25, 1.5) + dot(5, 4.4, .9) + dot(5, 11.6, .9) + ln(8, 4.4, 11, 4.4) + ln(8, 11.6, 11, 11.6)

@reg("network-workgroup", "places")
def workgroup():
    return c(8, 3.75, 2) + c(3.25, 12, 2) + c(12.75, 12, 2) + ln(7, 5.5, 4.2, 10.2) + ln(9, 5.5, 11.8, 10.2) + ln(5.25, 12, 10.75, 12)

@reg("bluetooth-active", "status")
def bt():
    return p("M4.25 5L11.25 10.75L8 13.75V2.25L11.25 5.25L4.25 11")

@reg("bluetooth-disabled", "status")
def bt_off():
    return p("M4.25 5L11.25 10.75L8 13.75V2.25L11.25 5.25L4.25 11", FAINT) + ln(2, 2, 14, 14)

@reg("battery", "status")
def battery():
    return _battery(7.5)

@reg("battery-good", "status")
def battery_good():
    return _battery(5.5)

@reg("battery-caution", "status")
def battery_caution():
    return _battery(1.8)

@reg("battery-full-charging", "status")
def battery_charging():
    bolt = s("M8.3 3.5L5 8.5H7.4L6.6 12.5L10.4 7.2H8Z", f' stroke="{C}" stroke-width=".6" stroke-linejoin="round"')
    return r(1.75, 4.75, 11, 6.5, 2) + rs(13.3, 6.5, 1.4, 3, .6) + bolt

@reg("power-profile-balanced", "status")
def pp_balanced():
    return _gauge(270)

@reg("power-profile-performance", "status")
def pp_perf():
    return _gauge(320)

@reg("power-profile-power-saver", "status")
def pp_saver():
    return _gauge(220)

@reg("system-shutdown", "actions")
def shutdown():
    return arc(8, 8.5, 5.75, -55, 235) + ln(8, 1.75, 8, 7.5)

@reg("system-reboot", "actions")
def reboot():
    return arc(8, 8, 5.75, -60, 250) + p("M11.5 1.75L11.2 4.1L13.5 4.6")

@reg("system-log-out", "actions")
def logout():
    return p("M9.25 2.25H4A1.25 1.25 0 0 0 2.75 3.5V12.5A1.25 1.25 0 0 0 4 13.75H9.25") + ln(6.5, 8, 14, 8) + p("M11.25 5.25L14 8L11.25 10.75")

@reg("system-lock-screen", "actions")
def lock():
    return _padlock()

@reg("system-suspend", "actions")
def suspend():
    return p("M13.5 9.5A5.75 5.75 0 1 1 6.5 2.5A4.5 4.5 0 0 0 13.5 9.5Z")

@reg("system-hibernate", "actions")
def hibernate():
    out = ""
    for a in (90, 150, 210):
        x, y = 5.75 * math.cos(math.radians(a)), 5.75 * math.sin(math.radians(a))
        out += ln(8 - x, 8 - y, 8 + x, 8 + y)
    return out + c(8, 8, 1.4)

@reg("view-app-grid", "actions")
def app_grid():
    return "".join(dot(x, y, 1.35) for y in (3.5, 8, 12.5) for x in (3.5, 8, 12.5))

@reg("view-pin", "actions")
def pin():
    return (p("M6 2H10L9.5 6.25L12 8.75V9.75H4V8.75L6.5 6.25Z") + ln(8, 9.75, 8, 14.25))

@reg("window-close", "actions")
def close():
    return ln(4, 4, 12, 12) + ln(12, 4, 4, 12)

@reg("window-minimize", "actions")
def minimize():
    return ln(4, 11.5, 12, 11.5)

@reg("window-maximize", "actions")
def maximize():
    return r(3.75, 3.75, 8.5, 8.5, 1.75)

@reg("window-restore", "actions")
def restore():
    return r(2.75, 5.25, 8, 8, 1.75) + p("M5.25 2.75H11.5A1.75 1.75 0 0 1 13.25 4.5V10.75")

@reg("list-add", "actions")
def add():
    return ln(8, 3, 8, 13) + ln(3, 8, 13, 8)

@reg("list-remove", "actions")
def remove():
    return ln(3, 8, 13, 8)

@reg("accessories-dictionary", "apps")
def dictionary():
    return p("M3 12.75V3.25A1.5 1.5 0 0 1 4.5 1.75H13V11.25H4.5A1.5 1.5 0 0 0 3 12.75A1.5 1.5 0 0 0 4.5 14.25H13") + p("M7 1.75V6.5L8.25 5.5L9.5 6.5V1.75")

@reg("action-unavailable", "status")
def unavailable():
    return c(8, 8, 6.25) + ln(3.6, 3.6, 12.4, 12.4)

@reg("applications-engineering", "categories")
def engineering():
    return p("M2.25 13.75V2.25L13.75 13.75Z") + p("M5.25 10.75V9.25L6.75 10.75Z") + ln(2.25, 5.5, 3.5, 5.5) + ln(2.25, 8.5, 3.5, 8.5)

@reg("applications-games", "categories")
def games():
    return _pad()

@reg("applications-graphics", "categories")
def graphics():
    return (p("M8 1.75A6.25 6.25 0 1 0 8 14.25C9 14.25 9.5 13.5 9 12.5C8.4 11.3 9.2 10 10.5 10H12"
              "A2.25 2.25 0 0 0 14.25 7.75C14.25 4.4 11.5 1.75 8 1.75Z") +
            dot(4.75, 7.5, 1) + dot(6.5, 4.5, 1) + dot(9.75, 4.5, 1))

@reg("applications-multimedia", "categories")
def multimedia():
    return c(8, 8, 6.25) + s("M6.5 5.2V10.8A.5.5 0 0 0 7.25 11.2L11.3 8.4A.5.5 0 0 0 11.3 7.6L7.25 4.8A.5.5 0 0 0 6.5 5.2Z")

@reg("applications-other", "categories")
def other():
    return r(2.25, 2.25, 4.75, 4.75, 1.5) + r(9, 2.25, 4.75, 4.75, 1.5) + r(2.25, 9, 4.75, 4.75, 1.5) + c(11.4, 11.4, 2.4)

@reg("applications-science", "categories")
def science():
    return p("M6 1.75V6L2.4 12.5A1.2 1.2 0 0 0 3.45 14.25H12.55A1.2 1.2 0 0 0 13.6 12.5L10 6V1.75") + ln(5, 1.75, 11, 1.75) + ln(4.25, 10, 11.75, 10)

@reg("applications-system", "categories")
def app_system():
    return _gear()

@reg("applications-utilities", "categories")
def utilities():
    return p("M9.5 2.2A3.5 3.5 0 0 0 7.6 7.1L2.5 12.2A1.2 1.2 0 0 0 4.2 13.9L9.3 8.8A3.5 3.5 0 0 0 14.2 6.9L12 7.1L9.8 4.6Z")

@reg("application-x-executable", "mimetypes")
def executable():
    return _gear(8, 8, 5.4, 1.8)

@reg("avatar-default", "status")
def avatar():
    return c(8, 8, 6.25) + c(8, 6.5, 2.1) + p("M4 12.4A4.5 4.5 0 0 1 12 12.4")

@reg("camera-photo", "devices")
def camera():
    return p("M1.75 5.5A1.25 1.25 0 0 1 3 4.25H4.75L6 2.5H10L11.25 4.25H13A1.25 1.25 0 0 1 14.25 5.5V12"
             "A1.25 1.25 0 0 1 13 13.25H3A1.25 1.25 0 0 1 1.75 12Z") + c(8, 8.5, 2.6)

@reg("changes-prevent", "status")
def prevent():
    return _padlock()

@reg("computer", "devices")
def computer():
    return r(2.75, 2.75, 10.5, 7.75, 1.5) + p("M1.25 13.25H14.75L13.25 10.5H2.75Z")

@reg("dialog-error", "status")
def error():
    return c(8, 8, 6.25) + ln(5.75, 5.75, 10.25, 10.25) + ln(10.25, 5.75, 5.75, 10.25)

@reg("dialog-information", "status")
def info():
    return c(8, 8, 6.25) + ln(8, 7.25, 8, 11) + dot(8, 4.9, 1)

@reg("dialog-password", "status")
def password():
    return c(5, 8, 3.25) + ln(8.25, 8, 14.25, 8) + ln(12, 8, 12, 10.5) + ln(14.25, 8, 14.25, 10)

@reg("dialog-warning", "status")
def warning():
    return p("M7 2.6A1.15 1.15 0 0 1 9 2.6L14.3 12.3A1.15 1.15 0 0 1 13.3 14H2.7A1.15 1.15 0 0 1 1.7 12.3Z") + ln(8, 6, 8, 9) + dot(8, 11.5, 1)

@reg("document-edit", "actions")
def edit():
    return p("M10.5 2.5A1.75 1.75 0 0 1 13 5L5.5 12.5L2.25 13.75L3.5 10.5Z") + ln(9.25, 3.75, 11.75, 6.25)

@reg("document-open", "actions")
def doc_open():
    return _folder(open_=True)

@reg("document-print", "actions")
def doc_print():
    return _printer()

@reg("document-revert", "actions")
def revert():
    return arc(8, 8, 5.75, -110, 200) + p("M2.1 3.2L2.4 6.2L5.4 5.8")

@reg("document-save-as", "actions")
def save_as():
    return (p("M9 14.25H3A1.25 1.25 0 0 1 1.75 13V3A1.25 1.25 0 0 1 3 1.75H11L14.25 5V7") + r(4.5, 1.75, 5, 3.5, .8) +
            p("M12.5 8.75A1.1 1.1 0 0 1 14.1 10.3L10.5 13.9L8.75 14.25L9.1 12.5Z"))

@reg("drive-harddisk", "devices")
def harddisk():
    return r(1.75, 4.25, 12.5, 7.5, 2) + dot(11.25, 8, 1) + ln(4.5, 8, 8, 8)

@reg("edit-clear", "actions")
def clear():
    return p("M5.5 3.25H13A1.25 1.25 0 0 1 14.25 4.5V11.5A1.25 1.25 0 0 1 13 12.75H5.5L1.75 8Z") + ln(7.75, 6, 11.25, 10) + ln(11.25, 6, 7.75, 10)

@reg("edit-copy", "actions")
def copy():
    return r(5.25, 5.25, 9, 9, 1.75) + p("M10.75 2.75V2.25A.5.5 0 0 0 10.25 1.75H3A1.25 1.25 0 0 0 1.75 3V10.25A.5.5 0 0 0 2.25 10.75H2.75")

@reg("edit-find", "actions")
def find():
    return c(6.75, 6.75, 4.75) + ln(10.2, 10.2, 14, 14)

@reg("edit-redo", "actions")
def redo():
    return p("M13.5 6.5H5.5A3.5 3.5 0 0 0 5.5 13.5H8") + p("M10.5 3.5L13.5 6.5L10.5 9.5")

@reg("edit-undo", "actions")
def undo():
    return p("M2.5 6.5H10.5A3.5 3.5 0 0 1 10.5 13.5H8") + p("M5.5 3.5L2.5 6.5L5.5 9.5")

@reg("emblem-favorite", "emblems")
def heart():
    return s("M8 14C8 14 1.5 10 1.5 5.6A3.3 3.3 0 0 1 8 4.3A3.3 3.3 0 0 1 14.5 5.6C14.5 10 8 14 8 14Z")

@reg("emblem-ok", "emblems")
def ok():
    return c(8, 8, 6.25) + dot(8, 8, 2.2)

@reg("emblem-system", "emblems")
def emblem_system():
    return _gear()

@reg("folder-download", "places")
def folder_dl():
    return _folder() + ln(8, 6, 8, 11) + p("M5.75 9L8 11.25L10.25 9")

@reg("folder-open", "places")
def folder_open():
    return _folder(open_=True)

@reg("folder", "places")
def folder():
    return _folder()

@reg("github", "apps")
def github():
    cat = s("M4.6 5.6L4.4 3.1L6.4 4.5A5.4 5.4 0 0 1 9.6 4.5L11.6 3.1L11.4 5.6A4.4 4.4 0 0 1 12.2 8.2"
            "C12.2 10.6 10.6 11.8 8 11.8C5.4 11.8 3.8 10.6 3.8 8.2A4.4 4.4 0 0 1 4.6 5.6Z")
    return c(8, 8, 6.75) + cat + p("M6.5 11.8V14.4M9.5 11.8V14.4")

@reg("go-bottom", "actions")
def go_bottom():
    return ln(8, 2, 8, 10) + p("M4.5 6.75L8 10.25L11.5 6.75") + ln(3.5, 13.75, 12.5, 13.75)

@reg("go-next", "actions")
def go_next():
    return p("M6 3L11 8L6 13")

@reg("go-previous", "actions")
def go_prev():
    return p("M10 3L5 8L10 13")

@reg("help-browser", "apps")
def help_():
    return c(8, 8, 6.25) + p("M6.1 6.2A2 2 0 0 1 9.9 6.4C9.9 7.9 8 8 8 9.5") + dot(8, 11.6, 1)

@reg("image-x-generic", "mimetypes")
def image():
    return r(1.75, 2.75, 12.5, 10.5, 2) + p("M1.75 11L5.5 7.5L9.5 11.25M8 9.75L10 8L14.25 11.5") + c(10.5, 5.75, 1.1)

@reg("input-gaming", "devices")
def gaming():
    return _pad()

@reg("input-mouse", "devices")
def mouse():
    return r(4, 1.75, 8, 12.5, 4) + ln(8, 4.25, 8, 6.75)

@reg("media-eject", "actions")
def eject():
    return s("M7.3 2.9A.9.9 0 0 1 8.7 2.9L13 8.4A.8.8 0 0 1 12.4 9.75H3.6A.8.8 0 0 1 3 8.4Z") + rs(3, 11.5, 10, 2, 1)

@reg("media-floppy", "devices")
def floppy():
    return (p("M3 1.75H11L14.25 5V13A1.25 1.25 0 0 1 13 14.25H3A1.25 1.25 0 0 1 1.75 13V3A1.25 1.25 0 0 1 3 1.75Z") +
            r(4.5, 1.75, 5.5, 3.5, .8) + r(4.25, 9, 7.5, 5.25, .8))

@reg("media-playback-start", "actions")
def play():
    return s("M4.5 2.9V13.1A.9.9 0 0 0 5.9 13.9L13.3 8.8A.95.95 0 0 0 13.3 7.2L5.9 2.1A.9.9 0 0 0 4.5 2.9Z")

@reg("media-playback-stop", "actions")
def stop():
    return rs(3, 3, 10, 10, 2)

@reg("media-removable", "devices")
def removable():
    return r(4.25, 5.75, 7.5, 8.5, 1.75) + p("M5.75 5.75V1.75H10.25V5.75") + dot(7, 3.75, .6) + dot(9, 3.75, .6)

@reg("object-select", "actions")
def select():
    return dot(8, 8, 3.25)

@reg("package-x-generic", "mimetypes")
def package():
    return p("M8 1.75L14 4.75V11.25L8 14.25L2 11.25V4.75Z") + p("M2 4.75L8 7.75L14 4.75M8 7.75V14.25") + ln(5, 3.25, 11, 6.25)

@reg("pan-down", "actions")
def pan_down():
    return p("M4.5 6.5L8 10L11.5 6.5")

@reg("phone", "devices")
def phone():
    return r(4, 1.75, 8, 12.5, 2) + ln(7, 11.75, 9, 11.75)

@reg("preferences-desktop-locale", "categories")
def locale():
    return _globe()

@reg("preferences-desktop-screensaver", "categories")
def screensaver():
    return _monitor() + p("M10.5 7.75A2.9 2.9 0 1 1 7.6 4.3A2.3 2.3 0 0 0 10.5 7.75Z")

@reg("preferences-desktop-wallpaper", "categories")
def wallpaper():
    return _monitor() + p("M4 8.5L6.5 6L8.75 8.25L10 7L12 9") + dot(10.5, 4.5, .9)

@reg("preferences-system", "categories")
def prefs_system():
    return _gear()

@reg("preferences-system-time", "categories")
def time_():
    return c(8, 8, 6.25) + p("M8 4.5V8L10.5 9.5")

@reg("printer", "devices")
def printer():
    return _printer()

@reg("printer-network", "devices")
def printer_net():
    return (p("M4.5 5.25V2.5A.75.75 0 0 1 5.25 1.75H10.75A.75.75 0 0 1 11.5 2.5V5.25") +
            p("M4.5 11.5H3A1.25 1.25 0 0 1 1.75 10.25V6.5A1.25 1.25 0 0 1 3 5.25H13A1.25 1.25 0 0 1 14.25 6.5V7.5") +
            r(4.5, 9, 4.5, 5.25, .75) + dot(12, 11, 1) + arc(12, 13.6, 2.6, 225, 315) + dot(10.4, 14.4, .01))

@reg("software-update-available", "status")
def update():
    return c(8, 8, 6.25) + ln(8, 4.5, 8, 11) + p("M5.25 8.5L8 11.25L10.75 8.5")

@reg("starred", "status")
def starred():
    pts = []
    for k in range(10):
        rad = 6.6 if k % 2 == 0 else 2.9
        a = math.radians(-90 + 36 * k)
        pts.append((8 + rad * math.cos(a), 8.4 + rad * math.sin(a)))
    return s("M" + "L".join(f"{n(x)} {n(y)}" for x, y in pts) + "Z",
             f' stroke="{C}" stroke-width="1.2" stroke-linejoin="round"')

@reg("system-run", "actions")
def run():
    return _gear(8, 8, 6.2, 0.01) + s("M6.6 5.6V10.4A.4.4 0 0 0 7.2 10.7L10.6 8.3A.4.4 0 0 0 10.6 7.7L7.2 5.3A.4.4 0 0 0 6.6 5.6Z")

@reg("system-users", "status")
def users():
    return (c(6, 5, 2.25) + p("M1.75 13.25A4.25 4 0 0 1 10.25 13.25") + p("M10.5 2.9A2.25 2.25 0 0 1 10.5 7.1") +
            p("M12 9.6A4.2 4 0 0 1 14.25 13.25"))

@reg("user-trash", "places")
def trash():
    return ln(2.25, 4, 13.75, 4) + p("M6 4V2.75A1 1 0 0 1 7 1.75H9A1 1 0 0 1 10 2.75V4") + p("M3.75 4L4.5 13A1.4 1.4 0 0 0 5.9 14.25H10.1A1.4 1.4 0 0 0 11.5 13L12.25 4") + ln(6.75, 7, 6.75, 11) + ln(9.25, 7, 9.25, 11)

@reg("utilities-system-monitor", "apps")
def sysmon():
    return r(1.75, 2.25, 12.5, 11.5, 2) + p("M3.75 8.5H5.75L7 5.5L9 11L10.25 8.5H12.25")

@reg("utilities-terminal", "apps")
def terminal():
    return r(1.75, 2.25, 12.5, 11.5, 2) + p("M4.5 6L6.75 8.25L4.5 10.5") + ln(8.5, 10.5, 11.5, 10.5)

@reg("video-display", "devices")
def display():
    return _monitor()

@reg("view-fullscreen", "actions")
def fullscreen():
    return p("M2.25 6V3.5A1.25 1.25 0 0 1 3.5 2.25H6M10 2.25H12.5A1.25 1.25 0 0 1 13.75 3.5V6M13.75 10V12.5A1.25 1.25 0 0 1 12.5 13.75H10M6 13.75H3.5A1.25 1.25 0 0 1 2.25 12.5V10")

@reg("view-more", "actions")
def more():
    return dot(8, 3.25, 1.4) + dot(8, 8, 1.4) + dot(8, 12.75, 1.4)

@reg("view-refresh", "actions")
def refresh():
    return arc(8, 8, 5.75, 200, 500) + p("M13.9 1.9L13.6 5.1L10.5 4.8")

@reg("view-reveal", "actions")
def reveal():
    return p("M1.5 8C3 5 5.3 3.5 8 3.5C10.7 3.5 13 5 14.5 8C13 11 10.7 12.5 8 12.5C5.3 12.5 3 11 1.5 8Z") + c(8, 8, 2.1)

@reg("web-browser", "apps")
def web():
    return _globe()

@reg("x-office-document", "mimetypes")
def document():
    return _doc() + ln(5.5, 4.5, 7.5, 4.5)

def _flip(body):
    """The same drawing mirrored left to right."""
    return f'<g transform="matrix(-1 0 0 1 16 0)">{body}</g>'

def _turn(body, deg):
    return f'<g transform="rotate({deg} 8 8)">{body}</g>'

def _plus(cx, cy, h=2.5):
    return ln(cx - h, cy, cx + h, cy) + ln(cx, cy - h, cx, cy + h)

def _house():
    return (p("M2.25 7.25L8 2.25L13.75 7.25") + p("M3.75 6V13A1.25 1.25 0 0 0 5 14.25H11A1.25 1.25 0 0 0 12.25 13V6") +
            p("M6.5 14.25V10.75A1 1 0 0 1 7.5 9.75H8.5A1 1 0 0 1 9.5 10.75V14.25"))

def _skip():
    return s("M3.5 3.3V12.7A.8.8 0 0 0 4.75 13.35L10.9 8.65A.8.8 0 0 0 10.9 7.35L4.75 2.65A.8.8 0 0 0 3.5 3.3Z") + rs(11.75, 2.5, 1.75, 11, .8)

def _seek():
    tri = "M{a} 4.2V11.8A.7.7 0 0 0 {b} 12.35L{c} 8.55A.7.7 0 0 0 {c} 7.45L{b} 3.65A.7.7 0 0 0 {a} 4.2Z"
    return (s(tri.format(a=1.5, b=2.6, c=7.5)) + s(tri.format(a=8, b=9.1, c=14)))

def _arrow_up():
    return ln(8, 13.5, 8, 2.75) + p("M3.75 7L8 2.75L12.25 7")

def _to_top():
    return ln(8, 14, 8, 6) + p("M4.5 9.25L8 5.75L11.5 9.25") + ln(3.5, 2.25, 12.5, 2.25)

@reg("media-playback-pause", "actions")
def pause():
    return rs(3.75, 2.5, 3, 11, 1) + rs(9.25, 2.5, 3, 11, 1)

@reg("media-skip-forward", "actions")
def skip_fwd():
    return _skip()

@reg("media-skip-backward", "actions")
def skip_back():
    return _flip(_skip())

@reg("media-seek-forward", "actions")
def seek_fwd():
    return _seek()

@reg("media-seek-backward", "actions")
def seek_back():
    return _flip(_seek())

@reg("media-record", "actions")
def record():
    return dot(8, 8, 5.25)

@reg("media-playlist-repeat", "actions")
def repeat():
    return (p("M2.75 9.25V7A2.25 2.25 0 0 1 5 4.75H12.75") + p("M10.75 2.75L12.75 4.75L10.75 6.75") +
            p("M13.25 6.75V9A2.25 2.25 0 0 1 11 11.25H3.25") + p("M5.25 13.25L3.25 11.25L5.25 9.25"))

@reg("media-playlist-shuffle", "actions")
def shuffle():
    return (p("M1.75 4.75H3.75C7.25 4.75 8.75 11.25 12.25 11.25H14") + p("M1.75 11.25H3.75C7.25 11.25 8.75 4.75 12.25 4.75H14") +
            p("M12.25 3L14 4.75L12.25 6.5") + p("M12.25 9.5L14 11.25L12.25 13"))

@reg("edit-delete", "actions")
def delete():
    return trash()

@reg("edit-cut", "actions")
def cut():
    return c(4.5, 11.5, 2.25) + c(11.5, 11.5, 2.25) + ln(6.1, 9.9, 11.75, 2) + ln(9.9, 9.9, 4.25, 2)

@reg("edit-select-all", "actions")
def select_all():
    edge = [(x, y) for x in (2.25, 5.1, 7.95, 10.8, 13.75) for y in (2.25, 13.75)] + \
           [(x, y) for x in (2.25, 13.75) for y in (5.1, 7.95, 10.8)]
    return "".join(dot(x, y, .85) for x, y in edge) + rs(5.25, 5.25, 5.5, 5.5, 1.2)

@reg("document-save", "actions")
def save():
    return floppy()

@reg("document-new", "actions")
def doc_new():
    return _doc(lines=False) + _plus(7.5, 9.25)

@reg("folder-new", "actions")
def folder_new():
    return _folder() + _plus(8, 8.5, 2.25)

@reg("window-new", "actions")
def window_new():
    return r(1.75, 2.25, 12.5, 11.5, 2) + ln(1.75, 5.5, 14.25, 5.5) + _plus(8, 9.6, 2.1)

@reg("tab-new", "actions")
def tab_new():
    return r(1.75, 2.25, 12.5, 11.5, 2) + ln(1.75, 5.5, 14.25, 5.5) + ln(7.25, 2.25, 7.25, 5.5) + _plus(8, 9.6, 2.1)

@reg("go-up", "actions")
def go_up():
    return _arrow_up()

@reg("go-down", "actions")
def go_down():
    return _turn(_arrow_up(), 180)

@reg("go-top", "actions")
def go_top():
    return _to_top()

@reg("go-first", "actions")
def go_first():
    return p("M11.5 3L6.5 8L11.5 13") + ln(3.75, 3, 3.75, 13)

@reg("go-last", "actions")
def go_last():
    return _flip(go_first())

@reg("go-home", "actions")
def go_home():
    return _house()

@reg("user-home", "places")
def user_home():
    return _house()

@reg("pan-up", "actions")
def pan_up():
    return p("M4.5 9.5L8 6L11.5 9.5")

@reg("pan-start", "actions")
def pan_start():
    return p("M9.5 4.5L6 8L9.5 11.5")

@reg("pan-end", "actions")
def pan_end():
    return p("M6.5 4.5L10 8L6.5 11.5")

@reg("zoom-out", "actions")
def zoom_out():
    return find() + ln(4.75, 6.75, 8.75, 6.75)

@reg("zoom-original", "actions")
def zoom_original():
    return find() + ln(6.75, 4.5, 6.75, 9) + ln(5.6, 5.4, 6.75, 4.5)

@reg("zoom-fit-best", "actions")
def zoom_fit():
    return (p("M2.25 5.5V3.5A1.25 1.25 0 0 1 3.5 2.25H5.5M10.5 2.25H12.5A1.25 1.25 0 0 1 13.75 3.5V5.5"
              "M13.75 10.5V12.5A1.25 1.25 0 0 1 12.5 13.75H10.5M5.5 13.75H3.5A1.25 1.25 0 0 1 2.25 12.5V10.5") +
            r(5.25, 5.25, 5.5, 5.5, 1.2))

@reg("view-list", "actions")
def view_list():
    return "".join(dot(3, y, 1.1) + ln(6, y, 13.75, y) for y in (3.5, 8, 12.5))

@reg("view-grid", "actions")
def view_grid():
    return "".join(r(x, y, 4.75, 4.75, 1.25) for x in (2.25, 9) for y in (2.25, 9))

@reg("view-sort-ascending", "actions")
def sort_up():
    return ln(2, 3.5, 6, 3.5) + ln(2, 8, 8, 8) + ln(2, 12.5, 10, 12.5) + ln(12.5, 12.75, 12.5, 3) + p("M10.25 5.25L12.5 3L14.75 5.25")

@reg("view-sort-descending", "actions")
def sort_down():
    return ln(2, 3.5, 10, 3.5) + ln(2, 8, 8, 8) + ln(2, 12.5, 6, 12.5) + ln(12.5, 3.25, 12.5, 13) + p("M10.25 10.75L12.5 13L14.75 10.75")

@reg("view-conceal", "actions")
def conceal():
    return reveal() + slash()

@reg("view-restore", "actions")
def view_restore():
    return p("M6 2.25V4.75A1.25 1.25 0 0 1 4.75 6H2.25M10 2.25V4.75A1.25 1.25 0 0 0 11.25 6H13.75"
             "M13.75 10H11.25A1.25 1.25 0 0 0 10 11.25V13.75M6 13.75V11.25A1.25 1.25 0 0 0 4.75 10H2.25")

@reg("open-menu", "actions")
def open_menu():
    return ln(2.5, 4, 13.5, 4) + ln(2.5, 8, 13.5, 8) + ln(2.5, 12, 13.5, 12)

@reg("mail-send", "actions")
def mail_send():
    return p("M14.25 1.75L1.75 6.75L6.75 9.25L9.25 14.25Z") + ln(6.75, 9.25, 14.25, 1.75)

@reg("bookmark-new", "actions")
def bookmark_new():
    return p("M4 2.75A1 1 0 0 1 5 1.75H11A1 1 0 0 1 12 2.75V14.25L8 11.25L4 14.25Z") + _plus(8, 6.5, 2)

@reg("insert-link", "actions")
def link():
    return (p("M6.9 9.1A2.75 2.75 0 0 0 10.8 9.1L13.1 6.8A2.75 2.75 0 0 0 9.2 2.9L8.1 4") +
            p("M9.1 6.9A2.75 2.75 0 0 0 5.2 6.9L2.9 9.2A2.75 2.75 0 0 0 6.8 13.1L7.9 12"))

@reg("system-search", "actions")
def system_search():
    return find()

@reg("dialog-question", "status")
def question():
    return help_()

@reg("help-about", "actions")
def help_about():
    return info()

@reg("help-contents", "actions")
def help_contents():
    return help_()

@reg("help-faq", "actions")
def help_faq():
    return help_()

def _tip(x, y, deg, k=2.6):
    """Arrowhead whose tip is at (x, y), pointing towards deg."""
    a, b = math.radians(deg + 145), math.radians(deg - 145)
    return p(f"M{n(x + k * math.cos(a))} {n(y + k * math.sin(a))}L{n(x)} {n(y)}"
             f"L{n(x + k * math.cos(b))} {n(y + k * math.sin(b))}")

def _spin(clockwise):
    """Most of a circle with an arrowhead, for turning a picture."""
    a0, a1 = (150, 380) if clockwise else (160, 390)
    body = arc(8, 8.5, 5.5, a0, a1)
    end = a1 if clockwise else a0
    x, y = 8 + 5.5 * math.cos(math.radians(end)), 8.5 + 5.5 * math.sin(math.radians(end))
    return body + _tip(x, y, end + 90 if clockwise else end - 90)

@reg("trindle-folders-install-font", "actions")
def folders_install_font():
    letter = p("M1.75 13.5L5.5 2.75L9.25 13.5") + ln(3.25, 9.75, 7.75, 9.75)
    arrow = ln(12.75, 2.75, 12.75, 10.25) + p("M10.5 8L12.75 10.25L15 8") + ln(10.75, 13.5, 14.75, 13.5)
    return letter + arrow

@reg("trindle-folders-checksum", "actions")
def folders_checksum():
    page = p("M3.25 2.75A1 1 0 0 1 4.25 1.75H9.25L12.75 5.25V13.25A1 1 0 0 1 11.75 14.25H4.25A1 1 0 0 1 3.25 13.25Z")
    return page + ln(7.1, 6.9, 6.4, 11.6) + ln(9.8, 6.9, 9.1, 11.6) + ln(5.4, 8.3, 10.6, 8.3) + ln(5.1, 10.3, 10.3, 10.3)

@reg("trindle-folders-forget", "actions")
def folders_forget():
    return _folder() + ln(6.25, 7.25, 9.75, 10.75) + ln(9.75, 7.25, 6.25, 10.75)

@reg("trindle-folders-rotate-left", "actions")
def folders_rotate_left():
    return _spin(False)

@reg("trindle-folders-rotate-right", "actions")
def folders_rotate_right():
    return _spin(True)

@reg("trindle-folders-rotate-half", "actions")
def folders_rotate_half():
    return p("M3 14V8A5 5 0 0 1 13 8V13.25") + _tip(13, 13.75, 90)

@reg("trindle-folders-resize", "actions")
def folders_resize():
    return ln(3, 13, 13, 3) + p("M8.5 2.75H13.25V7.5") + p("M2.75 8.5V13.25H7.5")

@reg("trindle-folders-type-location", "actions")
def folders_type_location():
    return r(1.25, 4.25, 13.5, 7.5, 2) + ln(4, 8, 7.25, 8) + ln(9.75, 6.25, 9.75, 9.75)

@reg("scanner", "devices")
def scanner():
    bed = r(1.75, 8.75, 12.5, 4.75, 1.5)
    lid = p("M4.75 8.75V3.25H11.25V8.75")
    return bed + lid + ln(4.5, 11.1, 11.5, 11.1)

@reg("network-home", "status")
def network_home():
    house = p("M1.5 13.25V7.25L4.5 4.25L7.5 7.25V13.25Z")
    return house + dot(10, 12.5, 1.1) + arc(10, 12.5, 2.8, 270, 360) + arc(10, 12.5, 4.5, 270, 360)

@reg("usb", "devices")
def usb():
    plug = r(5, 1.75, 6, 6, 1) + r(3.75, 7.75, 8.5, 6.5, 1.5)
    return plug + rs(6.4, 3.6, 1.1, 1.7, .4) + rs(8.5, 3.6, 1.1, 1.7, .4)
