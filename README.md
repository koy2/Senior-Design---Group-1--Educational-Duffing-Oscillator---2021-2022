## State University of New York at New Paltz: Senior Design I & II (2021-2022)
***
### About this Project:
Group 1: Educational Duffing Oscillator for Displaying Chaotic Motion

Team Members: Yan Lok Ko (EE), Bryce C. Manz (EE), Amira Shagan (EE), Steven Zakirov (EE)

Advisors: Dr. Richard Halpern (Physics) and Dr. Mohammad Zunoubi (EE)
***

### Hardware Diagram

![hardware](https://user-images.githubusercontent.com/100855196/168451199-951625f5-cbef-4280-ab89-30b381edbc63.PNG)

*Figure 01. Hardware Diagram*

This is the hardware diagram for the apparatus the programs were used for.

***

### Software Flowchart of the Interface
From the interface, the user can collect data, load a saved graph, change the save mode, view the "About Us", and exit the program. The interface is comprised of three programs running concurrently: main_pt1.py, main_pt2.py, and interface.py. The first program collects the data from the sensor and writes it into the files, one for time and one for distance, as well as plots the graph. The second program executes the save function after the windows for the plot and the listed data are closed; it also lists the data. The user interface itself is created by interface.py. User input from the interface determines how the first two programs will execute.

![interface](https://user-images.githubusercontent.com/100855196/168206307-388bd44c-f87f-4ab0-b0ee-81be744a5bc1.PNG)

*Figure 02. Flowchart for the Interface*
***
### Solid State Relay
There are two files for the solid state relay that are executed by (4a) and (4b). The one with the word 'double' runs two relay; the other runs a single relay. The period is this: (Period of the duty cycle)(the number of full steps made by dividing 1 by the step size). The step size range is (0,1], and the period of the duty cycle cannot be less than 0.04. This forces the minimum step size to be 0.05 (not tested for in current code).

***

### Required Import Statements on Raspberry Pi
* pip3 install tk
* pip3 install adafruit-circuitpython-vl53l0x
* pip3 install numpy
* pip3 install matlibplot
* pip3 install pandas
* pip3 install pillow
* pip3 install arr
* pip3 install adafruit-blinka

***

### Other Important Notes
* reset.py resets the files so that the interface can be reset.
* If the relay does not run, make sure that in Program_Files => System_Communication => status_relay.txt != 1. You can edit in a 0. This is not done automatically to avoid any relay damage that may result if two relay programs are running at a time.
* The pi and the power supply will need two separate 20 A outlets to run properly.
* The pi needs at least 32 GB of memory and the username MUST be pi or the paths for the files must be changed.
* DO NOT do pip3 install board 
* Go to Interfaces in the Raspberry Pi Configuration and enable I2C and SPI

***
### When All the Hardware has been Assembled:
1) Measure the offset using offset.py (Program #6) - if desired, can also put in one by editing offset.txt in System_Communication 
2) Run Reset (Program #0)
3) Open program #1, #2, #3 (in that order is best). A LED will light up after each program is started.
4) Relay - Use Program #4a, or connect another relay to use Program #4b, or write your own. (relay.txt may have to be set to 0 in System_Communication for #4a/#4b to run)

***
### References:
See **References.pdf**, please.
***

***

### YouTube Link
https://www.youtube.com/watch?v=xNzb_8S5Ylo
