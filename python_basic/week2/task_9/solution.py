n = int(input())

i = 2

Fn1 = 0
Fn2 = 1
Fn = 1

while i <= n:
    Fn = Fn1 + Fn2
    Fn1 = Fn2
    Fn2 = Fn
    i += 1

print(Fn)
