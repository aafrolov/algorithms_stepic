def fib_mod(n, m):

    if n < 3:
        return 1 % m

    fib_list = [0, 1, 1, 2 % m]

    while fib_list[-1] != 1 or fib_list[-2] != 0:
        fib_list.append((fib_list[-1] + fib_list[-2]) % m)

    return fib_list[n % (len(fib_list)-2)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
