import itertools

FILE = 'day7-snippet.dat'

def validate_equation(answer, numbers):
    operators = len(numbers) - 1
    combinations = list(itertools.product([0, 1], repeat=operators))
    for combination in combinations:
        index = 0
        result = numbers[index]
        for operator in combination:
            index += 1
            if operator == 0: # add
                result += numbers[index]
            else: # multiple
                result *= numbers[index]

        if result == answer:
            return True

    return False


file = open(FILE, 'r')
lines = file.readlines()

sum = 0
for line in lines:
    line = line.strip()
    components = line.split(':')
    answer = int(components[0])
    numbers = [int(x) for x in components[1].split()]

    if validate_equation(answer, numbers):
        sum += answer

file.close()

print('Part 1: '  + str(sum))