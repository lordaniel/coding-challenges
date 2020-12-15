import sys
import time
from functools import reduce


def add_valid_bus(buses, id):
    if id == "x":
        buses.append(-1)
    else:
        buses.append(int(id))
    return buses


def check_result(dic, buses, num):
    for x in buses:
        if dic[x] != num % x:
            return False
    return True


def main():
    for index, line in enumerate(sys.stdin):
        if index == 1:
            buses = reduce(lambda x, y: add_valid_bus(x, y), line.rstrip().split(","), [])

    dic = {}
    for i, x in enumerate(buses):
        if x != -1:
            dic[x] = (x - (i % x)) % x

    partial_buses = []
    result = 0

    for x in filter(lambda x: x != -1, buses):
        partial_buses.append(x)
        while True:
            if check_result(dic, partial_buses, result): break

            next_value = 1
            for k in partial_buses[:-1]:
                next_value *= k
            result += next_value


    print(result)


if __name__ == "__main__":
    main()
