import numpy as np
import pi_servo_hat
import qwiic_kx13x
import sys
from time import sleep

def runTest(test):

    secsBetweenSteps = 5
    secsBetweenPhases = 10
    secsBetweenMotionAndReading = 3

    myKx = qwiic_kx13x.QwiicKX132()

    if myKx.connected == False:
        print("The Qwiic KX13X Accelerometer device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    
    print('Getting first acc reading...')
    myKx.get_accel_data()
    print("({:.3f}g, {:.3f}g, {:.3f}g)".format(myKx.kx132_accel.x, myKx.kx132_accel.y, myKx.kx132_accel.z))  
    print('Starting...')
    sleep(5)

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

            # take reading after move
            sleep(secsBetweenMotionAndReading)
            myKx.get_accel_data()
            print("({:.3f}g, {:.3f}g, {:.3f}g)".format(myKx.kx132_accel.x, myKx.kx132_accel.y, myKx.kx132_accel.z))              

            # sleep before next move
            sleep(secsBetweenSteps)

        print('Pausing for {} secs...'.format(secsBetweenPhases))
        sleep(secsBetweenPhases)

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

            # take reading after move
            sleep(secsBetweenMotionAndReading)
            myKx.get_accel_data()
            print("({:.3f}g, {:.3f}g, {:.3f}g)".format(myKx.kx132_accel.x, myKx.kx132_accel.y, myKx.kx132_accel.z)) 

            # sleep before next move
            sleep(secsBetweenSteps)

        print('Pausing for {} secs...'.format(secsBetweenPhases))
        sleep(secsBetweenPhases)

if __name__ == '__main__':
    try:
        test = pi_servo_hat.PiServoHat()
        test.restart()
        runTest(test)
    except (KeyboardInterrupt, SystemExit) as exErr:
        print('\nFinishing test.')
        test.restart()
        sys.exit(0)
