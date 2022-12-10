INPUT_FILE = "input_10.txt"

OP_DURATIONS = {
    "noop": 1,
    "addx": 2,
}


def solve():
    register_X = 1
    cycle = 0
    buffer = ""

    def update(op: str):
        nonlocal cycle, buffer, register_X
        for _ in range(OP_DURATIONS[op]):
            if cycle % 40 >= register_X - 1 and cycle % 40 <= register_X + 1:
                buffer += "#"
            else:
                buffer += "."
            cycle += 1
            if cycle % 40 == 0:
                print(buffer)
                buffer = ""

    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            parts = row.split(" ")
            op = parts[0]
            update(op)
            if op == "addx":
                register_X += int(parts[1])


if __name__ == "__main__":
    solve()
