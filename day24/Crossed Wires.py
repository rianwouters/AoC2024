from itertools import combinations, permutations
from os.path import join, dirname
from re import match


def bool2int(a):
    i = 0
    for bit in a:
        i = (i << 1) | bit
    return i


with open(join(dirname(__file__), "input.txt")) as f:
    inputs = {}
    while len(l := f.readline()[:-1]) > 0:
        m = match("(.\d+): (\d)", l)
        inputs[m.group(1)] = bool(int(m.group(2)))

    X = bool2int(v for k,v in sorted(inputs.items(), reverse=True) if k[0] == 'x')
    Y = bool2int(v for k,v in sorted(inputs.items(), reverse=True) if k[0] == 'y')
    S = [bool(int(bit)) for bit in f"{X+Y:b}"] 
    print("X:", X, [bool(int(bit)) for bit in f"{X:b}"] )
    print("Y:", Y, [bool(int(bit)) for bit in f"{Y:b}"] )
    print("S:", S)
    gates = []
    nz = 0
    while len(l := f.readline()[:-1]) > 9:
        m = match("(\w*) (\w*) (\w*) -> (\w*)", l)
        if m.group(4)[0] == 'z':
            nz += 1
        gates.append([m.group(1), m.group(2), m.group(3), m.group(4)])

    def all_pairs(l):
        for p in permutations(l):
            i = iter(p)
            yield list(zip(i,i))

    r = []
    for g in combinations(gates, 8):
        for pairs in all_pairs(g):
            for p in pairs:
                pass
                # p[0][3], p[1][3] = p[1][3], p[0][3]
            n = nz
            d = inputs.copy()    
            while n > 0:
                print(n, nz)
                for x, op, y, z in gates:
                    if d.get(z) == None and (vx := d.get(x)) != None and (vy := d.get(y)) != None:
                        if op == 'AND':
                            d[z] = vx and vy
                        elif op == 'OR':
                            d[z] = vx or vy
                        elif op == 'XOR':
                            d[z] = vx != vy
                        if z[0] == 'z':
                            n -= 1
            r = [v for k,v in sorted(d.items(), reverse=True) if k[0] == 'z']
            print(r)
            if r == S:
                print(g)
                exit()
            for p in pairs:
                p[0][3], p[1][3] = p[1][3], p[0][3] 
