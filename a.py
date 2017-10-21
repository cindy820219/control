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

### Member 
'''
#01  8F43 ; #02  C713 ; #03  D44E ; #04  D334 ; #05  9B34 ; 
#06  E41E ; #07  B414 ; #08  630E ; #09  4056 ; #10  3C2D ; 
#11   ; #12   ; #13   ; #14   ; #15   ;
#16   ; #17   ; #18   ; #19   ; #20   ;
#21   ; #22   ; #23   ; #24   ; #25   ;
#26   ; #27   ; #28   ; #29   ; #30   ; 
''' 

dict = {'0000':'1' , '0001':'2' , '1A86':'3' , '6F76':'4' , '4697':'5', \
        '4726':'6' , '174A':'7' , '3C63':'8' , 'C59F':'9' , 'C83F':'10', \
        '635B':'11' , '281B':'12' , 'C418':'13' , '2762':'14' , '81BD':'15', \
        '56EC':'16' , 'AEEF':'17'}

### port
se = serial.Serial()
se.baudrate = 38400
se.bytesize = 8
se.stopbits = 1
se.port = '/dev/ttyACM0'
#~ se.port = '/dev/ttyUSB0'
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
        Day = time.strftime("%b%d")
        #~ print(Day)
        response = str(response)

        ### CO2 
        if response[13:14] == 'c':
            ### ID
            ID = response[37:41]
            Sensor = dict[ID]
            
            if Sensor == '14':
                print('------------------------------')
            
            if Sensor == '14':
                Count = Count + 1

            #~ print("CO2: ",response[63:69])
            #~ int(int('0x034B', 16))
            CO2 = int(int(response[63:69], 16))

            if int(CO2) > 60000:
                CO2 = str(int(CO2) - 65536)
                
            print( NOTE + str(Count), "Sensor:", Sensor, ",  Time:", tm, "; CO2:", CO2)
                
            Str_note = '_CO2_'
            Str_txt = '.txt'
            
            f = open( Day+Str_note + Sensor + Str_txt, 'a')
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
