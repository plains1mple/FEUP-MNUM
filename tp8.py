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

#apenas para funcoes divididas em 4 malhas
def int_dupla_Simpson(f,a0,b0,af,bf):
    result = 0
    hx = (af-a0)/2
    hy = (bf-b0)/2
    h = hx*hy/9
    for x in [a0,(af-a0)/2,af]:
        for y in [b0,(bf-b0)/2,bf]:
            if x == ((af-a0)/2) and y == ((bf-b0)/2):
                result += pow(4,2)*f(x, y)
            elif (x == a0 and y != (bf-b0)/2) or (x == af and y != (af-a0)/2):
                result += f(x,y)
            else:
                result += 4*f(x,y)
    return result*h

#print(int_dupla_Simpson(f,0,0,0.5,0.5))

#apenas para funcoes divididas em 4 malhas
def int_dupla_Trapezio(f,a0,b0,af,bf):
    result = 0
    hx = (af-a0)/2
    hy = (bf-b0)/2
    h = hx*hy/4
    for x in [a0,(af-a0)/2,af]:
        for y in [b0,(bf-b0)/2,bf]:
            if x == ((af-a0)/2) and y == ((bf-b0)/2):
                result += 4*f(x, y)
            elif (x == a0 and y != (bf-b0)/2) or (x == af and y != (af-a0)/2):
                result += f(x,y)
            else:
                result += 2*f(x,y)
    return result*h

#print(int_dupla_Trapezio(f,0,0,0.5,0.5))

#not working
def Euler(f, a, b, h):
    x = a
    y = f(a,a)
    while (x < b):
        x+=h
        y+= f(x,y)*h
    return y


#print(Euler(f1,0,1.4,0.1))