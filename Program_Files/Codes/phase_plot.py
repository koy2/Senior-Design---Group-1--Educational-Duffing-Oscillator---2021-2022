# This program creates phase plots.

import gpiozero
import time
import array as arr
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

import tkinter as Tk
from tkinter import *


def fileChoice():
    for i in listbox_files.curselection():
        fileChoice = listbox_files.get(i)
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/file_to_open.txt', 'w') as file_object: #move to append state
            file_object.write(fileChoice)
            file_object.close()
        time.sleep(1)
        root.destroy()

def forward_difference(x,y):
    x2 = np.array(x)
    y2 = np.array(y)

    x3 = np.diff(x2)
    y3 = np.diff(y2)

    return (y3/x3)

def userexit():
    root.destroy()
    sys.exit(0)


while True:
    #Load the directories(folders)
    autosave_dir =os.listdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved')
    manualsave_dir =os.listdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save')

    #Alphabetize the directories
    autosave_dir.sort()
    manualsave_dir.sort()

    # The Window
    root = Tk()
    root.geometry('300x700')
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

    # Exit Button
    exit = Button(root, text ='Exit', height = 2, width =20, command=userexit).place(x =35, y =550)

    root.mainloop()

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

    a = []
    b = []
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
    d = np.array(a)
    d = np.delete(d,len(d)-1)
    v = np.array(forward_difference(b,a)) # time, distance
    fig,ax = plt.subplots()
    ax.plot(d,v, linewidth = 0.5)
    ax.set(xlabel= 'distance (mm)', ylabel = 'velocity (mm/s)', title = 'The Duffing Oscillator')
    ax.grid()
    plt.show()
