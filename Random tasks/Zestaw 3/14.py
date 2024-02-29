import random

def prawdopodobienstwo(t):
    t.sort()
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return 1
    
    return 0


n = int(input("liczba ludzi: "))
suma = 0

for i in range(10000):
    t = [random.randint(1,365) for _ in range(n)]
    suma += prawdopodobienstwo(t)

print(suma/10000)