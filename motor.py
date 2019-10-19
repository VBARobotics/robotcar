from gpiozero import Motor
from time import sleep

leftmotor = Motor(forward=17, backward=18)

leftmotor.stop()
leftmotor.forward()
sleep(5)
leftmotor.backward()
sleep(5)
leftmotor.stop()
