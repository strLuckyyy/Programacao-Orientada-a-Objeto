#!/usr/bin/env python3

import csv


def exercicio02():
    # Exercicio 2:
    with open('file.csv') as file:
        reader = csv.reader(file, delimiter=',')

        info = []
        for r in reader:
            row = []
            row.append(r[0])
            row.append(r[1])
            row.append(r[2])
            row.append(r[3])
            row.append(r[4])
            # OU
            # info.append(r[:5])
            info.append(row)

    l = len(info)

    # Exercicio 2a
    info[0].append('performance')
    for i in range(1, l):
        p = (10 ** 6) / (float(info[i][1]) * 100 + float(info[i][2]) +
                         float(info[i][3]) + float(info[i][4]))
        info[i].append(p)
        print(f'Linguagem: {info[i][0]} \t - Performance: {float(info[i][5]):.2f}')

    # Exercicio 2b
    cpu = 0
    mem = 0
    time = 0
    lines = 0
    perf = 0
    for i in range(1, l):
        cpu += float(info[i][1])
        mem += float(info[i][2])
        time += float(info[i][3])
        lines += float(info[i][4])
        perf += float(info[i][5])
    # OU
    # cpu = sum(float(info[i][1]) for i in range(1, l))
    # mem = sum(float(info[i][2]) for i in range(1, l))

    print(f'Metric: {info[0][1]} - Average: {float(cpu / l):.3f}')
    print(f'Metric: {info[0][2]} - Average: {float(mem / l):.3f}')
    print(f'Metric: {info[0][3]} - Average: {float(time / l):.3f}')
    print(f'Metric: {info[0][4]} - Average: {float(lines / l):.3f}')
    print(f'Metric: {info[0][5]} - Average: {float(perf / l):.3f}')

    # Exercicios 2c e 2d
    bp = info[1][5]
    ip = 1
    ll = info[1][4]
    ill = 1
    for i in range(2, l):
        if info[i][5] > bp:
            bp = info[i][5]
            ip = i
        if info[i][4] < ll:
            ll = info[i][4]
            ill = i
    # OU
    # bp, ip = max((info[i][5], i) for i in range(1, l))
    # ll, ill = min((info[i][4], i) for i in range(1, l))

    print(f'Best performance: {info[ip][0]} - Value: {bp:.2f}')
    print(f'Less lines: {info[ill][0]} - Value: {ll}')


exercicio02()
