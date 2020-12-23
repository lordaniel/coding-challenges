import sys
input = sys.stdin.readline
from functools import reduce


def add_div(arr, div):
    if div != "0": return arr.append(div)

    return arr


def check_fair(n, divs):
    for x in divs:
        if n % x > 0: return False

    return True


def gen_divs(n):
    divs = {}
    for x in range(0, len(n)):
        div = int(n[x])
        if div > 1: divs[div] = div
    return divs.keys()


def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        curr_num = n

        while True:
            divs = gen_divs(str(curr_num))
            if check_fair(curr_num, divs): break
            curr_num += 1

        print(curr_num)


if __name__ == "__main__":
    main()
