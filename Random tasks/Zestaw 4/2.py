def oddDigits(liczba):
    while liczba > 0:
        if (liczba % 10) % 2 == 0:
            return False

        liczba //= 10

    return True

def zad2(T):
    n = len(T[0])

    for i in range(n):
        cnt = 0
        for j in range(n):
            if oddDigits(T[i][j]):
                cnt += 1

        if cnt == 0:
            return False
    
    return True