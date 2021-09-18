a = input()
h = input()

if a == '':
    print(1)
else:
    a = a.split(' ')
    for i, item in enumerate(a):
        if h > item:
            print(i+1)
            break
        elif h <= item and i + 1 == len(a):
            print(i+2)
            break
