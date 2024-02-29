from math import inf
from random import randint

def black_forest(c):
    n = len(c)
    F = [0] * n
    F[0] = c[0]
    F[1] = max(c[0], c[1])

    for i in range(2, n):
        F[i] = F[i - 2] + c[i]

        if F[i] < F[i - 1]:
            F[i] = F[i - 1]


    return F[n - 1]


def can_fall(a, b):
    return a[0] >= b[0] and a[1] <= b[1]

def falling_bricks(T):
    n = len(T)
    F = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if can_fall(T[i], T[j]):
                F[i] = max(F[i], F[j] + 1)
                
    return n - max(F)