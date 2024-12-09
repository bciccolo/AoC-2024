file = open('day1.dat', 'r')
lines = file.readlines()

left = []
right = []
for line in lines:
    parts = line.strip().split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

left.sort()
right.sort()

difference = 0
for i in range(len(left)):
    difference += abs(left[i] - right[i])

similarity = 0
for item in left:
    count = right.count(item)
    similarity += item * count

print('Part 1: '  + str(difference))
print('Part 2: '  + str(similarity))