from math import sqrt

def isPrime(liczba):
    if liczba < 2:
        return False

    for i in range(2, int(sqrt(liczba)) + 1):
        if liczba % i == 0:
            return False

    return True
        
n = 4
t1 = [1,3,2,4]
t2 = [9,7,4,8]
cnt = 0

for i in range(3 ** n):
    suma = 0
    
    maska = [0 for _ in range(n)]
    j = n - 1

    while i > 0:
        maska[j] = i % 3
        j -= 1
        i //= 3
    
    for k in range(n):
        if maska[k] == 0:
            suma += t1[k] + t2[k]
        
        elif maska[k] == 1:
            suma += t1[k]

        else:
            suma += t2[k]
    
    if isPrime(suma):
        print(suma)
        cnt += 1

print("liczba poprawnych sum: ", cnt)
    
