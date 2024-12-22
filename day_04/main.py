def main():
    input_file = read_input("input")
    total = find_word(input_file)
    print(f"Total Occurrences: {total}")


def read_input(input_path):
    with open(input_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def find_word(input):
    rows = len(input)
    cols = len(input[0])
    total_count = 0

    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # diag-down-right
        (1, -1),  # diag-down-left
        (-1, 1),  # diag-up-right
        (-1, -1),  # diag-up-left
    ]

    def is_valid_pos(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        word = ""
        for i in range(4):
            new_x, new_y = x + i * dx, y + i * dy
            if not is_valid_pos(new_x, new_y):
                return False
            word += input[new_x][new_y]
        return word == "XMAS"

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "X":
                for dx, dy in directions:
                    if check_word(i, j, dx, dy):
                        total_count += 1

    return total_count


if __name__ == "__main__":
    main()
