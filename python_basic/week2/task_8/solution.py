dollars = float(input())
percents = float(input())
summ = float(input())


def truncate(f, n):
    main_part = str(f).split('.')[0]
    decimal_part = str(f).split('.')[1]
    return float(main_part + '.' + decimal_part[:n])


acc = dollars
i = 0

while acc < summ:
    acc = truncate(acc*percents/100 + acc, 2)
    i += 1

print(int(i))
