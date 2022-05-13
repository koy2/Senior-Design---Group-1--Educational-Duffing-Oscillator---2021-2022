# Educational Duffing Oscillator for Displaying Chaotic Motion (Code - Interface)

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import sys
import gpiozero
import os
pin0 = gpiozero.LED(12)

windowMaster_1 = 0 # prevents multiple "About this Project" windows


# For "About this Project" (Window 1)
def open_window_1():
    global windowMaster_1
    if windowMaster_1 == 0:

        def close_window_1():
            global windowMaster_1
            windowMaster_1 = 0
            root_1.destroy()

        windowMaster_1 = 1
        root_1 = Toplevel(root_0)
        root_1.title("About this Project")
        root_1.geometry('800x200')
        label_1a = Label(root_1, text = "Team Members: Yan Lok Ko (EE), Bryce C. Manz (EE), Amira Shagan (EE), Steven Zakirov (EE)", font = ("Times New Roman", 12))
        label_1a.place(x =50, y=20)
        label_1b = Label(root_1, text = "Advisors: Dr. Mohammad Zunoubi and Dr. Richard Halpern", font = ("Times New Roman", 12))
        label_1b.place(x =50, y=45)
        label_1c = Label(root_1, text = "---------------------------------------------------------------------------------------------------------------------------------", font = ("Times New Roman", 12))
        label_1c.place(x =50, y=65)
        label_1d = Label(root_1, text = "State University of New York at New Paltz", font = ("Times New Roman", 12))
        label_1d.place(x =50, y=85)
        label_1e = Label(root_1, text = "Senior Design - Fall 2021 & Spring 2022", font = ("Times New Roman", 12))
        label_1e.place(x =50, y=110)
        label_1f = Label(root_1, text = "Group 1 - Educational Duffing Oscillator for Displaying Chaotic Motion", font = ("Times New Roman", 12))
        label_1f.place(x =50, y=135)
        root_1.protocol("WM_DELETE_WINDOW", close_window_1)

#For the collecting data and plotting graph button
def open_window_2():
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
        system_state = file_object.read().rstrip()
        file_object.close()
    if system_state == '0000':
        btn_0a = Button(root_0, text = 'Stop: Collect Data and Plot Graph', height = 2, width =34, command= open_window_2).place(x =50, y =105)
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/save_mode.txt', 'w') as file_object: #move to append state
            file_object.write(str(var.get()))
            file_object.close()
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
            file_object.write('0001')
            file_object.close()
        print('System Message: Data Collection Started.')
    elif system_state == '0010':
        btn_0a = Button(root_0, text = 'Start: Collect Data and Plot Graph', height = 2, width =34, command= open_window_2).place(x =50, y =105)
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
            file_object.write('0011')
            file_object.close()
        print('System Message: Data Collection Ended. Close plot and listed data to continue.')
    else:
        print('System Message: Busy. Current task has not been completed.')

# For the "Load Saved Graph" Button
def open_window_3():
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
        system_state = file_object.read().rstrip()
        file_object.close()
    if system_state == '0000':
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
            file_object.write('0100')
            file_object.close()
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/save_mode.txt', 'w') as file_object: #move to append state
            file_object.write('3') #neither save nor autosave
            file_object.close()
    else:
        print('System Message: Busy. Current task has not been completed.')

# For exiting the program
def close_window_0():
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
        system_state = file_object.read().rstrip()
        file_object.close()
    if system_state == '0000':
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object:
            file_object.write('1111')
            file_object.close()
        root_0.destroy()
        pin0.off()
        os.system ('python3 reset.py')
        time.sleep(0.5)
        sys.exit(0)
    else:
        print('System Message: Please finish current task before exiting the program.')

#For the main window (Main Menu)
def open_window_0():
    global root_0
    global var
    root_0 = Tk()
    root_0.title("Main Menu")
    root_0.geometry ('430x1000')
    image0a = Image.open("/home/pi/mu_code/code/hamster.jpeg")
    image0a = image0a.resize((335,250), Image.ANTIALIAS)
    image0a_2 = ImageTk.PhotoImage(image0a)
    font1 = tkFont.Font(family = "Times", size=12, underline=1) # font setting for Save Mode
    var = IntVar() # for the Save Mode
    label_pic_0a = tk.Label (image = image0a_2)
    label_pic_0a.place (x=50, y = 235)
    label_0a = Label(root_0, text = "Educational Duffing Oscillator", font = ("Times New Roman", 14))
    label_0a.place(x =50, y=20)
    label_0b = Label(root_0, text = " for Displaying Chaotic Motion", font = ("Times New Roman", 14))
    label_0b.place(x =115, y=45)
    btn_0a = Button(root_0, text = 'Start: Collect Data and Plot Graph', height = 2, width =34, command= open_window_2).place(x =50, y =105)
    btn_0b = Button(root_0, text = 'Load Saved Graph', height = 2, width = 34, command= open_window_3).place(x =50, y =165)
    btn_0c = Button(root_0, text = 'About', height = 2, width =15, command= open_window_1).place(x =50, y =520)
    btn_0d = Button(root_0, text = 'Exit', height =2, width =15, command= close_window_0).place(x =227, y =520)
    label_0c = Label(root_0, text = "Save Mode:                                                                ", font = font1)
    label_0c.place(x =50, y=600)
    r_0a = Radiobutton(root_0, text= 'Automatic', variable = var, value = 0).place(x=50, y = 630)
    r_0b = Radiobutton(root_0, text= 'Manual', variable = var, value = 1).place(x=250, y = 630)
    label_0d = Label(root_0, text = "                                                                                   ", font = font1)
    label_0d.place(x =50, y=660)
    label_0e = Label(root_0, text = "Note: To change frequency,", font = ("Times New Roman", 12))
    label_0e.place(x =50, y=700)
    label_0f = Label(root_0, text = "please press PushButton (Hardware).", font = ("Times New Roman", 12))
    label_0f.place(x =100, y=725)
    root_0.protocol("WM_DELETE_WINDOW", close_window_0)
    root_0.mainloop()

# The Main Program
# Prevent the user from opening multiple instances
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_interface.txt', 'r') as file_object:
        status_interface = file_object.read().rstrip()
        file_object.close()
if status_interface == '1':
        sys.exit(0)
else:
    pin0.on()
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main1.txt', 'r') as file_object:
        status_main1 = file_object.read().rstrip()
        file_object.close()
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main2.txt', 'r') as file_object:
        status_main2 = file_object.read().rstrip()
        file_object.close()
    if(status_main1 == '0'):
        print('Warning: main_pt1.py may not be running.')
    if(status_main2 == '0'):
        print('Warning: main_pt2.py may not be running.')
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_interface.txt', 'w') as file_object:
        file_object.write('1')
        file_object.close()
    open_window_0()