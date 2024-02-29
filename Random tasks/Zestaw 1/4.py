while True:
    liczba = int(input("podaj liczbe: "))

    a = 1
    suma = 0
    licznik = 0

    while suma < liczba:
        suma += a
        a += 2
        if suma > liczba:
            break
        licznik += 1

    print("pierwiastek calkowity z liczby ", liczba, " to: ", licznik)