INPUT_FILE = "input_8.txt"


def solve():
    map = []
    scenic_map = []
    row_len = None
    with open(INPUT_FILE, "r+") as input_file:
        for row in input_file:
            row = row.strip("\n")
            if not row_len:
                row_len = len(row)
            scenic_map.append([0 for _ in range(row_len)])
            map.append([int(c) for c in row])
    map_len = len(map)
    for i in range(1, map_len - 1):
        for j in range(1, row_len - 1):
            left = 1
            right = 1
            down = 1
            up = 1
            while j - left > 0 and map[i][j - left] < map[i][j]:
                left += 1
            while j + right < row_len - 1 and map[i][j + right] < map[i][j]:
                right += 1
            while i - up > 0 and map[i - up][j] < map[i][j]:
                up += 1
            while i + down < map_len - 1 and map[i + down][j] < map[i][j]:
                down += 1
            scenic_map[i][j] = left * right * up * down
            if scenic_map[i][j] == 599760:
                print(left, right, up, down)
    result = max([max(row) for row in scenic_map])
    print(result)


if __name__ == "__main__":
    solve()
