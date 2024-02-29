def zastapNajmniejszy(t, liczba):
    indeksMin = 0
    for i in range(1,10):
        if t[i] < t[indeksMin]:
            indeksMin = i
    
    if liczba > t[indeksMin]:
        t[indeksMin] = liczba
    
    return

def znajdzNajmniejszy(t):
    t.sort()
    i = 0
    while t[i] == 0 and i < 9:
        i += 1

    print("10 co do wielkosci element to: ", t[i])

t = [0 for _ in range(10)]

while True:
    x = int(input())
    if x == 0:
        znajdzNajmniejszy(t)
        print(t)
        break

    zastapNajmniejszy(t, x)