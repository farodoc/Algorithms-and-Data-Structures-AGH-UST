while True:
    x = int(input("x = "))

    dzielnik = 0

    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            dzielnik = i

    print(dzielnik, " * ", int(x / dzielnik), " = ", x)