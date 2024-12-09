import copy
from pprint import pprint

FILE = 'day6.dat'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

X = 1
Y = 0

grid = []

def find_starting_point():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return [y, x]


def follow_path():
    y, x = find_starting_point()
    direction = UP

    counter = 0
    while counter < len(grid) * len(grid[Y]):
        grid[y][x] = 'X'

        if direction == UP:
            if y == 0:
                return True
            if grid[y - 1][x] == '#':
                direction = RIGHT
            else:
                y -= 1

        elif direction == DOWN:
            if y == len(grid) - 1:
                return True
            if grid[y + 1][x] == '#':
                direction = LEFT
            else:
                y += 1

        elif direction == RIGHT:
            if x == len(grid[y]) - 1:
                return True
            if grid[y][x + 1] == '#':
                direction = DOWN
            else:
                x += 1

        elif direction == LEFT:
            if x == 0:
                return True
            if grid[y][x - 1] == '#':
                direction = UP
            else:
                x -= 1

        counter += 1

    return False


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        grid.append(list(line))

    file.close()


load_data()
original = copy.deepcopy(grid)

# Part 1
follow_path()

count = 0
for row in grid:
    count += row.count('X')

print('Part 1: '  + str(count))

# Part 2 - this is grossly inefficient but it works (just wait ~50 seconds)
count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        grid = copy.deepcopy(original)
        if grid[y][x] == '.':
            grid[y][x] = '#'
            if not follow_path():
                count += 1

print('Part 2: '  + str(count))