from os.path import join, dirname
from re import findall
from networkx import NetworkXNoPath, shortest_path_length

from utils.aoc import char_matrix_to_graph, print_char_matrix


fname, N, S = "input.txt", 71, 1024 
# fname, N, S = "test.txt", 7, 12
with open(join(dirname(__file__), fname)) as f:
    m = [N*['.'] for r in range(N)]
    for n in range(S):
        x,y = map(int, findall("\d+", f.readline()))
        m[y][x] = '#'
    print_char_matrix(m)

    g = char_matrix_to_graph(m)
    print(shortest_path_length(g, (0,0), (N-1, N-1)))

    while c := tuple(map(int, findall("\d+", f.readline()))):
        try:
            x,y = c
            g.remove_node((y,x))
            print(shortest_path_length(g, (0,0), (N-1, N-1)), c)
        except NetworkXNoPath:
            print(f"{x},{y}")
            break
        except:
            pass