def main():
    input_file = "input"
    left_numbers, right_numbers = read_input(input_file)
    total_distance = find_distance(left_numbers, right_numbers)
    print(total_distance)

def read_input(input_file):
    left_numbers = []
    right_numbers = []
    with open(input_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            split_line = line.split()
            left_numbers.append(int(split_line[0]))
            right_numbers.append(int(split_line[1]))
    return left_numbers, right_numbers

def find_distance(left_numbers, right_numbers):
    distances = []
    left_numbers.sort()
    right_numbers.sort()
    for i in range(len(left_numbers)):
        distances.append(abs(left_numbers[i] - right_numbers[i]))
    return sum(distances)


if __name__ == "__main__":
    main()
