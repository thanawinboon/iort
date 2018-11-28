from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0

def takePictureFor(times, wait):
    for index in range(times):
        index = str(index)
        sleep(wait)
        print("picture taken: " + index)
        camera.capture('image%s.jpg' % index)
    print("picture taken")
    

try:
    camera.start_preview()
    takePictureFor(1, 3)

finally:
    camera.stop_preview()
