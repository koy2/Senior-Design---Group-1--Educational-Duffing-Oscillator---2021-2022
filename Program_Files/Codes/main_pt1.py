# This code collects data from sensor and writes to file. It also plots the graph.

import gpiozero
import time
import array as arr
import sys
import os

import tkinter as Tk
from tkinter import *

from gpiozero import Button as Bt


#For the graph
import matplotlib.pyplot as plt
import numpy as np

# For the Tof(Time of Fight) sensor
import board
import busio
import adafruit_vl53l0x

# Initialize the ToF sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

#Initialize the LED and Switch
pin0 = gpiozero.LED(16)
pin1 = gpiozero.LED(5)

# (Other) Global variables
controlSwitch = 0 #for the switch
printInfo = False # boolean

sensor.measurement_timing_budget = 20000 # in nanoseconds #This can be lowered for speed but the trade off is accuracy at long distanc

#get the offset
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/offset.txt', 'r') as file_object:
    offset = file_object.read().rstrip()
    file_object.close()

# Prevent the user from opening multiple instances
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main1.txt', 'r') as file_object:
        status_main1 = file_object.read().rstrip()
        file_object.close()
if status_main1 == '1':
        sys.exit(0)
else:
    pin0.on()
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main1.txt', 'w') as file_object:
        file_object.write('1')
        file_object.close()
    while True:
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
            system_state = file_object.read().rstrip()
            file_object.close()

        if system_state == '0001':
            pin1.on()
            t4=0
            t4 = time.perf_counter() # capture start time reference
            distance = sensor.range # Collect data (distance pendulum is from laser)
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_time.txt', 'w') as file_object:
                file_object.write('0') # start at t = 0
                file_object.close()
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_distance.txt', 'w') as file_object:
                file_object.write(str(distance))  #Put the data into the file
                file_object.close()
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                file_object.write('0010')
                file_object.close()
        elif system_state == '0010':
            t2 = time.perf_counter()
            distance = sensor.range # Collect data (distance pendulum is from laser)
            distance = distance - int(offset) # subtract the offset
            x = t2-t4
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_time.txt', 'a') as file_object:
                file_object.write('\n')
                file_object.write(str(x))
                file_object.close()
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_distance.txt', 'a') as file_object:
                file_object.write('\n')
                file_object.write(str(distance))  #Put the data into the file
                file_object.close()
        elif (system_state == '0011') or (system_state =='0100'): # make the graph
            pin1.off()
            # Make the arrays
            a = arr.array('i', []) #the array of integers for the distance
            b = arr.array ('d', []) #the array of doubles for the time

            if(system_state == '0011'): # from temp data
                # Load the arrays
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_distance.txt', 'r') as file_object:
                    distance_data=file_object.readlines()
                    file_object.close()
                for line in distance_data:
                    a.append(int(line.rstrip()))
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_time.txt', 'r') as file_object:
                    time_data=file_object.readlines()
                    file_object.close()
                for line in time_data:
                    b.append(float(line.rstrip()))

            else: #loading a file
                def fileChoice():
                    for i in listbox_files.curselection():
                        fileChoice = listbox_files.get(i)
                        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/file_to_open.txt', 'w') as file_object: #move to append state
                            file_object.write(fileChoice)
                            file_object.close()
                        time.sleep(1)
                        root.destroy()

                def return_main():
                    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                        file_object.write('0000')
                        file_object.close()
                    root.destroy()

                #Load the directories(folders)
                autosave_dir =os.listdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved')
                manualsave_dir =os.listdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save')

                #Alphabetize the directories
                autosave_dir.sort()
                manualsave_dir.sort()

                # The Window
                root = Tk()
                root.geometry('300x600')
                root.title("Select File")

                # The Scrollbar
                scrollbar = Scrollbar(root)
                scrollbar.pack(side = RIGHT, fill =BOTH)

                # Listbox for the files
                listbox_files = Listbox(root, height = 20, width = 34)
                listbox_files.pack(side = LEFT, padx = 20, pady=20, anchor = 'n')
                listbox_files.config(yscrollcommand = scrollbar.set)

                #Load files onto listbox - manual save files first
                for line in manualsave_dir:
                    listbox_files.insert(END,line)
                for line in autosave_dir:
                    listbox_files.insert(END,line)

                #Configure the scrollbar
                scrollbar.config (command = listbox_files.yview)

                # Button for Submitting Chosen File
                fileChoice = Button(root, text ='Load Data', height = 2, width =20, command=fileChoice).place(x =35, y =450)

                #If the user exits without selecting something
                root.protocol("WM_DELETE_WINDOW", return_main)

                root.mainloop()

                #Ready to plot, signal other program
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                    file_object.write('0110')
                    file_object.close()


                #Load the arrays
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/file_to_open.txt', 'r') as file_object:
                    fileChoice = file_object.read().rstrip()
                    file_object.close()

                directoryChoice = 0
                if fileChoice in manualsave_dir:
                    directoryChoice = 1

                if directoryChoice == 1:
                    file_path_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save/' + fileChoice + '/' + fileChoice + '_distance.txt'
                    file_path_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save/' + fileChoice + '/' + fileChoice + '_time.txt'
                else:
                    file_path_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved/' + fileChoice + '/' + fileChoice + '_distance.txt'
                    file_path_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved/' + fileChoice + '/' + fileChoice + '_time.txt'

                # Distance Data
                with open(file_path_distance, 'r') as file_object:
                    distance_data=file_object.readlines()
                    file_object.close()
                for line in distance_data:
                        a.append(int(line.rstrip()))

                # Time Data
                with open(file_path_time, 'r') as file_object:
                    time_data=file_object.readlines()
                    file_object.close()
                for line in time_data:
                        b.append(float(line.rstrip()))

            # Now we plot:
            t = np.array(b)
            d = np.array(a)
            fig,ax = plt.subplots()
            ax.plot(t,d)
            ax.set(xlabel= 'time(s)', ylabel = 'distance (mm)', title = 'The Duffing Oscillator')
            ax.grid()
            plt.show()

            #Check system_state again
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
                system_state = file_object.read().rstrip()
                file_object.close()

            if(system_state == '0101'): # move to waiting state
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                    file_object.write('0000')
                    file_object.close()

            else: # change system_state to '0101' # for system_state == '0100' and system_state == '0110'
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                    file_object.write('0101')
                    file_object.close()

        elif system_state == '1111':
            pin0.off()
            sys.exit(0)