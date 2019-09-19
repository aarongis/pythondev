# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def update_position(num, data, plts):
    x1, y1, n = data
    theta = np.arange(2* num *np.pi,2* (num+1)*n*np.pi,np.pi/50)
    x2=x1[num]+1/n * np.cos(theta * n)
    y2=y1[num]+1/n * np.sin(theta * n)
    circular, scatter = plts
    x3, y3 =scatter.get_data()
    x3, y3 =np.asarray(x3),np.asarray(y3)
    x3, y3 =np.append(x3, [x2[-num]]),np.append(y3,[y2[-num]])
    scatter.set_data(x3,y3)
    return circular,scatter

fig=plt.figure(figsize=(8,8))
plt.ylim([-1.5,1.5])
plt.xlim([-1.5,1.5])
plt.grid(True)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

n=3
theta = np.arange(0,2*np.pi, np.pi/50)
x0=(n+1)/n * np.cos(theta)
y0=(n+1)/n * np.sin(theta)

plt.plot(x0,y0)

x1= np.cos(theta)
y1= np.sin(theta)

plt.plot(x1,y1,'--')
data=[x1,y1,n]
ani = animation.FuncAnimation(fig,update_position,50,data,plt)

plt.show()