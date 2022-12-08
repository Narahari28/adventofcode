def calc_max_from_lefts(grid):
    maxes = [row[:] for row in grid]
    for i in range(len(grid)):
        maxes[i][0] = -1
    for j in range(1, len(grid[i])):
        for i in range(len(grid)):
            maxes[i][j] = max(maxes[i][j-1], grid[i][j-1])
    return maxes

def calc_max_from_rights(grid):
    maxes = [row[:] for row in grid]
    for i in range(len(grid)):
        maxes[i][len(grid[i]) - 1] = -1
    for j in range(len(grid[0]) - 2, -1, -1):
        for i in range(len(grid)):
            maxes[i][j] = max(maxes[i][j+1], grid[i][j+1])
    return maxes

def calc_max_from_tops(grid):
    maxes = [row[:] for row in grid]
    for j in range(len(grid[0])):
        maxes[0][j] = -1
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            maxes[i][j] = max(maxes[i-1][j], grid[i-1][j])
    return maxes

def calc_max_from_bottoms(grid):
    maxes = [row[:] for row in grid]
    for j in range(len(grid)):
        maxes[len(grid) - 1][j] = -1
    for i in range(len(grid) - 2, -1, -1):
        for j in range(len(grid[0])):
            maxes[i][j] = max(maxes[i+1][j], grid[i+1][j])
    return maxes

###############################################################

def calc_dist_from_lefts(grid):
    dists = [row[:] for row in grid]
    for i in range(len(grid)):
        dists[i][0] = 0
    for i in range(len(grid)):
        dists[i][1] = 1
    for j in range(2, len(grid[i])):
        for i in range(len(grid)):
            count = 0
            ind = j
            while True:
                count += 1
                ind -= 1
                if ind < 0:
                    count -= 1
                    break
                if grid[i][j] <= grid[i][ind]:
                    break
            dists[i][j] = count
    return dists

def calc_dist_from_rights(grid):
    dists = [row[:] for row in grid]
    for i in range(len(grid)):
        dists[i][len(grid[i]) - 1] = 0
    for i in range(len(grid)):
        dists[i][len(grid[i]) - 2] = 1
    for j in range(len(grid[0]) - 3, -1, -1):
        for i in range(len(grid)):
            count = 0
            ind = j
            while True:
                count += 1
                ind += 1
                if ind >= len(grid[i]):
                    count -= 1
                    break
                if grid[i][j] <= grid[i][ind]:
                    break
            dists[i][j] = count
    return dists

def calc_dist_from_tops(grid):
    dists = [row[:] for row in grid]
    for j in range(len(grid[0])):
        dists[0][j] = 0
    for j in range(len(grid[0])):
        dists[1][j] = 1
    for i in range(2, len(grid)):
        for j in range(len(grid[0])):
            count = 0
            ind = i
            while True:
                count += 1
                ind -= 1
                if ind < 0:
                    count -= 1
                    break
                if grid[i][j] <= grid[ind][j]:
                    break
            dists[i][j] = count
    return dists

def calc_dist_from_bottoms(grid):
    dists = [row[:] for row in grid]
    for j in range(len(grid)):
        dists[len(grid) - 1][j] = 0
    for j in range(len(grid)):
        dists[len(grid) - 2][j] = 1
    for i in range(len(grid) - 3, -1, -1):
        for j in range(len(grid[0])):
            count = 0
            ind = i
            while True:
                count += 1
                ind += 1
                if ind >= len(grid):
                    count -= 1
                    break
                if grid[i][j] <= grid[ind][j]:
                    break
            dists[i][j] = count
    return dists

def p1():
    with open('tree_house.txt') as f:
        lines = f.readlines()
        grid = []
        for line in lines:
            stripped_line = line.strip()
            grid.append([int(stripped_line[i]) for i in range(len(stripped_line))])
            max_from_lefts = calc_max_from_lefts(grid)
            max_from_rights = calc_max_from_rights(grid)
            max_from_tops = calc_max_from_tops(grid)
            max_from_bottoms = calc_max_from_bottoms(grid)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > max_from_lefts[i][j] or grid[i][j] > max_from_rights[i][j] or grid[i][j] > max_from_tops[i][j] or grid[i][j] > max_from_bottoms[i][j]:
                    print(str(i) + " " + str(j) + " " + str(grid[i][j]), flush=True)
                    ans += 1
        print(ans, flush=True)

def p2():
    with open('tree_house.txt') as f:
        lines = f.readlines()
        grid = []
        for line in lines:
            stripped_line = line.strip()
            grid.append([int(stripped_line[i]) for i in range(len(stripped_line))])
        dists_from_lefts = calc_dist_from_lefts(grid)
        dists_from_rights = calc_dist_from_rights(grid)
        dists_from_tops = calc_dist_from_tops(grid)
        dists_from_bottoms = calc_dist_from_bottoms(grid)
        max_prod = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                candidate = dists_from_lefts[i][j] * dists_from_rights[i][j] * dists_from_tops[i][j] * dists_from_bottoms[i][j]
                if candidate > max_prod:
                    max_prod = candidate
        print(max_prod, flush=True)

if __name__ == "__main__":
    p2()