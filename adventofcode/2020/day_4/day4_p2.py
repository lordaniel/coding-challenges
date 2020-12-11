import sys
from functools import reduce


def add_item_to_dic(dic, item):
    k, v = item.split(":")
    dic[k] = v
    return dic


def arr_passport_to_dic(arr_passport):
    return reduce(lambda dic, item: add_item_to_dic(dic, item), arr_passport, {})


def is_valid_number(field, min_value, max_value):
    if not field.isnumeric():
        return False

    return int(field) in  range(min_value, max_value)


def is_valid_height(field):
    if "cm" in field:
        return is_valid_number(field[:len(field)-2], 150, 194)
    elif "in" in field:
        return is_valid_number(field[:len(field)-2], 59, 77)
    return False


def is_valid_hair_color(field):
    if field[0] != "#":
        return False

    for x in range(1, len(field)):
        if field[x] not in "0123456789abcdef":
            return False
    return True


def is_valid_eye_color(field):
    return field in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_id(field):
    return len(field) == 9


def is_valid_passport(passport):
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in mandatory_fields:
        if field not in passport:
            return False
        elif (
            (field == "byr" and not is_valid_number(passport[field], 1920, 2003)) or
            (field == "iyr" and not is_valid_number(passport[field], 2010, 2021)) or
            (field == "eyr"  and not is_valid_number(passport[field], 2020, 2031)) or
            (field == "hgt"  and not is_valid_height(passport[field])) or
            (field == "hcl" and not  is_valid_hair_color(passport[field])) or
            (field == "ecl" and not is_valid_eye_color(passport[field])) or
            (field == "pid" and not is_valid_id(passport[field]))
        ):
            return False
    return True


def main():
    passports = []
    new_passport = True
    for line in sys.stdin:
        arr_line = line.rstrip().split()

        if new_passport:
            passports.append(arr_line)
        else:
            passports[-1] += arr_line

        new_passport = len(arr_line) == 0

    count = 0
    for passport in map(lambda x: arr_passport_to_dic(x), passports):
        if is_valid_passport(passport):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
