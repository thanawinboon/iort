from gpiozero import Motor,RGBLED, Button, LED
import RPi.GPIO as GPIO
from time import sleep

motor = Motor(20,21)

try:
    motor.forward(0.5)
    sleep(3)
    motor.stop()
    sleep(4)
    motor.forward(1)
    sleep(3)

finally:
    motor.stop()
    print("stop")