from picamera import PiCamera, Color
import RPi.GPIO as GPIO
from time import sleep


camera = PiCamera()
camera.rotation = 180
sensorPin = 

currentlyOn = False
answered = False
userEffect = "none"

def askEFCT():
    global answered, effect
    while answered == False:
        ANS = input("Please enter the effect you want. Type q for no effect.")
        if ANS == "negative":
            effect = ANS
            answered = True
        elif ANS == "solarize":\
            effect = ANS
            answered = True
        elif ANS == "emboss":
            effect = ANS
            answered = True
        elif ANS == "cartoon":
            effect = ANS
            answered = True
        elif ANS == "q":
            effect = "none"
            answered = True
        else:
            print("Inputted effect doesn't exist. Please re-enter the effect OR type q to utilize no effect.")
            


def takeOnSensor(wow):
    global currentlyOn, userEffect
    while True:
        sensor = GPIO.input(sensorPin)
        
        if sensor == GPIO.LOW and currentlyOn == False:
            camera.start_preview()
            camera.start_recording('spyvid.h264')
            currentlyOn = True
            
            camera.image_effect = userEffect
            
            sleep(wow)
            
            camera.stop_recording()
            camera.stop_preview()
            currentlyOn = False
        
            
    

try:
    GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    askEFCT()
    takeOnSensor(1)
    

finally:
    if currentlyOn == True:
        camera.stop_preview()
