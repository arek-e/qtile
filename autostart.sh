#!/bin/sh

blueman-applet &
redshift -l 65.58404320418528:22.15559706893966 &

~/.fehbg &
copyq &
nm-applet &
mictray &
pasystray &
deadd-notification-center &
# picom -b --animations --animation-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 350 &
picom --config ~/.config/picom/picom.conf &
