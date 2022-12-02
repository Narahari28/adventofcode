def p1():
    with open('sonar.txt') as f:
        lines = f.readlines()
        nums = []
        for line in lines:
            nums.append(int(line.strip()))
        count = 0
        for i in range(1, len(nums)):
            if(nums[i] > nums[i - 1]):
                count += 1
        print(count, flush=True)

def p2():
    with open('sonar.txt') as f:
        lines = f.readlines()
        nums = []
        for line in lines:
            nums.append(int(line.strip()))
        count = 0
        for i in range(3, len(nums)):
            if(nums[i] > nums[i - 3]):
                count += 1
        print(count, flush=True)

if __name__ == "__main__":
    p2()