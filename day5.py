from pprint import pprint

AFTER = 1
BEFORE = 0
FILE = 'day5.dat'

rules = []
jobs = []

def load_data():
    file = open(FILE, 'r')
    lines = file.readlines()

    blank = False
    for line in lines:
        line = line.strip()

        if line == '':
            blank = True
            continue

        if blank:
            pages = [int(x) for x in line.split(',')]
            jobs.append(pages)
        else:
            rule = [int(x) for x in line.split('|')]
            rules.append(rule)

    file.close()


def fix_job(job):
    # print('original: ' + str(job))
    for i in range(len(job)):
        number = job[i]
        for rule in rules:
            if rule[BEFORE] == number and rule[AFTER] in job[:i]:
                # put the AFTER immediately after number
                job.remove(rule[AFTER])
                job.insert(i + 1, rule[AFTER])
            elif rule[AFTER] == number and rule[BEFORE] in job[i + 1:]:
                # put the BEFORE immediately before number
                job.remove(rule[BEFORE])
                job.insert(i, rule[BEFORE])

    # print('fixed:    ' + str(job))


def validate_job(job):
    for i in range(len(job)):
        number = job[i]
        for rule in rules:
            if rule[BEFORE] == number and rule[AFTER] in job[:i]:
                return False
            elif rule[AFTER] == number and rule[BEFORE] in job[i + 1:]:
                return False

    return True


load_data()
# pprint(rules)
# pprint(jobs)

part_1 = 0
part_2 = 0
for job in jobs:
    if validate_job(job):
        part_1 += job[len(job) // 2]
    else:
        while True:
            fix_job(job)
            if validate_job(job):
                break
        part_2 += job[len(job) // 2]


print('Part 1: '  + str(part_1))
print('Part 2: '  + str(part_2))