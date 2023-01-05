with open("2022/input/6.txt") as f:
    data = [data.rstrip() for data in f][0]

def validate_marker(input, size):
    unique_signal = set(input)
    if len(unique_signal) == size:
        return unique_signal
    else:
        return False

# Part 1
size = 4
for i in range(len(data)):
    marker = validate_marker(data[i:i+size], size)
    if marker != False:
        print(i+size)
        break

# Part 2
size = 14
for i in range(len(data)):
    marker = validate_marker(data[i:i+size], size)
    if marker != False:
        print(i+size)
        break
