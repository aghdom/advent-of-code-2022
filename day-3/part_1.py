INPUT_FILE = "input_3.txt"


def get_priority(item: str) -> int:
    if item.isupper():
        priority = ord(item) - ord("A") + 27
    else:
        priority = ord(item) - ord("a") + 1
    return priority


def solve():
    total = 0
    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            comp_size = int(len(row) / 2)
            comp_1 = row[comp_size:]
            comp_2 = row[:comp_size]
            in_both = set(comp_1) & set(comp_2)
            total += get_priority(in_both.pop())
    print(total)


if __name__ == "__main__":
    solve()
