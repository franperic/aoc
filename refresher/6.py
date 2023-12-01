with open("refresher/6.txt") as input:
    content = input.readline()[:-1]

for i in range(len(content)):
    if len(set(content[i : i + 4])) == 4:
        print(i+4)
        break

