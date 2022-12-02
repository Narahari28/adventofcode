def p1():
    with open('rock_paper_scissors.txt') as f:
        lines = f.readlines()
        total = 0
        opp_vector = ['A', 'B', 'C']
        us_vector = ['X', 'Y', 'Z']
        for line in lines:
            vals = line.split()
            opp = vals[0]
            us = vals[1]
            if us == 'X':
                total += 1
            elif us == 'Y':
                total += 2
            else:
                total += 3
            if us_vector.index(us) == opp_vector.index(opp):
                total += 3
            elif us_vector.index(us) == (opp_vector.index(opp) + 1) % 3:
                total += 6
            else:
                total += 0
        print(total, flush=True)

def p2():
    with open('rock_paper_scissors.txt') as f:
        lines = f.readlines()
        total = 0
        opp_vector = ['A', 'B', 'C']
        us_vector = ['X', 'Y', 'Z']
        for line in lines:
            vals = line.split()
            opp = vals[0]
            res = vals[1]
            if res == 'X':
                us = us_vector[(opp_vector.index(opp) + 2) % 3]
                total += 0
            elif res == 'Y':
                us = us_vector[opp_vector.index(opp)]
                total += 3
            else:
                us = us_vector[(opp_vector.index(opp) + 1) % 3]
                total += 6
            if us == 'X':
                total += 1
            elif us == 'Y':
                total += 2
            else:
                total += 3
        print(total, flush=True)

if __name__ == "__main__":
    p2()