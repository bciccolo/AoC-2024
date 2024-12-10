FILE = 'day9.dat'

def compact_files(disk_layout):
    last_index = 0
    for j in range(len(disk_layout) - 1, -1, -1):
        if disk_layout[j] != '.':
            last_index = j
            break

    # for i in range(len(disk_layout)):
    i = 0
    while i < last_index:
        if disk_layout[i] == '.':
            temp = disk_layout[i]
            disk_layout[i] = disk_layout[last_index]
            disk_layout[j] = temp

            for j in range(last_index - 1, -1, -1):
                if disk_layout[j] != '.':
                    last_index = j
                    break
        i += 1

    return disk_layout


def expand_disk_layout(disk_map):
    disk_layout = []

    file = True
    file_id = 0
    for item in disk_map:
        for i in range(item):
            if file:
                disk_layout.append(file_id)
            else:
                disk_layout.append('.')

        if file:
            file_id += 1
        file = not file

    return disk_layout


def get_checksum(disk_layout):
    checksum = 0

    index = 0
    for digit in disk_layout:
        if digit == '.':
            break
        checksum += int(digit) * index
        index += 1

    return checksum


def load_disk_map():
    file = open(FILE, 'r')
    lines = file.readlines()
    line = lines[0].strip()
    disk_map = [int(digit) for digit in line]
    file.close()
    return disk_map


disk_map = load_disk_map()
print(len(disk_map)) # 20,000 elements, could result in 180,000 elements in full layout

disk_layout = expand_disk_layout(disk_map)
print(''.join(map(str, disk_layout)))

disk_layout = compact_files(disk_layout)
print(''.join(map(str, disk_layout)))

print('Part 1: '  + str(get_checksum(disk_layout)))