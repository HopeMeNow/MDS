a = float(input())
b = float(input())
operation = input()


def calc(a, b, operation):
    operations = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b,
    }

    print(operations[operation])


calc(a, b, operation)
