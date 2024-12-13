FILE = 'day13-snippet.dat'

tokens = 0

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
    

file.close()

print("Part 1: " + str(tokens))
print("Part 2: " + str(0))