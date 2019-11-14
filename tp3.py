# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:42:32 2019

@author: Carlos Lousada
"""
import math
def func(x):
    return -2.75*pow(x,3)+18*pow(x,2)-21*x-12

def func2(x):
    return x-2*math.log(x)-5

def f3(x):
    return pow(2, math.sqrt(x))-10*x+1

def bissecao(f,a,b):
    it = 0
    while abs((a-b)/a) > 5**(-3):
        it+=1
        if f(a) * f((a+b)/2) < 0:
            b = (a+b)/2
        else:
            a = (a+b)/2
      
    return [(a+b)/2,it]


def corda(f,a,b):
    auxa = 0
    auxb = 0
    xn = 0
    i = 0
    while (abs(abs(a-b)-abs(auxa-auxb))) > pow(10,-5):
        i+=1
        xn = (a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(xn)<0:
            auxa = a
            auxb = b
            b = xn
        else:
            auxa = a
            auxb = b
            a = xn
    return [xn,i]
    