"""
runs only on the RPi Pico
"""
import math
from machine import ADC, SPI, Pin
from time import sleep
from ST7735 import TFT, TFTColor
from sysfont import sysfont

sck = 18
mosi = 19
miso = 16
dc = 21
rst = 20
cs = 17

spi = SPI(0, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))

tft = TFT(spi=spi, aDC=dc, aReset=rst, aCS=cs)
tft.initr()
tft.rgb(True)

thermistor = ADC(27)
photoresistor = ADC(26)

secs = 10
secsPause = 20

minTemp = float('inf')
maxTemp = float('-inf')
minLight = float('inf')
maxLight = float('-inf')

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
    temp_fahr = (temp_cels * 1.8) + 32
    return temp_cels

def displayTemp(minTemp, maxTemp, currTemp):
    tft.fill(TFT.BLACK);

    tft.rotation(3)
    v = 30
    tft.text((25, v), "Temp:", TFT.GREEN, sysfont, 3, nowrap=True)
    v += sysfont["Height"] * 3
    tft.text((25, v), "min: {:.2f}c".format(minTemp), TFT.WHITE, sysfont, 2, nowrap=False)
    v += sysfont["Height"] * 2
    tft.text((25, v), "max: {:.2f}c".format(maxTemp), TFT.WHITE, sysfont, 2, nowrap=False)
    v += sysfont["Height"] * 2
    tft.text((25, v), "now: {:.2f}c".format(currTemp), TFT.WHITE, sysfont, 2, nowrap=False)

def displayLight(minLight, maxLight, currLight):
    tft.fill(TFT.BLACK);

    tft.rotation(3)
    v = 30
    tft.text((25, v), "Light:", TFT.GREEN, sysfont, 3, nowrap=True)
    v += sysfont["Height"] * 3
    tft.text((25, v), "min: {:.2f}%".format(minLight), TFT.WHITE, sysfont, 2, nowrap=False)
    v += sysfont["Height"] * 2
    tft.text((25, v), "max: {:.2f}%".format(maxLight), TFT.WHITE, sysfont, 2, nowrap=False)
    v += sysfont["Height"] * 2
    tft.text((25, v), "now: {:.2f}%".format(currLight), TFT.WHITE, sysfont, 2, nowrap=False)

def displayImage(imageFile):
    tft.fill(TFT.BLACK)
    tft.rotation(0)
    f=open(imageFile, 'rb')
    if f.read(2) == b'BM':  #header
        dummy = f.read(8) #file size(4), creator bytes(4)
        offset = int.from_bytes(f.read(4), 'little')
        hdrsize = int.from_bytes(f.read(4), 'little')
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
            depth = int.from_bytes(f.read(2), 'little')
            if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                print("Image size:", width, "x", height)
                rowsize = (width * 3 + 3) & ~3
                if height < 0:
                    height = -height
                    flip = False
                else:
                    flip = True
                w, h = width, height
                if w > 128: w = 128
                if h > 160: h = 160
                tft._setwindowloc((0,0),(w - 1,h - 1))
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))

#######################################################
try:
    print("Starting...")
    while True:

        # first read TEMP
        temp = readTemp()

        if temp > maxTemp:
            maxTemp = temp
        if temp < minTemp:
            minTemp = temp

        print('Temp:\tMIN: {:.2f}C\tMAX: {:.2f}C\tCURR: {:.2f}C'.format(minTemp, maxTemp, temp))
        displayTemp(minTemp, maxTemp, temp)
        print('Pausing for {} secs'.format(secs))
        sleep(secs)

        # then read LIGHT
        light = readLight()

        if light > maxLight:
            maxLight = light
        if light < minLight:
            minLight = light

        print('Light:\tMIN: {:.2f}%\tMAX: {:.2f}%\tCURR: {:.2f}%'.format(minLight, maxLight, light))
        displayLight(minLight, maxLight, light)
        print('Pausing for {} secs'.format(secs))
        sleep(secs)

        # finally show a pretty PIC!
        displayImage('vico.bmp')
        print('Pausing for {} secs'.format(secs))


        print('Pausing for {} secs'.format(secsPause))
        print()
        sleep(secsPause)

except KeyboardInterrupt:
    tft.fill(TFT.BLACK);
    spi.deinit()
    print("Finishing!")
