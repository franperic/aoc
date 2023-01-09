import re

def get_items(line: str):
    line = line.replace("\n", "")
    line = line.replace("  Starting items: ", "")
    line = line.split(", ")
    return list(map(int, line))

def get_operation(line: str):
    line = line.replace("\n", "")
    if "old * old" in line:
        return "^", 2
    else:
        k, v = line.replace("  Operation: new = old ", "").split()
        return k, int(v) 

def get_test(line: str):
    line = line.replace("\n", "")
    return int(line.replace("  Test: divisible by ", ""))

def get_next(line: str):
    line = line.replace("\n", "")
    return int(line[-1:])
    

monkeys = {}
MONKEY_DIVISOR_CONSTANT = 1
with open("2022/input/11.txt") as f:
    for line in f:
        if "Monkey" in line:
            line = line.replace(":\n", "")
            monkey = int(line[-1:])
            monkeys[monkey] = {"items": [], "item_counter": 0, "operation": {"kind": [], "value": []}, "test": [], "pass": {True: [], False: []}}
        if "Starting" in line:
            monkeys[monkey]["items"] = get_items(line)
        if "Operation" in line:
            kind, value = get_operation(line)
            monkeys[monkey]["operation"]["kind"] = kind
            monkeys[monkey]["operation"]["value"] = value
        if "Test" in line:
            monkeys[monkey]["test"] = get_test(line)
            MONKEY_DIVISOR_CONSTANT *= get_test(line)
        if "true" in line:
            monkeys[monkey]["pass"][True] = get_next(line)
        if "false" in line:
            monkeys[monkey]["pass"][False] = get_next(line)

#def perform_playing(monkey: int, x)
for round in range(10_000):
    print(round)
    for monkey in range(len(monkeys)):
        for item in monkeys[monkey]["items"]:
            # update item counter
            monkeys[monkey]["item_counter"] += 1

            # update worrying level
            if "*" in monkeys[monkey]["operation"]["kind"]:
                item *= monkeys[monkey]["operation"]["value"]
            elif "^" in monkeys[monkey]["operation"]["kind"]:
                item *= item
            else:
                item += monkeys[monkey]["operation"]["value"]
            
            # relief
            item %= MONKEY_DIVISOR_CONSTANT

            # decision
            if item % monkeys[monkey]["test"] == 0:
               pass_to_monkey = monkeys[monkey]["pass"][True]
               monkeys[pass_to_monkey]["items"].append(item)
            else:
               pass_to_monkey = monkeys[monkey]["pass"][False]
               monkeys[pass_to_monkey]["items"].append(item)
            
        # refresh item list
        monkeys[monkey]["items"] = []

counter = []
for monkey in monkeys.values():
    counter.append(monkey["item_counter"])
counter = sorted(counter)
counter[-2] * counter[-1]