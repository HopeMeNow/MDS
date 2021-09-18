N = int(input())

possible = {x for x in range(1, N+1)}
answers = []

while True:
    string = input()
    if string == 'HELP':
        break
    answers.append(set(map(int, string.split())))

first = True
for answer in answers:
    if not first:
        intersection = possible.intersection(answer)
        if len(intersection) <= len(possible)/2.:
            print('NO')
            possible.difference_update(answer)
        else:
            print('YES')
            possible.intersection_update(answer)
    else:
        if len(answer) <= N/2:
            print('NO')
            possible.difference_update(answer)
        else:
            print('YES')
            possible = answer
        first = False
print(*sorted(possible))
