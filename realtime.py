### txt 

#~ import matplotlib.pyplot as plt
#~ import matplotlib.animation as animation
#~ import time

#~ fig = plt.figure()
#~ ax1 = fig.add_subplot(1,1,1)

#~ def animate(i):
    #~ pullData = open("try.txt","r").read()
    #~ dataArray = pullData.split('\n')
    #~ xar = []
    #~ yar = []
    #~ for eachLine in dataArray:
        #~ if len(eachLine)>1:
            #~ x,y = eachLine.split(',')
            #~ xar.append(int(x))
            #~ yar.append(int(y))
    #~ ax1.clear()
    #~ ax1.plot(xar,yar)
#~ ani = animation.FuncAnimation(fig, animate, interval=1000)
#~ plt.show()


#~ import numpy as np
#~ import matplotlib.pyplot as plt
#~ import matplotlib.animation as animation

#~ plt.axis([0, 100000, 0, 10])
#~ plt.ion()

#~ for i in range(1000):
    #~ y = np.random.random()
    #~ plt.scatter(i, y)
    #~ plt.pause(0.5)

#~ while True:
    #~ plt.pause(0.5)


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("try.txt","r").read()
    dataArray = pullData.split('\n')
    
    xar = []
    yar = []
    
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
