import sys


def fib(n):
    n = int(n)
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return b


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("No")
        sys.exit(1)
    else:
        fib(sys.argv[1])
