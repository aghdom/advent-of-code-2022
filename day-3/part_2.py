INPUT_FILE = "input_3.txt"


def get_priority(item: str) -> int:
    if item.isupper():
        priority = ord(item) - ord("A") + 27
    else:
        priority = ord(item) - ord("a") + 1
    return priority


def solve():
    i = 0
    total = 0
    group = []
    with open(INPUT_FILE, "r+") as input_file:
        for row in input_file:
            row = row.strip("\n")
            i += 1
            group.append(row)
            if i % 3 == 0:
                badge = set(group[0]) & set(group[1]) & set(group[2])
                total += get_priority(badge.pop())
                group.clear()
    print(total)


if __name__ == "__main__":
    solve()
