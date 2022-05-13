## State University of New York at New Paltz: Senior Design I & II (2021-2022)
***
### About this Project:
Group 1: Educational Duffing Oscillator for Display Chaotic Motion

Team Members: Yan Lok Ko (EE), Bryce C. Manz (EE), Amira Shagan (EE), Steven Zakirov (EE)

Advisors: Dr. Richard Halpern (Physics) and Dr. Mohammad Zunoubi (EE)
***

### Hardware Diagram

![hardware](https://user-images.githubusercontent.com/100855196/168207415-3be740d0-8f18-4b6e-a5ba-d93967334297.PNG)

*Figure 01. Hardware Diagram*

This is the hardware diagram for the apparatus the programs were used for.

### Software Flowchart of the Interface
From the interface, the user can collect data, load a saved graph, change the save mode, view the "About Us", and exit the program. The interface is comprised of three programs running concurrently: main_pt1.py, main_pt2.py, and interface.py. The first program collects the data from the sensor and writes it into the files, one for time and one for distance, as well as plots the graph. The second program executes the save function after the windows for the plot and the listed data are closed; it also lists the data. The user interface itself is created by interface.py. User input from the interface determines how the first two programs will execute.

![interface](https://user-images.githubusercontent.com/100855196/168206307-388bd44c-f87f-4ab0-b0ee-81be744a5bc1.PNG)

*Figure 02. Flowchart for the Interface*
***
### Solid State Relay
There are two files for the solid state relay: (4a) and (4b). The one with the word 'double' runs two relay; the other runs a single relay. The period is this: (Period of the duty cycle) x (the number of full steps made by dividing 1 by the step size). The step size range is (0,1], and the period of the duty cycle cannot be less than 0.04. This forces the minimum step size to be 0.05 (not tested for in current code).

***

### Required Import Statements on Raspberry Pi
### File Descriptions
### Other Important Notes
