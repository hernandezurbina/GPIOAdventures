from machine import Pin, ADC
import utime

greenLed = Pin(15, Pin.OUT)
redLed = Pin(16, Pin.OUT)

analog_value = ADC(28)

SENSOR_MIN = 50000

greenLed.low()
redLed.low()
utime.sleep(1)

turnGreen = False
turnRed = False

try:
    while True:
        reading = analog_value.read_u16()
        print("ADC: ",reading)

        if reading < SENSOR_MIN and not turnRed:
            turnRed = True
            turnGreen = False
            redLed.high()
            greenLed.low()
        else:
            if not turnGreen:
                turnGreen = True
                turnRed = False
                greenLed.high()
                redLed.low()
        utime.sleep(1)

except KeyboardInterrupt:
    print('Interrupted')
    greenLed.low()
    redLed.low()
