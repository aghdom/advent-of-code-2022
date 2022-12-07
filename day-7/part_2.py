INPUT_FILE = "input_7.txt"


def calculate_dir_sizes(filesystem: dict) -> dict:
    result = {}

    def sum_files(dir: dict, name: str) -> int:
        sum = 0
        for key, value in dir.items():
            if key == "..":
                continue
            if isinstance(value, dict):
                breadcrumb = f"{name}.{key}"
                total = sum_files(value, breadcrumb)
                result[breadcrumb] = total
                sum += total
            else:
                sum += value
        return sum

    result["/"] = sum_files(filesystem, "/")
    return result


def solve():
    filesystem = {}
    prev_dir = None
    curr_dir = filesystem
    with open(INPUT_FILE, "r") as file:
        while file:
            row = file.readline()
            row = row.strip("\n")
            if row.startswith("$"):
                parts = row.split(" ")
                cmd = parts[1]
                match cmd:
                    case "cd":
                        target = parts[2]
                        match target:
                            case "/":
                                curr_dir = filesystem
                            case "..":
                                curr_dir = prev_dir if prev_dir else filesystem
                                prev_dir = curr_dir[".."]
                            case other:
                                curr_dir[".."] = prev_dir
                                prev_dir, curr_dir = curr_dir, curr_dir[target]
                    case "ls":
                        while True:
                            pointer = file.tell()
                            line = file.readline()
                            line = line.strip("\n")
                            if line.startswith("$") or line == "":
                                file.seek(pointer)
                                break
                            parts = line.split(" ")
                            if parts[0] == "dir":
                                curr_dir[parts[1]] = {}
                            else:
                                curr_dir[parts[1]] = int(parts[0])
                    case other:
                        print(f"Unknown command!: {cmd}")
                        break
            else:
                break
    result = calculate_dir_sizes(filesystem)
    sizes = list(result.values())
    sizes.sort()

    max_memory = 70000000
    req_memory = 30000000
    curr_memory = max_memory - sizes[-1]
    to_delete = req_memory - curr_memory

    for size in sizes:
        if size >= to_delete:
            print(size)
            return


if __name__ == "__main__":
    solve()
