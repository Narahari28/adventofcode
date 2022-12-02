def p1():
    with open('calorie_counting.txt') as f:
        lines = f.readlines()
        max_sum = 0
        cur_sum = 0
        for line in lines:
            if line.strip() == "":
                if cur_sum > max_sum:
                    max_sum = cur_sum
                cur_sum = 0
            else:
                cur_sum += int(line.strip())
        if cur_sum > max_sum:
            max_sum = cur_sum
        print(max_sum, flush=True)

def p2():
    with open('calorie_counting.txt') as f:
        lines = f.readlines()
        max_sum = 0
        second_max_sum = 0
        third_max_sum = 0
        cur_sum = 0
        for line in lines:
            if line.strip() == "":
                if cur_sum >= max_sum:
                    third_max_sum = second_max_sum
                    second_max_sum = max_sum
                    max_sum = cur_sum
                elif cur_sum >= second_max_sum:
                    third_max_sum = second_max_sum
                    second_max_sum = cur_sum
                elif cur_sum >= third_max_sum:
                    third_max_sum = cur_sum
                cur_sum = 0
            else:
                cur_sum += int(line.strip())
        if cur_sum >= max_sum:
            third_max_sum = second_max_sum
            second_max_sum = max_sum
            max_sum = cur_sum
        elif cur_sum >= second_max_sum:
            third_max_sum = second_max_sum
            second_max_sum = cur_sum
        elif cur_sum >= third_max_sum:
            third_max_sum = cur_sum
        print(max_sum + second_max_sum + third_max_sum, flush=True)

if __name__ == "__main__":
    p2()