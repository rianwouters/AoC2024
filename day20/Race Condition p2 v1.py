from collections import defaultdict
from os.path import join, dirname

from utils.aoc import get_char_matrix, neighbors

def add_cheats(m, sy, sx, y, x, t, c, k, cheats):
    if t == 0:
        return
    for p,q in neighbors(y,x):
        if 0 <= p < M and 0 <= q < N:
            if m[p][q] == "#":
                m[p][q] = 'c'
                add_cheats(m, sy, sx, p, q, t - 1, c + 1, k, cheats)
                m[p][q] = '#'
            elif m[p][q] in ['.', 'E']:
                e = cheats[(p,q)].get((sy,sx), 10000)
                d = k + c + 1
                if d < e:
                    cheats[(p,q)][(sy,sx)] = d

with open(join(dirname(__file__), "test.txt")) as f:
    m = get_char_matrix(f)
    M, N = len(m), len(m[0])
    ny,nx = next((y,x) for y in range(1, M-1) for x in range(1, N-1) if m[y][x] == 'S')
    cheats = defaultdict(dict)
    f = defaultdict(int)
    r, k = 0, 0
    y, x = 0, 0
    while (y,x) != (ny, nx):
        y,x = ny, nx
        m[y][x] = '*'
        
        add_cheats(m, y, x, y, x, 21, 0, k, cheats)
        
        for s, d in cheats[(y,x)].items():
            f[k-d] += 1
            if k - d >= 100:
                r += 1  
            # if k - d == 50:
            #     print(y,x, s, k, d) 

        for p,q in ((y,x+1),(y,x-1), (y+1,x),(y-1,x)):
            if m[p][q] in ('.', 'E'):
                ny, nx = p, q
                k += 1
for k, v in f.items():
    if k >= 50:
        print(k, v)
print(r)