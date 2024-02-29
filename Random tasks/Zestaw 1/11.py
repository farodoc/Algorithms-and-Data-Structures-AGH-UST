from socket import IPV6_JOIN_GROUP


def sumaDzielnikow(liczba):
    suma = 0

    for i in range(1, liczba):
        if liczba % i == 0:
            suma += i

    return suma

for i in range(1000000):
    suma = sumaDzielnikow(i)

    for j in range(i + 1, 2 * i):
        if (suma == j) and (i == sumaDzielnikow(j)):
            print(i, "  ", j)
            break