from collections import defaultdict
from re import findall

def is_safe(report): 
    diffs  = [p - c for p, c in zip(report, report[1:])]        
    b = None
    for d in diffs:
        a = abs(d)
        if a < 1 or a > 3:
            return False
        b2 = d < 0
        if b == None:
            b = b2
        else:
            if b != b2:
                return False
    return True

with open("input.txt") as f:
    safe = 0
    for l in f.readlines():
        report = list(map(int, findall('\d+', l)))
        if is_safe(report):
            safe += 1
        else:
            for k,v in enumerate(report):
                if is_safe(report[0:k] + report[k+1:]):
                    safe += 1
                    break
    print(safe)

