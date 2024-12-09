import re

FILE = 'day3.dat'

file = open(FILE, 'r')
lines = file.readlines()

p = re.compile(r"mul")

sum = 0
for line in lines:
    line = line.strip()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    for match in matches:
        factors = [int(x) for x in match[4:-1].split(',')]
        sum += factors[0] * factors[1]

print('Part 1: '  + str(sum))