def p1():
    x = 0
    y = 0
    with open('dive.txt') as f:
        lines = f.readlines()
        nums = []
        for line in lines:
            line_txt = line.strip()
            print(line_txt, flush=True)
            if "forward" in line_txt:
                x += int(line_txt.split()[1])
            elif "down" in line_txt:
                y += int(line_txt.split()[1])
            elif "up" in line_txt:
                y -= int(line_txt.split()[1])
        print(x*y, flush=True)

def p2():
    x = 0
    y = 0
    aim = 0
    with open('dive.txt') as f:
        lines = f.readlines()
        nums = []
        for line in lines:
            line_txt = line.strip()
            print(line_txt, flush=True)
            if "forward" in line_txt:
                x += int(line_txt.split()[1])
                y += aim*int(line_txt.split()[1])
            elif "down" in line_txt:
                aim += int(line_txt.split()[1])
            elif "up" in line_txt:
                aim -= int(line_txt.split()[1])
        print(x*y, flush=True)

if __name__ == "__main__":
    p2()