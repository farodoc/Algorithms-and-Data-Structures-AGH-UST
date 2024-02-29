def czyZlozona(liczba):
    if liczba == 1:
        return False

    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return True

    return False

def condition(t, row, col):
    cnt = 0
    for i,j in (row, col+1),(row+1, col+1),(row+1, col),(row+1, col-1),(row, col-1),(row-1, col-1),(row-1, col),(row-1, col+1):
        if czyZlozona(t[i][j]):
            cnt += 1

    if cnt >= 6:
        return True

    return False

def zad11(t):
    n = len(t[0])

    for level in range(n):
        cnt = 0
        for row in range(2, n - 1):
            for col in range(2, n - 1):
                if condition(t[level], row, col):
                    cnt += 1

        if level == 0:
            prev = cnt

        if cnt != prev:
            return False

    return True
