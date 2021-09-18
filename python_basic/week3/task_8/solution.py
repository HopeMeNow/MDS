string = input()

first_str = ''
second_str = ''

if len(string) % 2 > 0:
    first_str = string[:len(string)//2 + 1]
    second_str = string[len(string)//2 + 1:]
else:
    first_str = string[:int(len(string)/2)]
    second_str = string[int(len(string)/2):]

print(second_str+first_str)
