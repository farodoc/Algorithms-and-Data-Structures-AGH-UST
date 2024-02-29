def czyNpCyfra(liczba):
    while liczba > 0:
        if (liczba % 10) % 2 == 1:
            return True
        
        liczba //= 10
    
    return False

def cyfryNpTablicy(tab):
    for i in range(len(tab)):
        if czyNpCyfra(tab[i]) == False:
            return False
        
    return True

while True:
    n = int(input("rozmiar tablicy: "))

    t = [0 for _ in range(n)]

    for i in range(n):
        t[i] = int(input())

    print(cyfryNpTablicy(t))
