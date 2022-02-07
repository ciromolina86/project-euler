"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math
import numpy as np


def isMultiple(mul, of):
    return mul % of == 0


def leastCommonMultiple(start=1, stop=10):
    """
    Get the smallest number that can be divided by each of the numbers from start to stop,
    a.k.a least common multiple (lcm)

    If none of a1,a2,...,ar is zero, then
    lcm(a1,a2,...,ar) = lcm(lcm(a1,a2,...,ar-1), ar)
    source: https://en.wikipedia.org/wiki/Least_common_multiple
    """
    lcm = 1

    for i in range(start, stop + 1):
        lcm = math.lcm(i, lcm)

    return lcm


if __name__ == '__main__':
    import time

    start = time.time()

    print(leastCommonMultiple(start=1, stop=20))

    end = time.time()
    print(f"{end - start} seconds")
