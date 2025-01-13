from problem import *

def p1():
    a = 0
    m = 0
    for ch in get_input(1).split(','):
        z = int(ch[1:])
        match ch[0]:
            case 'U':
                a += z
            case 'D':
                a -= z
        m = max(a, m)

    print(m)

seen = set()
words = []
for line in get_input(2).split('\n'):
    x, y, z = 0, 0, 0

    for ch in line.split(','):

        dx, dy, dz = {'U': (1,0,0),'D':(-1,0,0),'L':(0,1,0), \
                'R':(0,-1,0),'F':(0,0,1),'B':(0,0,-1)}[ch[0]]
        for _ in range(int(ch[1:])):
            seen.add((x,y,z))
            x += dx
            y += dy
            z += dz
        seen.add((x,y,z))


for i in range(-10, 10):
    for j in range(-10, 10):
        print('#' if (i,j,0) in seen else ' ', end='')
    print()
print(len(seen)-1)

