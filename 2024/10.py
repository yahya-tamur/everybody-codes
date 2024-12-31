from problem import *


def part12(part):
    inp = get_input(part).split('\n')

    def run(N, M):

        cols = [{inp[N+i][M+j] for i in (0,1,6,7)} for j in (2,3,4,5)]
        rows = [{inp[N+i][M+j] for j in (0,1,6,7)} for i in (2,3,4,5)]

        word = ''.join((cols[i%4] & rows[i//4]).pop() for i in range(16))

        return sum((i+1)*(ord(c)-ord('A')+1) for i, c in enumerate(word))

    return sum(run(N, M) for N in range(0, len(inp), 9) for M in range(0, len(inp[0]), 9))

print(f"part 1: {part12(1)}")
print(f"part 2: {part12(2)}")

inp = [list(x) for x in get_input(3).split('\n')]

puzzles = {(N, M) for N in range(0, len(inp)-2, 6) for M in range(0, len(inp[0])-2, 6)}

def colsrows(N, M):
    return [[inp[N+i][M+j] for i in (0,1,6,7)] for j in (2,3,4,5)], \
            [[inp[N+i][M+j] for j in (0,1,6,7)] for i in (2,3,4,5)]

def inner_colsrows(N, M):
    return [[inp[N+i][M+j] for i in (2,3,4,5)] for j in (2,3,4,5)], \
            [[inp[N+i][M+j] for j in (2,3,4,5)] for i in (2,3,4,5)]

# if the same character is in multiple cols or multiple rows (including the same
# row/col twice), discard that puzzle.
for (N, M) in list(puzzles):
    cols, rows = colsrows(N, M)
    ac = ''.join(''.join(col) for col in cols)
    if len(set(ac) - {'?'}) != 16 - ac.count('?'):
        puzzles.discard((N, M))
    ac = ''.join(''.join(row) for row in rows)
    if len(set(ac) - {'?'}) != 16 - ac.count('?'):
        puzzles.discard((N, M))

ans = 0

# repeating this twice was enough to solve all the puzzles.
for _ in range(2):
    for (N, M) in list(puzzles):
        cols, rows = colsrows(N, M)

        # if there's an intersection, fill inner
        for i in range(16):
            if inp[N+2+(i//4)][M+2+(i%4)] != '.':
                continue
            s = (set(cols[i%4]) & set(rows[i//4])) - {'?'}
            if s:
                c, = s
                inp[N+2+(i//4)][M+2+(i%4)] = c

        # if there's one option left in the inner, fill that
        icols, irows = inner_colsrows(N, M)
        for i in range(16):
            if inp[N+2+(i//4)][M+2+(i%4)] != '.':
                continue
            s = set(rows[i//4]) - set(irows[i//4]) - {'?'}
            if len(s) == 1:
                c, = s
                inp[N+2+(i//4)][M+2+(i%4)] = c
            s = set(cols[i%4]) - set(icols[i%4]) - {'?'}
            if len(s) == 1:
                c, = s
                inp[N+2+(i//4)][M+2+(i%4)] = c

        # fill question marks if there's one option
        cols, rows = colsrows(N, M)
        icols, irows = inner_colsrows(N, M)
        for i in range(16):
            if cols[i//4][i%4] != '?':
                continue
            s = set(icols[i//4]) - set(cols[i//4]) - {'.'}
            if len(s) == 1:
                c, = s
                inp[N+[0,1,6,7][i%4]][M+2+(i//4)] = c
        for i in range(16):
            if rows[i//4][i%4] != '?':
                continue
            s = set(irows[i//4]) - set(rows[i//4]) - {'.'}
            if len(s) == 1:
                c, = s
                inp[N+2+(i//4)][M+[0,1,6,7][i%4]] = c

        _, irows = inner_colsrows(N, M)
        if all('.' not in irow for irow in irows):
            word = ''.join(''.join(irow) for irow in irows)

            ans += sum((i+1)*(ord(c)-ord('A')+1) for i, c in enumerate(word))
            puzzles.discard((N, M))


print(f"part 3: {ans}")
