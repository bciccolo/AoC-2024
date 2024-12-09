FILE = 'day6-snippet.dat'

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
    while True:
        grid[y][x] = 'X'

        if direction == UP:
            if y == 0:
                return
            if grid[y - 1][x] == '#':
                direction = RIGHT
            else:
                y -= 1

        elif direction == DOWN:
            if y == len(grid) - 1:
                return
            if grid[y + 1][x] == '#':
                direction = LEFT
            else:
                y += 1

        elif direction == RIGHT:
            if x == len(grid[y]) - 1:
                return
            if grid[y][x + 1] == '#':
                direction = DOWN
            else:
                x += 1

        elif direction == LEFT:
            if x == 0:
                return
            if grid[y][x - 1] == '#':
                direction = UP
            else:
                x -= 1


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        grid.append(list(line))

    file.close()


load_data()
follow_path()

for row in grid:
    print("".join(row))

count = 0
for row in grid:
    count += row.count('X')

print('Part 1: '  + str(count))
print('Part 2: '  + str(0))