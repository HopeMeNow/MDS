a = []

for i in range(8):
    a.append(tuple(map(int, input().split(' '))))

zipped = list(zip(*a))
is_first_coord_different = len(zipped[0]) == len(set(zipped[0]))
is_second_coord_different = len(zipped[1]) == len(set(zipped[1]))
is_different_diagonal = False

for k in range(8):
    for j in range(1, 8):
        if not (abs(a[k][0] - a[j][0]) == abs(a[k][1] - a[j][1])):
            is_different_diagonal = True


if (
    is_first_coord_different and
    is_second_coord_different and
    is_different_diagonal
):
    print('NO')
else:
    print('YES')
