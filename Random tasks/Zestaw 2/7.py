while True:
    x = int(input("Podaj liczbe: "))
    a = 1  

    while True:
        if (a * a + a + 1) > x:
            print("nie")
            break

        if x % (a * a + a + 1) == 0:
            print("tak")
            break

        a += 1