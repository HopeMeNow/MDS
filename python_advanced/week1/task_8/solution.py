dictionary = {}
counts = []

while True:
    line = input()

    if line == '':
        break
    else:
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 0
                counts.append(0)
            else:
                dictionary[word] += 1
                counts.append(dictionary[word])

print(*counts)
