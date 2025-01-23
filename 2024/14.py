from problem import *
from math import inf

def solve(part):
    leaves = []
    seen = set()
    words = []
    for line in get_input(part).split('\n'):
        x, y, z = 0, 0, 0

        for ch in line.split(','):

            dx, dy, dz = {'U': (1,0,0),'D':(-1,0,0),'L':(0,1,0), \
                    'R':(0,-1,0),'F':(0,0,1),'B':(0,0,-1)}[ch[0]]
            for _ in range(int(ch[1:])):
                seen.add((x,y,z))
                x += dx
                y += dy
                z += dz
            seen.add((x,y,z))
        leaves.append((x,y,z))
    if part == 1:
        return max(s[0] for s in seen)
    elif part == 2:
        return len(seen)-1

    from collections import deque
    def pathlen(a, b):
        nonlocal seen
        visited = set()
        stack = deque([(0, a)])
        while stack:
            n, (x, y, z) = stack.popleft()
            if (x, y, z) == b:
                return n
            if (x, y, z) in visited:
                continue
            visited.add((x,y,z))

            for dx, dy, dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
                x_, y_, z_ = x+dx, y+dy, z+dz
                if (x_,y_,z_) not in seen:
                    continue
                stack.append((n+1,(x_,y_,z_)))
        return inf

    n = 0
    ans = inf

    while (n,0,0) in seen:
        ans = min(ans, sum(pathlen((n,0,0), leaf) for leaf in leaves))
        n += 1

    return ans

# part 3 takes a minute
for i in range(1, 4):
    print(f"part {i}: {solve(i)}")
