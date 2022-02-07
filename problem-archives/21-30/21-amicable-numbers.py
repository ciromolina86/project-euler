"""
Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
from collections import Counter


def getFactors(arg):
    """Get all the factors of a given number"""
    return [num for num in range(1, arg + 1) if arg % num == 0]


def getProperDivisor(arg):
    """Get all the proper divisors of a given number"""
    return getFactors(arg)[:-1]


def isAmicableNumbers(a, b):
    """Check if the numbers a and b are amicable numbers"""
    return a != b and sum(getProperDivisor(a)) == b and sum(getProperDivisor(b)) == a


def d(n):
    """get the sum of all the proper numbers for n"""
    return sum(getProperDivisor(n))


def amicableNumbersGenerator():
    """Generate amicable numbers without limit"""
    i = 1
    while True:
        a = d(i)  # condition 1
        b = d(a)  # condition 2

        if i == b and a != b and a < b:  # conditions check and filter to avoid duplicates
            yield a, b

        i += 1


def myApproach1():
    """my first approach brute force is too slow"""
    amicableNumbers = []
    countAmicableNumbers = 0
    sumAmicableNumbers = 0

    for a in range(220, 10001):
        for b in range(a, 2 * a):
            if isAmicableNumbers(a, b):
                amicableNumbers.append((a, b))
                print(amicableNumbers)

                countAmicableNumbers += 1
                sumAmicableNumbers += a
                sumAmicableNumbers += b

    print(f'{countAmicableNumbers / 2} amicable number pairs')
    print(f'the sum of all of them is {sumAmicableNumbers}')


if __name__ == '__main__':
    start = time.time()

    sumAmicableNumbers = 0
    amicableNumbers = amicableNumbersGenerator()

    while True:
        a, b = next(amicableNumbers)
        if a <= 10_000:
            sumAmicableNumbers = sumAmicableNumbers + a + b
        else:
            break

    print(sumAmicableNumbers)

    end = time.time()
    print(f"{(end - start):.6f} seconds")
