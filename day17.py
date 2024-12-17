# Day 17 snippet data
# register_a = 729
# register_b = 0
# register_c = 0
# instructions = [0,1,5,4,3,0]

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

    elif opcode == 6:
        numerator = register_a
        denominator = pow(2, combo(operand))
        register_b = int(numerator / denominator)

    elif opcode == 7:
        numerator = register_a
        denominator = pow(2, combo(operand))
        register_c = int(numerator / denominator)

    i += 2

print('Part 1: ' + ','.join([str(x) for x in output]))