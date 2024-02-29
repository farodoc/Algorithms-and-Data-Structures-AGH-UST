from math import sqrt
from math import log

def leng(liczba):
    return int(log(liczba, 10)) + 1

def isPrime(liczba):
    if liczba == 2 or liczba == 3:
        return True

    if liczba % 3 == 0 or liczba % 2 == 0 or liczba <= 1:
        return False
    
    i = 5

    while i <= sqrt(liczba):
        if liczba % i == 0:
            return False
        
        i += 2
        if liczba % i == 0:
            return False
        
        i += 4
    
    return True

def uniqDigits(liczba):
    dl = leng(liczba)

    if dl > 10:
        return False
    
    T = [-1 for _ in range(dl)]

    for i in range(dl):
        lastDigit = liczba % 10
        
        for j in range(dl):
            if T[j] == lastDigit:
                return False
        
        T[i] = lastDigit
        liczba //= 10
    
    return True

def cutNumber(liczba, start, end):
    res = 0
    for i in range(leng(liczba) - end - 1):
        liczba //= 10

    dl = end - start
    mult = 1

    for i in range(dl + 1):
        res += mult * (liczba % 10)
        liczba //= 10
        mult *= 10

    return res

def maxCut(k):
    maks = 0
    for i in range(leng(k) - 1):
        for j in range(i + 1, leng(k)):
            if isPrime(cutNumber(k, i, j)) and uniqDigits(cutNumber(k, i, j)):
                maks = max(maks, cutNumber(k, i, j))
    
    return maks

#print(maxCut(1202742516))
print(maxCut(101))