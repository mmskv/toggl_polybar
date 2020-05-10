# toggl_polybar
Simple toggl widget for polybar/i3bar/etc., that shows currently running project.
Simmilar to official dock widget for macOS.


## Screenshots
[this is how it looks](https://github.com/maksmeshkov/toggl_polybar/screenshot.png)


### Sample syntax to add this witget to polybar

[module/toggl]
type = custom/script
exec = "python3 $HOME/.config/polybar/toggl.py"
interval = 20.0

format = <label>
format-foreground =  ${colors.fg}

format-padding = 1
