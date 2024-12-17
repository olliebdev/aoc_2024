def main():
    input_file = "input"
    left_numbers, right_numbers = read_input(input_file)
    total_distance = find_distance(left_numbers, right_numbers)
    print(f"Total distance: {total_distance}")
    similarity_score = find_similarity_score(left_numbers, right_numbers)
    print(f"Similarity score: {similarity_score}")


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

# Part 2

def find_similarity_score(left_numbers, right_numbers):
    count = 0
    total_score = 0
    for left_number in left_numbers:
        count = 0
        for right_number in right_numbers:
            if left_number == right_number:
                count += 1
        total_score += left_number * count
    return total_score

if __name__ == "__main__":
    main()
