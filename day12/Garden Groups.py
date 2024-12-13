from collections import defaultdict
from os.path import join, dirname

from utils.aoc import add_borders, get_matrix 

with open(join(dirname(__file__), "input.txt")) as f:
    m = get_matrix(f)
    m = add_borders(m)
    N, M = len(m), len(m[0])
    b, r = [M*[True] for n in range(N)], 0
    for y in range(1,N-1):
        for x in range(1, M-1):
            if b[y][x]:
                b[y][x], visited, a, p = False, [(y,x)], 0, 0
                while a < len(visited):
                    u, v = visited[a]
                    for s,t in [(u, v + 1),(u, v - 1), (u - 1, v), (u + 1, v)]:
                        if m[s][t] == m[y][x]:
                            if b[s][t]:
                                visited.append((s,t))
                                b[s][t] = False
                        else:
                            p += 1
                    a += 1
                r += len(visited) * p
    print(r)
