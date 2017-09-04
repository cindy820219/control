import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import matplotlib.animation as animation
import os

plt.rc('ytick', labelsize=15)
fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

plt.title('CO2 Conc.', fontsize=30)        # give plot a title
plt.ylabel('CO2 Concentration (ppm)' , fontsize=20)
plt.xlabel('Time', fontsize=20)    # make axis labels


plt.title('PM 2.5')        # give plot a title
plt.xlabel('Time')    # make axis labels
plt.ylabel('PM2.5 (mg/..)' )


'''
#~ ax2 = fig.add_subplot(212)
#~ plt.title('CO2 2')        # give plot a title
#~ plt.xlabel('Real time')    # make axis labels
#~ plt.ylabel('ppm' )
'''

### intitional
list_k = [0,]

for i in range(200):
    list_k.append(i)    
#~ plt.xticks(list_k)

def animate(i):
    time1 = [0,]
    time2 = [0,]
    
    graph_data1 = open('CO2_1.txt','r').read()
    lines = graph_data1.split('\n')
    x1 = []
    y1 = []
    for line in lines:
        if len(line) > 1:
            line_1, time_1, y_1 = line.split(',')
            x1.append(line_1)
            y1.append(y_1)
            
            time1.append(time_1)
            ax1.text(line_1, y_1, y_1,fontsize=20)
            
    
    graph_data2 = open('CO2_2.txt','r').read()
    lines = graph_data2.split('\n')
    x2 = []
    y2 = []
    for line in lines:
        if len(line) > 1:
            line_2, time_2, y_2 = line.split(',')
            x2.append(line_2)
            y2.append(y_2)
            #~ time1.append(time_1)
            ax1.text(line_2, y_2, y_2, fontsize=20)
            
    #~ ### x label to time !
    #~ plt.xticks(list_k)
    #~ ##~ print(time1)
    
    #~ ### draw the view
    #~ ##~ ax1.clear()
    #~ ax1.plot(x1, y1, "r--")
    #~ ax1.plot(x2, y2, "g")
    #~ ax1.set_xticklabels(time1,rotation='vertical',fontsize=15)
  
    #~ ax1.plot(x1[-10:], y1[-10:], "r--")
    #~ ax1.plot(x2[-10:], y2[-10:], "g")
    #~ ax1.set_xticklabels(time1[-10:],rotation='vertical',fontsize=15)

    #~ ----------------------------------------------------------------
    #~ 01
    graph_data01 = open('PM_1.txt','r').read()
    lines = graph_data01.split('\n')
    x01 = []
    y01 = []
    for line in lines:
        if len(line) > 1:
            line_01, time_01, y_01 = line.split(',')
            x01.append(line_01)
            y01.append(y_01)
            ax2.text(line_01, y_01, y_01, fontsize=20)
            
    #~ 02
    graph_data02 = open('PM_2.txt','r').read()
    lines = graph_data02.split('\n')
    x02 = []
    y02 = []
    for line in lines:
        if len(line) > 1:
            line_02, time_02, y_02 = line.split(',')
            x02.append(line_02)
            y02.append(y_02)
            ax2.text(line_02, y_02, y_02, fontsize=20)

    #~ 03
    graph_data03 = open('PM_3.txt','r').read()
    lines = graph_data02.split('\n')
    x03 = []
    y03 = []
    for line in lines:
        if len(line) > 1:
            line_03, time_03, y_03 = line.split(',')
            x03.append(line_03)
            y03.append(y_03)
            ax2.text(line_03, y_03, y_03, fontsize=20)



    
    
    
    ### x label to time !
    plt.xticks(list_k)
    #~ print(time1)
    
    ### draw the view
    ##~ ax1.clear()
    ax1.plot(x1, y1, "r--")
    ax1.plot(x2, y2, "g")
    ax1.set_xticklabels(time1,rotation='vertical',fontsize=15)
    
    ax2.plot(x01, y01, "r--")
    ax2.plot(x02, y02, "g")
    ax3.plot(x03, y03, "b")
    ax4.plot(x04, y04, "y")
    ax5.plot(x05, y05, "g^")
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
