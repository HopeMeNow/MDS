def modify_list(a):
    b = []

    for index, item in enumerate(a):
        if item % 2 > 0:
            b.append(item)

    for item in b:
        a.remove(item)

    for index, item in enumerate(a):
        a[index] = int(item/2)
