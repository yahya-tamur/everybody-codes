from problem import *

def part1():
    i = int(get_input(1))
    from math import ceil, sqrt

    sqi = ceil(sqrt(i))
    return (2*sqi-1)*(sqi*sqi - i)

def part2():
    i = int(get_input(2))
    total = 1
    width = 3
    thickness = 1
    while True:
        thickness = (thickness*i) % 1111
        total += thickness*width
        width += 2
        if total > 20240000:
            return (total - 20240000)*(width - 2)

def part3():
    ACC, MAX = 10, 202400000
    inp = int(get_input(3))
    total = 1
    width = 1
    cols = [0 for _ in range(ACC)]
    cols[1] += 1
    thickness = 1

    while True:
        thickness = ((thickness*inp) % ACC) + ACC
        cols = [cols[(i-thickness)%ACC] for i in range(ACC)]
        width += 2
        total += width*thickness
        rem = sum(((i*2*width) % ACC)*val for i, val in enumerate(cols))
        cols[thickness % len(cols)] += 2
        if total - rem > MAX:
            return total - rem - MAX

for i in range(1, 4): eval(f"print(f'part {i}: {{part{i}()}}')")
