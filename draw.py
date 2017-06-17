import matplotlib.pyplot as plt
from tkinter import *
import numpy as np

import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

def animate(i):
    graph_data = open('note1.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            line, x, y = line.split(',')
            xs.append(line)
            ys.append(y)
            
    ax1.clear()
    ax1.plot(xs, ys)
    
    graph_data1 = open('note2.txt','r').read()
    lines = graph_data1.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            line, x, y = line.split(',')
            xs.append(line)
            ys.append(y)
            
    ax2.clear()
    ax2.plot(xs, ys)
    
    plt.xlabel('x axis / Real time')    # make axis labels
    plt.ylabel('y axis / ppm' )
    
    plt.title('CO2 real time')        # give plot a title


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
