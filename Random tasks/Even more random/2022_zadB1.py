def szukanieCiagu(t):
    n = len(t)
    maxPoczatek = 0
    minKoniec = 10**6

    i = 0
    while i < n:
        if i + 1 < n:
            if t[i] < t[i + 1]:
                tempMaxPoczatek = t[i]
                koniec = i + 1
                tempDl = 2
                while koniec + 1 < n and t[koniec] < t[koniec + 1]:
                    koniec += 1
                    tempDl += 1
                
                if tempDl > 2:
                    maxPoczatek = max(maxPoczatek, tempMaxPoczatek)
                    minKoniec = min(minKoniec, t[koniec])
                
                i = koniec + 1
            
            else:
                i += 1
        
        else:
            break
    
    return maxPoczatek > minKoniec

t = [2,15,17,13,17,19,23,2,6,4,8,3,5,14,1,2,3]

print(szukanieCiagu(t))