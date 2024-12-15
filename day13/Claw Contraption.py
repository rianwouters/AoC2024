from os.path import join, dirname
from re import findall

r = 0
with open(join(dirname(__file__), "input.txt")) as f:
    try:
        while True:
            ax, ay = map(int, findall("\d+", f.readline()))
            bx, by = map(int, findall("\d+", f.readline()))
            px, py = map(int, findall("\d+", f.readline()))
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
# px = ax * a + bx * b
# py = ay* a + by * b

# px = ax * a + bx * b
# (ax/ay) * py * (ax/ay) * ay* a + (ax/ay) * by * b

# px - (ax/ay) * py = bx * b - (ax/ay) * by * b
# ay*px - ax * py = (ay*bx - ax * by) * b
# b = (ay*px - ax * py) / (ay*bx - ax * by) 

# a = (py - by * b) / ay = py/ay - by/ay * (ay*px - ax * py) / (ay*bx - ax * by)* 



# 8400 = 94a + 22b
# 5400 = 34a + 67b) *(94/34) = 5400 * (94/34) = 94a + 67*(94/34)b

# 8400 - 5400 * (94/34) = 22b - 67*(94/34)b

# 8400 - 5400 * (94/34) = (22 - 67*(94/34)) * b
# b
# = 8400 - 5400 * (94/34) / (22 - 67*(94/34))
# = 34*8400 - 5400 * 94 / 22*34 - 67*94)
# 
# a = (8400 - 22b) / 94


