from math import log10
from math import sqrt

def leng(liczba):
    return int(log10(liczba)) + 1

def isPrime(x):
    if x == 2 or x == 3:
        return True
    
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False
    
    i = 5
    while i <= sqrt(x):
        if x % i == 0:
            return False

        i += 2
        if x % i == 0:
            return False
        
        i += 4

    return True

def rotate(liczba):
    L = leng(liczba)

    firstDigit = liczba // (10 ** (L - 1))
    n = liczba % 10 ** (L - 1)
    res = 10 * n + firstDigit

    return res

def iloczynBazy(x, base):
    res = 1

    while x > 0:
        digit = x % base
        res *= digit
        x //= base
    
    return res

def zad1(N):
    for base in range(2, 17):
        for _ in range(leng(N)):
            N = rotate(N)

            if isPrime(iloczynBazy(N, base)):
                return base
    
    return None

print(zad1(13))