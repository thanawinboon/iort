from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0
a = 1
b = 1

def takePictureFor(times):
    global a, b
    for index in range(1,4):
        timer = str(index)
        print(timer)
        camera.annotate_text = timer
        sleep(1)
    
    camera.annotate_text = ""
    
    if times < 10:
        for index in range(times, freq):
            camera.zoom = 0,0,a,b
            camera.capture('continue{counter}.jpg')
            sleep(freq)
            a = a - 0.1
            b = b - 0.1
    if times >= 10:
        for index in range(times):
            camera.zoom = 0,0,a,b
            camera.capture('continue{counter:02d}.jpg')
            sleep(freq)
            a = a - 0.1
            b = b - 0.1
        
    

try:
    camera.start_preview()
    takePictureFor(10, 0.1)

finally:
    camera.stop_preview()
