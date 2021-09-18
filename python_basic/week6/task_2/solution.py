a = int(input())


def is_prime(a):
    prime = True

    if a == 1 or a == 0:
        prime = False

    for i in range(2, abs(a), 1):
        if a == 1 or a == 0 or a % i == 0:
            prime = False
            break

    print('YES' if prime else 'NO')


is_prime(a)
