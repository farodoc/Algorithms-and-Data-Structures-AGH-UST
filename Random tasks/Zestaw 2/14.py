import math

def leng(liczba):
    return int(math.log(liczba,10)) + 1

def isPrime(liczba):
    if liczba == 2 or liczba == 3:
        return True
    
    if liczba % 2 == 0 or liczba % 3 == 0 or liczba <= 1:
        return False

    i = 5
    while i < int(liczba ** 0.5) + 1:
        if liczba % i == 0:
            return False
        
        i += 2
        if liczba % i == 0:
            return False 
        
        i += 4
    
    return True

def mix_numbers(a, b, mask):
    while mask > 0 or a > 0:
        num = 0
        multi = 1

        if mask % 2 == 0:
            d = a % 10
            a //= 10

        else:
            d = b % 10
            b //= 10

        mask //= 2
        num += d * multi
        multi *= 10
    
    return d

def vaildMask(a, b, mask):
    cnt1 = leng(a)
    cnt2 = leng(b)
   
    while mask > 0:
        if mask % 2 == 0:
            cnt1 -= 1
        
        else:
            cnt2 -= 1
        
        mask //= 2
    
    return cnt2 == 0 and cnt1 >= 0

a = int(input("a = "))
b = int(input("b = "))

cnt = 0

for mask in range(2 ** (leng(a) + leng(b))):
    if vaildMask(a,b,mask) and isPrime(mix_numbers(a,b,mask)):
        cnt += 1

print(cnt)