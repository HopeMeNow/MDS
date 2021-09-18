text = []
dictionary = {}

while True:
    line = input()

    if line == '':
        break
    else:
        text.extend(line.split())

for word in text:
    value = dictionary.setdefault(word, 0)
    dictionary.update({word: value + 1})

dictionary = sorted(dictionary.items())
dictionary = sorted(
    dictionary, key=lambda item: item[1], reverse=True
)

keys = list(zip(*dictionary))[0]
print(*keys, sep='\n')
