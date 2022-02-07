"""
Special Pythagorean triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

import numpy as np
from sympy import symbols, Eq, solve


def isPythagoreanTriplet(*args):
    """

    :param args:
    :return:
    """
    if args[0] ** 2 + args[1] ** 2 == args[2] ** 2:
        return True
    else:
        return False


def getPythagoreanTripletEuclid(m=2, n=1):
    """
    get a Pythagorean Triple by using Euclid’s Formula

    :param m: integer number
    :param n: integer number
    :return:
    """
    if m > n > 0:
        a = 2 * m * n
        b = m ** 2 - n ** 2
        c = m ** 2 + n ** 2
    else:
        print(f'wrong integers were provided. check that m>n>0')

    return a, b, c


def getPythagoreanTripletPerimeter(perimeter=1000):
    """ Solves for triplets whose sum equals perimeter """
    solutions = []
    for a in range(1, perimeter):
        denom = 2 * (perimeter - a)
        num = 2 * a ** 2 + perimeter ** 2 - 2 * perimeter * a
        if denom > 0 and num % denom == 0:
            c = num // denom
            b = perimeter - a - c
            if b > a:
                solutions.append((a, b, c))

    return solutions


if __name__ == '__main__':
    start = time.time()

    pythagoreanTriplet = getPythagoreanTripletPerimeter(1000)
    print(f'{isPythagoreanTriplet(pythagoreanTriplet[0][0], pythagoreanTriplet[0][1], pythagoreanTriplet[0][2])}')
    print(f'the pythagorean triplet where the sum of all elements is 1000 is {pythagoreanTriplet}')
    print(f'the product of the pythagorean triplet is {np.prod(pythagoreanTriplet)}')

    end = time.time()
    print(f"{(end - start):.6f} seconds")
