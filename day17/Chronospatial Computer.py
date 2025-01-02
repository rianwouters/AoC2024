test = ((0,1,5,4,3,0), (729,0,0))
test1 = ((2,6), (0,0,9))
test2 = ((5,0,5,1,5,4), (10,0,0))
test3 = ((0,1,5,4,3,0), (2024,0,0))
test4 = ((1,7), (0,29,0))
test5 = ((4,0), (0,2024,43690))
test6 = ((0,3,5,4,3,0), (117440,0,0))
input = ((2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0), (108107574778365,0,0))
program, (A,B,C) = input
output, k, N = [], 0, len(program)
while k < N:
    instr, op = program[k:k+2]
    combo = (A,B,C)[op-4] if 4 <= op < 7 else op
    match instr:
        case 1:
            B ^= op
        case 4:
            B ^= C
        case 3:
            if A != 0 and k != op:
                k = op - 2       
        case 2:
            B = combo % 8    
        case 5:
            output.append(combo % 8)
        case 0:
            A = A >> combo
        case 6:
            B = A >> combo
        case 7:
            C = A >> combo
    k += 2

print(",".join(map(str, output)))