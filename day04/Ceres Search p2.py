C = ["MS", "SM"]

with open("input.txt") as f:
    m = ["."+l[:-1] + "." for l in f.readlines()]
    N = len(m)
    m = [(N + 2)*"."] + m + [(N + 2)*"."]
    r = 0
    for i in range(1, N + 1):
        for j in range(1,N + 1):
            if m[i][j] == 'A':
                d1, d2 = m[i-1][j-1] + m[i+1][j+1], m[i-1][j+1] + m[i+1][j-1] 
                if d1 in C and d2 in C:
                    r += 1
    print(r)
