import re

with open("2022/input/4.txt") as f:
    assignment = [task.rstrip() for task in f]

def get_digits(assignment):
    digits = re.findall("\d+", assignment)
    return [int(digit) for digit in digits]

def find_complete_overlap(assignment):
    if (assignment[0] >= assignment[2]) & (assignment[1] <= assignment[3]):
        return 1
    elif (assignment[0] <= assignment[2]) & (assignment[1] >= assignment[3]):
        return 1 
    else:
        return 0

num_assignments = [get_digits(task) for task in assignment]
# Part 1
overlap = [find_complete_overlap(task) for task in num_assignments]
sum(overlap)

# Part 2

def find_overlap(assignment):
    if (assignment[0] >= assignment[2]) & (assignment[1] <= assignment[3]):
        return 1
    elif (assignment[0] <= assignment[2]) & (assignment[1] >= assignment[3]):
        return 1 
    elif (
        (assignment[0] >= assignment[2])
        & (assignment[0] <= assignment[3])
        & (assignment[1] >= assignment[3])
    ):
        return 1
    elif (
        (assignment[0] <= assignment[2]) 
        & (assignment[1] >= assignment[2]) 
        & (assignment[1] <= assignment[3])
    ):
        return 1
    else:
        return 0

overlap = [find_overlap(task) for task in num_assignments]
sum(overlap)
