import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

gpioPin = 11
dc = 12
# dc for 0 deg is 2
# dc for 90 deg is 7
# dc for 180 deg is 12

GPIO.setup(gpioPin, GPIO.OUT)
servo1 = GPIO.PWM(gpioPin, 50)

print('Setting up in 2 secs')
sleep(2)
servo1.start(2.5)
print('Moving in 2 secs. DC:', dc)
sleep(2)
servo1.ChangeDutyCycle(dc)
print('Returning to start pos in 2 secs')
sleep(2)
#servo1.ChangeDutyCycle(0)
#sleep(0.5)
servo1.ChangeDutyCycle(2.5)

sleep(2)
servo1.stop()
GPIO.cleanup()


