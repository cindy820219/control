### dmesg > yes.txt
### dmesg > no.txt
### diff yes.txt no.txt
### sudo python3 a.py

import serial
import struct
import time                             # time immedita

se = serial.Serial()
se.baudrate = 38400
se.bytesize = 8
se.stopbits = 1
se.port = '/dev/ttyACM0'
se.timeout = 0.5
se.rtscts = 1


se.open()                               # open port

def IDFunc(ID):
    print (time.strftime("%H:%M:%S"))
    if ID == 'FB13':
        Sensor = 1
    else:
        Sensor = 2
    print("Sensor: ", Sensor)

while True:
    response = se.readline()

    if response != "b''":
        response = str(response)
        #~ print(response)
        
        ### CO2 
        if response[13:14] == 'c':
            ### ID
            ID = response[37:41]
            IDFunc(ID)
            
            #~ print("CO2: ",response[63:69])
            #~ int(int('0x034B', 16))
            CO2 = int(int(response[63:69], 16))
            print("CO2:",CO2)
        
        print("-----")
        
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


ser.close()
