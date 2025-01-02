from collections import defaultdict
from os.path import join, dirname

from utils.aoc import get_char_matrix, neighbors, print_char_matrix


with open(join(dirname(__file__), "input.txt")) as f:
    keys, locks = [], []
    lines = f.readlines()
    n = 0
    while n < len(lines):
        l = locks if lines[n][0] == '#' else keys 
        p = []
        for c in range(5):
            k = sum(1 for r in range(7) if lines[n + r][c] == '#')
            p.append(k)
        l.append(p)
        n += 8

r = 0
for l in locks:
    for k in keys:
        for c in range(5):
            if l[c] + k[c] > 7:
                r += 1
                break
print(len(locks) * len(keys) - r)
