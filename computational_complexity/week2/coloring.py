edges = [(1, 2), (2, 3), (3, 1)]
n = 3
k = 5

clauses = []

for i_k in range(k):
    for u, v in edges:
        clauses.append((-(i_k*n + u), -(i_k*n + v)))

for v in range(1, n+1):
    clauses.append(tuple([i*n + v for i in range(k)]))

print(clauses)
