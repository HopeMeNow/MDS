n = int(input())

if n == 0:
    print(0)
else:
    i = 1

    Fn1 = 0
    Fn2 = 1
    Fn = 1

    while Fn != n:
        if Fn > n:
            i = -1
            break
        Fn = Fn1 + Fn2
        Fn1 = Fn2
        Fn2 = Fn
        i += 1

    print(i)
