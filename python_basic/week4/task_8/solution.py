n = int(input())

emails = []

for i in range(0, n):
    email = input()
    emailArr = email.split('@')
    if len(emailArr) > 1 and emailArr[1] == 'gmail.com':
        emails.append(email)

[print(email) for email in emails]
