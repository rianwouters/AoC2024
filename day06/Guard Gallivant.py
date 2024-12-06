with open("input.txt") as f:
    m = [l[:-1] for l in f.readlines()]
    y, x = next((n, l.find('^')) for n, l in enumerate(m) if l.find('^') >= 0)
    m[y] = m[y].replace("^", ".")
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d, r, visited = 0, 0, [(y, x)]
    while True:
        delta = deltas[d]
        ny, nx = y + delta[0], x + delta[1]
        if not(0 <= nx < len(m[0]) and 0 <= ny < len(m)):
            break
        if m[ny][nx] == '.':
            y, x = ny, nx
            if (y, x) not in visited:
                visited.append((y, x))
        else: 
            d = (d + 1) % 4
            

    print(visited)
    print(len(visited))
