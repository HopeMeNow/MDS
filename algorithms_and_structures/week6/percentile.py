import math
import random


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def naive_find_percentile(a, b, p):
    if len(a) == 0 and len(b) == 0:
        return None

    c = merge(a, b)
    k = (p/100)*len(c)
    return c[math.ceil(k) - 1]


def find_percentile(a, b, p):
    if len(a) == 0 and len(b) == 0:
        return None

    k = math.ceil((p/100)*(len(a) + len(b))) - 1

    if len(a) == 0:
        return b[k]

    if len(b) == 0:
        return a[k]

    k_a = math.floor((p/100)*len(a))
    k_b = k - k_a

    while True:
        k_a_in_range = -1 < k_a < len(a)
        k_b_in_range = -1 < k_b < len(b)

        left_a_smaller_right_b = (
            -1 < k_a - 1 and k_b_in_range and a[k_a-1] < b[k_b]
        )

        left_b_smaller_right_a = (
            -1 < k_b - 1 and k_a_in_range and b[k_b-1] < a[k_a]
        )

        if (
            (left_a_smaller_right_b or k_a - 1 < 0 or k_b >= len(b)) and
            (left_b_smaller_right_a or k_b - 1 < 0 or k_a >= len(a))
        ):
            if k_a_in_range and k_b_in_range:
                return min(a[k_a], b[k_b])
            elif not k_a_in_range and not k_b_in_range:
                return max(a[-1], b[-1])
            else:
                if not k_a_in_range:
                    return b[k_b]
                if not k_b_in_range:
                    return a[k_a]
        else:
            if -1 < k_a - 1 and k_b_in_range and a[k_a-1] > b[k_b]:
                k_a -= 1
                k_b += 1

            if -1 < k_b - 1 and k_a_in_range and b[k_b-1] > a[k_a]:
                k_a += 1
                k_b -= 1


def generate_test_arrays(arrays_max_length=10, arrays_max_range=100):
    random.seed(100)
    arr1 = []
    arr2 = []
    for _ in range(random.randint(0, arrays_max_length)):
        new_value = random.randint(0, arrays_max_range)
        if new_value not in arr1:
            arr1.append(new_value)

    for _ in range(random.randint(0, arrays_max_length)):
        new_value = random.randint(0, arrays_max_range)
        if new_value not in arr2 and new_value not in arr1:
            arr2.append(new_value)

    return sorted(arr1), sorted(arr2)


def test_solution(a, b, p, answer):
    result = find_percentile(a, b, p)

    error_text = 'Test failed\nInput:\na {0}\nb {1}\n\
        p {2}\nOutput: {3}\nCorrect answer: {4}'

    assert result == answer, error_text.format(a, b, p, result, answer)
    print(f'Test passed. Answer: {result}')


def stress_test(tests_number=10, arrays_max_length=100, arrays_max_range=1000):
    random.seed(100)
    for _ in range(tests_number):
        p = random.randint(1, 10) * 10
        a, b = generate_test_arrays()

        answer = naive_find_percentile(a, b, p)
        test_solution(a, b, p, answer)


def max_test():
    random.seed(100)
    p = random.randint(1, 10) * 10
    a, b = generate_test_arrays(
        arrays_max_length=10000,
        arrays_max_range=100000
    )

    test_solution(a, b, p, naive_find_percentile(a, b, p))
    print('Max test passed')


# some test code
if __name__ == "__main__":
    stress_test()
    max_test()

    # Unit tests
    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    test_solution(test_a, test_b, test_p, 7)

    test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    test_solution(test_a, test_b, test_p, 6)

    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    test_solution(test_a, test_b, test_p, 20)

    test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    test_solution(test_a, test_b, test_p, 20)
