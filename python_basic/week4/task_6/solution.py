n = int(input())

print('+___ '*n)
for i in range(1, n+1):
    print(f'|{i} / ', end='')
print('\n' + '|__\ '*n)
print('|    '*n)
