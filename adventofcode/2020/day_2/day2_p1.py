import sys

def main():
    count = 0
    for line in sys.stdin:
        min_val, max_val, letter, password = line.rstrip().replace("-", " ").replace(":", "").split()
        min_val = int(min_val)
        max_val = int(max_val)
        if password.count(letter) in range(min_val, max_val + 1):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
