from os.path import join, dirname
from re import match


def bool2int(a):
    i = 0
    for bit in a:
        i = (i << 1) | bit
    return i


with open(join(dirname(__file__), "test3.txt")) as f:
    inputs = {}
    while len(l := f.readline()[:-1]) > 0:
        m = match("(.\d+): (\d)", l)
        inputs[m.group(1)] = bool(int(m.group(2)))
    
    X = bool2int(v for k,v in sorted(inputs.items(), reverse=True) if k[0] == 'x')
    Y = bool2int(v for k,v in sorted(inputs.items(), reverse=True) if k[0] == 'y')
    S = X & Y
    print("X:", X, [bool(int(bit)) for bit in f"{X:b}"] )
    print("Y:", Y, [bool(int(bit)) for bit in f"{Y:b}"] )
    print("S:", S, [bool(int(bit)) for bit in f"{S:b}"])


    gates = set()
    nz = 0
    while len(l := f.readline()[:-1]) > 9:
        m = match("(\w*) (\w*) (\w*) -> (\w*)", l)
        if m.group(4)[0] == 'z':
            nz += 1
        gates.add((m.groups()))

    while nz > 0:
        for x, op, y, z in gates:
            if inputs.get(z) == None and (vx := inputs.get(x)) != None and (vy := inputs.get(y)) != None:
                if op == 'AND':
                    inputs[z] = vx and vy
                elif op == 'OR':
                    inputs[z] = vx or vy
                elif op == 'XOR':
                    inputs[z] = vx != vy
                if z[0] == 'z':
                    nz -= 1
r = [v for k,v in sorted(inputs.items(), reverse=True) if k[0] == 'z']
print(r, bool2int(r))