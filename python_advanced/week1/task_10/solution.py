# dictionary = {}

# while True:
#     line = input()
#     if line == '':
#         break
#     else:
#         for word in line.split():
#             if word not in dictionary:
#                 dictionary[word] = 0
#             dictionary[word] += 1

# max_value = max(dictionary.items(), key=lambda item: item[1])[1]
# filtered_dict = {k: v for k, v in dictionary.items() if v == max_value}
# sorted_dict = sorted(filtered_dict.items(), key=lambda item: item[0])

# print(sorted_dict[0][0])

a = '    dsfg hdsj   hdscj 48r    dhsfh         '.split()
print(a)
