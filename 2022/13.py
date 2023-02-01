pairs = [trunc_line for line in open("2022/input/13.txt").readlines() if (trunc_line := line.strip())]

def checker(l, r):
    # print(l, r)
    if isinstance(l, int) & isinstance(r, int):
        if l <= r:
            return True
        else:
            return False
    elif isinstance(l, int) & isinstance(r, list):
        return checker(l, r[0])
    elif isinstance(l, list) & isinstance(r, int):
        return checker(l[0], r)
    elif isinstance(l, list) & isinstance(r, list):
        for ll, rr in zip(l, r):
            if not checker(ll, rr):
                return False
        return True


total = []
for left, right in zip(pairs[::2], pairs[1::2]):
    print(left, right)
    results = []
    left = eval(left)
    right = eval(right)
    
    if len(left) > len(right):
        results.append(False)  
        total.append(results)  
        continue

    for l,r in zip(left, right):
        results.append(checker(l, r))
    print(results)    
    total.append(results)

indices = []
for i, pair in enumerate(total):
    if any(v is False for v in pair):
        indices.append(i)
sum(indices)



left = [[3,[[10,2,8],3,0,[2,1],7]],[[[1,9,5,5,8],1,9,[9,2,4,5]],2,1,[[],[4,3],3]],[],[7,[6,4,[7,0,5]],[],[8],1]]
right = [[3],[],[[4,4],[[5,4,3],10,[1,3,9],9],3,1],[6,[0,[9,0,1,1,1]]],[]]

len(left)
len(right)