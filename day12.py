FILE = 'day12-snippet.dat'

def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        row = list(line)
        grid.append(row)

    file.close()

grid = []
load_data()
print(grid)