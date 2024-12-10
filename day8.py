from pprint import pprint

FILE = 'day8-snippet.dat'
X = 1
Y = 0

grid = []
nodes = dict()

def check_bounds(y, x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        grid.append(list(line))

    file.close()


def find_nodes():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                if grid[y][x] in nodes.keys():
                    locations = nodes[grid[y][x]]
                else:
                    locations = []
                    nodes[grid[y][x]] = locations
                locations.append([y, x])


def count_antinodes(resonate):
    antinodes = []
    for row in grid:
        antinodes.append(list('.' * len(row)))

    for locations in nodes.values():
        for i in range(len(locations) - 1):
            for j in range(i + 1, len(locations)):
                node_1 = locations[i]
                node_2 = locations[j]
                dx = node_1[X] - node_2[X]
                dy = node_1[Y] - node_2[Y]

                # Antinode 1
                x = node_1[X]
                y = node_1[Y]
                if resonate:
                    while check_bounds(y, x):
                        antinodes[y][x] = 'X'
                        x += dx
                        y += dy
                else:
                    x += dx
                    y += dy
                    if check_bounds(y, x):
                        antinodes[y][x] = 'X'

                # Antinode 2
                x = node_2[X]
                y = node_2[Y]
                if resonate:
                    while check_bounds(y, x):
                        antinodes[y][x] = 'X'
                        x -= dx
                        y -= dy
                else:
                        x -= dx
                        y -= dy
                        if check_bounds(y, x):
                            antinodes[y][x] = 'X'

    count = 0
    for row in antinodes:
        count += row.count('X')

    return count


load_data()
find_nodes()

print('Part 1: '  + str(count_antinodes(False)))
print('Part 2: '  + str(count_antinodes(True)))