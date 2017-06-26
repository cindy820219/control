import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import matplotlib.animation as animation
import os

plt.rc('ytick', labelsize=15)
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.title('CO2 Conc.', fontsize=30)        # give plot a title
plt.ylabel('CO2 Concentration (ppm)' , fontsize=20)
plt.xlabel('Time', fontsize=20)    # make axis labels

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
            
    ### x label to time !
    plt.xticks(list_k)
    #~ print(time1)
    
    ### draw the view
    ##~ ax1.clear()
    ax1.plot(x1, y1, "r--")
    ax1.plot(x2, y2, "g")
    ax1.set_xticklabels(time1,rotation='vertical',fontsize=15)
  
    #~ ax1.plot(x1[-10:], y1[-10:], "r--")
    #~ ax1.plot(x2[-10:], y2[-10:], "g")
    #~ ax1.set_xticklabels(time1[-10:],rotation='vertical',fontsize=15)


'''
1. animation
2. line !
3. show 
'''
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.grid(True)  
plt.show()
