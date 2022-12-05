from collections import deque


INPUT_FILE = "input_5.txt"


def construct_stacks(diagram: deque) -> list:
    stacks = []
    legend = diagram.pop()
    num_of_stacks = len(legend.replace(" ", ""))
    for i in range(num_of_stacks):
        stacks.append(deque())
    while len(diagram) != 0:
        row = diagram.pop()
        slots = [row[i : i + 4] for i in range(0, len(row), 4)]
        for i, slot in enumerate(slots):
            label = slot[1]
            if label != " ":
                stacks[i].append(label)
    return stacks


def solve():
    diagram = deque()
    stacks = []
    with open(INPUT_FILE, "r+") as input_file:
        for row in input_file:
            row = row.strip("\n")
            if stacks == [] and row != "":
                diagram.append(row)
            elif row == "":
                stacks = construct_stacks(diagram)
            else:
                parts = row.split(" ")
                tmp_stack = deque()
                count, source, destination = (
                    int(parts[1]),
                    int(parts[3]) - 1,
                    int(parts[5]) - 1,
                )
                for i in range(count):
                    tmp_stack.append(stacks[source].pop())
                for i in range(count):
                    stacks[destination].append(tmp_stack.pop())
    result = ""
    for stack in stacks:
        result += stack.pop()
    print(result)


if __name__ == "__main__":
    solve()
