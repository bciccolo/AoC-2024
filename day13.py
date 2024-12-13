FILE = 'day13.dat'

def calculate_cost(a_x, a_y, b_x, b_y, p_x, p_y):
    matrix = [
        [a_x, b_x, p_x],
        [a_y, b_y, p_y]
    ]

    matrix[0] = [i * -a_y for i in matrix[0]]
    matrix[1] = [i * a_x for i in matrix[1]]

    b_coeffient = matrix[0][1] + matrix[1][1]
    answer = matrix[0][2] + matrix[1][2]
    b = answer / b_coeffient
    a = (p_x - (b * b_x)) / a_x

    if answer % b_coeffient == 0 and (p_x - (b * b_x)) % a_x == 0:
        return 3 * a + b

    return 0


tokens_1 = 0
tokens_2 = 0

file = open(FILE, 'r')
lines = file.readlines()

for i in range(0, len(lines), 4):
    # parse the data
    x, y = lines[i].strip().split(':')[1].split(',')
    a_x = int(x.split('+')[1])
    a_y = int(y.split('+')[1])

    x, y = lines[i + 1].strip().split(':')[1].split(',')
    b_x = int(x.split('+')[1])
    b_y = int(y.split('+')[1])

    x, y = lines[i + 2].strip().split(':')[1].split(',')
    p_x = int(x.split('=')[1])
    p_y = int(y.split('=')[1])

    # calculate cost
    tokens_1 += calculate_cost(a_x, a_y, b_x, b_y, p_x, p_y)
    tokens_2 += calculate_cost(a_x, a_y, b_x, b_y, p_x + 10000000000000, p_y + 10000000000000)

file.close()

print("Part 1: " + str(int(tokens_1)))
print("Part 2: " + str(int(tokens_2)))