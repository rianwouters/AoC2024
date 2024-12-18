from os.path import join, dirname

from networkx import Graph, shortest_path_length

from utils.aoc import get_char_matrix

with open(join(dirname(__file__), "input.txt")) as f:
    m = get_char_matrix(f)
    M, N = len(m), len(m[0])
    g = Graph()
    for y in range(1, M-1):
        for x in range(1, N-1):
            if m[y][x] == 'S':
                source = (y, x, 1)
                m[y][x] = '.'
            if m[y][x] == 'E':
                target = (y, x)
                m[y][x] = '.'
            if m[y][x] == '.':
                e = [((y,x,0), (y,x,1), 1000)]                
                for p,q,d in ((y,x+1,1),(y,x-1,1), (y+1,x,0),(y-1,x,0)):
                    if m[p][q] == '.':
                        e += [((y,x,d), (p,q,d), 1)]
                g.add_weighted_edges_from(e)
        g.add_weighted_edges_from([((target[0], target[1], 0), (target[0], target[1], 1), 1)])
    l = shortest_path_length(g, source, weight="weight")
    print(l[(target[0], target[1], 0)])