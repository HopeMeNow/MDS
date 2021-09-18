# from itertools import product
# import numpy as np
from collections import deque

# n_coin = 20

# omega_coin = list(product(['H', 'T'], repeat=n_coin))

# A = {om for om in omega_coin if om.count('H') % 2 == 0}
# B = {om for om in omega_coin if om.count('T') < 4}


# def conditional_probability(X, Y):
#     return len(X & Y)/len(Y)


# print(round(conditional_probability(A, B), 5))

# n_dice = 5

# omega_dice = list(product([1, 2, 3, 4, 5, 6], repeat=n_dice))

# C = {om for om in omega_dice if sum(om) % 3 == 0}
# D = {om for om in omega_dice if np.prod(om) > 500}

# print(round(conditional_probability(D, C), 3))

Q = deque()

Q.append(1)
Q.append(1)
Q.append(1)
Q.append(1)
Q.append(1)

print(Q.popleft())
