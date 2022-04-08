"""
Coin sums

Problem 31
In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time


def findCombCount(total=200):
    """brute force solution"""
    combCount = 0

    for _2e in range(total // 200 + 1):
        for _1e in range(total // 100 + 1):
            for _50p in range(total // 50 + 1):
                for _20p in range(total // 20 + 1):
                    for _10p in range(total // 10 + 1):
                        for _5p in range(total // 5 + 1):
                            for _2p in range(total // 2 + 1):
                                for _1p in range(total + 1):
                                    value = _2e * 200 + _1e * 100 + _50p * 50 + _20p * 20 + _10p * 10 + _5p * 5 + _2p * 2 + _1p
                                    if value == total:
                                        # print(f"{_2e}x£2 + {_1e}x£1 + {_50p}x50p + {_20p}x20p + {_10p}x10p + {_5p}x5p + {_2p}x2p + {_1p}x1p")
                                        combCount += 1
                                    elif value > total:
                                        break
                                    else:
                                        pass

    print(combCount)


def main():
    findCombCount(200)


if __name__ == '__main__':
    start = time.time()

    findCombCount()

    end = time.time()
    print(f"{(end - start):.6f} seconds")
