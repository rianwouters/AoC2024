from functools import cache
from math import log10


test1 = [0, 1, 10, 99, 999]
test2 = [125, 17]
input = [7568, 155731, 0, 972, 1, 6919238, 80646, 22]

@cache
def f(n):
    if n == 0:
        return [1]
    elif (e := int(log10(n))+1) % 2 == 0:
        d = 10**(e//2)
        return [n // d, n % d]
    else:
        return [n * 2024]
    

s = input
d = {}
for n in s:
    s = [n]
    print(s)
    for i in range(75):
        t = []
        for n in s:
            if not d.get(n):
                t += f(n)
                d[n] = True
            else:
                print(n)
        s = t
        print(s, i)

# print(len(t))







