### dmesg > yes.txt
### dmesg > no.txt
### diff yes.txt no.txt
### sudo python3 a.py

### sudo chown nien:nien note1.txt note2.txt
### wc -l [file]

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

### Member 
'''
#1  8F43 ; #2   C713 ; #3   D44E
#4  D334 ; #5   9B34 ; #6   E41E'':''
#7  B414 ; #8   630E ; #9   4056
#10 3C2D
''' 
dict = {'8F43':'1' , 'C713':'2', 'D44E':'3' , 'D334':'4' , '9B34':'5', 'E41E':'6',  'B414':'7' , '630E':'8', '4056':'9', '3C2D':'10'}

### port
se = serial.Serial()
se.baudrate = 38400
se.bytesize = 8
se.stopbits = 1
#~ se.port = '/dev/ttyACM0'
se.port = '/dev/ttyUSB0'
se.timeout = 0.5
se.rtscts = 1
se.open()                               # open port

#~ global Count
Count = 0

NOTE = '#'
NOTE1 = '*'

while True:
    response = se.readline()
    #~ print('response:', response)

    if response != "b''":
        tm = time.strftime("%H:%M:%S")
        Day = time.strftime("%D")
        #~ print(Day)
        response = str(response)

        ### CO2 
        if response[13:14] == 'c':
            ### ID
            ID = response[37:41]
            Sensor = dict[ID]
            
            if Sensor == '10':
                print('------------------------------')
            
            if Sensor == '10':
                Count = Count + 1
                
                
            #~ print("CO2: ",response[63:69])
            #~ int(int('0x034B', 16))
            CO2 = int(int(response[63:69], 16))
            if int(CO2) > 65500
                CO2 = str(int(CO2) - 65536)
                
            print(NOTE + str(Count), "Sensor:", Sensor, ",  Time:", tm, "; CO2:", CO2)
                
            Str_note = 'CO2_'
            Str_txt = '.txt'
            
            f = open( Str_note + Sensor + Str_txt, 'a')
            f.write(str(Count)+ ',' + str(tm) + ',' + str(CO2) + '\n') 
            
            
            f.close()
'''
    #~ else:
        ### Temp / Hum
        if response[13:14] == 't':
            ### ID
            ID = response[36:40]
            Sensor = dict[ID]

            Temp = int(int(response[63:69], 16))
            Hume = int(int(response[80:86], 16))
            
            Str_note = 'TH_'
            Str_txt = '.txt'
            
            print(NOTE1 + str(Count), "Sensor:", Sensor, ",  Time:", tm, "; Temp:", Temp, ", Hume:", Hume)
            
            f = open( Str_note + Sensor + Str_txt, 'a')
            f.write(str(Count)+ ',' + str(tm) + ',' + str(Temp) + ',' + str(Hume) + '\n') 
    
            if tag0 == 1 and Sensor == '4':
               tag0 = 0


            f.close()
'''
