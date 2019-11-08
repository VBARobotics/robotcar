from gpiozero import Robot
from time import sleep
robot = Robot(left=(4, 14), right=(17, 18))
for i in range(4):
  robot.forward()
  print (i, " Going Forward")
  sleep(5)
  robot.right()
  print(i, " Turning Right")
  sleep(2)
  
robot.stop()
