from math import log10

def isPrime(x):
    if x == 2 or x == 3:
        return True

    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False

    i = 5

    while i <= int(x ** 0.5):
        if x % i == 0 or x % (i + 2) == 0:
            return False

        i += 6

    return True

def divide(liczba):
    dl = int(log10(liczba)) + 1

    for mask in range(2, 2 ** dl, 2):
        czyOkPodzial = True
        x = liczba
        liczbaElementow = 1
        tempRes = 0
        multi = 1
        while x > 0:
            if mask % 2 == 0:
                lastDigit = x % 10
                tempRes += multi * lastDigit
                multi *= 10
            
            else:
                if not isPrime(tempRes):
                    czyOkPodzial = False
                    break
                
                liczbaElementow += 1
                tempRes = x % 10
                multi = 10
            
            mask //= 2
            x //= 10
        
        if czyOkPodzial and isPrime(tempRes) and isPrime(liczbaElementow):
                return True
    
    return False

print(divide(23672))