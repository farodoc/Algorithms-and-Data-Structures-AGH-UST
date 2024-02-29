def czySameCyfryPierwsze(liczba):
    while liczba > 0:
        x = liczba % 10
        if x != 2 or x != 3 or x != 5 or x != 7:
            return False
        
        liczba //= 10
    
    return True

def wierszPierwszy(t):
    n = len(t[0])

    for i in range(n):
        flag = False
        for j in range(n):
            if czySameCyfryPierwsze(t[i][j]):
                flag = True
        
        if not flag:
            return False

    return True