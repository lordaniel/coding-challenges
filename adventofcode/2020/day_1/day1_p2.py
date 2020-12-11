import sys

def main():
    nums = []
    for line in sys.stdin:
        nums.append(int(line.rstrip()))

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(f"{nums[i]} {nums[j]} {nums[k]}")
                    print(f"{nums[i] * nums[j] * nums[k]}")
                    return

if __name__ == "__main__":
    main()
