INPUT_FILE = "input_9.txt"

def move_tail(head, tail):
    x_diff = head["x"] - tail["x"]
    y_diff = head["y"] - tail["y"] 
    if abs(x_diff) > 1 and abs(y_diff) > 1:
        tail["x"] += int(x_diff / 2)
        tail["y"] += int(y_diff / 2)
    elif abs(x_diff) > 1:
        tail["x"] += int(x_diff / 2)
        tail["y"] += y_diff
    elif abs(y_diff) > 1:
        tail["y"] += int(y_diff / 2)
        tail["x"] += x_diff

def solve():
    positions = set()
    rope = []
    for _ in range(10):
        rope.append({"x":0,"y":0})

    def update_state(direction: str, steps:int):
        axis = "x" if direction in ["L", "R"] else "y"
        increment = -1 if direction in ["L", "U"] else 1
        for _ in range(steps):
            rope[0][axis] += increment
            for i in range(1,len(rope)):
                move_tail(rope[i-1], rope[i])
            positions.add(tuple(rope[-1].values()))

    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            direction, steps = row.split(" ")
            update_state(direction, int(steps))

    result = len(positions)    
    print(result)

if __name__ == "__main__":
    solve()
