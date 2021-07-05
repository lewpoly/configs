import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

mod = "mod4"
myTerm = "alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "m",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    ## Program Launch Hotkeys

    Key([mod, "shift"], "d", lazy.spawn("dmenu_run"), desc="Launch dmenu_run"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch pcmanfm"),
]

group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 10,
                "border_focus": "#e8dfd6",
                "border_normal": "#717171"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.TreeTab(
    layout.Floating(**layout_theme)
]

colors = [["#282a36", "#282a36"], # 0 Background
          ["#44475a", "#44475a"], # 1 Current Line
          ["#f8f8f2", "#f8f8f2"], # 2 Foreground
          ["#6272a4", "#6272a4"], # 3 Comment
          ["#8be9fd", "#8be9fd"], # 4 Cyan
          ["#50fa7b", "#50fa7b"], # 5 Green
          ["#ffb86c", "#ffb86c"], # 6 Orange
          ["#ff79c6", "#ff79c6"], # 7 Pink
          ["#bd93f9", "#bd93f9"], # 8 Purple
          ["#ff5555", "#ff5555"], # 9 Red
          ["#f1fa8c", "#f1fa8c"]] # 10 Yellow 

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


widget_defaults = dict(
    font='iosevka',
    fontsize=12,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(font = "iosevka",
                       fontsize = 15,
                       margin_y = 5,
                       margin_x = 5,
                       padding_y = 5,
                       padding_x = 5,
                       borderwidth = 3,
                       active = colors[4],
                       inactive = colors[3],
                       rounded = False,
                       highlight_color = colors[9],
                       highlight_method = "block",
                       this_current_screen_border = colors[1],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[7],
                       other_screen_border = colors[7],
                       foreground = colors[7],
                       background = colors[0]
                       ),
                widget.Prompt(),
                widget.WindowName(font = "iosevka",
                       fontsize = 14,
                       foreground = colors[5],
                       background = colors[0],
                       padding = 0
                       ),
                widget.Sep(),
                widget.TextBox(
                       text = "",
                       padding = 1,
                       foreground = colors[8],
                       background = colors[0],
                       fontsize = 20
                       ),
                widget.Volume(font = "iosevka",
                       margin_y = 0,
                       margin_x = 5,
                       padding_y = 0,
                       padding_x = 5,
                       foreground = colors[6],
                       background = colors[0],
                       fontsize = 15
                       ),
                widget.Sep(),
                widget.TextBox(
                       text = "",
                       padding = 2,
                       foreground = colors[8],
                       background = colors[0],
                       fontsize = 16
                       ),
                widget.Battery(font = "iosevka",
                       format = '{percent:2.0%}',
                       margin_y = 0,
                       margin_x = 5,
                       padding_y = 0,
                       padding_x = 5,
                       foreground = colors[6],
                       background = colors[0],
                       fontsize = 15
                       ),
                widget.Sep(),
                widget.TextBox(
                       text = "",
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0],
                       fontsize = 16
                       ),
                widget.Clock(font = "iosevka",
                       fontsize = 14,
                       foreground = colors[6],
                       background = colors[0],
                       format = "%A, %B %d"
                       ),
                widget.Sep(),
                widget.TextBox(
                       text = "",
                       padding = 5,
                       foreground = colors[4],
                       background = colors[0],
                       fontsize = 16
                       ),
                widget.Clock(font = "iosevka",
                       fontsize = 16,
                       foreground = colors[5],
                       background = colors[0],
                       format = "%I:%M"
                       ),
                widget.Sep(),
                widget.Systray(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, "control"], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
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
auto_fullscreen = True
focus_on_window_activation = "smart"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
