from collections import defaultdict
from itertools import combinations

d = defaultdict(list)

with open("input.txt") as f:
    m = [l[:-1] for l in f.readlines()]
    for n ,l in enumerate(m):
        for k, c in enumerate(l):
            if c != '.':
                d[c].append((n,k))
    s = set()
    s2 = set()
    for _ ,v in d.items():
        for (n1, n2) in combinations(v, 2):
            dy, dx  = n2[0] - n1[0], n2[1] - n1[1]

            s.add((n1[0] - dy, n1[1] - dx))
            s.add((n2[0] + dy, n2[1] + dx))
            
            n, k = n1
            while 0 <= n < len(m) and 0 <= k < len(m[0]):
                s2.add((n, k))
                n -= dy
                k -= dx 

            n, k = n2
            while 0 <= n < len(m) and 0 <= k < len(m[0]):
                s2.add((n, k))
                n += dy
                k += dx      
    
    print("part 1:", len([1 for (n,k) in s if 0 <= n < len(m) and 0 <= k < len(m[0])]))
    print("part 2:", len(s2))
