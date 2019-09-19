# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 10 
x = np.random.rand(N) 
y = np.random.rand(N) 
x2 = np.random.rand(N) 
y2 = np.random.rand(N) 
area = np.random.rand(N) * 1000 
fig = plt.figure() 
ax = plt.subplot() 
ax.scatter(x, y, s=area, alpha=0.5) 
ax.scatter(x2, y2, s=area, c='green', alpha=0.6) # �ı���ɫ 
plt.show()
