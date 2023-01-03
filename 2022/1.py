with open('2022/input/1.txt') as fp:
    contents = fp.readlines()

calories = [content.removesuffix("\n") for content in contents]

carrying = []
elf = []
for item in calories:
    if item == "":
        carrying.append(elf)
        elf = []
        continue
    elf.append(int(item))
    


elf_carrying = [sum(elf) for elf in carrying]
# Part 1
max(elf_carrying)
# Part 2
sum(sorted(elf_carrying)[-3:])
