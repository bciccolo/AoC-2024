import copy

FILE = 'day16-snippet-b.dat'

grid = []
path_values = []
attempts = []
attempted_vectors = dict()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

X = 0
Y = 1
DIRECTION = 2

class Attempt:
    def __init__(self, vector, visited, points):
        self.vector = vector
        self.visited = copy.deepcopy(visited)
        self.points = points


def find_start():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                return (x, y)


def follow_maze(attempt):
    y = attempt.vector[Y]
    x = attempt.vector[X]
    direction = attempt.vector[DIRECTION]
    visited = attempt.visited
    points = attempt.points

    while grid[y][x] != 'E':
        if (x, y, direction) in visited:
            break

        visited.add((x, y, direction))

        # Turn counter-clockwise
        if direction == UP and grid[y][x - 1] != '#':
            vector = (x, y, LEFT)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))
        elif direction == LEFT and grid[y + 1][x] != '#':
            vector = (x, y, DOWN)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))
        elif direction == DOWN and grid[y][x + 1] != '#':
            vector = (x, y, RIGHT)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))
        elif direction == RIGHT and grid[y - 1][x] != '#':
            vector = (x, y, UP)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))

        # Turn clockwise
        if direction == UP and grid[y][x + 1] != '#':
            vector = (x, y, RIGHT)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))
        elif direction == RIGHT and grid[y + 1][x] != '#':
            vector = (x, y, DOWN)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))
        elif direction == DOWN and grid[y][x - 1] != '#':
            vector = (x, y, LEFT)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))
        elif direction == LEFT and grid[y - 1][x] != '#':
            vector = (x, y, UP)
            if vector not in visited:
                attempts.append(Attempt(vector, visited, points + 1000))

        # Move forward
        if direction == UP:
            if grid[y - 1][x] == '#':
                break
            else:
                y -= 1
        elif direction == RIGHT:
            if grid[y][x + 1] == '#':
                break
            else:
                x += 1
        elif direction == DOWN:
            if grid[y + 1][x] == '#':
                break
            else:
                y += 1
        elif direction == LEFT:
            if grid[y][x - 1] == '#':
                break
            else:
                x -= 1

        points += 1

    if grid[y][x] == 'E':
        path_values.append(points)


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        grid.append(list(line))


load_data()

start = find_start()
attempts.append(Attempt((start[X], start[Y], RIGHT), set(), 0))
while len(attempts) > 0:
    attempt = attempts.pop()

    vector = attempt.vector
    if vector in attempted_vectors.keys():
        if attempted_vectors[vector] < attempt.points:
            continue
    attempted_vectors[vector] = attempt.points

    follow_maze(attempt)

print('Part 1: ' + str(min(path_values)))