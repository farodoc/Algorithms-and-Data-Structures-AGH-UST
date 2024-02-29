import random

def najdlAryt(t):
    maxDl = 1
    i = 0

    while i < len(t) - 1:
        r = t[i + 1] - t[i]
        koniec = i + 1
        tempDl = 2

        while koniec < len(t) - 1 and t[koniec] + r == t[koniec + 1]:
            tempDl += 1
            koniec += 1

        if tempDl > maxDl:
            maxDl = tempDl
        
        i = koniec
    
    return maxDl
        


#n = int(input("rozmiar tablicy: "))

#t = [random.randint(0,20) for _ in range(n)]
t = [0,1,2,1,2,3,4]

print(t)
print(najdlAryt(t))