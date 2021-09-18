line_1 = map(int, input().split())
line_2 = map(int, input().split())

result = map(lambda pair: int(pair[0] != pair[1]), zip(line_1, line_2))

print(*result, sep=' ')
