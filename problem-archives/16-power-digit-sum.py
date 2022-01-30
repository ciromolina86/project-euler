"""
Power digit sum

Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
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

    print(getDigitSum(2 ** 1000))

    end = time.time()
    print(f"{(end - start):.6f} seconds")
