import re
from pprint import pprint

with open("2022/input/5.txt") as f:
    instruction = [move.rstrip() for move in f]

def transform_input(move):
    digits = re.findall("\d+", move)
    return [int(digit) for digit in digits]

instruction = [transform_input(move) for move in instruction]


class Crane:
    stacks = {
        1: [["F"], ["H"], ["B"], ["V"], ["R"], ["Q"], ["D"], ["P"]],
        2: [["L"], ["D"], ["Z"], ["Q"], ["W"], ["V"]],
        3: [["H"], ["L"], ["Z"], ["Q"], ["G"], ["R"], ["P"], ["C"]],
        4: [["R"], ["D"], ["H"], ["F"], ["J"], ["V"], ["B"]],
        5: [["Z"], ["W"], ["L"], ["C"]],
        6: [["J"], ["R"], ["P"], ["N"], ["T"], ["G"], ["V"], ["M"]],
        7: [["J"], ["R"], ["L"], ["V"], ["M"], ["B"], ["S"]],
        8: [["D"], ["P"], ["J"]], 
        9: [["D"], ["C"], ["N"], ["W"], ["V"]],
    }

    def __init__(self):
        pass

    def perform_move(self, move: list):
        n = move[0]
        _from = move[1]
        _to = move[2]
        stacks = self.stacks

        for _ in range(n):
            transit = stacks[_from].pop(-1)
            stacks[_to].append(list(transit))
        
        self.stacks = stacks


loading = Crane()
for move in instruction:
    print(move)
    loading.perform_move(move)
# Part 1
pprint(loading.stacks)
# JDTMRWCQJ