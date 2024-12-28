from problem import get_input, clip

vals = {'A':0, 'B':1, 'C':3, 'D':5, 'x':0}

inp = get_input(1)

print(f"part 1: {sum(vals[x] for x in inp)}")

inp = get_input(2)
ans = sum(vals[x] for x in inp)

for i in range(0, len(inp), 2):
    pair = inp[i:i+2]
    ans += 2*('x' not in pair)

print(f"part 2: {ans}")

inp = get_input(3)
ans = sum(vals[x] for x in inp)

for i in range(0, len(inp), 3):
    pair = inp[i:i+3]
    match pair.count('x'):
        case 0:
            ans += 6
        case 1:
            ans += 2

print(f"part 3: {ans}")

