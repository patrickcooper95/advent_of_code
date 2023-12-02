import re


with open("input.txt", "r") as input_file:
     codes = input_file.readlines()

# Clean up
codes = [code.strip() for code in codes]


def part_one(codes: list):
    super_secret_sum = 0
    for code in codes:
        search_obj = re.search("[0-9](.*[0-9])?", code)
        if not search_obj:
            continue
        sub_string = search_obj.group()

        if len(sub_string) == 1:
            number = int(str(sub_string[0] + sub_string[0]))
        else:
            number = int(str(sub_string[0] + sub_string[-1]))
        print(number)
        super_secret_sum += number
    print(super_secret_sum)


def part_two(codes: list):
    super_secret_sum = 0
    word_to_number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9
    }
    word_match_string = "(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
    reverse_word_match = "(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)"

    for code in codes:
        print(code)
        forward_search = re.search(f"([0-9]|{word_match_string})", code)
        if not forward_search:
            continue
        first_number = forward_search.group()
        last_number = re.search(f"([0-9]|{reverse_word_match})", code[::-1]).group()

        for k, v in word_to_number.items():
            if k in str(last_number):
                last_number = v
            if k in str(first_number):
                first_number = v
        number = int(str(first_number) + str(last_number))
        super_secret_sum += number
        print(number)
    print(super_secret_sum)


part_two(codes)
