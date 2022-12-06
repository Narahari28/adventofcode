def is_legend(line):
    vals = line.strip().split()
    for val in vals:
        if not val.isnumeric():
            return False
    return True

def parse_crate_line(crate_positions, line):
    i = 0
    while i < len(line):
        if line[i] == '[':
            stack = crate_positions[i//4]
            stack.append(line[i + 1])
            crate_positions[i//4] = stack
        i += 4

def execute_move(crate_positions, crates, source, dest):
    stack_source = crate_positions[source]
    stack_dest = crate_positions[dest]
    for i in range(crates):
        val = stack_source.pop(0)
        stack_dest.insert(0, val)
    crate_positions[source] = stack_source
    crate_positions[dest] = stack_dest

def execute_move_v2(crate_positions, crates, source, dest):
    stack_source = crate_positions[source]
    stack_dest = crate_positions[dest]
    for i in range(crates):
        val = stack_source.pop(0)
        stack_dest.insert(i, val)
    crate_positions[source] = stack_source
    crate_positions[dest] = stack_dest

def p1():
    with open('supply_stacks.txt') as f:
        lines = f.readlines()
        crate_positions = [[], [], [], [], [], [], [], [], []]
        has_seen_legend = False
        for line in lines:
            if not has_seen_legend:
                if is_legend(line):
                    has_seen_legend = True
                else:
                    parse_crate_line(crate_positions, line)
            elif line.strip() != "":
                instruction_split = line.strip().split()
                crate_move_count = int(instruction_split[1])
                source = int(instruction_split[3]) - 1
                dest = int(instruction_split[5]) - 1
                execute_move(crate_positions, crate_move_count, source, dest)
        ans = ''
        for j in range(len(crate_positions)):
            ans += crate_positions[j][0]
        print(ans, flush=True)
        

def p2():
    with open('supply_stacks.txt') as f:
        lines = f.readlines()
        crate_positions = [[], [], [], [], [], [], [], [], []]
        has_seen_legend = False
        for line in lines:
            if not has_seen_legend:
                if is_legend(line):
                    has_seen_legend = True
                else:
                    parse_crate_line(crate_positions, line)
            elif line.strip() != "":
                instruction_split = line.strip().split()
                crate_move_count = int(instruction_split[1])
                source = int(instruction_split[3]) - 1
                dest = int(instruction_split[5]) - 1
                execute_move_v2(crate_positions, crate_move_count, source, dest)
        ans = ''
        for j in range(len(crate_positions)):
            ans += crate_positions[j][0]
        print(ans, flush=True)

if __name__ == "__main__":
    p2()