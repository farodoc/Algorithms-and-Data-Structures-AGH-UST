def silnia(liczba):
    if liczba == 0 or liczba == 1:
        return 1

    wynik = 1
    for i in range(2, liczba + 1):
        wynik *= i
    
    return wynik

suma = 0

for i in range(10):
    suma += 1/silnia(i)

print(suma)