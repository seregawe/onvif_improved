from ptz_cam import *
from time import sleep
#Init the cam
cam = ptzcam()
#Ensure camera is in home postion
cam.go_home()
#Move camera slowly to the lft
cam.smooth_move(4)
sleep(5)
cam.go_home()