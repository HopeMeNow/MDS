# def getZarr(string):
#     n = len(string)
#     z = [0]*n
#     # [L,R] make a window which matches
#     # with prefix of s
#     left, right, k = 0, 0, 0
#     for i in range(1, n):
#         # if i>R nothing matches so we will calculate.
#         # Z[i] using naive way.
#         if i > right:
#             left, right = i, i

#             # R-L = 0 in starting, so it will start
#             # checking from 0'th index. For example,
#             # for "ababab" and i = 1, the value of R
#             # remains 0 and Z[i] becomes 0. For string
#             # "aaaaaa" and i = 1, Z[i] and R become 5
#             while right < n and string[right - left] == string[right]:
#                 right += 1
#             z[i] = right - left
#             right -= 1
#         else:
#             # k = i-L so k corresponds to number which
#             # matches in [L,R] interval.
#             print('i', i)
#             print('left', left)
#             print('right', right)
#             k = i - left

#             print('k', k)
#             print('z[k]', z[k])

#             # if Z[k] is less than remaining interval
#             # then Z[i] will be equal to Z[k].
#             # For example, str = "ababab", i = 3, R = 5
#             # and L = 2
#             print('right - i + 1 =', right - i + 1)
#             if z[k] < right - i + 1:
#                 z[i] = z[k]

#             # For example str = "aaaaaa" and i = 2,
#             # R is 5, L is 0
#             else:
#                 # else start from R and check manually
#                 left = i
#                 while right < n and string[right - left] == string[right]:
#                     right += 1
#                 z[i] = right - left
#                 right -= 1
#             print(f'z[{i}]', z[i])
#     return z


# print(getZarr('ababab'))
