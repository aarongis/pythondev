# _*_ coding:utf-8 _*_
'''
Created on 2019��4��16��

@author: Administrator
'''
class FFib:
    '''
    classdocs
    '''


    def __init__(self, max):
        '''
        Constructor
        '''
        self.max=max
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib 