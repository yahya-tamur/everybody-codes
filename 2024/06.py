from problem import get_input, clip
from collections import deque, defaultdict

def solve(part):
    cons = dict()

    ai = 0
    cocons = defaultdict(list)

    for line in get_input(part).split('\n'):
        l, r = line.split(':')
        cons[l] = r.split(',')
        for rr in r.split(','):
            cocons[rr].append(l)

    start = '@'
    while cocons[start]:
        start = cocons[start][0]

    prevs = dict()
    lens = defaultdict(list)
    stack = deque([(0, start)])
    seen = set()

    while stack:
        i, a = stack.popleft()
        if a in seen:
            continue
        seen.add(a)
        if a not in cons:
            continue
        for b in cons[a]:
            if b == '@':
                lens[i].append(a)
            else:
                stack.append((i+1, b))
                prevs[b] = a

    l = next(v for v in lens.values() if len(v) == 1)
    while (w := prevs.get(l[-1])) is not None:
        l.append(w)

    if part == 1:
        return ''.join(l[::-1]) + '@'
    else:
        return ''.join(x[0] for x in l[::-1]) + '@'


print(f"part 1: {solve(1)}")
print(f"part 2: {solve(2)}")
print(f"part 3: {solve(3)}")
