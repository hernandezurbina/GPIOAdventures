import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
# this must change accordingly and taking care that we dont mess w
# the pins in the sensehat

# servo1
#gpioServo = 11

# servo2
gpioServo = 12

GPIO.setup(gpioServo, GPIO.OUT)
servo1 = GPIO.PWM(gpioServo, 50)

servo1.start(0)       

try:
    while True:
        # ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 and 180: '))
        dc = 2 + (angle / 18)
        print(angle, dc)
        servo1.ChangeDutyCycle(dc)
        sleep(0.5)
        servo1.ChangeDutyCycle(0)
except KeyboardInterrupt:
        # clean up things before leaving
        servo1.stop()
        GPIO.cleanup()
        print('Bye!')        