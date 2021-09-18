users = {}

while True:
    line = input()

    if line == '':
        break
    else:
        user_name, item, units = line.split()
        units_value = users.setdefault(user_name, {}).setdefault(item, 0)
        users[user_name][item] = units_value + int(units)


def get_key(item):
    print(item)
    return item[1]


users = dict(sorted(users.items()))

for user in users:
    users[user] = sorted(users[user].items())
    print(f'{user}:')
    for purchase in users[user]:
        print(f'{purchase[0]} {purchase[1]}')
