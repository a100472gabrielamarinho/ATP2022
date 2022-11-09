import csv

def ler(filename):
    file = open (filename, encoding= "UTF8")
    file.readline()
    csv_file = csv.reader (file, delimiter=",")
    lista = []
    for aluno in csv_file:
        lista.append (tuple(aluno))
    return lista

def curso2(aluno):
    diciC={}
    for nr,nome,curso, *_ in aluno:
        if curso not in diciC:
            diciC[curso]=[nome]
        else:
            diciC[curso] = diciC[curso] + [nome]
    return diciC

def cursoo(aluno):
    dic = {}
    for nr,nome,curso,nota1,nota2,nota3,nota4, media in aluno:
        if curso not in dic:
            dic[curso] = 1
        else:
            dic[curso] = dic[curso] + 1
    return dic


def media(alunos):
    for alun in alunos:
        nr,nome,curso,nota1,nota2,nota3,nota4 = alun
        medias = (int(nota1) + int(nota2) + int(nota3) + int(nota4))/4 
        if 1<=int(medias)<=4:
            medias=str(medias)
            medias=("E")
        elif 5<=int(medias)<=9:
            medias=str(medias)
            medias=("D")
        elif 8<=int(medias)<=12:
            medias=str(medias)
            medias=("C")
        elif 13<=int(medias)<=16:
            medias=str(medias)
            medias=("B")
        elif 11<=int(medias)<=20:
            medias=str(medias)
            medias=("A")
        new = list(alun)
        new.append(medias)
        x = tuple(new)
        alunos[alunos.index(alun)] = x
        
    return alunos
    

def distribNOMES(alunos):
    dic = {"A": [], "B":[], "C":[], "D":[]}
    for aluno in alunos:
        nr,nome,curso,nota1,nota2,nota3,nota4, media = aluno
        if aluno[7] == "C":
            dic["C"] = dic["C"] + [aluno[1]]
        elif aluno [7] == "A":
            dic["A"] = dic["A"] + [aluno[1]]
        elif aluno[7] == "B":
            dic["B"] = dic["B"] + [aluno[1]]
        elif aluno[7] == "D":
            dic["D"] = dic["D"] + [aluno[1]]
    return dic

        
def distribCONTAGEM(aluno):
    dic = {}
    for nr,nome,curso,nota1,nota2,nota3,nota4, media in aluno:
        if media not in dic:
            dic[media] = 1
        else:
            dic[media] = dic [media] + 1
    return dic

import matplotlib.pyplot as plt
def graficoLINHAS(distrib):
    eixox = list(distrib.values())
    eixoy = list(distrib.keys())
    plt.barh(eixoy,eixox,color="blue") 
    return 

#tabela de uma distribuição:

def tabela(distrib):
    new = list(distrib.items()) #transformar o dicionario numa lista
    for par in new:
        print(f"|{par[0]:^30} | {par[1]:^30}|") 
    return par