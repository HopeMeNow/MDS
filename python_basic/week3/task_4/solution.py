import math

a = float(input())

if a > 0:
    print(round(math.log(a), 5))
else:
    print('Undefined')
