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

DO = "do()"
DONT = "don't()"
include = True
sum = 0
for line in lines:
    line = line.strip()
    do = True
    i = 0
    for i in range(len(line)):
        letter = line[i]

        if letter == 'd':
            if i + len(DO) < len(line) and line[i:i + len(DO)] == DO:
                include = True
            if i + len(DONT) < len(line) and line[i:i + len(DONT)] == DONT:
                include = False
        if letter == 'm' and include:
            match = re.search(r"mul\(\d{1,3},\d{1,3}\)", line[i:])
            if match.span()[0] == 0:
                factors = [int(x) for x in match.group()[4:-1].split(',')]
                sum += factors[0] * factors[1]

        i += 1

print('Part 2: '  + str(sum))