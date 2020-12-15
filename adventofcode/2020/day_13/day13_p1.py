import sys
from functools import reduce


def add_valid_bus(buses, id):
    if id == "x": return buses

    buses.append(int(id))
    return buses

def main():
    for index, line in enumerate(sys.stdin):
        if index == 0:
            initial_time = int(line.rstrip())
        elif index == 1:
            buses = reduce(lambda x, y: add_valid_bus(x, y), line.rstrip().split(","), [])

    min_time = initial_time
    for bus in buses:
        waiting_time = bus - (initial_time % bus)
        if waiting_time < min_time:
            min_time = waiting_time
            result = bus * waiting_time

    print(result)


if __name__ == "__main__":
    main()
