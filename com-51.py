import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import matplotlib.animation as animation
import os

plt.rc('ytick', labelsize=15)
fig = plt.figure()

#~ ax1 = fig.add_subplot(2,1,1)
#~ plt.title('CO2 Conc.', fontsize=20)        # give plot a title
#~ plt.ylabel('CO2 Concentration (ppm)' , fontsize=15)
#~ plt.xlabel('Time', fontsize=20)    # make axis labels

ax2 = fig.add_subplot(1,1,1)
plt.title('CO2 Conc.', fontsize=20)        # give plot a title
plt.ylabel('CO2 Concentration (ppm)' , fontsize=15)
plt.xlabel('Time', fontsize=20)    # make axis labels


### intitional
list_k = [0,]

for i in range(200):
    list_k.append(i)    
##~ plt.xticks(list_k)

def animate(i):
    time1 = [0,]
    time2 = [0,]
        
    #~ ----------------------------------------------------------------
    #~ 01
    graph_data01 = open('Jan1_CO2_8.txt','r').read()
    lines = graph_data01.split('\n')
    x01 = []
    y01 = []
    for line in lines:
        if len(line) > 1:
            line_01, time_01, y_01 = line.split(',')
            x01.append(line_01)
            y01.append(y_01)
            ax2.text(line_01, y_01, y_01, fontsize=10)
            
    #~ 02
    graph_data02 = open('Jan11_CO2_11.txt','r').read()
    lines = graph_data02.split('\n')
    x02 = []
    y02 = []
    for line in lines:
        if len(line) > 1:
            line_02, time_02, y_02 = line.split(',')
            x02.append(line_02)
            y02.append(y_02)
            ax2.text(line_02, y_02, y_02, fontsize=10)

    #~ 03
    graph_data03 = open('Jan11_CO2_12.txt','r').read()
    lines = graph_data03.split('\n')
    x03 = []
    y03 = []
    for line in lines:
        if len(line) > 1:
            line_03, time_03, y_03 = line.split(',')
            x03.append(line_03)
            y03.append(y_03)
            ax2.text(line_03, y_03, y_03, fontsize=10)
            
    #~ 04
    graph_data04 = open('Jan11_CO2_14.txt','r').read()
    lines = graph_data04.split('\n')
    x04 = []
    y04 = []
    for line in lines:
        if len(line) > 1:
            line_04, time_04, y_04 = line.split(',')
            x04.append(line_04)
            y04.append(y_04)
            ax2.text(line_04, y_04, y_04, fontsize=10)

    #~ 05
    graph_data04 = open('Jan11_CO2_15.txt','r').read()
    lines = graph_data04.split('\n')
    x05 = []
    y05 = []
    for line in lines:
        if len(line) > 1:
            line_05, time_05, y_05 = line.split(',')
            x05.append(line_05)
            y05.append(y_05)
            ax2.text(line_05, y_05, y_05, fontsize=10)
    
    ### x label to time !
    plt.xticks(list_k)
    #~ print(time1)
    
    ### draw the view
    ##~ ax1.clear()
    #~ ax1.plot(x1, y1, "g--")
    #~ ax1.plot(x2, y2, "r")
    #~ ax1.set_xticklabels(time1,rotation='vertical',fontsize=15)
    
    ax2.plot(x01, y01, "r--")
    ax2.plot(x02, y02, "g")
    ax2.plot(x03, y03, "b")
    ax2.plot(x04, y04, "y")
    ax2.plot(x05, y05, "black")
    ax2.set_xticklabels(time1,rotation='vertical',fontsize=15)
    #~ ----------------------------------------------------------------


'''
1. animation
2. line !
3. show 
'''
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.grid(True)  
plt.show()
