from problem import *
from collections import deque


def solve(part, diagonal=False):
    grid = dict()
    n, m = 0, 0
    for i, line in enumerate(get_input(part).split('\n')):
        for j, c in enumerate(line):
            grid[i+1j*j] = c
            m = j
        n = i

    for j in (-1, m+1):
        for i in range(-1, n+2):
            grid[i+1j*j] = '.'

    for i in (-1, n+1):
        for j in range(-1, m+2):
            grid[i+1j*j] = '.'

    seen = set()
    active = deque([(0, z) for z, c in grid.items() if c == '.'])

    adj = {1, -1, 1j, -1j}
    if diagonal:
        adj |= {1+1j, 1-1j, -1+1j, -1-1j}

    ans = 0

    while active:
        (i, z) = active.popleft()

        if z in seen:
            continue
        seen.add(z)

        ans += i

        for d in adj:
            z_ = z + d
            if z_ in grid and z_ not in active and z_ not in seen:
                active.append((i+1, z_))

    return ans

print(f"part 1: {solve(1)}")
print(f"part 2: {solve(2)}")
print(f"part 3: {solve(3, True)}")


