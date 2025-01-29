from problem import *
def solve(part):
    inp = get_input(part).split('\n')

    right = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
    left = right[::-1]

    def rotate(g, z, d):
        lst = right if d == 'R' else left
        swp = g[z+lst[0]]

        for i in range(len(lst)-1):
            g[z+lst[i]] = g[z+lst[i+1]]

        g[z+lst[-1]] = swp


    instrs = inp[0]
    inp = inp[2:]

    def zero():
        m = dict()
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                m[i+1j*j] = i+1j*j
        return m

    m = zero()
    k = 0
    for i in range(1, len(inp)-1):
        for j in range(1, len(inp[0])-1):
            rotate(m, i+1j*j, instrs[k % len(instrs)])
            k += 1

    def times(m, n):
        ans = dict()
        for k in m:
            ans[k] = n[m[k]]
        return ans

    oo = zero()
    N = [-1, 1, 100, 1048576000][part]

    while N > 0:
        if N & 1:
            oo = times(m, oo)
        m = times(m, m)
        N >>= 1


    s = ''
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            z = oo[i+1j*j]
            s += inp[int(z.real)][int(z.imag)]
        s += '\n'
    #print(s)
    return s[s.find('>')+1:s.find('<')]

print(f"part 1: {solve(1)}")
print(f"part 2: {solve(2)}")
print(f"part 3: {solve(3)}")
