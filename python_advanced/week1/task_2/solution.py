num = input().split()

if num[0] != '':
    num_dict = {}

    for item in num:
        if item not in num_dict:
            print('NO')
            num_dict[item] = 1
        else:
            print('YES')
