import math

def czyPodobne(a,b):
    dl1 = int(math.log(a,10)) + 1
    dl2 = int(math.log(b,10)) + 1

    T1 = [10 for _ in range(dl1)]
    T2 = [10 for _ in range(dl2)]
    
    for i in range(dl1):
        lastDigit = a % 10
        czyUnikat = True

        for j in range(dl1):
            if lastDigit == T1[j]:
                czyUnikat = False
                break
            
        if czyUnikat:
            T1[i] = lastDigit
        
        a //= 10
    
    T1.sort()

    for i in range(dl2):
        lastDigit = b % 10
        czyUnikat = True

        for j in range(dl2):
            if lastDigit == T2[j]:
                czyUnikat = False
                break
            
        if czyUnikat:
            T2[i] = lastDigit
        
        b //= 10
    
    T2.sort()

    if dl1 > dl2:
        minDl = dl2
        if T1[minDl] != 10:
            return False
    
    elif dl1 < dl2:
        minDl = dl1
        if T2[minDl] != 10:
            return False

    else:
        minDl = dl1
    
    for i in range(minDl):
        if T1[i] != T2[i]:
            return False
    
    return True
        
print(czyPodobne(1233444444444454,35214))