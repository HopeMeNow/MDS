def lines(a):
    first_pointer = 0
    second_pointer = 0
    del_numbers = 0
    while len(a) > 1:
        if a[second_pointer+1] != a[second_pointer]:
            if len(a[first_pointer:second_pointer + 1]) >= 3:
                del a[first_pointer:second_pointer + 1]
                del_numbers += second_pointer - first_pointer + 1
                first_pointer = 0
                second_pointer = 0
            else:
                second_pointer += 1
                if second_pointer == len(a) - 1:
                    break
                first_pointer = second_pointer
        else:
            second_pointer += 1
            if second_pointer == len(a) - 1:
                if len(a[first_pointer:second_pointer + 1]) >= 3:
                    del a[first_pointer:second_pointer + 1]
                    del_numbers += second_pointer - first_pointer + 1
                break

    return del_numbers


# # some test code
# if __name__ == "__main__":
# test_a = [2, 2, 1, 1, 1, 2, 1]
# # should print 6
# print(lines(test_a))

# test_a = [0, 0, 0, 0, 0]
# # should print 5
# print(lines(test_a))

# test_a = [2, 3, 1, 4]
# # should print 0
# print(lines(test_a))
