import argparse

parser = argparse.ArgumentParser('You stink', usage='Gay')
parser.add_argument('--input', help='Input file')
parser.add_argument('--output', help='Output file')

args = parser.parse_args()

with open(args.input, 'r', encoding='utf-8') as f:
    data = f.read()
    data = data.split(',')
    data = [int(x) for x in data]

c = sum(data)

with open(args.output, 'w', encoding='utf-8') as f:
    f.write(str(c))

print()