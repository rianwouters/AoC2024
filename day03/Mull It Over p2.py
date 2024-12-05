from re import findall

with open("input.txt") as f:
    enabled, sum = True, 0
    for l in f.readlines():
        for op,a1,a2 in findall("(mul|do|don't)(?:(?:\(\))|(?:\((\d+),(\d+)\)))", l):
            if enabled and op == "mul":
                sum += int(a1)*int(a2)
            else:
                enabled = op == "do"
    print(sum) 


