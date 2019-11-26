# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:04:26 2019

@author: Carlos Lousada
"""

def f1(x2,x3):
    return x2/8 - x3/4 + 20/8

def f2(x1, x3):
    return -3*x1+7*x3+34

def f3(x1, x2):
    return 2*x1-6*x2+38

#updated Gauss-Jacobi code

def gaussJacobi(f1, f2, f3, x1 = 0, x2 = 0, x3 = 0):
    counter = 0
    x1g = x1
    x2g = x2
    x3g = x3
    while True:
        counter +=1
        x1 = x1g
        x2 = x2g
        x3 = x3g
        x1g = f1(x2,x3)
        x2g = f2(x1,x3)
        x3g = f3(x1,x2)
        if(abs(x1g-x1) < pow(10,-3) and abs(x2g - x2) < pow(10,-3) and abs(x3g-x3) < pow(10,-3)):
            break
        else:
            if str(x1g) == "inf" or str(x1g) == "-inf" or str(x2g) == "inf" or str(x2g) == "-inf" or str(x3g) == "inf" or str(x3g) =="-inf":
                return "Infinite values reached. Does not converge, infinite Loop"
    return ["x1: " + str(x1g), "x2: " + str(x2g), "x3: " + str(x3g), "Iterations: " + str(counter)]

#print(gaussJacobi(f1,f2,f3))

#updated Gauss Seidel code

def gaussSeidel(f1,f2,f3, x1 = 0, x2 = 0, x3 = 0):
    counter = 0
    x1g = x1
    x2g = x2
    x3g = x3
    while True:
        counter +=1
        x1 = x1g
        x2 = x2g
        x3 = x3g
        x1g = f1(x2,x3)
        x2g = f2(x1g,x3)
        x3g = f3(x1g,x2g)
        if(abs(x1g-x1) < pow(10,-3) and abs(x2g - x2) < pow(10,-3) and abs(x3g-x3) < pow(10,-3)):
            break
        else:
            if str(x1g) == "inf" or str(x1g) == "-inf" or str(x2g) == "inf" or str(x2g) == "-inf" or str(x3g) == "inf" or str(x3g) =="-inf":
                return "Infinite values reached. Does not converge, infinite Loop"
    return ["x1: " + str(x1g), "x2: " + str(x2g), "x3: " + str(x3g), "Iterations: " + str(counter)]
    
    
print(gaussSeidel(f1,f2,f3))

import math

def function(x):
    return math.sin(x) / x**2

#updated integrateTrapezio

def integrateTrapezio(f1, a, b, n):
    result = f1(a)
    h = (b-a)/n
    for i in range(1,n+1):
        result += 2*f1(a+i*h)
    return result*h/2


#updated integrateSimpson

def integrateSimpson(f1, a, b, n):
    result = f1(a)+f1(b)
    h = (b-a)/n
    for i in range(1, n+1):
        if(i%2 == 0):
            result += 2*f1(a+i*h)
        else:
            result += 4*f1(a+i*h)
    return result*h/3
