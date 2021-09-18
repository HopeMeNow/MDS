dictionary = {}
text = []

while True:
    line = input()

    if line == '':
        break
    line_arr = line.split()
    text.extend(line_arr)

for index, word in enumerate(text):
    word_inds = dictionary.setdefault(word, [])
    if len(word_inds) == 0:
        print('-1', end=' ')
    else:
        print(word_inds[-1], end=' ')
    word_inds.append(index)
