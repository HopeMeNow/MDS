import json

file_name = input()

with open(file_name) as f:
    data = f.read()
    data = json.loads(data)

links = []


def compose(result, dictionary):
    for in_key, in_value in dictionary.items():
        if len(in_value) == 0:
            links.append(result + '/' + in_key)
        else:
            compose(result + '/' + in_key, in_value)


for key, value in data.items():
    compose(key, value)

links.sort()
print(*links, sep='\n')
