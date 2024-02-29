from math import inf

def prom(T, L):
    n = len(T)
    F = [[-inf for _ in range(L + 1)] for _ in range(n)]

    F[0][T[0]] = 0
    F[0][0] = T[0]

    for i in range(1, n):
        not_placed = True
        for j in range(L + 1):
            if F[i - 1][j] != -inf:
                left = j
                right = F[i - 1][j]

                if left + T[i] <= L:
                    not_placed = False
                    F[i][j + T[i]] = right

                if right + T[i] <= L:
                    not_placed = False
                    F[i][left] = right + T[i]

        if not_placed:
            return i

    return n