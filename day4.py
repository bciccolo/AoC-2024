from pprint import pprint

FILE = 'day4.dat'
grid = []

def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        row = list(line)
        grid.append(row)

    file.close()


def find_neighbors(y, x, letter):
    coordinates = []

    # Check row above
    if y > 0:
        if grid[y - 1][x] == letter:
            coordinates.append([y - 1, x])
        if x > 1 and grid[y - 1][x - 1] == letter:
            coordinates.append([y - 1, x - 1])
        if x < len(grid[y - 1]) - 1 and grid[y - 1][x + 1] == letter:
            coordinates.append([y - 1, x + 1])

    # Check row of
    if x > 1 and grid[y][x - 1] == letter:
        coordinates.append([y, x - 1])
    if x < len(grid[y]) - 1 and grid[y][x + 1] == letter:
        coordinates.append([y, x + 1])

    # Check row below
    if y < len(grid) - 1:
        if grid[y + 1][x] == letter:
            coordinates.append([y + 1, x])
        if x > 1 and grid[y + 1][x - 1] == letter:
            coordinates.append([y + 1, x - 1])
        if x < len(grid[y + 1]) - 1 and grid[y + 1][x + 1] == letter:
            coordinates.append([y + 1, x + 1])

    return coordinates


def find_xmas():
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
                # Forward
                if x < len(grid[y]) - 3 and \
                    grid[y][x + 1] == 'M' and \
                    grid[y][x + 2] == 'A' and \
                    grid[y][x + 3] == 'S':
                    count += 1

                # Backward
                if x >= 3 and \
                    grid[y][x - 1] == 'M' and \
                    grid[y][x - 2] == 'A' and \
                    grid[y][x - 3] == 'S':
                    count += 1

                # Up
                if y >= 3 and \
                    grid[y - 1][x] == 'M' and \
                    grid[y - 2][x] == 'A' and \
                    grid[y - 3][x] == 'S':
                    count += 1

                # Down
                if y < len(grid) - 3 and \
                    grid[y + 1][x] == 'M' and \
                    grid[y + 2][x] == 'A' and \
                    grid[y + 3][x] == 'S':
                    count += 1

                # Up-right
                if y >= 3 and \
                    x < len(grid[y]) - 3 and \
                    grid[y - 1][x + 1] == 'M' and \
                    grid[y - 2][x + 2] == 'A' and \
                    grid[y - 3][x + 3] == 'S':
                    count += 1

                # Up-left
                if y >= 3 and \
                    x >= 3 and \
                    grid[y - 1][x - 1] == 'M' and \
                    grid[y - 2][x - 2] == 'A' and \
                    grid[y - 3][x - 3] == 'S':
                    count += 1

                # Down-right
                if y < len(grid) - 3 and \
                    x < len(grid[y]) - 3 and \
                    grid[y + 1][x + 1] == 'M' and \
                    grid[y + 2][x + 2] == 'A' and \
                    grid[y + 3][x + 3] == 'S':
                    count += 1

                # Down-left
                if y + 3 < len(grid) and \
                    x >= 3 and \
                    grid[y + 1][x - 1] == 'M' and \
                    grid[y + 2][x - 2] == 'A' and \
                    grid[y + 3][x - 3] == 'S':
                    count += 1

    return count


def find_x_mas():
    count = 0

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == 'A':
                ul = grid[y - 1][x - 1]
                br = grid[y + 1][x + 1]

                ur = grid[y - 1][x + 1]
                bl = grid[y + 1][x - 1]

                if ((ul == 'S' and br == 'M') or (ul == 'M' and br == 'S')) and ((ur == 'S' and bl == 'M') or (ur == 'M' and bl == 'S')):
                    count += 1

    return count


# Not how part 1 works but cool nonetheless
def find_xmas_strands():
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
                m_coordinates = find_neighbors(y, x, 'M')
                print('X at ' + str(y) + "," + str(x) + ", found M: " + str(len(m_coordinates)) + " times " + str(m_coordinates))
                # pprint(coordinates)
                for m_coordinate in m_coordinates:
                    a_coordinates = find_neighbors(m_coordinate[0], m_coordinate[1], 'A')
                    print('M at ' + str(m_coordinate[0]) + "," + str(m_coordinate[1]) + ", found A: " + str(len(a_coordinates)) + " times " + str(a_coordinates))
                    for a_coordinate in a_coordinates:
                        s_coordinates = find_neighbors(a_coordinate[0], a_coordinate[1], 'S')
                        print('A at ' + str(a_coordinate[0]) + "," + str(a_coordinate[1]) + ", found S: " + str(len(s_coordinates)) + " times " + str(s_coordinates))
                        pprint(s_coordinates)
                        count += len(s_coordinates)

    return count


load_data()
# pprint(grid)
print('Part 1: '  + str(find_xmas()))
print('Part 2: '  + str(find_x_mas()))