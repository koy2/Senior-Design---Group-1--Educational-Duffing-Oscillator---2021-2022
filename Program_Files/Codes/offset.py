import gpiozero
import time

# For the Tof(Time of Fight) sensor
import board
import busio
import adafruit_vl53l0x

# Initialize the ToF sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)
offset = sensor.range # Collect data (distance pendulum is from laser)

with open('/home/pi/Desktop/Educational_Duffing_Oscillator_for_Displaying_Chaotic_Motion/Program_Files/System_Communication/offset.txt', 'w') as file_object: #move to append state
    file_object.write(str(offset))
    file_object.close()