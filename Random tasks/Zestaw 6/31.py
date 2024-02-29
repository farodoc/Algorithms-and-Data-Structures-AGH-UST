def zad(t, p = 0, res = 1):
    if p == len(t):
        if res > 1:
            return res
        
        return 0
    
    return zad(t, p + 1, res) + zad(t, p + 1, res * t[p])

t = [2,3,5]

print(zad(t))