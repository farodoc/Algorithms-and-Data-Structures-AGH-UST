def evenDigit(liczba):
    while liczba > 0:
        if (liczba % 10) % 2 == 0:
            return True

        liczba //= 10

    return False

def zad3(T):
    n = len(T[0])

    for i in range(n):
        cnt = 0
        for j in range(n):
            if evenDigit(T[i][j]):
                cnt += 1

        if cnt == n:
            return True

    return False
