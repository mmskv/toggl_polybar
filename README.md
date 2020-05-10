# toggl_polybar
Simple toggl widget that shows currently running project and time it has been running.

Similar to official dock widget for macOS, but for polybar/i3bar/etc.


## Screenshots
![screenshot](https://github.com/maksmeshkov/toggl_polybar/blob/master/screenshot.png "This is how it looks")


### Sample syntax to add this widget to polybar

```
  [module/toggl]
  type = custom/script
  
  exec = "python3 $HOME/.config/polybar/toggl.py"
  interval = 20.0
  format = <label>
  format-foreground =  ${colors.fg}
  format-padding = 1
```
