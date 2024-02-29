import math

while True:
    n = int(input("podaj zakres: ")) + 1

    t = [True for _ in range(n)]
    t[0] = False
    t[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if t[i]:
            for j in range(i*i, n, i):
                t[j] = False
        
    for i in range(n):
        if t[i]:
            print(i)