def is_clean_window(window, marker):
    if len(window) < marker:
        return False
    for i in range(len(window)):
        if window.count(window[i]) != 1:
            return False
    return True

def insert_into_window(window, char, marker):
    window.append(char)
    if len(window) > marker:
        window.pop(0)

def p1():
    with open('tuning_trouble.txt') as f:
        lines = f.readlines()
        text = lines[0]
        window = []
        for i in range(len(text)):
            if is_clean_window(window, 4):
                break
            else:
                insert_into_window(window, text[i], 4)
        print(i, flush=True)

def p2():
    with open('tuning_trouble.txt') as f:
        lines = f.readlines()
        text = lines[0]
        window = []
        for i in range(len(text)):
            if is_clean_window(window, 14):
                break
            else:
                insert_into_window(window, text[i], 14)
        print(i, flush=True)

if __name__ == "__main__":
    p2()