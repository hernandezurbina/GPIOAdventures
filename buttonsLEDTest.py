from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.cleanup()

button1 = 16
button2 = 12

LED1 = 22
LED2 = 18

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

BS1 = False
BS2 = False

while True:
	if GPIO.input(button1) == 0:
		print('Button 1 pressed!')
		if not BS1:
			GPIO.output(LED1, True)
			BS1 = True
			sleep(0.5)
		else:
			GPIO.output(LED1, False)
			BS1 = False
			sleep(0.5)
	if GPIO.input(button2) == 0:
		print('Button 2 pressed!')
		if not BS2:
			GPIO.output(LED2, True)
			BS2 = True
			sleep(0.5)
		else:
			GPIO.output(LED2, False)
			BS2 = False
			sleep(0.5)

GPIO.cleanup()
