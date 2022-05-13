# Educational Duffing Oscillator for Displaying Chaotic Motion (Code - Reset)
# This is for the reset file.
import time
import gpiozero

# Turn off all LED
led_list = [5,6,12,13,16]

for x in led_list:
    pin = gpiozero.LED(x)
    pin.off()

# For status_interface.txt:
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_interface.txt', 'w') as file_object:
        file_object.write('0')
        file_object.close()

# For status_main1.txt:
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main1.txt', 'w') as file_object:
        file_object.write('0')
        file_object.close()

# For status_main2.txt:
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/status_main2.txt', 'w') as file_object:
        file_object.write('0')
        file_object.close()

# For system_state.txt
with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/system_state.txt', 'w') as file_object:
        file_object.write('0000')
        file_object.close()

# Notify user:
print("System reset complete. Please proceed with restarting or opening the programs.")

#Automatically close in five seconds
time.sleep(5)