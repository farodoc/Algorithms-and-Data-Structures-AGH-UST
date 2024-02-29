def czySzachowane(t, w, k):
    n = len(t)
    for i in range(n):
        if t[w][i] or t[i][k]:
            return True

    return False

def usuwanieWiezy(t, w, k):
    t2 = [[0 for _ in range(len(t))] for _ in range(len(t))]

    for i in range(len(t)):
        for j in range(len(t)):
            t2[i][j] = t[i][j]

    return t2

def szachowanePola(t):
    n = len(t)
    t2 = [[0 for _ in range(n)] for _ in range(n)]

    for w in range(n):
        for k in range(n):
            t2[w][k] = czySzachowane(t, w, k)

    return t2

def wypisz(t):
    n = len(t)

    for i in range(n):
        print(t[i])

def czyMoznaWstawic(t):
    n = len(t)
    flagW = True
    flagK = True
    for w in range(n):
        for k in range(n):
            if t[w][k] == 0:
                if flagW and flagK:
                    wiersz = w
                    flagW = False

                elif not flagW and flagK:
                    if w != wiersz:
                        kolumna = k
                        flagK = False
                
                else:
                    if w != wiersz and k != kolumna:
                        return False
    
    return True

def move(t):
    n = len(t)

    for w in range(n):
        for k in range(n):
            if t[w][k]:
                nowaTablica = usuwanieWiezy(t, w, k)
                tablicaSzachow = szachowanePola(nowaTablica)
                if czyMoznaWstawic(tablicaSzachow):
                    return True
    
    return False