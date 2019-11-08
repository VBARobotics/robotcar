from gpiozero import Motor, LED
from time import sleep

leftmotor = Motor(forward=17, backward=18)
red = LED(19)
green = LED(20)

leftmotor.stop()
red.blink(on_time=0.5,off_time=0.5)
leftmotor.forward()
sleep(5)
red.off()
green.blink()
leftmotor.backward()
sleep(5)
green.off()
leftmotor.stop()

