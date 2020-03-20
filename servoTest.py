import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # 11 is pin, 50 = 50Hz pulse
 
servo1.start(0)
print('Waiting 2 secs')
sleep(2)
 
print('Rotating 180 deg in 10 steps')
 
duty = 2
 
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    #sleep(1)
    sleep(0.3)
    servo1.ChangeDutyCycle(0)
    sleep(0.7)
    duty += 1
    
sleep(2)

print('Turning back to 90 deg for 2 secs')
servo1.ChangeDutyCycle(7)
sleep(0.5)
servo1.ChangeDutyCycle(0)
sleep(1.5)

print('Turning back to 0 deg')
servo1.ChangeDutyCycle(2)
sleep(0.5)
servo1.ChangeDutyCycle(0)

# cleanup when done!
servo1.stop()
GPIO.cleanup()


