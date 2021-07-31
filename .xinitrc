# compositor
picom -b &

# remap caps to escape
setxkbmap -option caps:escape

# Bluetooth systray icon
blueman-applet &

# Network Manager Applet
nm-applet --indicator &

# Environment variables set everywhere
export EDITOR="nvim"
export TERMINAL="alacritty"
export BROWSER="brave"

# XDG Paths
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share

# zsh config dir
export ZDOTDIR=$HOME/.config/zsh

# Hide mouse when typing
xbanish &

# feh set bg
~/.fehbg &

# dunst auto start
dunst &

# Screenshots
flameshot &

# slstatus
exec slstatus &

exec dwm
