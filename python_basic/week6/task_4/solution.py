a = int(input())
n = int(input())


def power(a, n):
    if n == 0:
        print(1)
    else:
        b = a
        for _ in range(2, n+1):
            b = b*a

        print(b)


power(a, n)
