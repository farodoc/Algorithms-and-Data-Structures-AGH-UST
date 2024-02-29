def spirala(T):
    n = len(T[0])
    c = 1
    a, b = 0, n - 1

    while a <= b:
        for i in range(a, b + 1):
            T[a][i] = c
            c += 1
        
        for i in range(a + 1, b):
            T[i][b] = c
            c += 1

        for i in range(b, a, - 1):
            T[b][i] = c
            c += 1

        for i in range(b, a, - 1):
            T[i][a] = c
            c += 1
        
        a += 1
        b -= 1

    print(*T, sep = "\n")



N = int(input("rozmiar tablicy: "))

T = [[0 for _ in range(N)] for _ in range(N)]

spirala(T)
