# -*_ coding=utf-8 -*-
import numpy  as np 
import matplotlib.pyplot as plt
imput_value=[1,2,3,4,5]
squares = [i*np.random.rand() for i in imput_value]
plt.plot(imput_value,squares,linewidth=5)
plt.title('square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('square of Value',fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()

