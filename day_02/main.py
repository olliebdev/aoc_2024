def main():
    input_file = read_input("input")
    print(safe_count(input_file))


def read_input(input_file):
    with open(input_file, "r") as file:
        lines_unclean = file.readlines()
        lines = [line.strip() for line in lines_unclean]
        return lines


def safe_count(input_file):
    total_safe = 0
    for i in range(len(input_file)):
        is_increasing = True
        is_decreasing = True
        is_safe = True
        split_report = str(input_file[i]).split()
        print(f"Report {i+1}: {split_report}")  # Debug
        for j in range(len(split_report) - 1):
            current_num = int(split_report[j])
            next_num = int(split_report[j + 1])
            difference = abs(current_num - next_num)
            print(
                f"Comparing {current_num} -> {next_num}, difference: {difference}"
            )  # Debug
            if difference < 1 or difference > 3:
                is_safe = False
                print("Invalid difference, not safe!")  # Debug
                break
            elif next_num > current_num:
                is_decreasing = False
            elif next_num < current_num:
                is_increasing = False
            else:
                is_safe = False
                break
        if is_increasing and is_decreasing:
            is_safe = False
        elif not is_increasing and not is_decreasing:
            is_safe = False
        if is_safe:
            print(f"Report {i+1} is safe!")  # Debug
            total_safe += 1
        else:
            print(f"Report {i+1} is not safe!")  # Debug
    return total_safe


# TODO part 2

if __name__ == "__main__":
    main()

