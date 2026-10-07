import machine
from machine import Pin, PWM
import utime

pwm = PWM(Pin(13))
pwm.freq(1000)

stby = Pin(12, Pin.OUT)
stby.value(1)

in1 = Pin(14, Pin.OUT)
in2 = Pin(15, Pin.OUT)

# for forward

def forward(speed):
    in1.value(1)
    in2.value(0)
    pwm.duty_u16(speed)

# for backward

def reverse(speed):
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(speed)
    
# to stop
    
def stop():
    in1.value(0)
    in2.value(0)
    pwm.duty_u16(0)
    
# code

#
utime.sleep(5)

#
forward(32000)
utime.sleep(3)

#
stop()
utime.sleep(5)

#
reverse(32000)
utime.sleep(3)

#
stop()

