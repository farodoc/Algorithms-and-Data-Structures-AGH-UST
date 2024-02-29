def czySamogloska(litera):
    t = ['a', 'e', 'i', 'o', 'u', 'y']
    return litera in t

def waga(slowo):
    suma = 0
    for i in range(len(slowo)):
        suma += ord(slowo[i])

    return suma

def liczbaSamoglosek(slowo):
    cnt = 0
    for i in range(len(slowo)):
        cnt += czySamogloska(slowo[i])

    return cnt

def rek(waga1, samog1, s2, waga2 = 0, samog2 = 0, slowo = "", i = 0):
    global stop

    if stop:
        return False

    if waga1 == waga2 and samog1 == samog2:
        stop = True
        return slowo

    if waga2 > waga1 or samog2 > samog1 or i == len(s2):
        return False
    
    #bierzemy litere                                                                                          #nie bierzemy
    return rek(waga1, samog1, s2, waga2 + ord(s2[i]), samog2 + czySamogloska(s2[i]), slowo + s2[i], i + 1) or rek(waga1, samog1, s2, waga2, samog2, slowo, i + 1)

    



stop = False

def wyraz(s1, s2):
    slowo = rek(waga(s1), liczbaSamoglosek(s1), s2)

    return slowo

print(wyraz("ala", "tttsdadadaddl"))

