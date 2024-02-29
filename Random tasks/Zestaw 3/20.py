def unikalneCzynniki(liczba):
    if liczba == 0:
        return False

    if liczba == 1:
        return True
    
    dzielnik = 2
    while liczba > 1:
        if liczba % dzielnik == 0:
            liczba //= dzielnik
            if liczba % dzielnik == 0:
                return False
        
        dzielnik += 1

    return True

def najdlCiag(t):
    maxDl = 0

    for i in range(len(t) - 1):
        if unikalneCzynniki(t[i]):
            tempDl = 1
            liczba = t[i]
            if tempDl > maxDl:
                maxDl = tempDl

            for j in range(i + 1, len(t)):
                liczba *= t[j]
                if unikalneCzynniki(liczba):
                    tempDl += 1
                    if tempDl > maxDl:
                        maxDl = tempDl
    
    return maxDl

t = [2,23,33,35,7,4,6,7,5,11,13,22]

print(najdlCiag(t))
