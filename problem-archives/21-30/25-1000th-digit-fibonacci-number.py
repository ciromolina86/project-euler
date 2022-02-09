"""
1000-digit Fibonacci number

Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time


def fibonacciSequenceGenerator():
    """Generate an infinite sequence of Fibonacci numbers"""
    seq = [1, 1]
    for num in seq:
        yield num

    while True:
        num = sum(seq)
        seq.append(num)
        seq.pop(0)

        yield num


def main():
    num = nth = 0
    fibo = fibonacciSequenceGenerator()

    while not (len(str(num)) == 1000):
        num = next(fibo)
        nth += 1
    print(f'{nth}th - {num}')


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()
    print(f"{(end - start):.6f} seconds")
