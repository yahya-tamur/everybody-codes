from problem import *
from collections import defaultdict

def part12(part):
    inp = get_input(part).split('\n')

    i, j = next((i, j) for i in range(len(inp)) for j in range(len(inp[0])) \
            if inp[i][j] == 'A')
    target = j - i

    vals = defaultdict(int, {'T': 1, 'H': 2})

    ans = 0
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            k = j - i - target
            ans += vals[inp[i][j]]*(1 + (k % 3))*(k // 3)

    return ans

print(f"part 1: {part12(1)}")
print(f"part 2: {part12(2)}")

ans = 0

specials = {(2,3):3, (1,1):0}

for line in get_input(3).split('\n'):
    if not line:
        break
    x, y = (int(s) for s in line.split(' '))

    x, y = (x // 2, (y - x + (x // 2)))

    if (x, y) in specials:
        ans += specials[(x,y)]

    if y-x >= 3:
        # unreachable!
        continue

    # can hit while ascending?
    if y-x in range(3):
        ans += (y-x+1)*x
        continue



    # can hit while coasting?
    if 2*y >= x:
        ans += y
        continue

    ans += (1 + ((x + y) % 3))*((x + y) // 3)

print(f"part 3: {ans}")
