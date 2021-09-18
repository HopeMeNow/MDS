isVotes = False
parties = {}
list_parts = []
counter = 0

while True:
    line = input()

    if line == '':
        break
    if line == 'PARTIES:':
        isVotes = False
        continue
    if line == 'VOTES:':
        isVotes = True
        continue

    if not isVotes:
        parties.setdefault(line, 0)
        list_parts.append(line)
    else:
        parties[line] += 1
        counter += 1

for party in list_parts:
    if float(parties[party])/counter >= 0.07:
        print(party)
