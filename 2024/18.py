from problem import *
from math import inf
from collections import deque

def solve(part):
    grid = dict()
    palms = set()
    start = []

    inp = get_input(part).split('\n')

    for i, line in enumerate(inp):
        for j, c in enumerate(line):
            if c == '#':
                continue
            z = i+1j*j
            if i == 0 or j == 0 or i == len(inp)-1 or j == len(line)-1:
                start.append(z)
            grid[z] = 0
            if c == 'P':
                palms.add(z)
    if part < 3:
        dq = deque([(0,s) for s in start])
        seen = set()
        while palms:
            n, z = dq.popleft()

            if z in seen:
                continue
            seen.add(z)
            palms.discard(z)

            for d in (1,-1,1j,-1j):
                if z+d in grid and z+d not in seen:
                    dq.append((n+1, z+d))
        return n



    for p in palms:
        dq = deque([(0, p)])
        seen = set()

        while dq:
            n, z = dq.popleft()

            if z in seen:
                continue
            seen.add(z)

            grid[z] += n

            for d in (1,-1,1j,-1j):
                if z+d in grid and z+d not in seen:
                    dq.append((n+1, z+d))

    return min(v for k, v in grid.items() if k not in palms)

print(f"part 1: {solve(1)}")
print(f"part 2: {solve(2)}")
print(f"part 3: {solve(3)}")

