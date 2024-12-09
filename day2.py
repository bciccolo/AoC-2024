FILE = 'day2.dat'

def safe_report(levels):
    increasing = levels[1] - levels[0] > 0
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff < 0 and increasing:
            return False
        elif diff > 0 and not increasing:
            return False
        elif abs(diff) == 0 or abs(diff) > 3:
            return False

    return True


file = open(FILE, 'r')
lines = file.readlines()

part1_count = 0
part2_count = 0
for line in lines:
    levels = [int(x) for x in line.strip().split()]
    if safe_report(levels):
        part1_count += 1
        part2_count += 1
    else:
        for i in range(len(levels)):
            copy = levels.copy()
            copy.pop(i)
            if safe_report(copy):
                part2_count += 1
                break

print('Part 1: '  + str(part1_count))
print('Part 2: '  + str(part2_count))
