size = int(input())
current_size = size
counter = 0

available_sizes = sorted(list(map(int, input().split())))

if available_sizes[-1] < size:
    print(counter)
else:
    for available_size in available_sizes:
        if (
            counter == 0 and available_size >= current_size
        ) or (
            counter > 0 and available_size >= current_size + 3
        ):
            counter += 1
            current_size = available_size
    print(counter)
