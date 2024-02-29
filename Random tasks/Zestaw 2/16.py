def sumCyfr(liczba):
    wynik = 0
    while liczba > 0:
        wynik += liczba % 10
        liczba //= 10

    return wynik

def rozkladSumaCyfr(liczba):
    i = 2
    suma = 0
    while liczba > 1:
        if liczba % i == 0:
            liczba /= i
            suma += sumCyfr(i)
        
        else:
            i += 1

    return suma

for i in range(2,90):
    if sumCyfr(i) == rozkladSumaCyfr(i):
        print(i)