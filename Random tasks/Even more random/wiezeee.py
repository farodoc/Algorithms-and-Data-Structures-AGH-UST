def f(t, w1, k1, w2, k2):
    n = len(t)
    sumWierszy = [0 for _ in range(n)]
    sumKolumn = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sumWierszy[i] += t[i][j]
            sumKolumn[i] += t[j][i]

    if w1 == w2:
        aktuSuma = sumWierszy[w1] + sumKolumn[k1] + sumKolumn[k2] - 2*t[w1][k1] - 2*t[w2][k2]
        
    elif k1 == k2:
        aktuSuma = sumWierszy[w1] + sumWierszy[w2] + sumKolumn[k1] - 2*t[w1][k1] - 2*t[w2][k2]

    else:
        aktuSuma = sumWierszy[w1] + sumWierszy[w2] + sumKolumn[k1] + sumKolumn[k2] - 2*t[w1][k1] - 2*t[w2][k2] - t[w1][k2] - t[w2][k1]


    for i in range(n):
        if i == w2:
            temp = sumWierszy[i] + sumKolumn[k1] + sumKolumn[k2] - 2*t[i][k1] - 2*t[w2][k2]
        
        elif k1 == k2:
            temp = sumWierszy[i] + sumWierszy[w2] + sumKolumn[k1] - 2*t[i][k1] - 2*t[w2][k2]

        else:
            temp = sumWierszy[i] + sumWierszy[w2] + sumKolumn[k1] + sumKolumn[k2] - 2*t[i][k1] - 2*t[w2][k2] - t[i][k2] - t[w2][k1]

        if temp > aktuSuma:
            return True

        if w1 == i:
            aktuSuma = sumWierszy[w1] + sumKolumn[k1] + sumKolumn[k2] - 2*t[w1][k1] - 2*t[i][k2]
            
        elif k1 == k2:
            aktuSuma = sumWierszy[w1] + sumWierszy[i] + sumKolumn[k1] - 2*t[w1][k1] - 2*t[i][k2]

        else:
            aktuSuma = sumWierszy[w1] + sumWierszy[i] + sumKolumn[k1] + sumKolumn[k2] - 2*t[w1][k1] - 2*t[i][k2] - t[w1][k2] - t[i][k1]

        if temp > aktuSuma:
            return True

    for j in range(n):
        if w1 == w2:
            aktuSuma = sumWierszy[w1] + sumKolumn[j] + sumKolumn[k2] - 2*t[w1][j] - 2*t[w2][k2]
            
        elif j == k2:
            aktuSuma = sumWierszy[w1] + sumWierszy[w2] + sumKolumn[j] - 2*t[w1][j] - 2*t[w2][k2]

        else:
            aktuSuma = sumWierszy[w1] + sumWierszy[w2] + sumKolumn[j] + sumKolumn[k2] - 2*t[w1][j] - 2*t[w2][k2] - t[w1][k2] - t[w2][j]

        if temp > aktuSuma:
            return True

        if w1 == w2:
            aktuSuma = sumWierszy[w1] + sumKolumn[k1] + sumKolumn[j] - 2*t[w1][k1] - 2*t[w2][j]
            
        elif k1 == j:
            aktuSuma = sumWierszy[w1] + sumWierszy[w2] + sumKolumn[k1] - 2*t[w1][k1] - 2*t[w2][j]

        else:
            aktuSuma = sumWierszy[w1] + sumWierszy[w2] + sumKolumn[k1] + sumKolumn[j] - 2*t[w1][k1] - 2*t[w2][j] - t[w1][j] - t[w2][k1]

        if temp > aktuSuma:
            return True
        
    return False

t =[[3,2,7],
    [1,3,2],
    [6,3,7]]

print(f(t, 0, 0, 1, 1))