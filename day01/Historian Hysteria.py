from collections import defaultdict
from re import findall

def dist(l0, l1):        
    sum = 0
    for i0, i1 in zip(l0, l1):
        sum += abs(i0 - i1)
    return sum


def similarity(l0, l1):        
    sum = 0
    f = defaultdict(lambda: 0)
    for i in l1:
        f[i] += 1
    for i in l0:
        sum += i * f[i]
    return sum


l= [[],[]]

with open("input.txt") as f:
    for line in f.readlines():
        i = list(map(int, findall('\d+',line)))
        l[0].append(i[0])
        l[1].append(i[1])
l[0].sort()
l[1].sort()
print(dist(l[0], l[1]))
print(similarity(l[0], l[1]))

