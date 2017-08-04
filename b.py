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

CO2_x1 = 0
CO2_x2 = 0

TH_x1 = 0
TH_x2 = 0

while True:
    response = se.readline()
    if response != "b''":
        tm = time.strftime("%H:%M:%S")
        Day = time.strftime("%D")
        response = str(response)
        print(response)
