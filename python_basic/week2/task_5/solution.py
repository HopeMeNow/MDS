import math

volume = int(input())
minutes = int(input())
number = int(input())

print(math.ceil(number/volume)*minutes*2)
