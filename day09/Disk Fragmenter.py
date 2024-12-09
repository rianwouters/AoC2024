with open("input.txt") as f:
    l = list(map(int, f.readline()))
    N = len(l)
    r, k, p, d1, d2 = 0, 0, 0, 0, (N-1)//2
    while k < N:
        n = l[k]
        if k % 2 == 0:
            d = d1
            d1 += 1
            k += 1
        else:
            d = d2
            if l[d*2] < n:
                n = l[d*2]
                l[k] -= n
                l[d*2] = l[d*2 - 1] = 0
                d2 -= 1
            else:
                l[d*2] -= n
                k += 1
        r += n * (n + 2 * p - 1) * d // 2
        p += n
    print(r)