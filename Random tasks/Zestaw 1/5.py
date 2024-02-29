while True:
    liczba = int(input("Podaj liczbe: "))

    a = liczba / 2
    b = liczba / a
    eps = 0.00001

    for i in range(1000):
        if abs((a ** 2) - liczba) < eps:
            print("pierwiastek drugiego stopnia z liczby ", liczba, " wynosi: ", a)
            break

        a = (a + b) / 2
        b = liczba / a