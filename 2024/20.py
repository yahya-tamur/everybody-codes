from problem import *
from math import inf
from collections import defaultdict

# delta altitude, fastest way S to A, A to B, B to C, C to S
# until zero?

# and then?

exit()

grid = dict()
start = None
vals = {'+': 1, '-': -2, '.': -1}

for i, line in enumerate(get_input(1).split('\n')):
    for j, c in enumerate(line):
        if c == '#':
            continue
        z = i + 1j*j
        grid[z] = c
        if c == 'S':
            grid[z] = '.'
            start = z

dirs = [1, 1j, -1j, -1]

most = [defaultdict(lambda:-inf) for _ in range(4)]

for m in most:
    m[start] = 1000

for _ in range(100):
    most_ = []

    for i in range(4):
        most_.append(defaultdict(lambda:-inf))
        for z in grid:
            most_[-1][z] = max(most[j][z+dirs[i]] + vals[grid[z]] for j in range(4) if i + j != 3)
    most = most_


print(max(max(m.values()) for m in most))
