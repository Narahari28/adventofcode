def val(character):
    if str(character).isnumeric():
        return 1000000000000
    if character == 'S':
        return 0
    elif character == 'E':
        return 25
    else:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        return alpha.index(character)

def valid_squares(grid, i, j, prev_total, vals):
    squares = []
    if i > 0:
        if vals[i-1][j] == -1 and val(grid[i - 1][j]) <= val(grid[i][j]) + 1:
            squares.append([i-1, j, prev_total + 1])
    if j > 0:
        if vals[i][j-1] == -1 and val(grid[i][j - 1]) <= val(grid[i][j]) + 1:
            squares.append([i, j-1, prev_total + 1])
    if i < len(grid) - 1:
        if vals[i+1][j] == -1 and val(grid[i + 1][j]) <= val(grid[i][j]) + 1:
            squares.append([i+1, j, prev_total + 1])
    if j < len(grid[0]) - 1:
        if vals[i][j+1] == -1 and val(grid[i][j+1]) <= val(grid[i][j]) + 1:
            squares.append([i, j+1, prev_total + 1])
    return squares

def valid_squares2(grid, i, j, prev_total, vals):
    squares = []
    if i > 0:
        if (vals[i-1][j] == -1 or vals[i-1][j] > prev_total + 1) and val(grid[i - 1][j]) <= val(grid[i][j]) + 1:
            squares.append([i-1, j, prev_total + 1])
    if j > 0:
        if (vals[i][j-1] == -1 or vals[i][j-1] > prev_total + 1) and val(grid[i][j - 1]) <= val(grid[i][j]) + 1:
            squares.append([i, j-1, prev_total + 1])
    if i < len(grid) - 1:
        if (vals[i+1][j] == -1 or vals[i+1][j] > prev_total + 1) and val(grid[i + 1][j]) <= val(grid[i][j]) + 1:
            squares.append([i+1, j, prev_total + 1])
    if j < len(grid[0]) - 1:
        if (vals[i][j+1] == -1 or vals[i][j+1] > prev_total + 1) and val(grid[i][j+1]) <= val(grid[i][j]) + 1:
            squares.append([i, j+1, prev_total + 1])
    return squares

def calc(grid):
    seen = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    vals = [[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
    cur_x = -1
    cur_y = -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                cur_x = i
                cur_y = j
                vals[i][j] = 0
                break
    queue = [[cur_x, cur_y, 0]]
    cnt = 0
    while len(queue) > 0:
        cur = queue.pop(0)
        cur_x = cur[0]
        cur_y = cur[1]
        prev_total = cur[2]
        print("Prev: " + str(cur_x) + " " + str(cur_y) + " " + str(prev_total), flush=True)
        dests = valid_squares(grid, cur_x, cur_y, prev_total, vals)
        print("Dests: " + str(dests), flush=True)
        for val in dests:
            if grid[val[0]][val[1]] == 'E':
                return val[2]
            if vals[val[0]][val[1]] == -1:
                vals[val[0]][val[1]] = val[2]
                queue.append(val)
        cnt += 1
        for row in grid:
            print(row, flush=True)
        print("Queue: " + str(queue), flush=True)

def calc2(grid):
    seen = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    vals = [[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
    queue = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S' or grid[i][j] == 'a':
                vals[i][j] = 0
                queue.append([i, j, 0])
    cnt = 0
    while len(queue) > 0:
        cur = queue.pop(0)
        cur_x = cur[0]
        cur_y = cur[1]
        prev_total = cur[2]
        print("Prev: " + str(cur_x) + " " + str(cur_y) + " " + str(prev_total), flush=True)
        dests = valid_squares2(grid, cur_x, cur_y, prev_total, vals)
        print("Dests: " + str(dests), flush=True)
        for val in dests:
            if grid[val[0]][val[1]] == 'E':
                return val[2]
            if vals[val[0]][val[1]] == -1:
                vals[val[0]][val[1]] = val[2]
                queue.append(val)
        cnt += 1
        for row in vals:
            print(row, flush=True)
        print("Queue: " + str(queue), flush=True)

def p1():
    with open('hill_climbing.txt') as f:
        lines = f.readlines()
        grid = []
        ans = 0
        for line in lines:
            split_line = [x for x in line.strip()]
            grid.append(split_line)
        ans = calc(grid)
        print(ans, flush=True)

def p2():
    with open('hill_climbing.txt') as f:
        lines = f.readlines()
        grid = []
        ans = 0
        for line in lines:
            split_line = [x for x in line.strip()]
            grid.append(split_line)
        ans = calc2(grid)
        print(ans, flush=True)

if __name__ == "__main__":
    p2()