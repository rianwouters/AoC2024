from os.path import join, dirname
from re import match


def bool2int(a):
    i = 0
    for bit in d:
        i = (i << 1) | bit
    return i


with open(join(dirname(__file__), "test4.txt")) as f:
    d = {}
    while len(l := f.readline()[:-1]) > 0:
        m = match("(.\d+): (\d)", l)
        d[m.group(1)] = bool(int(m.group(2)))
    
    gates = set()
    nz = 0
    while len(l := f.readline()[:-1]) > 9:
        m = match("(\w*) (\w*) (\w*) -> (\w*)", l)
        if m.group(4)[0] == 'z':
            nz += 1
        gates.add((m.groups()))

    while nz > 0:
        for x, op, y, z in gates:
            if d.get(z) == None and (vx := d.get(x)) != None and (vy := d.get(y)) != None:
                if op == 'AND':
                    d[z] = vx and vy
                elif op == 'OR':
                    d[z] = vx or vy
                elif op == 'XOR':
                    d[z] = vx != vy
                if z[0] == 'z':
                    nz -= 1
d = [v for k,v in sorted(d.items(), reverse=True) if k[0] == 'z']
print(bool2int(d))