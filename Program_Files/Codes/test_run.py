# For running a series of experiments
import numpy as np
import time
import gpiozero
from gpiozero import Button as Bt
import sys

pin0 = gpiozero.LED(6)
pin1 = gpiozero.LED(22) # Make pin 1 and pin 2 the same for single,


period_duty_cycle = 0.04 # do NOT go less than 0.04, may damage the relay
#step_size = [0.050]
step_size = np.arange(0.7, 0.05, -0.05) # MAX is 1, and do not allow 0

def duty_cycle(x,pin):
    global period_duty_cycle
    global notNewFreq
    pin.on()
    time.sleep(period_duty_cycle*x)
    pin.off()
    time.sleep(period_duty_cycle*(1-x))

notNewFreq = True
for element in step_size:
    forward = np.arange(0,1,element)
    backward = np.arange(1,0,-1*element)
    print(forward)
    for i in range(0,100):
        pin0.on()
        for x in forward:
            if notNewFreq:
                duty_cycle(x, pin1)
            else:
                break
        for x in backward:
            if notNewFreq:
                duty_cycle(x, pin1)
            else:
                break
        pin1.off()