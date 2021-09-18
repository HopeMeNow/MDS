import json

files = input().split()
output_name = input()

all_logs = {}
unique_logs = set()

for file_name in files:
    with open(file_name) as f:
        for line in f:
            log = json.loads(line)
            consumer_logs = all_logs.setdefault(log['consumer_id'], [])
            consumer_logs.append(tuple([log['date'], log['message']]))

for _, logs_arr in all_logs.items():
    unique_logs.update(logs_arr)

print(len(all_logs[0]) + len(all_logs[1]))
print(len(unique_logs))

# with open('output.tsv') as f:
#     output = f.readlines()
#     print(len(output))
