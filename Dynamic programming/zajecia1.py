from math import inf

def sub_sum(T, s):
    if s < 0:
        return False
    q = [[False for _ in range(s + 1)] for _ in range(len(T) + 1)]
    for i in range(len(T) + 1):
        q[i][0] = True
    for i in range(1, len(T) + 1):
        for j in range(1, s + 1):
            if T[i - 1] > j:
                q[i][j] = q[i - 1][j]
            else:
                q[i][j] = (q[i - 1][j] or q[i - 1][j - T[i - 1]])
    return q


def lcs_bu(A, B):
    n = len(A)
    m = len(B)

    F = [[0]*n for _ in range(m)]

    if A[0] == B[0]:
        F[0][0] = 1


    for i in range(1, n):
        if F[0][i - 1] or A[i] == B[0]:
            F[0][i] = 1

    for j in range(1, m):
        if F[j - 1][0] or B[j] == A[0]:
            F[j][0] = 1


    for i in range(1, m):
        for j in range(1, n):
            if A[j] == B[i]:
                F[i][j] = F[i-1][j-1] + 1

            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])


    return F[m-1][n-1]


def exchange(T, s):
    F = [inf] * (s + 1)
    F[0] = 0
    p = [None] * (s + 1)

    for i in range(s + 1):
        for value in T:
            if i - value >= 0 and F[i - value] + 1 < F[i]:
                F[i] =F[i - value] + 1
                p[i] = i - value


    res = [None] * F[s]
    i = s
    j = 0
    while i > 0:
        res[j] = i - p[i]
        i = p[i]
        j += 1

    return res


coins = [2, 5]
amount = 13
print(exchange(coins, amount))