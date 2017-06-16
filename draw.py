import matplotlib.pyplot as plt
from tkinter import *
import numpy as np

plt.title('CO2 real time')        # give plot a title
plt.xlabel('x axis / Real time')    # make axis labels
plt.ylabel('y axis / ppm' )

plt.axis([0, 10, 0, 2000])          # [x,x,y,y]


#~ filea = open("try.txt", "r")
#~ for lines in filea:  
    #~ print(str(lines[63:67]))
#~ filea.close()

#~ str = "{\"rtn_id\":\"co2_data\",\"nwk_addr\":\"0xFA8F\",\"phy_data\":[{\"co2\":\"0x054D\"}]}"
#~ print(str[63:67])

a = int(int('0x065C', 16))
b = int(int('0x053C', 16))
c = int(int('0x0344', 16))
d = int(int('0x039C', 16))
e = int(int('0x0340', 16))
f = int(int('0x038E', 16))
g = int(int('0x0337', 16))
h = int(int('0x0398', 16))
i = int(int('0x033E', 16))
j = int(int('0x038B', 16))
k = int(int('0x034B', 16))
l = int(int('0x0397', 16))

print(a,b,c,d,e,f,g,h,i,j,k,l)


### data 1 red
### x ---> real time
### y ---> ppm
x1 = [1,2,3,4,5]
y1 = [a,c,e,g,i]

### data 2 green
x2 = [1,2,3,4,5]
y2 = [b,d,f,h,j]

for i in range(5):
    plt.scatter(x1[i], y1[i])
    plt.scatter(x2[i], y2[i])
    
    #~ plt.plot(x1, y1, 'r')               # use pylab to plot x and y
    #~ plt.plot(x2, y2, 'g')
    plt.pause(0.5)

#~ plt.show()                          # show the plot on the screen
while True:
    plt.pause(0.5)
