from picamera import PiCamera, Color
from time import sleep


camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.framerate = 15

camera.annotate_text = "WOW!"
camera.annotate_text_size = 120
camera.annotate_foreground = Color('#92f4c3')
camera.annotate_background = Color('#000000')

def takeMeemee():
    sleep(10)
    camera.capture('mememax.jpg')
    

try:
    camera.start_preview()
    takeMeemee()

finally:
    camera.stop_preview()
