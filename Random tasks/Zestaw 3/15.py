import random

def czyZlozona(liczba):
    if liczba < 4:
        return False
    
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return True
    
    return False

def isPrime(liczba):
    if liczba == 2 or liczba == 3:
        return True
    
    if liczba % 2 == 0 or liczba % 3 == 0 or liczba <= 1:
        return False
    
    i = 5

    while i < int(liczba**0.5) + 1:
        if liczba % i == 0:
            return False
        
        i += 2

        if liczba % i == 0:
            return False
        
        i += 4
    
    return True

while True:
    n = int(input("rozmiar tablicy: "))

    t = [random.randint(1,100) for _ in range(n)]
    print(t)

    a, b = 1, 2

    czyOk = True
    bylaPrime = False

    for i in range(n):
        if i == a:
            if czyZlozona(t[i]) == False:
                czyOk = False
                print("Nie")
                break

            a, b = b, a + b
        
        else:
            if isPrime(t[i]):
                bylaPrime = True
    
    if czyOk and bylaPrime:
        print("tak")

    elif czyOk and not bylaPrime:
        print("nie")