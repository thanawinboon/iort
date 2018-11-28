from gpiozero import RGBLED 
from time import sleep

mainled = RGBLED(2,3,4)

mainled.off()
mainled.red = 1

sleep(1)
mainled.off()
mainled.blue = 1

sleep(1)
mainled.off()
mainled.green = 1

sleep(1)
mainled.off()