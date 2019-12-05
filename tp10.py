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
        return x3
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
        return x3

print(aurea(f1, -1, 0, "min"))