import pi_servo_hat
import qwiic_kx13x
import sys
from time import sleep
from random import randint

def runTest(test):

    myKx = qwiic_kx13x.QwiicKX132()

    if myKx.connected == False:
        print("The Qwiic KX13X Accelerometer device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    print('Starting...')
    print('r - get acc reading | 1 to 4 - move leg | e - exit')
    print('\n')

    legStatus = {1: 0, 2: 0, 3: 0, 4: 0} # 0: resting, `1: standing
    restingConf = {1: 0, 2: 90, 3: 90, 4: 0}
    standingConf = {1: 90, 2: 0, 3: 0, 4: 90}
    while True:

        x = input()

        if x == 'e':
            break
        elif x.isnumeric():
            #leg = randint(1, 4)
            leg = int(x)
            x = 'Z'
            if leg > 4 or leg < 1:
                print('Legs are 1 to 4!')
            print('Moving leg', leg)
            if legStatus[leg] == 0:
                # leg is resting now should stand
                test.move_servo_position(leg, standingConf[leg])
                legStatusp[leg] = 1
            else:
                # leg is standing now should rest
                test.move_servo_position(leg, restingConf[leg])
                legStatus[leg] = 0
        elif x == 'r':
            x = 'Z'
            print('Getting reading')
            myKx.get_accel_data()
            print("({:.3f}g, {:.3f}g, {:.3f}g)".format(myKx.kx132_accel.x, myKx.kx132_accel.y, myKx.kx132_accel.z))
        else:
            print('Unrecognised option!')


if __name__ == '__main__':
    try:
        test = pi_servo_hat.PiServoHat()
        test.restart()
        runTest(test)
        print('Finishing...')
        test.restart()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print('\nAborting...')
        test.restart()
