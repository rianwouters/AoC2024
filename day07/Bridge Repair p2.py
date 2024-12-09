from re import findall

def comp(values, n):
    n, s= 3*n, 0
    for v in values:
        m = n % 3
        if m == 0:
            s += v
        elif m == 1:
            s *= v
        else:
            s = int(str(s) + str(v))
        n //= 3
    return s

with open("test.txt") as f:
    r = 0
    for l in f.readlines():
        test, *values = list(map(int, findall('\d+', l)))
        N = len(values)
        for n in range(pow(3, N-1)):
            if comp(values, n) == test:
                r += test
                break        
    print(r)
