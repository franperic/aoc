map = [list(x.strip()) for x in open('2022/input/12.txt').readlines()]

def bfs(start):
    queue, seen = [[start]], {start}
    while queue:
        path = queue.pop(0)
        i, j = path[-1]
        if map[i][j] in "E":
            return path
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < len(map) and 0 <= y < len(map[0]) and f(map[x][y]) - f(map[i][j]) < 2 and (x, y) not in seen:
                queue.append(path + [(x, y)])
                seen.add((x, y))

f = lambda x: ord(x) if x not in 'SE' else ord('a') if x == 'S' else ord('z')
for part in ['S', 'aS']:
    starts = [(i, j) for j in range(len(map[0])) for i in range(len(map)) if map[i][j] in part]
    print(min(len(path) - 1 for s in starts if (path := bfs(s)) is not None))