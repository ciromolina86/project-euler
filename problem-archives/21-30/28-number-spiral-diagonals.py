"""
Number spiral diagonals

Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import math

import numpy as np


def isMultipleOf2(arg):
    """check if argument is multiple de 23"""
    if arg % 2 == 0:
        return True
    else:
        return False


def isEven(arg):
    """check if argument is even"""
    return isMultipleOf2(arg)


def isOdd(arg):
    """check if argument is odd"""
    return not isMultipleOf2(arg)


def getSumSpiralDiagonals(dim):
    """https://www.educative.io/edpresso/how-to-solve-the-number-spiral-diagonals-problem"""
    n = (dim - 1) / 2  # compute n
    return (3 + 2 * n * (8 * n ** 2 + 15 * n + 13)) / 3  # compute the diagonals summation


def spiralMatrix(dim=5):
    matrix = np.zeros(dim * dim).reshape(dim, dim)
    positions = spiralPositionGenerator(dim)

    if isOdd(dim):
        xo, yo = (dim - 1) // 2, (dim - 1) // 2
        matrix[xo][yo] = 1

        for num in range(2, dim * dim + 1):
            x, y = next(positions)
            matrix[yo + y][xo + x] = num

        return matrix
    else:
        print(f'Entered dimension ({dim}) is an even number, matrix requires an odd number. please try again')


def spiralPositionGenerator(dim):
    """https://stackoverflow.com/questions/3706219/algorithm-for-iterating-over-an-outward-spiral-on-a-discrete-2d-grid-from-the-or"""

    # (dx, dy) is a vector - direction in which we move right now
    dx, dy = (1, 0)

    # length of current segment
    segment_length = 1

    # current position (x, y) and how much of current segment we passed
    x, y = (0, 0)
    segment_passed = 0

    for i in range(dim * dim - 1):
        # make a step, add 'direction' vector (dx, dy) to current position (x, y)
        x += dx
        y += dy
        segment_passed += 1
        # print(f'{i} - {x},{y}')
        yield x, y

        if segment_passed == segment_length:
            # done with current segment
            segment_passed = 0

            # 'rotate' directions
            buffer = dx
            dx = -dy
            dy = buffer

            # increase segment length if necessary
            if dy == 0:
                segment_length += 1


def getSumDiagonals(matrix: np.ndarray):
    dim = len(matrix)
    if math.sqrt(matrix.size) == dim:
        print(f'matrix is square ({dim}x{dim})')

        if isOdd(dim):
            print(f'matrix dim is odd')
            sumDiag1 = sum(matrix.diagonal())
            sumDiag2 = sum(np.fliplr(matrix).diagonal())
            return sumDiag1 + sumDiag2 - matrix[dim // 2][dim // 2]
        else:
            print(f'matrix dim is even')
            sumDiag1 = sum(matrix.diagonal())
            sumDiag2 = sum(np.fliplr(matrix).diagonal())
            return sumDiag1 + sumDiag2


def main():
    dimension = 5
    matrix = spiralMatrix(dim=dimension)
    print()
    print(matrix)

    print()
    print(getSumDiagonals(matrix))

    sumSpiralDiagonals = getSumSpiralDiagonals(dim=dimension)
    print()
    print(sumSpiralDiagonals)


if __name__ == '__main__':
    main()
