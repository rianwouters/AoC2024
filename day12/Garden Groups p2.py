from itertools import groupby
from operator import itemgetter
from os.path import join, dirname

from utils.aoc import add_borders, get_matrix 


with open(join(dirname(__file__), "input.txt")) as f:
    m = get_matrix(f)
    m = add_borders(m)
    N, M = len(m), len(m[0])
    b, r, r2 = [M*[True] for n in range(N)], 0, 0
    for y in range(1,N-1):
        for x in range(1, M-1):
            if b[y][x]:
                b[y][x], visited, k, p, perimeter = False, [(y,x)], 0, 0, []
                while k < len(visited):
                    u, v = visited[k]
                    for d, s, t, py, px in [(0, u, v + 1, u, v),(2, u, v - 1, u, v-1), (1, u - 1, v, u - 1, v), (3, u + 1, v, u, v)]:
                        if m[s][t] == m[y][x]:
                            if b[s][t]:
                                visited.append((s,t))
                                b[s][t] = False
                        else:
                            perimeter.append((d ,py if d % 2 else px, px if d % 2 else py))
                            p += 1
                    k += 1
                a = len(visited)
                p2 = len(list(groupby(enumerate(sorted(perimeter)), lambda p: (p[1][0], p[1][1], p[0]-p[1][2]))))                                               
                r += a * p
                r2 += a * p2
    print("part 1: ", r)
    print("part 2: ", r2)
