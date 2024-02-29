def czyCyfra0(liczba):
    if liczba < 0:
        liczba *= -1

    while liczba > 0:
        if liczba % 10 == 0:
            return True

        liczba //= 10

    return False

def zad10(t):
    n = len(t[0])

    zeraW = [False for _ in range(n)]
    zeraK = [False for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if czyCyfra0(t[i][j]):
                zeraW[i] = True
                zeraK[j] = True
            
    if False in zeraK or False in zeraW:
        return False

    return True

t = [[1,1230],
     [13077,23]]

print(zad10(t))