# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:41:00 2019

@author: Carlos Lousada
"""

#codigo encontrado na net
#def eliminacao(a, b):
#  n = len(a)
#  for k in range(0, n-1):
#    for i in range(k+1, n):
#      x = a[i*n+k] / a[k*n+k]
#      for j in range(k, n):
#        a[i*n+j] = a[i*n+j] - x * a[k*n+j]
#      b[i] = b[i] - x * b[k]
#  return(b, a)
#
#a = [[2,-1,2],[1,-2,1],[3,-1,2]]
#b = [0,6,11]
#print(eliminacao(a,b))

def fazerlistas(A):
    aux = [0 for i in range(len(A))]
    return [aux for i in range(len(A[0]))]

# metodo de khaletsky por testar, possivelmente ainda tem erros em indexs, etc.

def khaletsky(A,b):
    L = fazerlistas(A);
    U = fazerlistas(A);
    for i in range(len(A)):
        L[i][0] = (A[i][0])
    for i in range(len(A)):
        U[0][i] = A[0][i] / L[0][0]
    for i in range(1,len(A)+1):
        for j in range(1,len(A[0])+1):
            value1 = 0
            value2 = 0
            for l in range(1,i):
                value2 += L[i][l]*U[l][j]
            U[i-1][j-1] = 1/L[i-1][i-1] * (A[i-1][j-1]-value2)
            for k in range(1,j):
                value1 += (L[i-1][k-1]*U[k-1][j-1])
            L[i-1][j-1] = A[i-1][j-1] - value1
    return (L,U)
            