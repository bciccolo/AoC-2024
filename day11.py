FILE = 'day11.dat'

def add_or_update(dictionary, value, count):
    if value in dictionary.keys():
        dictionary[value] += count
    else:
        dictionary[value] = count


def blink(stones, iterations):
    stone_counts = dict()
    for stone in stones:
        stone_counts[stone] = 1

    for i in range(iterations):
        next = dict()
        for stone, count in stone_counts.items():
            if stone == 0:
                add_or_update(next, 1, count)
            elif len(str(stone)) % 2 == 0:
                stone_string = str(stone)
                middle = len(stone_string) // 2
                add_or_update(next, int(stone_string[:middle]), count)
                add_or_update(next, int(stone_string[middle:]), count)
            else:
                add_or_update(next, stone * 2024, count)

        stone_counts = next
        # print(stone_counts)

    total = sum(stone_counts.values())

    return total


file = open(FILE, 'r')
lines = file.readlines()
stones = [int(x) for x in lines[0].strip().split()]

print("Part 1: " + str(blink(stones, 25)))
print("Part 2: " + str(blink(stones, 75)))