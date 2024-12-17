import copy
import time

FILE = 'day16.dat'

grid = []
attempts = []
best_vector_points = dict()
lowest_cost = 1_000_000_000_000 # Part 1: 200,000 is too high; 50,000 is too low

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Attempt:
    def __init__(self, vector, visited, points):
        self.vector = vector
        self.visited = copy.deepcopy(visited)
        self.points = points


def find_start():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                return (y, x)


def follow_maze(attempt):
    global lowest_cost

    y = attempt.vector[0]
    x = attempt.vector[1]
    direction = attempt.vector[2]
    visited = attempt.visited
    points = attempt.points

    while grid[y][x] != 'E' and points < lowest_cost:
        if (y, x) in visited:
            break
        visited.add((y, x))

        current_vector = (y, x, direction)
        if current_vector in best_vector_points.keys() and best_vector_points[current_vector] < points:
            break
        best_vector_points[current_vector] = points

        # Turn counter-clockwise
        if direction == UP and grid[y][x - 1] != '#':
            vector = (y, x - 1, LEFT)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))
        elif direction == LEFT and grid[y + 1][x] != '#':
            vector = (y + 1, x,DOWN)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))
        elif direction == DOWN and grid[y][x + 1] != '#':
            vector = (y, x + 1, RIGHT)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))
        elif direction == RIGHT and grid[y - 1][x] != '#':
            vector = (y - 1, x, UP)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))

        # Turn clockwise
        if direction == UP and grid[y][x + 1] != '#':
            vector = (y, x + 1, RIGHT)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))
        elif direction == RIGHT and grid[y + 1][x] != '#':
            vector = (y + 1, x, DOWN)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))
        elif direction == DOWN and grid[y][x - 1] != '#':
            vector = (y, x - 1, LEFT)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))
        elif direction == LEFT and grid[y - 1][x] != '#':
            vector = (y - 1, x, UP)
            if vector not in best_vector_points.keys() or best_vector_points[vector] > points + 1001:
                attempts.append(Attempt(vector, visited, points + 1001))

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
        if points < lowest_cost:
            lowest_cost = points
            print(lowest_cost)


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        grid.append(list(line))


load_data()
y, x = find_start()
attempts.append(Attempt((y, x, RIGHT), set(), 0))

start = time.time()
while len(attempts) > 0:
    attempt = attempts.pop(0)

    vector = attempt.vector
    if attempt.points > lowest_cost or (vector in best_vector_points.keys() and best_vector_points[vector] < attempt.points):
        continue
    best_vector_points[vector] = attempt.points

    follow_maze(attempt)

duration = round(time.time() - start, 4)
print('Run time: ' + str(duration) + ' seconds')
print('Part 1: ' + str(lowest_cost))