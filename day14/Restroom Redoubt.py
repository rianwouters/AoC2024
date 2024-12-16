from math import prod
from os.path import join, dirname
from re import findall

with open(join(dirname(__file__), "input.txt")) as f:
    a = [map(int, findall("-\d+|\d+", l)) for l in f.readlines()]
    N, M, S, q = 101, 103, 100, 4*[0]
    for px, py, vx, vy in a:
        x, y = (px + S * vx) % N, (py + S * vy) % M
        if x != N//2 and y != M//2:
            i = 2*(x // (N//2 + 1)) + y // (M//2 + 1)
            q[i] += 1 
    print(q, prod(q))    
        