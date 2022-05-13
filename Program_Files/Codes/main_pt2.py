# This code saves the data and lists the graphed data.

import tkinter as Tk
from tkinter import *
import os
import gpiozero

import shutil

windowMaster = False

pin0 = gpiozero.LED(13)

def scrolldata(*args):
    listbox_time.yview(*args)
    listbox_distance.yview(*args)

def save():
    global windowMaster
    fileMade = False
    def close_window():
        global windowMaster
        windowMaster = False
        save_window.destroy()
    def submit():
        runName = folder_name.get()
        try:
            os.mkdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save/' + runName)
            fileMade = True
        except:
            message = Label(save_window, text = "Invalid File Name. Please enter another.", font = ("Times New Roman", 12))
            message.place(x =50, y=200)
            fileMade = False
        if fileMade:
            src_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_time.txt'
            src_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_distance.txt'
            dst_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save/' + runName +'/' + runName + '_time.txt'
            dst_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save/' + runName +'/' + runName + '_distance.txt'
            shutil.copyfile(src_time, dst_time)
            shutil.copyfile(src_distance, dst_distance)
            message = Label(save_window, text = "Save Successful.                                                                 ", font = ("Times New Roman", 12))
            message.place(x =50, y=200)
            close = Button(save_window, text = 'Close', height = 2, width =20, command=close_window).place(x =400, y =200)
            btn_save = Button(root, text = 'Save Data', height = 2, width =34, command=save, state = 'disabled').place(x =75, y =900)

    # save the data (manual save)
    if not windowMaster:
        windowMaster = True
        save_window = Toplevel(root)
        save_window.geometry('700x300')
        save_window.title("Save Data")
        instr= Label(save_window, text = "Name of Folder for the Run:", font = ("Times New Roman", 14))
        instr.place(x =50, y=20)
        folder_name= Entry(save_window, width =40)
        folder_name.focus_set()
        folder_name.pack(pady =50)
        submit = Button(save_window, text = 'Submit', height = 2, width =20, command=submit).place(x =400, y =200)
        save_window.protocol("WM_DELETE_WINDOW", close_window)


# Prevent the user from opening multiple instances
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main2.txt', 'r') as file_object:
        status_main2 = file_object.read().rstrip()
        file_object.close()
if status_main2 == '1':
        sys.exit(0)
else:
    pin0.on()
    with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main2.txt', 'w') as file_object:
        file_object.write('1')
        file_object.close()
    while True:
        #Check system_state
        with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
            system_state = file_object.read().rstrip()
            file_object.close()

        if(system_state == '0011') or (system_state == '0110'): # state where a graph is plotted

            # File Setup
            # Assume loading from temporary data
            file_path_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_distance.txt'
            file_path_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_time.txt'

            #If the user is loading a graph
            if(system_state == '0110'):
                autosave_dir =os.listdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved')
                manualsave_dir =os.listdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Manual_Save')
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


            # The Save Mode
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/save_mode.txt', 'r') as file_object:
                save_mode = file_object.read().rstrip()
                file_object.close()
            # The Window
            root = Tk()
            root.geometry('500x1000')
            root.title("Listed Data")

            # Labels
            label_time = Label(root, text = "Time [s]", font = ("Times New Roman", 14))
            label_time.place(x =100, y=20)
            label_distance = Label(root, text = "Distance [mm]", font = ("Times New Roman", 14))
            label_distance.place(x =325, y=20)

            # Save Button if Manual Save
            if (save_mode == '1'):
                btn_save = Button(root, text = 'Save Data', height = 2, width =34, command=save).place(x =75, y =900)

            # The Scrollbar
            scrollbar = Scrollbar(root)
            scrollbar.pack(side = RIGHT, fill =BOTH)

            # For time
            listbox_time = Listbox(root, height = 45, width =25)
            listbox_time.pack(side = LEFT, padx = 20, pady=60, anchor = 'n')
            listbox_time.config(yscrollcommand = scrollbar.set)
            with open(file_path_time, 'r') as file_object:
                time_data=file_object.readlines()
                file_object.close()
            for line in time_data:
                listbox_time.insert(END,line.rstrip() + ' [s] ')

            #For distance
            listbox_distance = Listbox(root, height = 45, width=25)
            listbox_distance.pack(side = RIGHT, padx =20,pady=60, anchor = 'n')
            listbox_distance.config(yscrollcommand= scrollbar.set)
            with open(file_path_distance, 'r') as file_object:
                distance_data=file_object.readlines()
                file_object.close()
            for line in distance_data:
                listbox_distance.insert(END,line.rstrip() + ' [mm] ')

            #Configure the scrollbar
            scrollbar.config (command = scrolldata)
            root.mainloop()

            # save the data (autosave)
            if (save_mode == '0'):
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/run_number.txt', 'r') as file_object:
                    run_number = file_object.read().rstrip()
                    file_object.close()
                os.mkdir(path = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved/Auto_' + run_number)

                # Copy the temporary files
                src_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_time.txt'
                src_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/Temp_Data/temp_distance.txt'
                dst_time = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved/Auto_' + run_number +'/Auto_' + run_number + '_time.txt'
                dst_distance = '/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Saved_Runs/Autosaved/Auto_' + run_number +'/Auto_' + run_number + '_distance.txt'
                shutil.copyfile(src_time, dst_time)
                shutil.copyfile(src_distance, dst_distance)

                # increment the run number
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/run_number.txt', 'w') as file_object:
                    file_object.write(str(int(run_number)+1))
                    file_object.close()

            #Check system_state again
            with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'r') as file_object:
                system_state = file_object.read().rstrip()
                file_object.close()

            if(system_state == '0101'): # move to waiting state
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                    file_object.write('0000')
                    file_object.close()

            else: # change system_state to '0101'
                with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object: #move to append state
                    file_object.write('0101')
                    file_object.close()

        elif(system_state == '1111'):
            pin0.off()
            sys.exit(0)