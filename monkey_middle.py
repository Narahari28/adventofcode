def execute_moves(monkey_items, monkey_operations, monkey_test, monkey_dest_if_true, monkey_dest_if_false):
    counts = {}
    for i in range(20):
        for j in range(len(monkey_items)):
            if not j in counts:
                counts[j] = 0
            items = monkey_items[j]
            while(len(items) > 0):
                worry_level = items.pop(0)
                counts[j] = counts[j] + 1
                operation = monkey_operations[j].split()
                if operation[1] == '+':
                    if operation[2] == 'old':
                        worry_level += worry_level
                    else:
                        worry_level += int(operation[2])
                elif operation[1] == '*':
                    if operation[2] == 'old':
                        worry_level *= worry_level
                    else:
                        worry_level *= int(operation[2])
                worry_level = worry_level // 3
                if worry_level % monkey_test[j] == 0:
                    monkey_items[monkey_dest_if_true[j]].append(worry_level)
                else:
                    monkey_items[monkey_dest_if_false[j]].append(worry_level)
    counts = sorted(counts.values(), reverse=True)
    return counts[0]*counts[1]

def execute_moves2(monkey_items, monkey_operations, monkey_test, monkey_dest_if_true, monkey_dest_if_false):
    counts = {}
    prod = 1
    tests = monkey_test.values()
    for val in tests:
        prod *= val
    for i in range(10000):
        for j in range(len(monkey_items)):
            if not j in counts:
                counts[j] = 0
            items = monkey_items[j]
            while(len(items) > 0):
                worry_level = items.pop(0)
                counts[j] = counts[j] + 1
                operation = monkey_operations[j].split()
                if operation[1] == '+':
                    if operation[2] == 'old':
                        worry_level += worry_level
                    else:
                        worry_level += int(operation[2])
                elif operation[1] == '*':
                    if operation[2] == 'old':
                        worry_level *= worry_level
                    else:
                        worry_level *= int(operation[2])
                worry_level %= prod
                if worry_level % monkey_test[j] == 0:
                    monkey_items[monkey_dest_if_true[j]].append(worry_level)
                else:
                    monkey_items[monkey_dest_if_false[j]].append(worry_level)
    counts = sorted(counts.values(), reverse=True)
    return counts[0]*counts[1]

def p1():
    with open('monkey_middle.txt') as f:
        lines = f.readlines()
        monkey_items = []
        monkey_ind = -1
        monkey_operations = {}
        monkey_test = {}
        monkey_dest_if_true = {}
        monkey_dest_if_false = {}
        for line in lines:
            split_line = line.strip().split()
            if(len(split_line) == 0):
                continue
            elif split_line[0] == "Monkey":
                monkey_ind = int(split_line[1][:-1])
            elif split_line[0] == "Starting":
                vals = line.strip().split(":")[-1]
                vals = vals.split(",")
                monkey_items.append([int(x.strip()) for x in vals])
            elif split_line[0] == "Operation:":
                monkey_operations[monkey_ind] = line.strip().split("=")[-1].strip()
            elif split_line[0] == "Test:":
                monkey_test[monkey_ind] = int(line.strip().split()[-1])
            elif split_line[0] == "If" and split_line[1] == "true:":
                monkey_dest_if_true[monkey_ind] = int(line.strip().split()[-1])
            elif split_line[0] == "If" and split_line[1] == "false:":
                monkey_dest_if_false[monkey_ind] = int(line.strip().split()[-1])
        ans = execute_moves(monkey_items, monkey_operations, monkey_test, monkey_dest_if_true, monkey_dest_if_false)
        print(ans, flush=True)

def p2():
    with open('monkey_middle.txt') as f:
        lines = f.readlines()
        monkey_items = []
        monkey_ind = -1
        monkey_operations = {}
        monkey_test = {}
        monkey_dest_if_true = {}
        monkey_dest_if_false = {}
        for line in lines:
            split_line = line.strip().split()
            if(len(split_line) == 0):
                continue
            elif split_line[0] == "Monkey":
                monkey_ind = int(split_line[1][:-1])
            elif split_line[0] == "Starting":
                vals = line.strip().split(":")[-1]
                vals = vals.split(",")
                monkey_items.append([int(x.strip()) for x in vals])
            elif split_line[0] == "Operation:":
                monkey_operations[monkey_ind] = line.strip().split("=")[-1].strip()
            elif split_line[0] == "Test:":
                monkey_test[monkey_ind] = int(line.strip().split()[-1])
            elif split_line[0] == "If" and split_line[1] == "true:":
                monkey_dest_if_true[monkey_ind] = int(line.strip().split()[-1])
            elif split_line[0] == "If" and split_line[1] == "false:":
                monkey_dest_if_false[monkey_ind] = int(line.strip().split()[-1])
        ans = execute_moves2(monkey_items, monkey_operations, monkey_test, monkey_dest_if_true, monkey_dest_if_false)
        print(ans, flush=True)

if __name__ == "__main__":
    p2()