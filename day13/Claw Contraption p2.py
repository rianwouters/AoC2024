from os.path import join, dirname
from re import findall

r = 0
with open(join(dirname(__file__), "input.txt")) as f:
    try:
        while True:
            ax, ay, bx, by, px, py = map(int, findall("\d+", f.readline() + f.readline() + f.readline()))
            px += 10000000000000
            py += 10000000000000
            f.readline()
            print(ax, ay, bx, by, px, py)
            n1, d1 = ay*px - ax * py , ay*bx - ax * by
            b = n1 // d1 
            n2, d2 = py - by * b, ay
            a = n2 // d2
            if n1 % d1 == 0 and n2 % d2 == 0:
                r += 3*a + b
            print(a,b)
    except:
        pass
    print(r)