kms = list(map(int, input().split()))
prices = list(map(int, input().split()))

kms = sorted(enumerate(kms), key=lambda item: item[1])
prices = sorted(enumerate(prices), key=lambda item: item[1], reverse=True)
kms_indexes = list(zip(*kms))[0]
prices_indexes = list(zip(*prices))[0]
indexes_map = zip(kms_indexes, prices_indexes)
indexes_map = sorted(indexes_map, key=lambda item: item[0])

result = list(zip(*indexes_map))[1]
print(*result, sep=' ')
