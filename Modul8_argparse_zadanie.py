import argparse

parser = argparse.ArgumentParser(
    prog = 'Image bulk resizer',
    description = 'It can resize all images in specific directory',
    epilog = 'Author: Krzysztof Wazydrag'
)

parser.add_argument('path', type=str)
parser.add_argument('target', type=str)
parser.add_argument('--width', type=str, default=300)
parser.add_argument('--height', type=str, default=300)

arguments =  parser.parse_args()
print('path', arguments.path)
print('target', arguments.target)
print('width', arguments.width)
print('height', arguments.height)
