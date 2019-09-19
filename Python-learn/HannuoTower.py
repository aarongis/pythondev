#!/bin/python
# _*_ coding:utf-8 _*_
'''
Created on 2019��4��15��

@author: Administrator
'''
#----------------汉诺塔-----------------#
# 如果有n个圆盘,所需移动的步数为 2^n-1
i = 0
# 定义一个函数给4个参数n是圆盘的个数,a代表A柱子,b,c 函数里面的是形式参数
def move(n,a,b,c):
    # 把变量i全局化,如果不全局化,只可访问读取不能进行操作修改
    global i
    if n==1:
        i += 1
        print('移动第',i,'次',a,'-->',c)
    else:
        # 1.把A柱上n-1个圆盘移动到B柱上
        move(n-1,a,c,b) # 传的才是实际参数
        # 2.把A柱上最大的移动到C柱子上
        move(1,a,b,c)
        # 3.把B柱子上n-1个圆盘移动到C柱子上
        move(n-1,b,a,c)

        
move(4,'A','B','C')