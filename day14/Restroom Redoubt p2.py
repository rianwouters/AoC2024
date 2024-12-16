from itertools import chain
from math import prod
from os.path import join, dirname
from re import findall

with open(join(dirname(__file__), "input.txt")) as f:
    a = [list(map(int, findall("-\d+|\d+", l))) for l in f.readlines()]
    N, M = 101, 103

    for i in range(M*N):
        grid = [[0 for n in range(N)] for m in range(M)]
        for k, (x, y, vx, vy) in enumerate(a):
            x, y = (x + vx) % N, (y + vy) % M
            grid[y][x] += 1
            a[k][0], a[k][1] = x, y
        s = ''.join(chain(*(map(str, grid[m]) for m in range(M)))) 
        if '111111111' in s:
            print(i+1)
            # for m in range(M):
            #     print(''.join(map(str, grid[m])))
            # print()
