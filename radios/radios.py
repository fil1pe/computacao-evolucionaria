# -*- coding: utf-8 -*-
from pprint import pprint
from random import uniform, random, randint

def leitura():
    global tam_populacao, tam_cromossomo, Li_standard, Ui_standard, Li_luxo, Ui_luxo, L
    f = open('entrada.txt', 'r')
    linhas = f.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].split("\n")[0]

    tam_populacao = (int)(linhas[0].split("=")[1])
    tam_cromossomo = (int)(linhas[1].split("=")[1])
    Li_standard = (int)((linhas[2].split("=")[1]).split(",")[0].split("[")[1])
    Ui_standard = (int)((linhas[2].split("=")[1]).split(",")[1].split("]")[0])
    Li_luxo = (int)((linhas[3].split("=")[1]).split(",")[0].split("[")[1])
    Ui_luxo = (int)((linhas[3].split("=")[1]).split(",")[1].split("]")[0])
    L = tam_cromossomo/2

def mapeia_d_x_standard(d):
    return round(Li_standard + float(Ui_standard - Li_standard)/float(2**L - 1)*d)

def mapeia_d_x_luxo(d):
    return round(Li_luxo + float(Ui_luxo - Li_luxo)/float(2**L - 1)*d)

def lista_string(l):
    return ''.join(map(str, l))

def converte_bin_dec(lista_bin):
    bin_standard = lista_string(lista_bin[:5])
    bin_luxo = lista_string(lista_bin[5:])
    dec_standard = int(bin_standard,2)
    dec_luxo = int(bin_luxo,2)
    return (dec_standard,dec_luxo)

def populacao_inicial():
    populacao = []
    for i in range(tam_populacao):
        cromossomo = []
        for j in range(tam_cromossomo):
            cromossomo.append(randint(0,1))
        populacao.append(cromossomo)
    return populacao
        
def penalidade(total_funcionarios):
    return max(0, total_funcionarios - 40)/16

def fitness(individuo):
    decimal = converte_bin_dec(individuo)
    x_standard = mapeia_d_x_standard(decimal[0])
    x_luxo = mapeia_d_x_luxo(decimal[1])
    return (x_standard*30 + x_luxo*40)/1360 - 1 * penalidade(x_standard+x_luxo*2)

if __name__ == "__main__":
    leitura()
    populacao = populacao_inicial()

    populacao.sort(key=fitness)
    (minimo, maximo) = (populacao[0], populacao[-1])

    print('População:')
    pprint([lista_string(x) for x in populacao])
    
    print('Pior indivíduo:')
    print('-> Binário: ' + str(lista_string(minimo)))

    print('-> Decimal:')
    print('--Standard: ' + str(converte_bin_dec(minimo)[0]) )
    print('--Luxo: ' + str(converte_bin_dec(minimo)[1]) )

    print('-> X:')
    print('--Standard: ' + str(mapeia_d_x_standard(converte_bin_dec(lista_string(minimo))[0])))
    print('--Luxo: ' + str(mapeia_d_x_luxo(converte_bin_dec(lista_string(minimo))[1])))

    print('Fitness: ' + str(fitness(minimo)))


    print('Melhor indivíduo:')
    print('-> Binário: ' + str(lista_string(maximo)))

    print('-> Decimal:')
    print('--Standard: ' + str(converte_bin_dec(maximo)[0]) )
    print('--Luxo: ' + str(converte_bin_dec(maximo)[1]) )

    print('-> X:')
    print('-- Standard: ' + str(mapeia_d_x_standard(converte_bin_dec(lista_string(maximo))[0])))
    print('-- Luxo: ' + str(mapeia_d_x_luxo(converte_bin_dec(lista_string(maximo))[1])))

    print('Fitness: ' + str(fitness(maximo)))
