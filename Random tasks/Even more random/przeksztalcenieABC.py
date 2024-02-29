def C(x):
    res = 0
    multi = 1

    while x > 0:
        lastDigit = x % 10
        if lastDigit % 2 == 0:
            lastDigit += 1
        
        res += multi * lastDigit
        multi *= 10
        x //= 10

    return res

#tworzenie masek trinarnych

def isValid(mask):
    prev =  -1

    while mask > 0:
        lastDigit = mask % 3
        if lastDigit == prev:
            return False
        
        mask //= 3
        prev = lastDigit

    return True

def transform(x,y,n):
    cnt = 0
    for mask in range(3 ** n):
        tempRes = x
        tempDl = 0
        if isValid(mask):
            while mask > 0:
                if mask % 3 == 0:
                    tempRes += 3
                
                elif mask % 3 == 1:
                    tempRes *= 2

                else:
                    tempRes = C(tempRes)

                tempDl += 1
                mask //= 3

            if tempDl == n:
                if tempRes == y:
                    cnt += 1

            else:
                if tempRes == y:
                    cnt += 1

                if tempRes + 3 == y:
                    cnt += 1
    
    return cnt

print(transform(11,32,4))