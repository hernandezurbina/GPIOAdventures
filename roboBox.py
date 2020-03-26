import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
# this must change accordingly and taking care that we dont mess w
# the pins in the sensehat

# servo1
gpioServo1 = 11
# servo2
gpioServo2 = 12

GPIO.setup(gpioServo1, GPIO.OUT)
servo1 = GPIO.PWM(gpioServo1, 50)
GPIO.setup(gpioServo2, GPIO.OUT)
servo2 = GPIO.PWM(gpioServo2, 50)

servo1.start(0)       
servo2.start(0)

dc1 = 2.0
dc2 = 7.0

# starting position:
servo1.ChangeDutyCycle(dc1)
sleep(0.5)
servo2.ChangeDutyCycle(dc1)
sleep(0.5)
servo1.ChangeDutyCycle(dc2)
sleep(0.5)
servo2.ChangeDutyCycle(dc2)
sleep(0.5)



try:
    while True:
        servo1.ChangeDutyCycle(dc1)
        sleep(0.5)
        servo2.ChangeDutyCycle(dc1)
        sleep(0.5)
        servo1.ChangeDutyCycle(dc2)
        sleep(0.5)
        servo2.ChangeDutyCycle(dc2)
        sleep(0.5)        

except KeyboardInterrupt:
        # clean up things before leaving
        servo1.stop()
        servo2.stop()
        GPIO.cleanup()
        print('Bye!')
        
# servo1.stop()
# servo2.stop()
# GPIO.cleanup()
# print('Bye!')

