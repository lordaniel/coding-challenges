import sys
input = sys.stdin.readline


def count_end_chars(string, char):
    counter = 0
    i = len(string) - 1
    while i >= 0 and string[i] == char:
        counter += 1
        i -= 1

    return counter


def main():
    t = int(input())
    for x in range(0,t):
        n = int(input())
        s =input().strip()
        count = count_end_chars(s, ")")
        if count > (len(s) - count):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
