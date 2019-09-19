# _*_ coding:utf-8 _*_
'''
Created on 2019��4��16��

@author: Administrator
'''
from  fibonacci.FFib import FFib 

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

if __name__=='__main__':
    for i in fib(50):
        print(i,end=' ')
    print('\n')
    list1=list(fib(1000))
    print(list1)
    
    for n in FFib(1200):
        print(n,end=' ')