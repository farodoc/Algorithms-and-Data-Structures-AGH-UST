while True:
    n = int(input("podaj liczbe: "))
    n2 = 0
    n3 = 0

    pal10 = False
    pal2 = False
    temp = n

    while temp > 0:
        n2 = n2 * 10 + temp % 10
        temp //= 10

    temp = n

    while temp > 0:
        n3 = n3 * 2 + temp % 2
        temp //= 2

    if n == n2:
        pal10 = True

    if n == n3:
        pal2 = True

    print("pal10:", pal10, ", pal2: ", pal2)
