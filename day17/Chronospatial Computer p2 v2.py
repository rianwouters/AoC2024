program, (A0,B0,C0) = ((2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0), (51342988,0,0))
N, s = len(program), {0}
for n in range(N-1,-1,-1):
    t = set()
    for a in s:        
        for A0 in range(a*2*2*2, (a + 1)*2*2*2):
            A, B, C = A0, 0, 0
            B = A % 8    
            C = A >> (B^3)
            B ^= C
            B = B % 8
            if B == program[n] and (n < N-1 or A0 != 0):
                t.add(A0)
    s = t
print(sorted(s))