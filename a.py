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
import requests


### Member 
'''
#01  8F43 ; #02  C713 ; #03  D44E ; #04  D334 ; #05  9B34 ; 
#06  E41E ; #07  B414 ; #08  630E ; #09  4056 ; #10  3C2D ; 
#11   ; #12   ; #13   ; #14   ; #15   ;
#16   ; #17   ; #18   ; #19   ; #20   ;
#21   ; #22   ; #23   ; #24   ; #25   ;
#26   ; #27   ; #28   ; #29   ; #30   ; 
''' 

dict = {'3B3B':'8' , '3ED9':'11' , '8AC2':'12', '1DCA':'14' , 'D6DC':'15', \
        '62C7':'13' , '7AC2':'18' , '2DDB':'17' , '6292':'23' , '7F2F':'22', \
        'BDF6':'5' , '96E6':'24', '61A0':'20','8683':'19', 'AB0D':'1', \
        }

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
Count = 1

NOTE = '#'
NOTE1 = '*'
CO2_new = 0

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
            
                

            if Sensor == '8':
                print('------------------------------')
                Count = Count + 1
            #~ if Sensor == '22':
                

            #~ print("CO2: ",response[63:69])
            #~ int(int('0x034B', 16))
            CO2 = int(int(response[63:69], 16))

            if int(CO2) > 60000:
                CO2 = str(int(CO2) - 65536)
            
            if Sensor =='8':
                #~ CO2_new = str(int(int(CO2) * 1.1587))
                CO2_new = str(int(int(CO2) * 1.1987))
            if Sensor =='12':
                CO2_new = str(int(int(CO2) * 1.0598))
            if Sensor =='15':
                CO2_new = str(int(int(CO2) * 1.1121))
            if Sensor =='11':
                CO2_new = str(int(int(CO2) * 1.1011))
            if Sensor =='14':
                CO2_new = str(int(int(CO2) * 1.0051))
            if Sensor =='5':
                CO2_new = str(int(int(CO2) * 1.0103))
            if Sensor =='20':
                CO2_new = str(int(int(CO2) * 1.0047))
            if Sensor =='19':
                CO2_new = str(int(int(CO2) * 1.0889))
            
            
            if Sensor =='21':
                CO2_new = str(int(int(CO2) * 1.0321))
            if Sensor =='23':
                CO2_new = str(int(int(CO2) * 1.0158))
            if Sensor =='13':
                CO2_new = str(int(int(CO2) * 1.1121))
            if Sensor =='18':
                CO2_new = str(int(int(CO2) * 1.1317))
            if Sensor =='17':
                CO2_new = str(int(int(CO2) * 1.2302))
            if Sensor =='22':
                CO2_new = str(int(int(CO2) * 1.0184))
            if Sensor =='24':
                #~ CO2_new = str(int(int(CO2) * 1.0069))
                CO2_new = str(int(int(CO2) * 0.818))
            
            #~ if Sensor =='12' or Sensor =='24':
                #~ print( NOTE + str(Count), "Sensor:", Sensor, ",  Time:", tm, "; Old-CO2:", CO2 , "; New-CO2:", CO2_new )
            
            print( NOTE + str(Count), "Sensor:", Sensor, ",  Time:", tm, "; Old-CO2:", CO2 , "; New-CO2:", CO2_new )
                
            Str_note = '_CO2_'
            Str_txt = '.txt'
            
            url = 'http://206.189.86.183:8000/pd?'
            url += 'id=' + Sensor
            url += '&type=co2'
            url += '&value=' + str(CO2)
            r = requests.get(url)
            print(r.url)
            print(r.text)
            
            f = open( Day+Str_note + Sensor + Str_txt, 'a')
            f.write(str(Count)+ ',' + str(tm) + ',' + str(CO2_new) + '\n') 

            f = open( Day+Str_note + Sensor + '_old' + Str_txt , 'a')
            f.write(str(Count)+ ',' + str(tm) + ',' + str(CO2) + '\n') 
            
            f.close()

        else:
            #~ ### Temp / Hum
            if response[13:14] == 't':
                ### ID
                ID = response[36:40]
                Sensor = dict[ID]

                Temp = int(int(response[63:69], 16))
                Hume = int(int(response[80:86], 16))
                
                Str_note = 'TH_'
                Str_txt = '.txt'
                
                #~ if Sensor =='23':
                    #~ print(NOTE1 + str(Count), "Sensor:", Sensor, ",  Time:", tm, "; Temp:", Temp, ", Hume:", Hume)
                
                print("         ", "Sensor:", Sensor, ",  Time:", tm, "; Temp:", Temp, ", Hume:", Hume)
                
                url = 'http://206.189.86.183:8000/pd?'
                url += 'id=' + Sensor
                url += '&type=hum'
                url += '&value=' + str(Hume)
                r = requests.get(url)
                print(r.url)
                print(r.text)

                url = 'http://206.189.86.183:8000/pd?'
                url += 'id=' + Sensor
                url += '&type=temp'
                url += '&value=' + str(Temp)
                r = requests.get(url)
                print(r.url)
                print(r.text)

                
                f = open( Str_note + Sensor + Str_txt, 'a')
                f.write(str(Count)+ ',' + str(tm) + ',' + str(Temp) + ',' + str(Hume) + '\n') 



                f.close()

