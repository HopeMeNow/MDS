n_countries = int(input())

countries = {}

for i in range(n_countries):
    line = input().split()
    countries[line[0]] = line[1:]

n_requests = int(input())
requests = []

for j in range(n_requests):
    requests.append(input())

answers = []

for request in requests:
    for name, cities in countries.items():
        if request in cities:
            answers.append(name)

print(*answers, sep='\n')
