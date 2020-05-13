#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports

import os
import re
import socket
import subprocess
from libqtile.config import Key, EzKey, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List
from functions import Function
# import libqtile.core.manager

# Settings

wmname = "LG3D"
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
auto_fullscreen = True
focus_on_window_activation = "smart"
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])


# Simple Varialbes

mod = "mod1"

WEB = "firefox"
TERM = "st"
FILE = "st -e ranger"
HOME = os.path.expanduser("~")


# Custom Commands

RUN = "dmenu_run -p 'Run: '"
SEARCH = 'dsurf'
EDITCONF = 'deditconfig'
YOUTUBEMUSIC = TERM+" -e straw-viewer -n" # spawn yt search
AUDIOAPP = TERM+" -e pulsemixer" # spawn audio control app
TODOLIST = "dtodo" # show a list of todos
SPAWNTERM = "via" # spawn term in specfic wd
NETWORKSELECT = ""
BRIGHUP = "brightnessctl set +5%"
BRIGHDOWN = "brightnessctl set 5%-"
#

# Keys Config {{{
keymap = {
    # ~: System Control: ------------------------------------------------------

    "M-C-r"         : lazy.restart(),                       # Restart Qtile
    "M-C-x"         : lazy.shutdown(),                      # Exit Qtile
    "M-C-d"         : lazy.spawn("displayselect"),          # Configure Display
    "M-C-a"         : lazy.spawn(AUDIOAPP),                 # Audio controler
    "M-<equal>"     : Function.volume_ctl(10),              # Audio (+10)
    "M-<minus>"     : Function.volume_ctl(-10),             # Audio (-10)
    "M-<F2>"        : lazy.spawn(BRIGHUP),                  # brightness (+5)
    "M-<F1>"        : lazy.spawn(BRIGHDOWN),                # brightness (-5)

    # ~: Windows, Groups and Layout Contol : ----------------------------------

    "M-j"           : lazy.group.prev_window(),             # Window Focus up
    "M-k"           : lazy.group.next_window(),             # Window Focus Down
    "M-C-j"         : lazy.layout.shuffle_up(),             # Window Move up
    "M-C-k"         : lazy.layout.shuffle_down(),           # Window Move Down
    "M-C-q"         : lazy.window.kill(),                   # Quit Force
    "M-q"           : lazy.window.kill(),                   # Quit Normal

    "M-f"           : lazy.window.toggle_fullscreen(),      # Window Fullscreen
    "M-i"           : lazy.layout.shrink(),                 # Window Shrink
    "M-o"           : lazy.layout.grow(),                   # Window Grow
    "M-n"           : lazy.layout.normalize(),
    "M-m"           : lazy.layout.maximize(),
    "M-<slash>"     : lazy.layout.flip(),                   # Flip


    "M-<semicolon>" : lazy.screen.next_group(),             # Desktop Next
    "M-g"           : lazy.screen.prev_group(),             # Desktop Prev
    "M-<space>"     : lazy.screen.toggle_group(),           # Desktop ToggleLast


    "M-<Tab>"       : lazy.next_layout(),                   # Next Layout


    # ~: Launchers : ----------------------------------------------------

    "M-<Return>"    : lazy.spawn(TERM),                     # Terminal
    "M-C-<Return>"  : lazy.spawn(SPAWNTERM),                # TERM in a wd
    "M-r"           : lazy.spawn(FILE),                     # File Browser
    "M-w"           : lazy.spawn(WEB),                      # Web Browser
    "M-d"           : lazy.spawn(RUN),                      # Runners
    "M-s"           : lazy.spawn(SEARCH),                   # search the web
    "M-e"           : lazy.spawn(EDITCONF),                 # edit dotfiles
    "M-y"           : lazy.spawn(YOUTUBEMUSIC),             # Youtube Music
    "M-t"           : lazy.spawn(TODOLIST),                 # Todos list
    "M-C-n"         : lazy.spawn(NETWORKSELECT),            # Select Wifi

    # TODO Choice a set of layout and for every choicen layout there is a key.
    # Switch to MonadTall
    # "M-"       : lazy.next_layout(),                   # Next Layout
    # Switch to MonadWide
    # Switch to Zoomy or Max
    # Switch to Matrix
    # "M-<period>"             : Function.to_next_empty_group(),             # Desktop Next
    # "M-S-<period>"           : Function.moveto_next_empty_group(),             # Desktop Prev
}

