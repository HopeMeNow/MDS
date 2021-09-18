# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)


# n = int(input())
# print(calc_fib(n))

# a = [[3, 4], [5, 6]]
# b = list(a)
# b[0][0] = 1

# print(a)

# a = [1, 2, 3]
# b = list(a)
# b[0] = 7

# print(a)

a = [1, 2, 3]
b = a

print(a is b, a == b)
