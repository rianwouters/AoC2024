from re import findall


def comp(values, ops):
    s = values[0]
    for v, o in zip(values[1:], ops):
        if o == '0':
            s += v
        else:
            s *= v
    return s

r = 0
with open("input.txt") as f:
    for l in f.readlines():
        test, *values = list(map(int, findall('\d+', l)))
        N = len(values)
        for n in range(pow(2, N-1)):
            sum = comp(values, f"{n:b}".rjust(N-1,'0')) 
            if sum == test:
                print(test, values, n)
                r += test
                break
        
    print(r)
