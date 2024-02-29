def czyPierwsza(x):
    if x == 2 or x == 3:
        return True
    
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False

    i = 5

    while i <= int(x**0.5):
        if x % i == 0:
            return False

        i += 2

        if x % i == 0:
            return False
        
        i += 4

    return True

def komplementarne(t):
    n = len(t[0])

    for i in range(n):
        for j in range(n):
            komp = False
            for k in range(n):
                for m in range(n):
                    if (i != k or j != m) and t[i][j] != 0 and t[k][m] != 0:
                        if czyPierwsza(t[i][j] + t[k][m]):
                            komp = True
                            break
                
                if komp:
                    break
            
            if not komp:
                t[i][j] = 0
    
    return t
        
t1 = [[3,4],
      [2,2]]

print(*t1, sep = "\n")

t2 = komplementarne(t1)

print(*t2, sep = "\n")