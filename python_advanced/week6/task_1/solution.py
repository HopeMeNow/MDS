import re

texts = []
while True:
    input_ = input()
    if input_ == '':
        break
    pattern = re.compile('<i>(.*?)</i>')
    texts.extend(pattern.findall(input_))

print(*texts, sep='\n')
