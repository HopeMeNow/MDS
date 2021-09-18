line = input().split()

free_space = int(line[0])
n_users = int(line[1])
users_data = []

for i in range(n_users):
    users_data.append(int(input()))

users_data.sort()
summa = 0
counter = 0
for data in users_data:
    summa += data
    if summa >= free_space:
        break
    counter += 1

print(counter)
