import tkinter as Tk
from tkinter import *
import numpy as np
import time
import gpiozero
from gpiozero import Button as Bt
import sys

pin0 = gpiozero.LED(6)
pin1 = gpiozero.LED(22) # Make pin 1 and pin 2 the same for single,


validNum = False

def calculate():
    global validNum
    validNum = False

    period = 1

    step_size_test = stepSize.get()
    period_duty_cycle_test = periodDutyCycle.get()



    label5 = Label(pop, text = "System Message: Invalid Input", font = ("Times New Roman", 14))
    label6 = Label(pop, text = "System Message", font = ("Times New Roman", 14))
    label7 = Label(pop, text = "                                                                  ", font = ("Times New Roman", 14))


    if not (checkInput(step_size_test) and checkInput(period_duty_cycle_test)):
        label7.place(x=50, y =170)
        label5.place(x=50, y =170)
        label7.place(x=50, y =120)
        label7.place(x=50, y =145)
        return

    if ((float(step_size_test) > 0) and (float(step_size_test) <= 1) and (float(period_duty_cycle_test) >= 0.04)):
        forward_test = np.arange(0,1,float(step_size_test))
        backward_test = np.arange(1,0,-1*float(step_size_test))
        period = (forward_test.size + backward_test.size)* float(period_duty_cycle_test)
        label7.place(x=50, y =120)
        label7.place(x=50, y =145)
        label3 = Label(pop, text = "Period: " + str(period) + " sec", font = ("Times New Roman", 14)).place(x=50, y =120)
        label4 = Label(pop, text = "Frequency: " + str(1/period) +" Hz", font = ("Times New Roman", 14)).place(x=50, y =145)
        label7.place(x=50, y =170)

        validNum = True
    else:
        label6.place(x =50, y =170)
        label7.place(x=50, y =120)
        label7.place(x=50, y =145)
        return


def confirm():
        global step_size
        global period_duty_cycle
        global forward
        global backward
        try:
            calculate() # check for exceptions on last time
            step_size = float(stepSize.get())
            period_duty_cycle = float(periodDutyCycle.get())
            forward = np.arange(0,1,float(step_size))
            backward = np.arange(1,0,-1*float(step_size))
            pop.destroy()
        except:
            return


def checkInput(x):
    num = False
    test_float = ['0','1','2','3','4','5','6','7','8','9','.']
    for y in x:
        num = False
        for z in test_float:
            if y == z:
                num = True
        if not num:
            break
    if not num:
        return False
    else:
        return True


def exit():
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_relay.txt', 'w') as file_object:
        file_object.write('0')
        file_object.close()
    pin0.off()
    pin1.off()
    pop.destroy()
    sys.exit(0)

def windowFreq():
    global stepSize
    global periodDutyCycle
    global pop
    pop = Tk()
    pop.title("Set Frequency")
    pop.geometry ('750x400')
    label1 = Label(pop, text = "Step Size:", font = ("Times New Roman", 14)).place(x =50, y =10)
    label2 = Label(pop, text = "Period of the Duty Cycle:", font = ("Times New Roman", 14)).place(x =50, y =50)
    stepSize = Entry(pop, width = 20)
    stepSize.focus_set()
    stepSize.pack(pady =10)
    periodDutyCycle = Entry(pop, width = 20)
    periodDutyCycle.focus_set()
    periodDutyCycle.pack(pady =10)

    btn_1= Button(pop, text = 'Calculate Frequency', height = 2, width =20, command=calculate).place(x =325, y =300)
    btn_2= Button(pop, text = 'Confirm', height = 2, width =10, command=confirm).place(x =550, y =300)
    btn_2= Button(pop, text = 'Close Program', height = 2, width =10, command=exit).place(x =50, y =300)
    pop.mainloop()

def enter_freq(): # an interupt
    global notNewFreq
    notNewFreq = False

changeFreq = Bt(21)
changeFreq.when_pressed = enter_freq

def duty_cycle(x,pin):
    global period_duty_cycle
    global notNewFreq
    pin.on()
    time.sleep(period_duty_cycle*x)
    pin.off()
    time.sleep(period_duty_cycle*(1-x))

def adjust_freq():
    global notNewFreq
    windowFreq()
    notNewFreq = True

#period_duty_cycle = 0.04 # do NOT go less than 0.04, may damage the relay
#step_size = 0.001 # MAX is 1, and do not allow 0

notNewFreq = True
#forward = np.arange(0,1,step_size)
#backward = np.arange(1,0,-1*step_size)

pin0.on()
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_relay.txt', 'r') as file_object:
        status_relay = file_object.read().rstrip()
        file_object.close()
if status_relay == '1':
        sys.exit(0)
else:
    pin0.on()
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_relay.txt', 'w') as file_object:
        file_object.write('1')
        file_object.close()
    windowFreq()
    while True:
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
        if not notNewFreq: # break through all for loops and change the frequency
            adjust_freq()