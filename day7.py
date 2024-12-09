import itertools

FILE = 'day7.dat'

def validate_equation(answer, numbers, operators):
    combinations = list(itertools.product(operators, repeat=len(numbers) - 1))
    for combination in combinations:
        index = 0
        result = numbers[index]
        for operator in combination:
            index += 1
            if operator == 0: # add
                result += numbers[index]
            elif operator == 1: # multiply
                result *= numbers[index]
            else: # concatenate
                result = int(str(result) + str(numbers[index]))

        if result == answer:
            return True

    return False


file = open(FILE, 'r')
lines = file.readlines()

part_1 = 0
part_2 = 0
for line in lines:
    line = line.strip()
    components = line.split(':')
    answer = int(components[0])
    numbers = [int(x) for x in components[1].split()]

    if validate_equation(answer, numbers, [0, 1]):
        part_1 += answer

    if validate_equation(answer, numbers, [0, 1, 2]):
        part_2 += answer

file.close()

print('Part 1: '  + str(part_1))
print('Part 2: '  + str(part_2))