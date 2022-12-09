INPUT_FILE = "input_6.txt"
MARKER_LEN = 4


def solve():
    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            row = row.strip("\n")
            for i in range(len(row) - MARKER_LEN):
                uniq_chars = set(row[i : i + MARKER_LEN])
                if len(uniq_chars) == MARKER_LEN:
                    print(i + MARKER_LEN)
                    return


if __name__ == "__main__":
    solve()
