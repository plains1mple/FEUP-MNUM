# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:02:56 2019

@author: Carlos Lousada
"""

def newton_nao_linear(x_guess, y_guess, f1, f2, f1_derivada_x, f1_derivada_y, f2_derivada_x, f2_derivada_y):
    counter = 0
    xn = x_guess
    yn = y_guess
    xn = x_guess - (f1(x_guess,y_guess)*f2_derivada_y(x_guess,y_guess)-f2(x_guess,y_guess)*f1_derivada_y(x_guess,y_guess))/(f1_derivada_x(x_guess,y_guess)*f2_derivada_y(x_guess,y_guess)-f2_derivada_x(x_guess,y_guess)*f1_derivada_y(x_guess,y_guess))
    yn = y_guess - (f2(x_guess,y_guess)*f1_derivada_x(x_guess,y_guess)-f1(x_guess,y_guess)*f2_derivada_x(x_guess,y_guess))/(f1_derivada_x(x_guess,y_guess)*f2_derivada_y(x_guess,y_guess)-f2_derivada_x(x_guess,y_guess)*f1_derivada_y(x_guess,y_guess))
    counter += 1
    print([xn,yn])
    while (abs((xn - x_guess)/xn) > 5*10**(-3) and abs((yn - y_guess)/yn) > 5*10**(-3)):
        x_guess = xn
        y_guess = yn
        xn = x_guess - (f1(x_guess,y_guess)*f2_derivada_y(x_guess,y_guess)-f2(x_guess,y_guess)*f1_derivada_y(x_guess,y_guess))/(f1_derivada_x(x_guess,y_guess)*f2_derivada_y(x_guess,y_guess)-f2_derivada_x(x_guess,y_guess)*f1_derivada_y(x_guess,y_guess))
        yn = y_guess - (f2(x_guess,y_guess)*f1_derivada_x(x_guess,y_guess)-f1(x_guess,y_guess)*f2_derivada_x(x_guess,y_guess))/(f1_derivada_x(x_guess,y_guess)*f2_derivada_y(x_guess,y_guess)-f2_derivada_x(x_guess,y_guess)*f1_derivada_y(x_guess,y_guess))
        counter += 1
        print([xn,yn])
    return [xn,yn,counter]


def picard_peano_nao_linear(x_guess,y_guess, g1, g2):
    counter = 1
    xn = g1(x_guess, y_guess);
    yn = g2(x_guess, y_guess);
    #print(xn,yn,counter)
    while (( abs( xn - x_guess ) > 10**(-3) and abs( yn - y_guess ) > 10**(-3) )):
        x_guess = xn;
        y_guess = yn;
        xn = g1(x_guess, y_guess);
        yn = g2(x_guess, y_guess);
        counter += 1
        #print(xn,yn,counter)
    return [xn,yn,counter]


# ez solve com o numpy

#import numpy as np
#matrix = [[3,-1,2],[1,1,1],[2,0,1]]
#sols = [-1,8,5]
#x = (np.linalg.solve(matrix,sols))
#newx = [i for i in x]
#print(newx)

