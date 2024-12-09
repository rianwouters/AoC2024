from re import findall

def comp(values, n):
    n, s= 3 * n, 0
    for v in values:
        o = n % 3
        if o == 0:
            s += v
        elif o == 1:
            s *= v
        else:
            s = int(str(s) + str(v))
            # s = s * pow(10, int(log10(s))) + v
        n //= 3
    return s

with open("input.txt") as f:
    r = 0
    for l in f.readlines():
        test, *values = list(map(int, findall('\d+', l)))
        for n in range(pow(3, len(values) - 1)):
            if comp(values, n) == test:
                r += test
                break        
    print(r)
