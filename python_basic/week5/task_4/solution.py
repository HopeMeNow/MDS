a = input().split(' ')
k_c = input().split(' ')

k = int(k_c[0])
c = int(k_c[1])

a.insert(k, c)

print(*a, end=' ')
