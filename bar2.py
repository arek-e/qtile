from libqtile.bar import Bar

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayoutIcon
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.graph import MemoryGraph
from libqtile.widget.battery import Battery
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.volume import Volume
# from libqtile.widget.wlan import Wlan

from colors import gruvbox, deus
from unicodes import left_half_circle, right_half_circle, left_arrow, right_arrow

bar = Bar([
    left_half_circle(deus['blue']),
    right_arrow(deus['bright-yellow'], deus['blue']),
    CurrentLayoutIcon(
        scale=0.5,
        background=deus['bright-yellow'],
        foreground='#2c323b',
    ),

    right_arrow(deus['bright-green'], deus['bright-yellow']),


    Clock(
        background=deus['bright-green'],
        format=' %d/%m/%y %H:%M'),
    right_arrow(deus['bg'], deus['bright-green']),

    Spacer(length=10),

    WindowName(foreground=deus['fg']),

    left_half_circle(deus['black']),
    GroupBox(
        disable_drag=True,
        active=deus['fg'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=deus['violet'],
        borderwidth=1,
        highlight_color=deus['bg'],
        background=deus['black']
    ),
    right_half_circle(deus['black']),

    Spacer(length=350),

    Systray(
        padding=15,
    ),

    Spacer(length=15),

    left_half_circle(deus['blue']),
    right_arrow(deus['black'], deus['blue']),
    Spacer(
        background=deus['black'],
        length=15),
    Volume(
        font='Consolas',
        fmt='Vol: {}',
        background=deus['black'],
        foreground=deus['fg'],
              ),
    MemoryGraph(
        background=deus['black'],
        type='line',
        border_width=0,
        frequency=1,
        graph_color=deus['orange'],
        foreground=deus['fg']),
    CPU(
        format=' {load_percent}%',
        background=deus['black'],
        foreground=deus['fg']),
    Battery(
        background=deus['black'],
        foreground=deus['fg'],
        format="{percent:0.1%}",
        font='Consolas',
        fontsize=18,
        padding=3,
    ),
    Spacer(
        background=deus['black'],
        length=15),
    left_arrow(deus['black'], deus['blue']),
    right_half_circle(deus['blue']),
],
    margin=[5, 5, 0, 5],
    background=deus['bg'],
    opacity=1,
    size=30,
)
