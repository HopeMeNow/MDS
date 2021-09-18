N = int(input())
dictionary = {}

for i in range(N):
    word = input()
    dictionary[word] = len(word)

dictionary = sorted(dictionary.items(), key=lambda item: item[0][::-1])
dictionary = sorted(dictionary, key=lambda item: item[1])

words = list(zip(*dictionary))[0]
print(*words, sep='\n')
