import RPi.GPIO as GPIO
from time import sleep
from sense_hat import SenseHat
from threading import Thread

def show_message(i):
    sense.set_rotation(180)
    sense.show_message(i)

sense = SenseHat()
#sense.set_rotation(180)

GPIO.setmode(GPIO.BOARD)
# this must change accordingly and taking care that we dont mess w
# the pins in the sensehat
gpioServo = 11

GPIO.setup(gpioServo, GPIO.OUT)
servo1 = GPIO.PWM(gpioServo, 50)

servo1.start(0)       

try:
    while True:
        # ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 and 180: '))        
        servo1.ChangeDutyCycle(2 + (angle / 18))
        # sense.show_message(str(angle))
        t = Thread(target=show_message, args=(str(angle),))
        t.start()        
        sleep(0.5)
        servo1.ChangeDutyCycle(0)
except KeyboardInterrupt:
        # clean up things before leaving
        servo1.stop()
        GPIO.cleanup()
        sense.clear()
        print('Bye!')
