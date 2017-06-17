import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.title('CO2 1')        # give plot a title
#~ plt.xlabel('Real time')    # make axis labels
plt.ylabel('ppm' )

ax2 = fig.add_subplot(212)
plt.title('CO2 2')        # give plot a title
plt.xlabel('Real time')    # make axis labels
plt.ylabel('ppm' )

def animate(i):
    graph_data1 = open('note1.txt','r').read()
    lines = graph_data1.split('\n')
    x1 = []
    y1 = []
    for line in lines:
        if len(line) > 1:
            line_1, time_1, y_1 = line.split(',')
            x1.append(line_1)
            y1.append(y_1)
            ax1.text(line_1, y_1, time_1+'\n'+y_1)

    graph_data2 = open('note2.txt','r').read()
    lines = graph_data2.split('\n')
    x2 = []
    y2 = []
    for line in lines:
        if len(line) > 1:
            line_2, time_2, y_2 = line.split(',')
            x2.append(line_2)
            y2.append(y_2)
            ax2.text(line_2, y_2, time_2+'\n'+y_2)
            
    #~ ax1.clear()
    ax1.plot(x1, y1)
    #~ ax2.clear()
    ax2.plot(x2, y2)
    
    #~ plt.xlabel('x axis / Real time')    # make axis labels
    #~ plt.ylabel('y axis / ppm' )
    #~ plt.title('CO2 real time')        # give plot a title


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
