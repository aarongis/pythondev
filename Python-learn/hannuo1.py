#! /bin/python
# _*_ coding=utf-8 _*_
'''
Created on 2019��4��15��

@author: Administrator
'''
i=0
def hannuo(n, a, b, c):
    global  i
    if(n==1):
        i+=1
        print('move ', i, ' time:', a,'-->', c)
    else:
        hannuo(n-1,a,c,b)
        hannuo(1,a,b,c)
        hannuo(n-1,b,a,c)
    
if __name__ == '__main__':
    hannuo(4,'a','b','c')
