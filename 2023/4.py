import re

with open("2023/inputs/4.txt") as f:
    content = [line.rstrip() for line in f]


def get_score(x):
    score = 0
    for i in range(1, x + 1):
        if i == 1:
            score = 1
            continue
        else:
            score *= 2
    return score


def process_ticket(input):
    table_row = input.split("|")
    winning = table_row[0].split(":")[1]
    mine = table_row[1]

    number_pattern = re.compile("\d+")
    winning = re.findall(number_pattern, winning)
    mine = re.findall(number_pattern, mine)

    counter = 0
    for number in mine:
        if number in winning:
            counter += 1

    return get_score(counter)


points = [process_ticket(line) for line in content]
sum(points)


def update_tickets(tickets, winning_n, card):
    times = tickets[card]
    for i in range(1, winning_n + 1):
        tickets[card + i] = tickets[card + i] + times
    return tickets


tickets = {i + 1: 1 for i in range(len(content))}

for input in content:
    table_row = input.split("|")
    winning = table_row[0].split(":")[1]
    card = table_row[0].split(":")[0]
    mine = table_row[1]

    number_pattern = re.compile("\d+")
    card = re.findall(number_pattern, card)[0]
    winning = re.findall(number_pattern, winning)
    mine = re.findall(number_pattern, mine)

    counter = 0
    for number in mine:
        if number in winning:
            counter += 1

    tickets = update_tickets(tickets, counter, int(card))

total = 0
for n in tickets.values():
    total += n
