'''
Um benchmark foi realizado para identificar o desempenho geral de um mesmo algoritmo implementado em diferentes 
linguagens de programação. Durante os testes, foram registradas diversas métricas em um arquivo no formato CSV, como:
uso de cpu, memória e tempo de execução, além da quantidade de linhas de código necessárias para implementar o algoritmo 
em cada uma das linguagens. O desempenho geral foi calculado através da fórmula: 
desempenho = 106 / (cpu*100 + memória + tempo + linhas). Com base nessas informações, leia o arquivo CSV contendo os
dados obtidos no benchmark e mostre na tela:

         a)    Listagem apresentando os nomes das linguagens e seus respectivos desempenhos, com duas casas decimais;

         b)    Nome das métricas e valor médio de cada métrica entre todas as linguagens, inclusive desempenho, 
         com três casas decimais;

         c)    Nome da linguagem com o maior desempenho;

         d)    Nome da linguagem com o menor número de linhas;

Arquivo: 

linguagem,cpu,memória,tempo,linhas
C,20,2505.85,130,300
C++,23,3197.64,110,365
C#,28,3986.27,146,387
Java,32,4168.10,182,416
Python,25,3589.43,125,160
Delphi,23,3341.98,137,371
PHP,31,4033.50,158,322
'''
import csv

def main(lista):
    listLinguagem = []
    listCpu = []
    listMemory = []
    lisTempo = []
    listLinhas = []

    for cont in range(1, 8): 
        listLinguagem.append(lista[cont][0])
        listCpu.append(lista[cont][1])
        listMemory.append(lista[cont][2])
        lisTempo.append(lista[cont][3])
        listLinhas.append(lista[cont][4])
    
    inde = listLinhas.index(min(listLinhas)) ##numero index
    menorLinhas = f'\nLinguagem {listLinguagem[inde]}  //  {min(listLinhas)}' ##print

    strDesemp = desempenho(listLinguagem, listCpu, listMemory, lisTempo, listLinhas, 1)
    listDesemp = desempenho(listLinguagem, listCpu, listMemory, lisTempo, listLinhas, 2)
    
    metricas(listDesemp, listCpu, listMemory, lisTempo, listLinhas)
    relatorio(strDesemp, menorLinhas)
    


def metricas(desemp, cpu, memory, tempo, linha):
    mediaCpu = 0
    mediaMemory = 0
    mediaTempo = 0
    mediaLinha = 0
    mediaDesemp = 0

    for m in range(7):
        mediaCpu += float(cpu[m])
        mediaMemory += float(memory[m])
        mediaTempo += float(tempo[m])
        mediaLinha += float(linha[m])
        mediaDesemp += float(desemp[m])

    mediaCpu /= 7
    mediaMemory /= 7
    mediaTempo /= 7
    mediaLinha /= 7
    mediaDesemp /= 7
    print('\n\n')
    print('-' * 50)
    print(f'MEDIAS:')
    print('-' * 50)
    print(f'A media de CPU: {mediaCpu:.3f}\nA media de memoria: {mediaMemory:.3f}\nA media de tempo: {mediaTempo:.3f}\nA media de linhas: {mediaLinha:.3f}\nA media de desempenho: {mediaDesemp:.3f}')


def relatorio(desempenho, linhas):
    print('\n\n')
    print('-' * 50)
    print(f'LINGUAGEM COM MAIOR DESEMPENHO: {desempenho}\n\n\n'.center(50))
    print('-' * 50)
    print(f'LINGUAGEM COM MENOR NUMERO DE LINHAS: {linhas}'.center(50))
    print('-' * 50)


def desempenho(ling, cpu, memory, tempo, linha, num):
    vetDesemp = []
    vetLinguagem = []
    melhorDesemp = ''
    
    if num == 1:
        print('\n\n')
        print('-' * 50)
        print('DESEMPENHO DE CADA LINGUAGEM'.center(50))
        print('-' * 50)
        for i in range(7):
            desempenho = 10**6 / (int(cpu[i]) * 100 + float(memory[i]) + int(tempo[i]) + int(linha[i]))
            vetDesemp.append(desempenho)
            vetLinguagem.append(ling[i])
            print(f'{ling[i]}    =    {desempenho:.2f}')

        inde = vetDesemp.index(max(vetDesemp))
        melhorDesemp = f'\nLinguagem {vetLinguagem[inde]}  //  {max(vetDesemp):.3f}'

        return melhorDesemp
    elif num == 2:
        for i in range(7):
            desempenho = 106 / (int(cpu[i]) * 100 + float(memory[i]) + int(tempo[i]) + int(linha[i]))
            vetDesemp.append(desempenho)
        return vetDesemp


if __name__ == '__main__':
    with open('dados.csv', 'r') as csvfile:
        listCsv = list(csv.reader(csvfile))

    main(listCsv)