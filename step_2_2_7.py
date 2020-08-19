def fib_digit(n):
    """
    Вычисление последней цифры чисел Фибонначи

    >>> fib_digit(3)
    2
    >>> fib_digit(1)
    1
    >>> fib_digit(7)
    3
    >>> fib_digit(841645)
    5
    """
    if n < 3:
        return 1

    fib_0, fib_1 = 1, 1

    for i in range(3, n + 1):
        fib_0, fib_1 = fib_1, (fib_0 + fib_1) % 10

    return fib_1


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()