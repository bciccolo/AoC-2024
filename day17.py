# Day 17 snippet data A
# register_a = 729
# register_b = 0
# register_c = 0
# instructions = [0,1,5,4,3,0]

# Day 17 snippet data B
# register_a = 2024
# register_b = 0
# register_c = 0
# instructions = [0,3,5,4,3,0]

# Day 17 full data
register_a = 44374556
register_b = 0
register_c = 0
instructions = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]

def combo(operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return register_a
    elif operand == 5:
        return register_b
    elif operand == 6:
        return register_c
    else:
        print('Invalid combo operand')

def run_program(replicate):
    global register_a, register_b, register_c

    output = []

    i = 0
    while i < len(instructions):
        opcode = instructions[i]
        operand = instructions[i + 1]

        if opcode == 0:
            numerator = register_a
            denominator = pow(2, combo(operand))
            register_a = int(numerator / denominator)

        elif opcode == 1:
            register_b = register_b ^ operand

        elif opcode == 2:
            register_b = combo(operand) % 8

        elif opcode == 3: # Jump
            if register_a != 0:
                i = operand
                continue

        elif opcode == 4:
            register_b = register_b ^ register_c

        elif opcode == 5:
            output.append(combo(operand) % 8)

            if replicate:
                if len(output) > len(instructions):
                    return []
                last_index = len(output) - 1
                if output[last_index] != instructions[last_index]:
                    return []

        elif opcode == 6:
            numerator = register_a
            denominator = pow(2, combo(operand))
            register_b = int(numerator / denominator)

        elif opcode == 7:
            numerator = register_a
            denominator = pow(2, combo(operand))
            register_c = int(numerator / denominator)

        i += 2

    return output


output = run_program(False)
print('Part 1: ' + ','.join([str(x) for x in output]))

min_value = 0
while True:
    register_a = min_value
    register_b = 0
    register_c = 0

    output = run_program(True)
    if len(output) == len(instructions):
        break

    if min_value % 1_000_000 == 0:
        print(min_value)

    min_value += 1

print('Part 2: ' + str(min_value)) # 20_020_000_000 is too low based on puzzle feedback
