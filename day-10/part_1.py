INPUT_FILE = "input_10.txt"

OP_DURATIONS = {
    "noop": 1,
    "addx": 2,
}


def solve():
    register_X = 1
    cycle = 0
    result = 0
    intervals = [20 + i * 40 for i in range(6)]

    def update_and_check_clock(op: str):
        nonlocal cycle, result
        for _ in range(OP_DURATIONS[op]):
            cycle += 1
            if cycle in intervals:
                result += cycle * register_X

    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            parts = row.split(" ")
            op = parts[0]
            update_and_check_clock(op)
            if op == "addx":
                register_X += int(parts[1])

    print(result)


if __name__ == "__main__":
    solve()
