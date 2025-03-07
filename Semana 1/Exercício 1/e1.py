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

os.system('cls')

colunas = 6
linhas = 4

def matriz() -> list:
    matriz = [[0 for c in range(colunas)] for l in range(linhas)]
    return matriz


def primeira_linha(matriz: list) -> list:
    matriz[0].clear()
    for c in range(colunas): matriz[0].append(int(input(f'Insira o {c + 1}o valor: ')))
    return matriz


def segunda_linha(matriz: list) -> list:
    matriz[1].clear()
    for c in range(colunas): matriz[1].append(matriz[0][5 - c])
    return matriz


def terceira_linha(matriz: list) -> list:
    matriz[2].clear()
    for c in range(colunas): matriz[2].append(matriz[0][c] + matriz[1][c])
    return matriz


def quarta_linha(matriz: list) -> list:
    matriz[3].clear()
    par = []
    impar = []

    for c in range(colunas):
        if matriz[0][c] % 2 == 0: par.append(matriz[0][c])
        else: impar.append(matriz[0][c])

    matriz[3] = par + impar
    return matriz


def print_matriz(matriz: list) -> None:
    for l in range(linhas):
        for c in range(colunas):
            print(matriz[l][c], end='\t')
        print()


def print_matriz_trans(matriz: list) -> None:
    for c in range(colunas):
        for l in range(linhas):
            print(matriz[l][c], end='\t')
        print()


if __name__ == '__main__':
    matriz = matriz()
    matriz = primeira_linha(matriz)
    matriz = segunda_linha(matriz)
    matriz = terceira_linha(matriz)
    matriz = quarta_linha(matriz)

    print('\nMatriz Normal\n')
    print_matriz(matriz)

    print('\nMatriz Transposta\n')
    print_matriz_trans(matriz)
