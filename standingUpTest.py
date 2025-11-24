import numpy as np
import pi_servo_hat
import qwiic_kx13x
import sys
import math
from time import sleep

def get_roll_pitch(myKx):
    roll_deg = -1
    pitch_deg = -1
    
    if myKx.data_ready():    
        myKx.get_accel_data()
        ax = myKx.kx132_accel.x
        ay = -1 * myKx.kx132_accel.y
        az = myKx.kx132_accel.z
            
        roll  = math.atan2(ay, az)
        pitch = math.atan2(-ax, math.sqrt(ay*ay + az*az))

        roll_deg  = math.degrees(roll)
        pitch_deg = math.degrees(pitch)
    return roll_deg, pitch_deg
    

def runTest(test):

    secsBetweenSteps = 5
    secsBetweenPhases = 10
    secsBetweenMotionAndReading = 1

    # initializing the accelerometer
    print("initializing accelerometer")
    myKx = qwiic_kx13x.QwiicKX132()

    if myKx.connected == False:
        print("The Qwiic KX13X Accelerometer device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    if myKx.begin():
        print("Ready.")
    else:
        print("Make sure you're using the KX132 and not the KX134")

    if (myKx.software_reset()):
        print("Reset")
        
    myKx.enable_accel(False)
    myKx.set_range(myKx.KX132_RANGE2G)
    myKx.enable_data_engine()
    myKx.enable_accel()
    
    print('Getting first acc reading...')
    roll_deg, pitch_deg = get_roll_pitch(myKx)
    print("Roll: {:.2f}°, Pitch: {:.2f}°".format(roll_deg, pitch_deg))  
    
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
            roll_deg, pitch_deg = get_roll_pitch(myKx)
            print("Roll: {:.2f}°, Pitch: {:.2f}°".format(roll_deg, pitch_deg)) 
            
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
            roll_deg, pitch_deg = get_roll_pitch(myKx)
            print("Roll: {:.2f}°, Pitch: {:.2f}°".format(roll_deg, pitch_deg)) 
            # sleep before next move
            sleep(secsBetweenSteps)

        print('Pausing for {} secs...'.format(secsBetweenPhases))
        sleep(secsBetweenPhases)

###############################################################################################
if __name__ == '__main__':
    try:
        test = pi_servo_hat.PiServoHat()
        test.restart()
        runTest(test)
    except (KeyboardInterrupt, SystemExit) as exErr:
        print('\nFinishing test.')
        test.restart()
        sys.exit(0)
