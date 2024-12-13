from itertools import groupby
from os.path import join, dirname

from utils.aoc import add_borders, get_matrix 


with open(join(dirname(__file__), "input.txt")) as f:
    m = get_matrix(f)
    m = add_borders(m)
    N, M = len(m), len(m[0])
    b = [M*[True] for n in range(N)]
    r1 = r2 = 0
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if b[y][x]:
                b[y][x], visited, a, perimeter = False, [(y,x)], 0, []
                while a < len(visited):
                    u, v = visited[a]
                    for d, (s, t, py, px) in enumerate([(u, v + 1, u, v),(u - 1, v, u - 1, v), (u, v - 1, u, v - 1), (u + 1, v, u, v)]):
                        if m[s][t] == m[y][x]:
                            if b[s][t]:
                                visited.append((s,t))
                                b[s][t] = False
                        else:
                            perimeter.append((d ,py if d % 2 else px, px if d % 2 else py))
                    a += 1
                r1 += a * len(perimeter)
                r2 += a * sum(1 for _ in groupby(enumerate(sorted(perimeter)), lambda p: (p[1][0], p[1][1], p[0]-p[1][2])))
    print("part 1: ", r1)
    print("part 2: ", r2)
