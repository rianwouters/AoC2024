
"""
Not the nicest solution but nice to try ;-)
Probably the straighforward one, searching for the X first and looking in all directions is easier
"""

from re import findall

S = "XMAS"

def search(m):
    c = 0
    for r in m:
        c += len(findall(S, r)) + len(findall(S[::-1], r))
    return c


def diagonal_order(m, N): 
    return [''.join(m[min(N, l) - j - 1][max(0, l - N) + j] for j in range(min(l, (N - max(0, l - N)), N))) for l in range(1, 2*N)]

def vertical_order(m, N):
    return [''.join(l[n] for l in m) for n in range(len(m))]

with open("input.txt") as f:
    m = [l[:-1] for l in f.readlines()]
    N = len(m)
    assert(len(m[0]) == N)
    mv = vertical_order(m, N)
    md1 = diagonal_order(m, N)
    md2 = diagonal_order(m[::-1], N)
    print(search(m + mv + md1 + md2))
    
