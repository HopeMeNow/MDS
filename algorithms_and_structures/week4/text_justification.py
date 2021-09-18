import math



def tj_cost(L, W):
    n = len(W)
    tbl = [math.inf]*(n+1)
    tbl[0] = 0
    for i in range(1, n+1):
        length = - 1
        for j in range(i-1, -1, -1):
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                P = (L - length)**3
            # if i == n:
            #     P = 0
            # print('i', i)
            # print('j', j)
            # print('P', P)
            # print('tbl[j]', tbl[j])
            tbl[i] = min(tbl[i], tbl[j] + P)
            # print('tbl[i]', tbl[i])
        restLength = 0
        for k in range(i, n):
            restLength += len(W[k]) + 1
        if restLength <= L and tbl[i] > tbl[i-1]:
             tbl[i] = tbl[i-1]
    print('table', tbl)
    return tbl[n]


def tj(L, W):
    pass

if __name__ == "__main__":
    W_example = ["jars", "jaws", "joke", "jury", "juxtaposition"]
    L_example = 15
    # should print 432
    print(tj_cost(L_example, W_example))
    # should print:
    #jars jaws
    #joke jury
    #juxtaposition
    # print(tj(L_example, W_example))
