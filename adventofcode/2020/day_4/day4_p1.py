import sys
from functools import reduce

def add_item_to_dic(dic, item):
    k, v = item.split(":")
    dic[k] = v
    return dic

def arr_passport_to_dic(arr_passport):
    return reduce(lambda dic, item: add_item_to_dic(dic, item), arr_passport, {})

def is_valid_passport(passport):
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in mandatory_fields:
        if field not in passport:
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
