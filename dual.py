from gpiozero import Robot
from time import sleep
robotfront = Robot(left=(4, 14), right=(17, 18))
robotback = Robot(left=(22, 23), right=(24, 25))

robotfront.forward(speed=0.5)
robotback.forward(speed=0.5)
print (" Going Forward All Four Wheels")
sleep(5)
robotback.stop()
robotfront.right()
print(" Turning Right")
sleep(5)
robotfront.forward(speed=1.0)
print (" Going Forward front wheels only")
sleep(5)
robotfront.stop()
robotback.forward(speed=1.0)
print (" Going Forward back wheels only")
sleep(5)
robotback.stop()
print (" Turning Left Back wheels only")
robotback.left(speed=0.75)
sleep(5)
robotfront.stop()
robotback.reverse()
print (" Going Backwards back wheels only")
sleep(5)
robotfront.stop()
robotback.stop()
print(" Stopped")