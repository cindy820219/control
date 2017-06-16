### dmesg > yes.txt
### dmesg > no.txt
### diff yes.txt no.txt
### sudo python3 a.py

import serial
import struct

se = serial.Serial()
se.baudrate = 38400
se.bytesize = 8
se.stopbits = 1
se.port = '/dev/ttyACM0'
se.timeout = 0.5
se.rtscts = 1

# open port
se.open()                       

def IDFunc(ID):
    if ID == 'FB13':
        Sensor = 1
    else:
        Sensor = 2
    print("Sensor: ", Sensor)

while True:
    response = se.readline()
    response = str(response)
    if response != "b''":
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
        
        ### Temp / Hum
        else: 
            ### ID
            ID = response[36:40]
            IDFunc(ID)
            
            
            #~ print("Temp: ",response[63:69])
            #~ print("Hume: ",response[80:86])
            Temp = int(int(response[63:69], 16))
            Hume = int(int(response[80:86], 16))
            print("Temp:",Temp)
            print("Hume:",Hume)
        print("-----")


ser.close()
