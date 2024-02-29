def najdlCiag(t):
    i = 0
    maxDl = 0

    while i < len(t) - 1:
        if t[i] < t[i + 1]:
            sumaLiczb = t[i]
            sumaIndeksow = i
            koniec = i
            tempDl = 1

            while koniec < len(t) - 1 and t[koniec + 1] > t[koniec]:
                sumaLiczb += t[koniec + 1]
                sumaIndeksow += koniec + 1
                tempDl += 1
                koniec += 1

                if sumaLiczb == sumaIndeksow:
                    if tempDl > maxDl:
                        maxDl = tempDl
            
        i += 1
    
    if maxDl == 0:
        for i in range(len(t)):
            if i == t[i]:
                return 1

    return maxDl


#t = [0,1,2,3]
t = [0,1,0,4,5]

print(najdlCiag(t))