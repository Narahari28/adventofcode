def execute_move(h_x, h_y, t_x, t_y, dir_vector, move_by_default):
    if move_by_default:
        new_h_x = h_x + dir_vector[0]
        new_h_y = h_y + dir_vector[1]
    else:
        new_h_x = h_x
        new_h_y = h_y
    new_t_x = t_x
    new_t_y = t_y
    if (abs(new_h_x - new_t_x) == 0 and abs(new_h_y - new_t_y) == 2) or abs(new_h_x - new_t_x) == 2 and abs(new_h_y - new_t_y) == 0:
        if new_t_x == new_h_x - 2:
            new_t_x = new_h_x - 1
        if new_t_x == new_h_x + 2:
            new_t_x = new_h_x + 1
        if new_t_y == new_h_y + 2:
            new_t_y = new_h_y + 1
        if new_t_y == new_h_y  - 2:
            new_t_y = new_h_y - 1
    elif (abs(new_h_x - new_t_x) == 1 and abs(new_h_y - new_t_y) == 2) or (abs(new_h_x - new_t_x) == 2 and abs(new_h_y - new_t_y) == 1):
        if new_t_x == new_h_x - 2:
            new_t_x = new_h_x - 1
            new_t_y = new_h_y
        elif new_t_x == new_h_x + 2:
            new_t_x = new_h_x + 1
            new_t_y = new_h_y
        elif new_t_y == new_h_y - 2:
            new_t_y = new_h_y - 1
            new_t_x = new_h_x
        elif new_t_y == new_h_y + 2:
            new_t_y = new_h_y + 1
            new_t_x = new_h_x
    elif abs(new_h_x - new_t_x) == 2 and abs(new_h_y - new_t_y) == 2:
        if new_t_x == new_h_x - 2:
            new_t_x = new_h_x - 1
        elif new_t_x == new_h_x + 2:
            new_t_x = new_h_x + 1
        if new_t_y == new_h_y - 2:
            new_t_y = new_h_y - 1
        elif new_t_y == new_h_y + 2:
            new_t_y = new_h_y + 1
    return [new_h_x, new_h_y, new_t_x, new_t_y]

def p1():
    with open('rope_bridge.txt') as f:
        lines = f.readlines()
        grid = []
        h_x = 0
        h_y = 0
        t_x = 0
        t_y = 0
        seen_tail_positions = {"0_0": True}
        for line in lines:
            stripped_line = line.strip()
            split_line = stripped_line.split()
            direction = split_line[0]
            if direction == "R":
                dir_vector = [1, 0]
            elif direction == "L":
                dir_vector = [-1, 0]
            elif direction == "U":
                dir_vector = [0, 1]
            elif direction == "D":
                dir_vector = [0, -1]
            count = split_line[1]
            for i in range(int(count)):
                [h_x, h_y, t_x, t_y] = execute_move(h_x, h_y, t_x, t_y, dir_vector, True)
                seen_tail_positions[str(t_x) + "_" + str(t_y)] = True
        print(len(seen_tail_positions), flush=True)

def p2():
    with open('rope_bridge.txt') as f:
        lines = f.readlines()
        grid = []
        x_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        y_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        seen_tail_positions = {"0_0": True}
        for line in lines:
            stripped_line = line.strip()
            split_line = stripped_line.split()
            direction = split_line[0]
            if direction == "R":
                dir_vector = [1, 0]
            elif direction == "L":
                dir_vector = [-1, 0]
            elif direction == "U":
                dir_vector = [0, 1]
            elif direction == "D":
                dir_vector = [0, -1]
            count = split_line[1]
            for i in range(int(count)):
                # print("----------------------------", flush=True)
                # print(dir_vector, flush=True)
                # print(str(i + 1) + " of " + count, flush=True)
                [x_vals[0], y_vals[0], x_vals[1], y_vals[1]] = execute_move(x_vals[0], y_vals[0], x_vals[1], y_vals[1], dir_vector, True)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[1], y_vals[1], x_vals[2], y_vals[2]] = execute_move(x_vals[1], y_vals[1], x_vals[2], y_vals[2], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[2], y_vals[2], x_vals[3], y_vals[3]] = execute_move(x_vals[2], y_vals[2], x_vals[3], y_vals[3], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[3], y_vals[3], x_vals[4], y_vals[4]] = execute_move(x_vals[3], y_vals[3], x_vals[4], y_vals[4], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[4], y_vals[4], x_vals[5], y_vals[5]] = execute_move(x_vals[4], y_vals[4], x_vals[5], y_vals[5], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[5], y_vals[5], x_vals[6], y_vals[6]] = execute_move(x_vals[5], y_vals[5], x_vals[6], y_vals[6], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[6], y_vals[6], x_vals[7], y_vals[7]] = execute_move(x_vals[6], y_vals[6], x_vals[7], y_vals[7], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[7], y_vals[7], x_vals[8], y_vals[8]] = execute_move(x_vals[7], y_vals[7], x_vals[8], y_vals[8], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                [x_vals[8], y_vals[8], x_vals[9], y_vals[9]] = execute_move(x_vals[8], y_vals[8], x_vals[9], y_vals[9], dir_vector, False)
                # print(x_vals, flush=True)
                # print(y_vals, flush=True)
                # if not str(x_vals[9]) + "_" + str(y_vals[9]) in seen_tail_positions:
                    # print(str(x_vals[9]) + "_" + str(y_vals[9]), flush=True)
                    # print(dir_vector, flush=True)
                    # print(str(i + 1) + " of " + count, flush=True)
                seen_tail_positions[str(x_vals[9]) + "_" + str(y_vals[9])] = True
        print(len(seen_tail_positions), flush=True)

if __name__ == "__main__":
    p2()