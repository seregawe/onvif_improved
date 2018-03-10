# onvif_improved

Improved fork of https://github.com/vitshas/ptz_controller/

New features:
  
  go_home() function - sends camera home
  
  smooth_move(timeout) - smoothly moves camera to the left with speed up and slow down, continuously till timeout is reached
  
  smooth_move_right(timeout) - smoothly moves camera to the right with speed up and slow down, continuously till timeout is reached
  
  speed_up(interval, steps, direction) - Increases velocity with selected interval in selected amount of steps to the selected direction
  
  slowdown(interval, steps, direction) - Decreases velocity with selected interval in selected amount of steps to the selected direction.
  
This repo works with camera .52 by default!
