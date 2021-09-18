dimentions = input().split(' ')
arr = []

for _ in range(int(dimentions[0])):
    arr.append(input().split(' '))

transp = []
for i in range(int(dimentions[0])):
    for j in range(int(dimentions[1])):
        if len(transp) <= j:
            transp.append([])
        transp[j].append(arr[i][j])

for k in transp:
    print(*k)
