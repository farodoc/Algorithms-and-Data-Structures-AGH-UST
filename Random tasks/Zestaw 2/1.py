while True:
    x = int(input("Podaj liczbe: "))

    a = 1
    b = 1
    flag = True

    while a <= x:
        dzielnik = x / a
        c, d = b, a + b
        while c <= x:
            if c == dzielnik:
                print("tak: ", a, " ", c)
                flag = False
                break

            c, d = d, c + d

        if flag == 0:
            break

        a, b = b, a + b

    if flag:
        print("nie")



