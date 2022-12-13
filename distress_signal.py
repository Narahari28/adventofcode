import ast
from functools import cmp_to_key

def split(l):
    return ast.literal_eval(l)

def is_lower_val(v1, v2):
    return int(v1) < int(v2)

def is_lower(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if is_lower_val(l1, l2):
            return True
        elif is_lower_val(l2, l1):
            return False
        return False
    elif isinstance(l1, int):
        if is_lower([l1], l2):
            return True
        elif is_lower(l2, [l1]):
            return False
        return False

    elif isinstance(l2, int):
        if is_lower(l1, [l2]):
            return True
        elif is_lower([l2], l1):
            return False
        return False
    l1_split = l1
    l2_split = l2
    ind = 0
    while ind < len(l1_split) and ind < len(l2_split):
        if is_lower(l1_split[ind], l2_split[ind]):
            return True
        elif is_lower(l2_split[ind], l1_split[ind]):
            return False
        ind += 1
    if len(l1_split) > len(l2_split):
        return False
    elif len(l2_split) > len(l1_split):
        return True
    return False

def compare(item1, item2):
    if is_lower(item1, item2):
        return -1
    elif is_lower(item2, item1):
        return 1
    else:
        return 0

def p1():
    with open('distress_signal') as f:
        lines = f.readlines()
        ans = 0
        i = 0
        while i < len(lines):
            line_1 = lines[i].strip()
            line_2 = lines[i + 1].strip()
            if(is_lower(split(line_1), split(line_2))):
                ans += (i//3) + 1
            i += 3
        print(ans, flush=True)

def p2():
    with open('distress_signal') as f:
        lines = f.readlines()
        sorted_lines = []
        i = 0
        while i < len(lines):
            if(lines[i].strip() != ''):
                sorted_lines.append(split(lines[i].strip()))
            i += 1
        sorted_lines.append([[2]])
        sorted_lines.append([[6]])
        sorted_lines = sorted(sorted_lines, key=cmp_to_key(compare))
        ans = 1
        for i2 in range(len(sorted_lines)):
            if str(sorted_lines[i2]) == '[[2]]':
                ans *= (i2 + 1)
            elif str(sorted_lines[i2]) == '[[6]]':
                ans *= (i2 + 1)
        print(ans, flush=True)

if __name__ == "__main__":
    p2()