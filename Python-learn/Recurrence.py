#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2019��4��15��

@author: Administrator
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def tail_fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

if __name__ == '__main__':
    sum=tail_fact(998)
    print(sum)
    print(fact(998))