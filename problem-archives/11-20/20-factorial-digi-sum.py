"""
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import math
import time


def getDigitSum(num):
    """
    Get the individual digits sum

    :param num: any number
    :return: digits sum
    """
    digits = [int(d) for d in str(num)]
    return sum(digits)


if __name__ == '__main__':
    start = time.time()

    print(getDigitSum(math.factorial(100)))

    end = time.time()
    print(f"{(end - start):.6f} seconds")
