INPUT_FILE = "input_9.txt"


def solve():
    positions = set()
    head = {"x":0,"y":0}
    tail = {"x":0,"y":0}
    
    def move_tail():
        x_diff = head["x"] - tail["x"]
        y_diff = head["y"] - tail["y"]
        if abs(x_diff) > 1:
            tail["x"] += int(x_diff / 2)
            tail["y"] += y_diff
        elif abs(y_diff) > 1:
            tail["y"] += int(y_diff / 2)
            tail["x"] += x_diff
        positions.add(tuple(tail.values()))
        

    def update_state(direction: str, steps:int):
        axis = "x" if direction in ["L", "R"] else "y"
        increment = -1 if direction in ["L", "U"] else 1
        for _ in range(steps):
            head[axis] += increment
            move_tail()

    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            direction, steps = row.split(" ")
            update_state(direction, int(steps))

    result = len(positions)    
    print(result)

if __name__ == "__main__":
    solve()
