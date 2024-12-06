deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def walk(m, sy, sx):
    y, x, d, dy, dx, visited = sy, sx, 0, -1, 0, [(sy, sx, 0)]
    while 0 <= (nx := x + dx) < len(m[0]) and 0 <= (ny := y + dy) < len(m):
        if m[ny][nx] == '.':
            y, x = ny, nx
        else: 
            d = (d + 1) % 4
            dy, dx = deltas[d]
        if (y, x, d) in visited:
            return
        visited.append((y, x, d))            
    return visited

with open("test.txt") as f:
    r, m = 0, [l[:-1] for l in f.readlines()]
    sy, sx = next(((y, x) for y, l in enumerate(m) if (x := l.find('^')) >= 0))
    m[sy] = m[sy][:sx] + "." + m[sy][sx + 1:]
    route = list(set((x,y) for x, y, d in walk(m, sy, sx)))
    print("part 1:", len(route))

    for y, x in route[1:]:
        t = m[y]
        m[y] = t[:x] + "#" + t[x + 1:]
        if not walk(m, sy, sx):
            r += 1
        m[y] = t
    print("part 2: ", r)
