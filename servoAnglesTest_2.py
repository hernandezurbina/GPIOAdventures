import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# set pins 11 and 12 as outputs and define as PWM servo1 and 2
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
GPIO.setup(12, GPIO.OUT)
servo2 = GPIO.PWM(12, 50)

# start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

# turn servo1 to 90
servo1.ChangeDutyCycle(7)
sleep(0.5)
servo1.ChangeDutyCycle(0)

# wait for 2 secs
sleep(2)

# turn servo2 to 90 and servo1 back to 0
servo2.ChangeDutyCycle(7)
servo1.ChangeDutyCycle(2)
sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

sleep(2)

# turn servo2 to 180 and servo1 to 90
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(7)
sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

sleep(2)

# turn both servos back to 0
servo2.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(2)
sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

sleep(2)

# cleanup when done!
servo1.stop()
servo2.stop()
GPIO.cleanup()

