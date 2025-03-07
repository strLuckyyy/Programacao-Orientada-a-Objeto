'''
2. Um benchmark foi realizado para identificar o desempenho geral de um mesmo
algoritmo implementado em diferentes linguagens de programação. Durante os testes,
foram registradas diversas métricas em um arquivo no formato CSV, como: uso de cpu,
memória e tempo de execução, além da quantidade de linhas de código necessárias
para implementar o algoritmo em cada uma das linguagens. O desempenho geral foi
calculado através da fórmula:

        desempenho = 10^6 / (cpu * 100 + memória + tempo + linhas)

    Com base nessas informações, leia o arquivo CSV contendo os dados obtidos no
benchmark e mostre na tela:

        -a) Listagem apresentando os nomes das linguagens e seus respectivos
    desempenhos, com duas casas decimais;-
        -b) Nome das métricas e valor médio de cada métrica entre todas as linguagens,
    inclusive desempenho, com três casas decimais;-
        c) Nome da linguagem com o maior desempenho;
        d) Nome da linguagem com o menor número de linhas;
'''

import csv
import os

# Constântes
colunas = 5
linhas = 7


# Abertura do arquivo
with open('dados.csv') as csvfile:
    dadosLista = list(csv.reader(csvfile))


# Ferramentas para auxílio na criação das tabelas (titulo | corte)
def titulo(txt = 'TITULO'):
    print(
        f'-' * 50,
        f'{txt}'.center(50),
        f'-' * 50,
        sep='\n'
    )


def corte():
    print('-' * 50)
    print('.\n.\n.')


# Código principal
def calcularMedia(vlDesempenho: float):
    # Variáveis
    nomeMedia: str = ''
    strMedia: str = ''
    strDesempenho: str = f'{vlDesempenho:.3f}'
    vlMedia: float = 0.0

    for c in range(1, colunas):
        for l in range(1, linhas):
            nomeMedia = dadosLista[0][c]
            vlMedia += float(dadosLista[l][c])
        
        vlMedia /= (linhas - 1)
        strMedia = f'{vlMedia:.3f}'
        print(
            f'|Médias de {nomeMedia:<8}', f'||'.center(20), f'{strMedia:>8}|'
        )
        vlMedia = 0.0
    print('{:<8}'.format('|Médias de desempenho'), f'||'.center(15), f'\t{strDesempenho:>9}|')


def calculoDesempenho():
    # Lists
    calcDesemp: float = 0.0
    listDesempenho: list = []

    for i in range(1, linhas):
        # desempenho = 10^6 / (cpu * 100 + memória + tempo + linhas)
        calcDesemp = 10 ** 6 / (int(dadosLista[i][1]) * 100 + float(dadosLista[i][2]) + int(dadosLista[i][3]) + int(dadosLista[i][4]))
        listDesempenho.append(calcDesemp)
    
    return listDesempenho


def maxDesempenho(desempenho: list):
    # Variáveis
    strMDesem: str = ''
    indLingua: int = 0

    # List
    maxDes: list = []

    indLingua = desempenho.index(max(desempenho))
    maxDes.append(dadosLista[indLingua + 1][0])
    strMDesem = str(f'{desempenho[indLingua]:.3f}')
    maxDes.append(strMDesem)

    return maxDes
     

def menorNLinhas():
    # Variáveis
    ind: int = 0
    
    # Lists
    listLinhas: list = []
    resultado: list = []

    for i in range(1, linhas):
        listLinhas.append(dadosLista[i][4])

    ind = listLinhas.index(min(listLinhas))
    
    resultado.append(dadosLista[ind + 1][0])
    resultado.append(str(min(listLinhas)))

    return resultado


def main():
    # Variáveis
    listDesempenho = calculoDesempenho()
    maiorDesempenho = maxDesempenho(listDesempenho)
    menorNumeroLinhas = menorNLinhas()
    mediaDesempenho: float = sum(listDesempenho) / (linhas - 1)

    # Limpando o console
    os.system("cls")

    titulo('DESEMPENHO POR LINGUAGEM')
    for i in range(1, linhas):
        print(f'|{dadosLista[i][0]:<8}', f'||'.center(32), f'{listDesempenho[i - 1]:.2f}|')
    corte()

    titulo('MÉDIAS')
    calcularMedia(mediaDesempenho)
    corte()

    titulo('LINGUAGEM COM MAIOR DESEMPENHO')
    print(f'|{maiorDesempenho[0]:<8}', f'||'.center(30), f'{maiorDesempenho[1]:>8}|')
    corte()

    titulo('LINGUAGEM COM O MENOR NÚMERO DE LINHAS')
    print(f'|{menorNumeroLinhas[0]:<8}', f'||'.center(30), f'{menorNumeroLinhas[1]:>8}|')
    corte()


main()
