"""
Найдите наибольший общий делитель двух чисел
"""


def gcd(a, b):
    """
    >>> gcd(18, 35)
    1
    >>> gcd(14159572, 63967072)
    4
    """
    if a == 0 or b == 0:
        return a + b

    if a >= b:
        return gcd(a % b, b)

    return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()