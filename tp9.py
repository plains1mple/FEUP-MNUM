# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:50:21 2019

@author: Carlos Lousada
"""
import math

def func(x,y):
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

print(RK4(func, 0, 1, 0, 1))