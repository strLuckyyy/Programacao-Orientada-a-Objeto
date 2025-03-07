#!/usr/bin/env python3

def exercicio01(cols=6, rows=4):
    matrix = [[] for i in range(rows)]

    # Exercicio 1
    for i in range(cols):
        matrix[0].append(int(input(f"Informe o valor do indice {i}: ")))

    # Exercicio 1a
    for i in range(cols):
        matrix[1].append(matrix[0][cols - (i + 1)])

    # Exercicio 1b
    for i in range(cols):
        matrix[2].append(matrix[0][i] + matrix[1][i])

    # Exercicio 1c
    for i in range(cols):
        if matrix[0][i] % 2 == 0:
            matrix[3].append(matrix[0][i])

    for i in range(cols):
        if matrix[0][i] % 2 != 0:
            matrix[3].append(matrix[0][i])

    # Exercicio 1d
    tmatrix = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            tmatrix[j][i] = matrix[i][j]

    for i in range(rows):
        for j in range(cols):
            print(f'{matrix[i][j]} ', end="")
        print()

    print()

    for i in range(cols):
        for j in range(rows):
            print(f'{tmatrix[i][j]} ', end="")
        print()


exercicio01()
