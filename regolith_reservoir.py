def execute_move(r, c, rows, cols, settled):
    if not is_occupied(r + 1, c, rows, cols, settled):
        return [r + 1, c]
    elif not is_occupied(r + 1, c - 1, rows, cols, settled):
        return [r + 1, c - 1]
    elif not is_occupied(r + 1, c + 1, rows, cols, settled):
        return [r + 1, c + 1]

def is_occupied(r, c, rows, cols, settled):
    if r in rows:
        occupied_in_row = rows[r]
        for line in occupied_in_row:
            if c >= line[0] and c <= line[1]:
                return True
    if c in cols:
        occupied_in_col = cols[c]
        for line in occupied_in_col:
            if r >= line[0] and r <= line[1]:
                return True
    if str(r) + "_" + str(c) in settled:
        return True
    return False

def can_move(r, c, rows, cols, max_depth, settled):
    if r > max_depth:
        return False
    ans = not is_occupied(r + 1, c, rows, cols, settled) or not is_occupied(r + 1, c - 1, rows, cols, settled) or not is_occupied(r + 1, c + 1, rows, cols, settled)
    return ans

def simulate_particle(rows, cols, max_depth, settled, finite):
    cur_r = 0
    cur_c = 500
    while can_move(cur_r, cur_c, rows, cols, max_depth, settled):
        [cur_r, cur_c] = execute_move(cur_r, cur_c, rows, cols, settled)
    if not finite:
        if cur_r > max_depth:
            return False
        else:
            settled[str(cur_r) + "_" + str(cur_c)] = True
            return True
    else:
        if cur_r == 0 and cur_c == 500:
            return False
        else:
            settled[str(cur_r) + "_" + str(cur_c)] = True
            return True

def simulate(rows, cols, max_depth, finite):
    ans = 0
    settled = {}
    while(True):
        did_stop = simulate_particle(rows, cols, max_depth, settled, finite)
        if did_stop:
            ans += 1
        else:
            if finite:
                return ans + 1
            else:
                return ans

def p1():
    rows = {}
    cols = {}
    max_depth = 0
    with open('regolith_reservoir.txt') as f:
        lines = f.readlines()
        for line in lines:
            coords = [x.strip() for x in line.strip().split("->")]
            coords = [[int(x.split(",")[0]), int(x.split(",")[1])] for x in coords]
            ind = 0
            while ind < len(coords) - 1:
                max_depth = max(coords[ind][1], coords[ind + 1][1], max_depth)
                if coords[ind][0] == coords[ind + 1][0]:
                    s = min(coords[ind][1], coords[ind + 1][1])
                    e = max(coords[ind][1], coords[ind + 1][1])
                    if coords[ind][0] in cols:
                        cols[coords[ind][0]].append([s, e])
                    else:
                        cols[coords[ind][0]] = [[s, e]]
                else:
                    s = min(coords[ind][0], coords[ind + 1][0])
                    e = max(coords[ind][0], coords[ind + 1][0])
                    if coords[ind][1] in rows:
                        rows[coords[ind][1]].append([s, e])
                    else:
                        rows[coords[ind][1]] = [[s, e]]
                ind += 1
        ans = simulate(rows, cols, max_depth, False)
        print(ans, flush=True)

def p2():
    rows = {}
    cols = {}
    max_depth = 0
    with open('regolith_reservoir.txt') as f:
        lines = f.readlines()
        for line in lines:
            coords = [x.strip() for x in line.strip().split("->")]
            coords = [[int(x.split(",")[0]), int(x.split(",")[1])] for x in coords]
            ind = 0
            while ind < len(coords) - 1:
                max_depth = max(coords[ind][1], coords[ind + 1][1], max_depth)
                if coords[ind][0] == coords[ind + 1][0]:
                    s = min(coords[ind][1], coords[ind + 1][1])
                    e = max(coords[ind][1], coords[ind + 1][1])
                    if coords[ind][0] in cols:
                        cols[coords[ind][0]].append([s, e])
                    else:
                        cols[coords[ind][0]] = [[s, e]]
                else:
                    s = min(coords[ind][0], coords[ind + 1][0])
                    e = max(coords[ind][0], coords[ind + 1][0])
                    if coords[ind][1] in rows:
                        rows[coords[ind][1]].append([s, e])
                    else:
                        rows[coords[ind][1]] = [[s, e]]
                ind += 1
        ans = simulate(rows, cols, max_depth, True)
        print(ans, flush=True)

if __name__ == "__main__":
    p2()