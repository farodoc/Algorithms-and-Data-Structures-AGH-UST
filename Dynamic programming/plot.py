def plot(T, K):
    n = len(T)

    F = [[0 for _ in range(n)] for _ in range(K)]
    F[0][0] = T[0]

    for i in range(1, n):
        F[0][i] = F[0][i - 1] + T[i]


    for k in range(K):
        for i in range(k, n):
            for j in range(i - 1, k - 2, - 1):
                F[k][i] = max(F[k][i], min(F[0][i] - F[0][j], F[k - 1][j]))

    return F[K - 1][n - 1]