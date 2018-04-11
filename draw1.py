import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import matplotlib.animation as animation
import os

plt.rc('ytick', labelsize=10)
fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)
#~ ax2 = fig.add_subplot(2,1,2)

plt.title('CO2 Conc.', fontsize=20)        # give plot a title
plt.ylabel('CO2 Concentration (ppm)' , fontsize=10)
plt.xlabel('Time', fontsize=1)    # make axis labels

'''
#~ ax2 = fig.add_subplot(212)
#~ plt.title('CO2 2')        # give plot a title
#~ plt.xlabel('Real time')    # make axis labels
#~ plt.ylabel('ppm' )
'''

### intitional
list_k = [0,]

for i in range(700):
    list_k.append(i)    
#~ plt.xticks(list_k)
#~ time1 = [0, 0]
#~ time2 = [0, 0]

def animate(i):
    time1 = [0, 0]
    
    ### Red
    graph_data1 = open('Dec13_CO2_13.txt','r').read()
    lines = graph_data1.split('\n')
    x1 = []
    y1 = []
    for line in lines:
        if len(line) > 1:
            line_1, time_1, y_1 = line.split(',')
            x1.append(line_1)
            y1.append(y_1)
            
            time1.append(time_1)
            ax1.text(line_1, y_1, y_1,fontsize=10)
    
    ### Temp / Hum    
    graph_data1 = open('TH_13.txt','r').read()
    lines = graph_data1.split('\n')
    x4 = []
    y4 = []
    for line in lines:
        if len(line) > 1:
            line_4, time_4, y_4,H_4 = line.split(',')
            x4.append(line_4)
            y4.append(y_4)
            
            #~ time1.append(time_1)
            ax1.text(line_4, y_4, y_4+'°C / '+H_4+'%',fontsize=8)
            
    ### Green
    graph_data2 = open('Dec13_CO2_14.txt','r').read()
    lines = graph_data2.split('\n')
    x2 = []
    y2 = []
    for line in lines:
        if len(line) > 1:
            line_2, time_2, y_2 = line.split(',')
            x2.append(line_2)
            y2.append(y_2)
            #~ time1.append(time_2)
            ax1.text(line_2, y_2, y_2, fontsize=10)
                
    ### black
    graph_data1 = open('Dec13_CO2_15.txt','r').read()
    lines = graph_data1.split('\n')
    x3 = []
    y3 = []
    for line in lines:
        if len(line) > 1:
            line_3, time_3, y_3 = line.split(',')
            x3.append(line_3)
            y3.append(y_3)
            
            #~ time1.append(time_1)
            ax1.text(line_3, y_3, y_3,fontsize=10)        

    ### x label to time !
    plt.xticks(list_k)
    #~ print(time1)
    
    ### draw the view
    ##~ ax1.clear()
    ax1.plot(x1, y1, "r")
    ax1.plot(x2, y2, "g")
    ax1.plot(x3, y3, "b")
    
    ax1.plot(x4, y4, "r--")
    #~ ax1.plot(x5, y5, "g--")
    #~ ax1.plot(x6, y6, "b--")
    
    ax1.set_xticklabels(time1,rotation='vertical',fontsize=10)
  
    #~ ax1.plot(x1[-10:], y1[-10:], "r--")
    #~ ax1.plot(x2[-10:], y2[-10:], "g")
    #~ ax1.set_xticklabels(time1[-10:],rotation='vertical',fontsize=15)


'''
1. animation
2. line !
3. show 
'''
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.grid(True)  
plt.show()
