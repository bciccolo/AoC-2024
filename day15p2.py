FILE = 'day15.dat'

NO_FIT = -1
FIT = 0

grid = []
instructions = []
robot_x = 0
robot_y = 0

def calculate_gps_values():
    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '[':
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

        if not blank:
            row = []
            for item in list(line):
                if item == 'O':
                    row.append('[')
                    row.append(']')
                elif item == '@':
                    row.append('@')
                    row.append('.')
                else:
                    row.append(item)
                    row.append(item)
            grid.append(row)
        else:
            instructions.extend(list(line))


def check_fit(pieces, y, start_x):
    # No fit
    x = start_x
    for x in range(len(pieces)):
        if pieces[x] == '#':
            return NO_FIT
        if pieces[x] != '.' and grid[y][start_x + x] == '#':
            return NO_FIT

    # Fit
    openings = 0
    x = start_x
    for x in range(len(pieces)):
        if pieces[x] != '.' and grid[y][start_x + x] == '.':
            openings += 1
    if openings == len(pieces):
        return FIT

    # Possible fit
    range_start = start_x
    if grid[y][range_start] == ']':
        range_start -= 1

    range_end = start_x + len(pieces) - 1
    if grid[y][range_end] == '[':
        range_end += 1

    return (range_start, grid[y][range_start:range_end + 1])


def push_up_broken(start_x):
    pieces = ['[', ']']
    pieces_by_level = []
    starts_by_level = []

    # Find the first an opening starting going up from current position (skip the block immediately above)
    for y in range(robot_y - 2, -1, -1):
        pieces_by_level.append(pieces)
        starts_by_level.append(start_x)
        fit = check_fit(pieces, y, start_x)
        if fit == NO_FIT:
            return
        elif fit == FIT:
            break
        else:
            start_x = fit[0]
            pieces = fit[1]

    # Shift each row up
    for i in range(len(pieces_by_level)):
        # Clear the space from the row that's moving up in the next iteration
        if i < len(pieces_by_level) - 1:
            above_start = starts_by_level[i + 1]
            above_end = above_start + len(pieces_by_level[i + 1])
            for j in range(above_start, above_end):
                grid[robot_y - (i + 2)][j] = '.'

        # Move this row up
        pieces = pieces_by_level[i]
        x = starts_by_level[i]
        for piece in pieces:
            grid[robot_y - (i + 2)][x] = piece
            x += 1

    # Clear original box
    grid[robot_y - 1][starts_by_level[0]] = '.'
    grid[robot_y - 1][starts_by_level[0] + 1] = '.'


def push_down_broken(start_x):
    pieces = ['[', ']']
    pieces_by_level = []
    starts_by_level = []

    # Find the first an opening starting going down from current position (skip the block immediately below)
    for y in range(robot_y + 2, len(grid)):
        pieces_by_level.append(pieces)
        starts_by_level.append(start_x)
        fit = check_fit(pieces, y, start_x)
        if fit == NO_FIT:
            return
        elif fit == FIT:
            break
        else:
            start_x = fit[0]
            pieces = fit[1]

    # Shift each row down
    for i in range(len(pieces_by_level)):
        # Clear the space from the row that's moving down in the next iteration
        if i < len(pieces_by_level) - 1:
            above_start = starts_by_level[i + 1]
            above_end = above_start + len(pieces_by_level[i + 1])
            for j in range(above_start, above_end):
                grid[robot_y + (i + 2)][j] = '.'

        # Move this row down
        pieces = pieces_by_level[i]
        x = starts_by_level[i]
        for piece in pieces:
            grid[robot_y + (i + 2)][x] = piece
            x += 1

    # Clear original box
    grid[robot_y + 1][starts_by_level[0]] = '.'
    grid[robot_y + 1][starts_by_level[0] + 1] = '.'


def push_up(columns):
    columns_by_level = []

    # Find the first an opening starting going down from current position (skip the block immediately below)
    for y in range(robot_y - 2, -1, -1):
        columns_by_level.append(columns)
        next_columns = []
        for column in columns:
            if grid[y][column] == '#':
                return
            if grid[y][column] == '.':
                continue
            if grid[y][column] == grid[y + 1][column]:
                next_columns.append(column)
            elif grid[y][column] == ']': # grid[y + 1][column] == '['
                next_columns.append(column - 1)
                next_columns.append(column)
            elif grid[y][column] == '[': # grid[y + 1][column] == ']'
                next_columns.append(column)
                next_columns.append(column + 1)

        if len(next_columns) == 0:
            break

        columns = next_columns

    # Shift each row up
    entrance_row = robot_y - len(columns_by_level) - 1
    exit_row = entrance_row + 1

    for i in range(len(columns_by_level) - 1, -1, -1):
        columns = columns_by_level[i]

        # Move this row up
        for j in range(len(columns)):
            column = columns[j]
            if j % 2 == 0:
                grid[entrance_row][column] = '['
            else:
                grid[entrance_row][column] = ']'

        # Clear the space from the row we're exiting
        for column in columns:
            grid[exit_row][column] = '.'

        entrance_row += 1
        exit_row += 1


