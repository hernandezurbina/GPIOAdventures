import qwiic_kx13x
import time
import sys
import RPi.GPIO

def runExample():

    print("\nSparkFun KX13X Accelerometer Example 1\n")
    # myKx = qwiic_kx13x.QwiicKX134() # If using the KX134 un-comment this line and replace other instances of "kx132" with "kx134"
    myKx = qwiic_kx13x.QwiicKX132()

    if myKx.connected == False:
            print("The Qwiic KX13X Accelerometer device isn't connected to the system. Please check your connection", \
                    file=sys.stderr)
            return

    if myKx.begin():
        print("Ready.")
    else:
        print("Make sure you're using the KX132 and not the KX134")

    # myKx.set_range(myKx.KX132_RANGE8G) # Update the range of the data output.
    #myKx.initialize(myKx.BASIC_SETTINGS) # Load basic settings
    myKx.initialize(myKx.DEFAULT_SETTINGS) # Load basic settings 

    while True:

        myKx.get_accel_data()
        print("X: {:.2f}g Y: {:.2f}g Z: {:.2f}g".format(myKx.kx132_accel.x,
                                               myKx.kx132_accel.y,
                                               myKx.kx132_accel.z))
        time.sleep(.02) #Set delay to 1/Output Data Rate which is by default 50Hz 1/50 = .02


if __name__ == '__main__':
        try:
            runExample()
        except (KeyboardInterrupt, SystemExit) as exErr:
            print("\nEnding Example 1")
            sys.exit(0)
