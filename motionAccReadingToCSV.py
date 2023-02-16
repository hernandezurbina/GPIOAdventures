import pi_servo_hat
import qwiic_kx13x
import pandas as pd
from time import sleep
from random import randint

def runTest(test):

    myKx = qwiic_kx13x.QwiicKX132()

    if myKx.connected == False:
        print("The Qwiic KX13X Accelerometer device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    standingConf = {1: 0, 2: 90, 3: 90, 4: 0}
    restingConf = {1: 90, 2: 0, 3: 0, 4: 90}

    num_iterations = 5
    secsBetweenReadings = 5
    secsBetweenSteps = 1

    legs = []
    Xs = []
    Ys = []
    Zs = []

    for leg in range(0, 5):

        if leg > 0:
            # move
            if leg > 1:
                # no need to pull back leg 0
                test.move_servo_position(leg-1, restingConf[leg-1])
                sleep(secsBetweenSteps)
            
            test.move_servo_position(leg, standingConf[leg])


        for iteration in range(num_iterations):
            print('leg {} iteration ({}/{})'.format(leg, iteration+1, num_iterations))
            sleep(secsBetweenReadings)
            myKx.get_accel_data()
            legs.append(leg)
            Xs.append(float('{:.3f}'.format(myKx.kx132_accel.x)))
            Ys.append(float('{:.3f}'.format(myKx.kx132_accel.y)))
            Zs.append(float('{:.3f}'.format(myKx.kx132_accel.z)))

        print()
    
    # save to CSV using pandas
    test.move_servo_position(leg, restingConf[leg])
    print('Creating dataframe and csv file')
    data = pd.DataFrame({'leg': legs, 'x': Xs, 'y': Ys, 'z':Zs})
    data.to_csv('data.csv', index=False)
    print('Done!')

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
