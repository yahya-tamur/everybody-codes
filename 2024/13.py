from problem import *
def solve(part):

    grid = dict()
    start, end = [], None

    for i, line in enumerate(get_input(part).split('\n')):
        for j, c in enumerate(line):
            z = i + 1j*j
            match c:
                case _ if c.isdigit():
                    grid[z] = int(c)
                case 'S':
                    start.append(z)
                    grid[z] = 0
                case 'E':
                    end = z
                    grid[z] = 0

    dz10 = lambda a, b: min((a-b)%10, (b-a)%10)

    from collections import defaultdict
    from math import inf

    seen = defaultdict(lambda:inf)

    import heapq as h

    heap = [(0, str(st)) for st in start]

    while heap:
        steps, loc = h.heappop(heap)
        loc = complex(loc)
        if loc == end:
            return steps

        if seen[loc] <= steps:
            continue
        seen[loc] = steps

        for d in (1, -1, 1j, -1j):
            if loc+d not in grid:
                continue
            h.heappush(heap, (steps + dz10(grid[loc], grid[loc+d])+1, str(loc+d)))


            




for i in range(1, 4):
    print(f"part {i}: {solve(i)}")
