def isPrime(n):
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False

    i = 5

    while i <= n ** 0.5:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
        i += 6

    return True

def zmianaNaLiczbe(t, p, k):
    res = 0
    multi = 1

    for i in range(k, p - 1, -1):
        res += t[i] * multi
        multi *= 2

    return res

def podzial(t, p = 0, k = 1):
    if k >= len(t):
        return False

    if k == len(t) - 1 and isPrime(zmianaNaLiczbe(t, p, k)):
        return True

    for i in range(len(t) - k - 1):
        if isPrime(zmianaNaLiczbe(t, p, k + i)):
            return podzial(t, k + i + 1, k + i + 2)
        

t = [1,1,1,0,1,1,1,1,1,0,1,1]

print(podzial(t))
