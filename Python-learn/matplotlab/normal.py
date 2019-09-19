# -*- coding:utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt 
#绘图模块 
import scipy.stats as stats
#该模块包含了所有的统计分析函数 
import matplotlib.style as style 
from IPython.core.display import HTML
#PLOTTING CONFIG 绘图配置
#matplotlib inline
style.use('fivethirtyeight')
plt.rcParams['figure.figsize']=(14,7) 
plt.figure(dpi=100) 
#<matplotlib.figure.Figure at 0x1bd827ec6d8> 
#<matplotlib.figure.Figure at 0x1bd827ec6d8> 
#PDF 概率密度函数 
plt.plot(np.linspace(-4,4,100),stats.norm.pdf(np.linspace(-4,4,100))) 
#从（-4，4）中随机选取100个数，绘制该事件的概率密度函数 
plt.fill_between(np.linspace(-4,4,100),stats.norm.pdf(np.linspace(-4,4,100)),alpha=.15)

plt.plot(np.linspace(-4,4,100),stats.norm.cdf(np.linspace(-4,4,100))) 
#cdf函数表示之前的概率累积的结果，-4处为0，4处为1 ​ 
#LEGEND 图例
plt.text(x=-1.5,y=0.7,s="pdf(normed)",rotation=.65,weight="bold",color="#008fd5") 
plt.text(x=-0.4,y=0.5,s="cdf",rotation=.65,weight="bold",color="#fc4f30")
#Ticks 坐标轴
plt.tick_params(axis="both",which="major",labelsize=18) 
plt.axhline(y=0,color="black",linewidth=1.3,alpha=.7)
plt.show()