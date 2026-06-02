from sense_hat import SenseHat

sense = SenseHat()

R = (255, 0, 0)     # red
O = (0, 0, 0)       # off / black

heart = [
    O, R, R, O, O, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
]


print("Press the joystick button to display message...")

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            sense.show_message("Hello!")
            #sense.set_pixels(heart)    
            
 