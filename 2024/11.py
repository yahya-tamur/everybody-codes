from problem import *
from collections import defaultdict

def solve(part, start, loops):
    termites = defaultdict(int)
    termites[start] = 1
    for _ in range(loops):
        termites_ = defaultdict(int)
        for line in get_input(part).split('\n'):
            l, r = line.split(':')
            for rr in r.split(','):
                termites_[rr] += termites[l]
        termites = termites_
    return sum(termites.values())

print(f"part 1: {solve(1, 'A', 4)}")
print(f"part 2: {solve(2, 'Z', 10)}")

vals = [solve(3, line.split(':')[0], 20) for line in get_input(3).split('\n')]
print(f"part 3: {max(vals) - min(vals)}")

