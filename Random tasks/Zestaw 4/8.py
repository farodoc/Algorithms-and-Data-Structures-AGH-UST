def dlugoscCiagu(T, x, y):
    n = len(T[0])

    if x + 1 < n and y + 1 < n:
        q = T[x + 1][y + 1]/T[x][y]
        res = 2
    else:
        return 1

    x += 1
    y += 1

    while x + 1 < n and y + 1 < n:
        if T[x + 1][y + 1]/T[x][y] == q:
            x += 1
            y += 1
            res += 1
        
        else:
            break

    return res

def ciagGeo(T):
    n = len(T[0])
    res = 0

    for i in range(n):
        for j in range(n):
            res = max(res, dlugoscCiagu(T,j,i))

    if res >= 3:
        return res
    
    else:
        return "Nie ma"

T = [[1,2,3,4],
     [1,3,4,5],
     [1,2,9,8],
     [1,2,3,27]]

print(ciagGeo(T))