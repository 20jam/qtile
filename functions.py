#!/usr/bin/env python

import os
import subprocess
from libqtile.command import lazy

try:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
    from gi.repository.GLib import Variant as gi_variant
    FAILED_NOTIFY = False
except Exception:
    FAILED_NOTIFY = True

Notify.init("notifications")
notification = Notify.Notification.new("", "")

# from libqtile import manager

# functions

class Function(object):

    # Control volume

    @staticmethod
    def volume_ctl(vol):
        @lazy.function
        def __inner(qtile):
            sign = '+' if vol > 0 else '-'
            subprocess.Popen(
                f"pactl set-sink-volume @DEFAULT_SINK@ {sign}{abs(vol)}%",
                shell=True, text=True)
            if not FAILED_NOTIFY:
                cur_vol = int(subprocess.Popen(
                    'pamixer --get-volume', shell=True, text=True,
                    stdout=subprocess.PIPE).communicate()[0][:-1])
                icon = 'audio-volume-muted'
                if cur_vol >= 70:
                    icon = 'audio-volume-high'
                elif cur_vol >= 40:
                    icon = 'audio-volume-medium'
                elif cur_vol > 0:
                    icon = 'audio-volume-low'
                notification.update('Volume Changed', '', icon)
                notification.set_hint('value', gi_variant.new_int32(cur_vol))
                notification.show()
        return __inner

    @staticmethod
    def moveto_next_empty_group():
        @lazy.function
        def __inner(qtile):
            subprocess.Popen(
                os.path.expanduser('~/.config/qtile/scripts/tonext_emptygroup.py'))
        return __inner

    @staticmethod
    def to_next_empty_group():
        @lazy.function
        def __inner(qtile):
            subprocess.Popen(
                os.path.expanduser('~/.config/qtile/scripts/next_emptygroup.py'))
        return __inner

# Hides Topbar -------------------------------------------------------------------

    # @staticmethod

# Keymaps


    # Key([mod, 'shift'], 'b', lazy.function(toggle_bar)),
    #
    # Key([mod, "shift", "control"], "x",
    #     lazy.spawn("i3lock -e -B --force-clock --keylayout 0"
    #                " --insidecolor 1e58a46a --indicator")),
    #
    # Key([], "XF86AudioRaiseVolume", volume_ctl(5)),
    # Key([], "XF86AudioLowerVolume", volume_ctl(-10)),
    # Key([], "XF86MonBrightnessUp", brightness_ctl(2)),
    # Key([], "XF86MonBrightnessDown", brightness_ctl(-5)),

 #    Key([mod], "v", to_next_empty_group()),
 #    Key([mod, 'shift'], "v", moveto_next_empty_group()),
 #
 # Key([mod], 'F4', lazy.spawn('xkill')), Key([mod], 'F4', lazy.spawn('xkill')),


    # Control Brightness

    # @staticmethod
    # def brightness_ctl(vlu):
    #     @lazy.function
    #     def __inner(qtile):
    #         symbol = 'A' if vlu > 0 else 'U'
    #         subprocess.Popen(
    #             f"light -{symbol} {abs(vlu)}",
    #             shell=True, text=True)
    #         if not FAILED_NOTIFY:
    #             cur_bright = float(subprocess.Popen(
    #                 f'light', shell=True, text=True,
    #                 stdout=subprocess.PIPE).communicate()[0][:-1])
    #             # icon = 'display-brightness-off'
    #             # if cur_bright >= 70:
    #             #     icon = 'display-brightness-high'
    #             # elif cur_bright >= 40:
    #             #     icon = 'display-brightness-medium'
    #             # elif cur_bright > 0:
    #             #     icon = 'display-brightness-low'
    #             notification.update('Brightness Changed', '', icon)
    #             notification.set_hint('value', gi_variant.new_int32(cur_bright))
    #             notification.show()
    #     return __inner
