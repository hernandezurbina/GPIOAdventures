import pi_servo_hat
import time

test = pi_servo_hat.PiServoHat()
servo_number = 4

test.restart()

for i in range(0, 90):
    print(i)
    test.move_servo_position(servo_number, i)
    time.sleep(1)

time.sleep(5)

for i in range(90, 0, -1):
    print(i)
    test.move_servo_position(servo_number, i)
    time.sleep(1)

test.restart()