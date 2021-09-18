percents = float(input())
dollars = float(input())
cents = float(input())
years = float(input())


def truncate(f, n):
    main_part = str(f).split('.')[0]
    decimal_part = str(f).split('.')[1]
    return float(main_part + '.' + decimal_part[:n])


acc = dollars + cents/100
i = 0

while i < years:
    acc = truncate(acc*percents/100 + acc, 2)
    i += 1

print('{} {}'.format(int(acc), int((acc - int(acc))*100)))
