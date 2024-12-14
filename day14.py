# FILE = 'day14.dat'
# WIDTH = 101
# HEIGHT = 103

FILE = 'day14-snippet.dat'
WIDTH = 11
HEIGHT = 7

class Robot:
    def __init__(self, location, velocity):
        self.x = location[0]
        self.y = location[1]
        self.dx = velocity[0]
        self.dy = velocity[1]

    def move(self):
        self.x = (self.x + self.dx) % WIDTH
        self.y = (self.y + self.dy) % HEIGHT


def visualize(grid):
    for row in grid:
        for item in row:
            if item == 0:
                print('.', end='')
            else:
                print(item, end='')
        print()
    print()


robots = []

file = open(FILE, 'r')
lines = file.readlines()

for line in lines:
    parts = line.strip().split()
    origin = [int(x) for x in parts[0].split('=')[1].split(',')]
    velocity = [int(x) for x in parts[1].split('=')[1].split(',')]
    robots.append(Robot(origin, velocity))

for i in range(100):
    for robot in robots:
        robot.move()

grid=[]
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        row.append(0)
    grid.append(row)

for robot in robots:
    grid[robot.y][robot.x] += 1

visualize(grid)

mid_x = WIDTH // 2
mid_y = HEIGHT // 2

product = 1

# Quadrant 1
quadrant = 0
for y in range(mid_y):
    for x in range(mid_x):
        quadrant += grid[y][x]
product *= quadrant

# Quadrant 2
quadrant = 0
for y in range(mid_y):
    for x in range(mid_x + 1, WIDTH):
        quadrant += grid[y][x]
product *= quadrant

# Quadrant 3
quadrant = 0
for y in range(mid_y + 1, HEIGHT):
    for x in range(mid_x):
        quadrant += grid[y][x]
product *= quadrant

# Quadrant 4
quadrant = 0
for y in range(mid_y + 1, HEIGHT):
    for x in range(mid_x + 1, WIDTH):
        quadrant += grid[y][x]
product *= quadrant

print('Part 1: ' + str(product))
