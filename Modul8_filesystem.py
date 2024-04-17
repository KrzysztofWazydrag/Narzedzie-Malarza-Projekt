import argparse
from os import walk
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='Find Files',
    description='Find and resize files',
    epilog='Author: Kacper Sieradziński'
)
parser.add_argument('--dir')
parser.add_argument('--extension')
arguments = parser.parse_args()

for path, _ , photos in walk(arguments.dir):
    for photo in photos:
        source = Path(f'{path}\\{photo}')
        if source.suffix == '.jpg':
            print(source.absolute())