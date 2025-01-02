from os.path import join, dirname
from re import compile


def regex(d):
    if not d:
        return ""
    if len(d) == 1:
        return next(c + regex(v) for c,v in d.items())
    else: 
        return "(?:" + "|".join(c + regex(v) for c,v in d.items()) + ")" 
    
with open(join(dirname(__file__), "input.txt")) as f:
    p = sorted(f.readline()[:-1].split(", "))
    g = {}
    for d in p:
        h = g
        for c in d:
            if not h.get(c):
                h[c] = {}
            h = h[c]
        h[""] = {}
    p = regex(g) + "+"
    print(p)
    p = compile(p)

    # p = "(:?" + "|".join(sorted(f.readline()[:-1].split(", "))) + ")+?"
    # p = compile(p)
    # p = compile("(:?" + f.readline()[:-1].replace(", ","|") + ")+")
    f.readline()
    s = [l[:-1] for l in f.readlines()]
    # r = sum(1 for d in s if p.fullmatch(d))
    for d in s:
        print(d, p)
        print(p.fullmatch(d))