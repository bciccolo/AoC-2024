import copy
from pprint import pprint

FILE = 'day12-snippet.dat'

plants = set()
plots = []

def calculate_price(method):
    total = 0

    for plant in plants:

        plots_copy = copy.deepcopy(plots)
        region_index = 0
        for y in range(len(plots_copy)):
            for x in range(len(plots_copy[y])):
                if plots_copy[y][x] == plant:
                    map_region(plots_copy, plant, region_index, y, x)
                    # pprint(plots_copy)

                    area = 0
                    corners = 0
                    perimeter = 0
                    for r in range(len(plots_copy)):
                        for c in range(len(plots_copy[r])):
                            if plots_copy[r][c].startswith(plant + str(region_index)):
                                area += 1
                                corners += int(plots_copy[r][c][-3:-2])
                                perimeter += int(plots_copy[r][c][-1:])

                    # print('A region of ' + plant + ' plants with price ' + str(area) + ' * ' + str(perimeter) + ' = ' + str(area * perimeter))
                    # print('A region of ' + plant + ' plants with price ' + str(area) + ' * ' + str(corners) + ' = ' + str(area * corners))

                    if method:
                        total += area * perimeter
                    else:
                        total += area * corners

                    region_index += 1

    return total


def map_region(map, plant, index, y, x):
    map[y][x] = plant + str(index)

    left = False
    right = False
    down = False
    dr = False
    dl = False
    up = False
    ur = False
    ul = False

    # Check up
    if y > 0:
        if map[y - 1][x] == plant:
            map_region(map, plant, index, y - 1, x)

        if map[y - 1][x].startswith(plant):
            up = True
        if x > 0 and map[y - 1][x - 1].startswith(plant):
            ul = True
        if x < len(map[y]) - 1 and map[y - 1][x + 1].startswith(plant):
            ur = True

    # Check down
    if y < len(map) - 1:
        if map[y + 1][x] == plant:
            map_region(map, plant, index, y + 1, x)

        if map[y + 1][x].startswith(plant):
            down = True
        if x > 0 and map[y + 1][x - 1].startswith(plant):
            dl = True
        if x < len(map[y]) - 1 and map[y + 1][x + 1].startswith(plant):
            dr = True

    # Check left
    if x > 0:
        if map[y][x - 1] == plant:
            map_region(map, plant, index, y, x - 1)
        if map[y][x - 1].startswith(plant):
            left = True

    # Check right
    if x < len(map[y]) - 1:
        if map[y][x + 1] == plant:
            map_region(map, plant, index, y, x + 1)
        if map[y][x + 1].startswith(plant):
            right = True

    corners = 0

    if (up and left and not ul) or (not up and not left):
        corners += 1

    if (up and right and not ur) or (not up and not right):
        corners += 1

    if (down and left and not dl) or (not down and not left):
        corners += 1

    if (down and right and not dr) or (not down and not right):
        corners += 1

    perimeter = 4

    if up:
        perimeter -= 1

    if down:
        perimeter -= 1

    if left:
        perimeter -= 1

    if right:
        perimeter -= 1

    map[y][x] += '.' + str(corners) + '.' + str(perimeter)


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        row = list(line)
        plants.update(row)
        plots.append(row)

    file.close()


load_data()

print("Part 1: " + str(calculate_price(True)))
print("Part 2: " + str(calculate_price(False)))