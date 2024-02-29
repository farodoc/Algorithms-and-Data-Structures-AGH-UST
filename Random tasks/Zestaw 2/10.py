while True:
    x = int(input("x = "))
    a = 2

    while True:
        if a > x:
            print("nie")
            break

        if x % a == 0:
            print("tak")
            break

        a = 3 * a + 1
