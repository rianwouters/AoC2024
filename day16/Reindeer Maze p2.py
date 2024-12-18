from os.path import join, dirname

from networkx import Graph, all_shortest_paths, shortest_path_length

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
                target = (y, x, 0)
                m[y][x] = '.'
            if m[y][x] == '.':
                g.add_weighted_edges_from(
                    [((y,x,0), (y,x,1), 1000)] + 
                    [((y,x,d), (p,q,d), 1) for p,q,d in ((y,x+1,1),(y,x-1,1), (y+1,x,0),(y-1,x,0)) if m[p][q] == '.']
                )
        g.add_weighted_edges_from([(target, (target[0], target[1], 1), 1)])

    l = shortest_path_length(g, source, weight="weight")
    print(l[(target[0], target[1], 0)])        
    l = all_shortest_paths(g, source, target, weight="weight")
    print(len({(x,y) for p in l for x,y,z in p}))