groups = [Group(i) for i in "123456789"]
for i in groups:
    keymap[f'M-{i.name}'] = lazy.group[i.name].toscreen()
    keymap[f'M-S-{i.name}'] = lazy.window.togroup(i.name)

keys = [EzKey(k, v) for k, v in keymap.items()]

# }}}

layout_theme = {"border_width": 3,
                "margin": 14,
                "border_focus": "c5c8c6",
                "border_normal": "1d1f21"
                }

layouts = [
    layout.MonadTall(**layout_theme), #T
    layout.Max(**layout_theme),
    layout.MonadWide(**layout_theme), #W
    # layout.Stack(stacks=2, **layout_theme),
            # This layout is great for having one window on the right for the main work
            # and one on the left for supporting windows
    layout.Matrix(**layout_theme),
]

colors = [["#1d1f21", "#1d1f21"], # panel background
          ["#81a2be", "#81a2be"], # background for current screen tab
          ["#f0f0f0", "#f0f0f0"], # font color for group names
          ["#cc6666", "#cc6666"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#c5c8c6", "#c5c8c6"], # window name
          ["#808080", "#808080"]] # window name

widget_defaults = dict(
    font='San Francisco Text Medium',
    fontsize=13,
    foreground = colors[2],
    background = colors[0]
)

extension_defaults = widget_defaults.copy()

def init_screens():
    return [
            Screen(top = bar.Bar(
                [
                    widget.Sep(linewidth = 0, padding = 10,),
                    widget.TextBox(
                        font="SFMono Nerd Font",
                        text="",fontsize=15,
                        markup=True,
                        ),
                    widget.Sep(linewidth = 0, padding = 10,),
                    widget.GroupBox(
                        # active = colors[2],
                        # inactive = colors[0],
                        font='SFMono Nerd Font',
                        # markup = False,
                        disable_drag = False,
                        fontsize=11,
                        # hide_unused = True,
                        rounded = False,
                        # highlight_method="text",
                        padding = 0,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        inactive = colors[7],
                        highlight_color = colors[0],
                        highlight_method = "line",
                        active = colors[2],
                        this_current_screen_border = colors[2],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        # background = colors[0]
                        ),
                    # widget.Sep(linewidth = 0,padding = 10,),
                    widget.WindowName(
                        fontsize = 11,
                        ),
                    # widget.TextBox("default config", name="default"),
                    widget.Sep(linewidth = 0,padding = 2,),
                    widget.Systray(),
                    widget.Spacer(width=12),
                    # widget.CurrentLayoutIcon(
                    #                         custom_icon_paths=HOME+"/.config/qtile/icons",
                    #                         foreground = colors[0],
                    #                         background = colors[0],
                    #                         padding = 0,
                    #                         margin=5,
                    #                         scale=0.7
                    #                         ),
                    widget.Wlan(
                        interface="wlp4s0",
                        format="W:{quality}",
                        fontsize=10,
                    ),
                    # NetworkIcon(theme_path='/HOME/gem/.config/qtile/icons/mojave'),
                    widget.Sep(linewidth = 0,padding = 3,),
                    widget.PulseVolume(
                        volume_app="pavucontrol",
                        # emoji=True,
                        # get_volume_command="pamixer --get-volume",
                        # theme_path=HOME+'/.config/qtile/icons/mojave',
                        ),
                    widget.Sep(linewidth = 0,padding = 3,),
                    widget.BatteryIcon(
                        theme_path=HOME+'/.config/qtile/icons/mojave',
                        padding = 0,
                        ),
                    # widget.Battery(
                    #     format='B: {percent:2.0%}',
                    #     fontsize=12,
                    #     update_interval=30
                    #     ),
                    widget.Sep(linewidth = 0,padding = 3,),
                    widget.Clock(format='%a %I:%M %p [%u]'),
                    widget.Sep(linewidth = 0, padding = 3,),
                    widget.TextBox(
                            font="SFMono Nerd Font",text="",fontsize=12,markup=True,
                            mouse_callbacks={'Button1': '' }),
                    widget.Sep(linewidth = 0,padding = 10,),
                ],
                opacity = 0.8, size = 24))
	]

screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
