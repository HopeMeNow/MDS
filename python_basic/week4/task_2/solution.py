a = int(input())
b = int(input())

if b < a:
    b = b - 1
    step = -1
else:
    step = 1
    b = b + 1

for i in range(a, b, step):
    print(i, end=' ')
