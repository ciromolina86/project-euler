"""
Lattice paths

Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""
import time
import math
from scipy.special import binom


def getBinomialCoefficient(n, k):
    """ Get the binomial coefficient (nCk)

    https://en.wikipedia.org/wiki/Binomial_coefficient

    :param n: number of elements
    :param k: number of combinations
    :return:
    """

    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def getNumberOfLatticePaths(n: int, k: int) -> int:
    """Get the number of lattice paths

    The number of lattice paths from (0,0) to (n,k) is equal to
    the binomial coefficient (n+k)Ck where n >= k >= 0
    https://en.wikipedia.org/wiki/Lattice_path

    :param n: horizontal dimension of matrix
    :param k: vertical dimension of matrix
    :return: number of lattice paths
    """

    return int(binom(n + k, n))


if __name__ == '__main__':
    start = time.time()

    print(getNumberOfLatticePaths(20, 20))

    end = time.time()
    print(f"{(end - start):.6f} seconds")
