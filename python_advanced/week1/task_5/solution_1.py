N = int(input())

students_info = []

for i in range(N):
    M = int(input())
    langs = set()
    for k in range(M):
        langs.add(input())
    students_info.append(langs)

first_step = True

for lang_set in students_info:
    if first_step:
        intersection = lang_set
        first_step = False
    intersection.intersection_update(lang_set)

print(len(intersection))
if len(intersection) != 0:
    print(*sorted(intersection), sep='\n')
