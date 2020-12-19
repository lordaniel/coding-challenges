import sys
import re


def set_mask_bit(bit, value):
    if bit == "X": return value

    return bit


def main():
    mem = {}
    mask_0 = 000000000000000000000000000000000000
    mask_1 = 111111111111111111111111111111111111

    for line in sys.stdin:
        input = line.rstrip().split()
        if "mem" in input[0]:
            mem_index = int(re.findall('\d+', input[0])[0])
            value = int(input[2])
            value = value | mask_0
            value = value & mask_1
            mem[mem_index] = value
        else:
            mask_0 = int("".join(list(map(lambda x: set_mask_bit(x, "0"), input[2]))), 2)
            mask_1 = int("".join(list(map(lambda x: set_mask_bit(x, "1"), input[2]))), 2)

    print(sum(mem.values()))


if __name__ == "__main__":
    main()
