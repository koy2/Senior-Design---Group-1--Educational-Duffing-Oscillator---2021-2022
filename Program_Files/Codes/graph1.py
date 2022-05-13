import array as arr
import numpy as np
import matplotlib as plt

# Make the arrays
a = arr.array('i', []) #the array of integers for the distance
b = arr.array ('d', []) #the array of doubles for the time

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

# Now we plot:
t = np.array(b)
d = np.array(a)
fig,ax = plt.subplots()
ax.plot(t,d)
ax.set(xlabel= 'time(s)', ylabel = 'distance (mm)', title = 'The Duffing Oscillator')
ax.grid()
plt.show()