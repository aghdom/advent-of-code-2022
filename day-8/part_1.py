INPUT_FILE = "input_8.txt"

# TODO Refactor this whole solution as it's very ugly and not readable
def solve():
    map = []
    visibility_map = []
    row_len = None
    with open(INPUT_FILE, "r+") as input_file:
        i = 0
        for row in input_file:
            row = row.strip("\n")
            if not row_len:
                row_len = len(row)
            visibility_map.append([0 for x in range(row_len)])
            map.append(row)
            left = set()
            right = set()
            for j in range(row_len):
                if j == 0:
                    visibility_map[i][j] = 1
                    visibility_map[i][row_len - j - 1] = 1
                if visibility_map[i][j] != 1 and int(row[j]) > max(left):
                    visibility_map[i][j] = 1
                if visibility_map[i][row_len - j - 1] != 1 and int(
                    row[row_len - j - 1]
                ) > max(right):
                    visibility_map[i][row_len - j - 1] = 1
                left.add(int(row[j]))
                right.add(int(row[row_len - j - 1]))
            i += 1
    map_len = len(map)
    for j in range(row_len):
        down = set()
        up = set()
        for i in range(map_len):
            if i == 0:
                visibility_map[i][j] = 1
                visibility_map[map_len - i - 1][j] = 1
            if visibility_map[i][j] != 1 and int(map[i][j]) > max(down):
                visibility_map[i][j] = 1
            if visibility_map[map_len - i - 1][j] != 1 and int(
                map[map_len - i - 1][j]
            ) > max(up):
                visibility_map[map_len - i - 1][j] = 1
            down.add(int(map[i][j]))
            up.add(int(map[map_len - i - 1][j]))
    result = sum([sum(row) for row in visibility_map])
    print(result)


if __name__ == "__main__":
    solve()
