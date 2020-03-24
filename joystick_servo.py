from sense_hat import SenseHat
sense = SenseHat()

try:
    while True:
        for event in sense.stick.get_events():
            print(event.direction, event.action)
except KeyboardInterrupt:
    sense.clear()
    print('Bye')
