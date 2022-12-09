INPUT_FILE = "input_1.txt"


def solve():
    elves = []
    current_calories = 0
    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            if row == "":
                elves.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(row)
    elves.sort(reverse=True)
    print(elves[0] + elves[1] + elves[2])


if __name__ == "__main__":
    solve()
