n = int(input())

factorial = 1
summ = 0
for i in range(1, n+1):
    factorial = factorial*i
    summ = summ + factorial

print(summ)
