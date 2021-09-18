def largest_palindrome(s):
    result = s[0]

    for i in range(len(s)):
        left_pointer = i
        right_pointer = i

        while True:
            left_pointer -= 1
            right_pointer += 1
            flag = 0

            if left_pointer >= 0 and right_pointer < len(s):
                if s[left_pointer] == s[right_pointer]:
                    substr = s[left_pointer:right_pointer+1]
                    if len(substr) > len(result):
                        result = substr
                        flag = 1

                if (
                    right_pointer + 1 < len(s) and
                    right_pointer == i+1 and
                    s[i] == s[right_pointer]
                ):
                    print('left_pointer', left_pointer)
                    right_pointer += 1
                    if s[left_pointer] == s[right_pointer]:
                        substr = s[left_pointer:right_pointer+1]
                        if len(substr) > len(result):
                            result = substr
                            flag = 1

            if not flag:
                break

    return result


test_s = 'AAAAA'
print(largest_palindrome(test_s))

# # some test code
# if __name__ == "__main__":
test_s = 'ABBCB'
# should print BCB
print(largest_palindrome(test_s))

test_s = 'ABACABAD'
# should print ABACABA
print(largest_palindrome(test_s))

test_s = 'ABCDE'
# should print A
print(largest_palindrome(test_s))

test_s = 'BBBB'
# should print BB
print(largest_palindrome(test_s))

test_s = 'ABBC'
# should print BB
print(largest_palindrome(test_s))

test_s = 'ABBA'
# should print ABBA
print(largest_palindrome(test_s))

test_s = 'AAAAA'
print(largest_palindrome(test_s))

test_s = 'BBBBBAACCCC'
print(largest_palindrome(test_s))
