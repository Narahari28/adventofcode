def p1():
    with open('camp_cleanup.txt') as f:
        lines = f.readlines()
        ans = 0
        for line in lines:
            line_txt = line.strip()
            line_txt_split = line_txt.split(",")
            elf_1 = line_txt_split[0]
            elf_2 = line_txt_split[1]
            elf_1_split = elf_1.split("-")
            elf_2_split = elf_2.split("-")
            elf_1_start = int(elf_1_split[0])
            elf_1_end = int(elf_1_split[1])
            elf_2_start = int(elf_2_split[0])
            elf_2_end = int(elf_2_split[1])
            if elf_1_start <= elf_2_start and elf_1_end >= elf_2_end:
                ans += 1
            elif elf_2_start <= elf_1_start and elf_2_end >= elf_1_end:
                ans += 1
        print(ans, flush=True)

def p2():
    with open('camp_cleanup.txt') as f:
        lines = f.readlines()
        total = 0
        non_overlap = 0
        for line in lines:
            line_txt = line.strip()
            line_txt_split = line_txt.split(",")
            elf_1 = line_txt_split[0]
            elf_2 = line_txt_split[1]
            elf_1_split = elf_1.split("-")
            elf_2_split = elf_2.split("-")
            elf_1_start = int(elf_1_split[0])
            elf_1_end = int(elf_1_split[1])
            elf_2_start = int(elf_2_split[0])
            elf_2_end = int(elf_2_split[1])
            if elf_1_start > elf_2_end:
                non_overlap += 1
            elif elf_2_start > elf_1_end:
                non_overlap += 1
            total += 1
        print(total - non_overlap, flush=True)

if __name__ == "__main__":
    p2()