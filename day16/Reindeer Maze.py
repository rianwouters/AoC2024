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
                e = []
                if m[y][x+1] == '.':
                    e += [((y,x,1), (y,x+1,3), 1), ((y,x,1), (y,x,3), 0), ((y,x,1), (y,x,0), 1000), ((y,x,1), (y,x,2), 1000)]            
                if m[y][x-1] == '.':
                    e += [((y,x,3), (y,x-1,1), 1), ((y,x,3), (y,x,1), 0), ((y,x,3), (y,x,0), 1000), ((y,x,3), (y,x,2), 1000)]
                if m[y+1][x] == '.':
                    e += [((y,x,2), (y+1,x,0), 1), ((y,x,2), (y,x,0), 0), ((y,x,2), (y,x,1), 1000), ((y,x,2), (y,x,3), 1000)]
                if m[y-1][x] == '.':
                    e += [((y,x,0), (y-1,x,2), 1), ((y,x,0), (y,x,2), 0), ((y,x,0), (y,x,1), 1000), ((y,x,0), (y,x,3), 1000)]
                g.add_weighted_edges_from(e)
                        
    l = shortest_path_length(g, source, weight="weight")
    print(min(l[(target[0], target[1], d)] for d in range(4)))