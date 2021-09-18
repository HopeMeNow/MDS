def calc_rain_water(h):
    result = 0
    right_max = 0
    left_max = 0
    lo = 0
    hi = len(h) - 1

    while lo <= hi:
        if h[lo] < h[hi]:
            if h[lo] > left_max:
                left_max = h[lo]
            else:
                result += left_max - h[lo]
            lo += 1
        else:
            if h[hi] > right_max:
                right_max = h[hi]
            else:
                result += right_max - h[hi]
            hi -= 1

    return result


# some test code
if __name__ == "__main__":
    test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
    # should print 15
    print(calc_rain_water(test_h))

    test_h = [2, 4, 6, 8, 6, 4, 2]
    # should print 0
    print(calc_rain_water(test_h))

    test_h = [8, 6, 4, 2, 4, 6, 8]
    # should print 18
    print(calc_rain_water(test_h))
