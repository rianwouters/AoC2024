from math import prod
from os.path import join, dirname

from utils.aoc import add_borders, print_char_matrix

with open(join(dirname(__file__), "input.txt")) as f:
    m = []
    while len(l := f.readline()[:-1]) > 0:
        m.append(list(l))
    N, M = len(m), len(m[0])
    s = next((r,c) for r in range(N) for c in range(M) if m[r][c] == "@")

    moves = ""
    while len(l := f.readline()[:-1]) > 0:
        moves += l

    print_char_matrix(m)
    print(moves)

    r,c = s
    for move in moves:
        if move == "^":
            n = m[r - 1][c]
            if n == '.':
                m[r][c] = '.'
                m[r-1][c] = '@'
                r -= 1
            elif n == 'O':
                for r2 in range(r-2, 0, -1):
                    if m[r2][c] == '.':
                        m[r2][c] = 'O'
                        m[r-1][c] = '@'
                        m[r][c] = '.'
                        r -= 1
                        break
                    elif m[r2][c] == '#':
                        break
        elif move == "v":
            n = m[r + 1][c]
            if n == '.':
                m[r][c] = '.'
                m[r+1][c] = '@'
                r += 1
            elif n == 'O':
                for r2 in range(r+2, N):
                    if m[r2][c] == '.':
                        m[r2][c] = 'O'
                        m[r+1][c] = '@'
                        m[r][c] = '.'
                        r += 1
                        break
                    elif m[r2][c] == '#':
                        break
        elif move == ">":
            n = m[r][c + 1]
            if n == '.':
                m[r][c] = '.'
                m[r][c+1] = '@'
                c += 1
            elif n == 'O':
                for c2 in range(c+2, M):
                    if m[r][c2] == '.':
                        m[r][c2] = 'O'
                        m[r][c+1] = '@'
                        m[r][c] = '.'
                        c += 1
                        break
                    elif m[r][c2] == '#':
                        break
        elif move == "<":
            n = m[r][c - 1]
            if n == '.':
                m[r][c] = '.'
                m[r][c-1] = '@'
                c -= 1
            elif n == 'O':
                for c2 in range(c-2, 0, -1):
                    if m[r][c2] == '.':
                        m[r][c2] = 'O'
                        m[r][c-1] = '@'
                        m[r][c] = '.'
                        c -= 1
                        break
                    elif m[r][c2] == '#':
                        break
        # print(move)
        # print_char_matrix(m)

R, C = 0, 0
for r in range(N):
    for c in range(M):
        if m[r][c] == 'O':
            R += r
            C += c
print(100*R+C)
