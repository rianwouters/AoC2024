from string import digits


def borders(m):
    m = ['.' + l + '.' for l in m]
    h = [len(m[0]) * '.']
    return h + m + h

with open("input.txt") as f:
    m = [l[:-1] for l in f.readlines()] 
    m = borders(m)
    N, M, r = len(m), len(m[0]), 0
    for y in range(1,N-1):
        for x in range(1,M-1):
            if m[y][x] == '0':
                print(y,x)
                s = {(y,x)}
                for n in digits[1:]:
                    t = set()
                    for (v,u) in s:
                        for (q, p) in ((v,u-1), (v,u+1), (v-1,u), (v+1,u)):
                            if m[q][p] == n:
                                t.add((q,p)) 
                    s = t
                r += len(s)
    print(r)