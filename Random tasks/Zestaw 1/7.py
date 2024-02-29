while True:
    liczba = int(input("podaj liczbe: "))

    a,b = 1,1

    while True:
        if a * b == liczba:
            print("Tak")
            break

        if a * b > liczba:
            print("Nie")
            break

        c = a + b
        a = b 
        b = c