accounts = {}
replies = []

while True:
    line = input()
    if line == '':
        break
    command = line.split()
    if command[0] == 'DEPOSIT':
        value = accounts.get(command[1], 0)
        accounts[command[1]] = value + int(command[2])
    if command[0] == 'WITHDRAW':
        value = accounts.get(command[1], 0)
        accounts[command[1]] = value - int(command[2])
    if command[0] == 'BALANCE':
        value = accounts.get(command[1], None)
        if value is None:
            replies.append('ERROR')
        else:
            replies.append(value)
    if command[0] == 'TRANSFER':
        value1 = accounts.get(command[1], 0)
        value2 = accounts.get(command[2], 0)
        accounts[command[1]] = value1 - int(command[3])
        accounts[command[2]] = value2 + int(command[3])
    if command[0] == 'INCOME':
        for account_name, account_value in accounts.items():
            if account_value >= 0:
                accounts[account_name] = account_value + int(
                    account_value*int(command[1])/100
                )

print(*replies, sep='\n')
