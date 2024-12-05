
"""
Not the nicest solution but nice to try ;-)
Probably the straighforward one, searching for the X first and looking in all directions is easier
"""

from re import findall
from functools import cmp_to_key

    

rules = []
updates = []
with open("input.txt") as f:
    for l in f.readlines():
        digits = list(map(int, findall("\d+", l)))
        if "|" in l:
            rules.append(digits)
        elif "," in l:
            updates.append(digits)

    def rule_sort(x, y):
        return -1 if [x, y] in rules else 0 # why do we not need to check the reverse and return 1??
        
    s1 = s2 = 0

    for update in updates:
        update_sorted = sorted(update, key=cmp_to_key(rule_sort))
        m = update_sorted[len(update)//2]
        if update_sorted == update:
            s1 += m
        else:
            s2 += m
    print("part 1:", s1, "part 2: ", s2)
