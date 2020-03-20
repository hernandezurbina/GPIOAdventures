import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)

servo1.start(0)       

try:
    while True:
        # ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 and 180: '))
        servo1.ChangeDutyCycle(2 + (angle / 18))
        sleep(0.5)
        servo1.ChangeDutyCycle(0)
except KeyboardInterrupt:
        # clean up things before leaving
        servo1.stop()
        GPIO.cleanup()
        print('Bye!')        