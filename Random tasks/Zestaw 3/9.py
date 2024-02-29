while True:
    n = int(input("rozmiar tablicy: "))

    t = [0 for _ in range(n)]

    for i in range(n):
        t[i] = int(input())

    maxDl = 1
    i = 0

    while i < n - 1:
        if t[i] < t[i + 1]:
            start = i
            koniec = i + 1
            tempDl = 1
            while koniec < n and t[koniec] > t[koniec - 1]:
                koniec += 1
                tempDl += 1
            
            if tempDl > maxDl:
                maxDl = tempDl
            
        i += 1

    print(maxDl)