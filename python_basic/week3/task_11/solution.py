string = input()

print('YES' if string.lower()[::-1] == string.lower() else 'NO')
