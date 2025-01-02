from collections import defaultdict


program, (A0,B0,C0) = ((2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0), (51342988,0,0))
N = len(program)
r = ""
d = defaultdict(set)
for A0 in range(pow(2,10)):
    A, B, C = A0, 0, 0
    B = A % 8    
    C = A >> (B^3)
    B ^= C
    d[B%8].add(A0)

s = [[k] for k in d[program[0]]]

for n in range(1,N):
    t = []
    for k, *tail in s:
        if n < N-3:
            for l in d[program[n]]:
                if (l & 127) == (k >> 3):
                    t.append((l, k, *tail))
        else:
            if (k >> 3) in d[program[n]]:
                print(n,f"{k:b}", k>>3)
                t.append((k>>3, k, *tail))
    s = t
    
# s = [p for p in s if p[0] != 0]
t = []
for p in s:
    r = "".join(f"{k & 7:03b}" for k in p)
    t.append(int(r, base=2))

print(sorted(t))
for r in t:
    print(f"{r:b}")
