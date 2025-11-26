import pi_servo_hat
import time

"""
This works well. To run it you need to put the phat in top of the rpi,
then put all the servos, and finally open the virtualenv venv
"""

test = pi_servo_hat.PiServoHat()
servo_number = 0

test.restart()

print("starting...")

for i in range(0, 90):
    print(i)
    test.move_servo_position(servo_number, i)
    time.sleep(1)

time.sleep(5)

for i in range(90, 0, -1):
    print(i)
    test.move_servo_position(servo_number, i)
    time.sleep(1)

print("done! :-)")

test.restart()