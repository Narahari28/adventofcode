def p1():
    with open('binary_diag.txt') as f:
        lines = f.readlines()
        zeros = [0]*12
        ones = [0]*12
        for line in lines:
            line_txt = line.strip()
            for i in range(len(line_txt)):
                char = line_txt[i]
                if char == '0':
                    zeros[i] += 1
                else:
                    ones[i] += 1
        eps = 0
        gamma = 0
        for i in range(11, 0, -1):
            if(zeros[i] > ones[i]):
                eps += 2**(11 -i)
            else:
                gamma += 2**(11 - i)
        print(zeros, flush=True)
        print(ones, flush=True)
        print(eps*gamma, flush=True)

def p2():
    nums = []
    with open('binary_diag.txt') as f:
        lines = f.readlines()
        for line in lines:
            line_txt = line.strip()
            nums.append(line_txt)
    nums_copy = [num for num in nums]
    index = 0
    while len(nums_copy) > 1:
        values = [num[index] for num in nums_copy]
        zero_count = values.count('0')
        one_count = values.count('1')
        if(zero_count > one_count):
            nums_copy = [num for num in nums_copy if num[index] == '0']
        else:
            nums_copy = [num for num in nums_copy if num[index] == '1']
        index += 1
    a = nums_copy[0]
    nums_copy = [num for num in nums]
    index = 0
    while len(nums_copy) > 1:
        values = [num[index] for num in nums_copy]
        zero_count = values.count('0')
        one_count = values.count('1')
        if(zero_count <= one_count):
            nums_copy = [num for num in nums_copy if num[index] == '0']
        else:
            nums_copy = [num for num in nums_copy if num[index] == '1']
        index += 1
    b = nums_copy[0]
    print(int(a, 2)*int(b, 2), flush=True)

if __name__ == "__main__":
    p2()