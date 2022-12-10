def is_important(cycle):
    return cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220

def is_lit_pixel(val, cycle):
    return (cycle - 1) % 40 >= val - 1 and (cycle - 1) % 40 <= val + 1

def p1():
    with open('cathode_ray.txt') as f:
        lines = f.readlines()
        ans = 0
        val = 1
        cycle = 1
        for line in lines:
            split_line = line.strip().split()
            if split_line[0] == "noop":
                if is_important(cycle):
                    ans += cycle * val
                cycle += 1
            else:
                if is_important(cycle):
                    ans += cycle * val
                cycle += 1
                if is_important(cycle):
                    ans += cycle * val
                cycle += 1
                val += int(split_line[1])
        print(ans, flush=True)

def p2():
    with open('cathode_ray.txt') as f:
        lines = f.readlines()
        val = 1
        cycle = 1
        for line in lines:
            if cycle % 40 == 1:
                print("", flush=True)
            if is_lit_pixel(val, cycle):
                print("#", end="", flush=True)
            else:
                print(".", end="", flush=True)
            split_line = line.strip().split()
            if split_line[0] == "noop":
                cycle += 1
            else:
                cycle += 1
                if cycle % 40 == 1:
                    print("", flush=True)
                if is_lit_pixel(val, cycle):
                    print("#", end="", flush=True)
                else:
                    print(".", end="", flush=True)
                cycle += 1
                val += int(split_line[1])

if __name__ == "__main__":
    p2()