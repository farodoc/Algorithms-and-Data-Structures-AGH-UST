def czyKwadrat(t, x, y, k):
    n = len(t[0])
    skok = 2
    x2 = x + skok
    y2 = y + skok

    while x2 < n and y2 < n:
        if t[y][x] * t[y2][x] * t[y2][x2] * t[y][x2] == k:
            return (int((y + y2)/2) + 1, int((x + x2)/2) + 1)
        
        x2 += skok
        y2 += skok

    return False

def szukanieKwadratu(t, k):
    n = len(t[0])

    for i in range(n - 2):
        for j in range(n - 2):
            if czyKwadrat(t,j,i,k) != False:
                return czyKwadrat(t,j,i,k)

    return "Nie"

t = [[323,2,3,2],
     [12,5,4,1],
     [31,2,4,2],
     [32,22,33,44]]

print(szukanieKwadratu(t, 16))