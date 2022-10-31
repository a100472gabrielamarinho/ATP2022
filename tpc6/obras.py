# Modelo : [(nome,desc,periodo,ano...)]

import csv

def leObras(filename):
    file = open(filename, encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=";")

    lista = []
    for obra in csv_file:
        lista.append(tuple(obra))
    return lista

def tamanhoObras(obra):
    return len(obra)

def imprime(obra):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for nome, desc, ano, _, comp, *_ in obra:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")    #os primeiros :20(significa que quero imprimir o nome com as letras até À vigésima posição)

def ordem(tuplo):
    return tuplo[0]


def titAno(obra):
    lista = []
    for nome, _, ano, *_ in obra:     #o *_ siginifica q continue para a frente, I think :)
        lista.append((nome,ano))
    
    lista.sort(key=ordem)   #vai ordenar segundo a função ordem, definida em cima :)
    return lista


def titAno_2(obra):
    lista = []
    for nome, _, ano, *_ in obra:
        lista.append((nome,ano))
    
    lista.sort(key= lambda tuplo: tuplo[1])  #com o lambda estou a  definir uma função dentro da própria função(é como criar e um usar o def, mas dentro da função, tudo de uma vez)
    return lista     #selecionei tuplo[1] e não tuplo[2] pois tenho em conta o tuplo novo criado(nome,ano) e não o original maior


def titporAno(obra):
    dici = {}
    for nome, _, ano, *_ in obra:
        if ano in dici.keys():
            dici[ano]= dici[ano] + [nome] #dici[ano].append(nome) 
        else:
            dici[ano] = [nome]
    return dici

def distCOMPOSITORES(obra):
    lista = []
    for nome, desc, ano, _, comp, *_ in obra:
        lista.append(comp)
    lista.sort()
    return lista

def distPeriodo(obra):
    dici = {}
    for _, _, _, periodo, *_ in obra:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici    

def distANO(obra):
    dici = {}
    for _, _,ano, *_ in obra:
        if ano in dici.keys():
            dici[ano] = dici[ano] + 1
        else:
            dici[ano] = 1
    return dici   

def distCOMP(obra):
    dici = {}
    for _, _, _, periodo,comp, *_ in obra:
        if comp in dici.keys():
            dici[comp] = dici[comp] + 1
        else:
            dici[comp] = 1
    return dici 

def compOBRAS(obra):
    lista= []
    for nome, desc, ano, _, comp, *_ in obra:
        lista.append((comp,nome)) #tem de ter o parenteses dentro de parenteses senão ele não assume como um tuplo e dá erroSammartini, Giovanni Battista
    dici2 = {}
    for comp, nome in lista:
        if comp in dici2.keys():
            dici2[comp] = dici2[comp] + [nome]
        else:
            dici2[comp] = [nome]
    return dici2

import matplotlib.pyplot as plt
def plotDistrib(distrib):
    plt.figure(figsize=[10,25])
    eixoy = list(distrib.keys())
    eixox = list(distrib.values())
    plt.barh(eixoy,eixox,color= "green")   # aqui a ordem é sempre primeiro o y e depois o x , ou seja, primeiro o que vai no eixo das ordenadas
    plt.xticks([x for x in range(0,distrib.values())],distrib.values())
    plt.show()
    return

def visualizacao(dicio): 
    new = list(dicio.items())
    for par in new:
        print(f"{par[0]:<30} =>  {par[1]}") 
    return par
    