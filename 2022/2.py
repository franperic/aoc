with open("2022/input/2.txt") as f:
    strategy = [line.rstrip('\n') for line in f]

def get_first(input):
    score = {"X": 1, "Y": 2, "Z": 3}
    return score[input]

def get_second(input):
    score = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3,
    }
    return score[input]

def get_score(input):
    first = get_first(input[2])
    second = get_second(input)

    return first + second

# Part 1
scores = [get_score(game) for game in strategy]
sum(scores)

# Part 2
def get_first_adj(input):
    score = {
        "A X": 3,
        "A Y": 1,
        "A Z": 2,
        "B X": 1,
        "B Y": 2,
        "B Z": 3,
        "C X": 2,
        "C Y": 3,
        "C Z": 1,
    }
    return score[input]

def get_second_adj(input):
    score = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    return score[input]

def get_score(input):
    first = get_first_adj(input)
    second = get_second_adj(input[2])

    return first + second


scores = [get_score(game) for game in strategy]
sum(scores)