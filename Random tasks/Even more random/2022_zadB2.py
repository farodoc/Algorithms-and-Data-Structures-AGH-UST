def czy2czynniki(liczba):
    if liczba == 1:
        return False

    pierwszyCzynnik = False
    cnt = 0

    i = 2

    while liczba > 1:
        if liczba % i == 0:
            if pierwszyCzynnik == False:
                cnt += 1
                prev = i
                pierwszyCzynnik = True

            if i != prev:
                cnt += 1
                prev = i

            liczba //= i

        else:
            i += 1

    if cnt == 2:
        return True

    return False

def condition(t, row, col, bok):
    n = len(t[0])

    if row + bok - 1 < n and col + bok - 1 < n:
        iloczyn = t[row][col] * t[row + bok - 1][col] * t[row + bok - 1][col + bok - 1] * t[row][col + bok - 1]

        if czy2czynniki(iloczyn):
            return bok

    return False

def szukanieKwadratu(t):
    n = len(t[0])

    for bok in range(2, n):
        for i in range(n - bok + 1):
            for j in range(n - bok + 1):
                if condition(t,i,j,bok) != False:
                    return condition(t,i,j,bok)

    return 0

t = [[1,2,3],
     [1,1,1],
     [1,1,1]]

print(szukanieKwadratu(t))
print(czy2czynniki(6))