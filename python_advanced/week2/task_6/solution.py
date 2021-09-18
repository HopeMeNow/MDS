kms = list(map(int, input().split()))
prices = list(map(int, input().split()))

kms.sort()
prices.sort(reverse=True)

array = zip(kms, prices)
summa = 0
for item in array:
    summa += item[0]*item[1]
print(summa)
