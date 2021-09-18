N = int(input())

dictionary = {}
for i in range(N):
    line = input().split()
    dictionary[line[0]] = line[1]
    dictionary[line[1]] = line[0]

request = input()
print(dictionary[request])
