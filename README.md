# Script: Toggl.com widget
Simple toggl.com time tracker widget that shows currently running project and time it has been running.

Similar to official dock widget for macOS, but for polybar/i3bar/etc.


## Screenshots
![screenshot](https://github.com/maksmeshkov/toggl_polybar/blob/master/screenshot.png "This is how it looks")

# Configuration

Just add you toggl api key to the python file.

# Module

```
  [module/toggl]
  type = custom/script
  
  exec = "python3 $HOME/.config/polybar/toggl.py"
  interval = 20.0
  format = <label>
  format-foreground =  ${colors.fg}
  format-padding = 1
  ; Add this line if you have xdg-utils
  ; click-left = "xdg-open https://toggl.com/app/timer" 
```
