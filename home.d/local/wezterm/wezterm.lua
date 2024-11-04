local wezterm = require 'wezterm'

local config = wezterm.config_builder()

-- config.color_scheme = 'iceberg-dark'
-- config.color_scheme = 'zenwritten_dark'
config.color_scheme = 'Catppuccin Macchiato'
config.font = wezterm.font("HackGen Console NF", {weight="Regular", stretch="Normal"})
config.font_size = 16
config.window_decorations = "RESIZE"
config.window_background_opacity = 0.93



-- tab
config.hide_tab_bar_if_only_one_tab = false
-- config.tab_bar_at_bottom = true
config.use_fancy_tab_bar = false


return config
