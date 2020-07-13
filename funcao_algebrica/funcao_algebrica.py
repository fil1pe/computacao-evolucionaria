# -*- coding: utf-8 -*-
from pprint import pprint
from random import uniform, random, randint
from math import cos

def leitura():
    global tam_populacao, tam_cromossomo, Li, Ui, L
    f = open('entrada.txt', 'r')
    linhas = f.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].split("\n")[0]

    tam_populacao = (int)(linhas[0].split("=")[1])
    tam_cromossomo = (int)(linhas[1].split("=")[1])
    Li = (int)((linhas[2].split("=")[1]).split(",")[0].split("[")[1])
    Ui = (int)((linhas[2].split("=")[1]).split(",")[1].split("]")[0])
    L = tam_cromossomo

def lista_string(l):
    return ''.join(map(str, l))

def mapeia_d_x(d):
    return Li + float(Ui - Li)/float(2**L - 1)*d

def converte_bin_dec(lista_bin):
    return int(lista_string(lista_bin),2)
    
def populacao_inicial():
    populacao = []
    for i in range(tam_populacao):
        cromossomo = []
        for j in range(tam_cromossomo):
            cromossomo.append(randint(0,1))
        populacao.append(cromossomo)
    return populacao
        
def fitness_maximizacao(individuo):
    decimal = converte_bin_dec(individuo)
    x = mapeia_d_x(decimal)
    return cos(20*x) - abs(x)/2 + x*x*x/4.0


def fitness_minimizacao(individuo):
    return fitness_maximizacao(individuo)*-1

if __name__ == "__main__":
    leitura()

    populacao = populacao_inicial()

    populacao.sort(key=fitness_minimizacao)
    minimo = populacao[-1]

    print('População:')
    pprint([lista_string(x) for x in populacao])

    print('\nMinimização:')
    print('Indivíduo:')
    print('- Binário: ' + str(lista_string(minimo)))
    print('- Decimal: ' + str(converte_bin_dec(lista_string(minimo))))
    print('- X: ' + str(mapeia_d_x(converte_bin_dec(lista_string(minimo)))))
    print('Fitness: ' + str(fitness_minimizacao(minimo))) 

    populacao.sort(key=fitness_maximizacao)
    maximo = populacao[-1]

    print('\nMaximização:')
    print('Indivíduo:')
    print('- Binário: ' + str(lista_string(maximo)))
    print('- Decimal: ' + str(converte_bin_dec(lista_string(maximo))))
    print('- X: ' + str(mapeia_d_x(converte_bin_dec(lista_string(maximo)))))
    print('Fitness: ' + str(fitness_maximizacao(maximo)))