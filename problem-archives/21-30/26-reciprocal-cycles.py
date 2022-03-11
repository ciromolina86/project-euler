"""
Reciprocal cycles

Problem 26
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import math
import time


# from stackoverflow
def divide(a, b):
    """Returns the decimal representation of the fraction a / b in three parts:
    integer part, non-recurring fractional part, and recurring part."""
    assert b > 0
    integer = a // b
    remainder = a % b
    seen = {remainder: 0}  # Holds position where each remainder was first seen.
    digits = []
    while True:  # Loop executed at most b times (as remainders must be distinct)
        remainder *= 10
        digits.append(remainder // b)
        remainder = remainder % b
        if remainder in seen:  # Digits have begun to recur.
            where = seen[remainder]
            return (integer, digits[:where], digits[where:])
        else:
            seen[remainder] = len(digits)


def driver():
    maxRecurringCycles = 0
    maxRecurringCyclesNum = 0

    for denom in range(2, 1000):
        (i, f, r) = divide(1, denom)

        if len(r) > maxRecurringCycles:
            maxRecurringCyclesNum = denom

        maxRecurringCycles = max(maxRecurringCycles, len(r))

        # print(f'1/{denom}= {i}.{"".join(map(str, f))}({"".join(map(str, r))})')

    print(maxRecurringCyclesNum)


# https://github.com/dotzero/project-euler-python/blob/master/problem_26.py
def longestRecurringCycle():
    num = longest = 1
    for n in range(3, 1000, 2):
        if n % 5 == 0:
            continue

        p = 1
        while (10 ** p) % n != 1:
            p += 1

        if p > longest:
            num, longest = n, p

    print(num)


def main():
    longestRecurringCycle()


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()
    print(f"{(end - start):.6f} seconds")
