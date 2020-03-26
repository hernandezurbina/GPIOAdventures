import RPi.GPIO as GPIO
from time import sleep

from threading import Thread

def moveArm1():
    for i in range(5):
        print('A1', i)
        servo1.ChangeDutyCycle(dc1)
        sleep(0.5)
        servo1.ChangeDutyCycle(dc2)
        sleep(0.5)
        
def moveArm2():
    for i in range(5):
        print('A2', i)
        servo2.ChangeDutyCycle(dc1)
        sleep(0.5)
        servo2.ChangeDutyCycle(dc2)
        sleep(0.5)    

GPIO.setmode(GPIO.BOARD)

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

t1 = Thread(target=moveArm1)
t1.start()        
t2 = Thread(target=moveArm2)
t2.start()        


# try:
#     while True:      
#         servo1.ChangeDutyCycle(dc1)
#         sleep(0.5)
#         servo2.ChangeDutyCycle(dc1)
#         sleep(0.5)
#         servo1.ChangeDutyCycle(dc2)
#         sleep(0.5)
#         servo2.ChangeDutyCycle(dc2)
#         sleep(0.5)        
# except KeyboardInterrupt:
        # clean up things before leaving
#         servo1.stop()
#         servo2.stop()
#         GPIO.cleanup()
#         print('Bye!')
        
servo1.stop()
servo2.stop()
GPIO.cleanup()
print('Bye!')

