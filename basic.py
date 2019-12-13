from gpiozero import Robot
from time import sleep
robot = Robot(left=(4, 14), right=(17, 18))
i = 1
robot.forward(speed=0.5)
print (i, " Going Forward")
sleep(5)
robot.right()
print(i, " Turning Right")
sleep(2)
robot.forward(speed=1.0)
print (i, " Going Forward")
sleep(5)
robot.left(speed=0.75)
robot.stop()
