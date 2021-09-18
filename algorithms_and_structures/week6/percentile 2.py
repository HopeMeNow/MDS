def find_percentile(a, b, p):
    pass


# some test code
if __name__ == "__main__":
    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # should print 7
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # should print 6
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # should print 20
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # should print 20
    print(find_percentile(test_a, test_b, test_p))