import re


def problem_1():
  return re.compile('[-+]?[0-9]+')


def problem_2():
	return re.compile('\d+(?:\.\d+)?')


def problem_3():
	return re.compile('(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9]')


def problem_4():
	return re.compile('[1-2]\d{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2]\d|3[0-1])')


def problem_5():
	return re.compile('(?:\w|-|_){3,16}')


def problem_6():
	return re.compile('(?:\w|_|-|\.)+@[a-zA-Z]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*')


def problem_7():
	return re.compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')


def problem_8():
  return re.compile("(?:http|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")


# print(re.findall(problem_1(), 'There  are 15 apples and −2 oranges!'))
# print(re.findall(problem_2(), 'There  are 1.5 apples and 2 oranges!'))
# print(re.findall(problem_3(), 'At 17:00, or at 14:00, or at 25:61'))
# print(re.findall(problem_3(), 'At 4:30 or 04:30'))
# print(re.findall(problem_4(), 'It was a long time ago. In 1888-01-01 or in 2001-01-01 or in 1999-13-40.'))
# print(re.findall(problem_5(), "Hi! I'm megaduck2010!"))
# print(re.findall(problem_6(), "Hi! I am writing to you from example@example.com to hello@bye.com.org"))
# print(re.findall(problem_7(), "These are 0.0.0.1, 169.255.0.0 and 256.256.0.0 "))
# print(re.findall(problem_8(), "Welcome to https://wel.com/e, stranger!"))
