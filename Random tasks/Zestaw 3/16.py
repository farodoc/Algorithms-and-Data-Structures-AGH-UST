import random

def isMinMax(t):
    t.sort()

    if t[0] != t[1] and t[len(t) - 1] != t[len(t) - 2]:
        return True
    
    return False

n = int(input("rozmiar tablicy: "))

t = [random.randint(0,10) for _ in range(n)]

print(t)
print(isMinMax(t))