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

def gaussJacobi(f1, f2, f3):
    x1guess = 0
    x2guess = 0
    x3guess = 0
    #for i in range(11):
    while abs(f1(x2guess,x3guess)-x1guess) > pow(10,-3) or abs(f2(x1guess,x3guess)-x2guess) > pow(10,-3) or abs(f3(x1guess,x2guess)-x3guess) > pow(10,-3):
        x1guess = f1(x2guess,x3guess)
        x2guess = f2(x1guess,x3guess)
        x3guess = f3(x1guess,x2guess)
#        print(x1guess, x2guess, x3guess)
    x1guess = f1(x2guess,x3guess)
    x2guess = f2(x1guess,x3guess)
    x3guess = f3(x1guess,x2guess) 
    return ["x1: " + str(x1guess), "x2: " + str(x2guess), "x3: " + str(x3guess)]

#print(gaussJacobi(f1,f2,f3))

def gaussSeidel(f1,f2,f3):
    x1guess = 0
    x2guess = 0
    x3guess = 0
    while abs(f1(x2guess,x3guess)-x1guess) > pow(10,-3) or abs(f2(x1guess,x3guess)-x2guess) > pow(10,-3) or abs(f3(x1guess,x2guess)-x3guess) > pow(10,-3):
        x1guess = f1(x2guess,x3guess)
        x2guess = f2(f1(x2guess,x3guess),x3guess)
        x3guess = f3(f1(x2guess,x3guess),f2(x1guess,x3guess))
    x1guess = f1(x2guess,x3guess)
    x2guess = f2(f1(x2guess,x3guess),x3guess)
    x3guess = f3(f1(x2guess,x3guess),f2(x1guess,x3guess))
    return ["x1: " + str(x1guess), "x2: " + str(x2guess), "x3: " + str(x3guess)]
    
    
print(gaussSeidel(f1,f2,f3))

#import math
#
#def function(x):
#    return math.sin(x) / x**2
#
#def integrateTrapezio(f1, a, b, n):
#    result = f1(a)
#    h = (b-a)/n
#    for i in range(1,n+1):
#        result += 2*f1(a+i*h)
#    return result*h/2
#
##print(integrateTrapezio(function, math.pi/2, math.pi, 4))
#
#def integrateSimpson(f1, a, b, n):
#    result = f1(a)+f1(b)
#    h = (b-a)/n
#    for i in range(1, n+1):
#        if(i%2 == 0):
#            result += 2*f1(a+i*h)
#        else:
#            result += 4*f1(a+i*h)
#    return result*h/3
#    
##print(integrateSimpson(function, math.pi/2, math.pi, 4))