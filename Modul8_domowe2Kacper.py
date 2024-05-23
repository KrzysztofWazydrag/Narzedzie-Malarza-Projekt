from os import walk

with open('venv/scalone.txt', 'w') as output:
    for path, dirs, files in walk('source'):
        for file in files:
            if file.endswith('txt'):
                filename = f'{path}/{file}'
                with open(filename) as source:
                    output.write('\n'.join(source.readlines()))
                    output.write('\n')
