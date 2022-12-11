from math import gcd

INPUT_FILE = "input_11.txt"
LCM = 1


class Monkey:
    def __init__(
        self, items: list, operation: str, divisor: int, targets: dict
    ) -> None:
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.targets = targets
        self.inspections = 0

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def take_turn(self):
        for item in self.items:
            old = item
            worry_level = eval(self.operation)
            worry_level = worry_level % LCM
            result = worry_level % self.divisor == 0
            self.targets[result].add_item(worry_level)
            self.inspections += 1
        self.items = []


def parse_input() -> list:
    global LCM
    monkeys = []
    all_items = []
    with open(INPUT_FILE, "r") as input_file:
        while input_file:
            row = input_file.readline()
            row = row.strip("\n")
            if row.startswith("Monkey"):
                # Starting items
                row = input_file.readline().strip("\n")
                items = [
                    int(item) for item in row.replace(" ", "").split(":")[1].split(",")
                ]
                all_items += items
                # Operation
                row = input_file.readline().strip("\n")
                op = row.split(":")[1].split("=")[1]
                # Test
                row = input_file.readline().strip("\n")
                divisor = int(row.split(" ")[-1])
                LCM *= divisor
                # Targets
                targets = {}
                row = input_file.readline().strip("\n")
                targets[True] = int(row.split(" ")[-1])
                row = input_file.readline().strip("\n")
                targets[False] = int(row.split(" ")[-1])
                monkeys.append(Monkey(items, op, divisor, targets))
                input_file.readline()
            else:
                break
    for monkey in monkeys:
        monkey.targets[True] = monkeys[monkey.targets[True]]
        monkey.targets[False] = monkeys[monkey.targets[False]]
    return monkeys


def solve():
    monkeys = parse_input()
    for turn in range(10000):
        for monkey in monkeys:
            monkey.take_turn()
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])


if __name__ == "__main__":
    solve()
