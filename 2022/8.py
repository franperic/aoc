with open("2022/input/8.txt") as f:
    grid = [line.rstrip() for line in f]

def get_left(row, col):
    return [int(digit) for digit in grid[row][:col]]

def get_right(row, col):
    return [int(digit) for digit in grid[row][col+1:]]

def get_top(row, col):
    sub_grid = grid[:row]
    return [int(row[col]) for row in sub_grid]

def get_bottom(row, col):
    sub_grid = grid[row+1:]
    return [int(row[col]) for row in sub_grid]

def get_visible(row, col):
    height = int(grid[row][col])

    left = get_left(row, col)
    comparison = [digit < height for digit in left]
    if sum(comparison) == len(left):
        return 1
    
    right = get_right(row, col)   
    comparison = [digit < height for digit in right]
    if sum(comparison) == len(right):
        return 1
    
    top = get_top(row, col)
    comparison = [digit < height for digit in top]
    if sum(comparison) == len(top):
            return 1

    bottom = get_bottom(row, col)
    comparison = [digit < height for digit in bottom]
    if sum(comparison) == len(bottom):
        return 1
    
    else:
        return 0

# visible trees on the edges
edge = len(grid)
edges = edge + 2*(edge - 1) + (edge-2)

# visible tree on the interior of the grid
interior_grid = [i+1 for i in range(len(grid)-2)]
interior_visible = [get_visible(row, col) for row in interior_grid for col in interior_grid]

# Part 1
print(edges + sum(interior_visible))

# Part 2

def get_scenic_score(row, col):
    height = int(grid[row][col])

    left = get_left(row, col)
    for i in range(len(left)):
        if left[::-1][i] >= height:
            left_score = i+1
            break
    if "left_score" not in locals():
        left_score = len(left)

    right = get_right(row, col)   
    for i in range(len(right)):
        if right[i] >= height:
            right_score = i+1
            break
    if "right_score" not in locals():
        right_score = len(right) 
    
    top = get_top(row, col)
    for i in range(len(top)):
        if top[::-1][i] >= height:
            top_score = i+1
            break
    if "top_score" not in locals():
        top_score = len(top)

    bottom = get_bottom(row, col)
    for i in range(len(bottom)):
        if bottom[i] >= height:
            bottom_score = i+1
            break
    if "bottom_score" not in locals():
        bottom_score = len(bottom)

    return left_score * right_score * top_score * bottom_score

# Part 2
interior_score = [get_scenic_score(row, col) for row in interior_grid for col in interior_grid]
print(max(interior_score))