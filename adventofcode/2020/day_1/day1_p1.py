import sys

def main():
    nums = []
    for line in sys.stdin:
        nums.append(int(line.rstrip()))

    i = 0
    while i < len(nums) - 1:
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == 2020:
                print(f"{nums[i]} {nums[j]}")
                print(f"{nums[i] * nums[j]}")
                return
            j += 1
        i += 1

    print(len(nums))

if __name__ == "__main__":
    main()
