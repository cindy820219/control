### dmesg > yes.txt
### dmesg > no.txt
### diff yes.txt no.txt
### sudo python3 a.py

### port
import serial
import struct
import time                             # time immedita

### draw 
#~ import matplotlib.pyplot as plt
#~ from tkinter import *
#~ import numpy as np
#~ import matplotlib.animation as animation
#~ from matplotlib import style

### port
se = serial.Serial()
se.baudrate = 38400
se.bytesize = 8
se.stopbits = 1
se.port = '/dev/ttyUSB0'
se.timeout = 0.5
se.rtscts = 1
se.open()                               # open port

CO2_x1 = 0
CO2_x2 = 0

TH_x1 = 0
TH_x2 = 0

### ID
def IDFunc(ID):
    #~ 45E4 / C720
    #~ print("ID: ", ID)
    if ID == '45E4':
        Sensor = 1
    else:
        Sensor = 2
    return Sensor

while True:
    response = se.readline()
    #~ print(response)
    
    if response != "b''":
        tm = time.strftime("%H:%M")
        Day = time.strftime("%D")
        response = str(response)
        
        ### CO2 
        if response[13:14] == 'c':
            ### ID
            ID = response[37:41]
            Sensor = IDFunc(ID)
            
            #~ print("CO2: ",response[63:69])
            #~ int(int('0x034B', 16))
            CO2 = int(int(response[63:69], 16))
            print("Sensor:", Sensor, ",  Time:", tm, "; CO2:", CO2)

            if Sensor == 1:
                f = open("CO2_1.txt", 'a')
                f.write(str(CO2_x1)+ ',' + str(tm) + ',' + str(CO2) + '\n') 
                CO2_x1 = CO2_x1 + 1
            else: 
                f = open("CO2_2.txt", 'a')
                f.write(str(CO2_x2)+ ',' + str(tm) + ',' + str(CO2) + '\n') 
                CO2_x2 = CO2_x2 + 1
            f.close()


        ### Temp / Hum
        if response[13:14] == 't':
            ### ID
            ID = response[36:40]
            Sensor = IDFunc(ID)
            
            ##~ print("Temp: ",response[63:69])
            ##~ print("Hume: ",response[80:86])
            Temp = int(int(response[63:69], 16))
            Hume = int(int(response[80:86], 16))
            
            print("Sensor:", Sensor, ",  Time:", tm, "; Temp:", Temp, ", Hume:", Hume)
            
            if Sensor == 1:
                fTH = open("TH_1.txt", 'a')
                fTH.write(str(TH_x1)+ ',' + str(tm) + ',' + str(Temp) + ',' + str(Hume) + '\n') 
                TH_x1 = TH_x1 + 1
            else: 
                fTH = open("TH_2.txt", 'a')
                fTH.write(str(TH_x2)+ ',' + str(tm) + ',' + str(Temp) + ',' + str(Hume) + '\n') 
                TH_x2 = TH_x2 + 1
            fTH.close()

