"""
runs only on the RPi Pico
"""

from machine import ADC, Pin, UART
from time import sleep
import math

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
thermistor = ADC(27)
greenLed = Pin(15, Pin.OUT)
redLed = Pin(16, Pin.OUT)
photoresistor = ADC(26)
turnGreen = False
turnRed = False
SENSOR_THRES = 80

def readLight():
    light = photoresistor.read_u16()
    light = round((light/65535)*100, 2)
    return light

def readTemp():
    temp = thermistor.read_u16()
    Vr = 3.3 * float(temp) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    temp_cels = temp - 273.15
    #temp_fahr = (temp_cels * 1.8) + 32
    return temp_cels

try:
    print("Starting...")
    print(uart)
    while True:
        light = readLight()
        temp = readTemp()
        
        print('Light: {:.2f}% Temp: {:.2f}C'.format(light, temp))
        outputStr = 'Light: {:.2f}% Temp: {:.2f}C\n'.format(light, temp)
        uart.write(outputStr)
        
        if light < SENSOR_THRES:
            turnGreen = False
            greenLed.low()
            
            if not turnRed:                
                turnRed = True            
                redLed.high()                    
        else:
            turnRed = False
            redLed.low()
            
            if not turnGreen:
                turnGreen = True
                greenLed.high()        
        sleep(1)
except KeyboardInterrupt:
    print("Finishing!")
    greenLed.low()
    redLed.low()    
    