def push_down(columns):
    columns_by_level = []

    # Find the first an opening starting going down from current position (skip the block immediately below)
    for y in range(robot_y + 2, len(grid)):
        columns_by_level.append(columns)
        next_columns = []
        for column in columns:
            if grid[y][column] == '#':
                return
            if grid[y][column] == '.':
                continue
            if grid[y][column] == grid[y - 1][column]:
                next_columns.append(column)
            elif grid[y][column] == ']': # grid[y - 1][column] == '['
                next_columns.append(column - 1)
                next_columns.append(column)
            elif grid[y][column] == '[': # grid[y - 1][column] == ']'
                next_columns.append(column)
                next_columns.append(column + 1)

        if len(next_columns) == 0:
            break

        columns = next_columns

    # Shift each row down
    entrance_row = robot_y + len(columns_by_level) + 1
    exit_row = entrance_row - 1

    for i in range(len(columns_by_level) - 1, -1, -1):
        columns = columns_by_level[i]

        # Move this row down
        for j in range(len(columns)):
            column = columns[j]
            if j % 2 == 0:
                grid[entrance_row][column] = '['
            else:
                grid[entrance_row][column] = ']'

        # Clear the space from the row we're exiting
        for column in columns:
            grid[exit_row][column] = '.'

        entrance_row -= 1
        exit_row -= 1


def push_left():
    # HERE
    # Find the first an opening starting going down from current position (skip the block immediately to the left)
    opening_x = 0
    for x in range(robot_x - 2, 1, -1):
        if grid[robot_y][x] == '#':
            return

        if grid[robot_y][x] == '.':
            opening_x = x
            break

    # Shift the boxes one space each
    if opening_x > 0:
        for x in range(opening_x, robot_x):
            grid[robot_y][x] = grid[robot_y][x + 1]
        grid[robot_y][robot_x - 1] = '.'


def push_right():
    # HERE
    # Find the first an opening starting going down from current position (skip the block immediately to the right)
    opening_x = 0
    for x in range(robot_x + 2, len(grid[robot_y]) - 1):
        if grid[robot_y][x] == '#':
            return

        if grid[robot_y][x] == '.':
            opening_x = x
            break

    # Shift the boxes one space each
    if opening_x > 0:
        for x in range(opening_x, robot_x, - 1):
            grid[robot_y][x] = grid[robot_y][x - 1]
        grid[robot_y][robot_x + 1] = '.'


def run_instructions():
    global robot_x, robot_y

    count = 0
    for movement in instructions:
        # print('Instruction ' + str(count) + ': ' + movement)
        # Up
        count += 1
        if movement == '^':
            if grid[robot_y - 1][robot_x] == '[':
                push_up([robot_x, robot_x + 1])
            elif grid[robot_y - 1][robot_x] == ']':
                push_up([robot_x - 1, robot_x])

            if grid[robot_y - 1][robot_x] == '.':
                grid[robot_y - 1][robot_x] = '@'
                grid[robot_y][robot_x] = '.'
                robot_y -= 1

        # Down
        elif movement == 'v':
            if grid[robot_y + 1][robot_x] == '[':
                push_down([robot_x, robot_x + 1])
            if grid[robot_y + 1][robot_x] == ']':
                push_down([robot_x - 1, robot_x])

            if grid[robot_y + 1][robot_x] == '.':
                grid[robot_y + 1][robot_x] = '@'
                grid[robot_y][robot_x] = '.'
                robot_y += 1

        # Left
        elif movement == '<':
            if grid[robot_y][robot_x - 1] == ']':
                push_left()

            if grid[robot_y][robot_x - 1] == '.':
                grid[robot_y][robot_x - 1] = '@'
                grid[robot_y][robot_x] = '.'
                robot_x -= 1

        # Right
        elif movement == '>':
            if grid[robot_y][robot_x + 1] == '[':
                push_right()

            if grid[robot_y][robot_x + 1] == '.':
                grid[robot_y][robot_x + 1] = '@'
                grid[robot_y][robot_x] = '.'
                robot_x += 1

        # for row in grid:
        #     print(''.join(row))



load_data()
find_robot()

# for row in grid:
#     print(''.join(row))
# print(instructions)
# print(robot_y, robot_x)

run_instructions()

# for row in grid:
#     print(''.join(row))

print('Part 2: ' + str(calculate_gps_values()))