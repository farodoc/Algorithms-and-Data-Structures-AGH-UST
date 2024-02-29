def silnia(liczba):
    if liczba == 0 or liczba == 1:
        return 1

    wynik = 1
    for i in range(2, liczba + 1):
        wynik *= i
    
    return wynik

def dzielenie(liczba, N):
    t = [0 for i in range(N)]
    licznik = 1

    for i in range(N):
        t[i] = licznik//liczba
        if licznik % liczba == 0:
            break
        
        licznik -= t[i] * liczba
        licznik *= 10
    
    return t


N = int(input("dokladnos e: "))
e = [0 for i in range(N)]

for i in range(N):
    t = dzielenie(silnia(i),N)
    for j in range(N):
        e[j] += t[j]

for i in range(N - 1, 0, -1):
    e[i - 1] += e[i] // 10
    e[i] %= 10

print(e[0], end = "")
print(".", end = "")

for i in range(1,N):
    print(e[i], sep = "", end = "")


