### dmesg > yes.txt
### dmesg > no.txt
### diff yes.txt no.txt
### sudo python3 a.py

### port
import serial
import struct
import time                             # time immedita

### draw 
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import matplotlib.animation as animation
from matplotlib import style

### port
se = serial.Serial()
se.baudrate = 38400
se.bytesize = 8
se.stopbits = 1
se.port = '/dev/ttyACM0'
se.timeout = 0.5
se.rtscts = 1
se.open()                               # open port

x1 = 0
x2 = 0

### ID
def IDFunc(ID):
    if ID == 'FB13':
        Sensor = 1
    else:
        Sensor = 2
    return Sensor

while True:
    response = se.readline()
    if response != "b''":
        tm = time.strftime("%H:%M:%S")
        response = str(response)
        ### CO2 
        if response[13:14] == 'c':
            ### ID
            ID = response[37:41]
            Sensor = IDFunc(ID)
            
            #~ print("CO2: ",response[63:69])
            #~ int(int('0x034B', 16))
            CO2 = int(int(response[63:69], 16))
            print("Sensor:", Sensor, "; CO2:",CO2)

            if Sensor == 1:
                f = open("note1.txt", 'a')
                f.write(str(x1)+ ',' + str(tm) + ',' + str(CO2) + '\n') 
                x1 = x1 + 1
            else: 
                f = open("note2.txt", 'a')
                f.write(str(x2)+ ',' + str(tm) + ',' + str(CO2) + '\n') 
                x2 = x2 + 1
            f.close()
            

        ### Temp / Hum
        #~ else: 
            #~ ### ID
            #~ ID = response[36:40]
            #~ IDFunc(ID)
            
            
            #~ ##~ print("Temp: ",response[63:69])
            #~ ##~ print("Hume: ",response[80:86])
            #~ Temp = int(int(response[63:69], 16))
            #~ Hume = int(int(response[80:86], 16))
            #~ print("Temp:",Temp)
            #~ print("Hume:",Hume)
        #~ print("-----")
