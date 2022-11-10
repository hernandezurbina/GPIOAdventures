import time
import RPi.GPIO as GPIO

# setting GPIO board to default
GPIO.setmode(GPIO.BOARD)
# setting pins in the GPIO
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
	
for x in range(8):
	GPIO.output(7, True)
	time.sleep(0.5)
	GPIO.output(7, False)
	GPIO.output(11, True)
	time.sleep(0.5)
	GPIO.output(11, False)
	GPIO.output(13, True)
	time.sleep(0.5)
	GPIO.output(13, False)
	time.sleep(0.5)


GPIO.cleanup()
