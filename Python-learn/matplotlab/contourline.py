# -*- encoding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
 
#通过x，y计算高度
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
 
 
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
 
#把x，y绑定成网格的输入值
X,Y = np.meshgrid(x,y)
 
# use plt.contourf to filling contours
#X,Y and value for (X,Y) point
#contour为网格
#8代表分成10部分
#0分成2部分
#plt.cm.cool为冷色调,plt.cm.hot为暖色调,plt.cm.Spectral,plt.cm.hsv,plt.cm.ocean
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.cool)#画上颜色
 
#use plt.contour to add contounlines
#画线,contour为等高线的线
C = plt.contour(X,Y,f(X,Y),8,colors='black',linwidth=.5)
 
#adding label
plt.clabel(C,inline=True,fontsize=10)
 
 
plt.xticks(())
plt.yticks(())
plt.show()
