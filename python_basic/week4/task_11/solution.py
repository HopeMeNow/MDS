s = input()

flag = 0
for i in s.split('.'):
    if i.isnumeric() and int(float(i)) < 256 and int(float(i)) >= 0:
        flag += 1

if flag == 4:
    print('YES')
else:
    print('NO')
