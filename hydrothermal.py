def p1():
    with open('hydrothermal.txt') as f:
        lines = f.readlines()
        grid = []
        for i in range(1000):
            grid.append([0]*1000)
        for line in lines:
            line = line.strip()
            ends = [val.strip() for val in line.split("->")]
            start_split = ends[0].split(",")
            end_split = ends[1].split(",")
            start_x = int(start_split[0])
            start_y = int(start_split[1])
            end_x = int(end_split[0])
            end_y = int(end_split[1])
            if start_x == end_x:
                min_y = min(start_y, end_y)
                max_y = max(start_y, end_y)
                for i in range(min_y, max_y + 1):
                    print("Going at %s %s" % (start_x, i), flush=True)
                    grid[start_x][i] += 1
            elif start_y == end_y:
                min_x = min(start_x, end_x)
                max_x = max(start_x, end_x)
                for i in range(min_x, max_x + 1):
                    print("Going at %s %s" % (i, start_y), flush=True)
                    grid[i][start_y] += 1
        ans = 0
        for i in range(1000):
            for j in range(1000):
                if grid[i][j] > 1:
                    ans += 1
        print(ans, flush=True)

def p2():
    with open('hydrothermal.txt') as f:
        lines = f.readlines()
        grid = []
        for i in range(1000):
            grid.append([0]*1000)
        for line in lines:
            line = line.strip()
            ends = [val.strip() for val in line.split("->")]
            start_split = ends[0].split(",")
            end_split = ends[1].split(",")
            start_x = int(start_split[0])
            start_y = int(start_split[1])
            end_x = int(end_split[0])
            end_y = int(end_split[1])
            if start_x == end_x:
                min_y = min(start_y, end_y)
                max_y = max(start_y, end_y)
                for i in range(min_y, max_y + 1):
                    print("Going at %s %s" % (start_x, i), flush=True)
                    grid[start_x][i] += 1
            elif start_y == end_y:
                min_x = min(start_x, end_x)
                max_x = max(start_x, end_x)
                for i in range(min_x, max_x + 1):
                    print("Going at %s %s" % (i, start_y), flush=True)
                    grid[i][start_y] += 1
            else:
                x = start_x
                y = start_y
                deltas = [1 if end_x > start_x else -1, 1 if end_y > start_y else -1]
                while(x != end_x):
                    grid[x][y] += 1
                    x += deltas[0]
                    y += deltas[1]
                grid[end_x][end_y] += 1
        ans = 0
        for i in range(1000):
            for j in range(1000):
                if grid[i][j] > 1:
                    ans += 1
        print(ans, flush=True)

if __name__ == "__main__":
    p2()