import json

file_name = input()

correct_200 = 0
correct_not_200 = 0
not_int_status = 0
no_status = 0
broken_str = 0


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


with open(file_name) as f:
    for line in f:
        try:
            log = json.loads(line)
        except json.decoder.JSONDecodeError:
            broken_str += 1
            continue
        try:
            status = log['status']
        except KeyError:
            no_status += 1
            continue
        if status is None or status == '':
            no_status += 1
        elif status == 200 or (is_integer(status) and int(status) == 200):
            correct_200 += 1
        elif (
            type(status) == int and status != 200
        ) or (
            is_integer(status) and int(status) != 200
        ):
            correct_not_200 += 1
        elif type(status) != int:
            not_int_status += 1

print(correct_200)
print(correct_not_200)
print(not_int_status)
print(no_status)
print(broken_str)
