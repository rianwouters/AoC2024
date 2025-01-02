from ntpath import join
from posixpath import dirname

from networkx import Graph


def add_borders(m, n=1, c='.'):
    m = [n*c + l + n*c for l in m]
    h = n*[len(m[0]) * c]
    return h + m + h

def get_matrix(f):
    return [l[:-1] for l in f.readlines()] 

def get_char_matrix(f):
    return [list(l[:-1]) for l in f.readlines()] 

def neighbors(r,c):
    return ((r,c+1),(r,c-1), (r+1,c),(r-1,c))

def print_char_matrix(m):
    for l in m:
        for c in l:
            print(c, end="")
        print()

def char_matrix_to_graph(m):
    g = Graph()
    R, C = len(m), len(m[0])
    for r in range(R):
        for c in range(C):
            if m[r][c] == '.':
                for p,q in [(r+1, c), (r, c+1)]:
                    if p in range(R) and q in range(C) and m[p][q] == '.':
                        g.add_edge((r,c),(p,q))
    return g