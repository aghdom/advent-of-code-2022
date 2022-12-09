INPUT_FILE = "input_1.txt"


def solve():
    max_calories = 0
    current_calories = 0
    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            if row == "":
                if current_calories >= max_calories:
                    max_calories = current_calories
                current_calories = 0
            else:
                current_calories += int(row)
    print(max_calories)


if __name__ == "__main__":
    solve()
