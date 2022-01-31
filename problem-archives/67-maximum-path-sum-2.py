"""
Maximum path sum II

Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (1012) routes every second
it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
import time


def getMaxSumPath(matrix):
    """
    Get the max sum of any path from top to bottom
    :param matrix:
    :return:
    """
    for rowIdx in range(len(matrix) - 2, -1, -1):
        for colIdx in range(len(matrix[rowIdx])):
            matrix[rowIdx][colIdx] += max(matrix[rowIdx + 1][colIdx], matrix[rowIdx + 1][colIdx + 1])
    return matrix[0][0]


def loadData(fileName):
    """load data from file in matrix of integers format"""
    data = []

    with open(fileName, 'r') as f:
        for line in f:
            data.append(list(map(int, [x for x in line.strip().split()])))

    return data


if __name__ == '__main__':
    start = time.time()

    fileName = '../data/p067_triangle.txt'
    data = loadData(fileName)
    print(getMaxSumPath(data))

    end = time.time()
    print(f"{(end - start):.6f} seconds")
