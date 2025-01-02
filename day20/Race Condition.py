from collections import defaultdict
from os.path import join, dirname

from utils.aoc import get_char_matrix, neighbors, print_char_matrix

t = 20

with open(join(dirname(__file__), "test.txt")) as f:
    m = get_char_matrix(f)
M, N = len(m), len(m[0])
ny,nx = next((y,x) for y in range(1, M-1) for x in range(1, N-1) if m[y][x] == 'S')
f = defaultdict(int)
r, k = 0, 0
y, x, d, l = 0, 0, {}, []
while (y,x) != (ny, nx):
    y,x = ny, nx
    m[y][x] = '*'
    d[(y,x)] = k
    l.append((y,x))
    for p,q in ((y,x+1),(y,x-1), (y+1,x),(y-1,x)):
        if m[p][q] in ('.', 'E'):
            ny, nx = p, q
            k += 1
            break

def best_cheats(m, sy, sx, y, x, c, cheats):
    if c == t:
        return
    for p,q in neighbors(y,x):
        if 0 <= p < M and 0 <= q < N:
            if m[p][q] == "#":
                m[p][q] = 'c'
                best_cheats(m, sy, sx, p, q, c + 1, cheats)
                m[p][q] = '#'
            elif m[p][q] == '*':
                s = d[(p, q)] - d[(sy, sx)] - c - 1
                if s > cheats.get((p,q), 0):
                    cheats[(p,q)] = s
    
for (y,x) in l:        
    cheats = {}
    best_cheats(m, y, x, y, x, 0, cheats)
    for k, v in cheats.items():
        if v > 70 :
            print (y,x, k, v)
        f[v] += 1


for k, v in f.items():
    if k >= 50:
        print(k, v)
    if k >= 100:
        r += v
print(r)