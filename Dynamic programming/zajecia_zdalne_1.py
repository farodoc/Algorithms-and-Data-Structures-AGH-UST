from math import inf

#som przekaski, skok kosztuje odleglosc do kwadratu
def zabson(T):
    n = len(T)
    snack_amount = 0
    for i in range(n):
        snack_amount += T[i]

    F = [[inf]*n for _ in range(snack_amount + 1)]

    F[T[0]][0] = 0

    for i in range(n):
        for energy in range(snack_amount + 1):
            if F[energy][i] != inf:
                jump_to = 1
                while jump_to**2 <= energy and i + jump_to < n:
                    if F[energy - jump_to**2 + T[i + jump_to]][i + jump_to] > F[energy][i] + 1:
                        F[energy - jump_to**2 + T[i + jump_to]][i + jump_to] = F[energy][i] + 1

                    jump_to += 1


    min_jumps = inf
    for i in range(snack_amount + 1):
        if F[i][n - 1] < min_jumps:
            min_jumps = F[i][n - 1]

    return F

T=[2,4,1,2,0,0,1,1]
sum = 0

for i in range(len(T)):
    sum += T[i]

A = zabson(T)

for i in range(sum):
    print(A[i])