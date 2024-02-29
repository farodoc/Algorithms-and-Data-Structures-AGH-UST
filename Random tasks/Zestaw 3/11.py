def najdlGeo(t):
    maxDl = 1
    i = 0

    while i < len(t) - 1:
        if t[i] == 0 and t[i + 1] == 0:
            q = 0
        
        elif t[i] == 0 and t[i + 1] != 0:
            i += 1
            continue

        else:
            q = t[i + 1] / t[i]

        koniec = i + 1
        tempDl = 2

        while koniec < len(t) - 1 and t[koniec] * q == t[koniec + 1]:
            tempDl += 1
            koniec += 1

        if tempDl > maxDl:
            maxDl = tempDl
        
        i = koniec
    
    return maxDl
        

t = [1,2,4,8,0,0,0,0,0]

print(t)
print(najdlGeo(t))