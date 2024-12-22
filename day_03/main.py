import re


def main():
    input_file = read_input("input")
    parsed_input = parse_regex(input_file)
    print(f"Puzzle Answer: {resolve_instructions(parsed_input)}")


def read_input(input):
    with open(input, "r") as file:
        lines = file.readlines()
        return lines


def parse_regex(input):
    regex_pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(regex_pattern, str(input))

    return matches


def resolve_instructions(input):
    total = 0
    for item in input:
        numbers = re.findall(r"\d+", item)
        result = int(numbers[0]) * int(numbers[1])
        total += result
    return total


if __name__ == "__main__":
    main()
