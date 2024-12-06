deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def walk(m, sy, sx):
    y, x, d, visited = sy, sx, 0, [(sy, sx, 0)]
    while True:
        delta = deltas[d]
        ny, nx = y + delta[0], x + delta[1]
        if not(0 <= nx < len(m[0]) and 0 <= ny < len(m)):
            return visited
        if m[ny][nx] == '.':
            y, x = ny, nx
        else: 
            d = (d + 1) % 4
        if (y, x, d) in visited:
            return True
        else:
            visited.append((y, x, d))            

with open("test.txt") as f:
    m = [l[:-1] for l in f.readlines()]
    sy, sx = next(((y, x) for y, l in enumerate(m) if (x := l.find('^')) >= 0))
    m[sy] = m[sy][:sx] + "." + m[sy][sx + 1:]
    route = list(set((x,y) for x, y, d in walk(m, sy, sx)))
    print("part 1:", len(route))

    r = 0
    for n, (oy, ox) in enumerate(route[1:]):
        t, m[oy] = m[oy], m[oy][:ox] + "#" + m[oy][ox + 1:]
        if walk(m, sy, sx) == True:
            r += 1
        m[oy] = t
    print("part 2: ", r)
