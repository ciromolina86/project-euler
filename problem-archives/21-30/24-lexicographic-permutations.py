"""
Lexicographic permutations

Problem 24
A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time


def hasIndexK(a):
    """Check if k index exists in given sequence"""
    if findIndexK(a) is None:
        return False
    else:
        return True


def findIndexK(a):
    """Find the largest index k such that a[k] < a[k + 1].
    If no such index exists, the permutation is the last permutation."""
    n = len(a)
    ks = []

    for i in range(n - 1):
        if a[i] < a[i + 1]:
            ks.append(i)

    if len(ks) == 0:
        return None
    else:
        return max(ks)


def findIndexL(a, k):
    """Find the largest index l greater than k such that a[k] < a[l]."""
    n = len(a)
    ls = []

    if k is not None:
        for i in range(n):
            if a[k] < a[i] and i > k:
                ls.append(i)

    if ls:
        return max(ls)
    else:
        return None


def swapValues(a, k, l):
    """Swap the value of a[k] with that of a[l]"""
    ak = a[k]
    al = a[l]
    a[k] = al
    a[l] = ak

    return a


def reverseSeq(a, k):
    """Reverse the sequence from a[k + 1] up to and including the final element a[n]."""
    head = a[:k + 1]
    tail = a[k + 1:]
    tail = tail[::-1]

    return head + tail


def lexicographicPermutationsGenerator(a):
    """
    The following algorithm generates the next permutation lexicographically after a given permutation.
    It changes the given permutation in-place.

    Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    Find the largest index l greater than k such that a[k] < a[l].
    Swap the value of a[k] with that of a[l].
    Reverse the sequence from a[k + 1] up to and including the final element a[n].

    :param a: given sequence
    :return: next
    """
    yield a

    while hasIndexK(a):
        k = findIndexK(a)
        l = findIndexL(a, k)
        a = swapValues(a, k, l)
        a = reverseSeq(a, k)

        yield a


def debug(a):
    print(a)
    print(hasIndexK(a))
    k = findIndexK(a)
    print(f'k={k}')
    l = findIndexL(a, k)
    print(f'l={l}')
    a = swapValues(a, k, l)
    print(a)
    a = reverseSeq(a, k)
    print(a)


def main(a):
    a = sorted(a)
    lex = lexicographicPermutationsGenerator(a)

    nth = 0
    lexPerm = None

    while nth < 1_000_000:
        lexPerm = next(lex)
        nth += 1

    print(f'{nth}th - {lexPerm}')


if __name__ == '__main__':
    start = time.time()

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a = [0, 1, 2]

    # debug(a)
    main(a)

    end = time.time()
    print(f"{(end - start):.6f} seconds")
