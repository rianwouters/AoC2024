from collections import defaultdict
from os.path import dirname, join
from string import digits

from utils.aoc import add_borders, get_matrix


with open(join(dirname(__file__), "input.txt")) as f:
    m = get_matrix(f)
    m = add_borders(m)
    N, M, r1, r2 = len(m), len(m[0]), 0, 0
    for y in range(1,N-1):
        for x in range(1,M-1):
            if m[y][x] == '0':
                s = defaultdict(lambda:0)
                s[(y,x)] = 1
                for n in digits[1:]:
                    t = defaultdict(lambda:0)
                    for (v, u), c in s.items():
                        for (q, p) in ((v,u-1), (v,u+1), (v-1,u), (v+1,u)):
                            if m[q][p] == n:
                                t[(q,p)] += c 
                    s = t
                r1 += len(s.values())
                r2 += sum(c for c in s.values())
    
    print("part 1: ", r1)
    print("part 2: ", r2)