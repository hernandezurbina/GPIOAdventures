from utime import sleep
from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm0.freq(50)
pwm16 = PWM(Pin(16))
pwm16.freq(50)

### SERVO 1
pwm0.duty_u16(40)
print('Sleeping for 2 secs before shutting down SERVO 1')
sleep(2)
pwm0.duty_u16(0)
pwm0.deinit()
####################
print('Sleeping for 5 secs before turning on SERVO 2')
sleep(5)
### SERVO 2
pwm16.duty_u16(77)
print('Sleeping for 2 secs before shutting down SERVO 2')
sleep(2)
pwm16.duty_u16(0)
pwm16.deinit()
