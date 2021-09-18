a = input().split(' ')
n = {}

for i in a:
    if i not in n:
        n[i] = 1
    else:
        n[i] = n[i] + 1

for k in n:
    if n[k] == 1:
        print(k, end=' ')
