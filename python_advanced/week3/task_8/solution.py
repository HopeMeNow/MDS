import json

N = int(input())
words = []

for i in range(N):
    words.append(input())

file_name = input()

search_index = {}

for word in words:
    prefix_1 = word[0]
    level_2 = search_index.setdefault(prefix_1, {})
    prefix_2 = word[:2]
    level_3 = level_2.setdefault(prefix_2, [])
    level_3.append(word)
    level_3.sort()

with open(file_name, 'w') as f:
    dump = json.dumps(search_index)
    f.write(dump)
