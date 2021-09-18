N = int(input())

allNums = {x for x in range(1, N+1)}
yes = set()
no = set()
buffer = ''

while True:
    string = input()
    if string == 'HELP':
        if len(yes) == 0:
            print(*sorted(allNums - no))
        else:
            print(*sorted(yes - no))
        break
    elif string != 'NO' and string != 'YES':
        buffer = set(map(int, string.split(' ')))
    else:
        if string == 'NO':
            no.update(buffer)
        elif string == 'YES':
            if len(yes) == 0:
                yes.update(buffer)
            else:
                yes.intersection_update(buffer)
        buffer = ''
