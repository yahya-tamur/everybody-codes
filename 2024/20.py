from problem import *
from math import inf
from collections import defaultdict

def part1():
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


    return max(max(m.values()) for m in most)

def part2():
    grid = dict()
    specials = dict()
    vals = {'+': 1, '-': -2, '.': -1}

    for i, line in enumerate(get_input(2).split('\n')):
        for j, c in enumerate(line):
            if c == '#':
                continue
            z = i + 1j*j
            grid[z] = c
            if c not in '-+.':
                grid[z] = '.'
                specials[c] = z

    dirs = [1, 1j, -1j, -1]


# state[status][last_moved][z] at time t: highest altitude reachable at t steps

    state = [[defaultdict(lambda:-inf) for _dir in range(4) ] for _status in range(4)]

    ladders = [[specials[c]] for c in 'ABC'] + [[specials[c] for c in 'ABC']]

    for d in range(4):
        state[0][d][specials['S']] = 0

    t = 0
    while True:
        state_ = [[defaultdict(lambda:-inf) for _ in range(4)] for _ in range(4)]
        aaa = None

        for status in range(4):
            for di, d in enumerate(dirs):
                for z in grid:
                    if z-d not in grid:
                        continue
                    status_ = status + (z in ladders[status])
                    if status_ >= 4:
                        continue
                    state_[status_][di][z] = max(state_[status_][di][z], \
                            vals[grid[z]] + max(state[status][dj][z-d] for dj in range(4) if dj + di != 3))

        state = state_
        t += 1

        if any(state[3][di][specials['S']] >= 0 for di in range(4)):
            return t

def part3():
    n = 384400
    grid = get_input(3).split('\n')
    start = next(line.find('S') for line in grid if 'S' in line)
    starcols = [j for j in range(len(grid[0])) if {grid[i][j] for i in range(len(grid))} == {'.','+'}]
    dn, j = min((abs(start - j), j) for j in starcols)
    n -= dn

    line = [grid[i][j] for i in range(len(grid))]
    ans = 0
    while n > 0:
        ans += 1
        n += {'+': 1, '.': -1}[line[ans % len(line)]]
    return ans

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
print(f"part 3: {part3()}")
