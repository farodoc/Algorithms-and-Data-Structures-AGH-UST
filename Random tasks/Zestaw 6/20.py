from math import log10

def leng(liczba):
    if liczba == 0:
        return 1
    return int(log10(liczba)) + 1

def lastDigit(liczba):
    return liczba % 10

def firstDigit(liczba):
    return liczba // (10 ** (leng(liczba) - 1))

def canMove(t, curW, curK, nextW, nextK):
    if nextW < 0 or nextW > 7 or nextK < 0 or nextK > 7:
        return False

    return lastDigit(t[curW][curK]) < firstDigit(t[nextW][nextK])

def dlTrasy(w1, k1, w2, k2):
    return abs(w2 - w1) + abs(k2 - k1) - min(abs(w2 - w1), abs(k2 - k1))

def f(t, aktuW, aktuK, celW, celK, maxDl, tempDl = 0, trasa = []):
    global stop

    if stop:
        return

    if tempDl > maxDl:
        return
    
    if aktuW == celW and aktuK == celK:
        stop = True
        print(trasa)  
        return

    for i, j, n in [(-1,0,0),(-1,1,1),(0,1,2),(1,1,3),(1,0,4),(1,-1,5),(0,-1,6),(-1,-1,7)]:
        if canMove(t, aktuW, aktuK, aktuW + i, aktuK + j):
            return f(t, aktuW + i, aktuK + j, celW, celK, maxDl, tempDl + 1, trasa + [n])

def zad19(t, w, k):
    for i, j in [(0,0), (0,7), (7,7), (7,0)]:
        f(t, w, k, i, j, dlTrasy(w, k, i, j))
        if stop:
            return True
        
    return False


t = [[1,1,1,1,1,1,1,6],
     [1,2,1,1,1,2,3,1],
     [1,1,3,1,1,1,1,1],
     [1,1,1,4,1,1,1,1],
     [1,1,1,1,5,1,1,1],
     [1,1,1,1,1,6,1,1],
     [1,1,1,1,1,1,7,1],
     [1,1,1,1,1,1,1,8],]

stop = False

print(zad19(t,1,4))