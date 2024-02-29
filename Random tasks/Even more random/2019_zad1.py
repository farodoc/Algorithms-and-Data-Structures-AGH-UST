from math import sqrt

def czyPotega(liczba):
    if liczba == 1:
        return True
    
    dzielnik = 2
    while dzielnik < int(sqrt(liczba)) + 1:
        flaga = True
        n = liczba
        while n > 1:
            if n % dzielnik != 0:
                flaga = False
                break
            
            n //= dzielnik
        
        if flaga:
            return True
        
        dzielnik += 1

    return False

def sum_tab(t, indeks, dl):
    suma = 0
    for i in range(indeks, indeks + dl):
        suma += t[i]
    
    return suma

def funkcja(t1, t2):
    dl = len(t1)

    for i in range(1,24):
        for indeks1 in range(dl - i + 1):
            for indeks2 in range(dl - (24 - i) + 1):
                suma = sum_tab(t1, indeks1, i) + sum_tab(t2, indeks2, 24 - i)
                if czyPotega(suma):
                    return True
    
    return False