C = ["MAS", "SAM"]

with open("input.txt") as f:
    m = [l[:-1] for l in f.readlines()]
    s,r = 0, range(1, len(m) - 1)
    for i in r:
        for j in r:
            d1, d2 = m[i-1][j-1] + m[i][j] + m[i+1][j+1], m[i-1][j+1] + m[i][j] + m[i+1][j-1] 
            if d1 in C and d2 in C:
                s += 1
    print(s)
