# -*- coding=utf-8 -*-
import numpy  as np 
import math
import matplotlib.pyplot as plt

theta = np.linspace(0,1,500);
x = np.exp(theta)*np.sin(100*theta);
y = np.exp(theta)*np.cos(100*theta);
#sz = np.linspace(1,100,200);
plt.scatter(x,y)
plt.show()

