N = int(input())
numbers = {}

for i in range(N):
    number = input()
    comparison_n = 0
    for k in range(len(number)//2):
        comparison_n += int(number[k]) - int(number[-(k+1)])
    numbers[int(number)] = comparison_n

numbers = sorted(numbers.items())
numbers = sorted(numbers, key=lambda item: item[1])

result = list(zip(*numbers))[0]
print(*result, sep='\n')
