def p1():
    with open('rucksack.txt') as f:
        lines = f.readlines()
        total = 0
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for line in lines:
            line_txt = line.strip()
            line_length = len(line_txt)
            seen_chars = {}
            for i in range(line_length//2):
                seen_chars[line_txt[i]] = True
            for i in range(line_length//2, line_length):
                if line_txt[i] in seen_chars:
                    total += alpha.index(line_txt[i]) + 1
                    break
        print(total, flush=True)

def p2():
    with open('rucksack.txt') as f:
        lines = f.readlines()
        total = 0
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        while i < len(lines):
            line_1 = lines[i].strip()
            line_2 = lines[i + 1].strip()
            line_3 = lines[i + 2].strip()
            seen_chars_1 = {}
            seen_chars_2 = {}
            for j in range(len(line_1)):
                seen_chars_1[line_1[j]] = True
            for j in range(len(line_2)):
                seen_chars_2[line_2[j]] = True
            for j in range(len(line_3)):
                if line_3[j] in seen_chars_1 and line_3[j] in seen_chars_2:
                    total += alpha.index(line_3[j]) + 1
                    break
            i += 3
        print(total, flush=True)

if __name__ == "__main__":
    p2()