from picamera import PiCamera, Color
from time import sleep


camera = PiCamera()
camera.rotation = 0

def takeVid(wow):
    sleep(2)
    camera.start_recording('theVid.h264',format='h264', quality=40, bitrate=2000000)
    sleep(wow)
    camera.stop_recording()

try:
    camera.start_preview()
    takeVid(3)

finally:
    camera.stop_preview()
