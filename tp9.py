# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:50:21 2019

@author: Carlos Lousada
"""
import math

def func(x,y):
    return math.cos(x)

def f1(x):
    return math.cos(x)

def RK4(f, x0, xf, y0, h):
    yn = y0
    xn = x0
    while(True):
        x0 = xn
        y0 = yn
        xn = x0 + h
        dy1 = h * f(x0,y0)
        dy2 = h * f(x0 + h/2, y0 + dy1/2)
        dy3 = h * f(x0 + h/2, y0 + dy2/2)
        dy4 = h * f(x0 + h, y0 + dy3)
        yn = y0 + (dy1 + dy4)/6 + (dy2 + dy3)/3
        if(xn >= xf):
            break
    return yn

print(RK4(func, 0, 3, 0, 1))

import matplotlib.pyplot as plot

def floatrange(it0, itf, step = 0.1):
    result = []
    while it0 < itf:
        result.append(it0)
        it0+=step
    return result

def drawplot(f, x0, xf, step = 0.1):
    xlist = floatrange(x0, xf, step)
    ylist = []
    for i in xlist:
        ylist.append(f(i))
    plot.plot(xlist, ylist)    
    
#drawplot(f1, -5, 5, 0.01)