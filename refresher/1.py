# get a list of lists where each list is split by a new line from 1.txt file
with open("refresher/1.txt") as input:
    content = [line.strip() for line in input]

cal = []
elves = []
for line in content:
    if line == "":
        elves.append(cal)
        cal = []
        continue
    else:
        cal.append(int(line))

carrying = [sum(elf) for elf in elves]
max(carrying)

carrying = sorted(carrying)
sum(carrying[-3:])
