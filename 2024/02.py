from problem import *

inp = get_input(1).split('\n')

words = inp[0][len('WORDS:'):].split(',')

print(f"part 1: {sum(inp[2].count(word) for word in words)}")


inp = get_input(2).split('\n\n')
words = set()

for w in inp[0][len('WORDS:'):].split(','):
    words.add(w)
    words.add(w[::-1])

inp = inp[1]

ixs = set()

for i in range(len(inp)):
    for w in words:
        if inp[i:i+len(w)] == w:
            for j in range(i, i+len(w)):
                ixs.add(j)

print(f"part 2: {len(ixs)}")

inp = get_input(3).split('\n')
words = set()

for w in inp[0][len('WORDS:'):].split(','):
    words.add(w)
    words.add(w[::-1])

from collections import defaultdict
grid = defaultdict(lambda:'!')

n, m = 0, 0

for (i, line) in enumerate(inp[2:]):
    for (j, c) in enumerate(line):
        grid[i+1j*j] = c 
        m = j + 1
    n = i + 1

ixs = set()

for i in range(n):
    for j in range(m):
        for word in words:
            if all(grid[i + k + 1j*j] == c for (k, c) in enumerate(word)):
                for k in range(len(word)):
                    ixs.add(i + k + 1j*j)
            if all(grid[i+1j*((k+j) % m)] == c for (k, c) in enumerate(word)):
                for k in range(len(word)):
                    ixs.add(i + 1j*((k+j) % m))

print(f"part 3: {len(ixs)}")
