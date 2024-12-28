import os, sys

if 'clip' in sys.argv:
    print('Populating input from clipboard.')
    import pyperclip as p
    with open('input', 'w') as input_file:
        input_file.write(p.paste())

numfile = lambda file: file.name[-3:] == ".py" and file.name[:-3].isdigit()
mtime = lambda file: file.stat().st_mtime

file = max((file for file in os.scandir() if numfile(file)), key=mtime)

text = open(file, 'r').read()
text = text.replace('get_input', 'get_input_')

exec(text)
