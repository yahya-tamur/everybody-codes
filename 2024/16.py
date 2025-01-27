from problem import *
from math import inf
from collections import defaultdict


def make_cats_ds(part):
    inp = get_input(part).split('\n')
    cats = []

    for k, n in enumerate(inp[0].split(',')):
        n = int(n)
        cats.append([])
        j = 2
        while j < len(inp) and 4*k + 2 < len(inp[j]) and inp[j][4*k] != ' ':
            cats[-1].append(inp[j][4*k:4*k+3])
            j += 1

    ds = [int(x) for x in inp[0].split(',')]
    return (cats, ds)

cats, ds = make_cats_ds(1)
print(f"part 1: {' '.join(c[(d*100) % len(c)] for d, c in zip(ds, cats))}")

cats, ds = make_cats_ds(2)
def npulls(n):
    score = 0
    old_score = 0
    for n in range(0, n):
        cts = ' '.join(c[(ds[k]*n) % len(c)] for k, c in enumerate(cats))
        chars = {cts[k] for k in range(0, len(cts), 4)} | \
                {cts[k] for k in range(2, len(cts), 4)}
        for c in chars:
            if (z := cts.count(c)) >= 3:
                score += z - 2
        #if n == 100:
            #print(f"part 1: {cts}")
        #print(n, cts, chars, score - old_score)
        old_score = score
    return score

from math import lcm

lcmds = lcm(*(len(c) for c in cats))
q, r = divmod(202420242024, lcmds)
print(f"part 2: {q*npulls(lcmds) + npulls(r+1) - npulls(1)}")

cats, ds = make_cats_ds(3)
def p3max():
    ix = defaultdict(lambda:-inf)
    ix[tuple(0 for _ in ds)] = 0

    for n in range(256):
        ix_ = defaultdict(lambda:-inf)
        for t, m in ix.items():
            t_ = [(i+d)%len(c) for (i, d, c) in zip(t, ds, cats)]
            for d in (-1, 0, 1):
                t__ = tuple((i+d)%len(c) for (i, c) in zip(t_, cats))

                cts = ' '.join(c[i] for i, c in zip(t__, cats))
                chars = {cts[k] for k in range(0, len(cts), 4)} | \
                        {cts[k] for k in range(2, len(cts), 4)}
                score = 0
                for c in chars:
                    if (z := cts.count(c)) >= 3:
                        score += z - 2
                ix_[t__] = max(score+m, ix_[t__])

        ix = ix_
    return max(ix.values())

def p3min():
    ix = defaultdict(lambda:inf)
    ix[tuple(0 for _ in ds)] = 0

    for n in range(256):
        ix_ = defaultdict(lambda:inf)
        for t, m in ix.items():
            t_ = [(i+d)%len(c) for (i, d, c) in zip(t, ds, cats)]
            for d in (-1, 0, 1):
                t__ = tuple((i+d)%len(c) for (i, c) in zip(t_, cats))

                cts = ' '.join(c[i] for i, c in zip(t__, cats))
                chars = {cts[k] for k in range(0, len(cts), 4)} | \
                        {cts[k] for k in range(2, len(cts), 4)}
                score = 0
                for c in chars:
                    if (z := cts.count(c)) >= 3:
                        score += z - 2
                ix_[t__] = min(score+m, ix_[t__])

        ix = ix_
    return min(ix.values())
#print([p3try(i, d) for i in range(2) for d in (1,-1)])
#print(max(p3try(i, d) for i in range(3) for d in (1,-1)))
print(f"part 3: {p3max()} {p3min()}")
#print(min(p3try(i, d) for i in range(3) for d in (1,-1)))
        #print(n, cts, score)

# ANSWER: for all current states (i, j, k, ...) (12600 states),
# find the max scorefor next steps
