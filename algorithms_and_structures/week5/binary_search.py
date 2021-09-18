import random
count = 0


def bsearch1(arr, key):
    low, high = 0, len(arr)-1

    # if high != 0 and arr[low] == key:
    #     return low

    while high - low > 1:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid
        else:
            high = mid
    return None


def bsearch2(arr, key, left=0, right=None):
    if right is None:
        right = len(arr)
    if right < left:
        return None
    middle = (left + right) >> 1
    if middle > len(arr) - 1:
        return None
    if arr[middle] > key:
        return bsearch2(arr, key, left, middle)
    if arr[middle] < key:
        return bsearch2(arr, key, middle + 1, right)
    return middle


def bsearch3(arr, key):
    global count
    count += 1
    print('bsearch3', count)
    n = len(arr)
    if n < 2:
        return (0 if (n == 1 and arr[0] == key) else None)
    m = int(0.5 * n)
    if arr[m] > key:
        return bsearch3(arr[:m], key)
    result = bsearch3(arr[m:], key)
    return (result + m if result is not None else None)


def generate_test_array(array_max_length=100, array_max_range=1000):
    arr = []
    for _ in range(random.randint(1, array_max_length)):
        new_value = random.randint(-array_max_range, array_max_range)
        if new_value not in arr:
            arr.append(new_value)

    return sorted(arr)


def generate_test():
    arr = generate_test_array()
    index = random.randint(0, len(arr) - 1)
    return arr, arr[index], index


def test_search(search_f):
    for _ in range(1000):
        arr, number, answer = generate_test()
        result = search_f(arr, number)
        error = 'arr: {0}\nnumber: {1}\nanswer: {2}\nresult: {3}'

        assert result == answer, error.format(arr, number, answer, result)


if __name__ == "__main__":
    # test_search(bsearch1)
    # test_search(bsearch2)
    # test_search(bsearch3)
    arr = [-1, 20]
    # arr = []
    # arr = [-995, 986]
    # arr = [7]
    # for _ in range(4096):
    #     new_value = random.randint(-1000, 1000)
    #     arr.append(0)
    # print('len', len(arr))
    # print(bsearch1(arr, 0))
    print(bsearch2(arr, 2))
    # print(bsearch1(sorted(arr), -0))
