from problem import *

inp = get_input(2).split('\n')

i, j = next((i, j) for i in range(len(inp)) for j in range(len(inp[0])) \
        if inp[i][j] == 'A')

target = j - i
print(target)

ans = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 'T':
            ans += (1 + ((j - i - target) % 3))*((j - i - target) // 3)
        if inp[i][j] == 'H':
            ans += 2*(1 + ((j - i - target) % 3))*((j - i - target) // 3)

clip(ans)


