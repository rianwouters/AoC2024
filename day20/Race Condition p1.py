from os.path import join, dirname

from utils.aoc import get_char_matrix

with open(join(dirname(__file__), "input.txt")) as f:
    m = get_char_matrix(f)
    M, N = len(m), len(m[0])
    ny,nx = next((y,x) for y in range(1, M-1) for x in range(1, N-1) if m[y][x] == 'S')
    cheats = {}
    r, k = 0, 0
    y, x = 0, 0
    while (y,x) != (ny, nx):
        y,x = ny, nx
        m[y][x] = '*'
        for p,q in ((y,x+1),(y,x-1), (y+1,x),(y-1,x)):
            c = m[p][q]
            if c in ('.', 'E'):
                ny, nx = p, q
            elif c == '#':
                d = cheats.get((p,q))
                if d != None:
                    if k-d >= 100:
                        r += 1
                else:
                    cheats[(p,q)] = k + 2
        k += 1
print(r)