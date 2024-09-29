import argparse

parser = argparse.ArgumentParser('You stink', usage='Gay')
parser.add_argument('--input', help='Input file')
parser.add_argument('--output', help='Output file')
parser.add_argument('--check', help='WTF')

args = parser.parse_args()

with open(args.output, 'w', encoding='utf-8') as f:
    f.write('Anyad')

print()