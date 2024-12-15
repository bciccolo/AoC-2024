FILE = 'day15.dat'

grid = []
instructions = []
robot_x = 0
robot_y = 0

def calculate_gps_values():
    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                total += 100 * y + x

    return total


def find_robot():
    global robot_x, robot_y

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                robot_x = x
                robot_y = y
                return


def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    blank = False
    for line in lines:
        line = line.strip()

        if line == '':
            blank = True
            continue

        row = list(line)
        if not blank:
            grid.append(row)
        else:
            instructions.extend(row)


def push_up():
    # Find the first an opening starting going up from current position (skip the block immediately above)
    opening_y = 0
    for y in range(robot_y - 2, 0, -1):
        if grid[y][robot_x] == '#':
            return

        if grid[y][robot_x] == '.':
            opening_y = y
            break

    # "Shift" the boxes by swapping the first box with the first opening
    if opening_y > 0:
        grid[opening_y][robot_x] = 'O'
        grid[robot_y - 1][robot_x] = '.'


def push_down():
    # Find the first an opening starting going down from current position (skip the block immediately below)
    opening_y = 0
    for y in range(robot_y + 2, len(grid)):
        if grid[y][robot_x] == '#':
            return

        if grid[y][robot_x] == '.':
            opening_y = y
            break

    # "Shift" the boxes by swapping the first box with the first opening
    if opening_y > 0:
        grid[opening_y][robot_x] = 'O'
        grid[robot_y + 1][robot_x] = '.'


def push_left():
    # Find the first an opening starting going down from current position (skip the block immediately below)
    opening_x = 0
    for x in range(robot_x - 2, 0, -1):
        if grid[robot_y][x] == '#':
            return

        if grid[robot_y][x] == '.':
            opening_x = x
            break

    # "Shift" the boxes by swapping the first box with the first opening
    if opening_x > 0:
        grid[robot_y][opening_x] = 'O'
        grid[robot_y][robot_x - 1] = '.'


def push_right():
    # Find the first an opening starting going down from current position (skip the block immediately below)
    opening_x = 0
    for x in range(robot_x + 2, len(grid[robot_y])):
        if grid[robot_y][x] == '#':
            return

        if grid[robot_y][x] == '.':
            opening_x = x
            break

    # "Shift" the boxes by swapping the first box with the first opening
    if opening_x > 0:
        grid[robot_y][opening_x] = 'O'
        grid[robot_y][robot_x + 1] = '.'


def run_instructions():
    global robot_x, robot_y

    for movement in instructions:
        # Up
        if movement == '^':
            if grid[robot_y - 1][robot_x] == 'O':
                push_up()

            if grid[robot_y - 1][robot_x] == '.':
                grid[robot_y - 1][robot_x] = '@'
                grid[robot_y][robot_x] = '.'
                robot_y -= 1

        # Down
        elif movement == 'v':
            if grid[robot_y + 1][robot_x] == 'O':
                push_down()

            if grid[robot_y + 1][robot_x] == '.':
                grid[robot_y + 1][robot_x] = '@'
                grid[robot_y][robot_x] = '.'
                robot_y += 1

        # Left
        elif movement == '<':
            if grid[robot_y][robot_x - 1] == 'O':
                push_left()

            if grid[robot_y][robot_x - 1] == '.':
                grid[robot_y][robot_x - 1] = '@'
                grid[robot_y][robot_x] = '.'
                robot_x -= 1

        # Right
        elif movement == '>':
            if grid[robot_y][robot_x + 1] == 'O':
                push_right()

            if grid[robot_y][robot_x + 1] == '.':
                grid[robot_y][robot_x + 1] = '@'
                grid[robot_y][robot_x] = '.'
                robot_x += 1


load_data()
find_robot()

# for row in grid:
#     print(''.join(row))
# print(instructions)
# print(robot_y, robot_x)

run_instructions()

# for row in grid:
#     print(''.join(row))

print('Part 1: ' + str(calculate_gps_values()))