from pprint import pprint

with open("2022/input/10.txt") as f:
    instructions = [instruction.rstrip() for instruction in f]

def processing_signal(inputs):
    cycle = 0
    cycle_history = [cycle]
    signal = 1
    signal_history = [signal]

    for i, v in enumerate(inputs):
        instruction = v.split()
        if instruction[0] == "addx":
            for _ in range(2):
                cycle += 1
                cycle_history.append(cycle)
                signal_history.append(signal)
            signal += int(instruction[1])
            
        else:
            cycle += 1
            cycle_history.append(cycle)
            signal_history.append(signal)
    
    return cycle_history, signal_history

# Part 1
cycle, signal = processing_signal(instructions)

result = 0
for c, s in zip(cycle[20::40], signal[20::40]):
    result += c*s
print(result)

# Part 2
crt = ""
crt_position = [0, 0]
for s in signal[1:]:
    sprite_position = [s-1, s, s+1]
    if crt_position[0] in sprite_position:
        crt += "#"
    else:
        crt += "."
    crt_position[0] += 1
    if crt_position[0] == 40:
        crt += "\n"
        crt_position[0] = 0
        crt_position[1] += 1

pprint(crt.split())
# EHPZPJGL
