from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.framerate = 15

def takeVid():
    camera.capture('max.jpg')
    

try:
    camera.start_preview()
    takeVid()

finally:
    camera.stop_preview()
