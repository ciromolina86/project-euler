"""
Digit fifth powers

Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def isPowerSumNumber(num, power):
    digits = [int(char) for char in str(num)]
    powerSum = 0

    for digit in digits:
        powerSum += digit ** power

    return num == powerSum


def main():
    nums = []
    for num in range(1_000_000):
        if isPowerSumNumber(num, 5):
            nums.append(num)
    print(nums)
    print(sum(nums) - 1)


if __name__ == '__main__':
    main()
