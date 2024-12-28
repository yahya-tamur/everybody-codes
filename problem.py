# remember to write code to create the niputs/year folders!!!!
import sys
import os
import pyperclip as p

def download_input(year=None, day=None, part=None):
    if year is None:
        numfile = lambda file: file.name[-3:] == ".py" and file.name[:-3].isdigit()
        mtime = lambda file: file.stat().st_mtime

        file = max((file for file in os.scandir() if numfile(file)), key=mtime)

        year = os.getcwd()[-4:]
        day = int(float(file.name[:-3])) # leading zeroes :)

    if part is None:
        try:
            part = sys.argv[1]
        except:
            print('call with part as the first argument')
            exit()

    print(f'year: {year} day: {day} part: {part}')
    print('Press enter to populate input from clipboard, Ctrl-C to not.')
    input()

    with open(f'../_inputs/{year}/{day}-{part}.txt', 'w') as file:
        file.write(p.paste())
    print('Done!')
    return p.paste()

def get_input(part):
    fullpath = (os.getcwd() + '/' + sys.argv[0]).split('/')
    year = int(fullpath[-2])
    day = int(fullpath[-1][:-3])

    if 'clip' in sys.argv or \
            f'{day}-{part}.txt' not in os.listdir(f'../_inputs/{year}'):
        return download_input(year, day, part)
    return open(f'../_inputs/{year}/{day}-{part}.txt', 'r').read()

def get_input_(_part):
    return open(f'./input', 'r').read()
    
def clip(arg):
    s = str(arg)
    p.copy(s)
    print('Copied: ', end='')
    print(s)

if __name__ == '__main__':
    download_input()
