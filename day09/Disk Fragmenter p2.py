with open("input.txt") as f:
    l = list(map(int, f.readline()))
    N = len(l)
    M = (N-1) // 2 * 2
    c, r, k, p, m = l[:], 0, 0, 0, M
    while k < N:
        if k % 2 == 0:
            r += l[k] * (l[k] + 2 * p - 1) * k // 4
            p += c[k]
            k += 1
        elif 0 < l[m] <= l[k]:
            r += l[m] * (l[m] + 2 * p - 1) * m // 4
            l[k] -= l[m]
            p += l[m]
            l[m] = 0
        elif m - 2 > k:
            m -= 2
        else:
            m = M
            p += l[k]
            k += 1
    print(r)