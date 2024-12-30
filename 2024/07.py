from problem import get_input, clip

dd = {'=': 0, '+': 1, '-': -1, 'S': 0}

def decode_track(track):
    grid = dict()
    for i, line in enumerate(track.split('\n')):
        for j, c in enumerate(line):
            if c != ' ':
                grid[i+1j*j] = c
    path = [grid[1j]]
    prev = 0
    loc = 1j
    while path[-1] != 'S':
        for d in (1, -1, 1j, -1j):
            if loc+d != prev and loc+d in grid:
                prev = loc
                loc += d
                path.append(grid[loc])
                break

    return [dd[x] for x in path]

tracks = [None, [0], decode_track(\
"""S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""), \
        decode_track(\
"""S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-""")]

def eval_line(dds, loops, track):
    dds  = [dd[x] for x in dds]
    val, total = 10, 0
    for x in range(loops*len(track)):
        z = track[x % len(track)]
        val += dds[x % len(dds)] if z == 0 else z
        total += val
    return total

# requires: |dds| dividing |loops|
def fast_eval_line(dds, loops, track):
    n = len(dds)
    l0 = 0
    l1 = eval_line(dds, n, track)
    l2 = eval_line(dds, 2*n, track)
    a = (l2 - 2*l1) // 2
    b = l1 - a
    k = loops // len(dds)

    return a*k*k + b*k

def part12(part):
    names, scores = [], []
    for line in get_input(part).split('\n'):
        l, r = line.split(':')
        names.append(l)
        scores.append(-eval_line(r.split(','), 10, tracks[part]))

    return ''.join(x[1] for x in sorted(zip(scores, names)))

print(f"part 1: {part12(1)}")
print(f"part 2: {part12(2)}")

ref = fast_eval_line(get_input(3).split(':')[1].split(','), 2024, tracks[3])

a3 = 0

from itertools import combinations
for c1 in combinations(range(11), 6):
    for c2 in combinations(range(6), 3):
        l = ['+' for _ in range(11)]
        for x in c1:
            l[x] = '='
        for x in c2:
            l[c1[x]] = '-'
        a3 += fast_eval_line(l, 2024, tracks[3]) > ref

print(f"part 3: {a3}")
