import re
from collections import defaultdict

with open("2022/input/7.txt") as f:
    output = [line.rstrip() for line in f]

sizes = defaultdict(int)
stack = []

for line in output:
    if line.startswith("$ ls") or line.startswith("dir"):
        continue
    if line.startswith("$ cd"):
        dest = line.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = line.split()
        for path in stack:
            sizes[path] += int(size)

def filter_dirs(size, value):
    # task 1: 100000
    if size <= value:
        return size
    else:
        return 0

def filter_dirs_greater(size, value):
    if size >= value:
        return size
    else:
        return 0

# Problem 1
task_1 = []
for size in sizes.values():
    task_1.append(filter_dirs(size, 100000))
sum(task_1)

# Problem 2
free_storage = 70000000 - sizes["/"]
needed_space = 30000000 - free_storage

for size in sorted(sizes.values()):
    if size > needed_space:
        print(size)
        break