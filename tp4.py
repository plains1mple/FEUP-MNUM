# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:43:11 2019

@author: Carlos Lousada
"""

def f(x):
    return 2*pow(x,2)-5*x-2

def fpiano(x):
    #if(x<-8 or x>8):
    return 5/2 + 1/x
    #return (2*(pow(x,2))-2)/5

def fp(x):
    return 4*x-5

def newton(f,fp,guess):
    xn = guess
    for i in range(0, 21):
        xn = xn - (f(guess)/fp(guess))
        if abs(xn-guess) < pow(10, -5):
            return [xn,i]
        guess = xn
    return "Range too small"


def picardpeano(f, guess):
    for i in range(0, 21):
        xn = f(guess)
        if (abs(xn - guess)) < pow(10,-5):
            return [xn,i]
        guess = xn
    return "Range too small"

#print(newton(f,fp,2))
#print(picardpeano(fpiano, 8))