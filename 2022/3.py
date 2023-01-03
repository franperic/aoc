import string

with open("2022/input/3.txt") as f:
    rucksack = [line.rstrip("\n") for line in f]

def get_overlap(content):
    half = int(len(content)/2)
    first_comp = content[:half]
    second_comp = content[half:]

    for letter in first_comp:
        if letter in second_comp:
            return letter

scoring = {}
for i, letter in enumerate(string.ascii_lowercase):
    scoring[letter] = i+1

for i, letter in enumerate(string.ascii_uppercase):
    scoring[letter] = i+27

# Part 1
overlap = [get_overlap(content) for content in rucksack]
prio = [scoring[letter] for letter in overlap]
sum(prio)

# Part 2
def get_badge(rucksack):
    overlap = []
    for letter in rucksack[0]:
        if letter in rucksack[1]:
            overlap.append(letter)
    for letter in overlap:
        if letter in rucksack[2]:
            return letter

badges = []
for i in range(100):
    group = i*3
    badge = get_badge(rucksack[group:group+3])
    badges.append(badge)

badge_prio = [scoring[letter] for letter in badges]
sum(badge_prio)