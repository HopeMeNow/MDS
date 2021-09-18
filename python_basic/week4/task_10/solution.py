A = int(input())
B = int(input())

for i in range(A, B+1):
    if str(i) == str(i)[::-1]:
        print(i)
