N = int(input())

m = (N % 3600)//60
s = (N % 3600) % 60

print('{}:{}:{}'.format(
  N//3600,
  m if m > 9 else '0' + str(m),
  s if s > 9 else '0' + str(s),
))
