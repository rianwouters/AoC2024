from collections import defaultdict
from re import findall

with open("test1.txt") as f:
    sum = 0
    for l in f.readlines():
        for (m1,m2) in findall('mul\((\d+),(\d+)\)', l):
            sum += int(m1)*int(m2)
    print(sum)    
