FILE = 'day10.dat'

grid = []
complete_trails = 0

def count_trailheads():
    # last = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                follow_trail(y, x, 1, set())
                # print('Trailhead @ ' + str(y) + ',' + str(x) + ' has ' + str(complete_trails - last))
                # last = complete_trails


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        grid.append([int(x) for x in line])

    file.close()


def follow_trail(y, x, search_value, destinations):
    global complete_trails

    location = (y, x)
    if search_value == 10 and location not in destinations:
        complete_trails += 1
        destinations.add(location)
        return

    # Check up
    if y > 0 and grid[y - 1][x] == search_value:
        follow_trail(y - 1, x, search_value + 1, destinations)

    # Check left
    if x > 0 and grid[y][x - 1] == search_value:
        follow_trail(y, x - 1, search_value + 1, destinations)

    # Check right
    if x < len(grid[y]) - 1 and grid[y][x + 1] == search_value:
        follow_trail(y, x + 1, search_value + 1, destinations)

    # Check down
    if y < len(grid) - 1 and grid[y + 1][x] == search_value:
        follow_trail(y + 1, x, search_value + 1, destinations)


load_data()
count_trailheads()

print("Part 1: " + str(complete_trails))