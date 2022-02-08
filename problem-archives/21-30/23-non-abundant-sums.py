"""
Non-abundant sums

Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time


def getProperDivisor(n):
    """Get all the proper divisors of a given number"""
    return [1] + [num for num in range(2, n // 2 + 1) if n % num == 0]


def isPerfectNumber(n):
    return n == sum(getProperDivisor(n))


def isDeficientNumber(n):
    return sum(getProperDivisor(n)) < n


def isAbundantNumber(n):
    return sum(getProperDivisor(n)) > n


if __name__ == '__main__':
    start = time.time()

    lim = 28123
    abundantNumbers = [num for num in range(1, lim + 1) if isAbundantNumber(num)]
    abundantSumNumbers = set([x + y for x in abundantNumbers for y in abundantNumbers if (x + y) < lim])
    nonAbundantSumNumbers = [num for num in range(1, lim) if num not in abundantSumNumbers]

    # print(abundantSumNumbers)
    # print()
    # print(nonAbundantSumNumbers)
    # print()
    print(sum(nonAbundantSumNumbers))

    end = time.time()
    print(f"{(end - start):.6f} seconds")
