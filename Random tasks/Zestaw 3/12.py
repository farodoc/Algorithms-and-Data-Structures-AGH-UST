import random

def najdlArytDodatni(t):
    maxDl = 1
    i = 0

    while i < len(t) - 1:
        r = t[i + 1] - t[i]
        if r <= 0:
            i += 1

        else:
            koniec = i + 1
            tempDl = 2

            while koniec < len(t) - 1 and t[koniec] + r == t[koniec + 1]:
                tempDl += 1
                koniec += 1

            if tempDl > maxDl:
                maxDl = tempDl
            
            i = koniec
    
    return maxDl

def najdlArytUjemny(t):
    maxDl = 1
    i = 0

    while i < len(t) - 1:
        r = t[i + 1] - t[i]
        if r >= 0:
            i += 1

        else:
            koniec = i + 1
            tempDl = 2

            while koniec < len(t) - 1 and t[koniec] + r == t[koniec + 1]:
                tempDl += 1
                koniec += 1

            if tempDl > maxDl:
                maxDl = tempDl
            
            i = koniec
    
    return maxDl
        

while True:
    n = int(input("rozmiar tablicy: "))

    t = [random.randint(0,49) * 2 + 1 for _ in range(n)]


    print(t)
    print("dodatni: ", najdlArytDodatni(t), ", ujemny: ", najdlArytUjemny(t), ", roznica = ", abs(najdlArytUjemny(t) - najdlArytDodatni(t)))