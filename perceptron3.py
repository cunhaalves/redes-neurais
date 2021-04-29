# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:42:15 2017

@author: luiz
"""

import numpy as np

#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,0,0,1])
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,1,1,1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1


def stepFuntion(soma):
    if(soma>=1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFuntion(s)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.array(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i,j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))
        
treinar()

print('Rede treinada')

print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
