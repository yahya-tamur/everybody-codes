# find all gates
# find all paths between gates, including combinations of letters
# #
from problem import *
from collections import defaultdict, deque
from math import inf
import heapq as h

def solve(part):
    gates = []
    grid = dict()

    for i, line in enumerate(get_input(part).split('\n')):
        if sum(c == '#' for c in line) / len(line) > 0.8:
            for j, c in enumerate(line):
                if c == '.':
                    gates.append(i+1j*j)
        for j, c in enumerate(line):
            z = i+1j*j
            if c not in '~#':
                grid[z] = c

    paths = []

    for g in gates:
        seen = defaultdict(lambda:inf)
        active = deque([(str(g), '', 0)])
        while active:
            z, visited, steps = active.popleft()
            z = complex(z)

            if seen[(z, visited)] <= steps:
                continue
            seen[(z, visited)] = steps

            if z in gates and steps > 0:
                paths.append((g, z, visited, steps))
                continue

            for z_ in (z+1, z-1, z+1j, z-1j):
                if z_ not in grid:
                    continue

                visited_ = visited
                if grid[z_] != '.' and grid[z_] not in visited:
                    visited_ = ''.join(sorted(visited + grid[z_]))
                active.append((str(z_), visited_, steps+1))

    edges = {str(g): set() for g in gates}
    for (start, end, visited, steps) in paths:
        edges[str(start)].add((str(end), visited, steps))

    start = str(gates[0])

    heap = [(0, start, '')]
    seen = set()
    target = set(grid.values()) - {'#', '~', '.'}
    mmm = (1 << len(target))*len(gates)

    from time import time
    lp = time()

    while True:
        steps, loc, visited = h.heappop(heap)
        if time() - lp > 2:
            lp = time()
            heap = [(steps, loc, visited) for (steps, loc, visited) in heap if (loc, visited) not in seen]
            h.heapify(heap)

        if len(visited) == len(target) and loc == start:
            print(f"part {part}: {steps}")
            return

        if (loc, visited) in seen:
            continue
        seen.add((loc, visited))

        for (loc_, d_visited, d_steps) in edges[loc]:
            visited_ = ''.join(sorted(set(visited+d_visited)))
            if (loc_, visited_) not in seen:
                h.heappush(heap, (steps+d_steps, loc_, visited_))

for i in range(1, 4):
    solve(i)

