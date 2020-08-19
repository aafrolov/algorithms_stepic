def fib(n):
    """
    Вычисление чисел Фибонначи

    >>> fib(3)
    2
    >>> fib(1)
    1
    >>> fib(7)
    13
    """
    if n < 3:
        return 1

    fib_list = [1, 1]
    for i in range(3, n + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
