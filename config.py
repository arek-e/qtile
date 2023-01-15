# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import subprocess
from typing import Callable, List  # noqa: F401

from libqtile import hook

from libqtile.extension.dmenu import DmenuRun
from libqtile.extension.window_list import WindowList
from libqtile.extension.command_set import CommandSet

# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# import widgets and bar

from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from colors import gruvbox

# from bar1 import bar
from bar2 import bar

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
cur_font = "CaskaydiaCove NF"

keys = [
    Key([mod, "control"], "1", lazy.to_screen(0)),
    Key([mod, "control"], "2", lazy.to_screen(1)),

    # Launch applications
    Key([mod], "w", lazy.spawn('firefox'), desc="Launch browser"),
    # Key([mod], "e", lazy.spawn('kitty -e nnn -d -a -S'),
    #     desc="Launch nnn in home directory"),
    Key([mod], "d", lazy.spawn('Discord'), desc="Launch discord"),
    Key([mod], "s", lazy.spawn('obs'), desc="Launch OBS"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Command prompt
    # Key([mod], "p", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),

    # DmenuRun
    # Key([mod], 'p', lazy.run_extension(DmenuRun(
    #     font=cur_font,
    #     fontsize="13",
    #     dmenu_command="dmenu_run",
    #     dmenu_prompt=" ",
    #     dmenu_height=10,
    #     dmenu_lines=15,
    #     background=gruvbox['bg'],
    #     foreground=gruvbox['fg'],
    #     selected_foreground=gruvbox['dark-blue'],
    #     selected_background=gruvbox['bg'],
    # ))),

    Key([mod], 'r', lazy.run_extension(DmenuRun(
        dmenu_prompt=">",
        dmenu_font="Andika-8",
        background="#15181a",
        foreground="#00ff00",
        selected_background="#079822",
        selected_foreground="#fff",
        dmenu_height=24,  # Only supported by some dmenu forks
    ))),

    Key([mod, "shift"], 'w', lazy.run_extension(WindowList(
        all_groups=True,
        font="CaskaydiaCove NF",
        fontsize="13",
        dmenu_prompt=" ",
        dmenu_height=10,
        # dmenu_lines=15,
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        selected_foreground=gruvbox['dark-blue'],
        selected_background=gruvbox['bg'],
    ))),

    Key([mod, "control"], 'n', lazy.run_extension(CommandSet(
        commands={
            'Thesis notes': 'kitty nvim Neorg/Notes/Thesis/index.norg',
            'Dev notes': 'kitty nvim Neorg/Notes/Dev/index.norg',
            'JWL notes': 'kitty nvim Neorg/Notes/JWL/index.norg',
            'YouTube notes': 'kitty nvim Neorg/YT/index.norg',
        },
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        dmenu_prompt=' ',
        dmenu_lines=10,
        dmenu_height=10,
        selected_foreground=gruvbox['blue'],
        selected_background=gruvbox['bg'],
    ))),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Keybindings for resizing windows in MonadTall layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and Unsplit
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]


groups = [
    Group('1', label="", matches=[
          Match(wm_class='firefox'), Match(wm_class='brave'), Match(wm_class='qutebrowser')], layout="monadtall"),
    Group('2', label="", layout="monadtall"),
    Group('3', label="", layout="columns"),
    Group('4', label="ﭮ", matches=[
          Match(wm_class='discord'), Match(wm_class='zoom'), Match(wm_class="teams-for-linux")], layout="stack"),
    Group('5', label="", matches=[Match(wm_class="Spotify")], layout="stack"),
    Group('6', label="", layout="monadtall"),
    Group('7', label="漣", layout="monadtall"),
    Group('8', label="", layout="monadtall"),
    Group('9', label="", layout="monadtall"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Key([mod], i.name, lazy.function(go_to_group(i.name))),

        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    Stack(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        border_width=2,
        num_stacks=1,
        margin=8,
    ),
    MonadTall(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        margin=8,
        border_width=2,
        single_border_width=1,
        single_margin=8,
    ),
    Columns(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['cyan'],
        border_width=2,
        border_normal_stack=gruvbox['dark-gray'],
        border_focus_stack=gruvbox['dark-green'],
        border_on_single=2,
        margin=8,
        margin_on_single=8,
    )
]


floating_layout = Floating(
    border_normal=gruvbox['bg0'],
    border_focus=gruvbox['magenta'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        Match(title="Android Emulator - pixel5:5554"),
        Match(wm_class="Genymotion Player"),
        Match(title="AICOMS"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
        Match(wm_class="xarchiver"),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


widget_defaults = dict(
    font="CaskaydiaCove NF",
    fontsize=13,
    padding=10,
    foreground=gruvbox['bg'],
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(top=bar)
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
