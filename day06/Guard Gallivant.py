deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def walk(m, y, x):
    N, M, d, dy, dx, visited = len(m[0]), len(m), 0, -1, 0, {(y, x, 0)}
    while 0 <= (nx := x + dx) < N and 0 <= (ny := y + dy) < M:
        if m[ny][nx] == '.':
            y, x = ny, nx
        else: 
            d = (d + 1) % 4
            dy, dx = deltas[d]
        if (y, x, d) in visited:
            return
        visited.add((y, x, d))            
    return visited

with open("input.txt") as f:
    r, m = 0, [l[:-1] for l in f.readlines()]
    sy, sx = next(((y, x) for y, l in enumerate(m) if (x := l.find('^')) >= 0))
    m[sy] = m[sy][:sx] + "." + m[sy][sx + 1:]
    route = set((x,y) for x, y, d in walk(m, sy, sx))
    print("part 1:", len(route))

    for y, x in route - {(sy, sx)}:
        t = m[y]
        m[y] = t[:x] + "#" + t[x + 1:]
        if not walk(m, sy, sx):
            r += 1
        m[y] = t
    print("part 2: ", r)
