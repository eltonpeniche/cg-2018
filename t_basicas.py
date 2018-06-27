import matplotlib.pyplot as plt
from math import *
from matriz import *
from preenchimento import  *
lista = [[2, 4], [2, 5], [2, 6], [2, 6], [3, 6], [4, 5], [4, 5], [5, 6], [6, 6], [7, 7], [7, 5], \
        [7, 6], [7, 7], [2, 4], [3, 3], [4, 2], [4, 2], [5, 3], [6, 4], [7, 5]]

def escala(objeto, parametro):

    newlista = matriz(objeto)
    escala = matriz([[parametro[0], 0], [0, parametro[1]]])
    newlista = list(newlista * escala)

    for i in range(len(objeto)):
        plt.plot(objeto[i][0], objeto[i][1], 'ro')

    for i in range(len(newlista)):
        plt.plot(newlista[i][0], newlista[i][1], 'rs')

    plt.axis([0, 20, 0, 20])
    plt.grid(1)
    plt.show()
    return newlista


def translacao(objeto, parametro):
    p = matriz(parametro)
    newLista = objeto[:]

    for i in range(len(objeto)):
        newLista[i] = [objeto[i][0] + parametro[0], objeto[i][1] + parametro[1]]

    for i in range(len(objeto)):
        plt.plot(objeto[i][0], objeto[i][1], 'ro')

    for i in range(len(newLista)):
        plt.plot(newLista[i][0], newLista[i][1], 'rs')

    plt.axis([-10, 15, -10, 15])
    plt.grid(1)
    plt.show()
    return newLista


def rotacao(objeto, parametro, origem):
    newObject = []
    #transladando para a origem
    for i in range(len(objeto)):
        newObject.append([objeto[i][0] - origem[0], objeto[i][1] - origem[1]])

    #matriz de rotação
    pa = matriz([[cos(parametro), sin(parametro)],[-sin(parametro),cos(parametro)]])

    newlista = matriz(objeto)
    #rotacionando
    newlista = list(matriz(newObject) * pa)

    #rotacioando pro ponto inicial
    newObject = []
    # transladando para a origem
    for i in range(len(objeto)):
        newObject.append([newlista[i][0] + origem[0], newlista[i][1] + origem[1]])

    #mostrando
    for i in range(len(newlista)):
        plt.plot(objeto[i][0], objeto[i][1], 'bs')
        plt.plot(newObject[i][0], newObject[i][1], 'rs')
    plt.axis([-8, 15, -8, 15])
    plt.grid(1)
    plt.show()






