N = int(input())

dictionary = {}
for i in range(N):
    line = input()
    lower_line = line.lower()
    if lower_line not in dictionary:
        dictionary[lower_line] = [line]
    else:
        dictionary[lower_line].append(line)

hw = input().split()

result = 0
for word in hw:
    if word.lower() not in dictionary:
        n_capitals = sum(1 for letter in word if letter.isupper())
        if n_capitals != 1:
            result += 1
    else:
        if word not in dictionary[word.lower()]:
            result += 1

print(result)
