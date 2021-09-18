dimentions = input().split(' ')
arr = []

for _ in range(int(dimentions[0])):
    arr.append(input().split(' '))

rotate = []
for i in range(int(dimentions[0])):
    for j in range(int(dimentions[1])):
        if len(rotate) <= j:
            rotate.append([])
        rotate[j].insert(0, arr[i][j])

for k in rotate:
    print(*k)
