info = input().split()

N = int(info[0])
K = int(info[1])

strikes = []

for i in range(K):
    x, y = input().split()
    strikes.append({
        x for x in range(int(x), N+1, int(y)) if not (
            x % 7 == 0 or (x+1) % 7 == 0
        )
    })

result = set()
for j in strikes:
    result = result.union(j)

print(len(result))
