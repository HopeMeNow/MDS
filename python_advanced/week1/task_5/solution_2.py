N = int(input())

students_info = []

for i in range(N):
    M = int(input())
    langs = set()
    for k in range(M):
        langs.add(input())
    students_info.append(langs)

result = set()

for lang_set in students_info:
    result.update(lang_set)

print(len(result))
print(*sorted(result), sep='\n')
