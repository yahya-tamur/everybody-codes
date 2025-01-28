from problem import *
from math import prod

def man(z):
    return int(abs(z.real) + abs(z.imag))

def solve(part):
    stars = []

    inp = get_input(part)

    for i, line in enumerate(inp.split('\n')):
        for j, c in enumerate(line):
            if c == '*':
                stars.append(i+1j*j)

    trees = {z: i for i, z in enumerate(stars)}
    sizes = [1 for _ in stars]

    edges = [(s0, s1) for i, s1 in enumerate(stars) for s0 in stars[:i]]
    edges.sort(key=lambda zw:man(zw[0] - zw[1]))

    ans = 0

    c = 0
    for z, w in edges:
        if part == 3 and man(z - w) >= 6:
            break

        if trees[z] != trees[w]:
            sizes[trees[w]] += sizes[trees[z]] + man(z-w)
            sizes[trees[z]] = 0
            tz, tw = trees[z], trees[w]
            c += 1
            ans += man(z-w)
            for k, v in trees.items():
                if v == tz:
                    trees[k] = tw
    if part != 3:
        return ans + len(stars)

    sizes.sort()
    return prod(sizes[-3:])

print(f"part 1: {solve(1)}")
print(f"part 2: {solve(2)}")
print(f"part 3: {solve(3)}")


