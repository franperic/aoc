import re

with open("2023/inputs/1.txt") as input:
    content = [line.strip() for line in input]


def get_calibration(string):
    digits = re.findall(r"\d", string)
    return int(digits[0] + digits[-1])


calibration_values = [get_calibration(input) for input in content]
# A
sum(calibration_values)


# B
def get_calibration_2(string):
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "\d",
    ]

    pattern = re.compile("(?=({}))".format("|".join(numbers)))
    digits = re.findall(pattern, string)
    first = digits[0]
    last = digits[-1]

    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    try:
        int(first)
    except:
        first = mapping[first]

    try:
        int(last)
    except:
        last = mapping[last]

    return int(first + last)


calibration_values = [get_calibration_2(input) for input in content]
sum(calibration_values)
