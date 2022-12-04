INPUT_FILE = "input_4.txt"


def solve():
    count = 0
    with open(INPUT_FILE, "r+") as input_file:
        for row in input_file:
            row = row.strip("\n")
            ranges = row.split(",")
            range_1 = ranges[0].split("-")
            range_2 = ranges[1].split("-")
            elf_1 = range(int(range_1[0]), int(range_1[1]) + 1)
            elf_2 = range(int(range_2[0]), int(range_2[1]) + 1)
            if set(elf_1) & set(elf_2) != set():
                count += 1
    print(count)


if __name__ == "__main__":
    solve()
