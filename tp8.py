# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:47:34 2019

@author: Carlos Lousada
"""
import math

def f(x,y):
    return math.exp(y-x)

def f1(x,y):
    return pow(x,2)+pow(y,2)

def int_dupla_trapezio(f, a0, af, b0, bf, n):
    hx = (af-a0)/n
    hy = (bf-b0)/n
    result = f(a0, b0) + f(a0, bf) + f(af, b0) + f(af, bf)
    for i in range (1, n):
        result += 2* (f(a0, b0 + hy*i) + f(af, b0 + hy*i))
        result += 2* (f(a0 + hx*i, b0) + f(a0 + hx*i, bf))
        for j in range(1, n):
            result += 4* f(a0 + hx*i, b0+hy*j)
    result *= ((hx*hy)/4)
    return result

print(int_dupla_trapezio(f, -4, 4, -4, 4, 2))

#not sure if working or not

def int_dupla_simpson(f, a0, af, b0, bf, n):
    hx = (af-a0)/2
    hy = (bf-b0)/2
    result = f(a0, b0) + f(a0, bf) + f(af, b0) + f(af, bf)
    for i in range (1, n):
        result += 4* (f(a0, b0 + hy*i) + f(af, b0 + hy*i))
        result += 4* (f(a0 + hx*i, b0) + f(a0 + hx*i, bf))
        for j in range(1, n):
            result += 16* f(a0 + hx*i, b0+hy*j)
    result *= ((hx*hy)/9)
    return result


def Euler(f,x0,y0,xf,h):
    xn = x0
    yn = y0
    xn += h
    yn += h*f(x0,y0)
    while (xn<xf):
        y0 = yn
        x0 = xn
        xn += h
        yn += h*f(x0,y0)
    return yn


def RK2(x0,xf,y0,h,f):
    xn = x0
    yn = y0
    xn = x0 + h
    yn = y0 + h*f(x0+h/2,y0+(h/2)*f(x0,y0))
    while xn < xf:
        x0 = xn
        y0 = yn
        xn = x0 + h
        yn = y0 + h*f(x0+h/2,y0+(h/2)*f(x0,y0))
    return yn

