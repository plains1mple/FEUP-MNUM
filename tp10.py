# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:50:39 2019

@author: Carlos Lousada
"""

import math

def f1(x):
    return pow(2*x+1, 2)-5*math.cos(10*x)

def aurea(f, x1, x2, maxmin):
    if(maxmin)=="max" or (maxmin)=="MAX" or maxmin=="maximo":
        razao = (math.sqrt(5)-1)/2
        x3 = x1 + pow(razao,2)*(x2-x1)
        x4 = x1 + razao*(x2-x1)
        while abs(x2-x1)>pow(10, -3):
            if(f(x3) > f(x4)):
                x2 = x4
                x3 = x1 + pow(razao,2)*(x2-x1)
                x4 = x1 + razao*(x2-x1)
            else:
                x1 = x3
                x3 = x1 + pow(razao,2)*(x2-x1)
                x4 = x1 + razao*(x2-x1)
        return ["x = " + str(x3),"y = " + str(f(x3))]
    else:    
        razao = (math.sqrt(5)-1)/2
        x3 = x1 + pow(razao,2)*(x2-x1)
        x4 = x1 + razao*(x2-x1)
        while abs(x2-x1)>pow(10, -3):
            if(f(x3) < f(x4)):
                x2 = x4
                x3 = x1 + pow(razao,2)*(x2-x1)
                x4 = x1 + razao*(x2-x1)
            else:
                x1 = x3
                x3 = x1 + pow(razao,2)*(x2-x1)
                x4 = x1 + razao*(x2-x1)
        return ["x = " + str(x3),"y = " + str(f(x3))]

#print(aurea(f1, -1, 0, "min"))

def f2(x,y):
    return pow(y,2)-2*x*y-6*y+pow(x,2)*2 + 12

def dfx(x,y):
    return -2*y+ 4*x

def dfy(x,y):
    return 2*y- 2*x- 6

def gradiente(f, dfx, dfy, x, y, h, minmax):
    count = 0
    while(True):
        count +=1
        x0 = x
        y0 = y
        if(minmax == "max" or minmax=="maximo" or minmax=="MAX"):
            x = x0 + h*dfx(x0,y0)
            y = y0 + h*dfy(x0,y0)
            if(f(x,y)>f(x0,y0)):
                h*=2
            elif (f(x,y)<f(x0,y0)):
                h/=2
        else:
            x = x0 - h*dfx(x0,y0)
            y = y0 - h*dfy(x0,y0)
            if(f(x,y)<f(x0,y0)):
                h*=2
            elif(f(x,y)>f(x0,y0)):
                h/=2
        if((abs(x-x0) <= pow(10,-2)) and (abs(y-y0) <= pow(10,-2))):
            break
        if(x > pow(10, 6) or y > pow(10,6)):
            return ("A função tende para infinito, o " + minmax + " é infinito")
    return ["x = " + str(x), "y = " + str(f(x,y)), count]

print(gradiente(f2, dfx, dfy, 1, 1, 1, "min"))