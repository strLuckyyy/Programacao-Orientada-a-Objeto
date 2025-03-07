#!/usr/bin/env python3

def exercicio01(cols=6, rows=4):
    matrix = []

    # Exercicio 1
    row = []
    for i in range(cols):
        row.append(int(input(f"Informe o valor do indice {i}: ")))
    matrix.append(row)

    # Exercicio 1a
    row = [matrix[0][cols-i-1] for i in range(cols)]
    matrix.append(row)

    # Exercicio 1b
    row = [matrix[0][i] + matrix[1][i] for i in range(cols)]
    matrix.append(row)

    # Exercicio 1c
    even = [matrix[0][i] for i in range(cols) if matrix[0][i] % 2 == 0]
    odd = [matrix[0][i] for i in range(cols) if matrix[0][i] % 2 != 0]
    matrix.append(even + odd)

    # Exercicio 1d
    tmatrix = [[0 for i in range(rows)] for i in range(cols)]
    row = []
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
