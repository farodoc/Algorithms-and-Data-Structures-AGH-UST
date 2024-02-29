def czyCyfraPierwsza(liczba):
    while liczba > 0:
        x = liczba % 10
        if x == 2 or x == 3 or x == 5 or x == 7:
            return True
        
        liczba //= 10
    
    return False

def wierszPierwszy(t):
    n = len(t[0])

    for i in range(n):
        cnt = 0
        for j in range(n):
            if czyCyfraPierwsza(t[i][j]):
                cnt += 1
        
        if cnt == n:
            return True

    return False