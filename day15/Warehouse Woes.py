from math import prod
from os.path import join, dirname

from utils.aoc import print_char_matrix

with open(join(dirname(__file__), "test2.txt")) as f:
    m = []
    while len(l := f.readline()[:-1]) > 0:
        for k,v in {"#": "##", "O": "[]", ".": "..", "@": "@."}.items():
            l = l.replace(k, v)
        m.append(l)
    m = [[c for c in r] for r in m]
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
            elif n == '[' or n == ']':                
                cc = [(c, 1), (c if n == '[' else c-1, 2)]
                k = 1
                for r2 in range(r-2, 0, -1):
                    if m[r2][cc[k][0]:cc[k][0] + cc[k][1]] == cc[k][1]*["."]:
                        for r3 in range(r2, r):
                            m[r3][cc[k][0]:cc[k][0] + cc[k][1]] = m[r3+1][cc[k][0]:cc[k][0] + cc[k][1]]
                            m[r3+1][cc[k][0]:cc[k][0] + cc[k][1]] = cc[k][1]*["."]
                            k -= 1
                        m[r][c] = '.'
                        r -= 1
                        break
                    elif '#' in m[r2][cc[k][0]:cc[k][0] + cc[k][1]]:
                        break
        elif move == "v":
            n = m[r + 1][c]
            if n == '.':
                m[r][c] = '.'
                m[r+1][c] = '@'
                r += 1
            elif n == '[' or n == ']':
                for r2 in range(r+2, N):
                    if m[r2][c] == '.':
                        m[r2][c] = n
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
            elif n == '[':
                for c2 in range(c+2, M):
                    if m[r][c2] == '.':
                        m[r][c + 1:c2 + 1] = m[r][c:c2]
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
            elif n == ']':
                for c2 in range(c-2, 0, -1):
                    if m[r][c2] == '.':
                        m[r][c2:c] = m[r][c2 + 1:c + 1]
                        m[r][c] = '.'
                        c -= 1
                        break
                    elif m[r][c2] == '#':
                        break
        print(move)
        print_char_matrix(m)

R, C = 0, 0
for r in range(N):
    for c in range(M):
        if m[r][c] == '[':
            R += r
            C += c
print(100*R+C)
