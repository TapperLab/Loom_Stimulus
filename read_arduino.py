# set up arduino: https://learn.adafruit.com/ir-breakbeam-sensors/arduino
# communicating with python: https://pythonforundergradengineers.com/python-arduino-potentiometer.html

# get port number from Arduino IDE
# close Arduino IDE before running this code

import serial
import time
# import matplotlib.pyplot as plt

ser = serial.Serial('/dev/cu.usbmodem14301', 9600) # use computer port info from Arduino software
time.sleep(2)

states = []
data = []
for i in range(50): # duration to run this code for (TO DO: allow to manually stop code at end of session or to stop session based on other custom parameters)
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int

        state = 1 if num > 0 else num # TO DO: play around with other thresholds to determine what qualifies as a true "beam break"
        if i != 0:
	        if state != data[i-1]:
		        if state:
		        	print('unbroken')
		        else:
		        	print('broken') # TO DO: Make loom play if other criteria (i.e. duration since the previous loom) have been met
        
        states.append(state) # add int to data list
        data.append(num)

ser.close()

# # build the plot (TO DO: have some sort of output plot that's actually relevant)
# plt.plot(data)
# plt.xlabel('Time')
# plt.ylabel('Potentiometer Reading')
# plt.title('Potentiometer Reading vs. Time')
# plt.show()
