# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:33:18 2017

@author: luiz
"""
import numpy as np

entradas = np.array([1,7,5])
pesos = np.array([0.8,0.1,0])

def soma(e, p):
   return e.dot(p)

s=soma(entradas, pesos)

def stepFuntion(soma):
    if(soma>=1):
        return 1
    return 0

r=stepFuntion(s)
    