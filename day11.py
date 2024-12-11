FILE = 'day11-snippet.dat'

def blink(iterations):
    file = open(FILE, 'r')
    lines = file.readlines()
    stones = [int(x) for x in lines[0].strip().split()]

    # print(stones)

    for i in range(iterations):
        print(i)
        next = []
        for stone in stones:
            if stone == 0:
                next.append(1)
            elif len(str(stone)) % 2 == 0:
                stone_string = str(stone)
                middle = len(stone_string) // 2
                next.append(int(stone_string[:middle]))
                next.append(int(stone_string[middle:]))
            else:
                next.append(stone * 2024)
        stones = next

        print(stones)

    return len(stones)

print("Part 1: " + str(blink(25)))
# print("Part 2: " + str(blink(75)))
