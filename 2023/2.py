import re

with open("2023/inputs/2.txt") as file:
    content = [line.rstrip() for line in file]


def get_feasibility(string):
    pattern_red = re.compile("(\d+)\s(?=red)")
    pattern_green = re.compile("(\d+)\s(?=green)")
    pattern_blue = re.compile("(\d+)\s(?=blue)")
    patterns = [pattern_red, pattern_green, pattern_blue]

    colors = [0, 0, 0]
    for i, pattern in enumerate(patterns):
        cubes = re.findall(pattern, string)
        cubes = [int(cube) for cube in cubes]
        colors[i] = max(cubes)

    if colors[0] > 12:
        return False
    elif colors[1] > 13:
        return False
    elif colors[2] > 14:
        return False

    else:
        pattern = re.compile("(?<=Game\s)\d+")
        return int(re.findall(pattern, string)[0])


# A
sum([get_feasibility(game) for game in content])


# B
def get_power(string):
    pattern_red = re.compile("(\d+)\s(?=red)")
    pattern_green = re.compile("(\d+)\s(?=green)")
    pattern_blue = re.compile("(\d+)\s(?=blue)")
    patterns = [pattern_red, pattern_green, pattern_blue]

    colors = [0, 0, 0]
    for i, pattern in enumerate(patterns):
        cubes = re.findall(pattern, string)
        cubes = [int(cube) for cube in cubes]
        colors[i] = max(cubes)

    return colors[0] * colors[1] * colors[2]


sum([get_power(game) for game in content])
