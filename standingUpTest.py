import numpy as np
import pi_servo_hat
import sys
from time import sleep

def runTest(test):    

    while True:
        # standing phase
        print('Standing...')
        order = list(np.random.permutation(4))
        while len(order) > 0:
            servoNumber = (order.pop(0)) + 1 # servos are 1, 2, 3, and 4
            print(servoNumber)
            if servoNumber == 1:
                test.move_servo_position(servoNumber, 0) # check that this value is correct
            elif servoNumber == 2:
                test.move_servo_position(servoNumber, 90) # check that this value is correct
            elif servoNumber == 3:
                test.move_servo_position(servoNumber, 90) # check that this value is correct
            elif servoNumber == 4:
                test.move_servo_position(servoNumber, 0) # check that this value is correct
            sleep(1)

        sleep(5)

        # sitting phase
        print('Sitting...')
        order = list(np.random.permutation(4))
        while len(order) > 0:
            servoNumber = (order.pop(0)) + 1 # servos are 1, 2, 3, and 4
            print(servoNumber)
            ### now values should be different to what we used for standing phase
            if servoNumber == 1:
                test.move_servo_position(servoNumber, 90) # check that this value is correct
            elif servoNumber == 2:
                test.move_servo_position(servoNumber, 0) # check that this value is correct
            elif servoNumber == 3:
                test.move_servo_position(servoNumber, 0) # check that this value is correct
            elif servoNumber == 4:
                test.move_servo_position(servoNumber, 90) # check that this value is correct
            sleep(1)

        sleep(5)

if __name__ == '__main__':
    try:
        test = pi_servo_hat.PiServoHat()
        print('Starting...')
        test.restart()
        sleep(5)
        runTest(test)
    except (KeyboardInterrupt, SystemExit) as exErr:
        print('\nFinishing test.')
        test.restart()
        sys.exit(0)
