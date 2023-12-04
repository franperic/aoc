import re

with open("2023/inputs/3.txt") as f:
    content = [line.rsplit()[0] for line in f]


def get_horizontal(string):
    pattern_ahead = re.compile("(\d+)(?=[^\w\.])")
    pattern_behind = re.compile("(?<=[^\w\.])(\d+)")
    ahead = re.findall(pattern_ahead, string)
    behind = re.findall(pattern_behind, string)
    all = ahead + behind

    pattern = re.compile("(?<=[^\w\.])(\d+)(?=[^\w\.])")
    both = re.findall(pattern, string)

    if len(both) != 0:
        for num in both:
            all.remove(num)

    return all


def verify_diagonals(string, start, end):
    if start == 0:
        string = string[start : end + 1]
    elif len(string) < end + 1:
        string = string[start - 1 : end]
    else:
        string = string[start - 1 : end + 1]
    pattern = re.compile("[^\w\.]")
    symbols = re.findall(pattern, string)
    if len(symbols) > 0:
        return True
    else:
        return False


numbers = []
example = content
for i, line in enumerate(example):
    line = example[i]
    numbers_horizontal = get_horizontal(line)

    pattern = re.compile("\d+")
    check = re.finditer(pattern, line)
    numbers_vertical = []
    for number in check:
        if number.group() in numbers_horizontal:
            continue

        start = number.start()
        end = number.end()

        if i != 0:
            up = example[i - 1]
        else:
            up = "..." * 50
        if i != (len(example) - 1):
            down = example[i + 1]
        else:
            down = "..." * 50

        if verify_diagonals(up, start, end) or verify_diagonals(down, start, end):
            numbers_vertical.append(number.group())

    numbers += numbers_vertical + numbers_horizontal

sum([int(number) for number in numbers])


# test_custom = [
#     "467....114",
#     "...*.....*",
#     "..35..633.",
#     "...*..#...",
#     "617.300...",
#     "...*.+.58.",
#     "..592.....",
#     "......755.",
#     "....*.....",
#     "111....111",
# ]

# test_steps = content[23:28]

# test = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

# test2 = [
#     "12.......*..",
#     "+.........34",
#     ".......-12..",
#     "..78........",
#     "..*....60...",
#     "78..........",
#     ".......23...",
#     "....90*12...",
#     "............",
#     "2.2......12.",
#     ".*.........*",
#     "1.1.......56",
# ]

# test3 = [
#     "12.......*..",
#     "+.........34",
#     ".......-12..",
#     "..78........",
#     "..*....60...",
#     "78.........9",
#     ".5.....23..$",
#     "8...90*12...",
#     "............",
#     "2.2......12.",
#     ".*.........*",
#     "1.1..503+.56",
# ]

# test4 = [
#     ".......5......",
#     "..7*..*.....4*",
#     "...*13*......9",
#     ".......15.....",
#     "..............",
#     "..............",
#     "..............",
#     "..............",
#     "..............",
#     "..............",
#     "21............",
#     "...*9.........",
# ]

# test5 = ["100", "200"]
