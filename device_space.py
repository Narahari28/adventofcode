def is_command(line):
    return line[0] == '$'

def sum_under(limit, sizes):
    ans = 0
    for folder in sizes:
        if sizes[folder] <= limit:
            ans += sizes[folder]
    return ans

def minimum_to_remove(limit, sizes):
    total = sizes["/"]
    minimum_removal = total
    for key in sizes:
        candidate = sizes[key]
        if total - candidate <= limit and candidate <= minimum_removal:
            minimum_removal = candidate
    return minimum_removal

def get_parent(loc):
    if loc == "/":
        return None
    split_loc = loc.split("_")
    return "_".join(split_loc[:-1])

def propagate_size(file_size, cur_location, sizes):
    cur_node = cur_location
    while cur_node != None:
        if cur_node in sizes:
            sizes[cur_node] += file_size
        else:
            sizes[cur_node] = file_size
        cur_node = get_parent(cur_node)

def p1():
    with open('device_space.txt') as f:
        lines = f.readlines()
        sizes = {}
        cur_location = '/'
        for line in lines:
            split_line = line.split()
            if is_command(line):
                if split_line[1] == "cd":
                    dest = split_line[2]
                    if dest == "/":
                        cur_location = "/"
                    elif dest == "..":
                        cur_location = get_parent(cur_location)
                    else:
                        cur_location = cur_location + "_" + dest
            else:
                if split_line[0].isnumeric():
                    propagate_size(int(split_line[0]), cur_location, sizes)
        ans = sum_under(100000, sizes)
        print(ans, flush=True)
        

def p2():
    with open('device_space.txt') as f:
        lines = f.readlines()
        sizes = {}
        cur_location = '/'
        for line in lines:
            split_line = line.split()
            if is_command(line):
                if split_line[1] == "cd":
                    dest = split_line[2]
                    if dest == "/":
                        cur_location = "/"
                    elif dest == "..":
                        cur_location = get_parent(cur_location)
                    else:
                        cur_location = cur_location + "_" + dest
            else:
                if split_line[0].isnumeric():
                    propagate_size(int(split_line[0]), cur_location, sizes)
        ans = minimum_to_remove(40000000, sizes)
        print(ans, flush=True)

if __name__ == "__main__":
    p2()