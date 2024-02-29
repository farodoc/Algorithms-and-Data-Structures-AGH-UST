import random

def czySameNp(liczba):
    while liczba > 0:
        if (liczba % 10) % 2 == 0:
            return False
        
        liczba //= 10
    
    return True

while True:
    n = int(input("rozmiar tablicy:"))

    t = [0 for _ in range(n)]

    for i in range(n):
        t[i] = random.randint(1,1000)

    print(t)
    flag = True

    for i in range(n):
        if czySameNp(t[i]):
            print("tak: ", t[i])
            flag = False
            break

    if flag:
        print("nie")
