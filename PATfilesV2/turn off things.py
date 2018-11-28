from gpiozero import RGBLED 
from time import sleep

l = RGBLED(2,3,4)
try:
    print("off")
    l.red = 1
    l.blue = 1
    l.green = 1
    sleep(1)
    
    
finally:
    l.off()