from egzP5atesty import runtests
from math import inf

def inwestor ( T ):
    n = len(T)
    min_field = [[inf for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        min_field[i][i] = T[i]

    for i in range(n):
        for j in range(i + 1, n):
            min_field[i][j] = min(min_field[i][j - 1], T[j])

    profit = -inf

    for i in range(n):
        for j in range(i + 1, n):
            profit = max(profit, (j - i + 1) * min_field[i][j])

    return profit

runtests ( inwestor, all_tests=True )