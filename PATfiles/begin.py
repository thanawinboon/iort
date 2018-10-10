from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Motor,RGBLED, Button, LED


def on():
    global sensorOn
    global sensorOff
    global state
    global speed
    while True:
        sensorOn = GPIO.input(sensorPinon)
        sensorOff = GPIO.input(sensorPinoff)
        
        if sensorOn == GPIO.LOW:
            motor.forward(speed)
            state = "on"
            print("ON")
            
        if sensorOff == GPIO.LOW:
            motor.stop()
            state = "off"
            print("OFF")
        
        
        if state == "off":
            mainled.off()
            mainled.red = 1
            motor.stop()
            sleep(0.5)
        
        elif state == "on":
            mainled.off()
            mainled.green = 1
            sleep(0.5)
        
        
def speedcheck():
    global speed
    if button.is_pressed:
        if speed == 0.5:
            speed = 1
        elif speed == 1:
            speed = 0.5

try:
    sensorPinon = 14
    sensorPinoff = 26
    motor = Motor(20,21)
    mainled = RGBLED(2,3,4)
    #button = Button()

    speed = 0.6
    state = "off"
    GPIO.setup(sensorPinon, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(sensorPinoff, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    on()
    
finally:
    mainled.red = 0
    mainled.green = 0
    mainled.blue = 0
    mainled.off()
    GPIO.cleanup()
