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

se.open()                       # open ;port

while True:
  response = se.readline()
  print(str(response))
ser.close()


'''
def reader():
    while(True):
        try:
            se.open()                       # open ;port
            
            #~ print(se.portstr)            # confirm which port was really used
                
            #se.write(85)                   # send command string to meter
            bytes=struct.unpack("i", struct.pack('i',0x55)) #0x55  85
            #~ print("bytes: ", bytes)
            #~ se.write(bytes)
            
            #data = se.readline()           # read data from meter 
            data = se.read(5)               # read data from meter 

            #~ print(list(data))            # 10進制
            #~ print(hex(data[0]))          # 轉16進制
            #~ print(len(data))             # 長度
            
            if len(data)>1:
                print()
                print()
                print()

                #~ 16 [0x7b 0x22 0x72 0x74 0x6e]
                #~ 10 [123, 34, 114, 116, 110]
                
                print("d:", hex(data[0]), hex(data[1]),hex(data[2]),hex(data[3]), hex(data[4]))           # 16進制
                print(list(data))           # 10進制
                print("0:", data)

                #~ while i <= 4:
                    #~ print(hex(data[i]))
                    #~ i += 1
            else:
                #~ print("null")
                a=0
                
        except:
            print("except")
        else:
            #~ print("done!")
            a=0
            
        finally:
            se.close() 
        

reader()
'''
