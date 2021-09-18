a = input().split(' ')
a = list(map(int, a))

maxEl = max(a)
maxInd = a.index(maxEl)

print(f'{maxEl} {maxInd}')
