import re

p = re.compile('.{3,4}')

print(re.search(p, '  \n  '))
print(re.search(p, 'why hello!'))
print(re.search(p, '    '))
print(re.search(p, '  \n\n\n\n  '))
print(re.search(p, ' '))
