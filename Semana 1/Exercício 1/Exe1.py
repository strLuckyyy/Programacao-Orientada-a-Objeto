'''
1. Crie uma matriz com dimensão 4 linhas por 6 colunas e peça para o usuário informar
somente os valores da primeira linha, todos eles números inteiros. Em seguida, realize
as seguintes ações:

        a) A segunda linha deve ser uma cópia da primeira, em ordem inversa das colunas.

        b) A terceira linha deve ser a soma dos elementos da primeira e segunda linhas,
    coluna por coluna, respeitando suas respectivas posições.

        c) A quarta linha deve conter os números pares da primeira linha seguidos dos
    números ímpares também da primeira linha, um por coluna.

        d) Imprima a matriz normal e a transposta, utilizando o caractere “tab” como
    separador das colunas.
'''

import os

coluna = 6
linha = 4

os.system("cls")

def cMatriz():
    matriz = [[0 for c in range(coluna)] for l in range(linha)]
    return matriz


def primeriaLinha(matriz: list):
    matriz[0].clear()
    for i in range(coluna):
        n = int(input(f'Digite o {i + 1}o número: '))
        matriz[0].append(n)


def invertLinha(matriz: list):
    matriz[1].clear()
    for i in range(coluna):
        matriz[1].append(matriz[0][coluna - i - 1])


def somaLinhas(matriz: list, ):
    matriz[2].clear()
    for i in range(coluna):
        matriz[2].append(matriz[0][i] + matriz[1][i])


def parimpar(matriz: list):
    impar = []
    matriz[3].clear()
    for i in range(coluna):
        if matriz[0][i] % 2 == 0:
            matriz[3].append(matriz[0][i])
        else:
            impar.append(matriz[0][i])
    
    for i in range(len(impar)):
        matriz[3].append(impar[i])


def printM(matriz):
    for l in range(linha):
        for c in range(coluna):
            print(matriz[l][c], end='\t')
        print()


def printMT(matriz):
    for l in range(coluna):
        for c in range(linha):
            print(matriz[c][l], end='\t')
        print()


def main():
    matriz = cMatriz()
    primeriaLinha(matriz)
    invertLinha(matriz)
    somaLinhas(matriz)
    parimpar(matriz)

    print('\n', '-' * 50)
    print('\nMATRIZ\n\n')
    printM(matriz)
    print('\n', '-' * 50)
    print('\nMATRIZ TRANSPOSTA\n\n')
    printMT(matriz)
    print('\n', '-' * 50)

main()
