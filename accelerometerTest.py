#!/usr/bin/env python3
import qwiic_kx13x
import time
import sys
import math

def runExample():

    print("\nSparkFun KX13X Accelerometer Example 1\n")
    myKx = qwiic_kx13x.QwiicKX132()

    if myKx.connected == False:
            print("The Qwiic KX13X Accelerometer device isn't connected to the system. Please check your connection", \
                    file=sys.stderr)
            return

    if myKx.begin():
        print("Ready.")
    else:
        print("Make sure you're using the KX132 and not the KX134")

    if (myKx.software_reset()):
        print("Reset")

    # Many settings for KX13X can only be
    # applied when the accelerometer is powered down.
    # However there are many that can be changed "on-the-fly"
    # check datasheet for more info
    myKx.enable_accel(False)
    # myKx.set_range(myKx.KX132_RANGE16G)
    myKx.set_range(myKx.KX132_RANGE2G)
    myKx.enable_data_engine()
    myKx.enable_accel()

    while True:
        if myKx.data_ready():    
            myKx.get_accel_data()
            ax = myKx.kx132_accel.x
            ay = -1 * myKx.kx132_accel.y
            az = myKx.kx132_accel.z
            #print("X: {0} Y: {1} Z: {2}".format(ax, ay, az))
            
            roll  = math.atan2(ay, az)
            pitch = math.atan2(-ax, math.sqrt(ay*ay + az*az))

            roll_deg  = math.degrees(roll)
            pitch_deg = math.degrees(pitch)            
            
            print("Roll: {:.2f}°, Pitch: {:.2f}°".format(roll_deg, pitch_deg))
            time.sleep(.02) #Set delay to 1/Output Data Rate which is by default 50Hz 1/50 = .02

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)
