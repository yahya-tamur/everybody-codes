from problem import get_input

def get_cols(part):
    inp = [l.split(' ') for l in get_input(part).split('\n')]
    cols = [[] for _ in range(len(inp[0]))]

    for line in inp:
        for j, c in enumerate(line):
            cols[j].append(int(c))
    return cols

def p1():

    cols = get_cols(1)
    clapper = 0

    for _ in range(10):
        n = cols[clapper].pop(0)

        clapper = (clapper + 1) % len(cols)
        ix = (n - 1) % (2*len(cols[clapper]))

        if ix > len(cols[clapper]):
            ix = len(cols[clapper]) - ix


        cols[clapper].insert(ix, n)

    print(f"part 1: {''.join(str(c[0]) for c in cols)}")

def p2_3(part):
    from collections import defaultdict
    cols = get_cols(part)
    clapper = 0

    seen = defaultdict(int)

    round = 0
    while True:
        round += 1
        n = cols[clapper].pop(0)

        clapper = (clapper + 1) % len(cols)
        ix = (n - 1) % (2*len(cols[clapper]))

        if ix > len(cols[clapper]):
            ix = len(cols[clapper]) - ix


        cols[clapper].insert(ix, n)
        num = int(''.join(str(c[0]) for c in cols))
        seen[num] += 1
        if seen[num] == 2024:
            if part == 2:
                print(f"part 2: {round*num}")
            elif part == 3:
                print(f"part 3: {max(seen)}")
            return
p1()
p2_3(2)
p2_3(3)

