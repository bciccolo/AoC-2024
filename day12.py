import copy

FILE = 'day12.dat'

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
                    if method:
                        total += calculate_region_price_perimeter(plots_copy, plant + str(region_index))
                    else:
                        total += calculate_region_price_sides(plots_copy, plant + str(region_index))
                    region_index += 1

    return total


def calculate_region_price_perimeter(map, plant):
    area = 0
    perimeter = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == plant:
                area += 1
                perimeter += 4

                # Check up
                if y > 0 and map[y - 1][x] == plant:
                    perimeter -= 1

                # Check down
                if y < len(map) - 1 and map[y + 1][x] == plant:
                    perimeter -= 1

                # Check left
                if x > 0 and map[y][x - 1] == plant:
                    perimeter -= 1

                # Check right
                if x < len(map[y]) - 1 and map[y][x + 1] == plant:
                    perimeter -= 1

    price = area * perimeter
    # print('A region of ' + plant + ' plants with price ' + str(area) + ' * ' + str(perimeter) + ' = ' + str(price))

    return price

def calculate_region_price_sides(map, plant):
    return 0

def map_region(map, plant, index, y, x):
    map[y][x] = plant + str(index)

    # Check up
    if y > 0 and map[y - 1][x] == plant:
        map_region(map, plant, index, y - 1, x)

    # Check down
    if y < len(map) - 1 and map[y + 1][x] == plant:
        map_region(map, plant, index, y + 1, x)

    # Check left
    if x > 0 and map[y][x - 1] == plant:
        map_region(map, plant, index, y, x - 1)

    # Check right
    if x < len(map[y]) - 1 and map[y][x + 1] == plant:
        map_region(map, plant, index, y, x + 1)


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